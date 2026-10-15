# Working proof — direct Mishra v1/v2 investigation (14 October 2026)

**Verdict: OPEN. There is no full proof of the unrestricted Erdős–Rado Sunflower Conjecture.**

Notation: F is a finite simple k-uniform set family. An s-sunflower consists of s DISTINCT members with a common pairwise intersection (possibly empty); s>=3. Write tau(F) for maximum sunflower cardinality, with tau(empty)=0 and tau(singleton)=1; f_s(k) for maximum size of an s-free k-family, and f'_s(k) for the shifted-only maximum. Assertions about s-free families always mean tau(F)<=s-1. All logarithms below are natural. Main sources: [v1](https://arxiv.org/html/2606.02667v1), [v2](https://arxiv.org/html/2606.02667v2).

## 1. Independent check of the usable v2 core

**Shadow.** For k>=1 and any F, count pairs (E,A) with E a (k-1)-subset of A in F. There are k|F| pairs; each E belongs to at most tau(F) extensions, since those extensions form a sunflower with core E. Therefore

    k|F| <= tau(F) |partial F|.                                        (1)

No shiftedness is required. For empty families treat (1) as 0<=0.

**Shifted half-link.** Let F be globally shifted with tau(F)<=k; let B_i be the members avoiding [i] and A_i members of B_(i-1) containing i. For every (k-1)-set D in partial B_i, some j>i has D+{j} in B_i, so shiftedness implies D+{i} in A_i. These i-extensions are distinct as D varies. Thus |A_i|>=|partial B_i|>=k|B_i|/tau(B_i)>=|B_i| whenever B_i is nonempty; when empty, the inequality is trivial. Hence 2|A_i|>=|B_(i-1)|. A crucial prerequisite is that B_(i-1) remains i-compressed, which follows because each member avoids [i-1] and replacements of j>i by i do not introduce earlier vertices.

**Link closure.** If F is shifted, its link L_1={A\{1}:1 in A in F} is shifted under all pairs 2<=i<j<=n: replace j with i in A and use shiftedness of F, then remove 1.

**Rank recurrence.** When k>=s and F is s-free, tau(F)<=s-1<=k. From the half-link, |L_1|>=|F|/2. The link is itself s-free (else adding 1 produces s distinct original members). Therefore

    f'_s(k) <= 2 f'_s(k-1)   (k>=s).                                  (2)

The source's small-rank estimate can be proved without shifting: take a maximal matching M of size at most s-1 in an s-free family. Its union U has |U|<=k(s-1); every F-member meets U. Some x occurs in at least |F|/[k(s-1)] sets, and its rank-(k-1) link is s-free. Induction from f_s(1)=s-1 gives f_s(k)<=s^(2k) for k<=s (indeed for k<=s the displayed induction factor k(s-1)<=s^2). The source's references to s+1 petals and 'more than s' are indexing/slip errors: only s petals follow from the stated inductive hypothesis. Combining with (2),

    f'_s(k) <= s^(2s-2) * 2^k                                         (3)

for all k>=1 (loose but valid). In particular the v2 shifted-family conclusion can be independently derived. No claim that v2 implies the full unrestricted theorem.

**One shift.** Under C_ij each shifted output has a unique old-family ancestor differing exactly by j->i; an unchanged output has itself as ancestor. Split any image sunflower into shifted and unchanged outputs. Unchanged outputs form an original sunflower. All shifted outputs contain i, omit j; their ancestors replace the common i by common j and consequently form an original sunflower. Therefore

    tau(C_ij(F)) <= 2 tau(F).                                          (4)

This bound is SHARP: for m>=3, take m edges {1,a_r} and m edges {2,b_r}, all 2m leaves distinct and outside {1,2}. Original tau=m (two disjoint stars); C_12 makes one star with 2m petals. This settles the one-step estimate, NOT an n-independent bound under arbitrarily many shifts. Source v2 Appendix B partitions one step correctly, unlike v1's cumulative source claim.

## 2. More precise negative results

**V1 invalid.** P(q,k) is the family of all transversals of k disjoint q-vertex blocks. It has q^k members and tau=q: q members varying in one coordinate form a sunflower, and a sunflower of q+1 distinct transversals is impossible (each coordinate would have to be identical across all or use q+1 distinct symbols). For s=q+1>=4, P(q,k) defeats any universal O_s(2^k) bound, including v1's (3s^2)^(6s^2-2) 2^k. The v1 §3 claimed unique ORIGINAL single-source inverse is invalid for full shifts: {{3,4}} goes to {{1,2}}. Original sunflowers also need not survive the inverse: {{2,3},{1,4},{1,5}} is 3-free but C_12 produces the star {{1,3},{1,4},{1,5}}.

**Sharp obstruction to extracting a shifted ORIGINAL subfamily (proved).** Fix any total ordering of the qk points of P(q,k), with k>=2. Every globally shifted subfamily H contained in P(q,k) has

    |H| <= q.                                                          (5)

Proof: if H is nonempty, repeated downward replacements give [k] in H. If [k] is not a transversal, contradiction. Thus [k] contains precisely one point from each block, each being the first point of that block in the order. Let A in H and suppose i in [k-1] is absent. Choose the block whose prefix representative is i+1. Its unique A-point j is >=i+1>i (because its first point is i+1). Replacing j by i is required by shiftedness, but creates two points in the block of i and none in the block of i+1, contradicting H subset P. Therefore every A includes [k-1]. The final vertex must belong to the single block whose representative is k, which has q choices. Hence |H|<=q. This holds for **every order**, not merely a favourable example. For k=1 the same q bound is trivial. There is no constant- or polynomial-fraction globally shifted subfamily of the original product as k grows.

**Failure of unconditional constant-fraction link.** For any k>=2 construct k+1 original sets A_i={e_{ij}: j != i} for i=1,...,k+1, each e_{ij}=e_{ji} a private vertex for unordered pair {i,j}. These k-sets have pairwise intersections {e_{ij}}, pairwise different over every triple, hence are 3-free. Each ground vertex lies in exactly two sets; max link fraction is 2/(k+1), tending to zero. Thus a rank-independent half-link statement for arbitrary s-free families is false. This does not refute a **large exponential-family-only** link/dichotomy.

**Product implies significant full-shift sunflower inflation.** Independently verified (3), let G be ANY shifted family with |G|=q^k, q>=3, and let t=tau(G). Apply (3) with s=t+1 to G (assuming t>=1):

    q^k <= (t+1)^(2t) 2^k,
    2t log(t+1) >= k log(q/2).                                       (6)

Thus t=Omega_q(k/log(k+2)). For G=S(P(q,k)), original tau=q. Consequently no bound tau(SF)<=g(tau(F)) independent of rank can hold, and even any admissible rank-dependent bound must permit inflation of at least order k/log k for fixed q>=3. This is an UNCONDITIONAL no-go here because (3) was independently proved.

## 3. A valid restricted replacement bridge (proved, but insufficient)

**Bounded-support labelled inverse lemma.** Suppose a bijection pi:F->G preserves the outside of a fixed finite U, meaning A\U=pi(A)\U for all A in F. This holds in particular for any sequence of compressions C_ij with both i,j in U. Then

    tau(G) <= 2^|U| tau(F).                                           (7)

Proof: take an m-sunflower in G and transport its m distinct members to their distinct original ancestors. Colour each ancestor by its intersection with U (at most 2^|U| colours). Among >=ceil(m/2^|U|) same-colour ancestors, pairwise intersections outside U equal the original image core outside U, while intersections inside U are the fixed colour. Thus, whenever at least two such ancestors exist, they are a sunflower in F. For a one-member class the inequality follows from tau(F)>=1. This proof handles distinctness, the empty core, and arbitrary compositions supported within U.

For |U|<=b_s, (7) followed by (3) would give a valid C_s^k estimate **if** a sufficiently large arbitrary original subfamily can be compressed into a globally shifted family using operations only within U. No such structural/extraction theorem is established; products and (5) prevent a simplistic large shifted-original subfamily argument. If |U| grows with k, the factor 2^|U| becomes a large sunflower parameter in (3), giving superexponential losses in general.

## 4. Exact quantitative candidate and its danger

**Conditional rank-dependent bridge (implication correct but premise now DISPROVED).** Suppose for a fixed s there exists A_s>=1 such that for every s-free rank-k original family with k>=2 its full-shift image G satisfies

    tau(G) <= A_s k / log(k+2).                                       (H_s)

Let D_s=A_s+1. With u=tau(G)+1, u<=D_s k/log(k+2). Apply (3) to the shifted G with sunflower target u:

    |F|=|G|<=2^k u^(2u-2)
        <= [2 exp(2D_s(1+log(D_s)/log(4)))]^k.

For k=1 take at most s-1 singleton sets. Hence H_s would prove the unrestricted conjecture with

    C_s=max(s-1, 2 exp(2D_s(1+log(D_s)/log(4)))).

Equation (6) previously supplied a necessary Omega_q(k/log k) inflation, not a sufficient upper bound. The new [spoke-shift theorem](SPOKE_SHIFT_THEOREM.md) proves the stronger Omega_q(k) inflation for the specific lexicographic full shift, for EVERY q>=2 and rank k>=2, including binary products and a sparse q-ary subfamily. Thus H_s is FALSE for every fixed s>=3 under that shift order. The conditional implication above remains logically correct but cannot prove the conjecture because its premise is refuted.

**Other explored routes.** Arbitrary original link reduction loses a factor up to k(s-1) per rank and reproduces factorial bounds, not C_s^k. Indefinite one-step shift multiplication costs 2^T with T potentially depending on n. Global fixed-support colouring is rigorous but too expensive for growing support. Literal shifted-original subfamily extraction is destroyed by (5). Heavy stars have high links but cannot cover pair-private or product arrangements. None of these routes closes the full theorem.

## 5. Checkable finite diagnostics and exact next obligation

Run: python3 scripts/bridge_audit.py and python3 -m unittest discover -s tests -v.

Exhaustively enumerated all 2048 subfamilies of the 2- and 3-layers on [5]; verified (1), (4), cardinality preservation, shifted half-link and shifted link closure. Exhaustively enumerated all 15 pair partitions of [6], all 256 subfamilies of each P(2,3), and verified (5) in those 3840 cases; some achieve size 2. Checked (4) at equality via 4+4 two-star edges and the pair-private 3-free construction. These computations corroborate the symbolic proofs and are not substitutes for them. Product full-shift star growth reported above is only checked for k<=8.

**Decisive unresolved task:** The H_s problem is RESOLVED NEGATIVELY. Prove an ORIGINAL-witness-preserving structural theorem for sufficiently large s-free families, or an ancestor-compatible transfer, yielding O_s(1) exponential cost per rank. Sparse spokes, q-products and pair-private families are mandatory adversarial tests. All constants must be independent of k and n. **No complete proof has been obtained.**

## 6. New universal symbolic obstruction: spoke-to-star compression (PROVED)

The full proof is in [SPOKE_SHIFT_THEOREM.md](SPOKE_SHIFT_THEOREM.md). For each q>=2, k>=2, let T(q,k) consist of [k] and the (q-1)k coordinate neighbours [k]\\{l}+{l+ak}, 1<=l<=k, 1<=a<=q-1. It is contained in P(q,k), has EXACTLY (q-1)k+1 distinct original members and tau(T)=q. In one lexicographic compression pass, T becomes the COMPLETE star {[k-1]+{j}:k<=j<=qk}; P(q,k) contains this same star after compression, with persistence under all subsequent shifts. The proof tracks B_t(x)=([k]\\{t})+{x}: the pair C_(t,t+1) either creates B_(t+1)(x) or leaves an already existing one, and previous phases cannot disturb it. This resolves the previous finite-only observation for ALL ranks. Thus tau(S(P(q,k)))>=(q-1)k+1, and H_s with q=s-1 is FALSE for EVERY fixed s>=3, not merely unproved. No arbitrary shift-order assertion is claimed. The shifted-only recurrence cannot close the conjecture from this tau alone.

Finite corroboration: `python3 scripts/spoke_shift_audit.py` checks 22 spoke cases and 19 q-product cases; symbolic quantifiers rest on the induction, not testing. The original rank-reduction and origin-compatible witness transfer problems remain OPEN.


## 7. Exponential-density ancestor obstruction beyond the product base (PROVED, 14 October 2026)

See [DENSE_ANCESTOR_OBSTRUCTION.md](DENSE_ANCESTOR_OBSTRUCTION.md) for complete proofs, orderings, and tests. This is a new adversarial lemma for this **programme**, not a claim of novelty for the classical rank-2 extremal graph problem.

For q=s-1>=2, construct a rank-2 original q-free graph H_q of exactly M_q edges, where M_q=q(q+1) when q is even (two K_(q+1) components), and M_q=q^2+(q-1)/2 when q is odd (double-star plus a (q-1)-regular circulant). Both have maximum degree and matching number at most q, so no (q+1)-star or (q+1)-matching, and each contains a q-star. Their m-fold disjoint-coordinate tensor powers F_(q,m) have rank K=2m, original sunflower number q EXACTLY, and |F|=M_q^m=(sqrt(M_q))^K. The tensor preservation lemma tau(F tensor G)=max(tau(F),tau(G)) for nonempty uniform factors is proved by projecting a putative sunflower: in each factor its petals are either all identical or all distinct with constant pairwise intersection.

A stronger partial-spoke lemma handles arbitrary additional edges and shifting collisions. If a rank-K family contains [K] and r different initial spokes ([K]\{l_x})+{x}, with x>K distinct and l_x in [K], then one complete lex pass yields >=r+1 distinct edges with core [K-1]. Their core-membership count cannot decrease under later elementary compressions. Explicit labels give for H_q tensor m: r=K(q-1) when q is odd, and r=m(q-1) when q is even. Therefore the shifted image has tau >=r+1=Omega_q(K) although original tau=q and original size is exponential with base b_q=sqrt(M_q)>q=s-1.

Hence the false rank-dependent H_s is **still false even restricted to s-free original families of size >=D^K for every D<=b_(s-1)** (arbitrarily large even K). This does not exclude a restriction at a larger unknown D, and does not prove the full conjecture. Inverse compatible sunflower classes covering those manufactured petals require >=ceil((r+1)/q) classes if each class itself lifts to an original sunflower; the claimed lower bound concerns that particular certificate type, not every possible certificate. Source/literature caution: rank-two graph extremal theory predates this programme.

Validation: scripts/dense_obstruction_audit.py and tests/test_dense_obstruction_audit.py (finite corroboration only). The main unresolved obligations are a density-sensitive original-witness lemma **above the stronger b_q threshold**, a quantitatively useful rank induction, and a proof of C_s^K independent of n.

## 8. Higher-rank original-witness obstruction: stricter density floors (PROVED, 14 October 2026)

The complete symbolic proof and exact failure-mode analysis are in [HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md](HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md). A general anchored-factor lemma says: if any w-uniform s-free original family H of h members contains B and r>=1 distinct outside vertices x, each giving a one-vertex original replacement of B, then H^(tensor m) is still s-free, has rank K=wm, size h^m, and after a **specified lexicographic full shift** has at least rm+1 edges sharing [K-1] (the collision-safe partial-spoke lemma applies with all other tensor edges still present). This result holds for all m and is not a full sunflower proof.

Two known published finite factors yield strictly stronger quantified negative tests: for **s=3**, the Abbott–Hanson 54-edge rank-four 3-free factor has two distinct outside one-spoke witnesses. Its m-fold tensor has K=4m, size 54^m, original tau=2 and lex-shifted tau>=2m+1. Hence the false H_s restricted to |F|>=D^K is false through **D<=54^(1/4)>sqrt(6)**. For **s=4**, the Axante et al. 39-edge rank-three 4-free factor has one outside spoke; K=3m, size 39^m, original tau=3 and shifted tau>=m+1. The false restricted H_s fails through **D<=39^(1/3)>sqrt(10)**. Neither finite factor is claimed as a new construction.

The 54 factor also satisfies equality in the s=3 shadow-incidence inequality: |partial H|=108 and every (rank-1)-shadow has exactly 2 extensions. For all tensor powers, |partial F_m|=m*108*54^(m-1) and K|F_m|=2|partial F_m|. Thus strict positive shadow slack does not emerge automatically even at this higher exponential density. Exact original maximum links are 12*54^(m-1) (2/9 fraction) for s=3, and 9*39^(m-1) (3/13 fraction) for s=4. The fractional-link examples do **not** kill all conditional constant-loss link theorems; they set unavoidable constants at these density floors.

Independent original-link attempt: a maximal matching hitting set still gives |F|<= (s-1) K max_x|L_x|, so taking |F|>=D^K yields links of size >=C^(K-1) at sufficiently high K for each fixed C<D. This loses base and does not close a single-base induction. Exact trace residues around E in F are genuinely original s-free lower-rank families with matching number <=s-2, but the residual class disjoint from E remains at rank K; summing 2^K trace classes does not give a new per-rank bound. No unconditional C_s^K theorem follows.

Diagnostics: scripts/high_rank_tensor_audit.py; tests/test_high_rank_tensor_audit.py. All-m statements are symbolic; tests cover finite factors and m<=2 only. The central gap remains original-ancestor-compatible rank reduction **above** these stronger adversarial bases or by an invariant not defeated by them.

**Logical threshold audit:** The bare assertion that *there exist* D_s,B_s,k0 so that every s-free |F|>D_s^k has an original vertex with degree >=|F|/B_s is in fact **equivalent to the sunflower conjecture**. Forward: this links to f_s(k-1) and inducts with C_s>=D_s,B_s and finitely many base ranks. Backward: if a C_s bound already holds, choose D_s>C_s and the condition is vacuous. It cannot be advertised as a substantive independent bridge merely by assuming unquantified thresholds. See section 4a of HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md for the exact proof.


## 14 October: original intersecting-family reduction and s=6 adversarial factor

[Full proof, finite certificates and exact limitations](SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md).

**PROVED:** If i_s(k) is the maximum size of an INTERSECTING original s-free k-family, then i_s(k)<=f_s(k)<=(s-1)k*i_s(k): choose a maximal matching of at most s-1 edges, colour originals by a first vertex in its union; each class is intersecting. Consequently the full and intersecting extremal functions have equal limsup kth-root growth. An independently established fixed-base bound for intersecting original families would settle the full problem, but assuming such a bound is **circular**.

**PROVED correction to earlier trace bookkeeping:** for a fixed original edge E, matching number of exact-trace residues R_T is <=s-2 for EVERY proper T subset E, INCLUDING T=empty. Empty-trace rank stays k; no constant-coefficient rank recurrence follows.

**PROVED s=6 no-go:** published 153-triple s=6-free factor of Axante et al. §7.1 has nine distinct one-swap outsiders at B={0,1,10}. Rank 3m tensors of size 153^m remain original six-free, tau=5, and their ordered full-shift sunflower number is >=9m+1. This raises the density-shift-transfer obstruction base to 153^(1/3)>sqrt(27). The exact shadow-codegree histogram for the finite factor is (1:27,4:8,5:80), NOT globally saturated.

**PROVED strengthened general no-go:** for any anchored s-free factor H, fixing one baseline vertex in the first tensor coordinate yields an INTERSECTING original s-free tensor subfamily of constant density fraction d/h, while retaining r(m-1)+1 shifted core-star petals. Thus restricting naive full-shift sunflower-number transfer to intersecting originals still fails for all D strictly below the corresponding factor floor. This does NOT refute a direct intersecting original-size theorem.

**OPEN:** a valid independently proved fixed-base upper bound for intersecting original families or other O_s(1)-loss original rank reduction. No full proof.


## 10. Original multiwitness trace rank reduction (14 October 2026; PROVED, LOCAL)

See [full new symbolic proofs and explicit sharp examples](ORIGINAL_MULTIWITNESS_TRACE_RANK_REDUCTION.md). An intersecting s-free original k-family containing E=T+V and r<=s-2 members A_i=T+W_i, where all |V|=|W_i|=h and W_i are disjoint outside E, satisfies |F(E,U)|<=h^r f_s(k-|U|-r) for every nonempty U subseteq V. Rank negative means class empty. When h=1, r compatible original swaps force the opposite singleton trace to contain r+1 fixed original points, giving the sharp coefficient-one rank-(r+1) descent. This holds at rank k=r+2 with equality in explicit intersecting s-free examples for every s>=3 and 1<=r<=s-2. Cross disjoint traces obey a nonnegative edge-energy inequality, and tensor overlap polynomials multiply. None of these local identities covers a positive fraction of a general family or proves any C_s^k bound. The absence of pairwise intersection in the published 153-factor makes an unqualified invocation FALSE; the intersecting tensor restriction often makes the requisite opposite traces empty. Full conjecture still OPEN.


## 11. Core-free bounded-trace prevalence obstruction (PROVED, 15 October 2026)

See [TRIANGLE_TENSOR_PREVALENCE_OBSTRUCTION.md](TRIANGLE_TENSOR_PREVALENCE_OBSTRUCTION.md). The triangle tensor Q^m construction (with Q having empty global core) is an s-free INTERSECTING original family, itself with empty global core, of rank 2+wm and cardinality 3a^m. For EVERY anchor E, a uniformly random original B has |B intersect E| >= 1+wX with X~Bin(m,1/a), from blocks where projections coincide. Thus bounded opposite-trace mass is exponentially negligible at each anchor, irrespective of the existence of compatible witnesses. In H54, a block even intersects its anchor with probability exactly 1/2, sharpening the tail to 2^-m sum_(j=0)^(H-1) binom(m,j). The exact H54 ordered overlap polynomial is (27+12z+10z²+4z³+z⁴)/54. Consequently O_s(1) anchors CANNOT cover a positive fraction with h=O_s(1) opposite traces at every fixed density strictly below 54^(1/4) (s=3), 39^(1/3) (s=4), or 153^(1/3) (s=6), nor below s-1 for generic q products. This negates an apparently useful prevalence proposition but not an unknown higher-density proposition or sophisticated exponentially-many-anchor amortisation. No full conjecture proof.


## 12. Central-trace original recurrence and exact fractional anchor-cost audit (15 October 2026)

See [full independent note](CENTRAL_TRACE_AMORTISATION.md). **PROVED:** for EVERY proper exact original trace U subset E, R_U has matching number <=s-2, so for s=3 it is itself INTERSECTING; hence i_3(k)<=sum_(u=1)^k binom(k,u)i_3(k-u). Its envelope EGF 1/(2-e^x) has factorial growth, **not** C^k. The exact anchored polynomials of core-free T tensor q^m and T tensor H54^m show central-rank reduction loses the entropy of trace choices. **PROVED sharp fractional LP cost:** any nonnegative cover by <=1-overlap anchors needs total weight >=(3/2)(q/(q-1))^m and >=(3/2)2^m respectively, with equality under uniform weights; bounded *per-edge* charges remain possible and are not a counterexample to an unrelated original method. H153 ordered moments are averages, not asserted per-anchor distributions. **FALSE:** deleting a common vertex preserves intersectingness, or s>=4 proper traces are always intersecting. **OPEN:** a noncircular, entropy-absorbing original-family rank recurrence and full conjecture. Source factors are prior art. Independent finite tests in scripts/central_trace_amortisation_audit.py and tests/test_central_trace_amortisation_audit.py.


## 15 October: three-way cross-trace energy and scalar-rank-cost audit

[Standalone note](CROSS_TRACE_ENTROPY_AND_LINKS.md) PROVES the integer collision-energy inequality CT2 over three DISTINCT traces that themselves form a sunflower, including overlapping traces, and derives its aggregate certificate. Genuine ORIGINAL intersecting, three-free counterexamples show trace sunflowers need not lift, and that two distinct overlapping traces can have completely disjoint outside residues. Triangle q/H54 tensors show a compulsory outside triangle vertex can pay the entire three-trace collision energy while central binomial trace entropy survives.

An exact anchor-regular weighted LP theorem yields OPT_q,m(z)=3/[z(2+z)]*(q/(q-1+z))^m and OPT_54,m(z)=3/[z(2+z)]*(54/A(z))^m for 0<z<=1, with A=27+12z+10z^2+4z^3+z^4. For each fixed 0<z<1 these costs grow exponentially, so overlap-spectrum contraction alone cannot finance global anchor charge. H153 still has ONLY an averaged spectrum. Tensor ORIGINAL H54 gives the explicit strict-floor obstruction to a density-link theorem: D<54^(1/4), phi>2/9 is FALSE; H153 gives D<153^(1/3), phi>3/17 FALSE. A nonvacuous but AMBIENT-RESTRICTED s=3 link lemma is proved for n<=3k with D=2, phi=1/3 (two disjoint triangles witness nonvacuity); unrestricted point-links remain OPEN. A maximal matching hit-set charged once proves MH1 but fails fixed-base closure at u=1; deleting a common core may INCREASE matching number. No original C_s^k bound follows.

## 15 October: private occupancy defects and exact central trace vector LP (PROVED / scoped)

[PARTIAL_MULTIPLICITY_DUAL.md](PARTIAL_MULTIPLICITY_DUAL.md) upgrades cross-trace collision CT1 to an s-petal ORIGINAL **partial-multiplicity** certificate PM1: some outside vertex belongs to 2,...,s-1 of the s original residues. For s=3, the expected private-collision energy is sum_x(p1p2+p1p3+p2p3-3p1p2p3)>=1; triple-common compulsory hubs pay ZERO. An original 3-free four-edge family with one hub and precisely one private collision makes the bound sharp. At CENTRAL equal-size mask level r on triangle tensor P(s-1,m), the guaranteed defect-coordinate cover LP has an explicit matching primal/dual OPT=m/s for all 1<=r<=m-s+1. Hence THIS coordinate-indexed non-scalar scheme has no exponential rank gain, while richer correlated original-edge/multi-anchor schemes remain OPEN. On H54, expected private-pair defect vertices per block are 56/27; tensor expectations add. A nonvacuous unrestricted high-density point-link with constants would imply a C_s^k upper bound by direct link induction, but NONE is proved. Random k-colouring gives a sound original-witness-preserving reduction to k-partite families at loss k^k/k!<=e^k, not a bound for those families. Full conjecture OPEN.


## 15 October 2026: correlated actual original-edge defects and the partite entropy boundary

**PROVED, source-controlled, NO full solution.** The standalone [original partite witness/entropy audit](CORRELATED_PARTITE_ORIGINAL_DEFECTS.md) proves that on P(s-1,m), m>=2, every s-tuple of distinct ORIGINAL edges has at least 2 partial occupancy defect coordinates, and for every coordinate pair a genuine original tuple has precisely that pair as defect support. An additive fractional coordinate LP indexed by *all actual original edge tuples* has exact primal/dual OPT=m/2. This is a sharp barrier to charging only defect coordinates, not to nonlinear multi-anchor rank-drop reuse charges.

For an s-free ORIGINAL transversal family F let P be uniform, Q the external product of actual coordinate marginals, theta=Q(F), Gamma=product over coordinates of Q-probability "all s same or all s different", delta=sum_(x in F)Q(x)^s, eta=max_(x in F)Q(x), T=sum coordinate marginal entropies-log|F|. The noncircular original-witness certificate theta^s<=1-Gamma+delta and exp(-sT)<=1-Gamma+eta^(s-1) is proved; P(s-1,k) attains equality. The sharp classical bipartite rank-2 bound is (s-1)^2; the classical ternary quadratic rank-three cap with 9>2^3 edges refutes naive product-induction. **OPEN:** all-rank original k-partite B^k, multi-anchor bounded rank-drop charges, nonvacuous unrestricted original point link, full C_s^k. Tensor H54/H39/H153 floors unchanged. Finite tests corroborate symbolic proofs but are not a solution.

## 15 October — original-pair ranked-certificate LP: proved sharp-scale no-go, unrestricted theorem OPEN

[ORIGINAL_PAIR_BUDGET_AND_TENSOR_ENTROPY.md](ORIGINAL_PAIR_BUDGET_AND_TENSOR_ENTROPY.md) proves an ACTUAL original edge-pair/vertex fractional LP with exact certificate capacity binom(N-2,s-2)-binom(d_v-2,s-2) and universal quadratic dual Lambda_s(F)>=N(N-1)/(s(s-1)). On binary P(2,m) with N=2^m, an explicit nonlinear Hamming-distance primal and uniform dual give (N-1)(N-2)/3 <= Lambda_3 <= N(N-m-1)/2, so the naturally normalised certificate cost remains of constant order instead of exponential rank savings. A separate exact original anchor-trace entropy identity saturates on P(s-1,k); E3/E5 become vacuous on the classical nine-point quadratic cap tensor. Published H54 and NONREGULAR H153 vertex-spectrum controls are global averages only. This is meaningful mathematical no-go for a SPECIFIED pair witness LP, not for joint rank-drop entropy potentials; no unrestricted recurrence or full proof was found. `scripts/original_pair_budget_audit.py` and `tests/test_original_pair_budget_audit.py` include exact finite primal/dual and original witness checks.


## Original-owned packet rank/entropy ledger (15 October 2026)

**PROVED, insufficient:** Each original anchor E partitions F exactly once by U=A intersect E. For an intersecting F all packets have genuine rank drop r=|U|>=1; nonintersecting F may have rank-zero packets. Each residue family is simple, original and s-free. Exact full ledger at any C>1: k log C-log N=E[r]log C-H(U)+E[(k-r)log C-log n_U]. Gibbs dual gives H(U)-log C E[r]<=log(sum_U C^-r). See [complete standalone proof and finite audits](ORIGINAL_PACKET_KRAFT_AND_ENTROPY.md). On P(q,k), the surcharge is exactly cancelled by true residue slack; on a pair-private intersecting core-free 3-free k+1-edge family H(U)/E[r] tends to infinity for EVERY original anchor, so bounded ownership alone does not close rank induction. This sparse counterexample does not rule out a properly proved large-density lemma. AVERAGED anchor-overlap rank: H54=8/9, H39=9/13, H153=11201/23409 (nonregular); cap9=29/27. **No fixed-base all-original recurrence or unrestricted sunflower proof.**


## 15 October — one-vertex cross-trace tensor shielding and bounded-VC extraction barrier

[Full proof and finite audits](CROSS_TRACE_TENSOR_SHIELD_AND_VC_BARRIER.md): fixed-trace-rank s-tuples of ORIGINAL petals have either identical traces or s distinct sunflower traces (when their traces are equal-sized); exact rows indexed by an outside residue B are themselves s-free r-uniform original trace families. **PROVED** an all-s rank-s original seed with s+1 s-free edges whose s singleton traces are a sunflower but outside residues have one unavoidable partial-multiplicity collision. Tensoring with the classical nine-edge ternary quadratic cap at s=3 produces three exact packets of size 4^m each, with no compatible rainbow originals, and a tuple with only one defect vertex for all m. For s>=4 P(s-1,1)^m yields packet sizes (s-2)^m. This **refutes a uniform per-tensor-block cross-trace deficit from packet size alone**, not any properly high-density theorem.

Using the Sauer-Shelah lemma, every H subset P(2,k) of VC dimension <=d has |H|<=sum_(j<=d)binom(k,j). Thus a fixed-d subfamily is polynomial size, while a subfamily of size >=a^k (a>1) has VC dimension Omega_a(k). This is a quantified barrier to extracting large bounded-VC original subfamilies, **not a refutation** of Ge–Wang–Xu–Zhao (2026) or Shangguan (Sep 2026) bounded-VC theorems. Global certificate reuse, cross-trace conditional entropy, a genuinely noncircular original fixed-base induction, and the full sunflower conjecture remain OPEN. Earlier CT2/PM1 collision inequalities are retained as earlier deductions, not renamed as new.


## 15 October: alternating original trace shields and bounded rectangle-cover LP

[Complete standalone proof and finite tests](ALTERNATING_SHIELD_RECTANGLE_DUAL.md). The previous TS3/TS4 tensor obstruction had a SINGLE permanently defective vertex. There is now an all-s original rank-s counterexample F_s^alt with s+2 edges and an actual anchor E: its s singleton trace packets have sizes (1,2,1,...,1), form an s-sunflower at the trace level, and have NO compatible original rainbow sunflower. Depending on which of the two residues in the second packet is chosen, the *unique* partial multiplicity defect is a or b. There is NO vertex that defects in every tuple. Full F_s^alt is s-free. Private rank padding preserves all quantifiers and gives empty overall core.

The exact permanent-witness criterion for a cartesian rectangle is: some vertex x defects for every original tuple exactly when at least TWO packets force its inclusion and at least ONE packet forces its absence. Therefore removing only constant-single-vertex shields does NOT make residue selection compatible. Tensoring with classical Q9 for s=3, P(s-1,1) for s>=4, gives exponentially large packets (h^m,2h^m,h^m,...) for h=4 or s-2 while preserving this non-permanence. Their exact per-vertex selection capacities are L_a=L_b=h^(ms), total N=2h^(ms), and the exact local fractional defect-cover optimum is 2 for EVERY m: matching upper weights a=b=1 and two isolated-witness tuples provide the lower bound. This is an adversarial original-witness test; the integer load formula is already the earlier PM1, not newly claimed.

The full C_s^k problem remains OPEN. In particular no globally balanced certificate charge, unrestricted high-density original link, or noncircular f_s(k) recurrence has been derived. H54/H39/H153 and q-products are STRICT lower construction/density controls, not available upper bounds. Ge et al. (2026) and Shangguan (2026) only give VC-dimension-dependent exponential bases; TS5 still blocks a bounded-d original extraction from P(2,k).
