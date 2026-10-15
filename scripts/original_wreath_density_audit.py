#!/usr/bin/env python3
"""Exact ORIGINAL pair-star-shell witnesses; no floating-point LP certificates."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb

# Each original vertex is (category,index,...), never an inferred shifted point.
def wreath(q=2, m=1, n=3):
    assert 2 <= q and 1 <= m and n >= 3
    E = []
    for i in range(n):
        shell = {('pair',min(i,j),max(i,j)) for j in range(n) if j!=i}
        for word in product(range(q),repeat=m):
            private = {('inner',i,j,letter) for j,letter in enumerate(word)}
            E.append(frozenset(shell|private))
    return tuple(E)

def is_s_free(family,s):
    for edges in combinations(family,s):
        intersections=(edges[i]&edges[j] for i in range(s) for j in range(i+1,s))
        if len(set(intersections))==1:
            return False
    return True

def audit():
    for s,q,n,m in [(3,2,3,1),(3,2,4,2),(4,3,3,1),(6,5,3,1)]:
        family=wreath(q,m,n)
        W=q**m
        rank=n-1+m
        assert len(family)==n*W
        assert len(set(family))==n*W
        assert all(len(e)==rank for e in family)
        assert is_s_free(family,s), (s,q,n,m)
        deg=Counter(x for e in family for x in e)
        assert Fraction(max(deg.values()),len(family))==Fraction(2,n)
        assert all(Fraction(v,2*W)<=1 for v in deg.values())
        assert Fraction(len(family),2*W)==Fraction(n,2)
        assert all(sum(Fraction(1,n-1) for x in e if x[0]=='pair')==1 for e in family)
        assert Fraction(comb(n,2),n-1)==Fraction(n,2)
        print('SMALL',s,q,n,m,len(family),rank,'theta',Fraction(2,n),'nu*',Fraction(n,2))
    for s,n,M,d,num,den,m,phi_num,phi_den in [
        (3,11,54,4,5,2,21,1,5),
        (4,11,39,3,10,3,187,1,5),
        (6,13,153,3,21,4,311,1,6),
    ]:
        k=d*m+n-1
        assert n*M**m*den**k>num**k
        assert n*M**(m-1)*den**(d*(m-1)+n-1)<=num**(d*(m-1)+n-1)
        assert 2*phi_den<n*phi_num
        print('DENSITY',s,'N',n,'m',m,'rank',k,'edge_digits',len(str(n*M**m)),
              'theta',Fraction(2,n),'nu*',Fraction(n,2),
              'density_threshold',f'{num}/{den}', 'strictly_above',True)
    print('PASS exact original shell incidence, all-core sunflower checks, rational LP duality, integer density thresholds')
if __name__=='__main__': audit()
