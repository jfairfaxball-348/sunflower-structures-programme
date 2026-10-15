"""Finite independent checks for research/CENTRAL_TRACE_AMORTISATION.md."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from central_trace_amortisation_audit import check_traces,check_fractional,check_factors,fubini,q_spectrum
class CentralTraceAuditTests(unittest.TestCase):
    def test_traces(self): self.assertIn("PASS",check_traces())
    def test_fractional(self): self.assertIn("PASS",check_fractional())
    def test_factors(self): self.assertIn("PASS",check_factors())
    def test_exact_coefficients(self):
        self.assertEqual(fubini(4),[1,1,3,13,75])
        self.assertEqual(q_spectrum(2,2),[0,2,5,4,1])
if __name__=="__main__": unittest.main()
