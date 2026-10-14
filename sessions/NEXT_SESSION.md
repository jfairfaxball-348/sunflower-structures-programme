# NEXT DIRECT RESEARCH INVESTIGATION — ANCESTOR-COMPATIBLE RANK REDUCTION BEYOND THE SPOKE COUNTEREXAMPLE

Repository: https://github.com/jfairfaxball-348/sunflower-structures-programme
Primary versions: https://arxiv.org/html/2606.02667v1 and https://arxiv.org/html/2606.02667v2

## Mission and authoritative starting point

Find and prove a COMPLETE solution of the full Erdős–Rado Sunflower Conjecture for every fixed s>=3, with C_s independent of k and ground-set size, and ORIGINAL distinct sunflower petals (empty core allowed). This is a single-repository direct proof effort, not a child project, paper pipeline, session quota or background automation.

READ FIRST: research/SPOKE_SHIFT_THEOREM.md, research/WORKING_PROOF.md, research/VERSION_BRIDGE.md, authoritative/STATE.json.

**New PROVED session result:** For all q,k>=2 the sparse original spoke family
T(q,k)={ [k] } union { [k]\{l} union {l+ak}:1<=l<=k,1<=a<=q-1 }
is (q+1)-free of size (q-1)k+1, yet ONE lexicographic compression pass makes it EXACTLY the sunflower {[k-1] union {j}:k<=j<=qk}. The complete product P(q,k) ALSO acquires this permanent (q-1)k+1-sunflower. The proof handles already-present replacements without inventing ancestors. Therefore the rank-dependent hypothesis H_s: tau(SF)<=A_s*k/log(k+2) is FALSE for EVERY fixed s>=3, not merely computationally doubtful. STOP relying on it. This does not solve the full conjecture. Source v1's constant-times-2^k and universal full-shift source transfer are also invalid; v2 shifted recurrence is usable but lacks original witnesses.

## Principal proof attack — original witness or ancestor-compatible induction

A. **Design an original-family dichotomy with fixed per-rank cost.** Search for a rigorous large-family-only (density-sensitive) heavy-link versus dispersed-fibre theorem. Required output must either give an ORIGINAL s-sunflower or reduce k with |F|<=D_s*max |rank-(k-1) relevant ORIGINAL subfamily| plus an s-dependent exceptional bound whose accumulation stays <=C_s^k. Explore matching covers, fractional covers, shadows with sunflower-free extension limits, weighted fibres, degree spectrum, minimal cores, tensor tests, and multi-vertex conditioning. Specify the exact class, threshold, constants, and induction boundary. The k+1 pair-private 3-free family kills an unconditional constant-fraction link, but not a sufficiently-large-family theorem; P(s-1,k) forces C_s>=s-1.

B. **Find a compression inverse retaining origin compatibility, not tau alone.** A sunflower in shifted G can have mutually incompatible ancestors. Build a finite-rank certificate on labelled origin intersections, e.g. obstruction/conflict graphs on compressed petals or trace-fibre cliques, and prove quantitative guarantees. Demonstrate by explicit original-ancestor maps exactly how the k+1 newly produced spoke petals fail to lift. Any palette/label bound must tolerate linearly many incompatible petals in T(2,k). Investigate local partial shifts, bounded-width certificates, and high-density inverse selection; avoid full-shift tau transfer, which is now conclusively dead at k/log k.

C. **Try a genuine hybrid of (A) and (B).** One promising possibility is to restrict attention to families already larger than D_s^k before spending compression cost; sparse spokes should then be negligible but tensor products of spokes and P(q,k) may amplify the obstruction. Explicitly analyse T(q,k)^tensor m (disjoint product) and mixed product/spoke factors. Seek a lemma allowing rank reduction of a dense family while preserving the intersections of original petals. Also test two-star factor-2 sharpness and all pair-private configurations.

D. **Chase any positive result to the actual C_s^k target.** Do NOT stop at an informal lemma: derive the complete quantified recurrence, exact threshold and base cases k=1,2 and s=3; show no hidden n dependence, no collision of original ancestors, no loss of distinctness, and compatibility with (s-1)^k lower products. If a proposed bound fails, build a symbolic family counterexample and find the minimal missing condition. Explore multiple mathematically distinct approaches, not routine tuning of the rejected one.

## Recording and validation

Substantial investigation in this invocation; update research/WORKING_PROOF.md and research/VERSION_BRIDGE.md honestly, add independent proof/checkable tests for new falsifiers, keep authoritative/STATE.json accurate, and replace THIS NEXT_SESSION.md with a sharper direct continuation. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`; create and merge an ordinary PR after checks pass. All mathematical assertions are to be separately verified; CI tests cannot certify a full proof.

**No complete unrestricted proof currently exists in this repository. Do not claim otherwise.**
