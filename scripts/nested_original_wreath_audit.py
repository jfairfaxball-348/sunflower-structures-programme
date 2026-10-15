#!/usr/bin/env python3
"""Exact physically-original nested wreath and shell-only Kraft auditor (NW1-NW9)."""
from fractions import Fraction
from itertools import combinations, product
from functools import lru_cache
from math import prod


def original_nested_wreath(levels, q=2, m=1):
    """Classical q-singleton seed raised to m, in truly PRIVATE physical copies."""
    assert levels and min(levels) >= 3 and q >= 2 and m >= 1
    shells, edges = {}, []
    for leaf in product(*(range(n) for n in levels)):
        shell = set()
        for h, n in enumerate(levels):
            prefix, i = leaf[:h], leaf[h]
            shell.update(("shell", prefix, min(i, j), max(i, j))
                         for j in range(n) if i != j)
        shells[leaf] = frozenset(shell)
        for word in product(range(q), repeat=m):
            private = {("private", leaf, z, a) for z, a in enumerate(word)}
            edges.append(frozenset(shell | private))
    return shells, edges


def sunflower_witness(edges, s):
    for ids in combinations(range(len(edges)), s):
        common = edges[ids[0]] & edges[ids[1]]
        if all(edges[i] & edges[j] == common
               for i, j in combinations(ids, 2)):
            return ids
    return None


def symbolic_shell_cost(levels, C):
    """Exact NW2 DP; nested U is allowed to STOP at an existing ancestor shell."""
    C = Fraction(C)
    U = Fraction(1)
    stages = []
    for n in reversed(levels):
        a = U / C**(n-1)
        V = min(Fraction(j, 1) / C + (n-2*j)*a
                for j in range(n//2+1))
        stages.append((n, U, a, V))
        U = min(Fraction(1), V)
    return stages[-1][-1], stages


def exhaustive_shell_cost(levels, C):
    """Independent rational minimum set-cover over ALL actual shell-only anchors.

    No analytic NW2 formula or grouping reduction is used by the enumerator.
    An atomic original fibre has precisely the shell support of its leaf label.
    """
    shells, _ = original_nested_wreath(levels)
    atoms = list(shells)
    points = sorted(set().union(*shells.values()))
    best = {}
    for rank in range(1, len(points)+1):
        for chosen in combinations(points, rank):
            B = set(chosen)
            mask = sum(1 << i for i, v in enumerate(atoms) if B <= shells[v])
            if mask:
                cost = Fraction(1, C**rank)
                if mask not in best or cost < best[mask]:
                    best[mask] = cost
    full = (1 << len(atoms)) - 1
    actions = tuple(best.items())

    @lru_cache(None)
    def solve(covered):
        if covered == full:
            return Fraction(0)
        uncovered = next(i for i in range(len(atoms))
                         if not (covered >> i) & 1)
        return min(cost + solve(covered | mask)
                   for mask, cost in actions if (mask >> uncovered) & 1)

    return solve(0), len(actions), len(points)


def audit():
    for levels in ((3,), (3, 3)):
        for C in (2, 3):
            actual, actions, npoints = exhaustive_shell_cost(levels, C)
            formula, _ = symbolic_shell_cost(levels, C)
            assert actual == formula, (levels, C, actual, formula)
            print("EXACT ORIGINAL SHELL COVER", levels, C,
                  actual, "supports", actions, "points", npoints)

    for levels in ((3, 4), (4, 3)):
        assert symbolic_shell_cost(levels, 2)[0] == Fraction(3, 8)
        assert symbolic_shell_cost(levels, 3)[0] == Fraction(4, 81)

    for s, levels, q, m in ((3, (3, 3), 2, 1),
                            (3, (3, 4), 2, 1),
                            (4, (3, 3), 3, 1)):
        shells, edges = original_nested_wreath(levels, q, m)
        k = sum(n-1 for n in levels) + m
        assert len(edges) == prod(levels) * q**m
        assert len(set(edges)) == len(edges)
        assert {len(edge) for edge in edges} == {k}
        assert sunflower_witness(edges, s) is None
        print("ACTUAL ORIGINAL S-FREE", s, levels, len(edges), "rank", k)

    for depth in range(1, 5):
        levels = (3,) * depth
        assert symbolic_shell_cost(levels, 2)[0] == Fraction(3, 4)**depth
        # The rank 3t, cardinality 9^t, residual 3^t>2^t counterexample:
        assert 9**depth > 2**(3*depth)
        assert 3**depth > 2**depth
        assert 2*depth < 3*depth

    # Exact conditioned physical intersection probability at both scales.
    N, L = 3, 4
    pair_outer = Fraction(2*(N-1), N**3)
    pair_inner = Fraction(2*(L-1), L**3)
    all_same_outer = Fraction(1, N**3)
    assert all_same_outer * pair_inner == Fraction(2*(L-1), N**3*L**3)
    assert pair_outer == Fraction(4, 27)
    print("PASS: exact nested physical-original wreath auditor")


if __name__ == "__main__":
    audit()
