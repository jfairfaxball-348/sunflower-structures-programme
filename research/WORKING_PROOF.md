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

**Conditional rank-dependent bridge (fully proved as an implication, premise UNPROVED).** Suppose for a fixed s there exists A_s>=1 such that for every s-free rank-k original family with k>=2 its full-shift image G satisfies

    tau(G) <= A_s k / log(k+2).                                       (H_s)

Let D_s=A_s+1. With u=tau(G)+1, u<=D_s k/log(k+2). Apply (3) to the shifted G with sunflower target u:

    |F|=|G|<=2^k u^(2u-2)
        <= [2 exp(2D_s(1+log(D_s)/log(4)))]^k.

For k=1 take at most s-1 singleton sets. Hence H_s would prove the unrestricted conjecture with

    C_s=max(s-1, 2 exp(2D_s(1+log(D_s)/log(4)))).

Equation (6) shows k/log k is the smallest plausible ORDER of a universal shifted-tau upper bound of this kind when s>=4. However this is NOT a verified bridge: P(2,k) is 3-free, and exact full-shift computations at k=2,...,8 (using blocks {i,k+i}) produce a common-(k-1)-core star of k+1 sets after lexicographic full shifting. If that persists in all k, H_3 is FALSE for this shift order. This is finite evidence, not a proved universal refutation or a new bound. Do not claim H_s is true.

**Other explored routes.** Arbitrary original link reduction loses a factor up to k(s-1) per rank and reproduces factorial bounds, not C_s^k. Indefinite one-step shift multiplication costs 2^T with T potentially depending on n. Global fixed-support colouring is rigorous but too expensive for growing support. Literal shifted-original subfamily extraction is destroyed by (5). Heavy stars have high links but cannot cover pair-private or product arrangements. None of these routes closes the full theorem.

## 5. Checkable finite diagnostics and exact next obligation

Run: python3 scripts/bridge_audit.py and python3 -m unittest discover -s tests -v.

Exhaustively enumerated all 2048 subfamilies of the 2- and 3-layers on [5]; verified (1), (4), cardinality preservation, shifted half-link and shifted link closure. Exhaustively enumerated all 15 pair partitions of [6], all 256 subfamilies of each P(2,3), and verified (5) in those 3840 cases; some achieve size 2. Checked (4) at equality via 4+4 two-star edges and the pair-private 3-free construction. These computations corroborate the symbolic proofs and are not substitutes for them. Product full-shift star growth reported above is only checked for k<=8.

**Decisive unresolved task:** Prove a quantitatively valid ORIGINAL-witness-preserving structural theorem for sufficiently large arbitrary s-free families that avoids the source/collision barrier and yields O_s(1) exponential base per rank. One concrete falsifiable attack is to decide H_s decisively on P(2,k), by symbolic full-shift description and proof; if H_s fails, develop an alternative invariant (e.g. trace-resolved compatible lifted witnesses, not just final tau) strong enough to imply C_s^k. All constants must be independent of k and n. **No complete proof has been obtained.**
