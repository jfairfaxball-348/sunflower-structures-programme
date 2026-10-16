#!/usr/bin/env python3
"""Literal original-set and Fraction audits for TAP1--TAP5."""
from fractions import Fraction
from itertools import combinations, product

TRIANGLE=(frozenset(("a","b")),frozenset(("b","c")),frozenset(("a","c")))

def sunflower_free(family,s):
    fam=tuple(family)
    assert len(fam)==len(set(fam))
    for petals in combinations(fam,s):
        core=petals[0]&petals[1]
        if all(a&b==core for a,b in combinations(petals,2)):
            return False
    return True

def product_family(q,d):
    return tuple(frozenset((j,t) for j,t in enumerate(word))
                 for word in product(range(q),repeat=d))

def triangle_lift(seed):
    return tuple(frozenset(('triangle',p) for p in t)|
                 frozenset(('private',i,p) for p in a)
                 for i,t in enumerate(TRIANGLE) for a in seed)

def cover_number_at_most_one(fam):
    pts=set().union(*fam)
    return any(all(x in edge for edge in fam) for x in pts)

def canonical_two_cover(fam,x,y):
    assert all(x in edge or y in edge for edge in fam)
    a=tuple(edge-{x} for edge in fam if x in edge)
    b=tuple(edge-{y} for edge in fam if x not in edge)
    assert len(a)+len(b)==len(fam)
    return a,b

def trace_three_rows(fam,x,y):
    assert all(x in edge or y in edge for edge in fam)
    return (tuple(edge-{x} for edge in fam if x in edge and y not in edge),
            tuple(edge-{y} for edge in fam if y in edge and x not in edge),
            tuple(edge-{x,y} for edge in fam if x in edge and y in edge))

def vc_witness(seed,q,d):
    v=frozenset(('private',0,(j,0)) for j in range(d))
    fam=triangle_lift(seed)
    assert {frozenset(e&v) for e in fam}=={
        frozenset(('private',0,(j,0)) for j in range(d) if (bits>>j)&1)
        for bits in range(2**d)}
    return v

def audit():
    checks=[]
    for s,d in ((3,1),(3,2),(3,3),(4,1),(4,2),(6,1)):
        H=product_family(s-1,d)
        F=triangle_lift(H)
        assert len(F)==3*len(H)==len(set(F))
        assert {len(e) for e in F}=={d+2}
        assert sunflower_free(H,s)
        if len(F)<=24: assert sunflower_free(F,s)
        assert all(a&b for a,b in combinations(F,2))
        assert not set.intersection(*(set(e) for e in F))
        assert not cover_number_at_most_one(F)
        shell=[frozenset({('triangle',p)}) for p in "abc"]
        assert all(sum((Fraction(1,2) for v in shell if v<=e),Fraction())==1
                   for e in F)
        selected=(F[0],F[len(H)],F[2*len(H)])
        for v in set().union(*F):
            assert sum((Fraction(1,2) for e in selected if v in e),Fraction())<=1
        assert sum((Fraction(1,2) for _ in selected),Fraction())==Fraction(3,2)
        x,y=('triangle','a'),('triangle','b')
        a,b,c=trace_three_rows(F,x,y)
        assert tuple(map(len,(a,b,c)))==(len(H),)*3
        first,second=canonical_two_cover(F,x,y)
        assert (len(first),len(second))==(2*len(H),len(H))
        assert sunflower_free(first,s) and sunflower_free(second,s)
        vc_witness(H,s-1,d)
        checks.append((s,d,len(F),d+2,Fraction(3,2)))
    seed=tuple(map(frozenset,((0,1),(1,2),(0,2),(3,4),(4,5),(3,5))))
    assert sunflower_free(seed,3)
    assert sunflower_free(triangle_lift(seed),3)
    return checks

if __name__=="__main__":
    for x in audit():print("PASS",x)
    print("PASS two-anchor primitive residual exact certificates")
