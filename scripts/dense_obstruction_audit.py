"""Finite checks of dense graph tensor obstruction; general theorem is symbolic."""
from itertools import combinations, product


def base_graph(q):
    assert q >= 2
    if q % 2 == 0:
        n = 2 * (q + 1)
        graph = {frozenset(pair) for offset in (0, q+1)
                 for pair in combinations(range(offset, offset+q+1), 2)}
    else:
        n = 2*q + 1
        graph = {frozenset((0, 1))}
        graph.update(frozenset((0, x)) for x in range(2, q+1))
        graph.update(frozenset((1, x)) for x in range(q+1, 2*q))
        ring = list(range(2, n))
        for a, b in combinations(range(len(ring)), 2):
            if min(b-a, len(ring)-(b-a)) <= (q-1)//2:
                graph.add(frozenset((ring[a], ring[b])))
    return frozenset(graph), n


def tensor_graph(q, m):
    """Explicitly labelled tensor, with baseline centres 1,...,2m."""
    assert m >= 1
    E, n = base_graph(q)
    K = 2*m
    mapping = {}
    for t in range(m):
        mapping[t, 0] = 2*t+1
        mapping[t, 1] = 2*t+2
        if q % 2:
            for a in range(1, q):
                mapping[t, q+a] = (2*t+1) + a*K
                mapping[t, 1+a] = (2*t+2) + a*K
            mapping[t, 2*q] = q*K+t+1
        else:
            for a in range(2, q+1):
                mapping[t, a] = K+t*(q-1)+a-1
            for a in range(q+1, 2*q+2):
                mapping[t, a] = K+m*(q-1)+t*(q+1)+a-q
    assert set(mapping.values()) == set(range(1, n*m+1))
    local = [tuple(tuple(mapping[t, x] for x in e) for e in E)
             for t in range(m)]
    F = frozenset(frozenset(x for edge in word for x in edge)
                  for word in product(*local))
    assert len(F) == len(E)**m
    return F, n*m


def has_sunflower(combo):
    return len({a & b for a, b in combinations(combo, 2)}) == 1


def check_grid():
    """Keep modest finite domains; full ranks follow from the written proof."""
    from spoke_shift_audit import pass_lex
    summary = []
    for q in range(2, 10):
        E, n = base_graph(q)
        degree = [sum(x in e for e in E) for x in range(n)]
        expected = q*q+(q if q % 2 == 0 else q//2)
        assert len(E) == expected, (q, len(E), expected)
        assert max(degree) == q
        if q <= 4:
            assert all(not has_sunflower(t)
                       for t in combinations(E, q+1)), q
        summary.append((q, len(E)))
    cases = [(2, 1), (2, 2), (2, 3),
             (3, 1), (3, 2), (4, 1), (4, 2), (5, 1)]
    for q, m in cases:
        F, n = tensor_graph(q, m)
        K = 2*m
        if len(F) <= 130:
            assert all(not has_sunflower(t)
                       for t in combinations(F, q+1)), (q, m)
        G = pass_lex(F, n)
        petals = [e for e in G if set(range(1, K)) <= e]
        lower = m*(q-1)+1 if q % 2 == 0 else K*(q-1)+1
        assert len(petals) >= lower, (q, m, len(petals), lower)
        assert all(len(e) == K for e in G)
        summary.append((q, m, len(petals), lower))
    return summary


def main():
    result = check_grid()
    print("PASS: dense graph factors, tensors and ancestor-obstructed lex shifts",
          result)


if __name__ == "__main__":
    main()
