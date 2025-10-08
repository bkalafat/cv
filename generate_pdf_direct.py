"""
Direct PDF CV Generator - NO LATEX, NO WEBSITES NEEDED!
Uses ReportLab to create professional PDF directly from Python
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import yaml
import os
from datetime import datetime

def load_yaml_data():
    """Load all YAML data files"""
    with open('_data/data.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    with open('_data/experience.yml', 'r', encoding='utf-8') as f:
        experiences = yaml.safe_load(f)
    with open('_data/education.yml', 'r', encoding='utf-8') as f:
        education = yaml.safe_load(f)
    
    return data, experiences, education

def create_header_with_photo(canvas_obj, doc, data):
    """Create header with photo"""
    # Colors
    primary_color = HexColor('#0E4C92')
    accent_color = HexColor('#1A73E8')
    
    # Photo
    try:
        photo_path = 'assets/images/profile.png'
        if os.path.exists(photo_path):
            canvas_obj.drawImage(photo_path, 
                               30*mm, doc.height - 30*mm, 
                               width=25*mm, height=25*mm, 
                               preserveAspectRatio=True, 
                               mask='auto')
    except:
        pass
    
    # Name and title
    canvas_obj.setFont('Helvetica-Bold', 24)
    canvas_obj.setFillColor(primary_color)
    canvas_obj.drawString(60*mm, doc.height - 15*mm, data['sidebar']['name'])
    
    canvas_obj.setFont('Helvetica', 14)
    canvas_obj.setFillColor(accent_color)
    canvas_obj.drawString(60*mm, doc.height - 22*mm, data['sidebar']['tagline'])
    
    # Contact info
    canvas_obj.setFont('Helvetica', 9)
    canvas_obj.setFillColor(colors.grey)
    y_pos = doc.height - 28*mm
    
    contact_info = [
        f"📧 {data['sidebar']['email']}",
        f"📱 {data['sidebar']['phone']}",
        f"💼 linkedin.com/in/{data['sidebar']['linkedin']}",
        f"💻 github.com/{data['sidebar']['github']}",
    ]
    
    for info in contact_info:
        canvas_obj.drawString(60*mm, y_pos, info)
        y_pos -= 4*mm
    
    # Line separator
    canvas_obj.setStrokeColor(primary_color)
    canvas_obj.setLineWidth(2)
    canvas_obj.line(30*mm, doc.height - 48*mm, doc.width + 30*mm, doc.height - 48*mm)

def generate_professional_pdf():
    """Generate a beautiful PDF CV directly"""
    
    print("🚀 Loading data...")
    data, experiences, education = load_yaml_data()
    
    print("📄 Creating PDF...")
    
    # Create PDF
    filename = f"Burak_Kalafat_CV_{datetime.now().strftime('%Y%m%d')}.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=30*mm,
        leftMargin=30*mm,
        topMargin=55*mm,
        bottomMargin=20*mm
    )
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=HexColor('#0E4C92'),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#0E4C92'),
        spaceAfter=8,
        spaceBefore=16,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=HexColor('#1A73E8'),
        borderPadding=5,
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#2C2C2C'),
        fontName='Helvetica-Bold',
        spaceAfter=4
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1A73E8'),
        fontName='Helvetica-Bold',
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#333333'),
        spaceAfter=6,
        leftIndent=15,
        bulletIndent=10,
        fontName='Helvetica'
    )
    
    # Build content
    content = []
    
    # Summary
    content.append(Paragraph("PROFESSIONAL SUMMARY", heading_style))
    summary = data['career-profile']['summary'].replace('\n', '<br/>')
    content.append(Paragraph(summary, body_style))
    content.append(Spacer(1, 0.5*cm))
    
    # Experience
    content.append(Paragraph("PROFESSIONAL EXPERIENCE", heading_style))
    
    for exp in experiences:
        # Job title and company
        job_info = f"<b>{exp['job_title']}</b> | {exp['company']}"
        content.append(Paragraph(job_info, job_title_style))
        
        # Dates and location
        date_loc = f"{exp['dates']} | {exp['location']}"
        content.append(Paragraph(date_loc, ParagraphStyle('DateLoc', parent=body_style, fontSize=9, textColor=colors.grey)))
        
        # Description
        desc_lines = exp.get('description', '').strip().split('\n')
        for line in desc_lines:
            line = line.strip()
            if line.startswith('- '):
                content.append(Paragraph(f"• {line[2:]}", body_style))
            elif line and not line.startswith('Technologies:'):
                content.append(Paragraph(line, body_style))
        
        # Technologies
        tech_line = [l for l in desc_lines if l.startswith('Technologies:')]
        if tech_line:
            tech_style = ParagraphStyle('Tech', parent=body_style, textColor=HexColor('#34A853'), fontSize=9, fontName='Helvetica-Oblique')
            content.append(Paragraph(tech_line[0], tech_style))
        
        content.append(Spacer(1, 0.4*cm))
    
    # Education
    content.append(Paragraph("EDUCATION", heading_style))
    for edu in education:
        edu_text = f"<b>{edu['qualification']}</b><br/>{edu['name']}, {edu['location']}<br/>{edu['dates']}"
        content.append(Paragraph(edu_text, body_style))
        content.append(Spacer(1, 0.3*cm))
    
    # Skills
    content.append(Paragraph("TECHNICAL SKILLS", heading_style))
    skills_text = []
    
    skill_categories = {
        'Core': ['C#', '.NET Core', 'Java', 'Microservices'],
        'AI & Modern': ['GitHub Copilot Enterprise', 'Prompt Engineering', 'SDD'],
        'Architecture': ['Clean Architecture', 'Design Patterns', 'REST APIs'],
        'Databases': ['MSSQL', 'Oracle', 'EF Core'],
        'DevOps': ['Azure DevOps', 'GitHub Actions', 'CI/CD']
    }
    
    for category, skills in skill_categories.items():
        skills_line = f"<b>{category}:</b> {', '.join(skills)}"
        content.append(Paragraph(skills_line, body_style))
    
    content.append(Spacer(1, 0.3*cm))
    
    # Certifications
    content.append(Paragraph("CERTIFICATIONS", heading_style))
    for cert in data.get('certifications', {}).get('list', []):
        cert_text = f"• <b>{cert['name']}</b> - {cert['organization']} ({cert['start']})"
        content.append(Paragraph(cert_text, body_style))
    
    # Build PDF with custom header
    def add_header(canvas_obj, doc):
        canvas_obj.saveState()
        create_header_with_photo(canvas_obj, doc, data)
        canvas_obj.restoreState()
    
    doc.build(content, onFirstPage=add_header, onLaterPages=add_header)
    
    print(f"✅ PDF created successfully: {filename}")
    print(f"📂 Location: {os.path.abspath(filename)}")
    print(f"\n🎉 DONE! Open the PDF to see your beautiful CV!")
    
    return filename

if __name__ == "__main__":
    try:
        generate_professional_pdf()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n📦 Installing ReportLab library...")
        import subprocess
        subprocess.run(['python', '-m', 'pip', 'install', 'reportlab', 'pillow'])
        print("\n🔄 Trying again...")
        generate_professional_pdf()
