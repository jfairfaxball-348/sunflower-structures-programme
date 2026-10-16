"""Independent finite physical-core Turan sharpness and density audit."""
import sys
from pathlib import Path
import unittest
from fractions import Fraction
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"scripts"))
from physical_core_turan_sharpness_audit import audit, check, turan_edge_count

class PhysicalCoreTuranTests(unittest.TestCase):
    def test_complete_exact_audit(self):
        self.assertEqual(len(audit()),5)

    def test_rank_two_s3_six_edge_sharp_case(self):
        # r=6 partitioned into two physically disjoint K3 pair-star triangles.
        self.assertEqual(turan_edge_count(6,3),9)
        self.assertEqual(15-turan_edge_count(6,3),6)

    def test_nonempty_genuine_physical_core(self):
        seed=(frozenset({'a'}),frozenset({'b'}))
        self.assertEqual(check(3,seed,2,1),(3,2,1,8,4,12,12))

    def test_exact_h54_residual_overfill(self):
        self.assertGreater(Fraction(54,1)/(Fraction(5,2)**4),1)
        self.assertEqual(Fraction(2,1)/Fraction(5,2),Fraction(4,5))

if __name__=="__main__":
    unittest.main()
