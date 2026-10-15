# Cross-trace tensor shielding, two-axis residue structure, and VC barrier (15 October 2026)

**Verdict:** PROVED a fixed-rank trace-sunflower classification, an exact two-axis original trace/residue incidence decomposition, an all-s explicit counterexample in which exponentially large trace packets have NO compatible original sunflower and the incompatibility has a ONE-vertex certificate, and a quantified lower bound on VC dimension of large binary-product subfamilies. **OPEN:** an actual noncircular original-family C_s^k upper bound. These elementary deductions have NOT been priority-checked against the literature; do not announce novelty or a solution.

Let s>=3, F a finite simple original k-uniform s-sunflower-free family, E an actual original anchor, F_T={A:A cap E=T}, R_T={A setminus E:A in F_T}. Here "sunflower" ALWAYS means s distinct ORIGINAL edges with equal pairwise intersections, empty core allowed.

## TS1. Exact fixed-rank trace dichotomy (PROVED)

Choose s distinct original A_i all with |A_i cap E|=r, and write T_i=A_i cap E and B_i=A_i setminus E. If the A_i form an s-sunflower, then **either** all T_i are identical **or** all s traces are distinct and themselves form an s-sunflower. Indeed, the T_i have pairwise constant intersections. If T_a=T_b=T, their pairwise intersection is T. Every T_i must contain T; all have the same cardinality r, so all equal T. Otherwise all are distinct. Moreover, the lifts form a sunflower if and only if BOTH the traces (T_i) and residues (B_i) have constant pairwise intersections (with a common trace allowed in the first alternative). Their cores lie on disjoint sides of E, so this equivalence is exact. Conversely distinct sunflower traces plus equal residue pairwise intersections yield s distinct ORIGINAL sunflower petals.

Caution: the dichotomy about **repeated traces** requires equal trace cardinalities. Do not apply it across mixed-rank trace layers. For s>=4, distinct traces may have proper residue matching number s-2; never call them intersecting.

## TS2. Two-axis original incidence rows (PROVED)

Represent each original edge uniquely by (T,B)=(A cap E,A setminus E). For a fixed actual outside residue B, define G_B={T subset E:T union B in F}; all members have size k-|B|. If F is s-free, then G_B is s-free: s distinct sunflower traces together with the same B would lift to s distinct original petals with outside core B. Thus both every nonempty *column* R_T and every nonempty *row* G_B is an original s-free family. For each B,
 
    |G_B| <= min{ f_s(k-|B|), binom(k,k-|B|) }.                  (TS2)

This is a genuine simultaneous constraint, but the number of possible B on the unrestricted outside ground set is unbounded. Summing TS2 is not a rank recurrence, and using an unproved f_s bound is circular. It complements the earlier exact packet/entropy identity PL1 rather than replacing its trace entropy charge.

A necessary cross-column condition: for each s DISTINCT sunflower traces T_1,...,T_s, the residue intersection R_T1 cap ... cap R_Ts must be empty; more generally no choice B_i in R_Ti can have equal pairwise intersections. The previous PM1/CT2 inequalities already encode the weaker quantitative partial-occupancy collisions. We do NOT relabel those older inequalities as new.

## TS3. Universal s+1-edge original shield (PROVED)

For every s>=3 take disjoint symbols e_1,...,e_s, h_1,...,h_(s-2), z_1,...,z_(s-1). Put E={e_1,...,e_s}, H={h_1,...,h_(s-2)}, and

    A_i={e_i} union H union {z_i}      (1<=i<=s-1),
    A_s={e_s} union H union {z_1}.

All s+1 ORIGINAL edges have rank s and are distinct. The s traces A_i cap E={e_i} form a genuine core-empty s-sunflower of distinct traces. Nevertheless the A_i are NOT a sunflower: A_1 cap A_s=H union {z_1}, whereas A_1 cap A_2=H (for s>=3). F_s={E,A_1,...,A_s} is s-free: an s-tuple including E and at least two A_i has unequal intersections with E; the only s-tuple not including E is all A_i, already ruled out. The full s-tuple A_1,...,A_s has EXACTLY ONE vertex of partial multiplicity 2,...,s-1, namely z_1 (which occurs twice); all h_j occur s times, every other z_j occurs once. Thus the PM1 defect lower bound is SHARP even for all s.

This is a small, concrete FALSE-LIFT example; it does not by itself disprove any theorem asserted only above a high exponential density.

## TS4. Arbitrarily many exponentially large packets, but one permanent defect (PROVED)

Let Q be ANY nonempty s-free simple d-uniform family, with actual anchor D in Q and a nonempty residue packet R_U of cardinality a>=2 (U subset D). Form the disjoint-ground tensor product F_s tensor Q^m and anchor E tensor D^m. In each of its s exact packets indexed by T_i={e_i} union U^m, the ORIGINAL residue family has exactly a^m members and rank (s-1)+m(d-|U|); the common trace cardinality is 1+m|U|, so the T_i themselves form an s-sunflower with core U^m. **No selection** of one original edge from each packet can form a sunflower: all seed A_i projections remain fixed and already violate the equal-pairwise-intersection requirement in the seed block. Yet select the SAME auxiliary residue in all s packets: then the entire original s-tuple has exactly ONE partial-multiplicity vertex, z_1, independent of m. All auxiliary outside points occur either zero or s times. This is an exact one-vertex tensor shield with s packet sizes all a^m and product a^(ms).

Freeness of the complete tensor family is rigorous: in an s-sunflower of distinct product edges, at every factor coordinate the s uniform projections are either all identical or all distinct and form an s-sunflower. A repeated-but-not-all-equal projection is impossible: equality of the pair intersection for two equal uniform projections forces all projections to equal it. As every factor is s-free, all projections would be identical, contradicting global distinctness. This argument includes empty cores and all equality cases.

**Explicit dense s=3 auxiliary.** Let Q9={(x,y,x^2+y^2 mod 3):x,y in F_3}, with tagged coordinate vertices, rank 3, nine original edges, and no 3-sunflower (classical cap). At D=(0,0,0), EXACTLY four edges have empty trace. Thus for every m>=1, F_3 tensor Q9^m is 3-free, rank 3+3m, size 4*9^m, and has three distinct sunflower traces with an empty auxiliary core and **4^m residues in EACH packet**, yet ZERO compatible rainbow original triples and a selection with exactly one permanent defect. For s>=4 choose Q=P(s-1,1), the classical (s-1) singleton edges; relative to its zero-symbol anchor the empty trace packet has a=s-2>=2. Then F_s tensor Q^m has rank s+m, size (s+1)(s-1)^m and s shielded packets EACH of size (s-2)^m.

Therefore FALSE: "nonempty s trace sunflower packets with exponentially many residues per packet force compatible original petals", or "for every tuple of large packets the required partial defect must occupy Omega(m) independent tensor blocks". Neither is a valid replacement for the v1 ancestor lift. A high-density theorem *above* these factor bases, or with explicit non-concentration/correlated hypotheses, is NOT refuted; the s=3 factor base is 9^(1/3), below published 54^(1/4). A tuplewise PM1 inequality is completely paid by z_1 for ALL m, so summing such inequalities without controlling certificate reuse cannot pay the m log a packet growth.

## TS5. Independently quantified VC-dimension obstruction (PROVED / source-controlled)

For the CLASSICAL binary product P(2,k), select D consisting of one designated symbol in each of the k disjoint binary blocks. Each original transversal has a distinct trace on D, ranging over all 2^k subsets, so VCdim(P(2,k))=k (the upper bound follows because k-uniform members cannot shatter k+1 points). For ANY H subset P(2,k), the D-trace map remains injective. The Sauer-Shelah lemma gives

    |H| <= sum_{j=0}^{d} binom(k,j),       d=VCdim(H).         (TS5)

Consequently any H of bounded VC dimension d=O_s(1) has only O_d(k^d) edges, exponentially negligible relative to |P(2,k)|=2^k. More quantitatively, if |H|>=a^k with fixed 1<a<=2, then d>=c(a)k, where c(a) in (0,1/2] is the unique solution of h(c)=log a, with h binary entropy (for d>=k/2 the conclusion follows directly). This is because sum_{j<=d} binom(k,j)<=exp(k h(d/k)) when d<=k/2.

**Verified contemporary sources:** Ge–Wang–Xu–Zhao arXiv:2609.18995 (Jul 2026) prove C_{s,d}^k for bounded VC dimension, with displayed base 50ds for d>=1. Shangguan arXiv:2609.30263 (Sep 2026) improves the stated bounded-VC sunflower base to O(s log(d+1)); neither handles d proportional to k with a base depending on s alone. TS5 only rules out obtaining a large exponential subfamily of P(2,k) with VC dimension bounded independently of k; it does not rule out VC-dependent entropy amortisation.

## TS6. Why no global noncircular rank induction follows

Combining TS2 with PL1 yields exact conditional constraints *within* actual original packets but no bound on the number of different outside residues B; TS4 supplies cross-packet exclusion with no per-block deficit at all. Existing matching extraction gives only a 1/((s-1)k) point link. The s>=4 empty-trace rank-zero packet still exists, proper traces have matching number at most s-2, and TS1 cannot silently be applied across trace-size layers. A proof must distinguish high-entropy packet configurations from local seed-vertex shields by a certifiably bounded global charge, or exploit genuinely different structure. This is the central OPEN step.

Mandatory controls remain P(s-1,k); Q9^m; classical triangle tensors; prior-art Abbott–Hanson H54 (rank4, 3-free, link fraction 2/9), Axante et al. H39 (rank3, 4-free, 3/13) and nonregular H153 (rank3, 6-free, 3/17). Their strict tensor density floors 54^(1/4), 39^(1/3), 153^(1/3) are LOWER construction barriers only, never upper bounds. PB1 pair-certificate capacity is separate from edge ownership and is not contradicted. s=1,2 lie outside the target. For k=1, f_s(1)=s-1; for k=2, graph bounds cannot be deduced by TS4's rank-s seed. No new general bound at k=1,2,3 is asserted.

## Reproducible finite checks and attribution

scripts/cross_trace_shield_audit.py and tests/test_cross_trace_shield_audit.py audit all 387 nonempty 3-free triple subfamilies on five points, the equal-size trace dichotomy and two-axis row constraint, original F_s for s=3,...,8, Q9's four-element empty-trace packet, explicit tensor packets and original VC controls for binary products k<=4. Five local standalone tests passed. Tensor conclusions for arbitrary m and s are SYMBOLIC PROOFS above, not extrapolations from tests. Hosted full-repository checks must still run on the exact PR head.

Sources: Mishra arXiv:2606.02667v1 invalid full-shift transfer versus v2 shifted-only; classical Erdos-Rado product and Sauer-Shelah; Q9 classical quadratic cap; Abbott–Hanson / Axante et al. arXiv:2609.06175; Bell–Chueluecha–Warnke Discrete Math. 2021; Anup Rao JLMS 2026 survey; Ge et al. https://arxiv.org/abs/2609.18995 ; Shangguan https://arxiv.org/abs/2609.30263 . None is a verified proof of the unrestricted conjecture. This note claims no mathematics-literature priority.
