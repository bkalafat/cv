"""Regression checks for Unicode, XML escaping, and multi-page content loss."""

import copy
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from pypdf import PdfReader
from cv_data import load_cv
from cv_pdf import generate_cv
from validate_cv import validate_pdf


class PDFRegressionTests(unittest.TestCase):
    def test_long_role_preserves_every_bullet_and_unicode(self):
        data = copy.deepcopy(load_cv())
        data["experiences"]["info"][0]["bullets"] = [
            f"Regression {index:03}: Şişli, Türkiye, VakıfBank; C# & Java; x < y > z. "
            + "Long engineering context requiring reliable wrapping. " * 5
            for index in range(45)
        ]
        with tempfile.TemporaryDirectory() as temporary:
            for variant in ("ats", "professional"):
                with self.subTest(variant=variant):
                    path = generate_cv(variant, data=data, output_path=Path(temporary) / f"{variant}.pdf")
                    validate_pdf(path, data, max_pages=20)
                    text = " ".join(page.extract_text() for page in PdfReader(path).pages)
                    self.assertEqual(text.count("Regression"), 45)
                    self.assertIn("Şişli", text)


if __name__ == "__main__":
    unittest.main()
