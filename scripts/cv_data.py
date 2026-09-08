"""The shared CV content contract. Paths are independent of the working directory."""

from pathlib import Path

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "_data" / "data.yml"
PDF_NAMES = {
    "professional": "Burak_Kalafat_Professional_CV.pdf",
    "ats": "Burak_Kalafat_ATS_CV.pdf",
}


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject accidental duplicate keys instead of silently losing CV content."""


def _mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"Duplicate YAML key: {key!r}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _mapping)


def read_yaml(path):
    return yaml.load(Path(path).read_text(encoding="utf-8"), Loader=UniqueKeyLoader)


def load_cv():
    data = read_yaml(DATA_PATH)
    for section in ("sidebar", "career-profile", "skills", "experiences", "education", "certifications"):
        if not isinstance(data.get(section), dict):
            raise ValueError(f"Missing or invalid CV section: {section}")
    phone = data["sidebar"]["phone"]
    if not isinstance(phone, str) or not phone.startswith("+"):
        raise ValueError("Quote the phone number in YAML and include the country-code +.")
    return data


def profile_links(data):
    profile = data["sidebar"]
    return [
        (profile["email"], f'mailto:{profile["email"]}'),
        (profile["phone"], f'tel:{profile["phone"]}'),
        (f'https://www.linkedin.com/in/{profile["linkedin"]}/', f'https://www.linkedin.com/in/{profile["linkedin"]}/'),
        (f'https://github.com/{profile["github"]}', f'https://github.com/{profile["github"]}'),
        (profile["website"], profile["website"]),
    ]
