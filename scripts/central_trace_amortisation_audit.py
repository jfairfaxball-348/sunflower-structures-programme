"""Finite independent central-trace and fractional-anchor audits; symbolic proofs in research note."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,m):
    c=[1]
    for _ in range(m): c=multiply(c,a)
    return c

def triangle_q(q,m):
    return [frozenset(e).union(3+j*q+v[j] for j in range(m))
            for e in ((0,1),(0,2),(1,2)) for v in product(range(q),repeat=m)]

def q_spectrum(q,m):
    return multiply([0,2,1],power([q-1,1],m))

def factor54():
    return [frozenset(x+y) for copy in range(2)
            for i,j in combinations(range(3),2)
            for x in combinations(range(copy*9+3*i,copy*9+3*i+3),2)
            for y in combinations(range(copy*9+3*j,copy*9+3*j+3),2)]

def factor153():
    seeds=((0,1,5),(0,1,6),(0,1,7),(0,1,9),(0,1,10),
           (0,10,12),(0,2,6),(0,2,9),(0,2,10))
    cyclic={frozenset((x+t)%14 for x in e) for e in seeds for t in range(14)}
    graph={frozenset((j,(j+d)%11)) for j in range(11) for d in (1,2)}
    graph.update(frozenset((j,j+5)) for j in range(5))
    cone={frozenset({25}|{14+x for x in e}) for e in graph}
    return tuple(cyclic|cone)

def s_free(fam,s):
    return not any(all(a&b==v[0]&v[1] for a,b in combinations(v,2))
                   for v in combinations(fam,s))

def residues(fam,E):
    by={}
    for B in fam:
        U=B&E
        by.setdefault(U,[]).append(B-U)
    return by

def has_disjoint(fam,num):
    return any(all(not a&b for a,b in combinations(sample,2))
               for sample in combinations(fam,num))

def fubini(kmax):
    out=[1]
    for k in range(1,kmax+1):
        out.append(sum(comb(k,u)*out[k-u] for u in range(1,k+1)))
    return out

def check_traces():
    universe=[frozenset(e) for e in combinations(range(5),3)]
    examined=0
    for mask in range(1,1<<len(universe)):
        fam=[universe[j] for j in range(len(universe)) if mask>>j&1]
        if not s_free(fam,3): continue
        examined+=1
        for E in fam:
            for U,R in residues(fam,E).items():
                if U!=E: assert not has_disjoint(R,2)
            if all(a&b for a,b in combinations(fam,2)):
                assert len(fam)<=fubini(3)[3]
    assert examined==387
    assert fubini(5)==[1,1,3,13,75,541]
    star=[frozenset((0,1,2)),frozenset((0,3,4))]
    assert star[0]&star[1] and not (star[0]-{0})&(star[1]-{0})
    four=[frozenset((0,1)),frozenset((0,2)),frozenset((0,3))]
    assert s_free(four,4)
    assert has_disjoint(residues(four,four[0])[frozenset((0,))],2)
    return "PASS exhaustive s=3 proper trace closure and s>=4 counterexamples"

def check_fractional():
    for q in (2,3,4):
        for m in range(1,5):
            fam=triangle_q(q,m)
            N=len(fam)
            coeff=q_spectrum(q,m)
            assert sum(coeff)==N==3*q**m
            for E in fam:
                obs=Counter(len(E&B) for B in fam)
                assert [obs[i] for i in range(len(coeff))]==coeff
            assert coeff[1]==2*(q-1)**m
            p=Fraction(coeff[1],N)
            assert 1/p==Fraction(3*q**m,2*(q-1)**m)
            lam=1/(N*p)
            for B in fam:
                assert lam*sum(len(E&B)<=1 for E in fam)==1
    return "PASS q tensor exact anchored spectrum and optimal LP fractional cover"

def check_factors():
    fam=factor54()
    assert len(fam)==len(set(fam))==54
    a=[27,12,10,4,1]
    for E in fam:
        c=Counter(len(E&B) for B in fam)
        assert [c[i] for i in range(5)]==a
    assert sum(i*v for i,v in enumerate(a))==48
    for m in range(1,4):
        c=multiply([0,2,1],power(a,m))
        assert sum(c)==3*54**m and c[1]==2*27**m
        assert Fraction(3*54**m,c[1])==Fraction(3*2**m,2)
    six=factor153()
    assert len(six)==len(set(six))==153
    cnt=Counter(len(E&B) for E in six for B in six)
    assert tuple(cnt[i] for i in range(4))==(14210,7350,1696,153)
    assert sum(i*cnt[i] for i in range(4))==11201
    assert sum(cnt.values())==23409
    return "PASS H54 per-anchor and H153 ordered overlap profiles"

def main():
    print(check_traces());print(check_fractional());print(check_factors())

if __name__=="__main__": main()
