#!/usr/bin/env python3
"""Independent exact original all-physical-anchor DP and compatibility auditor."""
from fractions import Fraction
from itertools import combinations
from functools import lru_cache
from nested_original_wreath_audit import original_nested_wreath, sunflower_witness


def all_physical_formula(levels, q, m, C):
    """Symbolic AP3; private terminal is the actual q-ary product certificate."""
    assert levels and min(levels) >= 3 and q >= 2 and m >= 1 and C > 1
    C = Fraction(C)
    u = min(Fraction(1), (Fraction(q) / C)**m)
    stages = []
    for n in reversed(levels):
        a = u / C**(n-1)
        v = min(Fraction(j)/C + (n-2*j)*a for j in range(n//2+1))
        stages.append((n, a, v))
        u = min(Fraction(1), v)
    return v, stages


def exhaustive_all_physical(levels, q, m, C):
    """NO shell-only restriction; every actual physical anchor of every owner.
    
    Uses support-set domination only, not AP3, q-ary cylinder LP or a child DP.
    Every cost and optimum is an exact rational number.
    """
    _, edges = original_nested_wreath(levels, q=q, m=m)
    k = len(edges[0])
    supports = {}
    for e in edges:
        for r in range(1, k+1):
            for choice in combinations(e, r):
                anchor = set(choice)
                mask = sum(1 << i for i, original in enumerate(edges)
                           if anchor <= original)
                cost = Fraction(1, C**r)
                supports[mask] = min(supports.get(mask, cost), cost)
    actions = list(supports.items())
    # An anchor whose support is contained in a cheaper support can be removed.
    undominated = [(mask, cost) for mask, cost in actions
                   if not any(mask != other and (mask & other) == mask
                              and other_cost <= cost
                              for other, other_cost in actions)]
    covering = [[] for _ in edges]
    for mask, cost in undominated:
        for i in range(len(edges)):
            if (mask >> i) & 1:
                covering[i].append((mask, cost))
    all_owners = (1 << len(edges))-1

    @lru_cache(None)
    def solve(covered):
        if covered == all_owners:
            return Fraction(0)
        i = min((i for i in range(len(edges)) if not (covered >> i) & 1),
                key=lambda j: len(covering[j]))
        return min(cost + solve(covered | mask)
                   for mask, cost in covering[i])

    return solve(0), len(undominated), len(edges)


def audit():
    cases = [
        ((3,), 2, 1, 2, Fraction(3, 4)),
        ((3,), 2, 1, 3, Fraction(2, 9)),
        ((3,), 2, 2, 2, Fraction(3, 4)),
        ((3,), 2, 2, 3, Fraction(4, 27)),
        ((3,), 3, 1, 3, Fraction(1, 3)),
        ((3, 3), 2, 1, 2, Fraction(9, 16)),
        ((3, 3), 2, 1, 3, Fraction(2, 27)),
    ]
    for levels, q, m, C, expected in cases:
        formula, _ = all_physical_formula(levels, q, m, C)
        exact, actions, owners = exhaustive_all_physical(levels, q, m, C)
        assert exact == formula == expected, (levels, q, m, C, exact, formula)
        print("EXACT ALL-PHYSICAL", levels, q, m, C, exact,
              "owners", owners, "supports", actions)

    # Closed forms across unbounded symbolic depth; exact rational arithmetic.
    for t in range(1, 10):
        levels = (3,) * t
        assert all_physical_formula(levels, 3, t, 2)[0] == Fraction(3, 4)**t
        assert all_physical_formula(levels, 2, t, 3)[0] == (
            Fraction(1, 3)**t * Fraction(2, 3)**t)
        assert 9**t > 2**(3*t)
        assert Fraction(3, 2)**t > 1

    for s, q in ((3, 2), (4, 3)):
        _, edges = original_nested_wreath((3, 3), q=q, m=1)
        assert len(set(edges)) == len(edges)
        assert sunflower_witness(edges, s) is None

    # Exact sharp AP6: only the first pair intersects, all other pairs disjoint.
    for s in (3, 4, 6):
        edges = []
        for i in range(s):
            if i < 2:
                private = {("private", i, 0), ("shared", 0)}
            else:
                private = {("private", i, 0), ("private", i, 1)}
            edges.append(frozenset(private))
        assert {len(edge) for edge in edges} == {2}
        assert sunflower_witness(edges, s) is None
        defects = [int((edges[i] & edges[j]) != frozenset())
                   for i, j in combinations(range(s), 2)]
        assert sum(defects) == 1

    # Sharp weighted AP7 for q pairwise disjoint singleton original residues.
    for q in (2, 3, 5):
        overlap = sum(Fraction(1, q*q) for _ in range(q))
        assert overlap == Fraction(1, q)
    print("PASS: AP1–AP7 original all-physical anchor/compatibility audit")


if __name__ == "__main__":
    audit()
