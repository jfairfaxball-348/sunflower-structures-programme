"""Finite diagnostics for original multiwitness trace rank reduction."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from compatible_trace_audit import (check_sharpness, check_multiwitness,
                                    check_published_obstruction, check_overlap, sharp_family)

class CompatibleTraceTests(unittest.TestCase):
    def test_sharp_families(self):
        self.assertIn("PASS",check_sharpness())
        for s in range(3,7):
            members,_,_,_=sharp_family(s,s-2)
            self.assertEqual(len(members),2*s-2)
    def test_two_point_outside_witnesses(self):
        self.assertIn("PASS",check_multiwitness())
    def test_intersecting_requirement_is_essential(self):
        self.assertIn("PASS",check_published_obstruction())
    def test_overlap_polynomial(self):
        self.assertIn("PASS",check_overlap())

if __name__=="__main__":
    unittest.main()
