# Partial-multiplicity trace certificates and an exact central-layer vector dual (15 October 2026)

**STATUS: PROVED original-family inequalities and an exact restricted coordinate LP; full Erdős–Rado conjecture OPEN.** These are independent deductions within this programme; no claim of literature priority. In particular, the vector LP below is NOT a global multi-anchor LP and gives NO fixed-base bound. Existing factors and q-products are prior art.

## 1. Stronger ORIGINAL s-trace certificate (PROVED, all s>=3)

Let F be a finite simple s-sunflower-free k-uniform ORIGINAL family. Fix E in F and s distinct exact traces U_1,...,U_s subseteq E that themselves form an s-sunflower; assume all trace classes F(E,U_i) are nonempty. As usual R_i={B\U_i:B in F(E,U_i)} consists of original outside residues, and p_i(x)=|{R in R_i:x in R}|/|R_i| for x outside E. The traces may overlap.

A vertex of an s-tuple of edges is a **partial-multiplicity defect** if it belongs to exactly j of them for 2<=j<=s-1. An s-tuple is an s-sunflower **if and only if it has no such defect**: occupancy j=0,1,s is compatible with an exact common pairwise intersection, whereas 2<=j<s changes which pairs intersect.

Because the traces U_i already form an s-sunflower inside E, every choice of ONE original residue R_i from each class MUST have an outside partial-multiplicity defect. Otherwise the distinct original lifts U_i union R_i would be an s-sunflower. Hence

  1 <= sum_(x outside E) sum_(j=2)^(s-1) [t^j] product_(i=1)^s ((1-p_i(x))+t p_i(x)).    (PM1)

The product is the generating function of the independent sampled-residue occupancies of x, NOT an assumption of independence between distinct vertices. The random residues are sampled independently **between** trace classes only for the expectation; no family product hypothesis is used. PM1 follows because the sum of partial-multiplicity indicators is >=1 for every original residue tuple.

For s=3, PM1 is the PRIVATE pair-collision bound

  1 <= sum_x [p_1 p_2(1-p_3)+p_1 p_3(1-p_2)+p_2 p_3(1-p_1)]
    = sum_x [p_1p_2+p_1p_3+p_2p_3-3p_1p_2p_3].           (PM2)

This rigorously strengthens the previously proved CT1 by subtracting triple-common hubs. In integer form, writing n_i=|R_i| and d_i(x)=n_i p_i(x), multiply PM2 by n_1 n_2 n_3:

  n_1 n_2 n_3 <= sum_x [d_1d_2(n_3-d_3)+d_1d_3(n_2-d_2)+d_2d_3(n_1-d_1)].       (PM3)

These inequalities sum over all eligible trace sunflowers, with exact charges and WITHOUT claiming those charges are disjoint.

**Sharp hub counterexample (PROVED):** E=012, A=034, B=134, C=235. This four-member simple 3-uniform original family is 3-free. Its traces 0,1,2 relative to E form a 3-sunflower. The three outside residues have a compulsory common vertex 3, which PM2 assigns ZERO, but exactly one partial-multiplicity defect 4 (in A and B only). Thus the lower bound 1 is sharp even with a triple-common hub. The previous CT1 could be paid solely by hub 3; PM2 correctly detects the extra witness, but still does not force entropy savings.

## 2. Exact central-layer q-product vector LP (PROVED, all s>=3)

Set q=s-1. P(q,m) is the classical family choosing one of q symbols at each of m disjoint singleton blocks, with q^m edges and no s ORIGINAL sunflower. Tensor with the fixed triangle T={01,02,12} to make I_m=T tensor P(q,m), an intersecting core-free s-free ORIGINAL (m+2)-uniform family of size 3q^m. Fix anchor E with triangle component 01 and all coordinate symbols 0. Restrict to originals with triangle component 02; all have triangle trace {0}, all possess outside vertex 2, and for each mask S subseteq [m] the exact trace is {0} union {0_j:j in S}. Every S has (q-1)^(m-|S|) original residues.

Fix an integer r with 1<=r<=m-s+1 and restrict to the SAME central mask level |S|=r (for r about m/2 this is genuinely central). If s pairwise distinct r-masks S_1,...,S_s form a sunflower with common mask K, their private mask components P_i=S_i\K are pairwise disjoint, NONEMPTY, and all have the same size a=r-|K|>=1. Let D=union_i P_i, so |D|=s a >=s.

At every j in D exactly ONE original of the chosen s-tuple has the anchor symbol 0_j. The other s-1 originals take symbols from the q-1=s-2 alternatives. Pigeonhole forces some alternative to occur at least twice, and it occurs at most s-1 times. Therefore j has an ORIGINAL partial-multiplicity defect for **every** choice of residues. The common outside triangle vertex 2 has multiplicity s and contributes NO defect. Coordinates outside D need not contribute. In particular the total number of distinct defect **coordinates** is >=|D|>=s, with equality attainable: choose all s-1 nonanchor alternatives at each j in D identically, and choose an identical symbol for all s originals at other coordinates. This last choice constructs actual original witnesses, not merely abstract masks.

Consider the following rigorously delimited coordinate LP, covering EVERY s-sunflower of distinct r-masks by the guaranteed defect coordinates D:

  minimize sum_(j=1)^m w_j
  subject to w_j>=0 and sum_(j in D(S_1,...,S_s)) w_j>=1
  for all distinct s-sunflowers of r-masks.                                (LP-P)

**The optimum is EXACTLY m/s** for every s>=3, m>=s, 1<=r<=m-s+1. Primal: w_j=1/s for all j is feasible because |D|>=s. For EVERY s-subset D of [m], choose K subset [m]\D of size r-1 (possible by the specified range), and set S_i=K union {d_i} for d_i in D. These are genuine same-level sunflower masks with private support exactly D. Consequently LP-P contains every constraint sum_(j in D)w_j>=1 for |D|=s. A feasible dual to this subcollection assigns y_D=1/binom(m-1,s-1) to each s-subset: at every coordinate the incident dual mass is 1, and its total objective is binom(m,s)/binom(m-1,s-1)=m/s. Strong duality is explicit, with matching primal.

**Negative conclusion precisely scoped:** This non-scalar, trace-class/coordinate-indexed LP has an O(m) optimum and is already saturated on central mask levels in arbitrarily large ORIGINAL s-free families of exponential size 3(s-1)^m. It cannot, by itself, yield the missing exponential central-trace reduction. This does NOT refute arbitrary cross-anchor vector programmes: they may distinguish actual original edges, rank drops and dependent witness reuse rather than merely guaranteed collision coordinates.

## 3. Tensor moment and spectral controls (PROVED identity; exact finite computations)

For any finite simple family Q with N edges, set p_x=deg_Q(x)/N. For three independent uniform members (repetitions allowed), the expected NUMBER of private-pair collision vertices is

  H_3(Q)=3 sum_x p_x^2(1-p_x).                                      (M1)

This is immediate from independent sampling. On disjoint-block tensor products H_3(Q tensor R)=H_3(Q)+H_3(R), because multiplicities are determined coordinatewise. In particular H_3(T)=4/3, H_3(P(2,1))=3/4 and the PUBLISHED Abbott–Hanson H54 factor has 18 vertices all of degree 12 among 54 edges, giving H_3(H54)=56/27. Thus

  H_3(T tensor H54^m)=4/3+(56/27)m.                                (M2)

An additive O(m) collision expectation does not produce a fixed-base sunflower upper bound. It includes repeated ordered members and is not a count of eligible distinct trace triples.

For additional spectral scrutiny, the symmetric scalar overlap matrix K_Q(z)=(z^|A intersect B|)_(A,B in Q) satisfies K_(Q tensor R)(z)=K_Q(z) tensor K_R(z), hence its eigenvalues are pairwise products. At z=1/2, exact finite rational matrix calculation for H54 gives eigenvalue: multiplicity pairs
  (577/16:1), (-287/16:1), (-35/16:4), (7/16:12), (-17/16:12), (1/16:24).
The triangle matrix has 5/4 (once) and -1/4 (twice). Therefore the tensor spectrum for T tensor H54^m consists of all products; its constant row sum is (5/4)(577/16)^m. This confirms the earlier exact scalar normalisation but is **not** an eigenvalue bound on the non-scalar global charge operator. H153 is NOT treated as anchor regular.

## 4. Other routes attempted and exact limitations

**Unrestricted high-density ORIGINAL point link — OPEN.** Let f_s(k) be maximal s-free cardinality, with f_s(0)=1. If explicit D>=1, phi>0 satisfied the unrestricted statement that every s-free k-family with |F|>D^k has a vertex of degree >=phi|F|, then removing that vertex proves f_s(k)<=max(D^k,phi^(-1)f_s(k-1)), hence f_s(k)<=max(D,phi^(-1))^k by induction. This shows why proving such an unrestricted theorem is a central breakthrough obligation, not a harmless ingredient. The previous H54/H153 tensor degree floors remain. Ambient n<=3k gives only phi>=1/3, **not** the unrestricted claim. No numerical nonvacuous unrestricted (D,phi) pair was established.

**Rainbow random restriction — PROVED reduction, insufficient.** Independently k-colour all vertices uniformly. Each original k-edge is rainbow with probability k!/k^k, so some colouring retains at least that fraction; the retained k-partite transversal family is simple, original and s-free. Therefore a bound B^k for ALL such transversal families would imply f_s(k)<=(k^k/k!) B^k <= (eB)^k. But P(s-1,k) is already transversal and no B has been established. This avoids false shift-lifting but simply relocates the difficulty. It supplies no high-density link lemma.

**Matching hit set — PROVED previously, nonclosing.** A maximal original matching of <=s-1 edges covers the family with <=(s-1)k vertices, giving the earlier once-charged trace partition MH1. The u=1 term still has coefficient (s-1)k and deleting a common core may increase matching number; no persistent fixed-base amortised rank potential was derived. For s>=4, proper exact-trace residues have matching number <=s-2, NOT necessarily pairwise-intersecting.

**Alternative original extraction — OPEN.** The multiplicity certificate is a complete local characterisation of forbidden sunflower tuples, not an entropy theorem. To break the q-product dual obstruction requires structural information beyond single-coordinate guaranteed witnesses: e.g., correlated subfamily sparsification whose ORIGINAL edges inherit a bounded-charge rank-drop certificate.

## 5. Verification and controls

Independent finite script `scripts/partial_multiplicity_audit.py` verifies: 387 3-free simple 3-uniform subfamilies of the ten triples on five vertices; 420 eligible distinct-trace collision tuples and total 840 private-defect vertices; a sharp compulsory-hub example; exact LP values including (s,m,r)=(3,5,2),(3,7,3),(4,6,2),(5,8,3),(6,7,2); and H54's degree spectrum/private moment. A finite trace/LP check is NOT a proof of universal claims. Source constructions are classical or attributed to prior literature in SOURCE_REGISTER. Full C_s^k OPEN.
