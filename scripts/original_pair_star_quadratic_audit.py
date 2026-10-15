#!/usr/bin/env python3
"""Exact stdlib-only audit of complete-pair-star ORIGINAL witness LP.

For n>=s+1, original E_i contains the n-1 vertices {i,j}. Each actual
record is an anchor i and s distinct original petals J. The defect
consists of the C(s,2) original ground vertices {a,b} with a,b in J.
The symmetric primal/dual are checked using exact integer arithmetic.
"""
from itertools import combinations
from math import comb


def family(n):
    return tuple(
        frozenset(frozenset((i, j)) for j in range(n) if j != i)
        for i in range(n)
    )


def records(F, s):
    """Enumerate actual original records (no shifting, no ghost owners)."""
    for i, anchor in enumerate(F):
        packets = {}
        for j, petal in enumerate(F):
            if j != i:
                trace = anchor & petal
                if trace:
                    packets[trace] = (j, petal)
        for traces in combinations(packets, s):
            if len({len(t) for t in traces}) != 1:
                continue
            if len({a & b for a, b in combinations(traces, 2)}) != 1:
                continue
            picks = tuple(packets[t] for t in traces)
            petals = tuple(p for _, p in picks)
            defect = frozenset(
                x for x in set().union(*petals)
                if 2 <= sum(x in p for p in petals) < s
            )
            if defect and not (anchor & defect):
                yield i, tuple(j for j, _ in picks), defect



def disjoint_copies(n, r):
    """r physical disjoint copies of the same rank-(n-1) family."""
    return tuple(
        frozenset((copy, x) for x in E)
        for copy in range(r) for E in family(n)
    )

def audit():
    for s in (3, 4, 5, 6):
        for n in range(s + 1, 10):
            F = family(n)
            vertices = set().union(*F)
            assert len(F) == n and len(vertices) == comb(n, 2)
            assert all(len(e) == n - 1 for e in F)
            # Pairwise intersections are DISTINCT, so no s-sunflower.
            assert all(
                F[i] & F[j] == frozenset((frozenset((i, j)),))
                for i, j in combinations(range(n), 2)
            )
            assert len({F[i] & F[j]
                        for i, j in combinations(range(n), 2)}) == comb(n, 2)
            R = tuple(records(F, s))
            expected = (n - s) * comb(n, s)
            assert len(R) == expected, (n, s, len(R), expected)
            # y_r = 1/denominator is exact feasible dual;
            # z_x = 1/C(s,2) on each physical vertex is exact primal.
            denominator = (n - s) * comb(n - 2, s - 2)
            vertex_loads = dict.fromkeys(vertices, 0)
            owner_loads = dict.fromkeys(range(n), 0)
            for anchor, petals, defect in R:
                assert len(set((anchor,) + petals)) == s + 1
                assert defect == frozenset(
                    frozenset(pair) for pair in combinations(petals, 2)
                )
                assert len(defect) == comb(s, 2)
                for x in defect:
                    vertex_loads[x] += 1
                for owner in (anchor,) + petals:
                    owner_loads[owner] += 1
            assert set(vertex_loads.values()) == {denominator}
            assert set(owner_loads.values()) == {(s + 1) * expected // n}
            assert ((s + 1) * expected) % n == 0
            # Equality of primal and dual objectives.
            assert expected * comb(s, 2) == comb(n, 2) * denominator
            assert all(sum(x in e for e in F) == 2 for x in vertices)
            print("PASS complete-pair-star", "s", s, "n", n,
                  "rank", n - 1, "records", expected,
                  "V", f"{n*(n-1)}/{s*(s-1)}", "theta", f"2/{n}")
    for s in (3, 4, 5, 6):
        n = s + 2
        for r in (1, s - 1):
            F = disjoint_copies(n, r)
            R = tuple(records(F, s))
            expected = r * (n - s) * comb(n, s)
            assert len(R) == expected
            denominator = (n - s) * comb(n - 2, s - 2)
            vertices = set().union(*F)
            vertex_loads = {x: 0 for x in vertices}
            owners = {i: 0 for i in range(len(F))}
            for anchor, petals, D in R:
                for x in D: vertex_loads[x] += 1
                for h in (anchor,) + petals: owners[h] += 1
            assert set(vertex_loads.values()) == {denominator}
            assert set(owners.values()) == {(s + 1) * expected // (r * n)}
            assert expected * comb(s, 2) == len(vertices) * denominator
            assert len(vertices) == r * comb(n, 2)
            assert all(sum(x in E for E in F) == 2 for x in vertices)
    print("PASS exact ORIGINAL balanced quadratic LP, disjoint-copy optimum, vanishing links")


if __name__ == "__main__":
    audit()
