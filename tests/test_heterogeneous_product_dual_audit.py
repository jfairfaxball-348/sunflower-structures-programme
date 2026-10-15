"""Independent exact ORIGINAL finite checks; no all-rank theorem inferred."""
import sys, unittest
from itertools import combinations
from fractions import Fraction as Q
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import heterogeneous_product_dual_audit as H

class HeterogeneousOriginalTests(unittest.TestCase):
    def test_rational_primal_dual(self):
        for s,p in ((3,(2,2,2)),(3,(2,2,2,2)),(4,(3,3,3,3)),
                    (4,(2,2,3,3)),(5,(2,2,2,2,4)),(4,(2,3,3,3,3,3))):
            with self.subTest(s=s,p=p):
                V,w,y=H.exact_primal_dual(s,p)
                self.assertEqual(V,H.theoretical_value(s,p))
                self.assertEqual(sum(p[i]*v for i,v in w.items()),V)
                self.assertEqual(sum(y.values()),V)
                for S in combinations([i for i,x in enumerate(p) if x>1],s):
                    self.assertGreaterEqual(sum(w[i] for i in S),1)
                for i,q in enumerate(p):
                    if q>1:self.assertLessEqual(sum(z for S,z in y.items() if i in S),q)

    def test_private_two_and_frozen(self):
        for s,p in ((3,(2,)*6),(4,(2,)*9),(3,(1,2,2,2,2,2,2))):
            with self.subTest(s=s,p=p):
                V,w,y=H.exact_primal_dual(s,p,t=2)
                self.assertEqual(V,H.theoretical_value(s,p,t=2))
                self.assertEqual(sum(y.values()),V)

    def test_original_anchored_exhaustive(self):
        for s,p,n in ((3,(2,2,2),8),(3,(2,2,2,2),32),(4,(3,3,3,3),81),
                      (4,(2,2,3,3),36),(4,(1,2,2,3,3),36)):
            with self.subTest(s=s,p=p):
                Ds=H.all_global_defects(s,p)
                self.assertEqual(len(Ds),n)
                self.assertEqual(min(map(len,Ds)),s)
                V,w,y=H.exact_primal_dual(s,p)
                for D in Ds:self.assertGreaterEqual(sum(w[i] for i,a in D),1)
                for i,q in enumerate(p):
                    if q>1:self.assertLessEqual(sum(z for S,z in y.items() if i in S)/q,1)

    def test_density_single_and_double_deleted(self):
        for s,k in ((3,3),(3,4),(4,4)):
            with self.subTest(s=s,k=k):
                allwords=set(H.words([s-1]*k))
                self.assertEqual(H.orbit_survival(s,k,allwords),1)
                partial=allwords-{sorted(allwords)[0]}
                delta=Q(len(partial),len(allwords))
                self.assertEqual(H.orbit_survival(s,k,partial),(s+1)*delta-s)
                partial.remove(sorted(partial)[-1])
                delta=Q(len(partial),len(allwords))
                self.assertGreaterEqual(H.orbit_survival(s,k,partial),max(0,(s+1)*delta-s))

    def test_all_anchor_alternating_seed(self):
        Ds,recs=H.seed_all_anchor_defects()
        self.assertEqual(len(recs),3)
        self.assertEqual(Ds,{frozenset({'a'}),frozenset({'b'}),frozenset({'c'})})

    def test_rank_zero_and_low_variable_rank(self):
        self.assertEqual(H.theoretical_value(3,()),0)
        self.assertEqual(H.theoretical_value(3,(1,1,1,2,2)),0)
        self.assertEqual(H.theoretical_value(3,(2,2,2)),2)
        self.assertEqual(H.theoretical_value(4,(2,2,2,2)),2)

if __name__=='__main__':unittest.main()
