# Nonvacuous high-density ORIGINAL pair-star wreath: a universal obstruction to fixed point links

15 October 2026. **PROVED internally, original-edge construction, exact rational LP certificates and finite tests. Literature priority NOT CHECKED. Full Erdős–Rado sunflower conjecture remains OPEN.** This note corrects the speculative high-density point-link and fractional-collapse avenues in FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md. None of Mishra v1's original-source transfer is repaired; v2 applies to SHIFTED families only.

## WR1 — Pair-star-shell substitution, genuine original edges (PROVED)

Fix s>=3, a nonempty finite ORIGINAL simple s-sunflower-free d-uniform family H, d>=1 and M=|H|>=1. For integers N>=3 and m>=1, first take the complete disjoint-ground ORIGINAL tensor power T=H^m. It has rank r=dm and W=M^m distinct actual original sets, and remains s-free by the blockwise equal-intersection argument in FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md (FL1).

Let the shell ground be P={{i,j}:1<=i<j<=N}, each unordered pair being a **single actual point** p_ij, and let A_i={p_ij:j != i}, of size N-1. Take N pairwise disjoint relabelled *private physical copies* U_i of the ground of T, also disjoint from P; let T_i be the corresponding relabelled original T. Define

    W_N,m(H) = UNION_(i=1)^N { A_i UNION E : E in T_i }.

All unions denote actual set unions. Different i have distinct A_i for N>=3; different E inside one i are distinct. Every edge therefore is an ORIGINAL distinct set of rank k=N-1+dm, and |W_N,m(H)|=N M^m.

**Sunflower-freeness, including both core types:** consider s distinct candidate petals. If they come from one i, the common shell A_i cancels from their pair intersections, so their original private suffixes would form an s-sunflower in T_i: impossible. If at least two come from group i and another from group j != i, the within-i pair intersection contains ALL A_i, while the cross-i/j intersection has shell part just {p_ij}, a proper subset of A_i (N>=3): impossible regardless of private suffix intersections. Otherwise all s petals come from distinct groups. Their pairwise intersections are exactly shell singletons {p_ij}; for any three distinct indices i,j,l these are three different physical points, so no common pairwise intersection. Exhausts all possible distributions, and excludes empty as well as nonempty cores. No shifting, witnesses from outside the original family, or ghost ancestral edges.

This construction is a structured union of private tensor copies, **not** a subfamily of any single H^m on one shared tensor ground, so the correlated-deletion rigidity FL1c does not apply.

## WR2 — exact ORIGINAL fractional matching/cover and largest point link (PROVED)

Every shell point p_ij lies in exactly 2W actual edges; every private point lies in at most W, since its physical copy belongs to only one group. Hence

    theta(W_N,m(H)) = max_x deg(x)/|W_N,m(H)| = 2/N.

Give EACH original edge packing weight y_E=1/(2W). The load on every shell point is 1; the load on each private point is <=1/2. Thus this is a feasible original-edge fractional matching of total N/2. Independently set actual-point cover weights z_(p_ij)=1/(N-1) at ALL shell pairpoints and zero at all private points. Every original edge A_i UNION E has EXACTLY N-1 shell points, cover value one; the cover objective is choose(N,2)/(N-1)=N/2. Primal=dual rational certificate gives

    nu*(W_N,m(H))=tau*(W_N,m(H))=N/2,
    t(W_N,m(H))=theta(W_N,m(H))=2/N.

Unlike bounded-load tensor powers of one dense H, the entire outer-shell distribution has fractional matching growing linearly with N, despite exponential cardinality in rank.

## WR3 — no *nonvacuous* fixed fractional collapse or positive point-link theorem (PROVED)

Write f_s(d) for the finite maximal size of an ORIGINAL s-free simple d-uniform family; by the classical sunflower lemma these maxima exist. Put

    beta_s=sup_(d>=1) f_s(d)^(1/d).

For any 1<D<beta_s choose finite actual s-free H of some rank d with M^(1/d)>D. Let N_m=max(3,floor(sqrt(m))) (any N_m -> infinity with N_m/m ->0 works). The original family F_m=W_(N_m,m)(H) has

    log|F_m| / rank(F_m)
      = (log N_m + m log M)/(N_m-1+dm)
      -> log(M)/d > log D.

Consequently |F_m|>D^(rank F_m) for all sufficiently large m, while theta(F_m)=2/N_m ->0 and nu*(F_m)=N_m/2 -> infinity. The ranks tend to infinity. More quantitatively, fixing ANY phi>0, B finite and D<beta_s, choose N>max(2/phi,2B,3) and then any integer m large enough that

    m log(M/D^d) > (N-1)log D - log N.

This guarantees simultaneously theta<phi, nu*>B and |F|>D^k. For D<=1 the same construction works because M^(1/d)>1 can be chosen. For D>=beta_s the condition |F|>D^k is vacuous by the definition of beta_s; do not mistake this tautology for a useful positive theorem.

**Hence the formerly proposed strengthened hypothesis** 'there exist nonvacuous D_s<beta_s and fixed B_s so every s-free ORIGINAL F with |F|>D_s^k has nu*(F)<=B_s' is FALSE for every s>=3. Its weaker positive fixed point-link version is likewise FALSE for every nonvacuous D_s. The conditional one-step recurrence f_s(k)<=max(D^k,phi^(-1) f_s(k-1)) remains algebraically correct, but its required high-density PREMISE cannot hold. This closes the entire density-only, single-original-point-link programme—not the conjecture and not more sophisticated multi-point packet/rank-drop mechanisms.

## WR4 — exact finite ORIGINAL high-density adversaries (PROVED)

Choose H from the independently audited published lower-bound factors H54 (s=3, d=4, M=54), H39 (s=4, d=3, M=39) and H153 (s=6, d=3, M=153). Source factors are PRIOR ART. The fully explicit set construction WR1 produces the following actual ORIGINAL counterexamples (the test script checks exact integer inequalities without logarithms):

| s | D | proposed phi | N | m | rank k | number of distinct original edges | theta | nu* |
|---|---|---|---|---|---|---|---|---|
| 3 | 5/2 | 1/5 | 11 | 21 | 94 | 11*54^21 | 2/11 < 1/5 | 11/2 |
| 4 | 10/3 | 1/5 | 11 | 187 | 571 | 11*39^187 | 2/11 < 1/5 | 11/2 |
| 6 | 21/4 | 1/6 | 13 | 311 | 945 | 13*153^311 | 2/13 < 1/6 | 13/2 |

Each row has n*M^m > (a/b)^(d*m+n-1) for the displayed rational D=a/b, by integer test n*M^m*b^k>a^k. At m-1 the opposite weak inequality holds for these fixed N. This gives finite, rank-explicit falsifications of **every numeric candidate in the predecessor prompt**, not just asymptotic disproofs.

The outer construction works with the classical q=s-1 rank-one seed (the q different ORIGINAL singleton sets), so all-s elementary examples exist without published dense finite-factor code. For s=3,4,6 the density bases above have higher documented values 54^(1/4),39^(1/3),153^(1/3) than the classical floors 2,3,5. General beta_s is not determined, nor does any example settle an original fixed-base upper bound.

**Small-rank controls:** f_s(0)=1, f_s(1)=s-1 and f_3(2)=6 (two disjoint original triangles), so an unconditional original coefficient-two recursion starting at k=1 remains FALSE. Our smallest s=3 test has N=3,m=1, q=2: six ORIGINAL rank-three members with theta=2/3 and nu*=3/2, and brute force excludes all C(6,3) distinct triples. Further tests check N=4,m=2, s=3; and s=4,6 small original families. They enumerate both possible core types.

## WR5 — two other strategy attacks and the surviving ORIGINAL rank packet

**High-codegree / conditioning attempt:** Requiring a constant point link, or a constant joint codegree of any nonempty actual set of points, fails on WR1 since a joint star is contained in a single-point star, all of which have mass <=2/N. The flaw in proposed density-sensitive DRC is precisely replacing actual multi-point conditioning by a rank-independent, individually heavy physical point. This fails regardless of exponential cardinality.

**Trace-residue / joint entropy attempt:** FL1c remains valid inside any single tensor power H^m, but WR1 has N *private physically disjoint copies* behind a shell. Marginals onto a single common H factor are not defined across all F. Applying FL1c separately to each packet gives only conditional inner link probabilities; unconditioning incurs 1/N. Treating an abstract factor label as an actual common vertex is an INVALID inference. Any successful proof must quantitatively account for cross-packet multiplicity/trace cost rather than discard it.

**Concrete witness-compatible descent still works ON THIS FAMILY:** choose any shell group i, condition on the full actual anchor A_i (which is an original (N-1)-subset of every member of its packet), retain precisely W=M^m ORIGINAL owners, delete A_i, and recover the actual original rank-dm family T_i. The packet fraction is 1/N, while rank saving is N-1. At any fixed C>1, for N large, 1/N>=C^(-(N-1)); equivalently N<=C^(N-1). Thus simultaneous vanishing point links and **efficient large-rank fibre descent** are possible. This proves no general rank-descent theorem; it identifies a surviving target fundamentally different from a one-point link. A proposed all-F packet theorem must bound the total number, overlap and entropy of actual original-owner packets *without assuming the desired C_s^k bound*.

## WR6 — exact executable, source status and unresolved bridge

- scripts/original_wreath_density_audit.py builds actual small examples (physical shell points and separately labelled private points), exhaustively checks sunflower exclusion, verifies rational packing and physical-point covering constraints, and tests three strict density inequalities using arbitrary-precision integers. tests/test_original_wreath_density_audit.py has independent unittest cases.
- The previous tests scripts/fractional_link_lp_audit.py, scripts/original_pair_star_quadratic_audit.py, scripts/original_owner_balancing_audit.py, scripts/original_nonproduct_tensor_lp_audit.py remain authoritative for their **different** claims.
- Sources rechecked 15 October: Mishra [v1](https://arxiv.org/html/2606.02667v1) universal claimed O_s(2^k) FALSE for s>=4 and original-source transfer invalid; Mishra [v2](https://arxiv.org/html/2606.02667v2) SHIFTED-only. [Axante et al.](https://arxiv.org/abs/2609.06175) supply finite lower factors. [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367) and [Rao 2026](https://doi.org/10.1112/jlms.70380) general logarithmic-base upper regime; [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995) and [Shangguan](https://arxiv.org/abs/2609.30263) bounded-VC dimension-dependent. Wreath-like set-family constructions exist elsewhere (e.g., odd-sunflowers), and the **literature priority of WR1–WR5 is NOT CHECKED**.
- **OPEN:** original-compatible multi-point packet-cover/rank-reduction with an independent fixed base; inter-packet entropy saving; exact correlated defect LPs V_3(T^2) in [16,34] and V_3(AS3 tensor Q9^2) in [11,26]; the full unrestricted conjecture. This session proves NO universal ORIGINAL bound C_s^k.
