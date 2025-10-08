"""
ATS-Friendly CV Generator - Simple single-column layout
Optimized for Applicant Tracking Systems (ATS) parsing
No sidebars, no colors, plain text formatting
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import yaml
import re

def load_yaml_data():
    """Load all YAML data files"""
    with open('_data/data.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    with open('_data/experience.yml', 'r', encoding='utf-8') as f:
        experiences = yaml.safe_load(f)
    with open('_data/education.yml', 'r', encoding='utf-8') as f:
        education = yaml.safe_load(f)
    
    return data, experiences, education

def generate_ats_cv():
    """Generate ATS-friendly CV with simple single-column layout"""
    
    print("🚀 Loading data...")
    data, experiences, education = load_yaml_data()
    
    print("📄 Creating ATS-friendly PDF (single-column, plain text)...")
    
    filename = "Burak_Kalafat_ATS_CV.pdf"
    
    # Register font for Turkish characters
    try:
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
    except:
        pass  # Use default if fonts not available
    
    # Create PDF canvas
    pdf_canvas = canvas.Canvas(filename, pagesize=A4)
    page_width, page_height = A4
    
    # Simple margins for ATS parsing
    margin_x = 20*mm
    content_width = page_width - 2*margin_x
    y_position = page_height - 25*mm
    
    # ATS-friendly colors (mostly black on white)
    text_color = colors.black
    heading_color = colors.HexColor('#333333')
    
    # Header: Name and contact info
    pdf_canvas.setFont('Arial-Bold', 16)
    pdf_canvas.setFillColor(heading_color)
    name = data['sidebar']['name'].upper()
    pdf_canvas.drawString(margin_x, y_position, name)
    
    y_position -= 8*mm
    
    # Contact info - all in one line for ATS
    pdf_canvas.setFont('Arial', 9)
    pdf_canvas.setFillColor(text_color)
    contact_line = f"Email: {data['sidebar']['email']} | Phone: {data['sidebar']['phone']} | "
    contact_line += f"LinkedIn: linkedin.com/in/{data['sidebar']['linkedin']} | "
    contact_line += f"GitHub: github.com/{data['sidebar']['github']} | Location: Istanbul, Turkey"
    
    # Word wrap contact line if needed
    if pdf_canvas.stringWidth(contact_line, 'Arial', 9) > content_width:
        # Split into two lines
        parts = contact_line.split(' | ')
        line1 = ' | '.join(parts[:2])
        line2 = ' | '.join(parts[2:])
        pdf_canvas.drawString(margin_x, y_position, line1)
        y_position -= 5*mm
        pdf_canvas.drawString(margin_x, y_position, line2)
    else:
        pdf_canvas.drawString(margin_x, y_position, contact_line)
    
    y_position -= 10*mm
    
    # Horizontal line separator
    pdf_canvas.setStrokeColor(colors.grey)
    pdf_canvas.setLineWidth(0.5)
    pdf_canvas.line(margin_x, y_position, page_width - margin_x, y_position)
    y_position -= 8*mm
    
    # Professional Summary
    pdf_canvas.setFont('Arial-Bold', 12)
    pdf_canvas.setFillColor(heading_color)
    pdf_canvas.drawString(margin_x, y_position, "PROFESSIONAL SUMMARY")
    y_position -= 7*mm
    
    # Summary text - remove bold markers for ATS
    summary = data['career-profile']['summary']
    summary_clean = re.sub(r'\*\*(.+?)\*\*', r'\1', summary)  # Remove ** markers
    
    pdf_canvas.setFont('Arial', 10)
    pdf_canvas.setFillColor(text_color)
    
    # Word wrap summary
    paragraphs = summary_clean.split('\n\n')
    for para in paragraphs[:2]:
        words = para.split()
        line = []
        for word in words:
            test_line = ' '.join(line + [word])
            if pdf_canvas.stringWidth(test_line, 'Arial', 10) < content_width:
                line.append(word)
            else:
                pdf_canvas.drawString(margin_x, y_position, ' '.join(line))
                y_position -= 5*mm
                line = [word]
        
        if line:
            pdf_canvas.drawString(margin_x, y_position, ' '.join(line))
            y_position -= 7*mm
    
    # Skills section
    y_position -= 3*mm
    pdf_canvas.setFont('Arial-Bold', 12)
    pdf_canvas.setFillColor(heading_color)
    pdf_canvas.drawString(margin_x, y_position, "TECHNICAL SKILLS")
    y_position -= 7*mm
    
    # Skills as comma-separated list for ATS
    skills_list = [
        "C# and .NET Core", "Clean Architecture", "GitHub Copilot Enterprise",
        "Microservices", "REST APIs", "Azure DevOps", "MSSQL", "Oracle",
        "EF Core", "Java Spring Boot", "TypeScript", "JavaScript"
    ]
    
    pdf_canvas.setFont('Arial', 10)
    pdf_canvas.setFillColor(text_color)
    skills_text = ', '.join(skills_list)
    
    # Word wrap skills
    words = skills_text.split()
    line = []
    for word in words:
        test_line = ' '.join(line + [word])
        if pdf_canvas.stringWidth(test_line, 'Arial', 10) < content_width:
            line.append(word)
        else:
            pdf_canvas.drawString(margin_x, y_position, ' '.join(line))
            y_position -= 5*mm
            line = [word]
    
    if line:
        pdf_canvas.drawString(margin_x, y_position, ' '.join(line))
        y_position -= 10*mm
    
    # Professional Experience
    pdf_canvas.setFont('Arial-Bold', 12)
    pdf_canvas.setFillColor(heading_color)
    pdf_canvas.drawString(margin_x, y_position, "PROFESSIONAL EXPERIENCE")
    y_position -= 7*mm
    
    for exp in experiences:
        # Check if we need a new page
        if y_position < 40*mm:
            pdf_canvas.showPage()
            y_position = page_height - 25*mm
        
        # Job title - bold and larger
        pdf_canvas.setFont('Arial-Bold', 11)
        pdf_canvas.setFillColor(text_color)
        pdf_canvas.drawString(margin_x, y_position, exp['job_title'])
        y_position -= 6*mm
        
        # Company and dates on one line
        pdf_canvas.setFont('Arial', 10)
        company_line = f"{exp['company']}, {exp['location']} | {exp['dates']}"
        pdf_canvas.drawString(margin_x, y_position, company_line)
        y_position -= 6*mm
        
        # Description bullets - remove bold markers for ATS
        desc_lines = exp.get('description', '').strip().split('\n')
        bullet_count = 0
        
        for line in desc_lines:
            line = line.strip()
            if line.startswith('- ') and bullet_count < 5:  # Max 5 bullets for ATS
                bullet_text = line[2:]
                # Remove bold markers
                bullet_text = re.sub(r'\*\*(.+?)\*\*', r'\1', bullet_text)
                
                # Word wrap bullet
                words = bullet_text.split()
                current_line = []
                first_line = True
                
                for word in words:
                    test_line = ' '.join(current_line + [word])
                    test_width = pdf_canvas.stringWidth(test_line, 'Arial', 10)
                    indent = 8*mm if first_line else 10*mm
                    
                    if test_width < content_width - indent:
                        current_line.append(word)
                    else:
                        if first_line:
                            pdf_canvas.drawString(margin_x + 3*mm, y_position, '•')
                            pdf_canvas.drawString(margin_x + 8*mm, y_position, ' '.join(current_line))
                        else:
                            pdf_canvas.drawString(margin_x + 10*mm, y_position, ' '.join(current_line))
                        y_position -= 5*mm
                        current_line = [word]
                        first_line = False
                
                if current_line:
                    if first_line:
                        pdf_canvas.drawString(margin_x + 3*mm, y_position, '•')
                        pdf_canvas.drawString(margin_x + 8*mm, y_position, ' '.join(current_line))
                    else:
                        pdf_canvas.drawString(margin_x + 10*mm, y_position, ' '.join(current_line))
                    y_position -= 5*mm
                
                bullet_count += 1
        
        y_position -= 5*mm  # Space between jobs
    
    # Education
    if y_position < 50*mm:
        pdf_canvas.showPage()
        y_position = page_height - 25*mm
    
    y_position -= 3*mm
    pdf_canvas.setFont('Arial-Bold', 12)
    pdf_canvas.setFillColor(heading_color)
    pdf_canvas.drawString(margin_x, y_position, "EDUCATION")
    y_position -= 7*mm
    
    for edu in education:
        pdf_canvas.setFont('Arial-Bold', 11)
        pdf_canvas.setFillColor(text_color)
        pdf_canvas.drawString(margin_x, y_position, edu['qualification'])
        y_position -= 6*mm
        
        pdf_canvas.setFont('Arial', 10)
        edu_line = f"{edu['name']}, {edu['location']} | {edu['dates']}"
        pdf_canvas.drawString(margin_x, y_position, edu_line)
        y_position -= 10*mm
    
    # Certifications
    if 'certifications' in data and data['certifications']:
        if y_position < 50*mm:
            pdf_canvas.showPage()
            y_position = page_height - 25*mm
        
        y_position -= 3*mm
        pdf_canvas.setFont('Arial-Bold', 12)
        pdf_canvas.setFillColor(heading_color)
        pdf_canvas.drawString(margin_x, y_position, "CERTIFICATIONS")
        y_position -= 7*mm
        
        for cert in data['certifications']['list'][:3]:  # Top 3 for ATS
            pdf_canvas.setFont('Arial', 10)
            pdf_canvas.setFillColor(text_color)
            cert_text = f"• {cert['name']} - {cert['organization']} ({cert['start']})"
            pdf_canvas.drawString(margin_x, y_position, cert_text)
            y_position -= 5*mm
    
    # Languages
    y_position -= 5*mm
    pdf_canvas.setFont('Arial-Bold', 12)
    pdf_canvas.setFillColor(heading_color)
    pdf_canvas.drawString(margin_x, y_position, "LANGUAGES")
    y_position -= 7*mm
    
    pdf_canvas.setFont('Arial', 10)
    pdf_canvas.setFillColor(text_color)
    languages = data['sidebar']['languages']['info']
    lang_text = ', '.join([f"{lang['idiom']} ({lang['level']})" for lang in languages])
    pdf_canvas.drawString(margin_x, y_position, lang_text)
    
    # Save PDF
    pdf_canvas.save()
    
    print(f"✅ ATS-friendly CV created: {filename}")
    print(f"📂 Location: {filename}")
    print("\n🎉 ATS PDF READY!")

if __name__ == '__main__':
    generate_ats_cv()
