#!/usr/bin/env python3
"""Finite ORIGINAL trace-packet ownership, entropy and capacity audit (stdlib)."""
from collections import Counter,defaultdict
from itertools import combinations,product
from math import comb,log,isclose

def prod(q,k):
    return tuple(frozenset((i,a) for i,a in enumerate(w)) for w in product(range(q),repeat=k))
def cap9():
    return tuple(frozenset(((0,x),(1,y),(2,(x*x+y*y)%3))) for x in range(3) for y in range(3))
def private(k):
    return tuple(frozenset((min(i,j),max(i,j)) for j in range(k+1) if j!=i) for i in range(k+1))
def free(F,s):
    return all(len({a&b for a,b in combinations(S,2)})!=1 for S in combinations(F,s))
def ledger(F,E,C):
    N=len(F); k=len(E); assert N>0 and C>1 and all(len(A)==k for A in F)
    classes=defaultdict(list)
    for A in F: classes[A&E].append(A-E)
    assert sum(map(len,classes.values()))==N
    assert all(len(set(R))==len(R) and all(len(B)==k-len(T) for B in R) for T,R in classes.items())
    H=-sum(len(R)/N*log(len(R)/N) for R in classes.values())
    r=sum(len(T)*len(R)/N for T,R in classes.items())
    slack=sum(len(R)/N*((k-len(T))*log(C)-log(len(R))) for T,R in classes.items())
    assert isclose(k*log(C)-log(N),r*log(C)-H+slack,abs_tol=1e-10)
    return H,r,slack,classes
def capacity(F,s):
    N=len(F)
    for v in set().union(*F):
        owners=[i for i,A in enumerate(F) if v in A]
        d=len(owners)
        if d<2: continue
        m=comb(N-2,s-2)-(comb(d-2,s-2) if d>=s else 0)
        for a,b in combinations(owners,2):
            actual=sum(a in S and b in S and any(v not in F[j] for j in S)
                       for S in combinations(range(N),s))
            assert actual==m,(N,s,v,actual,m)
def small():
    e=list(combinations(range(5),3)); cnt=0
    for mask in range(1,1<<10):
        F=tuple(frozenset(e[i]) for i in range(10) if mask>>i&1)
        if not free(F,3): continue
        cnt+=1
        for E in F: ledger(F,E,3.5)
        if len(F)>=3: capacity(F,3)
    assert cnt==387
    return cnt
def products():
    results=[]
    for s in (3,4,5):
        q=s-1
        for k in (1,2,3):
            F=prod(q,k)
            if len(F)<=27: assert free(F,s)  # for larger products use the symbolic q=s-1 argument
            H,R,slack,_=ledger(F,F[0],q)
            h=-log(1/q)/q-(1-1/q)*log(1-1/q)
            assert isclose(H,k*h,abs_tol=1e-10)
            assert isclose(R,k/q,abs_tol=1e-10)
            assert isclose(slack,k*(1-1/q)*log(q/(q-1)),abs_tol=1e-10)
            if k==2: capacity(F,s)
            results.append((s,k,round(H/R,7)))
    return results
def private_audit():
    out=[]
    for k in (2,3,4,8,32):
        F=private(k);assert free(F,3) and all(len(A&B)==1 for A,B in combinations(F,2))
        H,R,_,classes=ledger(F,F[0],3)
        assert len(classes)==k+1 and isclose(H,log(k+1))
        assert isclose(R,2*k/(k+1)) and isclose(H/R,(k+1)*log(k+1)/(2*k))
        out.append((k,round(H/R,6)))
    return out
def cap_audit():
    F=cap9();assert len(F)==9 and free(F,3)
    N=len(F);degrees=Counter(v for A in F for v in A)
    assert Counter(degrees.values())==Counter({3:6,4:2,1:1})
    assert sum(d*d for d in degrees.values())==87 and N*N==81
    ratios=Counter(round(ledger(F,E,3)[0]/ledger(F,E,3)[1],8) for E in F)
    assert sorted(ratios.values())==[1,4,4]
    return sorted(ratios.items())
def factors():
    for N,k,hist,num,den,phi in (
        (54,4,{12:18},8,9,2/9),
        (39,3,{9:13},9,13,3/13),
        (153,3,{27:15,5:10,4:1},11201,23409,3/17)):
        assert sum(d*n for d,n in hist.items())==N*k
        assert den*sum(n*d*d for d,n in hist.items())==num*N*N
        assert max(hist)/N==phi
    return True
def main():
    print('3-free on five vertices',small())
    print('products',products())
    print('private entropy',private_audit())
    print('cap9 anchor classes',cap_audit())
    print('averaged 54/39/153 degrees',factors())
    print('PASS ORIGINAL PACKET ENTROPY')
if __name__=='__main__':main()
