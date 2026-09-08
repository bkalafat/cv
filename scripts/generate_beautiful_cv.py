"""Generate the professional CV from the canonical YAML content."""
from cv_pdf import generate_cv


def generate_modern_cv():
    return generate_cv("professional")


if __name__ == "__main__":
    generate_modern_cv()
