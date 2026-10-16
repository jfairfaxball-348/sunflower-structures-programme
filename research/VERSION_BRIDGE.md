# Mishra v1 → v2: corrected bridge audit, 14 October 2026

**16 October two-anchor update:** [TWO_ANCHOR_PRIMITIVE_CAPACITY.md](TWO_ANCHOR_PRIMITIVE_CAPACITY.md) proves the core-free intersecting ORIGINAL residual class with exact integral cover 2 and fractional cover/matching 3/2 retains the entire unrestricted exponential growth rate: 3 f_s(d)<=b_s(d+2)<=2 f_s(d+1). Literal triangle/private substitution preserves arbitrary H and VC dimension; a bounded-base even subexponential-overhead estimate on this special class is equivalent to the unsolved conjecture. Exact two-anchor canonical and trace-row decompositions give honest rank payments for 2-covered originals but do not apply to all originals, and this class is not preserved by links. Six sampled physical cases and independent tests corroborate the all-rank proof. NO unrestricted proof or novelty claim.

**16 October prior residual-capacity result:** [LRC1–LRC7](LOGARITHMIC_SHELL_RESIDUAL_CAPACITY.md) uses only actual original sets. Replacing the correlated pair-star shell by an intersecting triangle tensor reduces its rank to 2 log_3 n and removes the group marker: exponentially small relative core error can still cost half the original owners to purify, even with core-free neighbour residuals. A nonempty common D can be adjoined without changing the obstruction. The exact inequality 3f_s(d)<=i_s^0(d+2) prevents treating core-free intersecting residual exponential bounds as independent progress. A supplied finite-seed construction tree admits a proved fixed-base upper bound, but a reconstructed prior-art rank-ten shared-ground construction of 21552 three-free edges disproves universality at the H54 catalogue base. A larger-base grammar repair is proved only for that restricted class. These do not repair v1's invalid cumulative source attribution or extend v2 beyond shifted families; the unrestricted problem remains OPEN. Product/Fekete growth is classical; external priority of programme packaging is NOT CHECKED.

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


## 15 October continuation: exact central traces do descend, but entropy blocks closure

[Standalone central-trace and LP note](CENTRAL_TRACE_AMORTISATION.md) proves the s=3 ORIGINAL proper-trace residue is always intersecting (even if the original family is core-free), yielding i_3(k)<=sum_(u=1)^k binom(k,u)i_3(k-u). The upper envelope 1/(2-e^x) is factorial and does NOT bridge v2 shifted-only to unrestricted petals. Exact triangle q-product and H54 overlap polynomials account for all central traces. Optimal H=1 fractional anchor cover requires exponential **total** weights (3/2)(q/(q-1))^m and (3/2)2^m; per-edge charges can nonetheless be exactly one. This is a rigorously limited no-go, not a full-conjecture obstruction. H153 polynomial is averaged only. Multiwitness packet recurrences still contain f_s(k-2), not i_s(k-2), and unspecified high-density thresholds may be vacuous. **Full conjecture OPEN.**


## 15 October 2026 — cross-trace collision and original-link no-go

[Cross-trace entropy and links](CROSS_TRACE_ENTROPY_AND_LINKS.md) derives a NEW-TO-THIS-PROGRAMME (not literature-novelty-certified) original triple-trace collision energy inequality and shows explicit disjoint/overlapping original trace sunflowers that do NOT lift. The completely normalised scalar LP for z^|E intersect B| grows exponentially on triangle q-products and H54 powers; apparent moment contraction therefore cannot, by itself, close the unrestricted bridge. ORIGINAL tensor factors refute a dense link premise for D<54^(1/4), phi>2/9 (s=3) and D<153^(1/3), phi>3/17 (s=6); no endpoint claim. Nonvacuous n<=3k link counting is only AMBIENT-RESTRICTED. The full original conjecture and any viable v2-to-original witness bridge remain OPEN.


## 15 October continuation — private defects do not automatically defeat central entropy

[PARTIAL_MULTIPLICITY_DUAL.md](PARTIAL_MULTIPLICITY_DUAL.md) improves the triple-trace CT1 inequality: three distinct original traces forming a sunflower force an outside vertex belonging to exactly two residues, not merely a generic pair collision. For all s>=3, an s-tuple requires occupancy 2,...,s-1 somewhere. This removes a shared-hub false positive but does NOT bridge v2's SHIFTED theorem to ORIGINAL witnesses. A central equal-trace-rank coordinate vector LP on triangle tensor P(s-1,m) has **exact** optimum m/s with explicit dual for every 1<=r<=m-s+1, paid by unavoidable local defects. It refutes this specified coordinate-amortisation mechanism as an exponential-saving proof but leaves correlated multi-anchor original rank reductions open. A correct random k-colouring reduces unrestricted families to ORIGINAL transversal k-partite families losing at most e^k in cardinality; no constant-base partite theorem has been established. No original C_s^k bound and no source-lifting theorem follow.


## 15 October 2026: new original-partite information cannot lift shifted v2

The verified actual-original edge-tuple coordinate LP on classical P(s-1,m) has exact m/2 primal/dual optimum and does not price coupled rank drops. The exact k-partite original-family product-support entropy certificate is sharp on P(s-1,k), so it does not replace the invalid cumulative full-shift original-source lifting of Mishra v1 or prove any unrestricted bound. See [CORRELATED_PARTITE_ORIGINAL_DEFECTS.md](CORRELATED_PARTITE_ORIGINAL_DEFECTS.md). Full conjecture OPEN.

## 15 October continuation — actual pair-certificate capacity cannot replace original lift

[ORIGINAL_PAIR_BUDGET_AND_TENSOR_ENTROPY.md](ORIGINAL_PAIR_BUDGET_AND_TENSOR_ENTROPY.md) now proves a global LP that indexes ONLY real original edge pairs and common vertices, with exact no-overcount capacity on distinct original s-tuples. It has a universal quadratic lower bound and, on the full binary product P(2,m), an explicit nonlinear primal giving Lambda_3=Theta(|F|^2). Thus even an actual-edge, multi-anchor pair witness charge normalised by |F|^2 gives no intrinsic exponential rank savings. Anchored trace entropy is exact but not a decrement; nine-point ternary cap tensors make the earlier product-support E3/E5 vacuous. There is still NO legitimate replacement for v1 cumulative original-source lifting from the shifted v2 theorem. Full conjecture OPEN.


## Further original-witness bridge audit — exact packet accounting (15 October 2026)

[Original-owned packet entropy and slack](ORIGINAL_PACKET_KRAFT_AND_ENTROPY.md) proves each actual original edge is owned once by its exact trace relative to a real anchor and shows the rank/entropy/slack ledger is an IDENTITY, not a bridge. In intersecting 3-free pair-private examples the entropy/rank ratio diverges; on classical q-products conditional residue slack exactly balances trace entropy. Any claimed v1-to-unrestricted repair must add a noncircular cross-trace compatible-residue restriction, not merely ensure original edge ownership or shifted witnesses. Original theorem OPEN; shifted v2 separate.


## 15 October: cross-trace shielding prevents direct packet-based v1 repair

[CROSS_TRACE_TENSOR_SHIELD_AND_VC_BARRIER.md](CROSS_TRACE_TENSOR_SHIELD_AND_VC_BARRIER.md) gives a source-compatible, ORIGINAL-witness finite shield: s distinct exact traces form a sunflower and each of their residue packets can contain a^m members, yet no compatible original s-tuple exists; a single fixed vertex is sufficient to violate sunflower compatibility regardless of tensor rank. Therefore a cumulative v1 original-source lift cannot be repaired merely by large packet cardinalities, an independent per-block PM1 defect credit, or the PL1 entropy bookkeeping identity. This is **not** a universal high-density no-go or a proof of the conjecture. The restricted v2 shifted theorem is still separate.

The newer bounded-VC sources, Ge et al. arXiv:2609.18995 and Shangguan arXiv:2609.30263, are useful conditional structural upper bounds but do not solve unrestricted high-VC cases: even the classical original binary product P(2,k) has VC dimension k and any fixed-VC original subfamily has polynomial cardinality.


## 15 October: alternating shield beyond the permanent-vertex repair

[ALTERNATING_SHIELD_RECTANGLE_DUAL.md](ALTERNATING_SHIELD_RECTANGLE_DUAL.md) strengthens the original-shift lifting no-go: even when EVERY outside vertex fails to be a common partial-multiplicity defect of all residue choices, the s sunflower-shaped ORIGINAL trace packets can be entirely incompatible. The smallest specified anchor/singleton-trace configuration has s+2 original rank-s edges (five for s=3), two alternative defect vertices, and no single permanent blocker. Tensor powers have exponentially large original packets but local fractional defect-cover value exactly 2 irrespective of rank. Thus "remove compulsory single-vertex collisions and lift" is FALSE. Exact rank recurrence for the full original family remains OPEN; neither the v1 full-shift ancestor claim nor the v2 shifted-only theorem supplies it. See the note for all quantifiers, proof and original-witness tests.


## Global anchor reuse versus shifted transfer (15 October 2026)

The ORIGINAL all-anchor/equal-trace-rank fractional defect-cover LP has exact value (s-1)k/s on classical P(s-1,k) for k>=s, by a ground-vertex-transitive orbit of a real tight s-petal selection. This is a LINEAR-RANK obstruction to a bounded GLOBAL multishield LP, not merely to a rectangle-local or one-shift argument. It never identifies shifted-image petals as original petals. Original edge participation in canonical distinct anchored box templates is exactly s floor(k/s), exhibiting cross-anchor reuse. See research/GLOBAL_MULTISHIELD_ORIGINAL_OWNERSHIP.md. Mishra v1 full-shift transfer still invalid, its O_s(2^k) full bound false for s>=4; v2 concerns shifted families only. Unrestricted fixed-base rank descent OPEN.


## 15 October: density-sensitive heterogeneous ORIGINAL multishield (independently derived, not a full bridge)

[HETEROGENEOUS_PRODUCT_DENSITY_DUAL.md](HETEROGENEOUS_PRODUCT_DENSITY_DUAL.md) proves an exact LP value and explicit actual-original dual for variable-size product alphabets 1<=q_j<=s-1, plus density robustness at delta>s/(s+1), and the all-anchor alternating-seed LP 3. The new density bound is relative to the ENTIRE product box, and cannot be applied to arbitrary original families without a proved box representation. It is a certificate COVER lower bound, NOT a global sunflower cardinality upper bound; tensor factors above the classical product base are counterexamples to naive density-excess lifting. v1 remains INVALID as full-family transfer, v2 remains SHIFTED-ONLY, unrestricted C_s^k OPEN.


## 15 October 2026 — strictly nonseparable ORIGINAL tensor-certificate phenomenon

[Exact global AS3 tensor Q9 audit](NONPRODUCT_ORIGINAL_TENSOR_CORRELATION.md) establishes a genuinely ORIGINAL all-anchor LP with V_3(AS3 tensor Q9)=8>3+3=V_3(AS3)+V_3(Q9), exact integer primal/dual witnesses, 6403 records, and independently double-enumerated 457 defect sets. Global LP superadditivity holds universally for tensor products of s-free ORIGINAL families and owner-congestion yields a general honest density-deletion inequality. None of these certificates bounds f_s(k) by C_s^k: iterated tensor costs remain linear and balanced owner use is not forced. The invalid multi-shift original-ancestor step of v1 is NOT repaired; v2 is SHIFTED only. Full conjecture OPEN.


## 15 October: balanced ORIGINAL owners still do not imply a v2-to-original transfer

[Exact optimal owner balancing](OPTIMAL_ORIGINAL_OWNER_BALANCING.md) refutes the local suspicion that strict cross-factor certificate synergy intrinsically causes unavoidable original owner concentration: V_3(AS3×Q9)=8, lambda_min=1 with a 58-term integer-verifiable rational dual, versus optimal factor minimum congestions 5/4 and 3/2. This gives exact high-relative-density deletion within the 45-edge original tensor and its powers. It is **not** a structural original rank contraction: the tensor density base 45^(1/6)<2, the LP lower bound grows only 8m, and there is no proved conversion into a point-link fraction or sunflower. The conditional high-density link-to-recurrence implication is valid but its high-density premise is unproved. v1's ancestor transfer remains INVALID and its universal base-two bound FALSE for s>=4; v2 remains SHIFTED-only. The full unrestricted conjecture is OPEN.

## 15 October — balanced LP does not supply an ORIGINAL link fraction

[Original pair-star quadratic barrier](ORIGINAL_PAIR_STAR_QUADRATIC_LP_OBSTRUCTION.md) (PS1–PS3, internally PROVED) uses n ORIGINAL rank-(n-1) owners indexed by K_n vertices, on ground points indexed by K_n edges. All pairs of original edges meet at a unique, varying ground point; hence all s>=3 are sunflower-free. The genuine all-anchor original-witness LP is EXACTLY V_s=n(n-1)/[s(s-1)] with a perfect optimal owner balance lambda=1, but theta=2/n->0. r<=s-1 disjoint copies stay s-free and reduce theta to 2/(rn) while retaining perfect LP balance. Thus no density-free replacement of v1's false original-source transfer can be obtained simply from large, balanced cross-anchor LP certificates. At exponential cardinality |F|>D_s^k this obstruction is sparse and no density-to-link theorem has been proved. v2 remains SHIFTED only. This negative result is not a proof of the unrestricted conjecture, and literature novelty is NOT CHECKED.


## 15 October exact original point-link fractional LP cross-check

[FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md](FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md) proves a conditional-strategy barrier independent of shifting: an exact rational ORIGINAL-edge fractional matching / ACTUAL-point covering LP shows t(H54)=2/9, t(H39)=3/13, t(H153)=3/17. For every nonempty subfamily G of arbitrary tensor powers of each factor, the original point-link fraction satisfies theta(G)>=t(H); arbitrary correlated filtering cannot push it lower. The 360-edge rank-18 constant-composition example from a 3-free pair-star-plus-isolated factor shows that nonuniform entropy filtering *can* improve the point-link fraction of other factors and provides a mathematically genuine but weaker density lower control. This is not a new unrestricted upper bound and does not upgrade Mishra v2's shifted-family recurrence to ORIGINAL families. Full conjecture OPEN; source finite constructions prior art, programme LP priority unchecked.


## 15 October 2026 — NONVACUOUS high-density point-link impossibility (WR1–WR5, PROVED internally)

[Original pair-star wreath counterexample](NONVACUOUS_WREATH_POINT_LINK_OBSTRUCTION.md) is a genuine simple s-free ORIGINAL construction W_N,m(H) using N private tensor copies of any original s-free d-family H behind pair-star shell A_i. It has rank N-1+dm, size N|H|^m, theta=t=2/N and exact rational original fractional matching/physical-point cover nu*=N/2. For beta_s=sup_d f_s(d)^(1/d), EVERY threshold D<beta_s admits arbitrarily dense-above-D^k original witnesses with theta tending to zero and nu* unbounded; thresholds D>=beta_s are vacuous. Thus ALL previously proposed positive fixed point-link and bounded fractional-matching premises at **nonvacuous** density are FALSE, including the three explicit (5/2,1/5), (10/3,1/5), (21/4,1/6) proposals (integer-checked original witnesses). Previous conditional link-to-recurrence algebra is sound, but its required premise cannot hold. FL1 correlated-subfamily marginal rigidity on a shared tensor ground remains valid and is NOT contradicted. Efficient rank-(N-1) original multi-point packet extraction on this wreath survives; finding a NONCIRCULAR all-F packet recurrence is OPEN. Literature originality is NOT CHECKED, published H54/H39/H153 source factors remain PRIOR ART, and the full unrestricted sunflower conjecture remains OPEN.


## 15 October 2026 — multipoint packet depth and cross-packet intersection budget

The new [EXACT_WREATH_PACKET_KRAFT_OBSTRUCTION.md](EXACT_WREATH_PACKET_KRAFT_OBSTRUCTION.md) establishes an exact positive physical-anchor packet cost optimum for arbitrary private-tensor pair-star wreaths: for rank cap 1<=R<=N-1 and trial base C>1, min Z_C = min_j (j/C+(N-2j)/C^R), 0<=j<=floor(N/2). In the actual original construction, bounded R cannot give Z_C<=1 at arbitrarily high ranks even under ANY nonvacuous density restriction D<beta_s. Logarithmic rank R=ceil(log_C N) is necessary/sufficient asymptotically on wreaths; this does not imply an all-original fixed-base theorem. Without a rank cap, any genuine packet partition with Z_C<=1 has E[r]>=log_C(N/2) by the physical max-point degree and exact Gibbs entropy. Cross-group physical intersection coincidence of two independent pairs is exactly 2(N-1)/N^3 and tends to zero; unconditional positive collision-energy hopes fail. Source version verdict unchanged: Mishra v1 cumulative original transfer invalid and universal O_s(2^k) FALSE for s>=4; v2 shifted only. OPEN original unrestricted conjecture; PRIORITY NOT CHECKED.


## 15 October — adaptive ORIGINAL packet-depth nested-wreath audit

The exact multiscale physically-original argument in [NESTED_ORIGINAL_WREATH_PACKET_RECURSION.md](NESTED_ORIGINAL_WREATH_PACKET_RECURSION.md) does not use Mishra v1's invalid cumulative full-shift owner transfer or the shifted-only v2 conclusion. Its proved shell-only Kraft optimum for nested pair-star wreaths is V_1, with U_(t+1)=1, V_h=min_{0<=j<=floor(N_h/2)} [j/C+(N_h-2j) C^(-(N_h-1)) U_(h+1)], U_h=min(1,V_h). For C=2 and N_h>=3 all levels, the optimum is prod_h N_h/2^(N_h-1).

**Important negative logical control:** at s=4 and all N_h=3, a genuine original 4-free family of rank 3t, size 9^t, has a disjoint actual-shell anchored packet partition with total Z_2=(3/4)^t, while each rank-t residual is a q=3 product with 3^t>2^t original owners. The packet budget **does not** imply 2^k cardinality without an unavailable—and in this trial-base instance false—residual size hypothesis. Any putative original-compatible bridge must pay both the packet-label entropy and a noncircular actual-residual capacity or cross-packet s-way bonus. This is a proved barrier to the mechanism, not a counterexample to the full conjecture. PRIORITY NOT CHECKED; unrestricted theorem **OPEN**.


## 15 October addendum — no automatic original-owner transfer from physical packet Kraft budgets

[All-physical private-anchor theorem AP1–AP7](ALL_PHYSICAL_WREATH_COMPATIBILITY.md) removes the earlier shell-only caveat for nested wreaths with private q-ary product leaves: exact unrestricted anchored packet cost uses terminal min(1,(q/C)^m), while at C=2,q>=2 it remains prod N_h/2^(N_h-1). This is an ORIGINAL-sets theorem, not a shifted-image lift. Sharp conditional s-packet core defects and weighted fixed-core graph overlap use only true original pairwise intersections but yield NO rank-independent occupancy control. Mishra v1 remains invalid for cumulative shift sources; v2 remains restricted to shifted families. Full unrestricted conjecture OPEN. External mathematical priority NOT CHECKED.


## 16 October — original high-density fixed-core entropy/Turán barrier

[Exact genuine-original multi-packet theorem and sharpness](PHYSICAL_CORE_TURAN_HIGH_DENSITY_SHARPNESS.md): for r distinct owner packets and physical D, the D-equality intersection graph of any selected original tuple is K_s-free, hence sum delta_ij(D) >= binom(r,2)-ex(r,K_s). It is sharp for every m on (s-1) private shielded genuine-original tensor copies of any s-free seed H (rank dm+1+|D|). Their r=(s-1)|H|^m one-owner packet graph is the extremal complete (s-1)-partite Turán graph, and the weighted AP7 overlap inequality is likewise an equality 1/(s-1). For EVERY nonvacuous D_density<beta_s these saturating originals can exceed D_density^k exponentially. At s=3 with H54 and trial C=5/2, the q marker packets have Z_C=4/5 while each residue has (864/625)^m times the hypothesised capacity. This is a new obstruction to a strict fixed-core high-density bridge, not an unrestricted upper bound. Mishra v1's claimed universal base-2 transfer is false and its cumulative original-owner attribution invalid; v2 is SHIFTED-only. Full original conjecture OPEN, external priority NOT CHECKED.


## 16 October — actual cross-core coupling not a shifted-original transfer

[CC1–CC6](COUPLED_CROSS_CORE_NEAR_TURAN_OBSTRUCTION.md) give a positive nonlinear modal intersection-core inequality and exact Turan original physical support decomposition, but new s-free correlated-pairpoint witnesses have relative Turan deficit 1/n and J=4(n−1)/n² at exponential density while near-total original-owner exact purification requires deleting ≥(s−2)/(s−1) owners. Neither theorem pays for original residual capacity at a fixed C_s. v1 cumulative full-shift original ancestor step remains INVALID, and its universal O_s(2^k) conclusion FALSE for s≥4; v2 is SHIFTED-ONLY. Unrestricted original conjecture OPEN. EXTERNAL PRIORITY NOT CHECKED.


## 16 October — s=3 ORIGINAL physical core stability: no unearned inverse-shift lift

[CSM1–CSM6](ORIGINAL_CORE_STABILITY_MATCHING_CAPACITY.md) gives a proof-grade original-owner s=3 near-Turán decomposition: e(G_D)=r²/4-Delta>0 yields two physical D-containing independent neighbour packets missing at most 4Delta/r owners and at most 5Delta correct-D cross pairs, with an EXACT minimum matching-based deletion cost for exceptional cross intersections. Correlated original CC3 examples attain the neighbourhood leakage 4Delta/r and require losing half of actual original owners to exactify, despite relative Turán defect 1/n->0 and coupled cross-core J->0. The rank/noncircular residual inequality r<=4Delta/r+2i_3(k-|D|) still has no proven fixed-base closure and may have |D|=0. This is not a cumulative original-source shift lifting theorem: v1 remains INVALID at that step and its base-2 universal conclusion FALSE for s>=4; v2 remains SHIFTED-only. Full unrestricted conjecture **OPEN**; graph proofs classical, priority of programme packaging NOT CHECKED.
