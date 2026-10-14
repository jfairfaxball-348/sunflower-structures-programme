"""Independent regressions for cited high-rank sunflower-free tensor factors."""
import sys
import unittest
from collections import Counter
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from high_rank_tensor_audit import (
    factor54, factor39, shadows, has_sunflower, anchored_tensor, check_grid
)
from spoke_shift_audit import pass_lex


class HighRankTensorTests(unittest.TestCase):
    def test_rank_four_54_exact_shadow_saturation(self):
        F, n = factor54()
        self.assertEqual((len(F), n), (54, 18))
        self.assertFalse(has_sunflower(F, 3))
        shadow = shadows(F)
        self.assertEqual((len(shadow), set(shadow.values())), (108, {2}))
        self.assertEqual(max(sum(x in e for e in F) for x in range(n)), 12)
        self.assertEqual(4*len(F), 2*len(shadow))

    def test_rank_three_39_link_and_shadow_profiles(self):
        F, n = factor39()
        self.assertEqual((len(F), n), (39, 13))
        self.assertFalse(has_sunflower(F, 4))
        self.assertEqual(Counter(shadows(F).values()), {1: 27, 2: 18, 3: 18})
        self.assertEqual(max(sum(x in e for e in F) for x in range(n)), 9)

    def test_anchored_original_spokes(self):
        for s in (3, 4):
            T, _ = anchored_tensor(s, 2)
            K = (4 if s == 3 else 3)*2
            B = frozenset(range(1, K+1))
            self.assertIn(B, T)
            distinct_high = {
                next(iter(e-B)) for e in T
                if len(e-B) == 1 and len(B-e) == 1
            }
            self.assertGreaterEqual(len(distinct_high), 2*(2 if s == 3 else 1))

    def test_full_lex_audit_and_tensor_shadow_formula(self):
        self.assertIn("PASS", check_grid())


if __name__ == "__main__":
    unittest.main()
