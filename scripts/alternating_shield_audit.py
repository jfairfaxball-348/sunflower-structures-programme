#!/usr/bin/env python3
"""Standalone stdlib verification of original alternating shields (not an all-k proof)."""
from itertools import combinations, product


def sunflower(edges):
    """Equal pairwise intersections of DISTINCT original members."""
    edges = tuple(map(frozenset, edges))
    return len(set(edges)) == len(edges) and len({
        frozenset(a & b) for a, b in combinations(edges, 2)
    }) == 1


def defects(edges, s):
    vertices = set().union(*edges)
    return {
        x for x in vertices if 2 <= sum(x in a for a in edges) <= s - 1
    }


def seed(s):
    """Private-padded rank-s original family with s+2 edges."""
    assert s >= 3
    anchor = frozenset(("e", i) for i in range(s))

    def petal(i, pair, tag):
        return frozenset(
            {("e", i)} | set(pair) |
            {("pad", tag, j) for j in range(s - 3)}
        )

    packets = [
        [petal(0, {("a", 0), ("b", 0)}, "one")],
        [
            petal(1, {("a", 0), ("c", 0)}, "two0"),
            petal(1, {("b", 0), ("c", 0)}, "two1"),
        ],
    ]
    for i in range(2, s):
        packets.append([petal(i, {("u", i), ("v", i)}, ("other", i))])
    edges = [anchor] + [a for packet in packets for a in packet]
    assert len(set(edges)) == s + 2
    assert all(len(a) == s for a in edges)
    assert all(
        a & anchor == frozenset({("e", i)})
        for i, packet in enumerate(packets) for a in packet
    )
    return anchor, packets, edges


def q9():
    return [
        frozenset({(0, x), (1, y), (2, (x*x + y*y) % 3)})
        for x, y in product(range(3), repeat=2)
    ]


def tensor(family, factor):
    return [
        frozenset({(0, v) for v in a} | {(1, v) for v in b})
        for a, b in product(family, factor)
    ]


def audit_seed(s):
    anchor, packets, edges = seed(s)
    all_combos = tuple(combinations(edges, s))
    assert not any(sunflower(combo) for combo in all_combos)
    tuple_defects = []
    for choice in product(*packets):
        assert not sunflower(choice)
        want = {("a", 0)} if choice[1] == packets[1][0] else {("b", 0)}
        assert defects(choice, s) == want
        tuple_defects.append(want)
    assert set.intersection(*tuple_defects) == set()
    assert not set.intersection(*edges)
    assert len(edges) == s + 2 and len(all_combos) == (s+2)*(s+1)//2
    return len(all_combos)


def audit_tensor(s):
    anchor_seed, packets, seed_edges = seed(s)
    factor = q9() if s == 3 else [
        frozenset({("t", j)}) for j in range(s - 1)
    ]
    assert len(set(factor)) == len(factor)
    if s == 3:
        assert len(factor) == 9 and not any(
            sunflower(c) for c in combinations(factor, 3)
        )
    family = tensor(seed_edges, factor)
    if s <= 5:
        assert not any(sunflower(c) for c in combinations(family, s))
    auxiliary_anchor = factor[0]
    anchor = frozenset(
        {(0, v) for v in anchor_seed} |
        {(1, v) for v in auxiliary_anchor}
    )
    rows = []
    for i in range(s):
        trace = frozenset({(0, ("e", i))})
        rows.append([a for a in family if a & anchor == trace])
    h = 4 if s == 3 else s - 2
    assert [len(row) for row in rows] == (
        [h, 2*h] + [h] * (s - 2)
    )
    total = 1
    for row in rows:
        total *= len(row)
    assert total == 2 * h**s

    a, b = (0, ("a", 0)), (0, ("b", 0))
    count_a = count_b = 0
    for choice in product(*rows):
        ds = defects(choice, s)
        assert (a in ds) != (b in ds)
        count_a += a in ds
        count_b += b in ds
    assert count_a == count_b == h**s

    # Choose the same auxiliary residue in every packet to isolate each
    # alternative witness: exactly {a}, or exactly {b}.
    same_aux = next(q for q in factor if q.isdisjoint(auxiliary_anchor))
    for variant in (0, 1):
        lifted = [
            frozenset({(0, v) for v in packets[i][variant if i == 1 else 0]} |
                      {(1, v) for v in same_aux})
            for i in range(s)
        ]
        assert defects(lifted, s) == ({a} if variant == 0 else {b})
    # These two isolated tuples force w_a>=1 and w_b>=1. Conversely
    # w_a=w_b=1 certifies every tuple. Exact restricted fractional LP OPT=2.
    return (len(family), [len(row) for row in rows], total)


def main():
    for s in range(3, 10):
        print("seed", s, "all tuples", audit_seed(s))
    for s in (3, 4, 5):
        print("tensor", s, audit_tensor(s))
    # Construction LOWER floors only; never upper bounds.
    assert 54**0.25 > 2 and 39**(1/3) > 3 and 153**(1/3) > 5
    print("PASS: alternating shields, private padding, exact local LP")


if __name__ == "__main__":
    main()
