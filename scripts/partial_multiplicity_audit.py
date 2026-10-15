"""Finite diagnostics for original partial-multiplicity certificates and exact central LP."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb


def sunflower(edges):
    return len({frozenset(a & b) for a,b in combinations(edges,2)}) == 1


def defects(edges):
    counts=Counter(x for e in edges for x in e)
    return {x for x,n in counts.items() if 2 <= n < len(edges)}


def all_small_three_free():
    triples=list(map(frozenset,combinations(range(5),3)))
    free=certificates=mass=0
    for mask in range(1,1<<len(triples)):
        f=[e for i,e in enumerate(triples) if mask & (1<<i)]
        if any(sunflower(z) for z in combinations(f,3)):continue
        free+=1
        for E in f:
            groups={}
            for B in f:
                if B!=E:groups.setdefault(B&E,[]).append(B-E)
            for U,V,W in combinations(groups,3):
                if not sunflower((U,V,W)):continue
                for a in groups[U]:
                    for b in groups[V]:
                        for c in groups[W]:
                            assert defects((a,b,c))
                            certificates+=1
                            mass+=len(defects((a,b,c)))
    assert (free,certificates,mass)==(387,420,840)
    return free,certificates,mass


def compulsory_hub_not_a_defect():
    E,A,B,C=map(frozenset,((0,1,2),(0,3,4),(1,3,4),(2,3,5)))
    assert sunflower((A&E,B&E,C&E))
    assert all(not sunflower(z) for z in combinations((E,A,B,C),3))
    assert (A-E)&(B-E)&(C-E)=={3}
    assert defects((A-E,B-E,C-E))=={4}
    return True


def central_lp(s,m,r):
    assert 3<=s<=m and 1<=r<=m-s+1
    masks=list(map(frozenset,combinations(range(m),r)))
    active=0
    for t in combinations(masks,s):
        if not sunflower(t):continue
        common=set.intersection(*map(set,t))
        D=set.union(*map(set,t))-common
        assert len(D)>=s and len(D)%s==0
        active+=1
    assert active>0
    for D in combinations(range(m),s):
        K=set(list(set(range(m))-set(D))[:r-1])
        t=tuple(frozenset(K|{d}) for d in D)
        assert sunflower(t)
        assert set.union(*map(set,t))-set.intersection(*map(set,t))==set(D)
    primal=Fraction(m,s)
    dual=Fraction(comb(m,s),comb(m-1,s-1))
    assert primal==dual
    return s,m,r,active,primal


def h54():
    return [frozenset(I+J) for copy in range(2)
            for i,j in combinations(range(3),2)
            for I in combinations(range(copy*9+3*i,copy*9+3*i+3),2)
            for J in combinations(range(copy*9+3*j,copy*9+3*j+3),2)]


def moments():
    H=h54()
    assert len(H)==54 and len(set(H))==54
    assert not any(sunflower(z) for z in combinations(H,3))
    degree=Counter(x for e in H for x in e)
    assert len(degree)==18 and set(degree.values())=={12}
    private=sum((3*Fraction(d,54)**2*(1-Fraction(d,54)) for d in degree.values()),Fraction())
    assert private==Fraction(56,27)
    direct=Fraction(sum(len(defects((a,b,c))) for a in H for b in H for c in H),54**3)
    assert private==direct
    T=tuple(map(frozenset,((0,1),(0,2),(1,2))))
    assert Fraction(sum(len(defects((a,b,c))) for a in T for b in T for c in T),27)==Fraction(4,3)
    assert {sum(Fraction(1,2)**len(a&b) for b in H) for a in H}=={Fraction(577,16)}
    return private


def main():
    print("original finite three-free",all_small_three_free())
    print("compulsory hub",compulsory_hub_not_a_defect())
    for case in ((3,5,2),(3,7,3),(4,6,2),(5,8,3),(6,7,2)):
        print("central LP",central_lp(*case))
    print("H54 private moment",moments())


if __name__=="__main__":main()
