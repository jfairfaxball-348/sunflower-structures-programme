# Exact owner balancing emerging from nonproduct tensor synergy (15 October 2026)

**Scope and verdict.** This note improves NC3 of [NONPRODUCT_ORIGINAL_TENSOR_CORRELATION.md](NONPRODUCT_ORIGINAL_TENSOR_CORRELATION.md) using an **exact integer-checkable rational dual** of the actual ALL-ANCHOR original-record LP. The previously exhibited eight disjoint records in the 45-edge rank-six tensor have non-optimal edge-owner congestion. A 58-record *optimal* dual instead has **perfect edge-owner balance**, despite neither factor admitting perfect owner balance at its optimum. The dual propagates under tensor powers. These are programme-local exact results, **priority NOT CHECKED**. No original fixed-base sunflower theorem or source-lifting proof has been obtained.

## Definitions and elementary sharp inequality (OB1, PROVED)

Fix s>=3 and an s-free original simple uniform H, N=|H|. As in NC1, a record r has s+1 DISTINCT genuine original edge owners (its anchor and s petals), and a nonempty actual defect set D_r. A dual y>=0 is feasible if for each actual ground vertex x, sum_{r:x in D_r}y_r<=1. Set Y=sum_r y_r, m_e=sum_{r:e owner of r}y_r and M=max_{e in H}m_e. For Y>0 define lambda=N M/((s+1)Y).

Because EVERY record has exactly s+1 distinct owners,

    sum_{e in H} m_e = (s+1)Y,
    lambda >= 1, equality iff m_e = (s+1)Y/N for EVERY e in H.     (OB1)

Thus finding a perfectly balanced optimal dual means finding an actual original witness distribution with equality in the sharp *minimum* congestion inequality. In particular, the earlier dual's lambda=225/32 does NOT lower-bound the best congestion.

For an edge-transitive automorphism group of H preserving the actual-record definition, averaging ANY optimal feasible y over the group preserves Y and each actual vertex capacity, while all m_e become equal. Consequently every such H with V_s(H)>0 has a perfectly balanced *optimal* dual. This is a sufficient structural condition, **not** a theorem that sunflower-freeness forces edge-transitivity.

## Factor obstructions: minimum optimal congestion (OB2, PROVED finite)

Let S=AS3 and Q=Q9 from NC2. All records are enumerated by the original script; no preimage of a shifted edge is used.

**S** has exactly THREE anchored records and each record owns both S[0] and S[1]. Distinct singleton defects {a},{b},{c} force V_3(S)=3, and the unique vector y=(1,1,1) is optimal. The two common owner edges necessarily have m_e=3, giving

    min_{optimal y} M(S,y)=3, lambda_opt(S)=5*3/(4*3)=5/4.          (OB2a)

**Q** has TWENTY records. Fix e0=Q[0] and the actual ground vertex z=(2,1) (coordinate/value). Direct enumeration verifies that EVERY record either owns e0 OR has z in its defect (possibly both). Hence for every feasible y of Y=V_3(Q)=3,

    m_e0 >= sum_{r:z NOT in D_r} y_r >= Y-sum_{r:z in D_r}y_r >= 2.

Equality M=2 is witnessed by unit y on original-record indices 7,10,12 under the deterministic original enumeration. Their defects are vertex-disjoint, their owner loads are <=2, and Y=3. Thus

    min_{optimal y} M(Q,y)=2, lambda_opt(Q)=9*2/(4*3)=3/2.          (OB2b)

The record-incidence covering property, indexed examples and primal V values are checked by the new stdlib audit alongside the original audit. This is an exact combinatorial argument rather than reliance on floating-point optimisation.

## T=S tensor Q: perfect balance despite both imbalanced factors (OB3, EXACT)

Let T=S tensor Q, with 45 ORIGINAL edges and 17 actual ground vertices; the original NC2 integer primal cover proves V_3(T)<=8. All 6403 records and 457 distinct defects are identical to those in NC2. In

    scripts/original_owner_balancing_audit.py

CERT is a list of 58 pairs (deterministic ORIGINAL record index, positive integer numerator), with common denominator

    L=656234357670.

The script verifies using only Python standard-library **integer arithmetic**:

1. every indexed record owns exactly 4 DISTINCT edges of the ORIGINAL 45-edge family, and has its actual enumerated nonempty defect;
2. the integer numerators sum to 8L, so the dual objective is exactly Y=8;
3. for each of the 17 ACTUAL vertices x, the total numerator mass over selected defect sets containing x is at most L;
4. for **each** of the 45 ORIGINAL edges e (anchor AND petals counted), the total owner numerator mass is exactly 32L/45, an integer.

Therefore y is an exact feasible *optimal* dual (NC2's primal cover has size 8) and EVERY original owner has m_e=32/45. By OB1 the minimum congestion of any optimal dual is attained at the theoretical floor:

    V_3(T)=8, M_opt(T)=32/45, lambda_opt(T)=1.                   (OB3)

The previously reported eight-unit, disjoint-defect certificate has M=5 and lambda=225/32. It is still a valid dual but NOT a minimum-congestion optimal dual. This correction is important: strict cross-factor synergy and factor imbalance can coexist with PERFECT composite owner balancing.

Under NC3, for ANY n-edge ORIGINAL subfamily F subset T, the new actual balanced certificate gives

    V_3(F) >= max(0, 8-(45-n)*32/45)
           = max(0, (32n-1080)/45).                             (OB4)

It is strictly positive for integer n>=34, versus n>=44 from the prior high-congestion witness. The threshold is relative to the entire fixed 45-edge family: no arbitrary original F is known to embed in T.

## Tensor propagation and density threshold (OB5, PROVED all ranks)

**Tensor-lift lemma.** Suppose disjoint-ground s-free uniform H,K have feasible original-record duals y_H,y_K with masses Y_H,Y_K and perfect owner balance (not necessarily optimal). Lift every H record with each fixed K edge, dividing its mass by |K|, and independently every K record with each fixed H edge, dividing by |H|. Exact nonempty equal-trace sunflower conditions hold for the lifted records; original defects remain in their own ground blocks. Vertex dual loads of H and K do not increase. At each original product edge (h,k), owner loads equal

    m_(h,k) = m_h(H)/|K| + m_k(K)/|H|
             = (s+1)(Y_H+Y_K)/(|H||K|).

Thus the union dual has mass Y_H+Y_K and is perfectly balanced, with no fake owners. Its optimality is NOT asserted because NC1 only supplies a lower bound for V_s(H tensor K).

Apply this lemma to T in OB3, recursively over disjoint copies. For every m>=1 the rank-6m, 45^m-edge original 3-free family T^m carries an EXACT feasible balanced dual with

    Y=8m,  m_e=32m/45^m for EVERY original edge,
    V_3(T^m)>=8m.                                                  (OB5)

Together with independent factor copies, this gives a per-six-rank-block strict certificate saving 8>3+3, at most a **linear-in-rank** conclusion; it is NOT a proof of superlinear V, and not a bound on original-family cardinalities.

For any subfamily F of T^m of relative density delta=|F|/45^m, NC3 now gives

    V_3(F) >= m * max(0, 32 delta - 24).                          (OB6)

This is strictly positive for delta>3/4. Its density is relative to T^m, not an arbitrary ambient family. Importantly 45^(1/6)<2, so T^m is exponentially SMALLER than the classical 2^(6m) binary-product lower construction. Even strong balanced synergy of this type does not populate the high-density regime above a necessary C_3>=2, much less exceed the H54 base 54^(1/4). Non-vacuity above an explicitly justified density threshold remains unproved.

## Global-to-local and recurrence attacks: what failed

**Route A, weighted dual/DRC:** OB3 removes owner-congestion as the obstruction for T, but V and its balanced mass are sums of *defect capacities*, not a lower bound on max_x deg_F(x)/|F|. No implication from lambda=1 or V>=a k to a fixed positive original link fraction has been proved. The classical P(s-1,k) already has balanced duals, linear V and constant fractional point links; the independent H54/H39/H153 tensor link fractions are exactly 2/9, 3/13, 3/17. This mix does not establish a density-sensitive link theorem.

**Route B, maximal matching and original links:** If |F|>0 is s-free rank k, its maximum matching has <=s-1 edges. The union hits F, giving max_x deg_F(x)/|F|>=1/((s-1)k). Hence f_s(k)<=(s-1)k f_s(k-1), an honest original recurrence which grows factorially. It cannot be replaced by coefficient 2 from k=1 to k=2 when s=3: the disjoint union of two triangles has six original edges, no 3-sunflower and f_3(2)=6>2 f_3(1)=4.

**Exact conditional escape hatch (no premise proved).** If explicit D_s>1 and phi_s>0 exist such that every s-free ORIGINAL k-family of size strictly greater than D_s^k has a point link of fraction at least phi_s, then

    f_s(0)=1, f_s(1)=s-1,
    f_s(k) <= max(D_s^k, phi_s^(-1) f_s(k-1)),

implying f_s(k)<=C_s^k for C_s=max(D_s,phi_s^(-1),s-1,1). The proof is simple: families at most D_s^k are already bounded; any larger family has a real rank-k-1 link, which is s-free. This is a valid CONDITIONAL inference, not evidence that the high-density premise holds. Tensor H54 forbids phi_3>2/9 for D_3<54^(1/4), H39 forbids phi_4>3/13 below 39^(1/3), and H153 forbids phi_6>3/17 below 153^(1/3); no endpoint nonstrict density assertions are made.

**Audit of small ranks/core cases:** k=0 allows only the single empty ORIGINAL edge, so f_s(0)=1. k=1 has f_s(1)=s-1 distinct singleton originals, with empty core. k=2,s=3 has f_3(2)=6 (two triangles); pairwise nonempty-core 3-stars and empty-core 3-matchings are both forbidden. For s=4,6 the standard P(s-1,k) yields lower bounds 3^k,5^k at k=0,1,2,3 and all-zero/nonzero cores are accounted for by the actual original-sunflower definition. Published H54/H39/H153 are NOT freshly enumerated by this audit. Nothing from shifted v2 is used to assert original members.

## Source and novelty ledger

- [Mishra v1](https://arxiv.org/html/2606.02667v1): claimed universal base-two bound FALSE for s>=4 via P(s-1,k); multi-shift original-ancestor step invalid. **SOURCE CLAIM/REFUTED**, not available as an original-family lemma.
- [Mishra v2](https://arxiv.org/html/2606.02667v2): SHIFTED families only. **SOURCE CLAIM**, independently audited special recurrence in WORKING_PROOF.
- [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367), [Rao survey 2026](https://doi.org/10.1112/jlms.70380): known O_s(log k)-base upper regime, not fixed C_s. **PUBLISHED**.
- [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995), [Shangguan](https://arxiv.org/abs/2609.30263): fixed/bounded VC-dimension upper bounds with d dependence; products P(2,k) have VC dimension k. **SOURCE CLAIM**. Shangguan's abstract gives (C s log(d+1))^k and is not an unrestricted bound when d grows with k.
- [Axante et al.](https://arxiv.org/abs/2609.06175): published finite lower factors and related results; do not claim them new. **PRIOR ART**.
- **OB1–OB6: PROVED internally** by symbolic arguments and finite integer-checkable certificate. New mathematics-literature novelty and priority **NOT CHECKED**.
- **OPEN:** high-density all-original link theorem, a useful density-above-lower-bases original rank contraction, superlinear tensor certificate behaviour, unrestricted f_s(k)<=C_s^k. No claimed solution or v1->v2 lifting.
