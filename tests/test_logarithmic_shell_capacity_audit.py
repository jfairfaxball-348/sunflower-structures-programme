"""Independent checks of literal witnesses and necessary construction hypotheses."""
import sys
import unittest
from fractions import Fraction
from itertools import combinations
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from logarithmic_shell_capacity_audit import (
    TRIANGLE, audit, common, correlated, core_free_embedding, exact_case,
    exact_density_checks, free, tensor, construction_capacity_checks,
    shared_ground_checks, shared_ground_attachment,
)


class LogarithmicShellCapacityTests(unittest.TestCase):
    def test_entire_audit(self):
        self.assertEqual(len(audit()), 5)

    def test_core_free_neighbour_packets(self):
        result = exact_case(2, 2, 1)
        self.assertEqual((result['r'], result['rank'], result['matching']), (36, 6, 14))
        self.assertEqual(result['J'], Fraction(32, 81))

    def test_t_one_neighbour_caveat(self):
        group = correlated(2, TRIANGLE, (frozenset({0}), frozenset({1})), 1)[0]
        self.assertFalse(common(group))
        self.assertTrue(common(group[2:]))

    def test_intersecting_shell_is_necessary(self):
        shell = tuple(frozenset({(g,i),(g,j)})
                      for g in range(2) for i,j in combinations(range(3),2))
        self.assertTrue(free(shell, 3))
        # Violating intersectingness admits actual empty-core sunflowers.
        F = sum(correlated(2, shell, (frozenset(),), 0), ())
        self.assertFalse(free(F, 3))

    def test_rank_zero_core_free_embedding(self):
        F = core_free_embedding((frozenset(),), 3)
        self.assertEqual(len(F), 3)
        self.assertEqual({len(e) for e in F}, {2})

    def test_nonempty_physical_core_preserves_barrier(self):
        groups = correlated(2, tensor(TRIANGLE, 2),
                            (frozenset({0}), frozenset({1})), 1)
        D = frozenset({('actual-common-point',)})
        old = sum(groups, ())
        padded = tuple(e | D for e in old)
        self.assertTrue(free(padded, 3))
        self.assertEqual(sum(a & b == D for a,b in combinations(padded,2)),
                         sum(not (a & b) for a,b in combinations(old,2)))
        self.assertEqual(common(padded[:len(groups[0])]), D)

    def test_arbitrary_disconnected_seed_embedding(self):
        seed = (frozenset({0,1}), frozenset({0,2}), frozenset({1,2}),
                frozenset({3,4}), frozenset({3,5}), frozenset({4,5}))
        F = core_free_embedding(seed, 3)
        self.assertEqual((len(F), len(F[0])), (18, 4))

    def test_linear_vc_private_fibre(self):
        group = correlated(2, tensor(TRIANGLE, 1),
                           (frozenset({0}), frozenset({1})), 3)[0]
        points = frozenset(('H',0,0,(i,0)) for i in range(3))
        self.assertEqual(len({e & points for e in group[:8]}), 8)

    def test_six_petal_literal_case(self):
        result = exact_case(5, 1, 0)
        self.assertEqual((result['s'], result['rank'], result['r']), (6,3,15))

    def test_all_density_regimes(self):
        self.assertTrue(exact_density_checks())

    def test_non_circular_capacity_actual_constructions(self):
        self.assertTrue(construction_capacity_checks())

    def test_shared_ground_exceeds_finite_catalogue_class(self):
        counts = shared_ground_checks()
        self.assertEqual(2*counts[10], 21552)
        self.assertGreater(21552**4, 54**10)

    def test_shared_reuse_is_real(self):
        F = shared_ground_attachment(TRIANGLE, (frozenset({0}),))
        self.assertEqual((len(F), len(F[0])), (8, 3))
        self.assertTrue(free(F,3))
        # Both marker variants contain exactly the same original X-residual.
        self.assertEqual(F[0]-{('marker',0)}, F[1]-{('marker',1)})


if __name__ == '__main__':
    unittest.main()
