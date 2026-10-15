"""Exact original-point-link fractional LP audit. No LP solver required."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

def h54():
    F=set()
    for o in (0,9):
        blocks=[range(o+3*i,o+3*i+3) for i in range(3)]
        for i,j in combinations(range(3),2):
            for a in combinations(blocks[i],2):
                for b in combinations(blocks[j],2):
                    F.add(frozenset(a+b))
    return F

def h39():
    blocks=[range(3*i,3*i+3) for i in range(3)]
    F={frozenset(b) for b in blocks}
    for b in blocks:
        for p in combinations(b,2): F.add(frozenset((9,)+p))
    for (i,j),label in {(0,1):10,(0,2):11,(1,2):12}.items():
        for x in blocks[i]:
            for y in blocks[j]: F.add(frozenset((label,x,y)))
    return F

def h153():
    seeds=((0,1,5),(0,1,6),(0,1,7),(0,1,9),(0,1,10),
           (0,10,12),(0,2,6),(0,2,9),(0,2,10))
    A={frozenset((x+t)%14 for x in seed) for seed in seeds for t in range(14)}
    G={frozenset((i,(i+d)%11)) for i in range(11) for d in (1,2)}
    G|={frozenset((i,i+5)) for i in range(5)}
    B={frozenset({25}|{14+x for x in e}) for e in G}
    return A|B

def pair_star_isolated():
    E=[frozenset(("p",min(i,j),max(i,j)) for j in range(4) if j!=i)
       for i in range(4)]
    E.append(frozenset(("z",i) for i in range(3)))
    return E

def verify(F, packing, cover, objective):
    """Packing: max sum y_E, sum_(E containing x) y_E<=1.
    Cover: min sum z_x, sum_(x in E) z_x>=1.
    Equality is an exact optimality certificate."""
    F=tuple(F)
    loads=Counter()
    for e in F:
        assert packing[e]>=0
        for x in e: loads[x]+=packing[e]
        assert sum((cover.get(x,Fraction(0)) for x in e),Fraction(0))>=1
    assert all(y<=1 for y in loads.values())
    assert all(z>=0 for z in cover.values())
    assert sum(packing.values(),Fraction(0))==objective
    assert sum(cover.values(),Fraction(0))==objective
    return Fraction(1)/objective

def audit():
    F=h54()
    assert len(F)==54
    assert verify(F,{e:Fraction(1,12) for e in F},
                  {x:Fraction(1,4) for x in range(18)},Fraction(9,2))==Fraction(2,9)
    F=h39()
    assert len(F)==39
    assert verify(F,{e:Fraction(1,9) for e in F},
                  {x:Fraction(1,3) for x in range(13)},Fraction(13,3))==Fraction(3,13)
    F=h153()
    assert len(F)==153
    assert verify(F,{e:Fraction(1,27) for e in F},
                  {**{x:Fraction(1,3) for x in range(14)},25:Fraction(1)},
                  Fraction(17,3))==Fraction(3,17)
    F=pair_star_isolated()
    assert len(F)==5 and all(len(e)==3 for e in F)
    assert verify(F,{e:Fraction(1,2) for e in F[:4]}|{F[4]:Fraction(1)},
                  {**{("p",i,j):Fraction(1,3) for i,j in combinations(range(4),2)},
                   ("z",0):Fraction(1)},Fraction(3))==Fraction(1,3)
    words=set(permutations((0,1,2,3,4,4)))
    assert len(words)==factorial(6)//factorial(2)==360
    occurrences=Counter((j,x) for w in words for j,i in enumerate(w) for x in F[i])
    assert set(occurrences.values())=={120}
    assert all(len({a&b,a&c,b&c})>1 for a,b,c in combinations(F,3))
    print("PASS exact H54 2/9, H39 3/13, H153 3/17, pair-star+isolated 1/3; 360 original type words")

if __name__=="__main__":
    audit()
