# Copilot Instructions for CV Project

## Project Overview

**Jekyll-based CV/Resume website** hosted on GitHub Pages with automatic PDF generation.

**Live Site:** https://bkalafat.github.io/cv

## Tech Stack

- **Static Site Generator:** Jekyll 4.x with GitHub Pages gem
- **Theme:** Modern Resume Theme (customized)
- **Styling:** SCSS with skin options (`_sass/skins/`)
- **PDF Generation:** Python (ReportLab + Pillow + PyYAML)
- **CI/CD:** GitHub Actions
- **Hosting:** GitHub Pages

## Project Structure

```
├── _config.yml           # Jekyll configuration
├── _data/                # CV content (YAML)
│   ├── data.yml          # Personal info, skills, sidebar
│   ├── experience.yml    # Work experience
│   ├── education.yml     # Education history
│   └── projects.yml      # Certifications & projects
├── _includes/            # HTML partials (sections)
├── _layouts/             # Page templates
├── _sass/                # SCSS stylesheets
│   └── skins/            # Theme color options
├── assets/               # Static assets
│   ├── images/           # Profile photo, etc.
│   ├── css/              # Compiled styles
│   └── js/               # JavaScript
├── scripts/              # PDF generators
│   ├── generate_beautiful_cv.py      # Professional PDF (sidebar)
│   └── generate_beautiful_cv_ats.py  # ATS-friendly PDF (plain)
├── downloads/            # Generated PDF outputs
├── docs/                 # Documentation & archives
│   └── latex-cv/         # LaTeX CV alternative
├── .github/
│   └── workflows/        # GitHub Actions CI/CD
├── index.md              # Main page
├── Gemfile               # Ruby dependencies
└── README.md             # Project documentation
```

## Key Guidelines

### Editing CV Content
- Edit `_data/*.yml` files — not templates
- Use `**bold**` markers in YAML for emphasis
- Keep bullet points concise and quantifiable (STAR format)

### Running Locally

```powershell
bundle install
bundle exec jekyll serve
# Open http://localhost:4000/cv
```

### Generating PDFs

```powershell
pip install reportlab Pillow pyyaml

# From project root:
python scripts/generate_beautiful_cv.py       # Professional CV
python scripts/generate_beautiful_cv_ats.py   # ATS-optimized CV
# Output: downloads/*.pdf
```

### Theme Customization
- `theme_skin` in `_config.yml`: blue, turquoise, green, berry, orange, ceramic, teal
- Profile image: `assets/images/profile.png` (100x100px)

## Coding Conventions

- **YAML:** 2-space indent, UTF-8
- **SCSS:** BEM-like naming
- **Python:** PEP 8
- **Commits:** Conventional commits (feat, fix, docs, style, refactor)

## Notes

- PDF generators use Windows Arial fonts (`arial.ttf`, `arialbd.ttf`)
- GitHub Actions auto-deploys on push to `main`
- Turkish character support enabled via UTF-8
- `baseurl: "/cv"` for GitHub Pages subdirectory
