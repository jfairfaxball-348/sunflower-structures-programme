"""Independent original all-physical anchors and s-way compatibility tests."""
import unittest
from fractions import Fraction
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from all_physical_wreath_compatibility_audit import (
    all_physical_formula, exhaustive_all_physical, audit,
)


class AllPhysicalWreathCompatibilityTests(unittest.TestCase):
    def test_complete_audit(self):
        audit()

    def test_private_suffix_changes_true_physical_optimum(self):
        self.assertEqual(all_physical_formula((3, 3), 2, 1, 3)[0],
                         Fraction(2, 27))
        self.assertNotEqual(all_physical_formula((3, 3), 2, 1, 3)[0],
                            Fraction(1, 9))

    def test_all_private_anchors_preserve_base_two_barrier(self):
        for depth in range(1, 8):
            self.assertEqual(all_physical_formula((3,) * depth, 3, depth, 2)[0],
                             Fraction(3, 4)**depth)

    def test_actual_owners_exhaustive_not_shell_only(self):
        value, supports, edges = exhaustive_all_physical((3, 3), 2, 1, 3)
        self.assertEqual(value, Fraction(2, 27))
        self.assertEqual(edges, 18)
        self.assertGreater(supports, 9)


if __name__ == "__main__":
    unittest.main()
