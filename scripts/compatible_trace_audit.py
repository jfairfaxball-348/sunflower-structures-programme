"""Original intersecting witness trace audits; finite evidence, not an all-rank proof."""
from collections import Counter
from itertools import combinations
from six_petal_factor_audit import factor153

def sunflower(edges):
    return len({a & b for a,b in combinations(edges,2)}) == 1

def sharp_family(s, r):
    assert s >= 3 and 1 <= r <= s-2
    k = r+2
    T = frozenset(range(k-1))
    v = k-1
    xs = tuple(range(k,k+r))
    ys = tuple(range(k+r,k+r+s-1))
    E = T | {v}
    family = [E]
    family += [T | {x} for x in xs]
    family += [frozenset({v,*xs,y}) for y in ys]
    return family,E,v,xs

def check_sharpness():
    for s in range(3,7):
        for r in range(1,s-1):
            family,E,v,xs = sharp_family(s,r)
            assert len(set(family))==len(family)
            assert all(len(e)==r+2 for e in family)
            assert all(a & b for a,b in combinations(family,2))
            assert not any(sunflower(sample) for sample in combinations(family,s))
            opposite = [e for e in family if e & E == {v}]
            assert len(opposite)==s-1
            assert all(frozenset({v,*xs}) <= e for e in opposite)
    return "sharp compatible one-swap original trace families s=3..6 PASS"

def check_multiwitness():
    # A non-singleton exchanged face with two disjoint two-point outside witnesses.
    T=frozenset({0,1,2}); V=frozenset({3,4})
    W1=frozenset({5,6}); W2=frozenset({7,8})
    E=T|V
    F=[E,T|W1,T|W2,frozenset({3,5,7,9,10})]
    assert all(a&b for a,b in combinations(F,2))
    assert not any(sunflower(x) for x in combinations(F,4))
    for U in [frozenset({3}),frozenset({4}),V]:
        for B in F:
            if B&E==U:
                assert B&W1 and B&W2
                assert len(B-U)>=2
    return "two disjoint h=2 original witness packets PASS"

def check_published_obstruction():
    H,_,P=factor153()
    E=frozenset({0,1,10})
    groups={v:set() for v in E}
    for A in H:
        if len(E & A)==2:
            groups[next(iter(E-A))].add(next(iter(A-E)))
    assert {v:len(g) for v,g in groups.items()}=={0:4,1:4,10:4}
    assert {v:sum((A&E)=={v} for A in P) for v in E}=={0:18,1:18,10:18}
    # All forced-rank conclusions would be wrong WITHOUT the intersecting hypothesis.
    return "published 153 factor violates unqualified witness transfer PASS"

def check_overlap():
    _,_,P=factor153()
    ordered=Counter(len(A&B) for A in P for B in P)
    assert ordered=={0:14210,1:7350,2:1696,3:153}
    degrees=Counter(sum(v in A for A in P) for v in range(26))
    assert degrees=={4:1,5:10,27:15}
    assert sum(c*t for t,c in ordered.items())==11201
    # Independently check product overlap convolution with the tiny two-vertex singleton factor.
    Q=[frozenset({0}),frozenset({1})]
    tiny=Counter(len(a&b) for a in Q for b in Q)
    convolved=Counter()
    for i,a in tiny.items():
        for j,b in tiny.items():
            convolved[i+j]+=a*b
    product_family=[frozenset({x,y+2}) for x in (0,1) for y in (0,1)]
    assert Counter(len(a&b) for a in product_family for b in product_family)==convolved
    return "153-factor exact pair spectrum and tensor moment convolution PASS"

def main():
    print(check_sharpness())
    print(check_multiwitness())
    print(check_published_obstruction())
    print(check_overlap())

if __name__=="__main__":
    main()
