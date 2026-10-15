# Mishra v1 → v2: corrected bridge audit, 14 October 2026

The full Erdős–Rado sunflower conjecture is NOT proved here. See [independent working proofs](WORKING_PROOF.md) and the two primary versions [v1](https://arxiv.org/html/2606.02667v1) and [v2](https://arxiv.org/html/2606.02667v2). f_s(k) denotes maximum size of a simple s-free k-family (avoid ambiguity between 'at least' and 'more than' threshold conventions). No petals of empty size; original sets distinct; empty CORE is allowed.

## Claim-by-claim verdict

| Location | Claim | Verdict |
| --- | --- | --- |
| v1/v2 §2 shadow | k|F| <= tau(F)|partial F| | PROVED independently; double count extension incidences |
| v2 §3 / Appendix B | Single C_ij satisfies tau(C_ij F)<=2tau(F) | PROVED; exact sharp factor 2 from two disjoint m-stars, m>=3 |
| v2 §4 shifted half-link | |A_i|>=|B_(i-1)|/2 when tau<=k | PROVED independently, with empty B_i handled |
| v2 §5 small-rank | f_s(k)<=s^(2k), k<=s | PROVED with exact s-petal induction; source says 's+1' inconsistently |
| v2 §6 rank recurrence | f'_s(k)<=2f'_s(k-1) for k>=s | PROVED; rank-(k-1) first link remains shifted and s-free |
| v2 corollary | f'_s(k)<=s^(2s-2)2^k | PROVED; loose but valid |
| v1 §3 full-shift source graph | Each final shifted S with 1 in S comes from one original replacement x->1 | FALSE as claimed: {{3,4}}→{{1,2}} |
| v1 §3 full-shift bound | tau(SF)<=3tau(F)^2 | FALSE as universal statement, by product + independently verified v2 bound |
| v1 §7 unrestricted bound | f_s(k)<=(3s²)^(6s²-2) 2^k | FALSE for s>=4, by P(s-1,k) |
| Natural shifted-original-subfamily extraction | Every product P(q,k) contains large genuinely shifted ORIGINAL subfamily | FALSE: every such subfamily has <=q members, for ANY point ordering |
| Arbitrary-family constant-density link | Every s-free F has a vertex in c_s|F| sets | FALSE: pair-private k+1-set construction has maximum degree 2 |
| Global support-U inverse | If preimages preserve outside U then tau(G)<=2^|U|tau(F) | PROVED (colour ancestors by original U trace) |
| Rank-dependent full-shift bound H_s | tau(SF)<=A_s k/log(k+2) for all s-free F | **FALSE for every fixed s>=3** under lex shifting; universally proved spoke-to-star theorem |

## Precisely where v1's lifting argument breaks

One compression has exactly one ancestor for each image member and uses only two inverse types, giving factor 2. The inverse ancestor under MANY compressions may differ at several coordinates. V1 partitions a full-shift sunflower by a unique single original source x, presupposing a representation that does not exist. Thus the Step A original preimage sunflower and Step B source graph do not follow. V1 §3 Case 1 also invokes this unproved Step B. V1 §7 then invokes the invalid full-shift bound. An independently false base-2 numerical conclusion follows for s>=4.

The correct v2 theorem governs shifted families only; it cannot provide witnesses in arbitrary original families without a separate bridge. Changing the target from a **fixed-base 2** to a legitimate C_s>=s-1 does not resurrect v1's proof.

## Quantitative no-go and candidate

For q=s-1>=3, P(q,k) is s-free, |P|=q^k and tau(P)=q. Independently established shifted-only bound gives for t=tau(SP):

    (q/2)^k <= (t+1)^(2t),
    t log(t+1) >= (k/2) log(q/2).

So t must grow at least Omega_q(k/log k). No purely tau(F)-dependent uniform full-shift transfer is possible. A rank-dependent upper bound of the same order would logically suffice for C_s^k, but that specific H_s premise is **FALSE**: the universal proof in [SPOKE_SHIFT_THEOREM.md](SPOKE_SHIFT_THEOREM.md) gives a permanent shifted star with (q-1)k+1 petals for every q>=2, k>=2 in the lexicographic full shift of P(q,k). Even the sparse (q-1)k+1-edge original spoke family shifts EXACTLY to this star. Thus the earlier finite observations have been upgraded to a complete symbolic negative theorem for all s>=3.

A rigorous small-support replacement holds for ALL compositions supported on U: tau(G)<=2^|U|tau(F). The unresolved step is structural: bound necessary compression support or supply additional original-source compatibility that avoids exponential inflation inside the shifted extremal bound. Product P(q,k) also kills any constant-fraction shifted original subfamily and demands a nontrivial extraction mechanism.

**State: original-family bridge OPEN. Do not report v1's theorem or the full conjecture as solved.**

## New resolved question: linear shift inflation on sparse spokes

For q>=2 and k>=2 the original simple q-ary sparse spoke family T(q,k) has tau=q and (q-1)k+1 edges. One lexicographic compression pass maps it bijectively to the (q-1)k+1 edges with core [k-1] and singleton petals k,...,qk. The q-ary product P(q,k) also acquires all these edges in that pass and keeps them during subsequent compressions. This is a direct proof with exact quantifiers and with old-family collision handling, not an extrapolation. Consequently the conditional H_s implication in WORKING_PROOF remains logically valid, but the premise is refuted for all s by q=s-1. **Next bridge must contain compatibility information on original preimages or use an independent rank reduction.**


## 14 October addendum — dense original families can still inflate linearly

An additional rigorous [graph tensor and partial-spoke theorem](DENSE_ANCESTOR_OBSTRUCTION.md) strengthens the obstruction from sparse examples and q-ary products. For q=s-1, one can take rank K=2m, original q-free families of size b_q^K with b_q>q, yet lex shifting creates at least c_q*K+1 petals with one common core. Explicitly b_q=sqrt(q(q+1)) when q is even, and b_q=sqrt(q^2+(q-1)/2) when q is odd. This disproves the k/log(k+2) full-shift sunflower-number premise **even if it is restricted to original families of size >=D^K for any D<=b_q**. It does NOT falsify every possible high-density lemma or prove an unrestricted result. Rank-two extremal graph ideas are established prior art; the present proof and compression diagnostic are not asserted as first discoveries.

A collision-safe partial-spoke propagation lemma gives the quantitative result without assuming unique ancestors. The correct next attempt requires genuine compatibility of *original* petals and an exact fixed-base rank recurrence; simply changing a shifted-family size threshold is not enough below b_q.


## Further hostile audit — September 2026 high-rank factors (14 October session)

The older rank-two base b_q in DENSE_ANCESTOR_OBSTRUCTION.md is NOT the best obstruction discovered from available literature. By [HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md](HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md), published 54-member rank-four (s=3) and 39-member rank-three (s=4) sunflower-free families contain suitable original one-swap witnesses. Their tensor powers and a collision-safe lex-shift proof disprove the proposed O_s(K/log K) shifted-sunflower-number transfer **through D<=54^(1/4) for s=3** and **through D<=39^(1/3) for s=4**, strictly above the previous sqrt(6) and sqrt(10) cutoffs. These are limitations on this shifting-based bridge, not lower bounds on every possible proof method. The 54 family also saturates k|F|<=2|partial F| at every tensor rank 4m, refuting a naive density-forced strict improvement of the shadow inequality. Its construction originates with Abbott–Hanson; the 39 family is from Axante et al. (2026), both credited in SOURCE_REGISTER.md. The FULL conjecture is still OPEN.


## 14 October continuation: intersecting originals and six-petal factor

The next independently audited obstruction, including a standalone symbolic argument, is in [SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md](SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md). The published Axante et al. 153-edge rank-three family is six-sunflower-free; its anchor has NINE distinct original one-swap outsiders. By the collision-safe lemma, its K=3m tensor shifts to a star with >=3K+1 petals although original tau=5 and cardinality is (153^(1/3))^K. Density-restricted O(K/log K) full-shift transfer is FALSE through D<=153^(1/3) for s=6.

Even an INTERSECTING-original restriction cannot rescue that kind of transfer at D<153^(1/3): fixing one tensor coordinate to an original vertex-star leaves a constant fraction of the exponential size and nine per FREE coordinate shifting witnesses. The analogous statement holds at D<54^(1/4) for s=3 and D<39^(1/3) for s=4. Exact endpoints are NOT asserted for the restricted families.

An independent original-family reduction gives i_s(k)<=f_s(k)<=(s-1)k*i_s(k), where i_s is the INTERSECTING extremal function. Hence a fixed-base upper bound on intersecting ORIGINAL families would be sufficient, but it is equivalent to the full conjecture and remains OPEN. This is not an inference from Mishra v2's shifted-only theorem. Correct exact-trace bookkeeping also includes T=empty with matching number<=s-2, though the rank-k residue still blocks naive induction.


## New non-shifting original link route (14 October; local only)

[Multiwitness compatible trace proof](ORIGINAL_MULTIWITNESS_TRACE_RANK_REDUCTION.md): r distinct disjoint-outside original witnesses E=T+V, A_i=T+W_i in an INTERSECTING s-free k-family force each opposite exact trace U subseteq V of size u into at most h^r genuine (k-u-r)-uniform original links (h=|V|, r<=s-2). At h=1, this is coefficient-one rank-(r+1) reduction, sharp in finite families. It is not the missing unrestricted v1/v2 transfer because no theorem establishes a bounded-cost global partition of the original family into those opposite traces. Multi-shift source uniqueness remains false; shifted-only v2 bounds remain restricted.


## 15 October 2026 — another original-witness bridge attempt falsified

The local multiwitness Theorem A remains valid, but there is no positive mass prevalence even for large original INTERSECTING s-free families with EMPTY global core: triangle tensor Q^m, for any core-free finite factor Q, has at most an exponentially small fraction of its original members meeting a fixed original anchor E in O_s(1) points. Every opposite trace of an h=O_s(1) compatible witness lies there. The explicit all-rank counterexample and 54-edge factor polynomial appear in [TRIANGLE_TENSOR_PREVALENCE_OBSTRUCTION.md](TRIANGLE_TENSOR_PREVALENCE_OBSTRUCTION.md). Thus no trivial global bounded-anchor cover and no v1/v2 unrestricted bridge. This is a negative result for the local-rank-descent globalisation mechanism, not for original-family exponential upper bounds. The next task is central-trace charging or an independent original recurrence.
