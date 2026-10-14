"""Independent finite regressions for the proved density-dependent no-go."""
import sys
import unittest
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from dense_obstruction_audit import base_graph, tensor_graph, check_grid, has_sunflower
from spoke_shift_audit import pass_lex


class DenseObstructionTests(unittest.TestCase):
    def test_graph_sizes_degree_and_max_petal_capacity(self):
        for q in range(2, 8):
            edges, n = base_graph(q)
            expected = q*q + (q if q % 2 == 0 else q//2)
            self.assertEqual(len(edges), expected)
            self.assertEqual(max(sum(v in e for e in edges)
                                 for v in range(n)), q)
            if q <= 4:
                self.assertFalse(any(has_sunflower(x)
                                     for x in combinations(edges, q+1)))

    def test_tensor_counts_and_sunflower_free(self):
        for q, m in [(2, 2), (2, 3), (3, 2)]:
            F, _ = tensor_graph(q, m)
            E, _ = base_graph(q)
            self.assertEqual(len(F), len(E)**m)
            if len(F) <= 50:
                self.assertFalse(any(has_sunflower(x)
                                     for x in combinations(F, q+1)))

    def test_shifted_image_large_common_core(self):
        for q, m in [(2, 2), (3, 2), (4, 2)]:
            F, n = tensor_graph(q, m)
            G = pass_lex(F, n)
            core = frozenset(range(1, 2*m))
            count = sum(core <= edge for edge in G)
            lower = (2*m if q % 2 else m)*(q-1)+1
            self.assertGreaterEqual(count, lower)

    def test_full_grid(self):
        self.assertEqual(len(check_grid()), 16)


if __name__ == "__main__":
    unittest.main()
