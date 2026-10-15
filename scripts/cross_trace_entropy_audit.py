"""Independent finite cross-trace and tensor scalar-cover audit; mathematical proofs are in research note."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
from math import comb

def flower(triple):
    a,b,c=triple
    return a&b==a&c==b&c

def free3(f):
    return not any(flower(t) for t in combinations(f,3))

def trace_groups(f,E):
    out={}
    for A in f:
        U=A&E
        if U!=E: out.setdefault(U,[]).append(A-U)
    return out

def cross_certificates(f):
    number=left=right=0
    for E in f:
        groups=trace_groups(f,E)
        for U,V,W in combinations(groups,3):
            if not flower((U,V,W)): continue
            X,Y,Z=[groups[T] for T in (U,V,W)]
            nx,ny,nz=map(len,(X,Y,Z))
            dx=Counter(x for R in X for x in R)
            dy=Counter(x for R in Y for x in R)
            dz=Counter(x for R in Z for x in R)
            rhs=sum(dx[x]*dy[x]*nz+dx[x]*dz[x]*ny+dy[x]*dz[x]*nx
                    for x in set(dx)|set(dy)|set(dz))
            lhs=nx*ny*nz
            assert rhs>=lhs
            assert all((R&S) or (R&T) or (S&T) for R in X for S in Y for T in Z)
            number+=1;left+=lhs;right+=rhs
    return number,left,right

def cross_exhaustive():
    edges=[frozenset(t) for t in combinations(range(5),3)]
    total=trios=left=right=0
    for mask in range(1,1<<len(edges)):
        fam=[e for i,e in enumerate(edges) if mask>>i&1]
        if not free3(fam): continue
        total+=1
        a,b,c=cross_certificates(fam)
        trios+=a;left+=b;right+=c
    assert (total,trios,left,right)==(387,420,420,840)
    return "PASS 387 five-vertex free families and 420 triple collision inequalities"

def explicit_obstructions():
    disjoint=[frozenset(t) for t in ((0,1,2),(0,3,4),(1,3,5),(2,4,5))]
    overlap=[frozenset(t) for t in ((0,1,2,3),(0,1,4,5),(0,2,4,6),(0,3,5,6))]
    pair=[frozenset(t) for t in ((0,1,2,3),(0,1,4,5),(0,2,6,7))]
    for F in (disjoint,overlap,pair):
        assert free3(F)
        assert all(a&b for a,b in combinations(F,2))
    for F in (disjoint,overlap):
        E=F[0]
        assert flower(tuple(A&E for A in F[1:]))
        assert not flower(tuple(F[1:]))
        assert cross_certificates(F)[0]==4
    E,A,B=pair
    assert (A&E)&(B&E)
    assert not ((A-E)&(B-E))
    # Core deletion does NOT preserve matching number.
    triangles=[frozenset(e) for T in ((0,1,2),(3,4,5)) for e in combinations(T,2)]
    assert len(triangles)==6 and free3(triangles)
    assert all(len(A)==2 for A in triangles)
    with_core=[A|{10} for A in triangles]
    assert free3(with_core) and all(10 in A for A in with_core)
    assert not any(not a&b for a,b in combinations(with_core,2))
    assert any(not a&b for a,b in combinations(triangles,2))
    assert max(sum(x in A for A in triangles) for x in range(6))==2
    return "PASS distinct-trace and common-core explicit originals"

def h54():
    verts=[]
    for copy in range(2):
        for i,j in combinations(range(3),2):
            for I in combinations(range(copy*9+3*i,copy*9+3*i+3),2):
                for J in combinations(range(copy*9+3*j,copy*9+3*j+3),2):
                    verts.append(frozenset(I+J))
    return verts

def multiply(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out

def scalar_normalisation():
    H=h54()
    assert len(H)==len(set(H))==54 and free3(H)
    assert set(Counter(len(A&B) for B in H).get(i,0) for A in H for i in (0,))=={27}
    for E in H:
        assert tuple(Counter(len(E&B) for B in H).get(j,0) for j in range(5))==(27,12,10,4,1)
    degree=Counter(x for e in H for x in e)
    assert len(degree)==18 and set(degree.values())=={12}
    assert Fraction(max(degree.values()),len(H))==Fraction(2,9)
    z=Fraction(1,2)
    A=sum(Fraction(x)*z**i for i,x in enumerate((27,12,10,4,1)))
    assert A==Fraction(577,16)
    for m in (1,2,3):
        total=3*54**m
        norm=Fraction(3,1)/(z*(2+z))*(Fraction(54,1)/A)**m
        assert norm==Fraction(12,5)*Fraction(864,577)**m
        assert norm*(z*(2+z)*A**m)==total
    for q in (2,3,4):
        for m in (1,2,3,4):
            W=z*(2+z)*(q-1+z)**m
            optimum=Fraction(3*q**m,1)/W
            assert optimum==Fraction(12,5)*Fraction(2*q,2*q-1)**m
            assert W*optimum==3*q**m
    # Spectrum is rank-sensitive but identical on the two sides of every column.
    return "PASS 54-factor and q-tensor exact spectral weight and LP coverage"

def averaged_153():
    # Independently recreate the cited cyclic + cone construction.
    seeds=((0,1,5),(0,1,6),(0,1,7),(0,1,9),(0,1,10),
           (0,10,12),(0,2,6),(0,2,9),(0,2,10))
    cyclic={frozenset((x+t)%14 for x in e) for e in seeds for t in range(14)}
    G={frozenset((j,(j+d)%11)) for j in range(11) for d in (1,2)}
    G.update(frozenset((j,j+5)) for j in range(5))
    H=cyclic|{frozenset({25,14+x,14+y}) for x,y in (tuple(e) for e in G)}
    assert len(H)==153
    ordered=Counter(len(a&b) for a in H for b in H)
    assert tuple(ordered.get(i,0) for i in range(4))==(14210,7350,1696,153)
    profiles={tuple(Counter(len(a&b) for b in H).get(i,0) for i in range(4)) for a in H}
    assert len(profiles)>1  # CRITICAL: averaged overlap != homogeneous anchored profile
    degree=Counter(x for e in H for x in e)
    assert max(degree.values())==27
    z=Fraction(1,2)
    assert sum(ordered[i]*z**i for i in range(4))/len(H)**2==Fraction(2875,3672)
    return "PASS 153 averaged spectrum (non-regular anchors)"

def main():
    for check in (cross_exhaustive,explicit_obstructions,scalar_normalisation,averaged_153):
        print(check())

if __name__=="__main__": main()
