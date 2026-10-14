"""Direct single-repo mathematical sanity tests. Historical portfolio tests retired."""
import json
import sys
import unittest
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate
from shift_sanity import shift, fully_shift, has_sunflower, coordinate_product


class BridgeResearchTests(unittest.TestCase):
    def test_live_programme(self):
        validate.main()
        state = json.loads((ROOT / "authoritative/STATE.json").read_text())
        self.assertFalse(state["full_conjecture_proved"])
        self.assertFalse(state["legacy_hierarchy_active"])
        self.assertEqual(state["active_next_prompt"], "sessions/NEXT_SESSION.md")

    def test_one_shift_creates_sunflower_not_in_original(self):
        f = frozenset(map(frozenset, ({2, 3}, {1, 4}, {1, 5})))
        self.assertFalse(has_sunflower(f, 3))
        g = shift(f, 1, 2)
        self.assertTrue(has_sunflower(g, 3))
        self.assertEqual(len(f), len(g))

    def test_two_element_changes_in_singleton_full_shift(self):
        f = frozenset((frozenset({3, 4}),))
        g = fully_shift(f, 4)
        self.assertEqual(g, frozenset((frozenset({1, 2}),)))
        self.assertEqual(len(next(iter(f)) ^ next(iter(g))), 4)

    def test_product_obstruction_four_petals(self):
        for k in range(1, 4):
            f = coordinate_product(3, k)
            self.assertEqual(len(f), 3**k)
            self.assertFalse(has_sunflower(f, 4))

    def test_v1_universal_numerical_claim_impossible(self):
        self.assertGreater(3**1000, 48**94 * 2**1000)

    def test_source_versions_and_active_prompt(self):
        sources = (ROOT / "research/SOURCE_REGISTER.md").read_text()
        for version in ("v1", "v2"):
            self.assertIn("2606.02667" + version, sources)
        prompt = (ROOT / "sessions/NEXT_SESSION.md").read_text()
        self.assertIn("BUILD THE MISHRA", prompt)
        self.assertIn("NO", prompt)  # explicit negative controls


if __name__ == "__main__":
    unittest.main()
