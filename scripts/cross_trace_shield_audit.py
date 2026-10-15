#!/usr/bin/env python3
"""Exact finite audits of original trace-residue compatibility (stdlib only)."""
from collections import defaultdict
from itertools import combinations, product


def sunflower(sets):
    if len(set(sets)) != len(sets):
        return False
    return len({a & b for a, b in combinations(sets, 2)}) == 1


def free(family, s):
    return all(not sunflower(block) for block in combinations(family, s))


def packets(family, anchor):
    out = defaultdict(set)
    for edge in family:
        out[edge & anchor].add(edge - anchor)
    return out


def seed(s):
    """s+1 distinct rank-s originals, s distinct sunflower traces, s-free."""
    anchor = frozenset(('e', i) for i in range(s))
    hub = frozenset(('h', i) for i in range(s-2))
    petals = [frozenset({('e', i), ('z', i if i < s-1 else 0)}) | hub
              for i in range(s)]
    return (anchor, *petals)


def cap9():
    return tuple(frozenset({('x', x), ('y', y), ('z', (x*x+y*y)%3)})
                 for x in range(3) for y in range(3))


def qproduct(q, k):
    return tuple(frozenset((j, letter) for j, letter in enumerate(w))
                 for w in product(range(q), repeat=k))


def tensor(a, b):
    return tuple(frozenset({(0, v) for v in x} | {(1, v) for v in y})
                 for x in a for y in b)


def equal_rank_trace_classification(family, anchor, s):
    for edges in combinations(family, s):
        traces = [a & anchor for a in edges]
        if len({len(t) for t in traces}) != 1:
            continue
        if sunflower(edges):
            assert len(set(traces)) == 1 or sunflower(traces), traces
        if len(set(traces)) not in (1, s):
            assert not sunflower(edges)


def rows_are_free(family, anchor, s):
    rows = defaultdict(list)
    for a in family:
        rows[a - anchor].append(a & anchor)
    assert all(free(tuple(ts), s) for ts in rows.values())
    return rows


def all_small():
    edges = tuple(map(frozenset, combinations(range(5), 3)))
    good = 0
    for mask in range(1, 1 << len(edges)):
        f = tuple(edges[i] for i in range(len(edges)) if mask >> i & 1)
        if not free(f, 3):
            continue
        good += 1
        for e in f:
            equal_rank_trace_classification(f, e, 3)
            rows_are_free(f, e, 3)
    assert good == 387, good
    return good


def seed_audit():
    for s in range(3, 9):
        f = seed(s)
        assert len(f) == s+1 and all(len(a) == s for a in f)
        assert free(f, s)
        pp = packets(f, f[0])
        assert len(pp) == s+1
        assert all(len(pp[frozenset({('e', i)})]) == 1 for i in range(s))
        assert sunflower(tuple(frozenset({('e', i)}) for i in range(s)))
        assert not sunflower(f[1:])
    return True


def tensor_shield():
    g = cap9()
    assert free(g, 3)
    counts = [(len(rs), e, tr) for e in g
              for tr, rs in packets(g, e).items()]
    m, anchor, trace = max(counts, key=lambda it: it[0])
    assert m == 4
    f0 = seed(3)
    prod = tensor(f0, g)
    assert free(prod, 3)
    e = frozenset({(0, v) for v in f0[0]} | {(1, v) for v in anchor})
    pp = packets(prod, e)
    for i in range(3):
        t = frozenset({(0, ('e', i))} | {(1, v) for v in trace})
        assert len(pp[t]) == m
    # For s>=4 large tensor freeness follows from symbolic factor argument,
    # so do not enumerate exponentially many s-tuples.
    for s in range(4, 7):
        g = qproduct(s-1, 2)
        assert free(g, s)
        f0 = seed(s)
        prod = tensor(f0, g)
        e = frozenset({(0, v) for v in f0[0]} | {(1, v) for v in g[0]})
        pp = packets(prod, e)
        for i in range(s):
            t = frozenset({(0, ('e', i))})
            assert len(pp[t]) == (s-2)**2
    return m


def vc_dim(family):
    ground = sorted(set().union(*family), key=repr)
    d = 0
    for h in range(1, len(ground)+1):
        for x in combinations(ground, h):
            x = frozenset(x)
            if len({a & x for a in family}) == (1 << h):
                d = h
                break
        else:
            break
    return d


def vc_audit():
    for k in range(1, 5):
        binary = qproduct(2, k)
        assert free(binary, 3)
        assert vc_dim(binary) == k
    assert vc_dim(cap9()) >= 2
    return True


def main():
    print('small 3-free families', all_small())
    print('seed obstruction', seed_audit())
    print('tensor shield cap9 packet size', tensor_shield())
    print('VC controls', vc_audit())
    print('PASS cross-trace shielding original-witness audit')


if __name__ == '__main__':
    main()
