"""Editorial recruiter PDF; source content and ATS rendering stay independent."""

from html import escape

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from cv_data import profile_links

NAVY = colors.HexColor("#132D40")
TEAL = colors.HexColor("#16756E")
MUTED = colors.HexColor("#536572")
PALE = colors.HexColor("#EFF5F5")


def generate_professional(data, filename):
    from cv_pdf import link

    body = ParagraphStyle("EditorialBody", fontName="CV", fontSize=10, leading=13.5, textColor=NAVY, spaceAfter=4)
    styles = {
        "body": body,
        "name": ParagraphStyle("EditorialName", parent=body, fontName="CV-Bold", fontSize=30, leading=36, textColor=colors.white, spaceAfter=5),
        "headline": ParagraphStyle("EditorialHeadline", parent=body, fontSize=11, leading=16, textColor=colors.HexColor("#BCE1DC"), spaceAfter=9),
        "contact": ParagraphStyle("EditorialContact", parent=body, fontSize=8.2, leading=12, textColor=colors.white, spaceAfter=2),
        "section": ParagraphStyle("EditorialSection", parent=body, fontName="CV-Bold", fontSize=11, leading=15, textColor=TEAL, spaceBefore=9, spaceAfter=4, keepWithNext=True),
        "job": ParagraphStyle("EditorialJob", parent=body, fontName="CV-Bold", fontSize=10.1, leading=14, spaceAfter=3, keepWithNext=True),
        "meta": ParagraphStyle("EditorialMeta", parent=body, fontSize=8.5, leading=12, textColor=MUTED, spaceAfter=4, keepWithNext=True),
        "bullet": ParagraphStyle("EditorialBullet", parent=body, leftIndent=10, firstLineIndent=-10, spaceAfter=3),
        "small": ParagraphStyle("EditorialSmall", parent=body, fontSize=8.5, leading=12, spaceAfter=4),
        "skill": ParagraphStyle("EditorialSkill", parent=body, fontSize=8.7, leading=11.6, spaceAfter=5),
    }
    def p(text, style="body"):
        return Paragraph(escape(str(text)), styles[style])

    width = A4[0] - 34 * mm
    profile = data["sidebar"]
    links = profile_links(data)
    hero = [p(profile["name"], "name"), p(profile["tagline"], "headline")]
    hero += [Paragraph("  |  ".join(link(*item) for item in row), styles["contact"]) for row in (links[:2], links[2:])]
    hero.append(p(f'{profile["location"]} | {profile["timezone"]}', "contact"))
    masthead = Table([[hero]], colWidths=[width])
    masthead.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("BOX", (0, 0), (-1, -1), 0, NAVY),
        ("LINEBELOW", (0, 0), (-1, -1), 3, TEAL),
        ("LEFTPADDING", (0, 0), (-1, -1), 17), ("RIGHTPADDING", (0, 0), (-1, -1), 17),
        ("TOPPADDING", (0, 0), (-1, -1), 12), ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
    ]))
    story = [masthead, p(data["career-profile"]["title"], "section"), p(data["career-profile"]["summary"]), p(data["experiences"]["title"], "section")]
    for index, job in enumerate(data["experiences"]["info"]):
        if index == 3:
            story += [PageBreak(), p("Professional Experience · Continued", "section")]
        block = [p(f'{job["role"]} | {job["company"]}', "job"), p(f'{job["time"]} | {job["location"]}', "meta")]
        if job.get("previous_role"):
            block.append(p(f'Previously: {job["previous_role"]} | {job["previous_time"]}', "meta"))
        block += [p(f"• {bullet}", "bullet") for bullet in job["bullets"]]
        block.append(Spacer(1, 4))
        story.append(KeepTogether(block))

    story.append(p(data["skills"]["title"], "section"))
    categories = data["skills"]["categories"]
    cells = []
    for category in categories:
        cells.append(Paragraph(f'<b>{escape(category["name"])}</b><br/>{escape(", ".join(category["items"]))}', styles["skill"]))
    rows = [cells[i:i + 2] + ([""] if len(cells[i:i + 2]) == 1 else []) for i in range(0, len(cells), 2)]
    grid = Table(rows, colWidths=[width / 2] * 2, hAlign="LEFT")
    grid.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 11), ("RIGHTPADDING", (0, 0), (-1, -1), 11),
        ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    story.append(grid)
    story.append(p(data["education"]["title"], "section"))
    for degree in data["education"]["info"]:
        story.append(Paragraph(f'<b>{escape(degree["degree"])}</b> · {escape(degree["university"])}<br/>{escape(degree["location"])} | {escape(degree["time"])}', styles["small"]))
    story.append(p(data["certifications"]["title"], "section"))
    for credential in data["certifications"]["list"]:
        label = link(credential["name"], credential["credentialurl"]) if credential.get("credentialurl") else escape(credential["name"])
        meta = [credential["organization"], credential["kind"]]
        if credential.get("start"):
            meta.append(str(credential["start"]))
        if credential.get("expires"):
            meta.append("Expires " + credential["expires"])
        if credential.get("credentialname"):
            meta.append(credential["credentialname"])
        separator = "<br/>" if credential.get("credentialurl") else " · "
        story.append(Paragraph(f'<b>{label}</b>{separator}{escape(" | ".join(meta))}', styles["small"]))
    for key, value in (
        ("languages", "; ".join(f'{item["idiom"]}: {item["level"]}' for item in profile["languages"]["info"])),
        ("interests", "; ".join(item["item"] for item in profile["interests"]["info"])),
    ):
        story.append(Paragraph(f'<b>{escape(profile[key]["title"])}</b> · {escape(value)}', styles["small"]))

    def furniture(canvas, doc):
        canvas.saveState()
        w, h = A4
        canvas.setFillColor(TEAL)
        canvas.rect(17 * mm, h - 10 * mm, 15 * mm, 2, fill=1, stroke=0)
        if doc.page > 1:
            canvas.setFont("CV-Bold", 9)
            canvas.setFillColor(NAVY)
            canvas.drawString(36 * mm, h - 10 * mm, profile["name"])
        canvas.setStrokeColor(colors.HexColor("#C8D7DA"))
        canvas.line(17 * mm, 13 * mm, w - 17 * mm, 13 * mm)
        canvas.setFont("CV", 8)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(w - 17 * mm, 8 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(str(filename), pagesize=A4, leftMargin=17 * mm, rightMargin=17 * mm,
                            topMargin=16 * mm, bottomMargin=18 * mm, title=f'{profile["name"]} - {profile["tagline"]}',
                            author=profile["name"], subject=data["career-profile"]["summary"], pageCompression=1)
    doc.build(story, onFirstPage=furniture, onLaterPages=furniture)
    return filename
