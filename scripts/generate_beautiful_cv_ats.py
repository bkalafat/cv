"""Generate the single-column ATS CV from the canonical YAML content."""
from cv_pdf import generate_cv
from cv_text import generate_ats_text


def generate_ats_cv():
    result = generate_cv("ats")
    generate_ats_text()
    return result


if __name__ == "__main__":
    generate_ats_cv()
