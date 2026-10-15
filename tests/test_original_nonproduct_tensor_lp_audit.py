"""Independent direct-original-triple enumeration; stdlib."""
import sys,unittest
from itertools import combinations
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import original_nonproduct_tensor_lp_audit as A

class OriginalNonproductTests(unittest.TestCase):
    def test_factors_and_tensor_sunflower_free(self):
        for F in (A.seed(),A.cap9(),A.tensor(A.seed(),A.cap9())):
            self.assertEqual(len(set(F)),len(F))
            self.assertFalse(any(A.sunflower(t) for t in combinations(F,3)))

    def test_independent_direct_all_anchor_enumeration(self):
        F=A.tensor(A.seed(),A.cap9())
        brute=set()
        nr=0
        for anchor in F:
            for picked in combinations([p for p in F if p!=anchor],3):
                traces=[p&anchor for p in picked]
                if all(traces) and len({len(t) for t in traces})==1 and A.sunflower(traces):
                    nr+=1
                    brute.add(A.defects(picked))
        indexed=tuple(A.rectangle_records(F))
        self.assertEqual((nr,len(brute)),(6403,457))
        self.assertEqual(nr,len(indexed))
        self.assertEqual(brute,{r[2] for r in indexed})
        self.assertTrue(all(brute))
        self.assertTrue(all(A.COVER&D for D in brute))

    def test_eight_disjoint_actual_dual_witnesses(self):
        F=A.tensor(A.seed(),A.cap9())
        got={}
        for anchor,petals,D in A.rectangle_records(F):
            if D in A.DUAL_DEFECTS and D not in got:got[D]=(anchor,petals)
        self.assertEqual(set(got),set(A.DUAL_DEFECTS))
        used=set()
        for D in A.DUAL_DEFECTS:
            self.assertFalse(D&used)
            used|=D
            anchor,petals=got[D]
            self.assertIn(anchor,F)
            self.assertEqual(len(set(petals)|{anchor}),4)
            self.assertTrue(all(p in F for p in petals))
            self.assertEqual(A.defects(petals),D)

    def test_factor_primal_and_dual(self):
        for F,sets in (
            (A.seed(),(frozenset({'a'}),frozenset({'b'}),frozenset({'c'}))),
            (A.cap9(),(frozenset({(0,0)}),frozenset({(1,0)}),frozenset({(2,1)})))):
            allD={r[2] for r in A.rectangle_records(F)}
            self.assertTrue(all(D in allD for D in sets))
            self.assertEqual(len(set().union(*sets)),3)
            self.assertTrue(all(D&set().union(*sets) for D in allD))

    def test_low_rank_and_rank_two_recurrence_counterexample(self):
        self.assertEqual(len(tuple(A.rectangle_records((frozenset(),)))),0)
        self.assertEqual(len(tuple(A.rectangle_records((frozenset({'x'}),)))),0)
        F=tuple(frozenset({x,y}) for a in (0,3)
                for x,y in ((a,a+1),(a+1,a+2),(a,a+2)))
        self.assertEqual(len(F),6)
        self.assertFalse(any(A.sunflower(t) for t in combinations(F,3)))
        self.assertGreater(len(F),4)

if __name__=='__main__':unittest.main()
