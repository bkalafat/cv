# Burak Kalafat - CV

A Jekyll CV website with two selectable-text PDFs, hosted at [cv.bkalafat.com](https://cv.bkalafat.com).

- [Professional CV](https://cv.bkalafat.com/downloads/Burak_Kalafat_Professional_CV.pdf)
- [ATS CV](https://cv.bkalafat.com/downloads/Burak_Kalafat_ATS_CV.pdf)

## Content and source of truth

Edit **`_data/data.yml`** for all published CV content: profile, contacts, categorized skills, employment, education, credentials, languages, and interests. The website and both PDF generators read this same file. Do not add resume text to Python scripts or HTML templates.

The former `_data/experience.yml`, `education.yml`, and `projects.yml` duplicates have been consolidated and removed. Education month/year dates and course completion dates were retained. Historical originals remain in Git history. See [the audit](docs/CV_AUDIT.md) for editorial decisions, confirmed corrections, and outstanding facts.

- Employment uses month/year dates. Preserve verified role titles and distinguish employers from banking clients.
- Quote telephone numbers, including their leading `+`.
- Use plain UTF-8 text. The renderers escape HTML/XML characters such as `&` and `<`.
- Distinguish training from certifications and production experience.
- Credential `start` and `expires` fields are optional. A course/certification overview link is not a personal credential verification link.
- DiffPilot, numerical improvement claims, and Copilot promotion were removed at the owner's request.
- `docs/latex-cv/` contains archived, unsynchronized experiments. It is excluded from publishing and is not a current CV source.

## Local development

Requires Python 3.13, Ruby 3.3 or 3.4, and Bundler. CI uses Ruby 3.4.
On Windows, use RubyInstaller **with Devkit** for gems with native extensions.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
bundle install
python scripts/validate_cv.py
python scripts/generate_beautiful_cv.py
python scripts/generate_beautiful_cv_ats.py
bundle exec jekyll serve
```

On macOS/Linux, activate with `source .venv/bin/activate`. Open `http://localhost:4000`.
Keep `Gemfile.lock` under version control; it records Windows and Linux dependencies.

## Validation

```powershell
python -m unittest discover -s tests -v
python scripts/generate_beautiful_cv.py
python scripts/generate_beautiful_cv_ats.py
bundle exec jekyll build --trace
python scripts/validate_cv.py --outputs
git diff --check
```

Validation rejects duplicate YAML keys, malformed links, missing CV text, broken Unicode, wrong extraction order, text outside PDF pages, stale exclusions, missing local assets, and inconsistent downloadable PDFs. The current CV is limited to two pages per PDF; pagination regression tests exercise much longer content separately. Visually review both PDFs after content/layout changes; automated checks do not establish compatibility with every ATS.

The generators work from any current directory and write to `downloads/`. Both use a shared ReportLab renderer with bundled DejaVu fonts; the professional version adds navy accents, while the ATS version uses a plain single-column layout. Both include every published content section. Font licensing is in `assets/fonts/LICENSE`.

## Build and deployment

`.github/workflows/jekyll-gh-pages.yml` validates source data, tests pagination, regenerates both PDFs, builds Jekyll, verifies output parity, and uploads PDF and Pages artifacts. Pull requests run the build checks. Deployment runs only on the repository's default branch after a successful build.

In GitHub repository Settings → Pages, choose **GitHub Actions** as the source.
The canonical domain is configured in `_config.yml` and `CNAME`. Keep these and `sidebar.website` aligned.

Generated PDFs are included in the deployed website. Download links use the site's base URL and refer to PDFs generated from the same revision. CI does not commit PDFs back to the branch; regenerate the tracked copies locally when changing content. No DOCX generation is configured.

For a project subpath preview:
```powershell
bundle exec jekyll build --baseurl /cv --destination tmp/site-subpath
python scripts/validate_cv.py --outputs --site-dir tmp/site-subpath --baseurl /cv
```

## Structure

- `_data/data.yml`: canonical content
- `index.md`, `_includes/`, `_layouts/`: Jekyll sections and page structure
- `_sass/`: website, mobile, and print styles
- `scripts/cv_data.py`: shared content loading
- `scripts/cv_pdf.py`: shared PDF layout and pagination
- `scripts/generate_beautiful_cv*.py`: stable PDF entry points
- `scripts/validate_cv.py`, `tests/`: source/output validation and regression coverage
- `downloads/`: generated PDFs
- `docs/`: audit and excluded historical material

## Attribution

The original design is Orbit by Xiaoying Riley / 3rd Wave Media, adapted through the online-cv Jekyll template. The original SCSS identifies the Creative Commons Attribution 3.0 license; visible attribution is retained in the footer. Vendored assets retain their own licenses.
