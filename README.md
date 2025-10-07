# 🚀 Burak Kalafat - Professional CV Website

[![Build Status](https://github.com/bkalafat/cv/workflows/Build%20and%20Deploy%20CV/badge.svg)](https://github.com/bkalafat/cv/actions)
[![GitHub Pages](https://img.shields.io/badge/GitHub-Pages-blue)](https://bkalafat.github.io/cv)

A modern, responsive CV website built with Jekyll and hosted on GitHub Pages. Features automatic PDF and DOCX generation via GitHub Actions.

## 🌐 Live Site

Visit the live CV at: **[https://bkalafat.github.io/cv](https://bkalafat.github.io/cv)** *(Update this URL after deployment)*

## ✨ Features

- 🎨 **Modern Design**: Built with [modern-resume-theme](https://github.com/sproogen/modern-resume-theme)
- 📱 **Responsive**: Works perfectly on mobile, tablet, and desktop
- 🔄 **Auto-Generated Documents**: Automatic PDF and DOCX generation on every commit
- 🚀 **Fast Deployment**: Hosted on GitHub Pages with automatic builds
- ♿ **Accessible**: WCAG compliant and screen-reader friendly
- 🔍 **SEO Optimized**: Meta tags and sitemap included

## 📥 Download Resume

- **PDF**: [Download CV (PDF)](https://github.com/bkalafat/cv/actions) - Available in Actions artifacts
- **DOCX**: [Download CV (DOCX)](https://github.com/bkalafat/cv/actions) - Available in Actions artifacts
- **Web**: Print to PDF directly from the website

## 🛠️ Technology Stack

- **Static Site Generator**: Jekyll 4.3
- **Theme**: Modern Resume Theme 2.0
- **Hosting**: GitHub Pages
- **CI/CD**: GitHub Actions
- **Document Generation**: 
  - wkhtmltopdf (HTML to PDF)
  - Pandoc (Markdown to DOCX/PDF)

## 📁 Project Structure

```
cv/
├── .github/
│   └── workflows/
│       ├── build-resume.yml      # Main build & deploy workflow
│       └── generate-docx.yml     # DOCX/PDF generation workflow
├── _data/
│   ├── experience.yml            # Work experience data
│   ├── education.yml             # Education data
│   └── projects.yml              # Certifications & projects
├── assets/
│   └── images/
│       ├── profile.jpg           # Profile photo (add your own)
│       └── favicon.svg           # Site favicon
├── _config.yml                   # Jekyll & site configuration
├── index.md                      # Main page
├── Gemfile                       # Ruby dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## 🚀 Quick Start

### Prerequisites

- Ruby 3.1 or higher
- Bundler gem
- Git

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/bkalafat/cv.git
   cd cv
   ```

2. **Install dependencies**
   ```bash
   bundle install
   ```

3. **Run local server**
   ```bash
   bundle exec jekyll serve
   ```

4. **Open in browser**
   ```
   http://localhost:4000
   ```

## ✏️ How to Update Your CV

### 1. Update Personal Information

Edit `_config.yml`:
```yaml
name: Your Name
title: Your Job Title
email: your.email@example.com
phone: "+90xxxxxxxxxx"
```

### 2. Update Work Experience

Edit `_data/experience.yml`:
```yaml
- layout: left
  company: Company Name
  job_title: Your Position
  dates: Month Year - Present
  location: City, Country
  description: |
    - Achievement 1
    - Achievement 2
```

### 3. Update Education

Edit `_data/education.yml`:
```yaml
- layout: left
  name: University Name
  dates: Year - Year
  qualification: Degree Name
  description: Additional details
```

### 4. Update Certifications/Projects

Edit `_data/projects.yml`:
```yaml
- layout: top-middle
  name: Certification/Project Name
  dates: Month Year
  description: Details about the certification
```

### 5. Add Profile Photo

Replace `assets/images/profile.jpg` with your photo (recommended: 400x400px, square)

## 🚀 Deployment

### Initial Setup

1. **Create GitHub Repository**
   ```bash
   # Initialize git if not already done
   git init
   git add .
   git commit -m "Initial commit: CV website"
   
   # Create repo on GitHub, then:
   git remote add origin https://github.com/bkalafat/cv.git
   git branch -M main
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to repository Settings → Pages
   - Source: Deploy from a branch
   - Branch: Select `gh-pages` (will be created automatically by workflow)
   - Click Save

3. **Update URLs in _config.yml**
   ```yaml
   baseurl: "/cv"  # your repo name
   url: "https://bkalafat.github.io"  # your GitHub Pages URL
   ```

### Automatic Deployment

Every push to `main` branch will:
1. ✅ Build Jekyll site
2. ✅ Deploy to GitHub Pages
3. ✅ Generate PDF from HTML
4. ✅ Generate DOCX and PDF from Markdown

### Manual Deployment

Trigger workflows manually:
- Go to Actions tab
- Select workflow
- Click "Run workflow"

## 📦 Download Generated Documents

After each build:
1. Go to **Actions** tab
2. Click on latest workflow run
3. Download artifacts:
   - `cv-pdf`: PDF from HTML
   - `cv-docx`: DOCX and PDF from Markdown

## 🎨 Customization

### Change Theme Colors

Create `_sass/custom.scss` and override theme variables.

### Add Custom Sections

Create new YAML files in `_data/` folder and reference them in `index.md`.

### Modify Layout

The theme uses remote theme. To customize layouts, override them locally by creating files in `_layouts/` folder.

## 🧪 Testing

### Local Testing
```bash
# Build site
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve --livereload
```

### Validate HTML
```bash
bundle exec htmlproofer ./_site --disable-external
```

## 📝 Print to PDF (Manual)

From the website:
1. Open CV in browser
2. Press `Ctrl+P` (or `Cmd+P` on Mac)
3. Select "Save as PDF"
4. Adjust margins if needed
5. Save

## 🔧 Troubleshooting

### Build Fails
- Check Jekyll version compatibility
- Verify all YAML files are valid
- Ensure remote theme is accessible

### GitHub Pages Not Updating
- Wait 2-3 minutes after push
- Check Actions tab for build status
- Verify GitHub Pages is enabled

### PDF/DOCX Not Generated
- Check Actions tab for errors
- Verify workflows have correct permissions
- Check artifact retention settings

## 📄 License

This project uses the [Modern Resume Theme](https://github.com/sproogen/modern-resume-theme) which is licensed under MIT.

Your CV content is your own.

## 🙏 Credits

- **Theme**: [Modern Resume Theme](https://github.com/sproogen/modern-resume-theme) by James Grant
- **Static Site Generator**: [Jekyll](https://jekyllrb.com/)
- **Hosting**: [GitHub Pages](https://pages.github.com/)
- **PDF Generation**: [wkhtmltopdf](https://wkhtmltopdf.org/)
- **Document Conversion**: [Pandoc](https://pandoc.org/)

## 📞 Contact

**Burak Kalafat**
- Email: burakkalafat89@gmail.com
- GitHub: [@bkalafat](https://github.com/bkalafat)
- LinkedIn: [bkalafat](https://www.linkedin.com/in/bkalafat/)

---

⭐ If you found this helpful, please star the repository!

**Last Updated**: October 2025
