import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from original_pair_budget_audit import (product_family, cap9, defects, certificates,
    covered_by, verify_binary_fractional_certificates, enumerate_no_sunflower,
    solve_optional_lp, averaged_factor_pair_spectrum, audit_published_factors)

class OriginalPairBudgetTests(unittest.TestCase):
    def test_binary_primal_dual_exact(self):
        for m in (2, 3, 4):
            _, N, _, lo, hi = verify_binary_fractional_certificates(m)
            self.assertEqual(lo, Fraction((N-1)*(N-2), 3))
            self.assertEqual(hi, Fraction(N*(N-m-1), 2))
    def test_rank_one_two_three(self):
        for s in (3, 4, 5):
            self.assertTrue(enumerate_no_sunflower(product_family(s-1, 1), s))
            self.assertTrue(enumerate_no_sunflower(product_family(s-1, 2), s))
        self.assertTrue(enumerate_no_sunflower(product_family(2, 3), 3))
        self.assertTrue(enumerate_no_sunflower(cap9(), 3))
        self.assertEqual(len(cap9()), 9)
        self.assertGreater(len(cap9()), 2**3)
    def test_true_sunflower_rejected(self):
        self.assertFalse(enumerate_no_sunflower(((0,0),(1,1),(2,2)), 3))
        self.assertEqual(defects(((0,0),(1,1),(2,2))), ())
    def test_covers_and_does_not_charge_common_hub(self):
        fam=((0,0,0),(0,0,1),(0,1,0))
        self.assertTrue(covered_by(fam, (1,0,1), (0,1,2)))
        self.assertFalse(covered_by(fam, (0,0,1), (0,1,2)))
    def test_published_factor_averaged_spectra(self):
        spectra = audit_published_factors()
        if spectra is not None:
            self.assertEqual(spectra[0][2], 1188)
            self.assertEqual(spectra[1][1], {4: 1, 5: 10, 27: 15})
    def test_optional_small_lp(self):
        ans=solve_optional_lp(product_family(2,3), 3)
        if ans is not None:
            self.assertAlmostEqual(ans, 16)
            self.assertAlmostEqual(solve_optional_lp(cap9(),3), 20)
            self.assertAlmostEqual(solve_optional_lp(product_family(3,2),4), 9)

if __name__ == '__main__':
    unittest.main()
