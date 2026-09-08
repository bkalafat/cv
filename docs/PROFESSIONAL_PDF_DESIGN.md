# Professional PDF design

The recruiter PDF uses a separate editorial renderer in `scripts/cv_professional.py`.
The ATS renderer retains its plain, single-column structure.

The subsequent banking and enterprise AI rewrite uses the owner's latest career
context: 14+ years, Akbank payment/EOD/batch modernisation, enterprise Copilot plugin
development for the Architecture organisation, messaging, containers and DDD.
The website, professional PDF, ATS PDF and plain-text companion share this content.
Official employment titles and dates remain intact. New technology skills are
listed without inventing project-specific deployments, scale or measured gains.
The two-page English resume targets international remote and relocation opportunities.

[Prospects' UK CV guidance](https://www.prospects.ac.uk/careers-advice/cvs-and-cover-letters/how-to-write-a-cv/)
and the [National Careers Service](https://nationalcareers.service.gov.uk/careers-advice/cv-sections)
informed the concise profile, relevant skills, clear chronology and two-page length.

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
