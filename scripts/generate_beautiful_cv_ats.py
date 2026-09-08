"""Generate the single-column ATS CV from the canonical YAML content."""
from cv_pdf import generate_cv


def generate_ats_cv():
    return generate_cv("ats")


if __name__ == "__main__":
    generate_ats_cv()
