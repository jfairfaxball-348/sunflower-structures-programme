"""Independent finite verification of original cross-core collision obstruction."""
from fractions import Fraction
from pathlib import Path
import sys
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from coupled_cross_core_audit import family,exact_case,audit

class CoupledCrossCoreTests(unittest.TestCase):
    def test_all_cases(self):
        self.assertEqual(len(audit()),4)
    def test_genuine_shared_index_point(self):
        g,h=family(2,3,1)
        self.assertEqual(g[0]&h[0],frozenset({('y',0)}))
        self.assertEqual(g[0]&h[2],frozenset())
    def test_four_petals(self):
        self.assertEqual(exact_case(3,3,1)[-1],Fraction(8,9))
    def test_exact_deficit(self):
        self.assertEqual(exact_case(2,4,1)[-2],16)

if __name__=="__main__":
    unittest.main()
