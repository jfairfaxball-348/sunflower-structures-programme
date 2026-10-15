# Original-owned trace packets, exact entropy/slack ledger, and sharp sparse barrier (15 October 2026)

**Verdict:** PROVED an original-witness packet partition with total edge ownership exactly one; a rank/entropy/residual-slack identity and its Gibbs dual; exact product tensor equalities; an all-rank intersecting 3-free counterexample to an unconditional bounded entropy/rank-drop coefficient; and average (NOT per-anchor) finite-factor controls. **OPEN:** a cross-trace compatible-residue saving sufficient to bound f_s(k) by C_s^k. No source or novelty/priority claim.

## P1. Actual original rank-drop packets: one owner (PROVED)

Let F be a nonempty simple ORIGINAL k-uniform family on a finite ground set and E an actual original edge of F. For every trace T subset E put

    F_T = {A in F : A intersect E = T},
    R_T = {A setminus E : A in F_T},
    n_T=|F_T|, r_T=|T|.

Keep only nonempty packets. These are EXACT original trace/residue packets, not inverse shifted images. Each original A belongs to exactly ONE packet; its owner is the actual trace A intersect E, so the sum of packet multiplicities across the entire family is exactly |F|, with no k-dependent reuse. Every residue has exactly k-r_T elements, and the residue map is injective on its packet. If F is s-sunflower-free, each R_T is itself s-free: a sunflower of s distinct residues would lift by adding the SAME original trace T to each.

If F is intersecting, every T is nonempty and EVERY packet has a genuine simultaneous rank drop r_T>=1. For arbitrary F an empty-trace packet can remain at full rank k, and must not be silently passed to a rank-(k-1) induction. A singleton packet is legitimate but need not contribute useful density.

**Separation of counts:** one-time *edge ownership* does NOT bound how often a pair certificate covers distinct s-tuples. Its separate exact capacity remains the previous PB1: for c=(v,{A,B}), M_v=binom(N-2,s-2)-binom(deg(v)-2,s-2). Neither count implies the other.

## P2. Exact rank-drop/entropy/residual-slack identity (PROVED)

Draw A uniformly from F and write U=A intersect E, p_T=n_T/N, N=|F|. Let C>1 be ANY real trial exponential base and H(U)=-sum_T p_T log p_T. Define mean simultaneous rank drop R=E[r_U] and the ACTUAL conditional residue slack

    S_C = sum_T p_T ((k-r_T) log C - log n_T).

Then the following is an **exact equality** for every original family, even if some S_C terms are negative:

    k log C - log N = R log C - H(U) + S_C.              (PL1)

Proof: uniformity makes H(U)+E log n_U=log N; expand S_C and substitute. It makes no independence hypothesis, and keeps any rank-zero packet visible. If every packet has n_T <= C^(k-r_T), then S_C>=0, but this inequality is merely a conditional use of a rank-(k-r_T) bound; it must not be invoked inductively at r_T=0. Even S_C>=0 does NOT alone give log N<=k log C: the surcharge H(U)-R log C may be positive.

Gibbs/Kraft form, for fixed ACTUAL packet rank drops (r_T) and any probability vector p:

    H(p) - (log C) sum_T p_T r_T <= log Z_C,
    Z_C = sum_(T:n_T>0) C^(-r_T).                      (PL2)

Equality iff p_T=C^(-r_T)/Z_C (all packet masses positive). Proof: D_KL(p || C^(-r)/Z_C)>=0. Thus a bound on total packet *multiplicity* does not control the rank-weighted packet count Z_C or the entropy surcharge.

Under a disjoint-ground tensor product F tensor G anchored at (E,H), the trace variables are independent, n_(T,V)=n_T n_V, and k,N,r add/multiply in the obvious way. Consequently H, R, S_C and the two sides of PL1 all ADD exactly. A coefficient extracted solely from a separable copy of PL1 cannot be improved by raising a fixed factor to tensor powers.

## P3. Intersecting, core-free, s-free family destroying a UNIVERSAL coefficient (PROVED)

For every k>=2 let V={e_ij:1<=i<j<=k+1}; define k-uniform original edges

    A_i={e_min(i,j),max(i,j) : j!=i}, 1<=i<=k+1.

Every two A_i,A_j meet in the unique vertex e_ij; the intersections over three distinct pairs are all different, so there is no 3-sunflower (hence no s-sunflower for ANY s>=3). This family is intersecting and has empty global core. For ANY actual anchor E=A_i, the EXACT packets are the singleton {A_i} with trace E of size k, and k other singleton packets with DISTINCT singleton traces {e_ij}. Every original edge is used ONCE, and ALL packets have rank drop >=1. Nevertheless

    H(U)=log(k+1),  R=(k+k*1)/(k+1)=2k/(k+1),
    H(U)/R = ((k+1)/(2k)) log(k+1) -> infinity.     (PL3)

Hence no universal beta_s can ensure H(U)<=beta_s R for every intersecting original s-free family, even after choosing the best anchor and perfectly disjoint actual packet ownership. Its size k+1 is only polynomial: PL3 does NOT disprove a carefully proved high-density (|F|>D^k) restricted statement. Such a statement would be substantive, not free.

## P4. Mandatory q-product and nine-point cap controls (PROVED)

For q=s-1 and P(q,k), choose any original all-zero anchor. An original word has trace a subset of the k anchor symbols: each coordinate belongs to U independently with probability 1/q; a trace of size r has EXACTLY (q-1)^(k-r) original residues. Consequently

    H(U)=k h(1/q), R=k/q,
    S_q=k(1-1/q) log(q/(q-1)),
    H(U)-R log q=S_q,                                (PL4)

where h(p)=-p log p-(1-p)log(1-p), with 0 log 0=0. In particular k log q-log|P|=0. The entropy surcharge is EXACTLY cancelled by real residue slack. Discarding that slack cannot yield a tight q^k original bound. A trace-only inequality H<=R log C on these products would require

    C >= exp(q h(1/q)) = q*(q/(q-1))^(q-1).          (PL5)

This is 4 for q=2 and 27/4 for q=3, already above the original product cardinality base q. At any trial base C, the full ledger PL1 stays exact and tensor-additive. The q-product is prior art.

The nine-point 3-partite quadratic cap F9={(x,y,x^2+y^2):x,y in F_3} has 9 original rank-three edges and is 3-free, beating 2^3. Its globally averaged original pairwise intersection rank is 29/27 (87/81), from degree multiset (six degree-3 vertices, two degree-4 vertices and one degree-1 vertex). Individual anchor trace entropy/rank ratios are NOT uniform: the finite exhaustive audit gives three classes, approximately 1.56161381 (four anchors), 1.63675072 (one), and 1.64791843 (four). Tensor powers preserve per-factor additions without an automatic strict saving.

## P5. Averaged published-factor rank-drop controls and strict floors (PROVED from source constructions/degree audits)

For any finite original Q with N edges and degrees d_v, independent uniform ORIGINAL anchors A,B satisfy

    E|A intersect B|=sum_v (d_v/N)^2.                (PL6)

This is a GLOBAL average, not per-anchor regularity. With published finite factors:
- Abbott-Hanson H54 (rank 4, s=3): 18 vertices each degree 12; mean drop 8/9; maximum degree fraction 2/9; density base 54^(1/4).
- Axante et al. H39 (rank 3, s=4): 13 vertices each degree 9; mean drop 9/13; maximum fraction 3/13; density base 39^(1/3).
- Axante et al. H153 (rank 3, s=6): 15 vertices degree 27, 10 degree 5, one degree 4; mean drop 11201/23409; maximum fraction 3/17; density base 153^(1/3). DO NOT assume H153 anchor regularity.

Tensor powers show any asserted universal density-link implication |F|>D^k -> max_v d_v/|F|>=phi is FALSE if D is STRICTLY BELOW the appropriate factor root and phi is STRICTLY ABOVE the corresponding degree fraction (for the matching petal parameter). At D equal to the root, the strict trigger is absent: endpoint unproved either way. The point-link implication for some D,phi for ALL arbitrary original s-free families would itself furnish a fixed-base recurrence, so cannot be assumed.

## P6. Independent finite verification; logical status

New script scripts/original_packet_entropy_audit.py and unittest suite check all 387 sunflower-free 3-uniform subfamilies of 10 triples on five vertices, tracing every original edge exactly once, the PL1 identity, and independently enumerating EVERY pair-certificate capacity against PB1. They also test s=3,4,5 classical products through rank 3; the pair-private examples at k=2,3,4,8,32; the nine-point cap; and the exact global 54/39/153 degree-spectrum formulas. Local standalone script and five unittests PASS. These are finite checks of stated calculations, not an all-k theorem or novelty certification.

**OPEN CENTRAL GAP:** Find a truly cross-trace original-residue compatibility inequality that lower-bounds the conditional slack S_C (or an appropriate coupled analogue) more strongly than worst-case isolated packet capacity, without reintroducing n-dependent anchor entropy, assumed shifted lifts, or hidden f_s(k) hypotheses. Prove a *noncircular* fixed-base induction or give a concrete family falsifying the proposed strict saving. PL1 alone is an identity and NOT a breakthrough towards an upper bound.

Source attribution: Mishra v1 https://arxiv.org/html/2606.02667v1 (invalid unrestricted shift source) versus v2 https://arxiv.org/html/2606.02667v2 (shifted only); classical Erdos-Rado q-products; Abbott-Hanson / Axante et al. https://arxiv.org/abs/2609.06175; Bell-Chueluecha-Warnke https://doi.org/10.1016/j.disc.2021.112367; Rao's January 2026 survey https://doi.org/10.1112/jlms.70380 . No complete proof.