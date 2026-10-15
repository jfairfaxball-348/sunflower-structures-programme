#!/usr/bin/env python3
"""Exact all-anchor ORIGINAL multishield audit with stdlib only."""
from collections import defaultdict
from itertools import combinations, product

def seed():
    return tuple(map(frozenset, (
        ('e1','e2','e3'),('e1','a','b'),('e2','a','c'),
        ('e2','b','c'),('e3','u','v'))))

def cap9():
    return tuple(frozenset(((0,x),(1,y),(2,(x*x+y*y)%3)))
                 for x in range(3) for y in range(3))

def tensor(left,right):
    return tuple(frozenset({('A',x) for x in a}|{('B',x) for x in b})
                 for a,b in product(left,right))

def sunflower(edges):
    return len(set(edges))==len(edges) and len({a&b for a,b in combinations(edges,2)})==1

def defects(edges):
    return frozenset(x for x in set().union(*edges)
                     if 2<=sum(x in e for e in edges)<len(edges))

def rectangle_records(family,s=3):
    for anchor in family:
        packets=defaultdict(list)
        for edge in family:
            if edge!=anchor:
                t=edge&anchor
                if t:packets[t].append(edge)
        for ts in combinations(packets,s):
            if len({len(t) for t in ts})!=1 or not sunflower(ts):continue
            for picked in product(*(packets[t] for t in ts)):
                if len(set(picked)|{anchor})!=s+1:
                    raise AssertionError('non-distinct ORIGINAL owners')
                D=defects(picked)
                if not D or D&anchor:
                    raise AssertionError('original sunflower or bad anchor defect')
                yield anchor,picked,D

COVER=frozenset({('A',t) for t in ('a','b','c','e3','u')}|
                {('B',t) for t in ((0,0),(1,0),(2,1))})

DUAL_DEFECTS=(
    frozenset({('A','a')}),frozenset({('A','b')}),
    frozenset({('A','c')}),frozenset({('B',(0,0))}),
    frozenset({('B',(1,0))}),frozenset({('B',(2,1))}),
    frozenset({('A','u'),('A','v'),('B',(0,1)),('B',(1,1))}),
    frozenset({('A','e1'),('A','e3'),('B',(0,2)),
               ('B',(1,2)),('B',(2,2))}))

def audit():
    for F in (seed(),cap9()):
        assert not any(sunflower(t) for t in combinations(F,3))
    for name,F,expected,singleton in (
       ('AS3',seed(),(3,3),3),
       ('Q9',cap9(),(20,7),3),
       ('AS3_Q9',tensor(seed(),cap9()),(6403,457),6)):
        records=tuple(rectangle_records(F))
        sets={r[2] for r in records}
        assert (len(records),len(sets))==expected,(name,len(records),len(sets))
        assert sum(len(D)==1 for D in sets)==singleton
        if name=='AS3_Q9':
            assert len(F)==45 and len(set().union(*F))==17
            assert len(COVER)==8 and all(COVER&D for D in sets)
            assert all(D in sets for D in DUAL_DEFECTS)
            assert len(DUAL_DEFECTS)==8
            assert sum(map(len,DUAL_DEFECTS))==len(set().union(*DUAL_DEFECTS))
            for D in DUAL_DEFECTS:
                witness=next((r for r in records if r[2]==D),None)
                assert witness is not None
                assert witness[0] in F and all(p in F for p in witness[1])
        print(name,'edges',len(F),'records',len(records),'defect sets',len(sets))
    print('PASS: exact all-anchor AS3 x Q9 LP 8; factors 3 + 3')

if __name__=='__main__':audit()
