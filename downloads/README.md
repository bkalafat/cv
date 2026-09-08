# CV downloads

- `Burak_Kalafat_Professional_CV.pdf`: two-page professional layout with navy accents.
- `Burak_Kalafat_ATS_CV.pdf`: two-page, plain single-column layout.

The ATS entry point also generates `Burak_Kalafat_ATS_CV.txt`, a UTF-8 plain-text companion.

All versions contain the same CV content from `_data/data.yml`, with selectable Unicode text. PDFs have clickable contact links; the text companion contains full visible URLs.

Regenerate using the two entry points in `scripts/`. GitHub Actions regenerates the deployed PDFs on each build and provides a `cv-pdfs` artifact. It does not commit generated files back to the repository.

Live downloads:
- [Professional CV](https://cv.bkalafat.com/downloads/Burak_Kalafat_Professional_CV.pdf)
- [ATS CV](https://cv.bkalafat.com/downloads/Burak_Kalafat_ATS_CV.pdf)
