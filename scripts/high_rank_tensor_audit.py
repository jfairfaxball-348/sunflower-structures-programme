"""Finite adversarial diagnostics for published rank-3/rank-4 factors.

The general tensor and compression results require symbolic arguments, not this script.
"""
from collections import Counter
from itertools import combinations, product
from spoke_shift_audit import pass_lex


def factor54():
    """Two disjoint Abbott--Hanson 27-edge intersecting 4-families."""
    edges = set()
    for offset in (0, 9):
        blocks = [tuple(range(offset + 3*i, offset + 3*i + 3))
                  for i in range(3)]
        for i, j in combinations(range(3), 2):
            for left in combinations(blocks[i], 2):
                for right in combinations(blocks[j], 2):
                    edges.add(frozenset(left + right))
    return frozenset(edges), 18


def factor39():
    """Axante--Budala--Chitic--Dumitru--Nacu 39-triple construction."""
    blocks = [tuple(range(3*i, 3*i+3)) for i in range(3)]
    special = 9
    labels = {(0, 1): 10, (0, 2): 11, (1, 2): 12}
    edges = {frozenset(b) for b in blocks}
    for block in blocks:
        for pair in combinations(block, 2):
            edges.add(frozenset((special,) + pair))
    for (i, j), label in labels.items():
        for x in blocks[i]:
            for y in blocks[j]:
                edges.add(frozenset((label, x, y)))
    return frozenset(edges), 13


def shadows(family):
    return Counter(e - {x} for e in family for x in e)


def has_sunflower(family, size):
    return any(len({a & b for a, b in combinations(combo, 2)}) == 1
               for combo in combinations(family, size))


def anchored_tensor(s, m):
    """Tensor powers with [K] baseline and distinct high-spoke vertices."""
    assert s in (3, 4) and m >= 1
    F, n = factor54() if s == 3 else factor39()
    baseline = (0, 1, 3, 4) if s == 3 else (0, 1, 2)
    spoke_vertices = (2, 5) if s == 3 else (9,)
    w = len(baseline)
    K = w*m
    mapping = {}
    next_high = K + 1
    for t in range(m):
        for pos, x in enumerate(baseline):
            mapping[t, x] = w*t + pos + 1
    for t in range(m):
        for x in spoke_vertices:
            mapping[t, x] = next_high
            next_high += 1
    for t in range(m):
        for x in range(n):
            if (t, x) not in mapping:
                mapping[t, x] = next_high
                next_high += 1
    assert next_high == n*m + 1
    factors = [tuple(frozenset(mapping[t, x] for x in e) for e in F)
               for t in range(m)]
    tensor = frozenset(frozenset().union(*word) for word in product(*factors))
    assert len(tensor) == len(F)**m
    return tensor, n*m


def check_grid():
    factors = [(3, factor54(), 54, 4, 12, 108),
               (4, factor39(), 39, 3, 9, 63)]
    for s, (F, n), cardinality, rank, degree, shadow in factors:
        assert len(F) == cardinality
        assert all(len(e) == rank for e in F)
        assert max(sum(v in e for e in F) for v in range(n)) == degree
        assert len(shadows(F)) == shadow
        assert not has_sunflower(F, s)
        if s == 3:
            assert set(shadows(F).values()) == {2}
        else:
            assert Counter(shadows(F).values()) == {1: 27, 2: 18, 3: 18}
        for m in (1, 2):
            T, N = anchored_tensor(s, m)
            K = rank*m
            assert len(T) == cardinality**m
            assert len(shadows(T)) == m * shadow * cardinality**(m-1)
            assert max(sum(v in e for e in T) for v in range(1, N+1)) == degree*cardinality**(m-1)
            image = pass_lex(T, N)
            core = frozenset(range(1, K))
            bound = m*(2 if s == 3 else 1) + 1
            assert sum(core <= e for e in image) >= bound
    return "54/39 factors; m=1,2 tensor, shadow, max-degree, full shift PASS"


def main():
    print(check_grid())


if __name__ == "__main__":
    main()
