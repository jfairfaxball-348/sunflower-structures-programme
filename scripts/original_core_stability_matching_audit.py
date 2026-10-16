#!/usr/bin/env python3
"""Finite original-owner triangle-free core stability and exact matching deletion.

Uses literal physical ground points and brute-force sunflower tests, with
integer/Fraction assertions; imports only a predecessor's vertex constructor.
"""
from collections import deque
from fractions import Fraction
from itertools import combinations, product
from coupled_cross_core_audit import family as correlated_family


def is_sunflower(triple):
    d = triple[0] & triple[1]
    return all(a & b == d for a, b in combinations(triple, 2))


def two_disjoint_triangles():
    return tuple(frozenset({("t", g, i), ("t", g, j)})
                 for g in range(2) for i, j in combinations(range(3), 2))


def q_product(q, k):
    return tuple(frozenset({("coord", t, value) for t, value in enumerate(word)})
                 for word in product(range(q), repeat=k))


def max_matching_with_cover(left, right, bad):
    """Augmenting paths and independent Konig alternating-path cover check."""
    adj = {u: [v for v in right if (u, v) in bad] for u in left}
    matched_right = {}
    def augment(u, seen):
        for v in adj[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in matched_right or augment(matched_right[v], seen):
                matched_right[v] = u
                return True
        return False
    for u in left:
        augment(u, set())
    matched_left = {u: v for v, u in matched_right.items()}
    reached_l = set(u for u in left if u not in matched_left)
    reached_r = set()
    queue = deque(reached_l)
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if v == matched_left.get(u) or v in reached_r:
                continue
            reached_r.add(v)
            if v in matched_right and matched_right[v] not in reached_l:
                reached_l.add(matched_right[v])
                queue.append(matched_right[v])
    cover_l = set(left) - reached_l
    cover_r = reached_r
    assert len(cover_l) + len(cover_r) == len(matched_right)
    assert all(u in cover_l or v in cover_r for u, v in bad)
    return len(matched_right), cover_l, cover_r


def analyze(edges, core=frozenset()):
    """Check CSM1-CSM3 on all ORIGINAL actual k-uniform edges."""
    edges = tuple(edges)
    r = len(edges)
    assert r >= 3 and r == len(set(edges))
    assert len({len(a) for a in edges}) == 1
    assert not any(is_sunflower(t) for t in combinations(edges, 3))
    adjacent = {u: set() for u in range(r)}
    for u, v in combinations(range(r), 2):
        if edges[u] & edges[v] == core:
            adjacent[u].add(v)
            adjacent[v].add(u)
    e = sum(map(len, adjacent.values())) // 2
    if not e:
        return {"r": r, "e": 0, "status": "NO_FIXED_CORE_PAIR"}
    assert all(not (adjacent[u] & adjacent[v]) for u in range(r)
               for v in adjacent[u])
    delta = Fraction(r*r, 4) - e
    assert delta >= 0
    u, v = max(((i, j) for i in range(r) for j in adjacent[i] if i < j),
               key=lambda t: (len(adjacent[t[0]]) + len(adjacent[t[1]]),
                              -t[0], -t[1]))
    a, b = adjacent[u], adjacent[v]
    assert not (a & b)
    rem = set(range(r)) - a - b
    assert Fraction(len(rem), 1) <= 4*delta/r
    assert all(core <= edges[i] for i in a | b)
    assert all(j not in adjacent[i] for i, j in combinations(sorted(a), 2))
    assert all(j not in adjacent[i] for i, j in combinations(sorted(b), 2))
    bad = {(i, j) for i in a for j in b if j not in adjacent[i]}
    assert len(bad) <= 5*delta
    assert (len(a)-len(b))**2 <= 20*delta
    match, cover_a, cover_b = max_matching_with_cover(sorted(a), sorted(b), bad)
    retained_a, retained_b = a-cover_a, b-cover_b
    assert len(retained_a) + len(retained_b) == r-len(rem)-match
    assert all(edges[i] & edges[j] == core
               for i in retained_a for j in retained_b)
    physical_a = set().union(*(edges[i]-core for i in retained_a))
    physical_b = set().union(*(edges[j]-core for j in retained_b))
    assert not (physical_a & physical_b)
    return dict(r=r, e=e, delta=delta, leftover=len(rem),
                sizes=(len(a), len(b)), bad=len(bad),
                matching=match, cover=(len(cover_a),len(cover_b)),
                retained=len(retained_a)+len(retained_b),
                rank=len(edges[0]), core_rank=len(core))


def audit():
    cases = [
        ("two-triangles", two_disjoint_triangles(), 6, 9, 0, 0, 0, 6),
        ("correlated-n3m1", sum(correlated_family(2, 3, 1), ()), 12, 24, 4, 4, 2, 6),
        ("correlated-n4m1", sum(correlated_family(2, 4, 1), ()), 16, 48, 4, 8, 4, 8),
        ("correlated-n3m2", sum(correlated_family(2, 3, 2), ()), 24, 96, 8, 16, 4, 12),
    ]
    results = []
    for name, edges, r, e, remainder, bad, matching, retained in cases:
        ans = analyze(edges)
        assert tuple(ans[k] for k in ("r","e","leftover","bad","matching","retained")) == (
            r,e,remainder,bad,matching,retained), (name, ans)
        results.append((name, ans))
    assert analyze(q_product(2,3))["e"] == 4
    assert analyze(tuple(frozenset({("pair",min(i,j),max(i,j))
                         for j in range(4) if i!=j}) for i in range(4)))["e"] == 0
    # Correlated general n,m: Δ=nL², selected star pair leaves 2L,
    # and a bad-edge cover costs (n-2)L even as 1/n -> 0.
    for n, m in ((3,1),(4,1),(3,2)):
        L=2**m
        assert Fraction((2*n*L)**2,4)-n*(n-1)*L*L == n*L*L
        assert Fraction(4*n*L*L,2*n*L) == 2*L
        assert (n-2)*L*L > 0
    print("PASS: physical original near-Turan partition, matching cover, finite checks",
          [(n, a["delta"], a["matching"]) for n,a in results])
    return results


if __name__ == "__main__":
    audit()
