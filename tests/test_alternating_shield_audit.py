"""Independent finite tests for alternating original sunflower-free shields."""
import sys
import unittest
from itertools import combinations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import alternating_shield_audit as AS


class AlternatingShieldAudit(unittest.TestCase):
    def test_all_small_original_seeds(self):
        for s in range(3, 10):
            with self.subTest(s=s):
                self.assertEqual(AS.audit_seed(s), (s + 2)*(s + 1)//2)

    def test_smallest_rank_three_five_edge_example(self):
        E, packets, F = AS.seed(3)
        self.assertEqual(len(F), 5)
        self.assertEqual([len(p) for p in packets], [1, 2, 1])
        self.assertEqual(
            [AS.defects(c, 3) for c in product(*packets)],
            [{("a", 0)}, {("b", 0)}]
        )
        self.assertFalse(any(AS.sunflower(t) for t in combinations(F, 3)))

    def test_permanent_vertex_exact_criterion(self):
        # 0=forced absence, 1=forced presence, 2=variable.
        # The independently enumerated cartesian minimum and maximum agree
        # exactly with forced-present>=2 and forced-absent>=1.
        for s in range(3, 7):
            for choices in product(range(3), repeat=s):
                rows = [(0,) if c == 0 else (1,) if c == 1 else (0, 1)
                        for c in choices]
                permanent = all(
                    2 <= sum(bits) <= s - 1
                    for bits in product(*rows)
                )
                want = choices.count(1) >= 2 and choices.count(0) >= 1
                self.assertEqual(permanent, want, (s, choices))

    def test_tensors_and_exact_certificate_loads(self):
        for s, size in ((3, 45), (4, 18), (5, 28)):
            with self.subTest(s=s):
                got_size, rows, N = AS.audit_tensor(s)
                self.assertEqual(got_size, size)
                h = 4 if s == 3 else s - 2
                self.assertEqual(N, 2 * h**s)
                self.assertEqual(rows, [h, 2*h] + [h] * (s - 2))

    def test_classical_product_lower_controls(self):
        for s, k in ((3, 1), (3, 2), (3, 3), (4, 1), (4, 2)):
            q = s - 1
            family = [
                frozenset((j, symbol) for j, symbol in enumerate(word))
                for word in product(range(q), repeat=k)
            ]
            self.assertEqual(len(family), q**k)
            self.assertFalse(any(
                AS.sunflower(c) for c in combinations(family, s)
            ))

    def test_strict_published_factor_floors_only(self):
        self.assertGreater(54**0.25, 2)
        self.assertGreater(39**(1/3), 3)
        self.assertGreater(153**(1/3), 5)
        self.assertEqual((2/9, 3/13, 3/17), (12/54, 9/39, 27/153))


if __name__ == "__main__":
    unittest.main()
