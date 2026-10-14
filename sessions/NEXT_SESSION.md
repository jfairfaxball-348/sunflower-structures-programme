# NEXT DIRECT RESEARCH INVESTIGATION — ORIGINAL-WITNESS RANK REDUCTION ABOVE THE DENSE TENSOR BARRIER

Repository: https://github.com/jfairfaxball-348/sunflower-structures-programme
Sources: https://arxiv.org/html/2606.02667v1 and https://arxiv.org/html/2606.02667v2

## Mission (unchanged)

Prove the **full Erdős–Rado Sunflower Conjecture**: for each fixed s>=3, a constant C_s independent of k and the ground-set size exists so that any simple original k-family with more than C_s^k members contains s DISTINCT ORIGINAL petals of identical pairwise intersection, empty core allowed. Continue vigorous direct mathematical research in this ONE repository; legacy parent/child hierarchy, paper pipeline, session quotas and hard stops remain retired. Do not claim a proof while the original-family gap persists.

## READ FIRST — authoritative live results

- research/DENSE_ANCESTOR_OBSTRUCTION.md
- research/SPOKE_SHIFT_THEOREM.md
- research/WORKING_PROOF.md
- research/VERSION_BRIDGE.md
- authoritative/STATE.json and research/SOURCE_REGISTER.md
- scripts/dense_obstruction_audit.py and tests/test_dense_obstruction_audit.py

**New PROVED no-go:** Let q=s-1 and let
M_q=q(q+1) for even q and M_q=q^2+(q-1)/2 for odd q; b_q=sqrt(M_q)>q. There exist original (q+1)-free families F_(q,m) of rank K=2m with |F|=b_q^K and tau(F)=q such that lex shifted G has tau(G)>=m(q-1)+1 (even q) or 2m(q-1)+1 (odd q). It follows that any attempt to resurrect tau(G)<=A_s*K/log(K+2) merely by restricting original size to >=D^K is FALSE for every D<=b_q. This extends the q-ary product (s-1)^k obstruction to a **larger exponential density**. The partial-spoke lemma applies even with arbitrarily many extra original edges and fully handles collisions; its lower-bound star need not keep identical last-vertex labels after later shifts. Rank-two constructions overlap known extremal-graph prior art; do not advertise them as literature novelty. NO complete proof exists in the repository.

## Principal research programme — attack the missing ORIGINAL link

1. **Quantified density-sensitive original dichotomy.** Seek a theorem for any fixed s and threshold D_s>b_(s-1) (or a genuinely different invariant): every sufficiently large s-free original k-family either has an s-sunflower or admits a rank-(k-1) original link/restriction/extraction whose loss is bounded by a fixed number B_s independent of k,n. State a precise inequality, e.g. |F| <= B_s max_{x} |L_x| + E_s(k), and prove that any E_s(k) can be absorbed into a C_s^k induction with explicit k=1,2 and s=3 boundaries. Watch for circularity: a size condition that is itself stronger than the target is not a proof.

2. **Falsify naive fibre, shadow and matching claims first.** Apply proposed lemmas to: binary double triangles H_2 and tensor powers (base sqrt(6)); odd-q double-star/circulant H_q; even-q two-clique tensors; T(q,k); P(q,k); pair-private (k+1)-family; the sharp two-star one-compression example. For every candidate compute the exact original max degree, shadows, links and tensor scaling. In particular any threshold <=b_q is already below valid dense counterexamples for shift inflation. Look for a *new adversarial original family* with a larger exponential density before assuming success.

3. **Ancestor-compatible full-shift inverse with genuinely useful colour cost.** A final compressed star from H_q tensor m has Omega_s(K) petals but original sunflower number q; any partition into classes that each lift to an original sunflower takes Omega_s(K) classes. Invent an alternative certificate that tracks source intersections, uses density to find s compatible original petals, and avoids superexponential loss. State and audit the exact inverse mapping; no unique-source or sunflower-number-only transfer.

4. **New distinct approach not solely full compression.** Explore minimal cores, weighted deletion, randomized restrictions on original families, entropy/measure bounds, fractional hitting sets, nonuniform trace lemmas and multi-vertex conditioning. Prove a meaningful rank-reducing step or construct a fully symbolic counterexample. Do not spend the session merely optimizing the already-false H_s.

5. **Derive the actual target when a candidate survives.** Show all constants and recursion steps, no n dependence, exact original distinctness and empty-core coverage. Check consistency with both P(s-1,k) of size (s-1)^k and dense factor tensor powers of size b_(s-1)^k (even ranks). A claimed C_s must be at least b_(s-1) unless a larger original lower family is found.

## Session deliverables

Conduct substantial mathematical attempts NOW, not just a plan. Preserve proved/falsified/conditional distinctions; make explicit symbolic counterexamples where necessary. Update research/WORKING_PROOF.md, research/VERSION_BRIDGE.md, authoritative/STATE.json, relevant executable diagnostics, and replace this file with the strongest DIRECT next-session prompt. Run python3 scripts/validate.py and python3 -m unittest discover -s tests -v; open and merge an ordinary GitHub PR after checks succeed. Always output closeout, mathematical verdict, commit/PR link, and the newly queued next prompt. GitHub CI is evidence about code integrity, not a certificate of a general mathematical proof.
