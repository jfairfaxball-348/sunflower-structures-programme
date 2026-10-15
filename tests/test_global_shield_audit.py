"""Tests for exact global original multishield certificate calculations."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import global_shield_audit as G


class GlobalShieldAudit(unittest.TestCase):
    def test_rank_below_s_has_no_equal_rank_trace_sunflower(self):
        for k in (0,1,2):
            self.assertFalse(G.all_global_defects(3,k))

    def test_small_exact_all_anchor_orig_products(self):
        for k,number in ((3,8),(4,32)):
            with self.subTest(k=k):
                sets=G.all_global_defects(3,k)
                self.assertEqual(len(sets),number)
                self.assertEqual(min(map(len,sets)),3)

    def test_original_tight_tuple_all_s_and_private_t(self):
        for s,t in ((3,1),(3,2),(4,1),(4,2),(5,1),(6,1)):
            for k in (s*t,s*t+2):
                with self.subTest(s=s,k=k,t=t):
                    a,es=G.tight_original_tuple(s,k,t)
                    self.assertEqual(len(G.defects(es,s)),s*t)
                    self.assertNotIn(a,es)

    def test_actual_edge_ownership_cross_anchor(self):
        for s,k in ((3,3),(3,5),(4,4),(4,8),(5,5)):
            with self.subTest(s=s,k=k):
                n,b,count=G.count_owner_reuse(s,k)
                self.assertEqual(n,(s-1)**k)
                self.assertEqual(count,s*b)

    def test_global_uniform_primal_tightness(self):
        for k in (3,4):
            sets=G.all_global_defects(3,k)
            self.assertTrue(all(len(ds)/3 >= 1 for ds in sets))
            self.assertTrue(any(len(ds) == 3 for ds in sets))
            self.assertEqual(2*k/3, (3-1)*k/3)


if __name__ == "__main__":
    unittest.main()
