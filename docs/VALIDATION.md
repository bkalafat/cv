# Validation record

Date: September 8, 2026.

## Results

| Command/check | Result |
| --- | --- |
| `python scripts/validate_cv.py` | Pass: all 10 repository YAML files, duplicate keys, canonical content, contact URLs, and domain consistency. Dependency/cache directories excluded. |
| `python -m compileall -q scripts tests` | Pass. |
| `python scripts/generate_beautiful_cv.py` | Pass: professional PDF, two pages. |
| `python scripts/generate_beautiful_cv_ats.py` | Pass: ATS PDF, two pages, and UTF-8 text companion. |
| `python -m unittest discover -s tests -v` | Pass: one parameterized regression test across both layouts; 45 long bullets generate six-page stress documents without content loss, character corruption, or page overflow. |
| `bundle exec jekyll build --trace` with `JEKYLL_ENV=production` | Pass using Ruby 3.4.8 and Jekyll 4.4.1. Legacy Sass @import deprecation notices are non-fatal. |
| `python scripts/validate_cv.py --outputs` | Pass: every content field in both PDFs and HTML; all six roles in extraction order; Unicode, clickable PDF links, page bounds, local assets, exact generated downloads, ATS text parity, semantic/SEO markers, and excluded repository files. |
| `bundle exec jekyll build --baseurl /cv --destination tmp/site-subpath` | Pass. |
| `python scripts/validate_cv.py --outputs --site-dir tmp/site-subpath --baseurl /cv` | Pass: subpath-aware assets and download links. |
| `actionlint .github/workflows/jekyll-gh-pages.yml` | Pass, actionlint 1.7.12. |
| `git diff --check` | Pass; only informational CRLF normalization notices. |
| PDF visual review | All four final PDF pages inspected as rendered images. No clipped text, missing sections, broken Turkish characters, or layout collisions. |
| Desktop/mobile Chrome review | Pass at 1440, 900, 768, 700, 390, and 320px widths: no horizontal overflow or title/date overlaps. Reviewed screenshots at desktop/mobile sizes. |
| Keyboard and downloads | Skip link focuses main content; both PDF download buttons produce the exact generated files; no browser page errors or failed resource responses. |
| Browser print | Three readable A4 pages; download controls/photo hidden and role blocks kept together. Use either generated PDF for the two-page deliverable. |
| Public link checks | CV site, GitHub profile, Microsoft certification overview, and Microsoft Learn course returned HTTP 200. LinkedIn blocks automated access; URL format verified. |
| Independent release review | No material findings. Publication exclusions and chronology/subpath validator checks tightened. |

The latest authoritative PDFs use the same content and typography. The professional version adds navy accents and page furniture; ATS has no graphics, columns, sidebars, tables, or decorative furniture. Normal PDF extraction and the plain-text companion retain full LinkedIn/GitHub/site URLs.

## Environment

Python dependencies are installed in the ignored local .venv. Bundled DejaVu fonts make Windows and Linux rendering independent of system fonts. Gemfile.lock includes Windows and x86_64 Linux platforms.

Ruby was initially absent. A portable Ruby and its native toolchain were prepared under ignored tmp/tools, and dependencies were installed under ignored vendor/bundle. Initial setup failures (missing native compiler and a stale MSYS2 package database) were resolved before successful builds. No application source workaround or fake build was used.

The in-app Browser runtime exposed no browser session. Browser QA therefore used an isolated headless Chrome instance via a local Playwright installation. Page rendering used PyMuPDF because Poppler was not installed. QA intermediates are under ignored tmp/.

## Source review and scope

The initial source baseline was b0a3845. Concurrent user commits d5bf35a, 88a88db, cffc65e, and 3306806 captured earlier work during the task. The full CV changes were reviewed against the original source as well as the current working diff.

Unrelated .codex/agent configuration, AGENTS.md, .github agent/prompt/skill additions, and agent-team documentation were preserved. They are not part of the CV change inventory below. The user's concurrent additions to .github/copilot-instructions.md are also preserved.

## CV files changed during this task

- `.github/copilot-instructions.md`
- `.github/workflows/jekyll-gh-pages.yml`
- `.gitignore`
- `Gemfile`
- `Gemfile.lock`
- `requirements.txt`
- `README.md`
- `_config.yml`
- `index.md`
- `robots.txt`
- `_data/data.yml`
- `_data/experience.yml (removed)`
- `_data/education.yml (removed)`
- `_data/projects.yml (removed)`
- `_includes/career-profile.html`
- `_includes/certifications.html`
- `_includes/contact.html`
- `_includes/education.html`
- `_includes/experiences.html`
- `_includes/head.html`
- `_includes/interests.html`
- `_includes/language.html`
- `_includes/sidebar.html`
- `_includes/skills.html`
- `_layouts/default.html`
- `_layouts/print.html`
- `_sass/_base.scss`
- `_sass/_responsive.scss`
- `_sass/_print.scss`
- `assets/fonts/DejaVuSans.ttf`
- `assets/fonts/DejaVuSans-Bold.ttf`
- `assets/fonts/LICENSE`
- `assets/js/pdf-generator.js (removed)`
- `scripts/cv_data.py`
- `scripts/cv_pdf.py`
- `scripts/cv_text.py`
- `scripts/generate_beautiful_cv.py`
- `scripts/generate_beautiful_cv_ats.py`
- `scripts/validate_cv.py`
- `tests/test_pdf_generation.py`
- `downloads/Burak_Kalafat_Professional_CV.pdf`
- `downloads/Burak_Kalafat_ATS_CV.pdf`
- `downloads/Burak_Kalafat_ATS_CV.txt`
- `downloads/README.md`
- `docs/CV_AUDIT.md`
- `docs/RECRUITER_REVIEW.md`
- `docs/VALIDATION.md`
- `docs/latex-cv/README.md`
- `docs/latex-cv/README-jake.md`
- `docs/latex-cv/QUICKSTART.md`
- `docs/latex-cv/cv.tex`
- `docs/latex-cv/burak_kalafat_resume.tex`

## Publication

The earlier 3306806 revision completed GitHub Actions successfully: [build and deployment](https://github.com/bkalafat/cv/actions/runs/34200174725).
The final mobile/print refinements and recruiter/validation reports are prepared for publication using the existing GitHub Pages workflow. Final deployment status and live output checks are reported in the task's completion message.

## Remaining limitations

- There is no claim of a universal ATS compatibility score or complete WCAG certification.
- Current employment/title confirmation and stronger insightsoftware/Staff-level scope evidence remain documented in the audit and recruiter review.
- Numerical improvement claims remain omitted by owner instruction.
- Legacy Sass imports can be migrated to modules in a future stylesheet maintenance pass.
