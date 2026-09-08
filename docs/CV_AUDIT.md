# CV audit and editorial record

Audit date: September 8, 2026. The initial audit was delivered before repository edits.

## Initial findings

| Area | Finding and consequence |
| --- | --- |
| Career narrative | Banking modernization, architecture, and mentoring were the strongest evidence, obscured by repetitive promotional language. |
| Role fit | Senior Backend Engineer and .NET Technical Lead were supported. Staff/Software Architect applications would benefit from cross-team scope and decision ownership; Principal-level organization-wide ownership was not established. |
| Missing information | Team sizes, production scale, architecture tradeoffs, operational ownership, and specific insightsoftware contributions were absent. |
| Accuracy and age | Role titles conflicted across YAML and LaTeX. Modernization timelines disagreed. VakıfBank/TÜBİTAK dates overlapped. Older technology versions are historical experience, not evidence of current platform expertise. |
| Duplicate data | The website used data.yml, while both PDFs mixed it with experience.yml and education.yml. projects.yml actually contained training. |
| Data flow | Scripts hard-coded skills and omitted bullets, summary paragraphs, training, and projects. The workflow did not run either PDF generator. |
| ATS | Extracted PDFs contained replacement characters, broken Turkish employer names, a missing phone +, and fragmented word order. Some professional PDF skills had no source evidence. |
| Visual/UX | Skill percentages implied unsupported precision. Title/date positioning could overlap, pale text reduced contrast, and fixed download buttons competed with content. |
| SEO and links | The SEO plugin was configured but not invoked. robots.txt pointed at the old domain. Credential links incorrectly prepended // to https URLs. |
| Build/deployment | downloads/ was excluded. Ruby 2.7 was obsolete, fonts depended on Windows, dependencies were not locked, and pull requests were not excluded from deployment. |
| Claims/evidence | Absolute claims about hallucinations, scope drift, compliance, and air-gapped AI operation were not substantiated. Published DiffPilot details differed from the CV. |
| Content allocation | The project section was not rendered, training was described as certification, older experience was repetitive, and archived LaTeX instructions referenced missing generators. |

## Owner corrections applied

- Use nearly 14 years of experience, including the part-time role beginning December 2012.
- The final recruiter pass uses concise experience bullets, full profile URLs in ATS output, standard headings, and no duplicated per-role technology lists. See RECRUITER_REVIEW.md for the complete evidence review.

- Remove DiffPilot from the CV, including its product and compliance claims.
- Remove delivery/performance metrics and promotional Copilot adoption claims. Keep factual modernization, architecture, engineering tools, and technical responsibilities.
- VakıfBank ended January 15, 2017; TÜBİTAK began around January 15, 2017. Published chronology uses January 2017 for both sides of this transition.
- Add **Microsoft Certified: Azure AI Engineer Associate**, earned March 6, 2026, expiring March 6, 2027. The owner supplied the expiry time as 02:59 UTC+03:00; the CV uses date precision.
- Use the supplied Microsoft certification overview URL, labeled as an overview (AI-102), not as personal credential verification.

## Implemented strategy

All published factual content now lives in _data/data.yml. The duplicate experience, education, and training files were removed after consolidation. The website and both PDFs use the same summary, skills, employment bullets with relevant technologies, education, credentials, languages, and interests. The exact website URL is shared with the site configuration and checked by validation.

The headline targets senior backend/.NET work and technical leadership. Historical job titles remain factual rather than being upgraded to Staff or Principal. Recent banking architecture and modernization lead the narrative; early Java, .NET, and part-time roles preserve career progression. Skills use searchable categories, with AWS/microservices/containerization/React training separated from production expertise. No new cloud-operating experience is inferred from the AI-102 credential.

Both PDF entry points use shared flow-based pagination and bundled Unicode fonts. All published content is retained without bullet/credential count caps. The professional format uses navy accents; the ATS format uses a plain single column. Both have selectable text and full clickable contact information. Certification titles, issue/expiry dates, and overview labels are shared with the website.

The website has semantic headings and landmarks, a keyboard skip link, visible focus, flexible role/date layout, mobile contact wrapping, readable contrast, and print rules. Download links point to same-build PDFs. SEO metadata, canonical URL, and sitemap origin are now emitted correctly. The broken unused browser PDF path was removed.

The build uses explicit Jekyll dependencies, supported Ruby, a committed dependency lockfile, and pinned Python packages. CI generates PDFs before Jekyll, checks parity before publishing, and limits deployment privileges to the default-branch deploy job. Archived documents, tooling, and unused third-party assets are excluded from the deployed site.

## Preservation and exclusions

- All six employers, client assignments, supplied role dates (with the owner correction), education, and relevant engineering technologies remain.
- Education month/year dates and February dates for Udemy/Udacity training were retained from the former auxiliary YAML files.
- Training course titles and providers remain; their promotional descriptions were condensed. React is retained as training, not removed.
- Interests and languages remain across all three surfaces. IELTS Band 7 is dated 2023, without implying a current test validity period.
- The IELTS reference number was removed from the public CV; it is retained in Git history. It is not necessary for recruiting or proof of identity.
- Unsupported hard-coded PDF skills (including Kubernetes, gRPC, CQRS/event sourcing, DDD, and claimed Azure cloud expertise) were removed. Windows/legacy technologies with an employment basis remain.
- Earlier LaTeX experiments remain explicitly archived and excluded from Jekyll. They preserve history, contain superseded facts, and must not be submitted as current CVs.

## Facts still needing confirmation

1. Whether Innovance is still current and the exact contractual title. May 2024 - Present and the original main-site role title were retained.
2. Exact titles at insightsoftware and OBSS; the original main-site titles were retained rather than using conflicting archive labels.
3. A personal Microsoft credential verification URL, if desired. The supplied link describes the certification, not the holder's credential.
4. Specific insightsoftware product/features and engineering ownership, plus concrete architecture decisions, team scope, production operations, and remote collaboration practices for future Staff/Architect applications.
5. Playwright E2E experience is carried forward from the original skills data; a project example would strengthen it. No proficiency score is retained.

The removed numerical metrics and DiffPilot details no longer need confirmation for this CV.

## Reference checks

- [DiffPilot Marketplace](https://marketplace.visualstudio.com/items?itemName=BurakKalafat.diffpilot) and its linked source contradicted the original .NET/tool-count claims; the product was subsequently removed at the owner's request.
- [Ruby maintenance branches](https://www.ruby-lang.org/en/downloads/branches/) confirm Ruby 2.7 is unsupported.
- [Jekyll GitHub Actions documentation](https://jekyllrb.com/docs/continuous-integration/github-actions/) supports building Jekyll with explicit dependencies and publishing through the Actions Pages source.
- [Jekyll Windows setup](https://jekyllrb.com/docs/installation/windows/) documents the native Devkit requirement.

Validation results and the final changed-file inventory are recorded in VALIDATION.md after output review.
