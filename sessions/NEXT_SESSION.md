# NEXT DIRECT RESEARCH INVESTIGATION — CENTRAL-TRACE AMORTISATION AND AN ORIGINAL-FAMILY RANK RECURRENCE

Repository: https://github.com/jfairfaxball-348/sunflower-structures-programme

Owner invocation of this linked prompt authorises its execution immediately. Work in this same repository; no parent/child process, quotas, paper staging or hard stop.

## Governing problem and source audit

Prove the full Erdős–Rado Sunflower Conjecture for every fixed s>=3: some C_s independent of rank k and ground-set size makes every simple k-uniform family of cardinality >C_s^k contain s distinct ORIGINAL petals with identical pairwise intersections, possibly empty core. **NO complete proof has been obtained.** V2 https://arxiv.org/html/2606.02667v2 concerns SHIFTED families only; v1 https://arxiv.org/html/2606.02667v1 has an invalid cumulative original-source transfer, and its claimed O_s(2^k) universal conclusion is false for s>=4. Axante et al. 2026 https://arxiv.org/abs/2609.06175 provide PRIOR ART finite factors.

Read AGENTS.md, authoritative/STATE.json, research/WORKING_PROOF.md, research/VERSION_BRIDGE.md, research/SOURCE_REGISTER.md, research/ORIGINAL_MULTIWITNESS_TRACE_RANK_REDUCTION.md, research/TRIANGLE_TENSOR_PREVALENCE_OBSTRUCTION.md, research/SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md, research/HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md, scripts/triangle_tensor_prevalence_audit.py and tests/test_triangle_tensor_prevalence_audit.py. Verify LIVE main commit, commit tree, open PRs and CI, do not assume the handover is already executed.

## Starting theorem / no-go (15 October 2026)

For every finite s-free w-uniform Q of a>=2 edges with no common vertex, T=the 3 edges of a triangle and I_m=T tensor Q^m form pairwise-intersecting, empty-global-core, s-free original families with rank 2+wm and size 3a^m. For every anchor E and H>=1:

    |{B: |B intersect E|<=H}|/|I_m|
       <= Pr[Bin(m,1/a)<=floor((H-1)/w)].

Hence ANY union of compatible opposite traces with exchanged h<=H at one anchor is exponentially negligible for fixed H (even H=o(m)); any fixed-fraction covering by anchors needs exponentially many distinct anchors. Exact q-ary spectrum is 2 sum_(j<=H-1) binom(m,j)(q-1)^(m-j) + sum_(j<=H-2) ...; the classical 54 rank-four three-free factor improves the 3-petal tail to 2^(-m) sum_(j=0)^(H-1) binom(m,j) because two supports are disjoint and within a support edges intersect. These yield core-free barriers at all fixed D<54^(1/4),39^(1/3),153^(1/3) for s=3,4,6; not at their exact endpoints and not a full-conjecture obstruction.

Earlier multiwitness theorem A (PROVED LOCAL): with original E=T+V and r witness A_i=T+W_i, disjoint |V|=|W_i|=h, each exact opposite U subseteq V obeys |F(E,U)|<=h^r f_s(k-|U|-r). There is no theorem concentrating mass into such U. Even quantifying a positive anchor fraction only above an unspecified D can be logically equivalent to the full conjecture by an otherwise vacuous threshold.

## Attack tasks — substantive current mathematics, not plans

1. **Central-trace decomposition.** In triangle tensor and arbitrary s-free intersecting F, most members B have |B cap E|=Theta(k). Derive a nontrivial original-family compatibility lemma on these CENTRAL trace levels; test whether removing E cap B still forces rank descent and track exact (potentially exponential) multiplicity. Find a legitimate coefficient generating function, not a sum of 2^k unpriced errors. Include null common-core cases.

2. **Exponential anchors, bounded edge charges.** The previous obstruction requires exponentially many anchors for any h=o(k) cover, but does NOT exclude a family of exponentially many anchors with clever assignments. Formulate a rank-uniform fractionally weighted incidence/entropy charging theorem; either prove it with explicit constants or refute it by the exact triangle tensor q-product and H54 spectrum. Counts must be normalized so exponential anchor abundance does not secretly produce a rank-dependent induction cost.

3. **Noncircular density-sensitive lemma.** Quantify D,B,phi,H and compare with H54,H39,H153 and q-products. Demonstrate whether each hypothesis is independently provable or is vacuous above an unknown sunflower threshold. Seek a ground-set-independent theorem for original petals genuinely strong enough for f_s(k)<=C_s^k. Verify k=1 f_s(1)=s-1, i_s(1)=1; k=2 i_s(2)=max(s-1,3); rank-three known exact cases sourced, not invented.

4. **Global matching parameter paid once.** Use f_s(k)<=(s-1)k i_s(k), with matching support cost only at final stage, and seek induction on matching number or core-free decomposition. Do not assert deleting an arbitrary common point makes residues intersect; if all originals share a fixed x, removing x preserves their s-freeness but not necessarily intersecting property. Construct real counterexamples to false closure statements.

5. **Energy and exact trace polynomials.** For T tensor H54^m, Z_T(z)=(2z+z²)/3 and Z_H54(z)=(27+12z+10z²+4z³+z⁴)/54. For H153, use the proven (14210,7350,1696,153) ordered overlap profile divided by 23409. Calculate any proposed correlation/entropy contraction EXACTLY and use tensor multiplicativity to falsify false strict inequalities. Distinguish moment growth from mass transfer.

6. **Alternative bridge independent of shifting.** If central traces remain intractable, attempt structural extraction, random restrictions, containers, or an inverse-original certificate; prove a real theorem or construct a symbolic falsifier. Do not claim an induction from a conjecturally tiny extremal family or from shifted petals that have no certified original preimages.

## Closeout

Produce and test explicit lemmas/counterexamples; rigorously mark PROVED, CONDITIONAL, FALSE and OPEN. Persist a standalone note and finite independent tests to this SAME repo; update WORKING_PROOF.md, VERSION_BRIDGE.md, SOURCE_REGISTER.md, authoritative/STATE.json and replace this NEXT_SESSION.md. Run python3 scripts/validate.py and python3 -m unittest discover -s tests -v locally if available; otherwise report local network restriction, require genuinely successful GitHub Actions job covering BOTH commands, and merge ONE normal PR only after matching green exact-head CI. Check merged main and distinct push workflow afterwards where available. CI does not certify universal mathematics. End with exact mathematical verdict, truthful PR/commit links and FULL next prompt. No arXiv, author outreach or public solved claim without new owner authorisation.
