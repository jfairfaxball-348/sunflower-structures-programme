"""Regression assertions for exact cross-trace original-witness diagnostics."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from cross_trace_entropy_audit import (cross_exhaustive, explicit_obstructions,
                                       scalar_normalisation, averaged_153,
                                       h54, cross_certificates, flower)
class CrossTraceEntropyTests(unittest.TestCase):
    def test_all_original_rank_three_families(self):
        self.assertIn("387",cross_exhaustive())
    def test_original_counterexamples(self):
        self.assertIn("PASS",explicit_obstructions())
    def test_scalar_lp(self):
        self.assertIn("PASS",scalar_normalisation())
    def test_averaged_153_only(self):
        self.assertIn("non-regular",averaged_153())
    def test_54_anchor(self):
        self.assertEqual(len(h54()),54)
    def test_vacuous_trace_triple(self):
        self.assertEqual(cross_certificates([frozenset({0,1})]),(0,0,0))
if __name__=="__main__": unittest.main()
