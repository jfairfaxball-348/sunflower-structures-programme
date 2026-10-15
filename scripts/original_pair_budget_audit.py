#!/usr/bin/env python3
"""Finite original-edge pair-certificate audit; stdlib proofs, optional SciPy."""
from fractions import Fraction
from collections import Counter
from itertools import combinations, product
from math import comb

def product_family(q, k):
    return tuple(product(range(q), repeat=k))

def cap9():
    return tuple((x, y, (x*x + y*y) % 3) for x in range(3) for y in range(3))

def defects(words):
    s = len(words)
    return tuple(i for i in range(len(words[0])) if any(
        1 < sum(w[i] == a for w in words) < s for a in {w[i] for w in words}))

def certificates(family):
    return tuple((i, a, b) for i in range(len(family[0]))
                 for a, b in combinations(range(len(family)), 2)
                 if family[a][i] == family[b][i])

def covered_by(family, cert, chosen):
    i, a, b = cert
    return a in chosen and b in chosen and any(family[c][i] != family[a][i] for c in chosen)

def verify_binary_fractional_certificates(m):
    assert m >= 2
    family = product_family(2, m)
    N = len(family)
    cert = certificates(family)
    primal = {}
    for c in cert:
        _, a, b = c
        d = sum(x != y for x, y in zip(family[a], family[b]))
        assert 1 <= d < m
        primal[c] = Fraction(1, d + 1)
    for chosen in combinations(range(N), 3):
        assert sum((primal[c] for c in cert if covered_by(family, c, chosen)), Fraction()) >= 1
    upper = sum(primal.values(), Fraction())
    assert upper == Fraction(N*(N-m-1), 2)
    for c in cert:
        count = sum(covered_by(family, c, chosen) for chosen in combinations(range(N), 3))
        assert count == N // 2
    lower = Fraction(2*comb(N, 3), N)
    assert lower == Fraction((N-1)*(N-2), 3)
    assert lower <= upper
    return (m, N, len(cert), lower, upper)

def enumerate_no_sunflower(family, s):
    return all(defects(edges) for edges in combinations(family, s))

def solve_optional_lp(family, s):
    """Exploratory optimisation only; does not prove a universal theorem."""
    try:
        import numpy as np
        from scipy.optimize import linprog
        from scipy.sparse import lil_matrix
    except ImportError:
        return None
    cert = certificates(family)
    tuples = tuple(combinations(range(len(family)), s))
    A = lil_matrix((len(tuples), len(cert)), dtype=float)
    for j, selected in enumerate(tuples):
        for h, c in enumerate(cert):
            if covered_by(family, c, selected):
                A[j, h] = 1
        assert A.rows[j], (s, selected, 'unexpected original sunflower')
    result = linprog([1.0]*len(cert), A_ub=-A.tocsr(),
                     b_ub=-np.ones(len(tuples)), bounds=(0, None), method='highs')
    assert result.success, result.message
    return round(float(result.fun), 8)

def averaged_factor_pair_spectrum(family):
    N = len(family)
    degrees = Counter(v for edge in family for v in edge)
    histogram = Counter(degrees.values())
    pair_certificates = sum(comb(d, 2) for d in degrees.values())
    three_way_incidence = sum(comb(d, 2)*(N-d) for d in degrees.values())
    return N, dict(sorted(histogram.items())), pair_certificates, three_way_incidence

def audit_published_factors():
    try:
        from high_rank_tensor_audit import factor54
        from six_petal_factor_audit import factor153
    except ImportError:
        return None
    H54, _ = factor54()
    _, _, H153 = factor153()
    a, b = averaged_factor_pair_spectrum(H54), averaged_factor_pair_spectrum(H153)
    assert a == (54, {12: 18}, 1188, 49896), a
    assert b == (153, {4: 1, 5: 10, 27: 15}, 5371, 679084), b
    return a, b

def main():
    for m in (2, 3, 4):
        print('binary fractional pair bound', verify_binary_fractional_certificates(m))
    for s, fam in ((3, product_family(2, 3)), (3, cap9()),
                   (4, product_family(3, 2)), (5, product_family(4, 2))):
        assert enumerate_no_sunflower(fam, s)
        print('partite finite factor', s, len(fam),
              'rank', len(fam[0]), 'certificates', len(certificates(fam)),
              'optional solver optimum', solve_optional_lp(fam, s))
    print('published factor averaged pair spectra', audit_published_factors())
    print('PASS: original pair-certificate finite audit')

if __name__ == '__main__':
    main()
