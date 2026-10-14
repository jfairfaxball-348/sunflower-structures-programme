# Full-shift spoke theorem — symbolic obstruction (14 October 2026)

**Status: proved by an elementary, rank-uniform argument.** This theorem REFUTES the proposed rank-dependent transfer hypothesis H_s; it DOES NOT prove the unrestricted Erdős–Rado conjecture. The finite tests are independently executable diagnostics, not substitutes for the proof.

## Precise framework

Let k>=2, q>=2, and n=qk. Give the n vertices their natural order. For 1<=l<=k let V_l={l+ak: 0<=a<=q-1}; the V_l partition [qk]. The q-ary product P(q,k) is the family of all k-sets containing exactly one vertex of each V_l. It has q^k members and its largest sunflower has q petals: q petals are obtained by varying just one coordinate; any sunflower of at least two distinct transversals must vary in some coordinate, and the values in such a coordinate must be pairwise distinct, so it cannot have more than q petals.

Let K=[k]. Define the **sparse spoke** subfamily

    T(q,k) = {K} union { (K\{l}) union {l+ak} :
                            1<=l<=k, 1<=a<=q-1 }.

All these (q-1)k+1 k-sets are distinct original product members, so T(q,k) has sunflower number exactly q (q members obtained by varying one coordinate; no q+1-sunflower as T is a subset of P).

Use the standard simultaneous Frankl C_ij: for an edge E containing j but not i, replace j by i only if the replacement is absent from the CURRENT old family. Apply C_ij in lexicographic order, increasing i, then increasing j, once over 1<=i<j<=qk; any additional shifts may follow.

## Main theorem

**Theorem (sparse spokes collapse to a star).** After that one complete lexicographic pass, T(q,k) becomes EXACTLY

    Star(q,k) = { [k-1] union {x} : k<=x<=qk }.

Consequently the full image contains (q-1)k+1 distinct members with common core [k-1]. Moreover, for the full product P(q,k), the same pass creates and permanently retains Star(q,k) as a SUBFAMILY, even though its original maximum sunflower has just q petals. The star persists under every later elementary compression C_ij, regardless of order. In particular any globally shifted image obtained by continuing the lexicographic pass contains the star.

### Proof, including the simultaneous-shift collision case

The argument applies to ANY initial k-family F containing T(q,k), not only T or P.

Fix a high vertex x=l+ak with 1<=l<=k-1 and 1<=a<=q-1. For l<=t<=k define

    B_t(x)=([k]\{t}) union {x}.

Initially B_l(x) is present. It contains [l-1], so all operations whose first index i<l leave B_l(x) unchanged. At the beginning of phase i=l, B_l(x) therefore exists. For any t with l<=t<k, suppose B_t(x) exists at the beginning of phase i=t. It contains every vertex of [t-1], so earlier phases do not affect it, and within the current phase the FIRST pair is (t,t+1). In this pair, B_t(x) contains t+1 and avoids t. Its candidate replacement is precisely B_(t+1)(x).

If B_(t+1)(x) is already in the old family, it remains as an unchanged member of C_(t,t+1)(F): it contains t and thus cannot itself move in this operation. Otherwise the operation replaces B_t(x) by B_(t+1)(x). In either case B_(t+1)(x) exists immediately after the pair. It contains t, so no remaining operation of phase t can move it. Therefore B_(t+1)(x) exists when phase t+1 starts. Induction on t gives B_k(x)=[k-1] union {x} after phase k-1.

This reasoning is **not** an invalid claim of a unique original ancestor. At each induction step either the specific replacement is created or it was already available, and both cases are covered. It also remains valid with arbitrary additional members of F.

For x=k+ak (the high vertices of the last block V_k), [k-1] union {x} was already an original member. Likewise K=[k]=[k-1] union {k} is original. All these edges contain [k-1], so every compression with first index i<=k-1 leaves them alone. By the end of phase k-1, for every x in [k,qk] the edge [k-1] union {x} is present. The set of high vertices x=l+ak for l<=k-1 and a>=1, together with x=k and x=k+ak for a>=1, is EXACTLY [k,qk].

Finally this full star is fixed setwise by EVERY elementary compression. If i<=k-1, every star edge contains i, hence it is unchanged; if i>=k, a possible replacement of a star edge [k-1]+{j} with j>i is [k-1]+{i}, itself present in the star, and therefore the current-family collision rule prevents the move. Neither an additional outside edge nor any compression can remove a star member, as every such move is blocked by a member of the star. The star thus survives the rest of the pass and all subsequent passes.

For F=T(q,k), every member is in the star by the end and compression preserves family cardinality; |T|=|Star|=(q-1)k+1, so equality holds. For F=P(q,k) only containment is asserted. QED.

## Consequence: H_s is FALSE, for every fixed s>=3

The previously proposed hypothesis H_s said: for fixed s there is A_s<infinity such that for every original s-free k-family F, the lexicographically fully shifted image G satisfies

    tau(G) <= A_s*k/log(k+2) (k>=2).

Set q=s-1 and take F=T(q,k) (or F=P(q,k)); it is s-free and after shifting tau(G)>=(q-1)k+1=(s-2)k+1. Hence

    tau(G)*log(k+2)/k >= (s-2)*log(k+2)

diverges as k grows. No such A_s exists. This is a universal, symbolic counterexample for the ACTUAL lexicographic shifting sequence, rather than extrapolation from k<=8 computations. It strengthens the previous product-based lower bound Omega_q(k/log k) to an EXPLICIT Omega_q(k) for this prescribed order. It does NOT assert the same lower bound for every possible shifting schedule.

## Implications for future bridges

1. A bridge whose ONLY quantitative input is the full-shift sunflower number and H_s is no longer viable. Replacing H_s by a linear tau upper bound and feeding it into the loose shifted-only estimate 2^k(t+1)^(2t) incurs exp(O(k log k)) rather than a fixed-base exponential. This does not rule out a strengthened two-parameter shifted estimate or an ancestor-compatible transfer.
2. The sparse example is more diagnostic than the full product for witness lifting: q petals are possible in the original, whereas (q-1)k+1 are manufactured in its shifted image. A universal final-sunflower lifting certificate must use origin-pattern information not encoded by tau(G) alone.
3. This negative theorem is intentionally narrow. It does NOT show that every full-shift sequence of P(q,k) has a linear sunflower, does NOT exclude a useful partial shifting algorithm, and does NOT imply anything like a complete proof of the full conjecture.
4. Useful next target: formulate a genuinely **original-ancestor** induction or weighted link/fibre dichotomy whose per-rank loss is O_s(1), robust to T(q,k), P(q,k), pair-private configurations, and two-star one-shift sharpness.

## Finite independent corroboration

See scripts/spoke_shift_audit.py and tests/test_spoke_shift_audit.py. They independently generate the sparse family, product and standard old-family simultaneous shifts and verify equality/containment for finite grids of q,k, including one full lexicographic pass. These checks do not establish the quantified theorem: the displayed induction does.
