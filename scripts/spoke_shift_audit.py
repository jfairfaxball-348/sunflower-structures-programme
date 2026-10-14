"""Finite corroboration of the general spoke-shift theorem; proof is symbolic."""
from itertools import product


def compress(family, i, j):
    old = set(family)
    result = set()
    for edge in old:
        moved = (edge - {j}) | {i}
        if j in edge and i not in edge and frozenset(moved) not in old:
            result.add(frozenset(moved))
        else:
            result.add(edge)
    assert len(result) == len(old)
    return frozenset(result)


def pass_lex(family, n):
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            family = compress(family, i, j)
    return family


def spoke(q, k):
    core = set(range(1, k + 1))
    out = {frozenset(core)}
    for l in range(1, k + 1):
        for a in range(1, q):
            out.add(frozenset((core - {l}) | {l + a*k}))
    return frozenset(out)


def full_product(q, k):
    blocks = [[l + a*k for a in range(q)] for l in range(1, k + 1)]
    return frozenset(frozenset(word) for word in product(*blocks))


def star(q, k):
    core = frozenset(range(1, k))
    return frozenset(core | {j} for j in range(k, q*k + 1))


def check_grid():
    spoke_cases = product_cases = 0
    for q in range(2, 6):
        for k in range(2, 9):
            if q**k > 5000:
                continue
            output = pass_lex(spoke(q, k), q*k)
            assert output == star(q, k), (q, k)
            spoke_cases += 1
            if q**k <= 1024:
                product_image = pass_lex(full_product(q, k), q*k)
                assert star(q, k) <= product_image, (q, k)
                product_cases += 1
    assert spoke_cases == 22 and product_cases == 17, (spoke_cases, product_cases)
    return spoke_cases, product_cases


def main():
    result = check_grid()
    print("PASS: spoke equality and full-product containment", result)


if __name__ == "__main__":
    main()
