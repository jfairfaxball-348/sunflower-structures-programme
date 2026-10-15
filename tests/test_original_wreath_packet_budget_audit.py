"""Independent all-original tests of MP1-MP5 packet/entropy calculations."""
import unittest
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from original_wreath_packet_budget_audit import (
    original_wreath, predicted_cost, exhaustive_cost, audit
)


class ExactOriginalPacketBudgetTests(unittest.TestCase):
    def test_all_nine_exact_rational_cover_cases(self):
        audit()

    def test_analytic_rank_threshold(self):
        self.assertEqual(predicted_cost(11,3,Fraction(2)),Fraction(11,8))
        self.assertEqual(predicted_cost(11,4,Fraction(2)),Fraction(11,16))
        for n in range(3,20):
            for R in range(1,n):
                C=Fraction(2)
                self.assertEqual(predicted_cost(n,R,C),
                    min(Fraction(j,2) + Fraction(n-2*j,2**R)
                        for j in range(n//2+1)))
        self.assertEqual(predicted_cost(4,2,Fraction(3,2)),Fraction(4,3))

    def test_actual_owner_original_sunflower_freeness_both_cores(self):
        for s,q,n,m in ((3,2,3,1),(3,2,4,1),(4,3,3,1)):
            edges=original_wreath(n,q,m)
            for members in combinations(edges,s):
                intersections={a & b for a,b in combinations(members,2)}
                self.assertGreater(len(intersections),1)

    def test_actual_packet_anchors_and_disjoint_owner_partition(self):
        n,q,m=5,2,2
        edges=original_wreath(n,q,m)
        R=3
        groups=[]
        for i in range(n):
            group={e for e in edges if all(
                ("p",min(i,j),max(i,j)) in e for j in range(n) if j!=i)}
            self.assertEqual(len(group),q**m)
            groups.append(group)
            anchor=frozenset(sorted(
                ("p",min(i,j),max(i,j)) for j in range(n) if i!=j)[:R])
            self.assertEqual(len(anchor),R)
            self.assertTrue(all(anchor <= e for e in group))
            residual={e-anchor for e in group}
            self.assertEqual(len(residual),len(group))
            self.assertEqual({len(x) for x in residual},{n-1+m-R})
        self.assertEqual(set.union(*groups),set(edges))
        self.assertEqual(sum(len(g) for g in groups),len(edges))

    def test_cross_group_actual_intersection_collision(self):
        n,q,m=4,2,1
        edges=original_wreath(n,q,m)
        W=q**m
        def owner(e):
            support=[i for i in range(n) if all(
                ("p",min(i,j),max(i,j)) in e for j in range(n) if i!=j)]
            self.assertEqual(len(support),1)
            return support[0]
        counter=Counter()
        for x in edges:
            for y in edges:
                if owner(x)!=owner(y):
                    intersection=x & y
                    self.assertEqual(len(intersection),1)
                    counter[frozenset(intersection)]+=1
        self.assertEqual(len(counter),n*(n-1)//2)
        self.assertEqual(set(counter.values()),{2*W*W})
        collision=Fraction(sum(c*c for c in counter.values()), len(edges)**4)
        self.assertEqual(collision,Fraction(2*(n-1),n**3))

    def test_entropy_budget_lower_rank_necessity(self):
        # Exact integer reformulation for uniform one-group packets:
        # Z=n/2^R<=1 implies R>=log_2(n), hence >=log_2(n/2).
        for n in range(5,21):
            R=next(r for r in range(1,n) if 2**r>=n)
            self.assertLessEqual(Fraction(n,2**R),1)
            self.assertGreaterEqual(2**R, n//2)
            self.assertGreater(R,0)


if __name__=="__main__":
    unittest.main()
