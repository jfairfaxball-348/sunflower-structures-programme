import sys,unittest
from itertools import combinations
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from correlated_partite_audit import product_family,cap9,defects,witness,check
class OriginalPartiteTest(unittest.TestCase):
    def test_all_product_original_tuples(self):
        for s,m in ((3,4),(4,3),(5,2)):
            f=product_family(s-1,m)
            self.assertTrue(all(len(defects(t))>=2 for t in combinations(f,s)))
    def test_exact_pair_dual_witnesses(self):
        for s in range(3,8):
            for m in range(2,6):
                for i,j in combinations(range(m),2):
                    self.assertEqual(defects(witness(s,m,i,j)),(i,j))
    def test_entropy_equality_on_classical_products(self):
        for s,m in ((3,2),(3,3),(4,2),(5,2)):
            g,t,d,T=check(product_family(s-1,m),s)
            self.assertEqual(t,1)
            self.assertEqual(g,d)
    def test_quadratic_cap(self):
        cap=cap9(); self.assertEqual(len(set(cap)),9)
        self.assertTrue(all(defects(t) for t in combinations(cap,3)))
        self.assertLess(check(cap,3)[1],1)
    def test_reject_known_sunflower(self):
        with self.assertRaises(AssertionError):
            check(((0,0),(1,1),(2,2)),3)
if __name__=="__main__": unittest.main()
