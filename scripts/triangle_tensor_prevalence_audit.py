"""Finite independent triangle-tensor prevalence audits; symbolic all-rank proofs live in research note."""
from collections import Counter
from itertools import combinations, product
from math import comb

def factor54():
    out = []
    for copy in range(2):
        for i, j in combinations(range(3), 2):
            for x in combinations(range(copy*9+3*i, copy*9+3*i+3), 2):
                for y in combinations(range(copy*9+3*j, copy*9+3*j+3), 2):
                    out.append(frozenset(x+y))
    return out

def check_h54_spectrum():
    family=factor54()
    assert len(family)==len(set(family))==54
    ordered=Counter(len(a&b) for a in family for b in family)
    assert ordered=={0:1458,1:648,2:540,3:216,4:54}, ordered
    assert all(sum(bool(a&b) for b in family)==27 for a in family)
    assert sum(j*v for j,v in ordered.items())==18*12**2
    assert not any(len({a&b for a,b in combinations(sample,2)})==1 for sample in combinations(family,3))
    return "54-factor full ordered overlap and anchor intersection checks PASS"

def q_count_formula(q,m,H):
    def c(j):
        return comb(m,j)*(q-1)**(m-j) if 0<=j<=m else 0
    return 2*sum(c(j) for j in range(H)) + sum(c(j) for j in range(H-1))

def check_q_exact_traces():
    for q in range(2,6):
        for m in range(1,6):
            E=frozenset([0,1]+[3+j*q for j in range(m)])
            family=[]
            for edge in ((0,1),(0,2),(1,2)):
                for symbols in product(range(q),repeat=m):
                    family.append(frozenset(edge).union(3+j*q+symbols[j] for j in range(m)))
            assert len(set(family))==len(family)==3*q**m
            assert not set.intersection(*(set(a) for a in family))
            for H in (1,2,3):
                observed=sum(len(a&E)<=H for a in family)
                assert observed==q_count_formula(q,m,H),(q,m,H,observed)
    return "triangle tensor q-product exact low trace spectrum q=2..5,m=1..5 PASS"

def main():
    print(check_h54_spectrum())
    print(check_q_exact_traces())

if __name__=="__main__":
    main()
