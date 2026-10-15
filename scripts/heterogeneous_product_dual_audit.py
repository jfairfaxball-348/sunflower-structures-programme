#!/usr/bin/env python3
"""Exact rational heterogeneous ORIGINAL product LP and finite anchor audit; stdlib only."""
from fractions import Fraction as Q
from itertools import combinations, product
from math import prod, log

def words(palettes):
    return tuple(product(*(range(q) for q in palettes)))

def edge(word):
    return frozenset((i,a) for i,a in enumerate(word))

def sunflower(edges):
    return len(set(edges))==len(edges) and len({a & b for a,b in combinations(edges,2)})==1

def defect(edges):
    return frozenset(x for x in set().union(*edges) if 2<=sum(x in e for e in edges)<=len(edges)-1)

def all_global_defects(s,palettes,private_t=1):
    family=tuple(map(edge,words(palettes)))
    found=set()
    for anchor in family:
        rows={}
        for A in family:
            if A!=anchor:
                rows.setdefault(A & anchor,[]).append(A)
        for traces in combinations(rows,s):
            sizes={len(T) for T in traces}
            if len(sizes)!=1 or not sunflower(traces):
                continue
            core=set.intersection(*(set(T) for T in traces))
            if next(iter(sizes))-len(core)!=private_t:
                continue
            for petals in product(*(rows[T] for T in traces)):
                assert len(set(petals))==s
                D=defect(petals)
                assert D and not D & anchor
                found.add(D)
    return found

def theoretical_value(s,palettes,t=1):
    q=sorted(x for x in palettes if x>=2)
    m,L=len(q),s*t
    if m<L: return Q(0)
    return min(Q(sum(q[:m-h]),L-h) for h in range(L))

def dual_decomposition(p):
    """Rational two-coordinate rounding: p in hypersimplex -> vertex distribution."""
    p=tuple(p)
    assert all(0<=v<=1 for v in p) and sum(p).denominator==1
    ids=[i for i,v in enumerate(p) if 0<v<1]
    if not ids:
        return [(Q(1),frozenset(i for i,v in enumerate(p) if v==1))]
    i,j=ids[:2]
    plus=min(1-p[i],p[j]); minus=min(p[i],1-p[j])
    A,B=list(p),list(p)
    A[i]+=plus; A[j]-=plus
    B[i]-=minus; B[j]+=minus
    alpha=minus/(plus+minus)
    return [(alpha*w,S) for w,S in dual_decomposition(A)]+[((1-alpha)*w,S) for w,S in dual_decomposition(B)]

def exact_primal_dual(s,palettes,t=1):
    q=sorted((x,i) for i,x in enumerate(palettes) if x>=2)
    m,L=len(q),s*t
    if m<L:return Q(0),{},{}
    h=min(range(L),key=lambda z:Q(sum(x for x,_ in q[:m-z]),L-z))
    cheap,expensive=q[:m-h],q[m-h:]
    a=L-h
    Y=Q(sum(x for x,_ in cheap),a)
    primal={i:(Q(1,a) if (x,i) in cheap else Q(0)) for x,i in q}
    dual={}
    for probability,S in dual_decomposition([Q(x,Y) for x,_ in cheap]):
        full=frozenset([i for _,i in expensive]+[cheap[j][1] for j in S])
        dual[full]=dual.get(full,Q(0))+Y*probability
    assert sum(dual.values())==Y
    assert sum(palettes[i]*v for i,v in primal.items())==Y
    for S in combinations([i for _,i in q],L):
        assert sum(primal[j] for j in S)>=1
    for i,x in enumerate(palettes):
        if x>=2:assert sum(y for S,y in dual.items() if i in S)<=x
    return Y,primal,dual

def tight_orbit(s,k):
    q=s-1
    for anchor in product(range(q),repeat=k):
        for S in combinations(range(k),s):
            petals=[]
            for singled in S:
                w=list(anchor)
                for j in S:
                    if j!=singled:w[j]=(w[j]+1)%q
                petals.append(tuple(w))
            assert len(set(petals)|{anchor})==s+1
            assert defect(tuple(map(edge,petals)))==frozenset((j,(anchor[j]+1)%q) for j in S)
            yield anchor,tuple(petals)

def orbit_survival(s,k,subfamily):
    total=kept=0
    for anchor,petals in tight_orbit(s,k):
        total+=1
        kept+=int(anchor in subfamily and all(w in subfamily for w in petals))
    return Q(kept,total)

def seed_all_anchor_defects():
    E=frozenset([('e',0),('e',1),('e',2)])
    family=(E,frozenset([('e',0),'a','b']),frozenset([('e',1),'a','c']),
            frozenset([('e',1),'b','c']),frozenset([('e',2),'u','v']))
    assert not any(sunflower(t) for t in combinations(family,3))
    found=set(); records=[]
    for anchor in family:
        rows={}
        for A in family:
            if A!=anchor:rows.setdefault(A & anchor,[]).append(A)
        for traces in combinations(rows,3):
            if len({len(T) for T in traces})==1 and sunflower(traces):
                for tup in product(*(rows[T] for T in traces)):
                    D=defect(tup)
                    found.add(D);records.append((anchor,tup,D))
    return found,records

def main():
    for s,p in ((3,(2,2,2)),(3,(2,2,2,2)),(4,(3,3,3,3)),(4,(2,2,3,3)),
                (4,(1,2,2,3,3)),(5,(2,2,2,2,4)),(4,(2,3,3,3,3,3)),(3,(1,2,2,2,2,2))):
        v,w,y=exact_primal_dual(s,p)
        assert v==theoretical_value(s,p)
        print('palettes',s,p,'LP',v,'dual records',len(y))
    for s,p,n in ((3,(2,2,2),8),(3,(2,2,2,2),32),(4,(3,3,3,3),81),
                  (4,(2,2,3,3),36),(4,(1,2,2,3,3),36)):
        Ds=all_global_defects(s,p)
        assert len(Ds)==n and min(map(len,Ds))==s
        print('original rectangles',s,p,len(Ds))
    for s,k in ((3,3),(3,4),(4,4)):
        whole=set(words([s-1]*k))
        assert orbit_survival(s,k,whole)==1
        reduced=whole-{sorted(whole)[0]}
        assert orbit_survival(s,k,reduced)==Q(1)-Q(s+1,len(whole))
    Ds,recs=seed_all_anchor_defects()
    assert len(recs)==3 and Ds=={frozenset({'a'}),frozenset({'b'}),frozenset({'c'})}
    print('PASS: exact original LP, density orbit, all-anchor AS3')

if __name__=='__main__':main()
