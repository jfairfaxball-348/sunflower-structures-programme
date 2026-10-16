"""Original-owner physical-core stability: independent exact witness assertions."""
import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from original_core_stability_matching_audit import (
    analyze, audit, correlated_family, q_product, two_disjoint_triangles,
    max_matching_with_cover
)


class OriginalCoreStabilityTests(unittest.TestCase):
    def test_entire_audit(self):
        self.assertEqual(len(audit()), 4)

    def test_exact_turan_triangles(self):
        d = analyze(two_disjoint_triangles())
        self.assertEqual((d["delta"], d["leftover"], d["bad"]), (0, 0, 0))
        self.assertEqual(d["retained"], 6)

    def test_correlated_rank_and_fraction(self):
        d = analyze(sum(correlated_family(2, 3, 2), ()))
        self.assertEqual((d["rank"], d["r"], d["delta"]), (6, 24, Fraction(48)))
        self.assertEqual((d["matching"], d["retained"]), (4, 12))

    def test_large_deficit_product(self):
        self.assertEqual(analyze(q_product(2, 3))["e"], 4)

    def test_konig_unequal(self):
        n, la, lb = max_matching_with_cover([0,1,2], [3,4], {(0,3),(1,3),(2,4)})
        self.assertEqual(n, 2)
        self.assertEqual(len(la)+len(lb), 2)


if __name__ == "__main__":
    unittest.main()
