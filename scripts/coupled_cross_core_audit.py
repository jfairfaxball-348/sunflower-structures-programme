#!/usr/bin/env python3
"""Exact physical-original correlated core and sunflower enumeration."""
from fractions import Fraction
from itertools import combinations, product
from math import comb, isqrt

def family(q,n,m):
    """Use physically private original H=P(q,1) at each (group,index)."""
    assert q>=2 and n>=3 and m>=1
    groups=[]
    for g in range(q):
        block=[]
        for i in range(n):
            shell={('x',g),('y',i)}
            shell|={('p',g,min(i,j),max(i,j)) for j in range(n) if j!=i}
            for word in product(range(q),repeat=m):
                block.append(frozenset(shell|{('h',g,i,t,value) for t,value in enumerate(word)}))
        groups.append(tuple(block))
    return tuple(groups)

def is_sunflower(tup):
    D=tup[0]&tup[1]
    return all(a&b==D for a,b in combinations(tup,2))

def exact_case(q,n,m):
    s=q+1
    groups=family(q,n,m)
    edges=tuple(e for block in groups for e in block)
    L=q**m
    assert len(edges)==q*n*L==len(set(edges))
    assert {len(e) for e in edges}=={n+1+m}
    assert not any(is_sunflower(tup) for tup in combinations(edges,s))
    cross_bad=sum(bool(a&b) for g,h in combinations(groups,2) for a in g for b in h)
    deficit=comb(q,2)*n*L**2
    assert cross_bad==deficit
    assert Fraction(cross_bad,comb(q,2)*(n*L)**2)==Fraction(1,n)
    # Independent samples with replacement of (index I,I',J).
    diff=sum((frozenset({('y',i)}) if i==j else frozenset()) !=
             (frozenset({('y',ip)}) if ip==j else frozenset())
             for i in range(n) for ip in range(n) for j in range(n))
    J=2*Fraction(diff,n**3)
    assert J==Fraction(4*(n-1),n*n)
    assert n*L*q==len(edges)
    return (s,n,m,len(edges),len(edges[0]),deficit,J)

def audit():
    result=[exact_case(*v) for v in ((2,3,1),(2,4,1),(2,3,2),(3,3,1))]
    assert [r[-1] for r in result]==[Fraction(8,9),Fraction(3,4),Fraction(8,9),Fraction(8,9)]
    T=Fraction(5,2)
    assert Fraction(54,1)/T**4==Fraction(864,625)>1
    for m in (16,25,36):
        n=isqrt(m)
        assert 2*n*54**m>T**(n+1+4*m)
    print("PASS: ORIGINAL correlated physical intersection cores, exact fractions:",result)
    return result

if __name__=="__main__":
    audit()
