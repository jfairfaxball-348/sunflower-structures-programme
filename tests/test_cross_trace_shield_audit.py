"""Standalone finite tests for original cross-trace shields and VC obstruction."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from cross_trace_shield_audit import (
    all_small, seed_audit, tensor_shield, vc_audit, seed, cap9,
    packets, sunflower
)


class TestCrossTraceShield(unittest.TestCase):
    def test_all_small(self):
        self.assertEqual(all_small(), 387)

    def test_seed_all_s(self):
        self.assertTrue(seed_audit())

    def test_cap9_tensor(self):
        self.assertEqual(tensor_shield(), 4)

    def test_vc(self):
        self.assertTrue(vc_audit())

    def test_three_trace_counterexample(self):
        f = seed(3)
        self.assertTrue(sunflower(tuple(frozenset({("e", i)}) for i in range(3))))
        self.assertFalse(sunflower(f[1:]))
        self.assertEqual(max(len(v) for v in packets(cap9(), cap9()[0]).values()), 4)


if __name__ == "__main__":
    unittest.main()
