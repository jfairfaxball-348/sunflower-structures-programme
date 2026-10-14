# Erdős–Rado Sunflower Conjecture — Mishra v1/v2 bridge research

**Single research programme. One goal: prove the unrestricted conjecture.** This established repository now investigates the precise mathematical gap between Tapas Kumar Mishra's *Erdős Rado Sunflower (Conjecture) Theorem* **v1** (1 June 2026) and *Erdős Rado Sunflower Theorem for Shifted Families* **v2** (8 June 2026), plus any independent approach needed to overcome that gap.

For each fixed integer s>=3 we seek a constant C_s independent of k such that every finite family of k-element sets with more than C_s^k distinct members contains s distinct sets with identical pairwise intersections (empty core allowed). **No proof of this full conjecture is currently claimed by this repository.**

**Strongest quantified obstruction at s=3,4:** [higher-rank published factors with original-witness tensorization](research/HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md) show dense s-free original families whose lex shifts have linearly many sunflower petals through exponential density bases 54^(1/4) (s=3) and 39^(1/3) (s=4); for s=3 the standard shadow inequality is exactly saturated. These finite factors are prior art and no unrestricted upper bound is proved.

**Earlier proved obstruction:** [universal spoke-to-star compression theorem](research/SPOKE_SHIFT_THEOREM.md) shows that lexicographic full shifting inflates the sunflower number from q to (q-1)k+1 on explicit q-ary product examples (and even sparse subfamilies), thereby refuting the suggested O_s(k/log k) sunflower-number transfer for every s>=3. **The full conjecture remains open.**

**Read first:** [Exact version comparison and obstructions](research/VERSION_BRIDGE.md) · [Sources](research/SOURCE_REGISTER.md) · [Working proof and open directions](research/WORKING_PROOF.md) · [NEXT DIRECT RESEARCH PROMPT](sessions/NEXT_SESSION.md).

## Why the gap matters

- [Mishra v1 (1 June 2026)](https://arxiv.org/html/2606.02667v1) claimed an unrestricted bound by showing a quantitative bound on the maximum sunflower after full shifting, then applying a shifted-family theorem. The exact claimed `(3s^2)^(6s^2-2) * 2^k` universal bound is mathematically impossible for s>=4, since explicit s-sunflower-free families have (s-1)^k members.
- [Mishra v2 (8 June 2026)](https://arxiv.org/html/2606.02667v2) confines its main result to *shifted families*, with a recurrence for the shifted extremal function. It no longer claims the unrestricted solution. All source proofs remain subject to auditing.
- Compression need not preserve sunflower-freeness: `{{2,3},{1,4},{1,5}}` has no 3-sunflower but its (1,2)-shift `{{1,3},{1,4},{1,5}}` does. A transfer theorem therefore needs stronger ideas than naive shifting.

**Primary open problem:** find a mathematically valid route from the special structure of shifted families to the full arbitrary-family bound with a base C_s >= s-1 allowed to depend on s but NOT on k or the ground-set size.

## Working policy

Explore original mathematics relentlessly within each invoked research task, including repaired shifts, witness-lifting, structured subfamilies, inverse compression, encoding, shadows and other independent techniques. Falsify overstrong lemmas quickly; keep counterexamples. No parent/child folders or stage gates; the single repository is the research notebook. Old `programme/`, `papers/`, `tournament/` and historical `sessions/S*/` are archival evidence only, not binding instructions. There is **no longer any STOP_NO_ACTIVE_CHILD or S011 restriction**.

GitHub Actions checks repository consistency and exact counterexamples, not novelty or a proof of the conjecture. We will not declare success without a complete proof and independent scrutiny.


**Further proved bridge diagnostics (14 October):** [six-petal 153-tensor and intersecting-original obstruction](research/SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md). The published 153-edge six-petal-free rank-three factor gives shifted stars of >=3k+1 petals at k divisible by three (base 153^(1/3)). Fixing one coordinate to a vertex-star shows density-restricted full-shift sunflower-number transfer also fails on **intersecting original** s-free families at all fixed densities strictly below the known factor bases for s=3,4,6. Separately every s-free family has an intersecting original subfamily of size at least |F|/((s-1)k), so the intersecting and unrestricted problems have equal exponential growth rates. This is an equivalent unsolved formulation, **not** a completed proof.
