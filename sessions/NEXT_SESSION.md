# NEXT DIRECT RESEARCH INVESTIGATION — BUILD THE MISHRA v2 → UNRESTRICTED BRIDGE: RANK-DEPENDENT OBSTRUCTION

Repository: https://github.com/jfairfaxball-348/sunflower-structures-programme
Primary sources: https://arxiv.org/html/2606.02667v1 and https://arxiv.org/html/2606.02667v2

## Governing mission

Prove the full Erdős–Rado Sunflower Conjecture: for every s>=3 a C_s independent of k,n exists such that every simple k-uniform family with >C_s^k ORIGINAL members contains s distinct original sets with equal pairwise intersections. Empty core allowed. Single repository, no child projects, paper pipeline, staged audits, hard stops, or premature proof claims. Pursue rigorous mathematics intensively in this invocation, then update and commit genuine results.

## Established knowledge to USE (read research/WORKING_PROOF.md and research/VERSION_BRIDGE.md)

1. The v2 shifted-only rank recurrence, shadow inequality, small-rank bound, and single-shift factor 2 are now independently proved in the notebook. The single-shift factor 2 is exactly tight (two disjoint stars). V1's full-shift single-original-source argument is invalid, and its constant_s*2^k conclusion is outright false for s>=4 by P(s-1,k).
2. New no-go: for ANY ordering, every globally shifted ORIGINAL subfamily of P(q,k) has at most q members, despite |P|=q^k. So 'find a large shifted subfamily of the original' is not a free transfer.
3. New elementary countercontrol: k+1 rank-k sets indexed by unordered pairs e_ij are 3-free, all points of degree 2. Thus no unconditional constant-fraction original link reduction.
4. Valid positive bounded-support lift: if compression/transport preserves outside U, tau(G)<=2^|U|tau(F). A successful route must make its trace alphabet small enough or exploit compatibility beyond this crude factor.
5. For q>=3, full shifting P(q,k) necessarily raises tau to Omega_q(k/log k) by the independently proved v2 bound. Moreover, CONDITIONAL on tau(SF)<=A_s k/log(k+2) for every s-free original F, one obtains a rigorous C_s^k bound; see exact constant in notebook. This conditional premise is UNPROVED. Finite P(2,k) full shifts for k=2..8 contain k+1-star witnesses, suggesting the naive premise is FALSE. Finite experiments are not universal proofs.

## Primary concrete investigation: DECIDE THE RANK-DEPENDENT BRIDGE

A. **Exact full shift of products.** Symbolically analyse S(P(2,k)) with the specific order of the 2k ground vertices and lex i<j compressions. Determine rigorously whether it contains all {1,...,k-1} union {j}, k<=j<=2k, for every k. This is seen computationally through k=8 but MUST be proved or falsified for general k. Check s=3 and products P(q,k), q>=3. If the k+1 sunflower is universal, formally KILL the tau=O_s(k/log k) premise. Track possible alternate shift sequences and trace labels.

B. **Construct genuinely adequate transfer.** If simple tau transfer is dead, seek a different ORIGINAL-ancestor invariant: core-compatible colourings, origin intersection-pattern hypergraphs, collision budgets, low-complexity fibre partitions, partial shifts, or a density-driven dichotomy. State complete quantifiers and show for every fixed s exactly how an n- and k-independent base C_s follows. Test all candidates against q-ary products (for all k), pair-private incidences, two-star sharpness and shifted-star creation. Avoid rebuilding a false universal g(tau).

C. **Independent original-family rank reduction.** Seek a sharp large-family-only theorem distinguishing high-concentration links from sufficiently spread original families, where every outcome reduces k or yields an ORIGINAL s-sunflower with per-rank cost O_s(1). The k+1 pair-private family rules out unconditional half-link; product forces any viable theorem to allow (s-1)^k growth. Test shadows, matching covers, tensor products, heavy hubs and structured fibres. No 'induction works' claim without the full quantified recurrence.

D. **Try the full proof now.** For any genuine bridge, chase induction all the way to a C_s, check distinct original members, empty core, rank k=1, s=3, loss of n, and threshold conventions. Prove or refute new subclaims rather than citing source authority. If full closure fails, leave exactly the strongest theorem or falsifier and the narrowest quantitative missing lemma.

## Repository and validation

Update research/WORKING_PROOF.md and research/VERSION_BRIDGE.md, add checkable symbolic or computational tests where useful, correct authoritative/STATE.json only for proved status, and REPLACE sessions/NEXT_SESSION.md with the resulting next direct proof attack. Run python3 scripts/validate.py and python3 -m unittest discover -s tests -v, create and merge an ordinary GitHub PR after checks pass. Do not confuse CI with verification of open mathematics.

**NO full proof currently exists in this repo. The next investigation's purpose is to change that with rigor, not with claims.** Full Erdős–Rado mission is the sole target. P(s-1,k) precludes an impossible FULL-shift fixed-base-2 conclusion.
