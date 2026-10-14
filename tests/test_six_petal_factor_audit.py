"""Finite checks supplement, but never prove, infinite-rank arguments."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from six_petal_factor_audit import (
    factor153,pair_codegrees,matching_number_graph,
    check_factor,check_intersecting_tensor_certificate,check_one_block_shift
)


class SixPetalFactorTests(unittest.TestCase):
    def test_exact_factor_and_shadow(self):
        self.assertIn("PASS",check_factor())
        H,J,P=factor153()
        self.assertEqual((len(H),len(J),len(P)),(126,27,153))
        self.assertEqual(sum(pair_codegrees(P).values()),459)

    def test_every_vertex_link_and_intersecting_restriction(self):
        _,_,P=factor153()
        for v in range(26):
            graph={frozenset(e-{v}) for e in P if v in e}
            self.assertLessEqual(matching_number_graph(graph),5)
        self.assertIn("PASS",check_intersecting_tensor_certificate())

    def test_complete_one_block_shift(self):
        self.assertIn("PASS",check_one_block_shift())


if __name__=="__main__":
    unittest.main()
