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


## 15 October 2026 — global ORIGINAL multishield LP and ownership (PROVED; unrestricted proof OPEN)

[Standalone original-family proof and finite audit](GLOBAL_MULTISHIELD_ORIGINAL_OWNERSHIP.md): across ALL actual original anchors and ALL equal-trace-rank sunflower packet rectangles, the global partial-defect vertex fractional covering LP on P(s-1,k) has **exact value (s-1)k/s** for k>=s; at fixed trace-private size t it has value (s-1)k/(s*t) if k>=s*t and 0 otherwise. A tight original s-tuple and alphabet/coordinate transitive orbit give matching explicit primal and dual, not mere local aggregation. Original edge participation under canonical s-coordinate block anchored tuples is exactly s floor(k/s) occurrences per edge, so fixed-anchor ownership is not global once-ownership. This kills an O_s(1) global covering-weight prerequisite even though P has point-link fraction 1/(s-1). This does NOT disprove the existence of a density-sensitive decomposition or fixed-base f_s(k) recurrence. Five standalone finite unit tests passed; full GitHub exact-head suite pending. No literature-priority claim.


## 15 October 2026 — heterogeneous original global dual and density robustness

See [HETEROGENEOUS_PRODUCT_DENSITY_DUAL.md](HETEROGENEOUS_PRODUCT_DENSITY_DUAL.md). **PROVED (programme-local):** For any genuine ORIGINAL product box with variable alphabet sizes b_1<=...<=b_m<=s-1 and private rank t, the complete all-anchor equal-trace rectangle fractional defect-cover LP has the exact value 0 for m<st, otherwise min_(0<=h<st)(sum_(j<=m-h)b_j)/(st-h), with explicit feasible actual-witness dual supported on tight rectangles. This extends G4/G5, has a matching dual, and counts actual global vertices rather than copied anchor defects. **PROVED:** any original subfamily F of density delta relative to this whole box retains global LP value at least max(0,(s+1)delta-s) times the full product optimum; the union-bound constant is sharp for canonical orbit record survival upon deleting a single original edge (not necessarily the restricted LP optimum). **PROVED:** the five-edge s=3 AS3 seed has THREE all-anchor rectangle records with singleton outside defects {a},{b},{c}; its all-anchor LP is 3, versus 2 locally. **PROVED identity:** coordinate conditional entropy deficit is log(1/delta), hence zero on the complete product despite a linearly growing LP. **FALSE inference:** global linear certificate pressure or positive log-density excess over the classical product threshold forces an original sunflower; H54/H39/H153 tensor factors remain s-free above their classical product bases. **OPEN:** an unrestricted noncircular original-family C_s^k recurrence; no such recurrence follows from these product-specific results. Finite original checks include s=4,k=4, rational LP primal/dual and six new tests. No outside novelty priority check.


## 15 October 2026: strict original tensor-certificate synergy (PROVED finite)

[NONPRODUCT_ORIGINAL_TENSOR_CORRELATION.md](NONPRODUCT_ORIGINAL_TENSOR_CORRELATION.md) proves the universal original all-anchor defect-cover superadditivity V_s(A tensor B)>=V_s(A)+V_s(B), with genuine ORIGINAL anchors and physical vertex capacity. A 45-edge rank-six AS3 tensor Q9 example has **exact** V_3=8, strictly above individual LP costs 3+3. The finite certificate has 6403 real selection records, 457 defect sets, an eight-vertex primal and eight ACTUALLY ATTAINED disjoint defect sets as a matching dual; an independent direct brute-force unit test confirms the enumeration. Its all-family-normalized nonseparable synergy J=2/45, but iterates yield merely linear growth >=3m+5, not rank savings. A further universal density-transfer inequality (NC3/NC4) measures maximal owner reuse rather than assuming uniformity: V_s(F)>=V_s(H)-sum_(missing original e) m_e(y). Balanced duals beyond symmetric products and any noncircular fixed-base recurrence remain OPEN.

## 15 October: OPTIMAL original-edge owner balance in nonproduct tensor (PROVED exact)

[OPTIMAL_ORIGINAL_OWNER_BALANCING.md](OPTIMAL_ORIGINAL_OWNER_BALANCING.md) corrects the prior diagnosis of AS3×Q9 as necessarily owner-congested. For every feasible actual-record dual, the edge-load identity sum_e m_e=(s+1)Y gives lambda>=1. Exact integer verification of a 58-record rational optimal dual proves **lambda_opt(AS3×Q9)=1**, even though each factor has strictly greater optimum minimum congestion: 5/4 for AS3 and 3/2 for Q9. All 45 original edges carry precisely 32/45 owner load; the certificate has total Y=8 and per-vertex defect load <=1. The old eight-unit dual's lambda=225/32 remains valid but is not minimal.

This improves the arbitrary-original-subfamily deletion guarantee to V_3(F)>=max(0,(32|F|-1080)/45) for F subset AS3×Q9, nonzero at |F|>=34. A symbolic ORIGINAL tensor-lift theorem propagates the balanced dual to (AS3×Q9)^m (rank 6m, |F|=45^m): Y=8m, every original-edge owner load 32m/45^m and any relative-density delta subfamily has V_3>=m max(0,32delta-24). This is **linear** certificate growth and is below the binary-product sunflower-free size base: 45^(1/6)<2. Neither this density inheritance nor perfect dual balancing forces an original large-link theorem.

OB1–OB6 are programme-local PROVED algebra/finite exact certificates with literature priority NOT CHECKED. f_s(0)=1, f_s(1)=s-1; for s=3 f_3(2)=6 precludes a 2-fold link recurrence. The conditional high-density point-link hypothesis at explicit D_s and phi_s would give f_s(k)<=C_s^k, but the needed premise is OPEN. Unrestricted original conjecture remains OPEN; Mishra v2 is shifted only.

## New exact all-s original-pair-star obstruction (15 October 2026)

[ORIGINAL_PAIR_STAR_QUADRATIC_LP_OBSTRUCTION.md](ORIGINAL_PAIR_STAR_QUADRATIC_LP_OBSTRUCTION.md) proves **PS1–PS3** without shifting: for n>=s+1, the n original rank-(n-1) star edges E_i consisting of all physical pairs {i,j} form an s-sunflower-free family. Every pair of original edges intersects at a unique, pair-specific physical vertex. Every anchor i and s-set J of other original edges gives a real equal-size, empty-core trace sunflower and an original defect consisting of the C(s,2) pair-vertices within J. An all-vertex symmetric primal and uniform actual-record dual are both feasible and match exactly:

    V_s(H_n)=n(n-1)/[s(s-1)],
    optimal lambda=1, theta(H_n)=2/n -> 0.

A disjoint union of r<=s-1 copies is still s-free and has V_s=r*n(n-1)/[s(s-1)], optimal lambda=1 and theta=2/(rn). With r=s-1, this is within factor two asymptotically of the maximal-matching lower bound 1/[(s-1)k]. Consequently even a QUADRATIC, optimally balanced original witness LP and abundant equal traces do not, **without an exponential cardinality condition**, force a constant point link. The family has N=r(k+1), so this is a valid negative theorem for an unconditional LP-to-link lemma, not a counterexample above |F|>D_s^k. All exact arithmetic tests and independently enumerated genuine original records are in scripts/original_pair_star_quadratic_audit.py and tests/test_original_pair_star_quadratic_audit.py.

The density-link premise from OB5 remains wholly CONDITIONAL. Define beta_s=sup_k f_s(k)^(1/k), possibly infinite. Original tensor powers prove: D_s<beta_s yields arbitrarily high-rank s-free originals with |F|>D_s^k, whereas D_s>=beta_s makes such a premise VACUOUS. The nonvacuous high-density bridge must include a new, rank-independent bound in the regime where known H54/H39/H153 lower products challenge the point-link fraction. No superadditivity beyond V_3(T^2)>=16 or V_3(S tensor Q9^2)>=11 was proved; crude ground-size upper bounds are 34 and 26. The full conjecture remains OPEN.


## 15 October continuation — exact fractional ORIGINAL point-link LP (FL1–FL3)

Full proofs, every exact rational packing/cover, finite independent audit and honest failed bridges: [FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md](FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md).

For nonempty original H, set t(H)=min_{probability p on original edges} max_{actual x} P_p(x in E). Exact LP duality yields t(H)=1/nu*(H), where nu* is the fractional matching number and its dual is a fractional actual-point vertex cover (not the previously used anchored-defect LP V_s). For arbitrary disjoint-ground factor products H_i, t(tensor_i H_i)=max_i t(H_i). Crucially ANY nonempty correlated ORIGINAL subfamily G of the product has theta(G)>=max_i t(H_i), without independence or density assumptions; the proof uses factor marginals and actual vertex incidences. This does not prove a positive original-family theorem beyond these factors.

For published H54, H39 and H153 the exact optimal primal/dual values are respectively nu*=9/2, 13/3, 17/3. The packings y_E constant 1/12, 1/9, 1/27 and the covers z_x equal 1/4 on H54's 18 points, 1/3 on H39's 13 points, and 1/3 on H153's 14 cyclic points plus 1 on its disjoint cone apex are valid equal-value rational certificates. Thus t=theta=2/9,3/13,3/17; these inequalities survive arbitrary subfamilies of tensor powers. New-in-programme exact LP analysis; published finite factors are prior art, priority of LP observation NOT CHECKED.

The original rank-three 3-free family B formed by the four rank-three pair-stars of K4 on six actual pair-points together with a disjoint three-private-point edge has theta(B)=2/5 but t(B)=1/3, witnessed by packing (1/2,1/2,1/2,1/2,1), fractional actual-point cover of objective 3, and probability vector (1/6,1/6,1/6,1/6,1/3). Constant-composition original tensor subfamilies of length 6h contain (6h)!/((h!)^4(2h)!) distinct original 18h-sets, theta=1/3, and exponential cardinality base 108^(1/9)>1. This is a genuine nonvacuous type-class test, although H54 gives a strictly stronger global s=3 density/fraction obstruction. For arbitrary seeds H and rational p, the necessary high-density link obstruction is D<exp(H(p)/rank(H)) and phi>max_x p(x in E); such pairs are FALSE by actual type classes.

The new exact fractional minimax identities and entropy control neither bound nu*(F) for arbitrary dense s-free F nor establish any witness-compatible recurrence. Previously honest correlated-defect bounds remain 16<=V_3(T^2)<=34 and 11<=V_3(AS3 tensor Q9^2)<=26. Proposed numerics s=3 (D,phi)=(5/2,1/5), s=4 (10/3,1/5), s=6 (21/4,1/6) lie inside demonstrated nonvacuous density ranges but are entirely UNPROVED. The full original sunflower conjecture remains OPEN. No shift-lifting conclusion or coefficient-two original recursion has been inferred.


## 15 October 2026 — NONVACUOUS high-density point-link impossibility (WR1–WR5, PROVED internally)

[Original pair-star wreath counterexample](NONVACUOUS_WREATH_POINT_LINK_OBSTRUCTION.md) is a genuine simple s-free ORIGINAL construction W_N,m(H) using N private tensor copies of any original s-free d-family H behind pair-star shell A_i. It has rank N-1+dm, size N|H|^m, theta=t=2/N and exact rational original fractional matching/physical-point cover nu*=N/2. For beta_s=sup_d f_s(d)^(1/d), EVERY threshold D<beta_s admits arbitrarily dense-above-D^k original witnesses with theta tending to zero and nu* unbounded; thresholds D>=beta_s are vacuous. Thus ALL previously proposed positive fixed point-link and bounded fractional-matching premises at **nonvacuous** density are FALSE, including the three explicit (5/2,1/5), (10/3,1/5), (21/4,1/6) proposals (integer-checked original witnesses). Previous conditional link-to-recurrence algebra is sound, but its required premise cannot hold. FL1 correlated-subfamily marginal rigidity on a shared tensor ground remains valid and is NOT contradicted. Efficient rank-(N-1) original multi-point packet extraction on this wreath survives; finding a NONCIRCULAR all-F packet recurrence is OPEN. Literature originality is NOT CHECKED, published H54/H39/H153 source factors remain PRIOR ART, and the full unrestricted sunflower conjecture remains OPEN.


## 15 October 2026 — exact bounded-anchor ORIGINAL packet Kraft optimum (MP1–MP5; PROVED internally)

[Sharp ORIGINAL wreath packet theorem](EXACT_WREATH_PACKET_KRAFT_OBSTRUCTION.md) computes, not estimates, the optimum rank-weighted cost of every genuine original nonempty physical-anchor partition of W_{N,m}(H) when anchors have 1<=r<=R<=N-1:

    min Z_C = min_(0<=j<=floor(N/2)) [ j/C + (N-2j)/C^R ].

All original packets meeting two wreath groups are anchored by the unique physical pairpoint p_ij and have rank drop one; packets meeting a single group can use any R actual shell points. The optimal weighted support cover of group indices is an exactly solvable singleton/pair cover, with actual original witness partitions attaining equality. For any fixed trial base C>1 and fixed cap R, Z_C grows linearly with N. Combining WR3 with N->infinity and m/N->infinity proves no bounded-rank positive-anchor packet-cost<=1 strategy can work for ALL original families above ANY nonvacuous exponential density threshold D<beta_s. Conversely this same wreath admits budget<=1 with R=ceil(log_C N) actual shell vertices for sufficiently large N. Thus logarithmic anchor rank is SHARP on the wreath, not a general theorem.

For ANY nonempty anchored partition (no rank cap), max packet probability <=2/N, entropy H(I)>=log(N/2), and the old exact Gibbs identity gives log Z_C>=log(N/2)-E[r]log C. A budget<=1 forces average physical rank drop E[r]>=log_C(N/2). For two independent cross-group pairs of original wreath edges, the exact physical pair-intersection collision probability is 2(N-1)/N^3; unconditional constant cross-packet collision/energy methods therefore fail at every D<beta_s. New exact rational set-cover DP independently tests all actual positive anchors in small cases (nine parameter choices). This is a precise NONCIRCULAR OBSTRUCTION plus a sharp construction on this family, NOT a universal positive rank recurrence. No original s-sunflower found; no shift-owner lifting. General maximal-matching coefficient (s-1)k remains. Literature priority NOT CHECKED and unrestricted conjecture OPEN.


## 15 October continuation — nested ORIGINAL wreath packet costs (NW1–NW9, PROVED restricted)

See [NESTED_ORIGINAL_WREATH_PACKET_RECURSION.md](NESTED_ORIGINAL_WREATH_PACKET_RECURSION.md). For genuinely distinct physical pair-star shells at each of t tree levels and private s-free H^m copies at leaves, the ORIGINAL family is s-free, has rank dm+sum_h(N_h-1), and cardinality M^m prod_h N_h. All actual owners are used once; both empty- and nonempty-core sunflowers are excluded.

For **shell-only physical anchors** (NOT unrestricted private-point anchors), exact minimum Kraft cost has the backward recursion U_(t+1)=1, a_h=C^(-(N_h-1))U_(h+1), V_h=min_j[j/C+(N_h-2j)a_h], U_h=min(1,V_h), with the ROOT optimum V_1 (zero-anchor root stop prohibited). Proof is a sharp atomic-leaf support-cover: packets joining two children have exactly one common point at that node; deeper shell anchors can be added to the actual ancestor shell. At trial C=2 and all N_h>=3, exact cost is prod_h N_h/2^(N_h-1), so for every N_h=3 it is (3/4)^t. Independent exact rational all-shell-anchor enumeration verifies (3,3) cost 9/16 at C=2 and 1/9 at C=3.

**Explicit counterexample to a false induction:** take s=4, t shells each of size N_h=3, and private P(3,t) suffixes. This is a genuine-original 4-free family of rank k=3t and size 9^t>2^k, despite 3^t distinct nonempty original leaf packets each of rank drop 2t<k and TOTAL budget Z_2=(3/4)^t. Their residuals P(3,t) have 3^t>2^t owners, so no base-two residual inductive hypothesis holds. Thus the premise 'actual anchored packet cover with Z_C<=1' is insufficient **without a noncircular residual-size theorem**, even as Z_2 vanishes. This example does NOT refute a larger unknown C_4.

At each nested node an actual pair intersection conditioned on different child labels is the ancestor shell plus one unique physical pairpoint. Independent two-pair collision is 2(N-1)/N^3; this can be very small at each level, even when conditioning on common prefixes. No automatic uniform positive **s-way** cross-packet credit proved. This is a restricted rank/packet mechanism obstruction, NOT an unrestricted fixed-base original-family recurrence. Literature priority NOT CHECKED. The full Erdős–Rado conjecture remains **OPEN**.


## 15 October — AP1–AP7: all-physical nested wreath and conditional original core energy

[Proof-grade restricted-class note](ALL_PHYSICAL_WREATH_COMPATIBILITY.md) upgrades NW2: for physically private q-ary leaf P(q,m), the EXACT minimum nonempty packet Kraft cost over ALL true physical anchors (including private points) is the NW2 recurrence with terminal U_(t+1)=min(1,(q/C)^m), not always 1. At C=2 and q>=2, the old product prod_h N_h/2^(N_h-1) is therefore optimal even over all private-point anchors. For s=4,q=3,N_h=3,t=m, the exact all-anchor cost (3/4)^t tends to zero while the original four-free size 9^t>2^(3t) and leaf rank-t residual density (3/2)^t violates trial base 2. At C=3,q=2,N_h=3, all-physical optimum (1/3)^t(2/3)^m is strictly smaller than shell-only. AP4 gives a sharp TRUE-original conditional s-way compatibility defect inequality sum delta_ij(D)>=1 for each fixed physical D across any s disjoint packets; AP5 gives weighted core-overlap probability >=1/(s-1), but its crude degree consequence is only the old matching bound (s-1)k. These are rigorous NONCIRCULAR conditional laws, not a universal occupancy bound or a completed proof. PRIORITY NOT CHECKED; sources, unresolved AS3/Q9 LP and full conjecture remain as before.


## 16 October — sharp MANY-packet original physical-core Turán obstruction (TC1–TC4)

[PHYSICAL_CORE_TURAN_HIGH_DENSITY_SHARPNESS.md](PHYSICAL_CORE_TURAN_HIGH_DENSITY_SHARPNESS.md) proves a noncircular **r-packet** original-owner compatibility law: for r>=s disjoint nonempty original packets and any actual physical D, sum_{i<j} Pr[A_i intersect A_j !=D] >= binom(r,2)-ex(r,K_s). Apply the classical Turán theorem pointwise to the sampled original D-intersection graph; every K_s is an actual forbidden sunflower, with distinct original petals. Crucially this sharpens repeated AP6 when r grows, yet is **exactly attained** by q=s-1 physically disjoint, single-marker-shielded ORIGINAL copies of H^{tensor m}, any s-free seed H of size M and rank d. The rank is dm+1+|D| and cardinality (s-1)M^m; within-shield pair intersections contain the actual marker, cross-shield intersections equal D, so equality in Turán holds with one original-owner packet per edge, even when r grows exponentially in rank.

Uniform independent originals from this same family give **EXACT equality** in AP7 overlap probability 1/(s-1), for arbitrarily large samples and for every exponential density threshold D_density<beta_s=sup_d f_s(d)^(1/d). Therefore NO universal **strict** AP7 energy, Turán multi-packet, or one-fixed-physical-core bonus is forced at any NONVACUOUS high-density threshold. The q genuine physical marker packets have budget q/C<=1 whenever C>=q but each rank-dm residual has occupancy (M/C^d)^m, which diverges for C<M^(1/d). For s=3 and prior-art H54 at C=5/2 this is Z_C=4/5, residual occupancy (864/625)^m and exact AP7 value 1/2. This does NOT disprove a larger-base unrestricted theorem. Finite original edge and core enumeration, rational density and Turán checks are in scripts/physical_core_turan_sharpness_audit.py; external priority NOT CHECKED. Future work MUST use genuinely cross-core/higher-order physical intersection coupling or independently measured structural residual capacity, not another appeal to unconditional fixed-core overlap. Full Erdős–Rado conjecture remains OPEN.


## 16 October — coupled changing actual physical cores and high-density near-Turan no-go

[CC1–CC6 internally proved](COUPLED_CROSS_CORE_NEAR_TURAN_OBSTRUCTION.md): an original-owner coupled same-B/same-A core variation J obeys 1−sum_D p_D²≤J and J=0 iff every original cross-pair has the SAME physical intersection D. Exact G_D Turan equality forces true balanced q=s−1-partite support separation outside common D, with genuinely intersecting original residual classes. But the correlated actual-marker/pair-star tensor W^corr has rank n+1+dm, size qnM^m and is s-free; its relative Turan deficit is 1/n, J=4(n−1)/n², while every exact empty-cross refinement of original groups retains at most 1/q of owners. Setting n=o(m) produces such counterexamples above EVERY nonvacuous exponential T<beta_s. Exact original-vertex enumeration at s=3,4 checks small cases and independent Fraction J. This refutes near-total exact purification or uniform positive coupled-core bonuses from nonvacuous density ALONE. It does NOT refute constant-factor deletion with amortised rank, or the unrestricted conjecture. Direct approaches via exact shield peeling fail from unpaid residual H^m capacity; bounded-VC route fails because H^{⊗m} shatters m physical vertices (VCdim≥m). Original witnesses only; no shift lifts or full fixed-base recurrence. EXTERNAL PRIORITY NOT CHECKED; full conjecture OPEN.


## 16 October — CSM1–CSM6: original s=3 near-Turán stability and sharp matching payment

See [ORIGINAL_CORE_STABILITY_MATCHING_CAPACITY.md](ORIGINAL_CORE_STABILITY_MATCHING_CAPACITY.md). For ANY fixed physical D in a genuinely ORIGINAL simple 3-free k-family (r members), with e(G_D)>0, Delta=r²/4-e(G_D), a pure degree-sum proof obtains ACTUAL owner packets A=N(u), B=N(v): no more than 4Delta/r excluded original owners; both packets contain D and are internally D-intersecting; at most 5Delta actual cross pairs differ from D; and (|A|-|B|)²<=20Delta. The required exact original-cross purification loss is the maximum matching number in the literal bipartite bad-cross graph (classical König), not bounded by missing cross-edge *density*.

On the already-proved literal s=3 CC3 correlated pair-star with L=2^m, n index points, k=n+1+m, r=2nL, the CSM1 neighbourhoods have precisely |R|=2L=4Delta/r and (n-2)L² bad crosses, but their exact matching deletion costs (n-2)L original owners. The remaining original owners number r/2 even as Delta/(r²/4)=1/n tends to zero. Finite ORIGINAL edge enumeration and Fraction audits verify n=3,4,m=1,2 and the two-triangle extremal s=3 rank2 family.

Residual-size obligation remains: the local sharp inequality r <= 4Delta/r+2i_3(k-|D|) invokes TRUE intersecting original residual extremal capacity, not a known fixed exponential base. When D is empty no rank descends. Two attempted recurrences fail at identified premises: (A) a universally near-Turán nonempty physical core does not exist (P(2,k)); (B) small cross-edge density cannot pay exact matching deletion even at nonvacuous exponentially high density (CC3). The original H^m inner residual remains exponentially full. **NO fixed-base proof; full conjecture OPEN.** All classic graph ingredients prior art; external priority of this packaging NOT CHECKED.
