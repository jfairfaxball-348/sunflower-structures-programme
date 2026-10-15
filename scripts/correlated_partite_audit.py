#!/usr/bin/env python3
"""Exact finite original-transversal witnesses and support/entropy checks."""
from collections import Counter
from fractions import Fraction
from itertools import product,combinations
from math import factorial,log,exp

def product_family(q,k): return tuple(product(range(q),repeat=k))
def defects(rows):
    s=len(rows)
    assert s>=3
    return tuple(i for i in range(len(rows[0])) if any(
        2<=v<s for v in Counter(r[i] for r in rows).values()))
def cap9(): return tuple((x,y,(x*x+y*y)%3) for x in range(3) for y in range(3))
def multiply(xs):
    z=Fraction(1)
    for x in xs: z*=x
    return z
def support(family,s):
    family=tuple(family); N=len(family); k=len(family[0])
    ps=[]
    for i in range(k):
        cnt=Counter(x[i] for x in family)
        ps.append({a:Fraction(t,N) for a,t in cnt.items()})
    gamma=multiply(sum((p**s for p in pm.values()),Fraction(0))
      +factorial(s)*sum((multiply(t) for t in combinations(pm.values(),s)),Fraction(0))
      for pm in ps)
    def mass(x): return multiply(ps[i][a] for i,a in enumerate(x))
    theta=sum((mass(x) for x in family),Fraction(0))
    diag=sum((mass(x)**s for x in family),Fraction(0))
    collision=sum((p*p for pm in ps for p in pm.values()),Fraction(0))
    T=sum(-float(p)*log(float(p)) for pm in ps for p in pm.values())-log(N)
    return gamma,theta,diag,collision,T
def check(family,s):
    assert all(defects(t) for t in combinations(family,s))
    gamma,theta,diag,collision,T=support(family,s)
    assert theta**s<=1-gamma+diag
    assert theta**s<=Fraction(s*(s-1),2)*collision+diag
    assert exp(-T)<=float(theta)+1e-10
    return gamma,theta,diag,T
def witness(s,m,i,j):
    assert 0<=i<j<m and m>=2
    rows=[]
    for a in range(s-1):
        x=[0]*m; x[i]=a; rows.append(tuple(x))
    x=[0]*m; x[j]=1; rows.append(tuple(x))
    assert len(set(rows))==s and defects(rows)==(i,j)
    return tuple(rows)
def main():
    for s,m in ((3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(6,2)):
        fam=product_family(s-1,m)
        assert all(len(defects(t))>=2 for t in combinations(fam,s))
        for i,j in combinations(range(m),2): witness(s,m,i,j)
        g,t,d,T=check(fam,s)
        assert t==1 and g==d==Fraction(1,len(fam)**(s-1)) and abs(T)<1e-9
    cap=cap9()
    assert len(set(cap))==9
    check(cap,3)
    grid=product_family(3,2); best=0
    for mask in range(1<<len(grid)):
        fam=tuple(grid[i] for i in range(len(grid)) if mask>>i&1)
        if all(defects(t) for t in combinations(fam,3)):
            best=max(best,len(fam))
    assert best==4
    print("PASS: actual original tuple LP pair witnesses, exact rational partite entropy, cap9, rank-two")
if __name__=="__main__": main()
