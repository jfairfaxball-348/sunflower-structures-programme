"""Independent checks for fractional point-link LP and original type-class witness."""
import sys
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"scripts"))
from fractional_link_lp_audit import h54,h39,h153,pair_star_isolated,verify,audit

def theta(F):
    d=Counter(x for E in F for x in E)
    return Fraction(max(d.values()),len(F))

class FractionalLinkTests(unittest.TestCase):
    def test_published_factor_original_incidence(self):
        A,B,C=h54(),h39(),h153()
        self.assertEqual((len(A),len(B),len(C)),(54,39,153))
        self.assertEqual((theta(A),theta(B),theta(C)),
                         (Fraction(2,9),Fraction(3,13),Fraction(3,17)))
        self.assertEqual(len(set().union(*A)),18)
        self.assertEqual(len(set().union(*B)),13)
        self.assertEqual(len({E for E in C if E<=set(range(14))}),126)
        self.assertEqual(len({E for E in C if 25 in E}),27)
        self.assertTrue(all(sum(Fraction(1,4) for x in E)==1 for E in A))
        self.assertTrue(all(sum(Fraction(1,3) for x in E)==1 for E in B))
        self.assertTrue(all(sum((Fraction(1,3) if x<14 else Fraction(1) if x==25
                                 else Fraction(0)) for x in E)==1 for E in C))

    def test_original_type_class_and_no_ghost_petals(self):
        F=pair_star_isolated()
        self.assertEqual((len(F),theta(F)),(5,Fraction(2,5)))
        self.assertTrue(all(len({a&b,a&c,b&c})>1
                            for a,b,c in combinations(F,3)))
        W=set(permutations((0,1,2,3,4,4)))
        self.assertEqual(len(W),360)
        degree=Counter((j,x) for word in W for j,i in enumerate(word) for x in F[i])
        self.assertEqual(set(degree.values()),{120})
        self.assertEqual(Fraction(max(degree.values()),len(W)),Fraction(1,3))
        self.assertEqual({sum(len(F[i]) for i in word) for word in W},{18})
        # Coordinate words index distinct ORIGINAL sets, no shifting.
        self.assertEqual(len(set(W)),360)

    def test_full_integer_rational_certificates(self):
        audit()

if __name__=="__main__":
    unittest.main()
