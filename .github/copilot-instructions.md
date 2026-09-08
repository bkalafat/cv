# CV project conventions

- Preserve the existing Jekyll architecture and GitHub Pages deployment.
- Edit published CV content only in `_data/data.yml`. All HTML and PDF surfaces consume it.
- Use UTF-8, two-space YAML indentation, and plain text content. Quote the international phone number.
- Preserve factual dates and role titles. Do not invent outcomes, technologies, credentials, or levels of responsibility.
- Do not restore DiffPilot, numerical performance/delivery claims, or Copilot promotion; the owner requested their removal.
- Training must be labeled as training. Certification overview links are not personal verification links.
- Shared ReportLab layout lives in `scripts/cv_pdf.py`; the two existing generator scripts remain entry points.
- Bundle fonts from `assets/fonts/`; never rely on Windows-only fonts or silently fall back to fonts that lose Turkish characters.
- Keep both current PDFs to two readable pages and inspect page images after layout changes.
- Run the validation commands in README.md, including Jekyll build, both generators, output parity, and pagination regression tests.
- `docs/latex-cv/` is archived, excluded from publishing, and not synchronized.
- The site uses `https://cv.bkalafat.com` with an empty baseurl. Local preview is `http://localhost:4000`.
