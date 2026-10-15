#!/usr/bin/env python3
"""Exact original-shell anchored-packet Kraft optimum (stdlib; rational DP)."""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, product


def original_wreath(n, q, m):
    """Every emitted member is an ORIGINAL set of actual pair/private points."""
    assert n >= 3 and q >= 2 and m >= 1
    edges = []
    for i in range(n):
        shell = frozenset(("p", min(i, j), max(i, j)) for j in range(n) if i != j)
        for word in product(range(q), repeat=m):
            private = frozenset(("v", i, t, a) for t, a in enumerate(word))
            edges.append(shell | private)
    assert len(edges) == len(set(edges)) == n * q**m
    assert {len(e) for e in edges} == {n - 1 + m}
    return tuple(edges)


def predicted_cost(n, R, C):
    """Theorem MP1, exact rational optimal packet budget."""
    assert 1 <= R <= n-1
    C = Fraction(C)
    assert C > 1
    return min(Fraction(j, 1)/C + Fraction(n-2*j, 1)/(C**R)
               for j in range(n//2 + 1))


def exhaustive_cost(edges, R, C):
    """Independently minimise over ALL nonempty ACTUAL anchors |B|<=R.

    A partition with anchor B can be replaced by a cover of edges by its
    full incidence fibre {E:B subset E}, and vice versa (allocate each
    covered original E to one selected anchor). Thus exact set-cover DP
    over fibres is equivalent to the original packet problem.
    """
    C = Fraction(C)
    assert C > 1 and R >= 1
    anchors = set()
    for e in edges:
        ordered = sorted(e)
        for r in range(1, min(R,len(e))+1):
            anchors.update(combinations(ordered, r))
    covers = {}
    for anchor in anchors:
        B = frozenset(anchor)
        fibre = sum((1 << i) for i, E in enumerate(edges) if B <= E)
        if fibre:
            covers[fibre] = min(covers.get(fibre, Fraction(10**9)), C**(-len(B)))
    incident = [[(fibre, cost) for fibre, cost in covers.items() if fibre & (1 << i)]
                for i in range(len(edges))]
    assert all(incident)
    @lru_cache(None)
    def solve(uncovered):
        if not uncovered:
            return Fraction(0)
        i = (uncovered & -uncovered).bit_length()-1
        return min(cost + solve(uncovered & ~fibre) for fibre,cost in incident[i])
    optimum = solve((1 << len(edges))-1)
    return optimum, len(anchors), len(covers), solve.cache_info().currsize


def audit():
    cases = [
        (3,2,1,1,Fraction(3,2)),
        (3,2,1,2,Fraction(3,2)),
        (3,2,1,2,Fraction(3)),
        (4,2,1,1,Fraction(2)),
        (4,2,1,2,Fraction(3,2)),
        (4,2,1,3,Fraction(2)),
        (5,2,1,2,Fraction(3,2)),
        (5,2,1,4,Fraction(2)),
        (3,3,1,2,Fraction(7,3)),
    ]
    for n,q,m,R,C in cases:
        edges = original_wreath(n,q,m)
        actual, n_anchors, n_fibres, n_states = exhaustive_cost(edges,R,C)
        predicted = predicted_cost(n,R,C)
        assert actual == predicted, (n,q,m,R,C,actual,predicted)
        print("PASS", "n", n, "q", q, "m", m, "R", R, "C", C,
              "min_cost", actual, "anchors", n_anchors,
              "fibres", n_fibres, "states", n_states)
    print("PASS exact original physical-anchor Kraft optimum")


if __name__ == "__main__":
    audit()
