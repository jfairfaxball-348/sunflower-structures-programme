#!/usr/bin/env python3
"""Exact integer owner-balancing certificate for all-ORIGINAL AS3 x Q9 records.

No SciPy is needed to verify the certificate. Record indices use the deterministic
enumeration in original_nonproduct_tensor_lp_audit.rectangle_records.
"""
from collections import defaultdict
from original_nonproduct_tensor_lp_audit import seed, cap9, tensor, rectangle_records, COVER

DENOM = 656234357670
CERT = (
 (15,23167335970),(128,19910756588),(135,100510819568),
 (168,286207073598),(204,90306583542),(302,90141886092),
 (308,86173012923),(316,73031014923),(417,10401990745),
 (491,119683643597),(623,5992544281),(672,273029360192),
 (753,26117202415),(817,98311142345),(851,158722601197),
 (1088,48852619547),(1125,18086602363),(1446,67871026505),
 (1538,41393148645),(1638,220508142971),(1748,52409746677),
 (1820,262256167),(1930,119989012305),(2167,70724284188),
 (2184,109724185446),(2187,154854920872),(2300,153078021163),
 (2700,41835643796),(2831,42548930308),(2902,80982143254),
 (3044,76279125503),(3125,10219449310),(3206,24787416298),
 (3233,61212279741),(3267,2718287023),(3299,66460618843),
 (3316,138518733785),(3436,139396582140),(3605,88298647830),
 (3648,61737453019),(3699,118381431843),(3820,190443491204),
 (4008,173715426452),(4079,102343953544),(4204,130563645569),
 (4224,26354458374),(4374,21219229608),(4429,157830620185),
 (4547,54025521589),(4572,273635516004),(4646,255407162642),
 (4685,90583906663),(4890,79058154121),(4934,36650543086),
 (5042,1032204518),(5611,34471516344),(5661,143803446717),
 (5957,5898387222),
)

def loads(family, records, weighted_records):
    owners = defaultdict(int)
    vertices = defaultdict(int)
    for index, numerator in weighted_records:
        assert numerator > 0
        anchor, petals, defect = records[index]
        distinct = (anchor,) + tuple(petals)
        assert len(set(distinct)) == 4
        assert all(edge in family for edge in distinct)
        assert defect and not defect & anchor
        for edge in distinct:
            owners[edge] += numerator
        for vertex in defect:
            vertices[vertex] += numerator
    return owners, vertices

def audit():
    F = tensor(seed(), cap9())
    records = tuple(rectangle_records(F))
    assert len(F) == 45 and len(records) == 6403
    assert len(CERT) == 58 and len(set(i for i, _ in CERT)) == 58
    assert sum(w for _, w in CERT) == 8 * DENOM
    o, v = loads(F, records, CERT)
    assert set(o) == set(F)
    assert all(o[edge] == 32 * DENOM // 45 for edge in F)
    assert 32 * DENOM % 45 == 0
    assert all(v[vertex] <= DENOM for vertex in set().union(*F))
    assert all(COVER & D for _, _, D in records)
    # Eight-unit primal cover + eight-unit feasible dual establish V=8.
    # Any y with total Y has sum_e m_e = 4Y, so M >= 4Y/45.
    # The exact dual above has M=32/45, proving lambda_min=1.
    S, Q = seed(), cap9()
    sr, qr = tuple(rectangle_records(S)), tuple(rectangle_records(Q))
    assert len(sr) == 3 and len(qr) == 20
    so, sv = loads(S, sr, ((0,1),(1,1),(2,1)))
    assert max(so.values()) == 3 and all(t <= 1 for t in sv.values())
    assert all(S[0] in (a,*p) and S[1] in (a,*p) for a,p,d in sr)
    # Every Q record is owned by Q[0], or has defect vertex (2,1).
    # For any dual y of mass Y=3, m_{Q[0]} >= Y - load_{(2,1)} >= 2.
    assert all(Q[0] in (a,*p) or (2,1) in d for a,p,d in qr)
    qo, qv = loads(Q, qr, ((7,1),(10,1),(12,1)))
    assert max(qo.values()) == 2 and all(t <= 1 for t in qv.values())
    print("PASS: exact 58-term balanced Q9 tensor dual, V=8, lambda=1")
    print("PASS: factor optimum congestion AS3=5/4, Q9=3/2")

if __name__ == "__main__":
    audit()
