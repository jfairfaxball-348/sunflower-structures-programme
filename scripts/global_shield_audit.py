#!/usr/bin/env python3
"""Finite ORIGINAL q-ary global multishield/owner reuse checks. Stdlib only."""
from itertools import combinations, product


def product_family(s, k):
    assert s >= 3 and k >= 0
    return tuple(frozenset((i, a) for i, a in enumerate(z))
                 for z in product(range(s - 1), repeat=k))


def sunflower(edges):
    edges = tuple(edges)
    return len(set(edges)) == len(edges) and len({
        a & b for a, b in combinations(edges, 2)
    }) == 1


def defects(edges, s):
    return frozenset(x for x in set().union(*edges)
                     if 2 <= sum(x in e for e in edges) <= s - 1)


def all_global_defects(s, k):
    """Enumerate original anchors and equal-rank trace rectangles (small k)."""
    family = product_family(s, k)
    observed = set()
    for anchor in family:
        rows = {}
        for edge in family:
            if edge != anchor:
                rows.setdefault(edge & anchor, []).append(edge)
        for traces in combinations(rows, s):
            if len({len(t) for t in traces}) != 1 or not sunflower(traces):
                continue
            for selection in product(*(rows[t] for t in traces)):
                assert len(set(selection)) == s
                ds = defects(selection, s)
                assert ds and not (ds & anchor)
                observed.add(ds)
    return observed


def tight_original_tuple(s, k, t=1):
    """Witness attaining exactly s*t outside defects for any k>=s*t."""
    assert s >= 3 and 1 <= t and k >= s*t
    q = s - 1
    anchor = frozenset((j, 0) for j in range(k))
    edges = []
    for i in range(s):
        word = [0] * k
        for j in range(s*t):
            if not (i*t <= j < (i+1)*t):
                word[j] = 1 % q
        edges.append(frozenset(enumerate(word)))
    traces = [e & anchor for e in edges]
    assert len({len(x) for x in traces}) == 1 and sunflower(traces)
    assert all(len(e) == k and e != anchor for e in edges)
    assert len(set(edges)) == s and len(defects(edges, s)) == s*t
    assert not sunflower(edges)
    return anchor, edges


def count_owner_reuse(s, k):
    """Count cross-anchor ORIGINAL edge incidence using one tuple/block."""
    assert k >= s
    q = s-1
    b = k//s
    reuse = {edge: 0 for edge in product_family(s, k)}
    defect_load = {(j,a): 0 for j in range(k) for a in range(q)}
    for word in product(range(q), repeat=k):
        anchor = frozenset(enumerate(word))
        for block in range(b):
            chosen = []
            for i in range(s):
                z = list(word)
                for j in range(block*s, (block+1)*s):
                    if j != block*s+i:
                        z[j] = (z[j]+1) % q
                edge = frozenset(enumerate(z))
                assert edge != anchor
                reuse[edge] += 1
                chosen.append(edge)
            traces = [e & anchor for e in chosen]
            assert len({len(t) for t in traces}) == 1 and sunflower(traces)
            ds = defects(chosen, s)
            assert len(ds) == s and not (ds & anchor)
            for x in ds:
                defect_load[x] += 1
    assert set(reuse.values()) == {s*b}
    assert all(defect_load[j,a] == (q**(k-1) if j < s*b else 0)
               for j in range(k) for a in range(q))
    return len(reuse), b, s*b


def main():
    for s,k in ((3,2),(3,3),(3,4)):
        sets = all_global_defects(s,k)
        assert min(map(len,sets), default=0) == (s if k >= s else 0)
        print("global original",s,k,"defect sets",len(sets))
    for s,k,t in ((3,3,1),(3,6,2),(4,4,1),(4,8,2),(5,5,1)):
        tight_original_tuple(s,k,t)
    for s,k in ((3,3),(3,5),(4,4),(4,8),(5,5)):
        print("original owner reuse",s,k,count_owner_reuse(s,k))
    print("PASS: original global multishield dual and ownership witnesses")


if __name__ == "__main__":
    main()
