"""Validate source YAML, generated text, hyperlinks, and PDF page boundaries."""

import argparse
import os
from html.parser import HTMLParser
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from pypdf import PdfReader
import pymupdf

from cv_data import PDF_NAMES, PROJECT_ROOT, load_cv, profile_links, read_yaml


def normalized(value):
    return " ".join(str(value).split())


def expected_content(data):
    profile = data["sidebar"]
    for key in ("name", "tagline", "email", "phone", "location", "timezone"):
        yield profile[key]
    yield from (label for label, _ in profile_links(data))
    yield data["career-profile"]["summary"]
    for key in ("career-profile", "skills", "experiences", "education", "certifications"):
        yield data[key]["title"]
    for category in data["skills"]["categories"]:
        yield category["name"]
        yield from category["items"]
    for job in data["experiences"]["info"]:
        for key in ("role", "company", "time", "location"):
            yield job[key]
        yield from job["bullets"]
        if job.get("previous_role"):
            yield job["previous_role"]
            yield job["previous_time"]
    for degree in data["education"]["info"]:
        yield from (degree[key] for key in ("degree", "university", "location", "time"))
    for credential in data["certifications"]["list"]:
        for key in ("name", "organization", "kind", "start", "expires", "credentialname"):
            if credential.get(key):
                yield credential[key]
    for key, fields in (("languages", ("idiom", "level")), ("interests", ("item",))):
        yield profile[key]["title"]
        for item in profile[key]["info"]:
            yield from (item[field] for field in fields)


def check_content(text, data, label):
    text = normalized(text)
    missing = [item for item in expected_content(data) if normalized(item).casefold() not in text.casefold()]
    if missing:
        raise ValueError(f"{label}: missing content: {missing}")
    for stale in ("DiffPilot", "6-8", "5-6", "hallucination-free", "zero scope drift", "GDPR compliant", "February 2017"):
        if stale in text:
            raise ValueError(f"{label}: removed or stale content remains: {stale}")
    if "\ufffd" in text or "\x00" in text:
        raise ValueError(f"{label}: broken Unicode text")


def check_url(url):
    parts = urlsplit(url)
    if any(character.isspace() for character in url) or url.startswith("//"):
        raise ValueError(f"Malformed URL: {url}")
    if parts.scheme and parts.scheme not in ("https", "http", "mailto", "tel"):
        raise ValueError(f"Unsupported link scheme: {url}")
    if parts.scheme in ("https", "http") and (not parts.netloc or parts.netloc.endswith(":")):
        raise ValueError(f"Malformed HTTP URL: {url}")


def validate_sources():
    ignored = {".git", ".venv", "vendor", "tmp", "temp", "output", "_site", "node_modules"}
    paths = []
    for directory, children, filenames in os.walk(PROJECT_ROOT):
        children[:] = [name for name in children if name not in ignored]
        paths.extend(Path(directory) / name for name in filenames if Path(name).suffix in (".yml", ".yaml"))
    for path in paths:
        read_yaml(path)
    data = load_cv()
    for _, url in profile_links(data):
        check_url(url)
    for item in data["certifications"]["list"]:
        if item.get("credentialurl"):
            check_url(item["credentialurl"])
    config = read_yaml(PROJECT_ROOT / "_config.yml")
    if config["url"].rstrip("/") != data["sidebar"]["website"].rstrip("/"):
        raise ValueError("Website URL differs between CV and Jekyll configuration")
    if urlsplit(config["url"]).netloc != (PROJECT_ROOT / "CNAME").read_text().strip():
        raise ValueError("CNAME differs from Jekyll URL")
    if re.search(r"DiffPilot|6-8|5-6|hallucination-free|zero scope drift", (PROJECT_ROOT / "_data/data.yml").read_text(encoding="utf-8")):
        raise ValueError("Removed content remains in the canonical source")
    print(f"PASS: {len(paths)} YAML files; canonical CV, contact URLs, and domain consistency")
    return data


def validate_pdf(path, data, max_pages=2):
    reader = PdfReader(path)
    if not 1 <= len(reader.pages) <= max_pages:
        raise ValueError(f"{path.name}: expected at most {max_pages} pages, got {len(reader.pages)}")
    texts = []
    for index, page in enumerate(reader.pages):
        lines = (page.extract_text() or "").splitlines()
        # Running headers/footers may occur inside a paragraph split across pages.
        texts.append(" ".join(line for line in lines
                              if not re.fullmatch(r"Page \d+", line.strip())
                              and not (index > 0 and line.strip() == data["sidebar"]["name"])))
    if any(not text.strip() for text in texts):
        raise ValueError(f"{path.name}: blank page")
    check_content(" ".join(texts), data, path.name)
    positions = [normalized(" ".join(texts)).find(f'{job["role"]} | {job["company"]}')
                 for job in data["experiences"]["info"]]
    if -1 in positions or positions != sorted(positions):
        raise ValueError(f"{path.name}: experience extraction order is incorrect")
    with pymupdf.open(path) as document:
        for page in document:
            for word in page.get_text("words"):
                if not page.rect.contains(pymupdf.Rect(word[:4])):
                    raise ValueError(f"{path.name}: text outside page {page.number + 1}: {word[4]}")
                if word[1] < 8 or word[3] > page.rect.height - 8:
                    raise ValueError(f"{path.name}: text too close to page edge: {word[4]}")
    links = []
    for page in reader.pages:
        for annotation in page.get("/Annots", []):
            url = annotation.get_object().get("/A", {}).get("/URI")
            if url:
                check_url(url)
                links.append(url)
    required_links = [url for _, url in profile_links(data)]
    required_links += [c["credentialurl"] for c in data["certifications"]["list"] if c.get("credentialurl")]
    if set(required_links) - set(links):
        raise ValueError(f"{path.name}: missing clickable links")
    print(f"PASS: {path.name}: {len(reader.pages)} pages, complete selectable Unicode text, chronology, bounds, links")


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.links = []
        self.ids = []
        self.h1_count = 0
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.hidden += 1
        if tag == "h1":
            self.h1_count += 1
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.hidden -= 1

    def handle_data(self, text):
        if not self.hidden:
            self.text.append(text)


def validate_site(site_dir, data, baseurl=""):
    parser = SiteParser()
    html = (site_dir / "index.html").read_text(encoding="utf-8")
    parser.feed(html)
    check_content(" ".join(parser.text), data, "Jekyll HTML")
    if parser.h1_count != 1 or len(parser.ids) != len(set(parser.ids)):
        raise ValueError("Expected one h1 and unique element IDs")
    for url in parser.links:
        check_url(url)
        parts = urlsplit(url)
        if not parts.scheme and not parts.netloc:
            path = unquote(parts.path)
            if baseurl and path.startswith("/") and not path.startswith(baseurl + "/"):
                raise ValueError(f"Local link omits configured base URL {baseurl}: {url}")
            if baseurl and path.startswith(baseurl + "/"):
                path = path[len(baseurl):]
            target = site_dir / path.lstrip("/") if path else site_dir / "index.html"
            if not target.exists():
                raise ValueError(f"Missing local website target: {url}")
            if not parts.path and parts.fragment and parts.fragment not in parser.ids:
                raise ValueError(f"Broken fragment: {url}")
    for marker in ('rel="canonical"', 'property="og:title"', 'name="description"', 'name="twitter:card"'):
        if marker not in html:
            raise ValueError(f"Missing SEO markup: {marker}")
    for name in PDF_NAMES.values():
        if (site_dir / "downloads" / name).read_bytes() != (PROJECT_ROOT / "downloads" / name).read_bytes():
            raise ValueError(f"Deployed PDF differs from generated PDF: {name}")
    text_name = "Burak_Kalafat_ATS_CV.txt"
    plain_text = (PROJECT_ROOT / "downloads" / text_name).read_text(encoding="utf-8")
    check_content(plain_text, data, "ATS plain text")
    if (site_dir / "downloads" / text_name).read_bytes() != (PROJECT_ROOT / "downloads" / text_name).read_bytes():
        raise ValueError("Deployed ATS text differs from generated text")
    for excluded in ("docs", "scripts", "tests", "requirements.txt", "Gemfile", "AGENTS.md", "VALIDATION.md", ".codex", ".agents"):
        if (site_dir / excluded).exists():
            raise ValueError(f"Private build/archive content was published: {excluded}")
    print("PASS: Jekyll content parity, local links, downloads, headings, SEO, and publication exclusions")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--outputs", action="store_true")
    parser.add_argument("--site-dir", type=Path, default=PROJECT_ROOT / "_site")
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    data = validate_sources()
    if args.outputs:
        for name in PDF_NAMES.values():
            validate_pdf(PROJECT_ROOT / "downloads" / name, data)
        validate_site(args.site_dir, data, args.baseurl)


if __name__ == "__main__":
    main()
