"""PDF entry point and plain ATS renderer; professional design is independent.

All CV content is read from _data/data.yml. Platypus measures and paginates
flowables; no section, bullet, contact field, or credential is truncated.
"""

from html import escape
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

from cv_data import PDF_NAMES, PROJECT_ROOT, load_cv, profile_links


def register_fonts():
    font_dir = PROJECT_ROOT / "assets" / "fonts"
    for name, filename in (("CV", "DejaVuSans.ttf"), ("CV-Bold", "DejaVuSans-Bold.ttf")):
        path = font_dir / filename
        if not path.is_file():
            raise FileNotFoundError(f"Required Unicode font missing: {path}")
        pdfmetrics.registerFont(TTFont(name, str(path)))
    pdfmetrics.registerFontFamily("CV", normal="CV", bold="CV-Bold", italic="CV", boldItalic="CV-Bold")


def link(label, url):
    return f'<a href="{escape(url, quote=True)}">{escape(str(label))}</a>'


def make_styles(variant):
    ink = colors.HexColor("#172D42") if variant == "professional" else colors.black
    muted = colors.HexColor("#465669") if variant == "professional" else colors.HexColor("#333333")
    base = dict(fontName="CV", fontSize=9.4, leading=13, textColor=ink)
    body = ParagraphStyle("Body", **base, spaceAfter=4)
    return {
        "body": body,
        "name": ParagraphStyle("Name", parent=body, fontName="CV-Bold", fontSize=23, leading=29, spaceAfter=3),
        "headline": ParagraphStyle("Headline", parent=body, fontSize=11, leading=15, spaceAfter=7),
        "contact": ParagraphStyle("Contact", parent=body, fontSize=8.4, leading=12, spaceAfter=2),
        "section": ParagraphStyle("Section", parent=body, fontName="CV-Bold", fontSize=11,
                                  leading=15, spaceBefore=11, spaceAfter=6, keepWithNext=True),
        "job": ParagraphStyle("Job", parent=body, fontName="CV-Bold", fontSize=10,
                              leading=14, spaceBefore=3, spaceAfter=2, keepWithNext=True),
        "meta": ParagraphStyle("Meta", parent=body, fontSize=8.5, leading=12,
                               textColor=muted, spaceAfter=4, keepWithNext=True),
        "bullet": ParagraphStyle("Bullet", parent=body, leftIndent=10, firstLineIndent=-8, spaceAfter=3),
        "small": ParagraphStyle("Small", parent=body, fontSize=8.3, leading=11.5, textColor=muted, spaceAfter=4),
        "skill": ParagraphStyle("Skill", parent=body, fontSize=8.7, leading=12, spaceAfter=3),
    }


def build_story(data, styles, variant):
    story = []
    profile = data["sidebar"]

    def paragraph(text, style="body"):
        return Paragraph(escape(str(text)), styles[style])

    def section(key):
        heading = data[key]["title"]
        story.append(paragraph(heading.upper() if variant == "ats" else heading, "section"))

    story.extend([paragraph(profile["name"], "name"), paragraph(profile["tagline"], "headline")])
    links = profile_links(data)
    story.append(Paragraph(" | ".join(link(*item) for item in links[:2]), styles["contact"]))
    story.append(Paragraph(" | ".join(link(*item) for item in links[2:]), styles["contact"]))
    story.append(paragraph(f'{profile["location"]} | {profile["timezone"]}', "contact"))

    section("career-profile")
    story.append(paragraph(data["career-profile"]["summary"]))
    section("skills")
    for category in data["skills"]["categories"]:
        story.append(Paragraph(f'<b>{escape(category["name"])}:</b> {escape(", ".join(category["items"]))}', styles["skill"]))

    section("experiences")
    for job in data["experiences"]["info"]:
        block = [
            paragraph(f'{job["role"]} | {job["company"]}', "job"),
            paragraph(f'{job["time"]} | {job["location"]}', "meta"),
        ]
        block.extend(paragraph(f"- {bullet}", "bullet") for bullet in job["bullets"])
        block.append(Spacer(1, 3))
        # Keep ordinary roles together; ReportLab can split an over-page block safely.
        story.append(KeepTogether(block))

    section("education")
    for degree in data["education"]["info"]:
        story.append(KeepTogether([
            paragraph(degree["degree"], "job"),
            paragraph(f'{degree["university"]}, {degree["location"]} | {degree["time"]}', "body"),
        ]))

    section("certifications")
    for credential in data["certifications"]["list"]:
        label = f'<b>{escape(credential["name"])}</b>'
        if credential.get("credentialurl"):
            label = "<b>" + link(credential["name"], credential["credentialurl"]) + "</b>"
        metadata = [credential["organization"], credential["kind"]]
        if credential.get("start"):
            metadata.append(str(credential["start"]))
        if credential.get("expires"):
            metadata.append("Expires " + credential["expires"])
        if credential.get("credentialname"):
            metadata.append(credential["credentialname"])
        story.append(Paragraph(label + "<br/>" + escape(" | ".join(metadata)), styles["small"]))

    for key, text in (
        ("languages", "; ".join(f'{item["idiom"]}: {item["level"]}' for item in profile["languages"]["info"])),
        ("interests", "; ".join(item["item"] for item in profile["interests"]["info"])),
    ):
        heading = profile[key]["title"]
        story.append(paragraph(heading.upper() if variant == "ats" else heading, "section"))
        story.append(paragraph(text, "small"))
    return story


def generate_cv(variant="professional", *, data=None, output_path=None):
    if variant not in PDF_NAMES:
        raise ValueError(f"Unknown CV variant: {variant}")
    data = data if data is not None else load_cv()
    register_fonts()
    filename = Path(output_path or PROJECT_ROOT / "downloads" / PDF_NAMES[variant])
    filename.parent.mkdir(parents=True, exist_ok=True)
    if variant == "professional":
        from cv_professional import generate_professional
        generate_professional(data, filename)
        print(f"Generated {variant} CV: {filename}")
        return filename
    doc = SimpleDocTemplate(
        str(filename), pagesize=A4, rightMargin=17 * mm, leftMargin=17 * mm,
        topMargin=16 * mm, bottomMargin=16 * mm, pageCompression=1,
        title=f'{data["sidebar"]["name"]} - {data["sidebar"]["tagline"]}',
        author=data["sidebar"]["name"], subject=data["career-profile"]["summary"],
    )

    def page_furniture(canvas, document):
        if variant == "ats":
            return
        canvas.saveState()
        width, height = A4
        if variant == "professional":
            canvas.setFillColor(colors.HexColor("#172D42"))
            canvas.rect(0, height - 4 * mm, width, 4 * mm, fill=1, stroke=0)
            canvas.setStrokeColor(colors.HexColor("#CAD6E0"))
            canvas.line(17 * mm, 12 * mm, width - 17 * mm, 12 * mm)
        canvas.setFillColor(colors.HexColor("#465669"))
        canvas.setFont("CV", 7.5)
        if document.page > 1:
            canvas.drawString(17 * mm, height - 10 * mm, data["sidebar"]["name"])
        canvas.drawRightString(width - 17 * mm, 8 * mm, f"Page {document.page}")
        canvas.restoreState()

    doc.build(build_story(data, make_styles(variant), variant), onFirstPage=page_furniture, onLaterPages=page_furniture)
    print(f"Generated {variant} CV: {filename}")
    return filename
