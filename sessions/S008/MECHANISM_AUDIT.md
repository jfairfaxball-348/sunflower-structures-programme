# SUN-PARENT-S008 — one-mechanism hostile audit and binary STOP
2026-10-14. Parent-only session. **Outcome: STOP_NO_ACTIVE_CHILD.** This is a falsification of an attempted sufficient structural principle, **not** an original theorem or improvement of Erdős–Rado.

## Scope, source baseline, and novelty bar
For each integer r≥3 and k≥2 let f(k,r) be the maximum size of a *simple* k-uniform family without r **distinct** sets having *every pairwise intersection equal as a set* (the common kernel, possibly empty). Permanent conjecture: ∀ fixed r≥3 ∃ constant C_r independent of k such that f(k,r)≤C_r^k for every k. Best general source baseline is `(Cr log k)^k` (Bell–Chueluecha–Warnke). The fixed VC≤d base `(50dr)^k` already occurs in Ge–Wang–Xu–Zhao arXiv:2609.18995, 2026 preprint; its use of spread links, squared marginals, entropy and matching means that raw collision-energy extraction is **not itself an original method**. ECCC TR26-220 already has O(w)-wise robust derandomisation. Source-proved statements are their work; this same-assistant elementary audit is not a priority certificate. [Primary source register](../../programme/S008_SOURCE_REGISTER.md).

## Exactly one proposed noncircular mechanism L: FULL-LINK COLLISION DROPOFF
Let F be a finite, simple k-uniform family and let C be any subset of its ground set. Its *full original-family link* is F_C={A∈F:C⊆A}. When F_C≠∅, define
`p_C(v)=|{A∈F_C:v∈A}|/|F_C|` for every vertex v outside C, and
`Q(F,C)=Σ_{v∉C}p_C(v)^2`. All quantifiers concern finite objects; no ad hoc selection H or assumed sunflower is hidden inside Q.

**Proposed L(r,k), now FALSE:** For all integers r≥3,k≥2 and every such F with `|F|≥(r−1)^k` and `VC(F)≥k−1`, there exists `C⊆∪F` with `0≤|C|<k`, `|F_C|≥r`, and `Q(F,C)<1/binom(r,2)=2/[r(r−1)]`.

This was investigated as a high-VC *full-link second-moment regularisation* claim, not as the tautology “a sufficiently large F contains a sunflower”: Q is computed on the **entire** original link F_C without being allowed to select r sunflower witnesses or replace Q by the desired conclusion. The highly aggressive threshold was chosen for falsifiable quantitative strength rather than being declared attainable or novel.

### Exact theorem implication, conditional on L
Draw A_1,...,A_r independently and uniformly from the *whole* F_C. For any i≠j,
`P[(A_i\C)∩(A_j\C)≠∅]≤Σ_{v∉C}p_C(v)^2=Q(F,C)`,
by union bound, even accounting for repeats. Summing over all binom(r,2) pairs gives a failure probability strictly <1. Thus there exist r pairwise disjoint nonempty petals A_i\C, necessarily distinct A_i in **the original F**, with each pair intersection exactly C. If L held, it would imply
`f_{VC≥k−1}(k,r)<(r−1)^k` (subject to integer ceilings), an unusually sharp all-rank high-VC theorem independent of P001A/B/C. It would **NOT** imply the full unrestricted Erdős–Rado bound without additional control of VC<k−1 families; no such transfer is supplied. Conditional strength ≠ verified result, publishability, or novelty.

### Adversarial falsifier: q-ary product P(q,k), q=r−1
Let ground set X=[k]×[q] (q=r−1≥2). Define
`F=P(q,k)={A_x={(i,x_i):i∈[k]}:x∈[q]^k}`.
- **Simple k-uniform; size exactly q^k=(r−1)^k.**
- **VC=k**: fix T={(i,1):i∈[k]}; choose x_i=1 for a trace present and any other symbol for absent. No k-uniform family shatters k+1 points.
- **No r-sunflower**: in each coordinate block, r symbols among only q=r−1 choices have equal pairwise intersections only if all r symbols are equal (distinct r symbols cannot fit in q). All blocks would be equal, so all r members identical, forbidden.

Take ANY proposed C with F_C nonempty. It can contain at most one symbol from each coordinate block; write t=|C|. For each of the k−t unpinned coordinates, F_C uniformly exhibits all q symbols, with p_C((i,b))=1/q for all b. Hence **exactly**
`Q(F,C)=(k−t)q(1/q²)=(k−t)/(r−1)`.
If |F_C|≥r, then `q^(k−t)≥r>q`, so k−t≥2 and therefore
`Q(F,C)≥2/(r−1)>2/[r(r−1)]=1/binom(r,2)` for every r≥3. If F_C is empty or |F_C|<r, C already fails another L condition. Thus every permissible C fails, **for every r≥3 and k≥2**, including the binary B_k=P(2,k) at r=3. No unspecified asymptotic constants, hidden H, or external computation are needed.

Even with an arbitrary probability distribution μ on any F_C subfamily, the per-block Cauchy–Schwarz bound Σ_{b=1}^q μ(i,b)^2≥1/q yields `Q_μ≥(k−t)/q`. This stronger check shows that reweighting alone cannot repair the collision claim on product blocks.

### Distinct P001A-type high-hub original-mass countercontrol
Cone the q-ary product by a common hub h:
`F_h={ {h}∪A_x:x∈[q]^(k−1) }`, a *k*-uniform, VC=k−1, r-free original family with `q^(k−1)` edges. This DOES NOT meet L's size premise q^k and is **not** advertised as a second counterexample to the exact L. Rather, it tests its promised mechanism against the P001A-type heavy-vertex control. For any C with |(F_h)_C|≥r:
- If h∉C, its marginal p_C(h)=1, so Q(F_h,C)≥1>1/binom(r,2).
- If h∈C, the remaining q-ary product block coordinates have residual collision energy (k−|C|)/q, and ≥2 free blocks are necessary for r choices, hence Q≥2/q>1/binom(r,2).
Thus no collision-energy slice is rescued by fixing or ignoring the original heavy hub. The precise P001A S051 high-richness/overlap controls are separate and remain unsolved; this cone does not purport to reproduce their full five-certificate problem. On the original mass, all q^(k−1) edges retain h until it is pinned.

### Finite reproducibility and hostile scope check
The exact counting, VC witness, distinctness, conditional-link moment and no-r-sunflower arguments above are symbolic for **all** r,k, not a finite extrapolation. Local explicit fraction checks for r=3,4,5,6 at k=3 gave Q on a one-coordinate link respectively 1, 2/3, 1/2, 2/5 vs thresholds 1/3,1/6,1/10,1/15. Automated bounded enumerations are included in `tests/test_programme.py`. The lower bound is an elementary product consequence, NOT novel. Only the specifically quantified L is falsified; it does not refute the Erdős–Rado conjecture, every second-moment strategy, nor the true sourced bounded-VC theorem.

## Hard-stop verdict
**(b) STOP_NO_ACTIVE_CHILD**. L is false on all-r q-ary product families at its stated sharp threshold; its collision method materially overlaps the Ge et al. sourced second-moment/spread architecture and has no surviving novelty or quantitative unrestricted-rank transfer. There is no independent lemma, proposed new child theorem, kill-gate launch, new repository request, new global inequality, first paper, proof/formal verification, or priority clearance. P001A remains retired at S051 (no S052), P001B paused at S003 (no S004), P001C paused at S002 (no S003). Preserve the existing restriction that every possible future claim requires genuine independent proof and targeted original source checking, not no-hit searches.

**Sources:** [Ge et al. arXiv:2609.18995](https://arxiv.org/abs/2609.18995); [BCW Note on Sunflowers](https://arxiv.org/abs/2009.09327); [ECCC TR26-220](https://eccc.weizmann.ac.il/report/2026/220/); [S007 primary register](../../programme/S007_SOURCE_REGISTER.md); [P001A asset review](../../programme/P001A_MATHEMATICAL_ASSET_REVIEW.md); [P001A S051 source proof](https://github.com/jfairfaxball-348/sunflower-internal-kernel-extraction/blob/c7ede2676909f335ea2bb9f247d5a0e2abdff12c/research/S051_RICH_LINK_STRESS_AND_SHARP_PARTITE.md).
