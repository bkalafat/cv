"""
Modern Sidebar CV Generator - Matches your original beautiful design!
Creates PDF with blue sidebar, white content area, and professional layout
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak, Frame, PageTemplate
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.rl_config import defaultEncoding
import yaml
import os
from datetime import datetime
from io import BytesIO

# Enable UTF-8 support for Turkish characters
defaultEncoding = 'utf-8'

# Professional colors - FAANG/Enterprise standard with higher contrast
SIDEBAR_COLOR = HexColor('#2B5A8F')  # Professional navy blue (better contrast)
ACCENT_COLOR = HexColor('#4A90E2')    # Vibrant azure (WCAG AA compliant)
TEXT_COLOR = HexColor('#1a1a1a')      # Near black (better readability)
LIGHT_GRAY = HexColor('#f5f7fa')      # Softer background
WHITE = colors.white

def load_yaml_data():
    """Load all YAML data files"""
    with open('_data/data.yml', 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    with open('_data/experience.yml', 'r', encoding='utf-8') as f:
        experiences = yaml.safe_load(f)
    with open('_data/education.yml', 'r', encoding='utf-8') as f:
        education = yaml.safe_load(f)
    
    return data, experiences, education

class ModernCVCanvas(canvas.Canvas):
    """Custom canvas with sidebar - ONLY on first page!"""
    
    def __init__(self, *args, **kwargs):
        self.data = kwargs.pop('data', None)
        self.page_num = 0  # Track page number
        canvas.Canvas.__init__(self, *args, **kwargs)
        
    def showPage(self):
        self.draw_sidebar()
        canvas.Canvas.showPage(self)
        self.page_num += 1  # Increment after each page
    
    def draw_sidebar(self):
        """Draw the blue sidebar with photo and contact info - ONLY ON FIRST PAGE"""
        if not self.data:
            return
        
        # CRITICAL FIX: Only draw sidebar on first page!
        if self.page_num > 0:
            return  # Skip sidebar on subsequent pages
            
        page_width, page_height = A4
        sidebar_width = 65*mm
        
        # Draw sidebar background
        self.setFillColor(SIDEBAR_COLOR)
        self.rect(0, 0, sidebar_width, page_height, fill=1, stroke=0)
        
        # Profile photo (circular with clipping)
        try:
            photo_path = 'assets/images/profile.png'
            if os.path.exists(photo_path):
                from PIL import Image as PILImage
                
                photo_size = 35*mm
                x = (sidebar_width - photo_size) / 2
                y = page_height - 50*mm
                
                # White circle background
                self.setFillColor(WHITE)
                self.circle(x + photo_size/2, y + photo_size/2, photo_size/2 + 2*mm, fill=1, stroke=0)
                
                # Save state and create circular clipping path
                self.saveState()
                
                # Create circular clipping path
                p = self.beginPath()
                p.circle(x + photo_size/2, y + photo_size/2, photo_size/2)
                self.clipPath(p, stroke=0, fill=0)
                
                # Draw photo within circular clip
                self.drawImage(photo_path, x, y, 
                             width=photo_size, height=photo_size,
                             preserveAspectRatio=True)
                
                self.restoreState()
        except Exception as e:
            print(f"Note: Could not load photo: {e}")
        
        # Name - Larger and more prominent (FAANG standard: 18-20pt)
        self.setFillColor(WHITE)
        self.setFont('Arial-Bold', 18)
        name = self.data['sidebar']['name']
        name_width = self.stringWidth(name, 'Arial-Bold', 18)
        self.drawString((sidebar_width - name_width) / 2, page_height - 60*mm, name)
        
        # Tagline - Professional size (10pt for better hierarchy)
        self.setFont('Arial', 10)
        tagline = self.data['sidebar']['tagline']
        # Split long tagline
        words = tagline.split()
        if len(words) > 3:
            line1 = ' '.join(words[:3])
            line2 = ' '.join(words[3:])
            w1 = self.stringWidth(line1, 'Arial', 10)
            w2 = self.stringWidth(line2, 'Arial', 10)
            self.drawString((sidebar_width - w1) / 2, page_height - 67*mm, line1)
            self.drawString((sidebar_width - w2) / 2, page_height - 72*mm, line2)
        else:
            w = self.stringWidth(tagline, 'Arial', 10)
            self.drawString((sidebar_width - w) / 2, page_height - 67*mm, tagline)
        
        # Contact section
        y_pos = page_height - 90*mm
        self.setFont('Arial-Bold', 12)
        self.setFillColor(WHITE)
        self.drawString(10*mm, y_pos, "CONTACT")
        
        # Line under CONTACT
        self.setStrokeColor(ACCENT_COLOR)
        self.setLineWidth(2)
        self.line(10*mm, y_pos - 2*mm, 55*mm, y_pos - 2*mm)
        
        # Contact details
        y_pos -= 8*mm
        self.setFont('Arial', 9)
        contact_items = [
            ("📧 Email", self.data['sidebar']['email']),
            ("📱 Phone", self.data['sidebar']['phone']),
            ("💼 LinkedIn", self.data['sidebar']['linkedin']),
            ("💻 GitHub", self.data['sidebar']['github']),
            ("📍 Location", "Istanbul, Turkey")
        ]
        
        for label, value in contact_items:
            # CRITICAL FIX: White text on dark blue for readability (WCAG AA)
            self.setFillColor(WHITE)
            self.setFont('Arial-Bold', 9)  # Slightly larger for better readability
            self.drawString(10*mm, y_pos, label)
            
            self.setFillColor(WHITE)  # WHITE not accent color!
            self.setFont('Arial', 9)  # Consistent size
            # Wrap long text
            value_str = str(value)
            if len(value_str) > 25:
                value_str = value_str[:22] + "..."
            
            text_y = y_pos - 4*mm
            self.drawString(10*mm, text_y, value_str)
            
            # Add clickable hyperlinks for email, LinkedIn, GitHub
            if "Email" in label and "@" in value_str:
                # Email link
                link_rect = (10*mm, text_y - 1*mm, 55*mm, text_y + 3*mm)
                self.linkURL(f"mailto:{value}", link_rect, relative=0)
            elif "LinkedIn" in label:
                # LinkedIn link
                link_rect = (10*mm, text_y - 1*mm, 55*mm, text_y + 3*mm)
                linkedin_url = value if value.startswith('http') else f"https://linkedin.com/in/{value}"
                self.linkURL(linkedin_url, link_rect, relative=0)
            elif "GitHub" in label:
                # GitHub link
                link_rect = (10*mm, text_y - 1*mm, 55*mm, text_y + 3*mm)
                github_url = value if value.startswith('http') else f"https://github.com/{value}"
                self.linkURL(github_url, link_rect, relative=0)
            
            y_pos -= 11*mm  # More breathing room
        
        # Skills section
        y_pos -= 5*mm
        self.setFont('Arial-Bold', 12)
        self.setFillColor(WHITE)
        self.drawString(10*mm, y_pos, "SKILLS")
        
        self.setStrokeColor(ACCENT_COLOR)
        self.setLineWidth(2)
        self.line(10*mm, y_pos - 2*mm, 55*mm, y_pos - 2*mm)
        
        y_pos -= 8*mm
        # Skills ordered by importance and proficiency (0-100%)
        # Following FAANG/enterprise best practices: Core tech → Architecture → Cloud → Tools
        skills = [
            ("C# & .NET Core", 98),
            ("Clean Architecture", 95),
            ("GitHub Copilot", 95),
            ("Microservices & DDD", 92),
            ("REST APIs & gRPC", 95),
            ("Event Sourcing/CQRS", 90),
            ("Azure Cloud & DevOps", 88),
            ("Docker & Kubernetes", 85),
            ("MSSQL & Oracle", 90),
            ("Java & Spring Boot", 85)
        ]
        
        self.setFont('Arial', 9)
        for skill, level in skills:
            # Background bar
            self.setFillColor(HexColor('#34495e'))
            self.rect(10*mm, y_pos - 2*mm, 45*mm, 3*mm, fill=1, stroke=0)
            
            # Filled bar based on actual level
            self.setFillColor(ACCENT_COLOR)
            bar_width = (45*mm * level) / 100
            self.rect(10*mm, y_pos - 2*mm, bar_width, 3*mm, fill=1, stroke=0)
            
            # Skill name
            self.setFillColor(WHITE)
            self.drawString(10*mm, y_pos + 1.5*mm, skill)
            
            y_pos -= 7*mm
            if y_pos < 30*mm:  # Stop if running out of space
                break
        
        # Languages
        if y_pos > 40*mm:
            y_pos -= 5*mm
            self.setFont('Arial-Bold', 12)
            self.setFillColor(WHITE)
            self.drawString(10*mm, y_pos, "LANGUAGES")
            
            self.setStrokeColor(ACCENT_COLOR)
            self.setLineWidth(2)
            self.line(10*mm, y_pos - 2*mm, 55*mm, y_pos - 2*mm)
            
            y_pos -= 8*mm
            self.setFont('Arial', 9)
            languages = [
                ("Turkish", "Native"),
                ("English", "Professional")
            ]
            
            for lang, level in languages:
                self.setFillColor(WHITE)
                self.setFont('Arial-Bold', 9)
                self.drawString(10*mm, y_pos, lang)
                self.setFont('Arial', 9)
                self.setFillColor(ACCENT_COLOR)
                self.drawString(35*mm, y_pos, level)
                y_pos -= 6*mm

def generate_modern_cv():
    """Generate CV with modern sidebar design"""
    
    print("🚀 Loading data...")
    data, experiences, education = load_yaml_data()
    
    print("🎨 Creating beautiful PDF with sidebar...")
    
    filename = f"Burak_Kalafat_Professional_CV.pdf"
    
    # Create custom canvas
    pdf_canvas = ModernCVCanvas(filename, pagesize=A4, data=data)
    
    # Register font for Turkish characters
    try:
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        # Use system fonts that support Turkish
        pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))
        pdfmetrics.registerFont(TTFont('Arial-Bold', 'arialbd.ttf'))
    except:
        pass  # If fonts not available, use default
    
    # Page dimensions
    page_width, page_height = A4
    sidebar_width = 65*mm
    content_x = sidebar_width + 10*mm
    content_width = page_width - sidebar_width - 20*mm
    
    # Styles
    styles = getSampleStyleSheet()
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=SIDEBAR_COLOR,
        spaceAfter=8,
        spaceBefore=14,
        fontName='Arial-Bold',
        borderWidth=1,
        borderColor=ACCENT_COLOR,
        borderPadding=4,
        leftIndent=0,
    )
    
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=SIDEBAR_COLOR,
        fontName='Arial-Bold',
        spaceAfter=3
    )
    
    company_style = ParagraphStyle(
        'Company',
        parent=styles['Normal'],
        fontSize=10,
        textColor=ACCENT_COLOR,
        fontName='Arial-Bold',
        spaceAfter=2
    )
    
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        fontName='Helvetica-Oblique',
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=9,
        textColor=TEXT_COLOR,
        spaceAfter=4,
        leftIndent=12,
        bulletIndent=8,
        fontName='Arial',
        leading=13  # Increased from 12 to 13 (line-height ~1.44)
    )
    
    # Start drawing content
    y_position = page_height - 30*mm
    
    # Professional Profile (renamed from 'Professional Summary' for better tone)
    pdf_canvas.setFillColor(SIDEBAR_COLOR)
    pdf_canvas.setFont('Arial-Bold', 15)
    pdf_canvas.drawString(content_x, y_position, "PROFESSIONAL PROFILE")
    
    # Thicker accent line for better visual hierarchy
    pdf_canvas.setStrokeColor(ACCENT_COLOR)
    pdf_canvas.setLineWidth(2.5)
    pdf_canvas.line(content_x, y_position - 3*mm, content_x + content_width, y_position - 3*mm)
    
    y_position -= 10*mm
    
    # Summary text with bold support
    summary = data['career-profile']['summary']
    summary_lines = summary.split('\n\n')
    
    for para in summary_lines[:2]:  # First 2 paragraphs
        # Process bold markers (**text**)
        import re
        segments = []
        last_end = 0
        
        for match in re.finditer(r'\*\*(.+?)\*\*', para):
            # Add text before bold
            if match.start() > last_end:
                segments.append(('normal', para[last_end:match.start()]))
            # Add bold text
            segments.append(('bold', match.group(1)))
            last_end = match.end()
        
        # Add remaining text
        if last_end < len(para):
            segments.append(('normal', para[last_end:]))
        
        # Draw segments with word wrapping
        line_words = []
        line_styles = []
        
        for style, text in segments:
            words = text.split()
            for word in words:
                line_words.append(word)
                line_styles.append(style)
        
        current_line = []
        current_styles = []
        
        for word, style in zip(line_words, line_styles):
            test_line = ' '.join(current_line + [word])
            # Approximate width (bold is wider)
            test_width = sum([
                pdf_canvas.stringWidth(w + ' ', 'Arial-Bold' if s == 'bold' else 'Arial', 9)
                for w, s in zip(current_line + [word], current_styles + [style])
            ])
            
            if test_width < content_width:
                current_line.append(word)
                current_styles.append(style)
            else:
                # Draw current line
                x_pos = content_x
                for w, s in zip(current_line, current_styles):
                    pdf_canvas.setFont('Arial-Bold' if s == 'bold' else 'Arial', 9)
                    pdf_canvas.setFillColor(TEXT_COLOR)
                    pdf_canvas.drawString(x_pos, y_position, w)
                    x_pos += pdf_canvas.stringWidth(w + ' ', 'Arial-Bold' if s == 'bold' else 'Arial', 9)
                
                y_position -= 5*mm  # Increased line spacing within paragraphs
                current_line = [word]
                current_styles = [style]
        
        # Draw remaining line
        if current_line:
            x_pos = content_x
            for w, s in zip(current_line, current_styles):
                pdf_canvas.setFont('Arial-Bold' if s == 'bold' else 'Arial', 9)
                pdf_canvas.setFillColor(TEXT_COLOR)
                pdf_canvas.drawString(x_pos, y_position, w)
                x_pos += pdf_canvas.stringWidth(w + ' ', 'Arial-Bold' if s == 'bold' else 'Arial', 9)
            y_position -= 7*mm  # Increased paragraph spacing
    
    # Experience - Larger heading for better hierarchy
    y_position -= 10*mm  # Increased spacing between sections for better visual separation
    pdf_canvas.setFillColor(SIDEBAR_COLOR)
    pdf_canvas.setFont('Arial-Bold', 15)
    pdf_canvas.drawString(content_x, y_position, "PROFESSIONAL EXPERIENCE")
    
    pdf_canvas.setStrokeColor(ACCENT_COLOR)
    pdf_canvas.setLineWidth(2.5)
    pdf_canvas.line(content_x, y_position - 3*mm, content_x + content_width, y_position - 3*mm)
    
    y_position -= 10*mm
    
    for i, exp in enumerate(experiences):  # ALL experiences
        if y_position < 50*mm:  # New page if needed
            pdf_canvas.showPage()
            y_position = page_height - 30*mm
            # CRITICAL: Full-width content on page 2+
            if pdf_canvas.page_num > 0:
                content_x = 20*mm
                content_width = page_width - 40*mm
        
        # Job title - Larger and more prominent (12pt)
        pdf_canvas.setFont('Arial-Bold', 12)
        pdf_canvas.setFillColor(SIDEBAR_COLOR)
        pdf_canvas.drawString(content_x, y_position, exp['job_title'])
        
        y_position -= 6*mm  # Better spacing
        
        # Company and dates - More contrast
        pdf_canvas.setFont('Arial-Bold', 10)
        pdf_canvas.setFillColor(ACCENT_COLOR)
        pdf_canvas.drawString(content_x, y_position, exp['company'])
        
        pdf_canvas.setFont('Arial', 9)
        pdf_canvas.setFillColor(HexColor('#666666'))  # Darker gray for better readability
        dates_text = f"{exp['dates']} | {exp['location']}"
        pdf_canvas.drawRightString(content_x + content_width, y_position, dates_text)
        
        y_position -= 6*mm
        
        # Highlights (bullet points) - IMPROVED READABILITY
        desc_lines = exp.get('description', '').strip().split('\n')
        pdf_canvas.setFont('Arial', 9)  # 9pt instead of 8pt for better readability
        pdf_canvas.setFillColor(TEXT_COLOR)
        
        bullet_count = 0
        for line in desc_lines:
            line = line.strip()
            if line.startswith('- ') and bullet_count < 4:  # Max 4 bullets per job (cleaner)
                bullet_text = line[2:]
                
                # Process bold markers
                import re
                segments = []
                last_end = 0
                
                for match in re.finditer(r'\*\*(.+?)\*\*', bullet_text):
                    if match.start() > last_end:
                        segments.append(('normal', bullet_text[last_end:match.start()]))
                    segments.append(('bold', match.group(1)))
                    last_end = match.end()
                
                if last_end < len(bullet_text):
                    segments.append(('normal', bullet_text[last_end:]))
                
                # Draw with word wrapping and bold support
                first_line = True
                x_offset = content_x + 5*mm
                
                for style, text in segments:
                    words = text.split()
                    for word in words:
                        font = 'Arial-Bold' if style == 'bold' else 'Arial'
                        word_width = pdf_canvas.stringWidth(word + ' ', font, 9)  # 9pt
                        
                        if x_offset + word_width > content_x + content_width - 10*mm:
                            y_position -= 6*mm  # Increased breathing room between lines
                            x_offset = content_x + 8*mm  # Indent continuation
                            first_line = False
                        
                        if first_line and x_offset == content_x + 5*mm:
                            pdf_canvas.setFont('Arial', 9)  # 9pt bullet
                            pdf_canvas.drawString(x_offset, y_position, "•")
                            x_offset += 3*mm
                        
                        pdf_canvas.setFont(font, 9)  # 9pt text
                        pdf_canvas.drawString(x_offset, y_position, word)
                        x_offset += word_width
                
                y_position -= 6*mm  # Increased space between bullets for better readability
                bullet_count += 1
        
        y_position -= 4*mm  # Increased spacing after experience items
    
    # Education
    if y_position < 80*mm:
        pdf_canvas.showPage()
        y_position = page_height - 30*mm
        # CRITICAL: Full-width content on page 2+
        if pdf_canvas.page_num > 0:
            content_x = 20*mm
            content_width = page_width - 40*mm
    
    y_position -= 10*mm  # Increased spacing before new section
    pdf_canvas.setFillColor(SIDEBAR_COLOR)
    pdf_canvas.setFont('Arial-Bold', 15)
    pdf_canvas.drawString(content_x, y_position, "EDUCATION")
    
    pdf_canvas.setStrokeColor(ACCENT_COLOR)
    pdf_canvas.setLineWidth(2.5)
    pdf_canvas.line(content_x, y_position - 3*mm, content_x + content_width, y_position - 3*mm)
    
    y_position -= 10*mm
    
    for edu in education:
        pdf_canvas.setFont('Arial-Bold', 11)
        pdf_canvas.setFillColor(SIDEBAR_COLOR)
        pdf_canvas.drawString(content_x, y_position, edu['qualification'])
        
        y_position -= 5*mm
        
        pdf_canvas.setFont('Arial', 9)
        pdf_canvas.setFillColor(TEXT_COLOR)
        pdf_canvas.drawString(content_x, y_position, f"{edu['name']}, {edu['location']}")
        
        pdf_canvas.setFont('Arial', 9)
        pdf_canvas.setFillColor(colors.grey)
        pdf_canvas.drawRightString(content_x + content_width, y_position, edu['dates'])
        
        y_position -= 8*mm
    
    # Certifications
    y_position -= 5*mm
    pdf_canvas.setFillColor(SIDEBAR_COLOR)
    pdf_canvas.setFont('Arial-Bold', 14)
    pdf_canvas.drawString(content_x, y_position, "CERTIFICATIONS")
    
    pdf_canvas.setStrokeColor(ACCENT_COLOR)
    pdf_canvas.setLineWidth(2)
    pdf_canvas.line(content_x, y_position - 3*mm, content_x + content_width, y_position - 3*mm)
    
    y_position -= 10*mm
    
    for cert in data.get('certifications', {}).get('list', [])[:3]:
        pdf_canvas.setFont('Arial-Bold', 9)
        pdf_canvas.setFillColor(TEXT_COLOR)
        pdf_canvas.drawString(content_x + 5*mm, y_position, f"• {cert['name']}")
        
        y_position -= 4*mm
        
        pdf_canvas.setFont('Arial', 9)
        pdf_canvas.setFillColor(colors.grey)
        pdf_canvas.drawString(content_x + 8*mm, y_position, f"{cert['organization']} ({cert['start']})")
        
        y_position -= 6*mm
    
    pdf_canvas.save()
    
    print(f"✅ Professional CV created: {filename}")
    print(f"📂 Location: {os.path.abspath(filename)}")
    print(f"\n🎉 BEAUTIFUL PDF READY! Open it now!")
    
    return filename

if __name__ == "__main__":
    generate_modern_cv()
