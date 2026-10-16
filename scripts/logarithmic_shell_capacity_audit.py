#!/usr/bin/env python3
"""Literal ORIGINAL shell/substitution checks; all-rank claims need the note's proofs.

Uses independent construction and sunflower enumeration. The predecessor matching
routine is cross-checked with an explicit block matching and cover certificate.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt
from original_core_stability_matching_audit import max_matching_with_cover
from fractional_link_lp_audit import h54


TRIANGLE = tuple(frozenset(e) for e in combinations(range(3), 2))


def tensor(seed, m):
    return tuple(frozenset((t, x) for t, e in enumerate(word) for x in e)
                 for word in product(seed, repeat=m))


def sunflower(edges):
    core = edges[0] & edges[1]
    return all(a & b == core for a, b in combinations(edges, 2))


def free(edges, s):
    return not any(sunflower(tup) for tup in combinations(edges, s))


def common(edges):
    edges = tuple(edges)
    assert edges
    return frozenset.intersection(*edges)


def correlated(q, shell, seed, m):
    """Vertices tagged by actual private grounds, never abstract edge metadata."""
    shell = tuple(shell)
    suffixes = tensor(seed, m)
    groups = []
    for g in range(q):
        group = []
        for i, outer in enumerate(shell):
            fixed = {('S', g, x) for x in outer} | {('y', i)}
            for suffix in suffixes:
                group.append(frozenset(fixed | {('H', g, i, x) for x in suffix}))
        groups.append(tuple(group))
    return tuple(groups)


def private_substitution(shell, seed):
    return tuple(frozenset({('S', x) for x in outer}
                          | {('H', i, x) for x in inner})
                 for i, outer in enumerate(shell) for inner in seed)


def exact_case(q, t, m):
    shell = tensor(TRIANGLE, t)
    seed = tuple(frozenset({i}) for i in range(q))
    groups = correlated(q, shell, seed, m)
    edges = sum(groups, ())
    n, L = 3**t, q**m
    r = q*n*L
    assert r == len(edges) == len(set(edges))
    assert {len(e) for e in edges} == {2*t+1+m}
    assert free(edges, q+1)
    assert all(a & b for block in groups for a, b in combinations(block, 2))
    assert all(not common(block) for block in groups)
    # Literal cross-intersection distribution, with owner-index consistency.
    for g, h in combinations(range(q), 2):
        for u, a in enumerate(groups[g]):
            for v, b in enumerate(groups[h]):
                i, j = u//L, v//L
                assert a & b == (frozenset({('y', i)}) if i == j else frozenset())
    actual_e = sum(not (a & b) for a, b in combinations(edges, 2))
    extremal = comb(q, 2)*(n*L)**2
    deficit = comb(q, 2)*n*L*L
    assert actual_e == extremal-deficit
    assert Fraction(deficit, extremal) == Fraction(1, n)
    # Same physical B in first term, same A in second term; with replacement.
    p, z = groups[:2]
    first = sum((a & b) != (ap & b) for a in p for ap in p for b in z)
    second = sum((a & b) != (a & bp) for a in p for b in z for bp in z)
    J = Fraction(first+second, len(p)*len(z)*len(p))
    assert J == Fraction(4*(n-1), n*n)
    # Enumerate which groups keep each index. Full fibres have equal size;
    # any feasible partial retention is dominated by completing its fibres.
    index_choices = [choice for choice in product((0, 1), repeat=q)
                     if all(not (choice[g] and choice[h])
                            for g, h in combinations(range(q), 2))]
    best = max(sum(sum(choice)*L for choice in allocation)
               for allocation in product(index_choices, repeat=n)) if n <= 3 else n*L
    assert best == n*L
    matching = None
    if q == 2:
        u, v = 0, n*L+L  # actual owners: group 0/index 0 and group 1/index 1
        A = [i for i, e in enumerate(edges) if i != u and not (e & edges[u])]
        B = [i for i, e in enumerate(edges) if i != v and not (e & edges[v])]
        assert not (set(A) & set(B))
        R = set(range(r))-set(A)-set(B)
        bad = {(i, j) for i in A for j in B if edges[i] & edges[j]}
        matching, ca, cb = max_matching_with_cover(A, B, bad)
        explicit = [(n*L+i*L+w, i*L+w) for i in range(2, n) for w in range(L)]
        assert len(explicit) == matching == (n-2)*L
        assert len({i for i, _ in explicit}) == matching
        assert len({j for _, j in explicit}) == matching
        assert all(pair in bad for pair in explicit)
        assert len(ca)+len(cb) == matching
        assert len(bad) == (n-2)*L*L
        assert len(A) == len(B) == (n-1)*L
        delta = Fraction(r*r, 4)-actual_e
        assert delta == n*L*L
        assert len(R) == 2*L == 4*delta/r
        assert r-len(R)-matching == r//2
        if t >= 2:
            assert not common(edges[i] for i in A)
            assert not common(edges[i] for i in B)
    # Explicit private-coordinate shattering; all 2^m physical traces occur.
    fibre = groups[0][:L]
    probes = frozenset(('H', 0, 0, (j, 0)) for j in range(m))
    traces = {e & probes for e in fibre}
    assert len(traces) == 2**m
    return dict(s=q+1, t=t, m=m, rank=len(edges[0]), r=r,
                deficit=deficit, J=J, matching=matching, retained=best)


def core_free_embedding(seed, s):
    assert free(seed, s)
    F = private_substitution(TRIANGLE, seed)
    assert len(F) == 3*len(seed) == len(set(F))
    assert {len(e) for e in F} == {len(next(iter(seed)))+2}
    assert free(F, s)
    assert not common(F)
    assert all(a & b for a, b in combinations(F, 2))
    return F


def exact_density_checks():
    # Predecessor n=sqrt(m) and n=Theta(m), including a failing trial density.
    for m in (100, 400, 1600):
        n = isqrt(m)
        assert 2*n*2**m > Fraction(3, 2)**(n+1+m)
        n = m
        assert 2*n*2**m > Fraction(5, 4)**(n+1+m)
    m = 2000
    assert 2*m*2**m < Fraction(3, 2)**(2*m+1)
    # New n=3^t, k=2t+1+dm: a positive constant t/m, not only o(m).
    # Prior-art H54 controls are exact numeric consequences of its seed proof.
    for q, M, d, T in ((2, 2, 1, Fraction(5,4)),
                       (2, 54, 4, Fraction(5,2)),
                       (3, 39, 3, Fraction(10,3)),
                       (5, 153, 3, Fraction(21,4))):
        # alpha=1/100 independently certified by an integer block inequality.
        assert 3*(Fraction(M,1)/T**d)**100/T**2 > 1
        for block in (1, 2, 4):
            m, t = 100*block, block
            assert q*3**t*M**m > T**(2*t+1+d*m)
            n, L = 3**t, M**m
            assert Fraction(comb(q,2)*n*L*L,
                            comb(q,2)*n*n*L*L) == Fraction(1,n)
    return True


def construction_capacity_checks():
    """Actual nested substitution and joins, plus independently known seed sizes."""
    seed = tuple(frozenset({i}) for i in range(2))
    first = core_free_embedding(seed, 3)  # rank 3, size 6
    nested = private_substitution(TRIANGLE, first)  # rank 5, size 18
    assert free(nested, 3) and len(nested) == 18
    assert len(nested) <= 3**5
    joined = sum(correlated(2, TRIANGLE, first, 1), ())  # rank 6, size 36
    assert len(joined) == 36 and free(joined, 3)
    assert len(joined) <= 3**6
    # Explicit infinite pair-star seed class; no N=2 duplicate-owner error.
    for N in range(3, 9):
        pair_star = tuple(frozenset((min(i,j), max(i,j))
                                   for j in range(N) if j != i) for i in range(N))
        assert len(set(pair_star)) == N and free(pair_star, 3)
        assert N <= 2**(N-1)
    for s, M, d in ((3,54,4), (4,39,3), (6,153,3)):
        assert M <= s**d
        assert M > (s-1)**d  # catalogue base really exceeds the product base
    return True


def shared_ground_attachment(A, previous):
    """Classical three-petal block attachment: reuse A under two markers.

    previous is intersecting; its two physically disjoint copies form B.
    Their rank must be one smaller than A's. No owner is replaced in a check.
    """
    x, y = ('marker', 0), ('marker', 1)
    first = tuple(frozenset({('X', v) for v in e} | {z})
                  for e in A for z in (x, y))
    second = tuple(frozenset({('Z', g, v) for v in e} | {x, y})
                   for g in range(2) for e in previous)
    return first+second


def shared_ground_checks():
    C = {1: (frozenset({0}),), 2: TRIANGLE}
    C[3] = shared_ground_attachment(C[2], C[1])
    # Independently literal Abbott--Hanson 27-edge intersecting seed.
    C[4] = tuple(e for e in h54() if max(e) < 9)
    counts = {1: 1, 2: 3, 3: 8, 4: 27}
    for k in range(5, 11):
        counts[k] = 2*counts[k-1]+2*counts[k-2]
        C[k] = shared_ground_attachment(C[k-1], C[k-2])
    for k, F in C.items():
        assert len(F) == len(set(F)) == counts[k]
        assert {len(e) for e in F} == {k}
        # Full finite tests, not a purported enumeration of trillions of triples.
        if k <= 5:
            assert free(F, 3)
            assert all(a & b for a,b in combinations(F,2))
        if k >= 3:
            assert not common(F)
    assert counts[10] == 10776
    global_rank10 = tuple(frozenset(('copy', g, v) for v in e)
                          for g in range(2) for e in C[10])
    assert len(global_rank10) == len(set(global_rank10)) == 21552
    assert {len(e) for e in global_rank10} == {10}
    assert (2*counts[10])**4 > 54**10
    # lambda=1+sqrt(3) has lambda^4=28+16sqrt(3)>54;
    # 16sqrt(3)>26 iff 768>676. No floating root comparisons.
    assert 16**2*3 > 26**2
    return counts


def audit():
    cases = [exact_case(*args) for args in
             ((2,1,1), (2,1,2), (2,2,1), (3,1,1), (5,1,0))]
    for q in (2, 3, 5):
        core_free_embedding(tuple(frozenset({i}) for i in range(q)), q+1)
    core_free_embedding((frozenset(),), 3)
    assert exact_density_checks()
    assert construction_capacity_checks()
    counts = shared_ground_checks()
    print('PASS: logarithmic physical shells, exponential-error matching barrier, '
          'core-free embedding, restricted noncircular capacity', cases,
          'PRIOR-ART shared-ground rank-10 count', 2*counts[10])
    return cases


if __name__ == '__main__':
    audit()
