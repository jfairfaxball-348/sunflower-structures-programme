# NEXT DIRECT RESEARCH INVESTIGATION — ORIGINAL INTERSECTING FAMILIES AND WITNESS-COMPATIBLE RANK REDUCTION

Repository: https://github.com/jfairfaxball-348/sunflower-structures-programme
Primary sources: https://arxiv.org/html/2606.02667v1 and https://arxiv.org/html/2606.02667v2
Recent finite-factor prior art: https://arxiv.org/pdf/2609.06175 (Axante et al., September 2026)

## Governing objective

Prove the full Erdős–Rado Sunflower Conjecture: for each fixed s>=3 find C_s independent of k and ground-set size such that an original simple k-uniform family with more than C_s^k members has s distinct ORIGINAL sunflower petals, including empty core. No parent/child workflow or artificial stop. Conduct substantial new mathematics, independently and adversarially. **NO complete proof has been obtained.**

## Read first / verified starting point

1. research/SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md, especially inequality f_s(k) <= (s-1) k i_s(k), exact trace INCLUDING empty T, six-petal 153-factor proof and nine one-swap directions, and star-restricted intersecting tensor theorem.
2. research/HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md, research/DENSE_ANCESTOR_OBSTRUCTION.md and research/SPOKE_SHIFT_THEOREM.md.
3. research/WORKING_PROOF.md, research/VERSION_BRIDGE.md, research/SOURCE_REGISTER.md, authoritative/STATE.json and AGENTS.md.
4. scripts/six_petal_factor_audit.py, tests/test_six_petal_factor_audit.py and scripts/validate.py.

PROVED: for every k and fixed s, the maximal s-free k-family size f_s(k) is between i_s(k) and (s-1)k i_s(k), where i_s counts INTERSECTING original families. The two functions have the same exponential growth rate. This reduction is elementary, NOT itself a fixed-base bound; claiming an unknown i_s(k)<=A_s^k is exactly as difficult as the conjecture without independent proof.

PROVED: published six-petal-free factor P has 153 rank-three edges, tau(P)=5, nine outsider swaps for B={0,1,10}. Its rank K=3m tensor has 153^m originals and lex shifted tau>=9m+1=3K+1. Thus false density-restricted O_s(K/log K) shifting transfer persists through D<=153^(1/3) for s=6 (previous graph floor sqrt27). Also PROVED for ANY anchored factor, fixing the first coordinate to one original vertex link produces INTERSECTING originals of size (d/h)h^m, with lexshift tau>=r(m-1)+1. Consequently intersecting restriction alone cannot rescue that transfer at D strictly below factor base (54^(1/4),39^(1/3),153^(1/3) for s=3,4,6). The source constructions are prior art. For s=3 the 54 tensor exactly saturates the shadow incidence inequality; do not generalise its equality to s=6.

## Direct research tasks — attack the central proof gap

A. **Original intersecting sunflower theorem, not shifted version.** Start with an arbitrary pairwise-intersecting original s-free k-uniform F. Seek a noncircular n-independent fixed-base size bound |F|<=A_s^k directly, perhaps by controlled cores, a matching-constrained energy inequality, fractional vertex covers, or multi-links. PROVE an explicit useful structural lemma with constants and test against star-restricted 54/39/153 tensors, pair-private constructions, and q-ary products. Do not merely assume the exponential bound: it is equivalent to the full conjecture.

B. **Canonical witness-preserving decomposition.** For maximal matching support U of <=(s-1)k points, we can partition into at most (s-1)k INTERSECTING original subfamilies (loss polynomial once, not per rank). Explore whether a compatible per-rank recurrence can be proved INSIDE intersecting families without reintroducing k at each rank. A forced one-point core does NOT imply its residue link is intersecting. Inspect this exact failure and repair it or prove a symbolic obstruction.

C. **Complete original exact traces.** For E in F and EVERY proper T subset E, INCLUDING empty T, the residues {A\T: A∩E=T} have matching number <=s-2. The empty-T class retains full rank; this is the difficulty. Develop genuine CROSS-T compatibility inequalities and an original rank reduction with O_s(1) coefficient plus demonstrably absorbable error. Calculate constants at k=1,2,3 and provide a valid induction; do not hide an unknown conjecture-level threshold.

D. **Test nontrivial probabilistic/entropy or link-moment certificates.** The 54 tensor has exactly maximum shadow codegree2 at every shadow; the 153 factor has histogram (1:27,4:8,5:80) and d_max/|P|=3/17. Quantify any new independent invariant and its tensor behaviour. Explicitly disprove proposed mass-transfer inequalities that secretly require positive shadow slack or O(1) sunflower-lifting colours.

E. **Survey sharper six-/five-/higher-petal factors only if they materially affect the target.** Existing published f(3,6)>=153 and f(3,7)>=259 come from different certified constructions; never assume the 259 factor beats rank-two at s=7 without comparing bases and exhibiting ORIGINAL adjacent edges. If a superior factor is found, prove its sunflower freeness, anchors and all-rank tensor consequence. No claim that published finite examples are novel.

F. **Complete and audit if a proof survives.** State explicit C_s with no k/n dependence, prove the bound at all small ranks and genuine extraction of s distinct original petals with one exact core. Check C_3>=54^(1/4), C_4>=39^(1/3), C_6>=153^(1/3) as currently known lower floors; also P(s-1,k) for all s. Do not treat the v2 shifted theorem as unrestricted.

## Required closeout

Do substantial mathematical work in this invocation, not just planning. Preserve PROVED/FALSE/CONDITIONAL and source attribution. Extend standalone research notes, WORKING_PROOF.md, VERSION_BRIDGE.md, SOURCE_REGISTER.md, authoritative/STATE.json, executable tests and this prompt as warranted. Run python3 scripts/validate.py and python3 -m unittest discover -s tests -v (locally or report exact tool restriction and obtain passing GitHub CI); use one normal PR and merge only on green checks. End with mathematical verdict, verified commit/PR links and FULL next research prompt. CI verifies finite diagnostics, not an unrestricted theorem.

A full-shift sunflower-number transfer with no original-witness compatibility is disproved by these examples.
