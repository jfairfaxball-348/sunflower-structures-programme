"""Independent ORIGINAL record enumeration for the complete-pair-star theorem."""
import sys
import unittest
from itertools import combinations
from math import comb
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import original_pair_star_quadratic_audit as A
from original_nonproduct_tensor_lp_audit import rectangle_records


class OriginalPairStarQuadraticTest(unittest.TestCase):
    def test_full_exact_audit(self):
        A.audit()

    def test_independent_all_anchor_enumerator(self):
        for s in (3, 4):
            for n in range(s + 1, 9):
                F = A.family(n)
                independent = []
                for i, anchor in enumerate(F):
                    for J in combinations((j for j in range(n) if j != i), s):
                        traces = [anchor & F[j] for j in J]
                        if not all(t and len(t) == len(traces[0]) for t in traces):
                            continue
                        if len({u & v for u, v in combinations(traces, 2)}) != 1:
                            continue
                        petals = [F[j] for j in J]
                        defect = frozenset(
                            x for x in set().union(*petals)
                            if 2 <= sum(x in p for p in petals) < s
                        )
                        self.assertFalse(defect & anchor)
                        if defect:
                            independent.append((i, J, defect))
                actual = set(A.records(F, s))
                self.assertEqual(set(independent), actual)
                self.assertEqual(len(actual), (n - s) * comb(n, s))
                # Independently check the repository's general original enumerator.
                universal = {
                    (F.index(anchor), tuple(sorted(F.index(p) for p in petals)), D)
                    for anchor, petals, D in rectangle_records(F, s=s)
                }
                canonical = {(i, tuple(sorted(J)), D) for i, J, D in actual}
                self.assertEqual(universal, canonical)

    def test_exact_degree_and_primitive_obstruction(self):
        for n in (5, 7, 11):
            F = A.family(n)
            for s in (3, 4):
                R = tuple(A.records(F, s))
                assert n >= s + 1
                self.assertEqual(len(R), (n - s) * comb(n, s))
                degrees = {
                    x: sum(x in e for e in F)
                    for x in set().union(*F)
                }
                self.assertEqual(set(degrees.values()), {2})
                self.assertEqual(max(degrees.values()) / len(F), 2 / n)


if __name__ == "__main__":
    unittest.main()
