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
