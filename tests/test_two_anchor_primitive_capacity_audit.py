import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from two_anchor_primitive_capacity_audit import (
    audit,product_family,triangle_lift,trace_three_rows,
    canonical_two_cover,sunflower_free,cover_number_at_most_one,vc_witness
)
class TwoAnchorPrimitiveCapacityTests(unittest.TestCase):
    def test_full_audit(self):
        self.assertEqual(len(audit()),6)
    def test_exact_rows(self):
        F=triangle_lift(product_family(2,2))
        x,y=('triangle','a'),('triangle','b')
        self.assertEqual(tuple(map(len,trace_three_rows(F,x,y))),(4,4,4))
        a,b=canonical_two_cover(F,x,y)
        self.assertEqual((len(a),len(b)),(8,4))
        self.assertTrue(sunflower_free(a,3))
        self.assertTrue(sunflower_free(b,3))
    def test_rank_zero_triangle(self):
        F=triangle_lift((frozenset(),))
        self.assertEqual((len(F),len(F[0])),(3,2))
        self.assertFalse(cover_number_at_most_one(F))
    def test_six_petals(self):
        F=triangle_lift(product_family(5,1))
        self.assertEqual((len(F),len(F[0])),(15,3))
        self.assertTrue(sunflower_free(F,6))
    def test_shattering_at_linear_rank(self):
        self.assertEqual(len(vc_witness(product_family(2,4),2,4)),4)
    def test_nonintersecting_private_seed(self):
        H=tuple(map(frozenset,((0,1),(1,2),(0,2),(3,4),(4,5),(3,5))))
        self.assertTrue(sunflower_free(triangle_lift(H),3))
if __name__=="__main__":unittest.main()
