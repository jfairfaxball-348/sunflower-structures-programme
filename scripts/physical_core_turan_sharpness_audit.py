#!/usr/bin/env python3
"""Exact ORIGINAL finite sunflower and physical-core Turan sharpness checks."""
from fractions import Fraction
from itertools import combinations, product
from math import comb

def tensor_product(seed, m, namespace):
    return [frozenset((namespace, t, x) for t, block in enumerate(word) for x in block)
            for word in product(seed, repeat=m)]

def shielded_copies(s, seed, m, d=0):
    q=s-1
    D=frozenset(('D', i) for i in range(d))
    edges=[]
    groups=[]
    for g in range(q):
        block=tensor_product(seed, m, g)
        groups.append(tuple(D | frozenset({('marker',g)}) | e for e in block))
        edges.extend(groups[-1])
    return tuple(edges),tuple(groups),D

def is_sunflower(tuple_edges):
    c=tuple_edges[0]&tuple_edges[1]
    return all(a&b==c for a,b in combinations(tuple_edges,2))

def turan_edge_count(r,s):
    q=s-1
    a,b=divmod(r,q)
    return (r*r - (b*(a+1)**2+(q-b)*a*a))//2

def check(s,seed,m,common_core):
    F,groups,D=shielded_copies(s,seed,m,common_core)
    assert len(set(F))==len(F)
    assert len({len(e) for e in F})==1
    assert all(not is_sunflower(tup) for tup in combinations(F,s))
    r=len(F); assert r>=s
    bad=sum(a&b!=D for a,b in combinations(F,2))
    rhs=comb(r,2)-turan_edge_count(r,s)
    assert bad==rhs,(bad,rhs)
    same=sum(a&b!=D for a in F for b in F)
    assert Fraction(same,r*r)==Fraction(1,s-1),(same,r)
    assert len(groups)==s-1 and len(set(map(len,groups)))==1
    return (s,m,common_core,len(F),len(F[0]),bad,rhs)

def audit():
    seed2=(frozenset({'a'}),frozenset({'b'}))
    seed3=(frozenset({'a'}),frozenset({'b'}),frozenset({'c'}))
    results=[check(3,seed2,1,0),check(3,seed2,2,0),
             check(3,seed2,2,1),check(4,seed3,1,0),check(4,seed3,1,2)]
    C=Fraction(5,2)
    growth=Fraction(54,1)/C**4
    assert growth==Fraction(864,625)>1
    assert Fraction(2,1)/C==Fraction(4,5)
    assert Fraction(2*54,1)>C**5
    print('PASS: exact physical original s-free Turan equality:',results)
    print('PASS: H54 growth',growth,'packet_cost',Fraction(4,5))
    return results

if __name__=='__main__':
    audit()
