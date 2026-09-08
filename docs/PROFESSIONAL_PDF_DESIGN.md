# Professional PDF design

The recruiter PDF uses a separate editorial renderer in `scripts/cv_professional.py`.
The ATS renderer and canonical career facts are unchanged.

Design decisions:

- Navy masthead, large name, teal hierarchy, and white contact text establish a clear entry point.
- Ten-point experience text and restrained spacing keep the career history readable.
- The three recent roles appear on page one; earlier roles continue on page two.
- A pale two-column technical skills panel groups supporting expertise for scanning.
- Credentials retain their names, dates, classification, and clickable source links.
- Text remains selectable, fonts are embedded, and oversized experience blocks can paginate.

Research: [Harvard's resume guidance](https://cdn-careerservices.fas.harvard.edu/wp-content/uploads/sites/161/2024/10/2024-HES_resume-and-letter.pdf)
informed consistent hierarchy, whitespace, reverse chronology, and checking the exported PDF.
The palette and masthead are design choices for the human-facing version.

Validation: rendered and visually inspected both final pages; checked complete source
text, chronological extraction, Unicode, page bounds, and hyperlinks. The existing
45-bullet stress test passes for both renderers. The normal professional PDF is two pages.
