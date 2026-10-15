"""Independent integer verification of all-owner exact balance."""
import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import original_owner_balancing_audit as A
import original_nonproduct_tensor_lp_audit as B

class BalancedOwnerTest(unittest.TestCase):
    def test_exact_audit(self):
        A.audit()

    def test_independent_numerator_totals_and_deletion(self):
        F = B.tensor(B.seed(), B.cap9())
        rec = tuple(B.rectangle_records(F))
        own = {e:0 for e in F}
        vert = {v:0 for v in set().union(*F)}
        for i,w in A.CERT:
            a, petals, D = rec[i]
            for e in (a,) + petals:
                own[e] += w
            for v in D:
                vert[v] += w
        self.assertEqual(len(A.CERT),58)
        self.assertEqual(sum(w for i,w in A.CERT),8*A.DENOM)
        self.assertEqual(set(own.values()),{32*A.DENOM//45})
        self.assertTrue(all(x<=A.DENOM for x in vert.values()))
        # For n retained original edges, NC3 gives max(0,8-(45-n)*32/45).
        self.assertEqual(8*A.DENOM-11*(32*A.DENOM//45),
                         (8*45-11*32)*A.DENOM//45)
        self.assertGreater(8*45-11*32,0)
        self.assertLessEqual(8*45-12*32,0)

if __name__ == "__main__":
    unittest.main()
