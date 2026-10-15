"""Independent exact rational tests of NW1-NW9 nested ORIGINAL shell packet theorem."""
import unittest
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from nested_original_wreath_audit import (
    audit, original_nested_wreath, sunflower_witness,
    symbolic_shell_cost, exhaustive_shell_cost,
)


class NestedOriginalWreathTests(unittest.TestCase):
    def test_audit_all_original_and_exact_cover(self):
        audit()

    def test_nested_physical_shells_are_distinct(self):
        shells, edges = original_nested_wreath((3, 3), 2, 1)
        self.assertEqual(len(shells), 9)
        self.assertEqual(len(edges), 18)
        self.assertEqual(len(set(edges)), 18)
        self.assertEqual({len(e) for e in edges}, {5})
        for leaf, shell in shells.items():
            self.assertEqual(len(shell), 4)
            self.assertTrue(all(shell <= e for e in edges
                if ("private", leaf, 0, 0) in e or ("private", leaf, 0, 1) in e))
        self.assertIsNone(sunflower_witness(edges, 3))

    def test_level_two_exact_rational_minimum(self):
        for C, expected in ((2, Fraction(9, 16)), (3, Fraction(1, 9))):
            self.assertEqual(exhaustive_shell_cost((3, 3), C)[0], expected)
            self.assertEqual(symbolic_shell_cost((3, 3), C)[0], expected)

    def test_rank_entropy_multiplicativity(self):
        for t in range(1, 9):
            self.assertEqual(symbolic_shell_cost((3,) * t, 2)[0],
                             Fraction(3, 4)**t)
            self.assertEqual(3**t * 3**t, 9**t)
            self.assertGreater(9**t, 2**(3*t))
            self.assertGreater(3**t, 2**t)

    def test_conditional_original_pair_intersections(self):
        shells, edges = original_nested_wreath((3, 3), 2, 1)
        # Pick one original owner in each of four distinct ordered leaf roles:
        # outer 0/1 pairs meet exactly in the unique outer physical point.
        e01 = next(e for e in edges if ("private", (0, 1), 0, 0) in e)
        e12 = next(e for e in edges if ("private", (1, 2), 0, 0) in e)
        self.assertEqual(e01 & e12, {("shell", (), 0, 1)})
        e00 = next(e for e in edges if ("private", (0, 0), 0, 0) in e)
        e02 = next(e for e in edges if ("private", (0, 2), 0, 0) in e)
        self.assertEqual(e00 & e02, {
            ("shell", (), 0, 1), ("shell", (), 0, 2),
            ("shell", (0,), 0, 2)
        })
        self.assertIsNone(sunflower_witness(edges, 3))


if __name__ == "__main__":
    unittest.main()
