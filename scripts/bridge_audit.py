"""Finite counterexample audits for the Mishra bridge. Not universal proofs."""
from itertools import combinations, product


def shift(family, i, j):
    old = set(family)
    new = set()
    for a in old:
        b = frozenset((a - {j}) | {i})
        new.add(b if j in a and i not in a and b not in old else a)
    assert len(new) == len(old)
    return frozenset(new)


def sunflower(family):
    if len(family) < 2 or len(set(family)) != len(family):
        return False
    return len({a & b for a, b in combinations(family, 2)}) == 1


def tau(family):
    for r in range(len(family), 1, -1):
        if any(sunflower(candidate) for candidate in combinations(family, r)):
            return r
    return int(bool(family))


def shadow(family):
    return {frozenset(a - {x}) for a in family for x in a}


def shifted(family, n):
    return all(shift(family, i, j) == family
               for i in range(1, n) for j in range(i + 1, n + 1))


def audit_layers(n=5):
    """All subfamilies in the k=2 and k=3 layers of [5]: 2048 tests."""
    total = stable = 0
    for k in (2, 3):
        edges = list(map(frozenset, combinations(range(1, n + 1), k)))
        for mask in range(1 << len(edges)):
            f = frozenset(edges[j] for j in range(len(edges)) if mask & (1 << j))
            tf = tau(f)
            if f:
                assert k * len(f) <= tf * len(shadow(f))
            for i in range(1, n):
                for j in range(i + 1, n + 1):
                    g = shift(f, i, j)
                    assert len(f) == len(g) and tau(g) <= 2 * tf
            if shifted(f, n):
                stable += 1
                if f and tf <= k:
                    assert 2 * sum(1 in a for a in f) >= len(f)
                link = frozenset(frozenset(a - {1}) for a in f if 1 in a)
                assert all(shift(link, i, j) == link
                           for i in range(2, n) for j in range(i + 1, n + 1))
            total += 1
    return total, stable


def audit_product_subfamilies():
    """Every pairing of [6], and every shifted subfamily of each P(2,3)."""
    universe = set(range(1, 7))
    pairings = {tuple(sorted(tuple(sorted(p)) for p in pairs))
                for pairs in combinations(list(combinations(universe, 2)), 3)
                if set().union(*(set(p) for p in pairs)) == universe}
    assert len(pairings) == 15
    maximum = checked = 0
    for blocks in pairings:
        edges = [frozenset(x) for x in product(*blocks)]
        for mask in range(1 << len(edges)):
            f = frozenset(edges[j] for j in range(len(edges)) if mask & (1 << j))
            if shifted(f, 6):
                maximum = max(maximum, len(f))
                assert len(f) <= 2
            checked += 1
    assert shifted(frozenset((frozenset({1, 2, 3}),
                              frozenset({1, 2, 4}))), 6)
    return len(pairings), checked, maximum


def audit_sharpness(m=4):
    f = frozenset([frozenset({1, 3+a}) for a in range(m)] +
                  [frozenset({2, 3+m+a}) for a in range(m)])
    assert tau(f) == m and tau(shift(f, 1, 2)) == 2*m
    return m, 2*m


def audit_pair_private(k=5):
    f = frozenset(frozenset((min(i, j), max(i, j))
                             for j in range(k+1) if i != j)
                  for i in range(k+1))
    assert len(f) == k+1 and all(len(a) == k for a in f)
    assert max(sum(x in a for a in f) for x in set().union(*f)) == 2
    assert not any(sunflower(t) for t in combinations(f, 3))
    return len(f)


def experimental_shifted_stars():
    """Only checks k=2..8: no universal assertion about rank dependence."""
    for k in range(2, 9):
        blocks = [(i+1, k+i+1) for i in range(k)]
        family = frozenset(frozenset(x) for x in product(*blocks))
        for _ in range(5):
            old = family
            for i in range(1, 2*k):
                for j in range(i+1, 2*k+1):
                    family = shift(family, i, j)
            if family == old:
                break
        assert shifted(family, 2*k)
        assert all(frozenset(set(range(1, k)) | {j}) in family
                   for j in range(k, 2*k+1))
    return 2, 8


def main():
    assert audit_layers() == (2048, 32)
    assert audit_product_subfamilies() == (15, 3840, 2)
    assert audit_sharpness() == (4, 8)
    assert audit_pair_private() == 6
    assert experimental_shifted_stars() == (2, 8)
    print("PASS: exhaustive shadows/one-shifts, q-ary shifted-original extraction,"
          " sharp factor 2, pair-private links, finite product-star experiments")


if __name__ == "__main__":
    main()
