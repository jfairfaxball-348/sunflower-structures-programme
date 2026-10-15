"""Independent unittests for original partial-multiplicity certificates."""
import sys
import unittest
from fractions import Fraction
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from partial_multiplicity_audit import (
    all_small_three_free,compulsory_hub_not_a_defect,central_lp,h54,moments
)

class PartialMultiplicityTests(unittest.TestCase):
    def test_exhaustive_original_families(self):
        self.assertEqual(all_small_three_free(),(387,420,840))
    def test_hub_obstruction(self):
        self.assertTrue(compulsory_hub_not_a_defect())
    def test_central_dual_three(self):
        self.assertEqual(central_lp(3,7,3)[-1],Fraction(7,3))
    def test_general_s_central_dual(self):
        for s,m,r in ((4,6,2),(5,8,3),(6,7,2)):
            self.assertEqual(central_lp(s,m,r)[-1],Fraction(m,s))
    def test_54_moment(self):
        self.assertEqual(len(h54()),54)
        self.assertEqual(moments(),Fraction(56,27))

if __name__=="__main__":unittest.main()
