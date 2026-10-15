"""Regression tests for the triangle-tensor prevalence obstruction (finite only)."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from triangle_tensor_prevalence_audit import check_h54_spectrum, check_q_exact_traces, q_count_formula

class TriangleTensorPrevalenceTests(unittest.TestCase):
    def test_54_intersection_histogram(self):
        self.assertIn("PASS",check_h54_spectrum())
    def test_q_product_trace_formula(self):
        self.assertIn("PASS",check_q_exact_traces())
        self.assertEqual(q_count_formula(2,8,1),2)
        self.assertEqual(q_count_formula(5,8,1),2*4**8)

if __name__=="__main__":
    unittest.main()
