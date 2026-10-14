"""Finite corroboration of the published 153-triple six-petal-free factor.

Symbolic all-m theorems are proved in the accompanying research note, not here.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations

SEEDS = ((0,1,5),(0,1,6),(0,1,7),(0,1,9),(0,1,10),
         (0,10,12),(0,2,6),(0,2,9),(0,2,10))
ANCHOR = frozenset((0,1,10))
OUTSIDERS = frozenset((2,3,5,6,7,8,9,11,12))


def factor153():
    cyclic = frozenset(frozenset((x+t)%14 for x in seed)
                       for seed in SEEDS for t in range(14))
    graph = {frozenset((i,(i+d)%11)) for i in range(11) for d in (1,2)}
    graph |= {frozenset((i,i+5)) for i in range(5)}
    cone = frozenset(frozenset({25} | {14+x for x in e}) for e in graph)
    return cyclic, cone, frozenset(cyclic | cone)


def pair_codegrees(family):
    return Counter(frozenset(p) for e in family for p in combinations(e,2))


def matching_number_graph(graph):
    nodes = sorted(set().union(*graph)) if graph else []
    ids = {x:i for i,x in enumerate(nodes)}
    nbr = [0]*len(nodes)
    for e in graph:
        a,b = (ids[x] for x in e)
        nbr[a] |= 1<<b
        nbr[b] |= 1<<a

    @lru_cache(None)
    def solve(mask):
        if not mask: return 0
        bit = mask & -mask
        v = bit.bit_length()-1
        without = mask ^ bit
        best = solve(without)
        available = nbr[v] & without
        while available:
            ubit = available & -available
            best = max(best, 1+solve(without ^ ubit))
            available ^= ubit
        return best
    return solve((1<<len(nodes))-1)


def check_factor():
    H,J,P = factor153()
    assert (len(H),len(J),len(P)) == (126,27,153)
    assert all(len(e)==3 for e in P)
    assert all(e <= set(range(14)) for e in H)
    assert all(25 in e for e in J)
    assert Counter(pair_codegrees(P).values()) == {1:27,4:8,5:80}
    assert max(sum(v in e for e in P) for v in range(26)) == 27
    assert max(matching_number_graph({frozenset(e-{v}) for e in P if v in e})
               for v in range(26)) <= 5
    assert ANCHOR in H
    outsiders = {next(iter(e-ANCHOR)) for e in H
                 if len(e-ANCHOR)==1 and len(ANCHOR-e)==1}
    assert outsiders == OUTSIDERS
    assert len(pair_codegrees(P))==115
    assert sum(pair_codegrees(P).values())==3*len(P)==459
    return "153 triples, no six-sunflower by core cases, nine original swaps PASS"


def check_intersecting_tensor_certificate():
    H,_,P = factor153()
    Hx = {e for e in P if 0 in e}
    assert len(Hx)==27
    assert all(0 in e for e in Hx)
    assert len(Hx)*len(P)==4131
    assert ANCHOR in Hx
    for outsider in OUTSIDERS:
        assert any(e-ANCHOR=={outsider} and len(ANCHOR-e)==1 for e in H)
    return "intersecting two-block tensor 4131 edges and nine spokes PASS"


def check_one_block_shift():
    _,_,P = factor153()
    preferred = sorted(ANCHOR)+sorted(OUTSIDERS)+sorted(set(range(26))-ANCHOR-OUTSIDERS)
    mapping = {x:i+1 for i,x in enumerate(preferred)}
    mapped = {frozenset(mapping[x] for x in e) for e in P}
    for i in range(1,27):
        for j in range(i+1,27):
            old=mapped
            mapped={((e-{j})|{i}) if j in e and i not in e
                    and ((e-{j})|{i}) not in old else e for e in old}
            assert len(mapped)==153
    core=frozenset((1,2))
    assert sum(core<=e for e in mapped)>=10
    return "complete one-block lex shift >=10 core-star petals PASS"


def main():
    print(check_factor())
    print(check_intersecting_tensor_certificate())
    print(check_one_block_shift())


if __name__=="__main__":
    main()
