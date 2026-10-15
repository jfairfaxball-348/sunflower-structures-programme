"""Independent tests of original-shell construction and rational LP bounds."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from original_wreath_density_audit import wreath, is_s_free, audit

class OriginalWreathTests(unittest.TestCase):
    def test_exact_small_sunflower_and_incidence(self):
        for s,q,n,m in ((3,2,3,1),(3,2,4,2),(4,3,3,1),(6,5,3,1)):
            edges=wreath(q,m,n)
            self.assertEqual(len(edges),n*q**m)
            self.assertEqual(len(set(edges)),len(edges))
            self.assertTrue(is_s_free(edges,s))
            self.assertEqual({len(e) for e in edges},{n-1+m})
            cnt=Counter(x for e in edges for x in e)
            self.assertEqual(max(cnt.values()),2*q**m)
            self.assertEqual(Fraction(max(cnt.values()),len(edges)),Fraction(2,n))
    def test_every_shell_point_and_private_point(self):
        edges=wreath(2,3,5)
        cnt=Counter(x for e in edges for x in e)
        self.assertEqual({v for x,v in cnt.items() if x[0]=='pair'}, {16})
        self.assertEqual({v for x,v in cnt.items() if x[0]=='inner'}, {4})
    def test_no_empty_or_nonempty_cores(self):
        edges=wreath(2,1,3)
        intersections=[(a&b,a&c,b&c) for a,b,c in combinations(edges,3)]
        self.assertTrue(all(not (x==y==z) for x,y,z in intersections))
    def test_arithmetic_and_certificates(self):
        audit()

if __name__=='__main__': unittest.main()
