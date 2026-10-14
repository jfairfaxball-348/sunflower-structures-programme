"""Regression cases for the symbolic spoke-shift obstruction."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from spoke_shift_audit import check_grid, pass_lex, spoke, star


class SpokeShiftAuditTests(unittest.TestCase):
    def test_general_grid(self):
        self.assertEqual(check_grid(), (22, 19))

    def test_binary_small_examples(self):
        for k in range(2, 7):
            self.assertEqual(pass_lex(spoke(2, k), 2*k), star(2, k))

    def test_sparse_family_tiny_case(self):
        self.assertEqual(pass_lex(spoke(2, 2), 4),
                         frozenset(map(frozenset, ((1, 2), (1, 3), (1, 4)))))


if __name__ == "__main__":
    unittest.main()
