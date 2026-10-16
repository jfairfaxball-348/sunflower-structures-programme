# Two-anchor shared-ground residuals: exact fractional cover, universal trace payments, and primitive-capacity barrier

16 October 2026. **Programme-internal, mathematically proved statements, not a claim of literature novelty.** All edges are actual distinct physical sets. The full unrestricted Erdős–Rado sunflower conjecture remains OPEN.

## TAP1. A uniform physical triangle lift with exact cover invariants (PROVED)

For s>=3, let H be any nonempty simple s-sunflower-free d-uniform family, d>=0. Use physical triangle vertices a,b,c, and mutually private ground copies X_1,X_2,X_3 of the support of H. Put T_1={a,b}, T_2={b,c}, T_3={a,c}. Define

    U_s(H) = { T_i union h^(i) : i in {1,2,3}, h in H }.       (TAP1)

No shifted petals or abstract proxies occur. It is a simple (d+2)-uniform family of 3|H| actual owners. For every s>=3:

* U_s(H) is s-free. In a purported s-sunflower, repeated triangle indices and a different index are impossible: the repeated pair's shell intersection is a full two-point T_i but a cross-index pair's shell intersection has size one. Thus indices are all equal or all distinct. For s>3 all distinct is impossible; for s=3 the three distinct triangle edges have pairwise shell intersections {a},{b},{c}, which differ. All equal would produce an s-sunflower of distinct private H copies, excluded.
* It is intersecting (triangle edges pairwise meet), **globally core-free**, and has integral transversal number tau_cover(U)=2. The shell pair {a,b} hits all three shell classes; no single physical point hits all three classes (triangle vertices hit two, a private point at most one).
* Its fractional vertex-cover and fractional matching optima are BOTH exactly 3/2. The rational cover weighting each of a,b,c by 1/2 gives weight 3/2 and covers every member with equality. The rational matching assigning weight 1/2 to one selected original member of each of the three private classes is feasible: each triangle vertex sees exactly two selected edges and every private vertex at most one. Both certificates have weight 3/2; weak duality proves equality, with no LP solver approximation.
* Any shattered physical coordinate set V for H is still shattered by U, inside one private class; hence VCdim(U)>=VCdim(H). No bounded-VC conclusion follows from tau_cover=2 or tau_fractional=3/2.

This strictly strengthens LRC4's core-free intersecting equivalence by fixing TWO separate transversal invariants at the smallest possible nontrivial values. It does not prove an upper bound.

## TAP2. Exact two-anchor original-owner decompositions (PROVED, upper *reductions* not new universal upper estimates)

Let F be any nonempty s-free rank-k ORIGINAL family, k>=2, with a physical transversal {x,y}. Assign every E containing x to owner x; assign the rest to y. Removing the assigned physical vertex produces two distinct s-free rank-(k-1) families F_x, F_y, and the assignment is injective within each slice:

    |F|=|F_x|+|F_y| <= 2 f_s(k-1).                      (TAP2)

No edge is counted twice; shared residual points are allowed. This is an actual-owner upper decomposition for the tau_cover<=2 class, NOT for all original F.

Independently partition by exact trace on {x,y}, obtaining disjoint original rows A (trace {x}), B (trace {y}), C (trace {x,y}). Their residual ranks are k-1,k-1,k-2; each row is s-free, and

    |F|=|A|+|B|+|C| <= 2 f_s(k-1)+f_s(k-2).             (TAP3)

When F is intersecting, A and B are cross-intersecting in the common residual physical ground: their original markers are disjoint. The three row families need NOT be independent; deleting the markers does not make a single s-free union. This decomposition permits unrestricted original shared-ground reuse, unlike LRC5's private substitution.

For U_s(H), choose x=a,y=b. Every one of A,B,C has exactly |H| original members (each from one triangle class); the canonical x/y split has 2|H| and |H|. The residual of the row C is literally a private copy of arbitrary H. Also the full x-link of U has disjoint b- and c-marked branches; its fractional matching number is 2, with two singleton branch markers giving a cover of 2. Thus the tightly specified tau_fractional=3/2 class is NOT closed under even this legitimate rank-lowering link. These exact witnesses block an induction that silently reapplies TAP1's special invariant to its link.

For comparison, the known prior-art Abbott–Exoo / Axante shared-ground attachment J(A,C) uses two marker variants of the same intersecting rank-(k-1) family A and a doubly replicated intersecting rank-(k-2) family C. It yields a LOWER construction recurrence a_k>=2a_(k-1)+2a_(k-2), with characteristic root 1+sqrt(3). This is NOT an upper recurrence for f_s(k). The 2 f(k-1)+f(k-2) in TAP3 also does NOT close an induction over all originals: the two children are bounded by the unknown unrestricted f_s, and F need not have a two-point cover.

## TAP3. A sharply defined primitive residual class retains the FULL exponential growth capacity (PROVED)

For k>=2 let b_s(k) be the maximum size of a rank-k simple original s-free family with (i) pairwise intersecting edges, (ii) empty total physical intersection, (iii) integral cover number EXACTLY 2 and (iv) fractional cover number EXACTLY 3/2. These are genuine numerical conditions, not a reference to an unknown construction grammar.

From TAP1 and the canonical reduction TAP2, for all d>=0,

    3 f_s(d) <= b_s(d+2) <= 2 f_s(d+1).                (TAP4)

The upper inequality follows by setting k=d+2 in TAP2, and does not use the extra structural conditions. All quantifiers include arbitrary original grounds and arbitrary seeds; f_s(0)=1. By disjoint-ground tensor closure for s-free uniform originals and the elementary Fekete limit,

    lim_(k->infty) b_s(k)^(1/k) = lim f_s(k)^(1/k)
                              = beta_s in [1,infinity]. (TAP5)

This identity includes the possibility beta_s=infinity: logarithmic shifts of rank by a constant do not change the extended limit. In fact, suppose any proposed estimate b_s(k)<=exp(eps(k) k) C^k for all sufficiently large k, where eps(k)->0 and C>=1 is fixed. For ANY d>=1 and ANY s-free original H with M=|H|, apply TAP1 to H^m, obtaining

    3 M^m <= b_s(dm+2) <= exp(o(dm)) C^(dm+2).

Taking m-th roots gives M<=C^d. Therefore this proposed *subexponential-overhead fixed-base* bound on the strongly restricted primitive class would PROVE f_s(d)<=C^d for all d and the entire unrestricted conjecture. The reverse implication is immediate with overhead 1. Hence this apparently primitive capacity hypothesis is logically equivalent in strength to the full unresolved bound, not an independent bootstrap input.

In particular no argument using only intersectingness, empty common physical core, tau_cover=2, tau_fractional=3/2 and large rank can charge the arbitrary H residual for free. The correct gap is a **universally produced class with an additional genuinely contracting property**, proved to arise from arbitrary F rather than postulated.

## TAP4. High-VC physical stress test and two unsuccessful proof routes

Let q=s-1>=2 and H=P(q,m), the classical q-ary rank-m product on m physical blocks. It is s-free with q^m originals. The m designated coordinate-zero points are shattered: choose zero or a nonzero symbol independently in each block. TAP1 yields rank m+2 and 3q^m owners, while tau_cover=2 and tau_fractional=3/2 EXACTLY and VCdim>=m. Thus VCdim/rank tends to one even within the narrowly fixed invariant class. Taking H=G^m for arbitrary better-than-q finite seeds G produces the same obstruction at every nonvacuous density threshold T<beta_s. At T<beta_s choose G of rank d with |G|>T^d, so 3|G|^m/T^(dm+2)->infinity.

**Attempt A, finite-rank matrix/spectral closure.** TAP2 gives an honest coefficient 2 on a proper rank-drop for restricted F; TAP3 gives an honest three-row payment. A fixed spectral radius is feasible for a *supplied closed construction grammar*, as in LRC5–LRC6, but arbitrary two-covered F conceal arbitrary original H behind a rank-(k-2) row, and even the fractional-invariant class is not stable under a link. No all-F fixed-base upper system was obtained.

**Attempt B, primitive residual and high-VC dichotomy.** Fixing both integral and fractional transversals to their smallest core-free intersecting values does not lower exponential capacity (TAP5); shattering survives with linear VC. Ge–Wang–Xu–Zhao and Shangguan obtain C(s,d_VC)^k bounds with dimension-dependent bases, so these results cannot simply be substituted when d_VC=Theta(k). The original point/packet and Turán-LRC obstructions remain relevant; no universal structural decomposition producing a smaller independently certified residual class has been established.

**Controls:** P(s-1,k) satisfies the required (s-1)^k lower control; the two-triangle disjoint rank-two s=3 original seed is also tested. No assertion is made about the previously certified 16<=V_3(T^2)<=34 and 11<=V_3(S tensor Q9^2)<=26 LP intervals. No purported new literature lower bound follows from this embedding.

## TAP5. External sources, exact auditor and verdict

Classical triangle, products/Fekete, matching-cover duality and Abbott-style attachments are **prior art**. The programme's packaging in TAP1–TAP5 is internally proved but **external priority has NOT been audited**. Axante–Budala–Chitic–Dumitru–Nacu, https://arxiv.org/html/2609.06175v1 section 2.4 establishes product/Fekete and section 3 explicitly identifies the block recurrences as LOWER bounds, with Abbott–Exoo antecedents. Mishra https://arxiv.org/html/2606.02667v1 has a false s>=4 O_s(2^k) consequence and invalid cumulative original-source attribution; https://arxiv.org/html/2606.02667v2 applies to SHIFTED families only. Bounded-VC sources: https://arxiv.org/abs/2609.18995 and https://arxiv.org/abs/2609.30263. The classical beta_3>=sqrt(10) is stronger than the J grammar lower root; no new priority is claimed.

Independent stdlib auditor `scripts/two_anchor_primitive_capacity_audit.py` constructs literal original physical sets for s=3,4,6, verifies actual cardinalities and ranks, exhaustive small-case freeness, nonempty pair intersections, core-freeness, integral cover witnesses, exact rational primal and dual fractional-cover certificates, trace partitions and linear VC witnesses. Its finite tests are corroboration, not proofs of the symbolic all-rank statements.

**VERDICT: TAP1–TAP5 proved as scoped structural statements. Full original Erdős–Rado sunflower conjecture OPEN. No universal exponential upper bound, no proof of finite-grammar universality, no literature novelty claim.**
