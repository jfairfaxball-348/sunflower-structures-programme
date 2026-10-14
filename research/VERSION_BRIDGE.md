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
| Rank-dependent full-shift bound H_s | tau(SF)<=A_s k/log(k+2) for all s-free F | UNPROVED, and finite P(2,k) tests strongly challenge it |

## Precisely where v1's lifting argument breaks

One compression has exactly one ancestor for each image member and uses only two inverse types, giving factor 2. The inverse ancestor under MANY compressions may differ at several coordinates. V1 partitions a full-shift sunflower by a unique single original source x, presupposing a representation that does not exist. Thus the Step A original preimage sunflower and Step B source graph do not follow. V1 §3 Case 1 also invokes this unproved Step B. V1 §7 then invokes the invalid full-shift bound. An independently false base-2 numerical conclusion follows for s>=4.

The correct v2 theorem governs shifted families only; it cannot provide witnesses in arbitrary original families without a separate bridge. Changing the target from a **fixed-base 2** to a legitimate C_s>=s-1 does not resurrect v1's proof.

## Quantitative no-go and candidate

For q=s-1>=3, P(q,k) is s-free, |P|=q^k and tau(P)=q. Independently established shifted-only bound gives for t=tau(SP):

    (q/2)^k <= (t+1)^(2t),
    t log(t+1) >= (k/2) log(q/2).

So t must grow at least Omega_q(k/log k). No purely tau(F)-dependent uniform full-shift transfer is possible. A *rank-dependent* upper bound of the same order would suffice for C_s^k (proof and exact constant in WORKING_PROOF.md), but has not been established; small full-shift P(2,k) computations produce stars of k+1 petals, warning against such a bound even for s=3.

A rigorous small-support replacement holds for ALL compositions supported on U: tau(G)<=2^|U|tau(F). The unresolved step is structural: bound necessary compression support or supply additional original-source compatibility that avoids exponential inflation inside the shifted extremal bound. Product P(q,k) also kills any constant-fraction shifted original subfamily and demands a nontrivial extraction mechanism.

**State: original-family bridge OPEN. Do not report v1's theorem or the full conjecture as solved.**
