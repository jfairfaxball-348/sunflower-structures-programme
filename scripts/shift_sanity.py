"""Exact finite sunflower and compression examples. Not a proof of the full conjecture."""
from itertools import combinations, product


def shift(family, i, j):
    """Frankl C_ij, i<j: simultaneous family operation with old-family membership."""
    original = set(family)
    result = set()
    for edge in original:
        replacement = (edge - {j}) | {i}
        if j in edge and i not in edge and replacement not in original:
            result.add(frozenset(replacement))
        else:
            result.add(edge)
    assert len(result) == len(original), "Compression must preserve cardinality"
    return frozenset(result)


def fully_shift(family, n):
    """Repeated lexicographic (i,j) shifts, until no operation changes the family."""
    family = frozenset(family)
    while True:
        previous = family
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                family = shift(family, i, j)
        if family == previous:
            return family


def sunflower(sets):
    if len(sets) < 2 or len(set(sets)) != len(sets):
        return False
    intersections = [a & b for a, b in combinations(sets, 2)]
    return len(set(intersections)) == 1


def has_sunflower(family, s):
    return any(sunflower(tuple(petals)) for petals in combinations(family, s))


def coordinate_product(q, k):
    """P(q,k): one element from each of k disjoint q-symbol blocks."""
    return frozenset(
        frozenset((i, symbol) for i, symbol in enumerate(word))
        for word in product(range(q), repeat=k)
    )


def main():
    f = frozenset(map(frozenset, ({2, 3}, {1, 4}, {1, 5})))
    g = shift(f, 1, 2)
    assert not has_sunflower(f, 3)
    assert g == frozenset(map(frozenset, ({1, 3}, {1, 4}, {1, 5})))
    assert has_sunflower(g, 3)
    assert fully_shift(frozenset((frozenset({3, 4}),)), 4) == frozenset((frozenset({1, 2}),))
    for k in (1, 2, 3):
        p = coordinate_product(3, k)
        assert len(p) == 3**k
        assert not has_sunflower(p, 4)
    assert 3**1000 > 48**94 * 2**1000
    print("PASS: compression creates a 3-sunflower; full shift can replace two positions; q-ary lower bound refutes v1 numerical claim")


if __name__ == "__main__":
    main()
