# Heterogeneous ORIGINAL product multishield dual, density robustness, and all-anchor AS3 audit (15 October 2026)

**Status:** Elementary programme-local theorems HD1–HD4 PROVED, finite tests independently run. Literature novelty **NOT CHECKED**. These are diagnostic lower bounds for a certificate LP, **not** sunflower-size upper bounds. The full unrestricted Erdős–Rado conjecture remains **OPEN**. Every left vertex below is an actual ORIGINAL anchor and actual ORIGINAL petals, never a shifted preimage.

## HD1. Exact global LP for heterogeneous product boxes (PROVED)

Fix s>=3. Let Q=Q(q_1,...,q_k) consist of all original labelled transversals of k disjoint alphabet blocks, 1<=q_j<=s-1. Thus Q has |Q|=product_j q_j distinct k-sets and is s-free (at every coordinate of a sunflower, s symbols must be all equal or s distinct; s distinct symbols are unavailable). An alphabet-1 coordinate is a common-core/frozen coordinate. Let m be the number of variable coordinates (q_j>=2); reorder their sizes nondecreasingly as 2<=b_1<=...<=b_m<=s-1.

For each t>=1 put L=s*t. Let B_t contain ALL anchored ORIGINAL equal-trace-rank rectangles with exactly t private trace vertices per petal, defined precisely as G1/G2 in [GLOBAL_MULTISHIELD_ORIGINAL_OWNERSHIP.md](GLOBAL_MULTISHIELD_ORIGINAL_OWNERSHIP.md). Let V_t(Q) be the exact GLOBAL *actual ground-vertex*, not anchor-copied, fractional defect-cover optimum. Then

    V_t(Q)=0                                                  if m<L;
    V_t(Q)= min_(0<=h<L) (b_1+...+b_(m-h))/(L-h)             if m>=L.    (HD1)

For B_all (all t>=1), V_all(Q)=V_1(Q), by the proof below. If all m=k sizes are the common q=s-1 and k>=L, HD1 gives V_t=q*k/L, recovering G4; for B_all and k>=s it gives q*k/s, recovering G5. The distinction between equal-rank and unequal-rank trace rectangles remains mandatory.

**Proof of exact constraint reduction.** Take a real anchored selection. Each of the s equal-size traces is a sunflower: the private trace parts are pairwise disjoint t-subsets of the anchor, with union D of L distinct coordinate positions. No frozen coordinate can be private, since every original edge agrees with the anchor there. At each j in D, exactly one of the s selected ORIGINAL petals has the anchor symbol. The other s-1 choose from q_j-1<=s-2 alternatives, so at least two must share an outside symbol, with multiplicity between 2 and s-1. Hence every active coordinate supplies an actual defect; there are at least L active variable coordinates. Symmetrise any feasible global vertex weights over independent within-coordinate alphabet permutations. This preserves the LP and objective, producing a uniform weight u_j on EACH symbol at coordinate j, and zero is sufficient on frozen vertices. Feasibility of such a weight vector is ensured by sum_(j in S)u_j>=1 for every L-subset S of variable coordinates (all real selection defects include those L active coordinates).

Conversely EVERY L-subset S of variable coordinates yields a tight ORIGINAL selection: choose an arbitrary actual anchor a; partition S into s disjoint t-sets S_i; the i-th selected ORIGINAL petal agrees with a on S_i and outside S, and replaces a_j with its cyclic next symbol in each coordinate j in S\S_i. The s equal-rank traces have private parts S_i and all the same outside-S core; the original petals are distinct and different from the anchor. Their defect set comprises EXACTLY the L outside vertices (j,a_j+1 mod q_j) for j in S. As the anchor varies, each prescribed defect symbol can appear. Therefore all L-subset inequalities are also NECESSARY after symmetrisation, and HD1 reduces EXACTLY to

    minimise sum_j b_j u_j,   u_j>=0,
    sum_(j in S) u_j>=1 for every |S|=L.                        (HD2)

To solve HD2 sort the nonnegative weights increasingly. All constraints are equivalent to saying the sum of the L SMALLEST weights is >=1; rearrangement puts the LARGEST weights on the CHEAPEST alphabet sizes. Write successive nonnegative differences d_i=u_i-u_(i-1) in this sorted order. Differences after the L-th weight may be set to zero without increasing any of the L smallest, while decreasing cost. The resulting LP has one inequality with coefficients L,L-1,...,1 in d_1,...,d_L and strictly positive objective coefficients. A minimum occurs at one of its L one-positive-variable extreme points. These correspond precisely to h=0,...,L-1 zero weights on the h most expensive coordinates, and weight 1/(L-h) on every other variable coordinate. This gives HD1. For B_all the t=1 constraints suffice because every t>=1 record already has at least s active variable-coordinate defects, and the same s-subset certificate inequality covers them. QED.

**Explicit matching GLOBAL dual.** Take a minimising h, put a=L-h, let C be the cheapest m-h coordinates, H the remaining h expensive ones, and Y=(sum_(j in C)b_j)/a. Optimality against adjacent h implies b_j<=Y for all j in C (when h=L-1 this is automatic), and b_j>=Y for all j in H (when h=0 vacuous). Therefore p_j=b_j/Y (j in C) lies in [0,1] and has sum a. The hypersimplex identity decomposes p as a convex combination of incidence vectors of a-subsets R of C; an exact rational two-coordinate dependent-rounding decomposition is implemented in the audit. Assign dual mass y_(H union R)=Y times that convex probability to every L-subset H union R. Loads on C equal b_j, and on H equal Y<=b_j; total dual mass is Y. To lift this to ACTUAL anchored ORIGINAL selections, for each such L-subset S and each uniformly chosen full-product anchor a use the tight original t-private rectangle above and place dual mass y_S/|Q| on its left record. At a vertex (j,z), this loads exactly (1/b_j)sum_(S contains j)y_S<=1, since the anchor symbol is uniform and the outside defect symbol is a coordinatewise permutation of it. The dual value equals Y=HD1, with NO fictional edge ownership. This is a genuine all-anchor LP primal/dual equality.

Examples: s=4, sizes (2,2,3,3), m=4, V_all=2 rather than naive total-vertex/s=10/4; s=5, sizes (2,2,2,2,4), m=5, V_all=2 rather than 12/5; s=4, sizes (2,3,3,3,3,3), m=6, V_all=17/4. For frozen coordinates (1,2,2,3,3) at s=4, V_all is 2: the common-core point is NEVER a defect.

## HD2. Density-normalised robustness of the GLOBAL dual (PROVED)

Let F be ANY nonempty ORIGINAL subfamily of Q above; write delta=|F|/|Q|. Since Q is s-free, so is F. For each t>=1,

    V_t(F) >= max(0,(s+1)*delta-s) * V_t(Q).                     (HD3)

Likewise with t=1 or all rectangles, V_all(F)>=max(0,(s+1)*delta-s) V_all(Q). Here the normaliser is the ENTIRE |Q|, not |F| or a cherry-picked anchor packet. The interval delta>s/(s+1) is an explicit, provable condition rather than a hidden density hypothesis.

**Proof.** Use the exact full-product ORIGINAL dual in HD1. Each left record is determined by S and an actual uniformly varying anchor word a and owns s+1 DISTINCT original edges: the anchor and s ORIGINAL petals. For fixed S, the anchor map is the identity on Q and each petal-position map from a into its ORIGINAL petal is a bijection of Q (per-coordinate identity or cyclic symbol addition). For each of these s+1 positions the missing-edge probability is 1-delta. A union bound gives probability that ALL s+1 owners lie in F at least 1-(s+1)(1-delta). Restrict the dual mass to these surviving genuine original records. Restricting can only DECREASE actual vertex loads, so it remains feasible. Its objective is at least the stated fraction of the full dual mass. Empty rectangle instances contribute zero. QED.

For F=Q\{one edge}, the union bound on RECORD SURVIVAL is an equality: each left record has s+1 distinct owners, and removal of the one edge makes mutually exclusive position-failure events. This does **not** assert the resulting restricted LP optimum equals the lower bound.

Thus even a dense part of a product can require O(m) global defect-cover weight while still having a constant point link. In fact for any nonempty F subset Q, each variable coordinate j partitions F into at most b_j ORIGINAL point links: max_x deg_F(x)/|F| >=1/b_j. This fixed-fraction link is elementary because a small alphabet was supplied in advance, not obtained from the unrestricted sunflower-free hypothesis. The resulting class-restricted rank recurrence |F|<=b_j f_s(k-1) does NOT yield f_s(k)<=C_s^k for unrestricted original families. Tensor-frozen coordinates and k=0,1 are explicit boundary cases; f_s(0)=1, f_s(1)=s-1.

## HD3. Nonlinear information and density-excess routes: exact failure controls (PROVED identity, OPEN application)

For uniformly selected ORIGINAL word X in F subset Q, under any fixed coordinate order the chain rule gives

    log|Q|-log|F|
     = sum_(j=1)^k [log q_j - H(X_j | X_1,...,X_(j-1))].         (HD4)

This is the KL divergence of the uniform-on-F law from uniform-on-Q, and EXACTLY tensor-additive. It vanishes for F=Q even while HD1's cover is linear in the number m of active coordinates. Conditional entropy uniformity therefore cannot by itself imply bounded global defect budget. For density delta, the total entropy deficit is log(1/delta); Pinsker gives an average conditional-coordinate total-variation bound, but no unrestricted rank recurrence without *first proving a small-alphabet original representation*. This is a diagnosis, not a new sunflower inequality.

The classical floor P(s-1,k) is not a valid universal density threshold: prior-art tensor powers of the actual s-free factors Abbott–Hanson H54 (s=3, rank4, 54 edges), Axante H39 (s=4, rank3, 39) and NONREGULAR H153 (s=6, rank3, 153) have positive per-rank log-density excess over the corresponding P floor:
    s=3: (1/4)log(54/16)>0,
    s=4: (1/3)log(39/27)>0,
    s=6: (1/3)log(153/125)>0.
These excesses are tensor-additive and can grow linearly with rank while the ORIGINAL families remain s-free. Consequently **positive excess over P(s-1,k)** does not force a sunflower. The factors' previously recorded maximum vertex fractions are 2/9,3/13,3/17, respectively; their full edge lists were NOT re-enumerated here and H153 must not be treated as regular. Stronger thresholds could remain possible but are not demonstrated by HD3/HD4.

For arbitrary F, the old universal maximal-matching link bound is still only max_x deg_F(x)>=|F|/((s-1)k); substituting gives f_s(k)<=k(s-1)f_s(k-1), factorial growth. No density-sensitive original-family link theorem above any new explicit base was proved in this investigation. In particular HD1 and HD3 DO NOT imply a noncircular inequality f_s(k)<=C_s^k.

## HD4. The five-edge s=3 alternating shield: ALL-anchor exact LP (PROVED)

The AS3 original seed consists of E={e1,e2,e3}, A1={e1,a,b}, A2a={e2,a,c}, A2b={e2,b,c}, A3={e3,u,v}. It is a simple 3-free family. The COMPLETE all-anchor, nonempty equal-trace-rank triple-rectangle enumeration has precisely THREE left records: two at anchor E with singleton defect sets {a} and {b}, and one at anchor A1 using the triple (E,A2a,A2b), with singleton defect set {c}. There are none at anchors A2a,A2b,A3. Hence its global actual-ground-vertex defect-cover LP is exactly

    V(F_alt,B_all)=3,    with w_a=w_b=w_c=1 forced.               (HD5)

For the SINGLE anchor E, the earlier AS7 cost is 2. Thus true global cross-anchor coupling changes the LP, but a bounded local shield can remain bounded globally on this seed. No permanent vertex certifies all selections. All originals and anchor/trace identities were explicitly enumerated; no conclusion for AS3 tensor powers' global LP is claimed.

## Rank recurrence / research verdict

- **PROVED:** HD1/HD2 exact global fractional LP and explicit dual for all alphabet-size vectors; HD3 density robustness; HD4 entropy identity; HD5 global AS3 example.
- **FALSE as an inference:** linear multishield LP cost, entropy uniformity, and positive excess over the baseline product alone yield a universal ORIGINAL sunflower or a rank-independent point-link theorem.
- **OPEN:** a new *nonseparable* original-witness correlation/ownership inequality above ALL known s-free tensor floors, and a noncircular fixed-base inequality for unrestricted f_s(k).
- **NOT CHECKED:** priority of these elementary LP/entropy formulas in outside mathematical literature. Full unrestricted conjecture is **OPEN**.

Finite script `scripts/heterogeneous_product_dual_audit.py` and six independent `tests/test_heterogeneous_product_dual_audit.py` unit tests use Python stdlib only. They check exact rational primal/dual certificates including t=2, exhaustive ORIGINAL anchored rectangles for (s,k)=(4,4) (81 distinct defect sets for q=(3,3,3,3), and 36 for mixed (2,2,3,3)), single-deletion orbit survival for s=3,4, and the complete three-record AS3 all-anchor result. These finite checks corroborate, not replace, the universal proofs. Full GitHub CI remains a separate exact-head gate.

Source controls: [Mishra v1](https://arxiv.org/html/2606.02667v1) has an invalid cumulative inverse-transfer and its base-2 unrestricted bound is FALSE for s>=4; [v2](https://arxiv.org/html/2606.02667v2) concerns SHIFTED families only. [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367) and [Rao's 2026 survey](https://doi.org/10.1112/jlms.70380) retain the O_s(log k) published baseline. [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995) and [Shangguan](https://arxiv.org/abs/2609.30263) are bounded-VC results with base depending on d; taking d=Omega(k) does not supply a constant base. Finite tensor factor counts are from [Axante et al.](https://arxiv.org/abs/2609.06175), not claimed original here.
