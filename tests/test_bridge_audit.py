"""Independent finite diagnostics for bridge notebook assertions."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from bridge_audit import (audit_layers, audit_product_subfamilies,
                          audit_sharpness, audit_pair_private,
                          experimental_shifted_stars)


class MishraBridgeAuditTests(unittest.TestCase):
    def test_exhaustive_small_shadows_and_one_shifts(self):
        self.assertEqual(audit_layers(), (2048, 32))

    def test_product_has_no_large_shifted_original_subfamily(self):
        self.assertEqual(audit_product_subfamilies(), (15, 3840, 2))

    def test_sharp_single_shift_and_sparse_link(self):
        self.assertEqual(audit_sharpness(), (4, 8))
        self.assertEqual(audit_pair_private(), 6)

    def test_product_full_shift_stars_finite_only(self):
        self.assertEqual(experimental_shifted_stars(), (2, 8))


if __name__ == "__main__":
    unittest.main()
