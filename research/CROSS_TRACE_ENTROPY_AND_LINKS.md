# Cross-trace collision energy, exact scalar normalisation and original density obstructions (15 October 2026)

**STATUS: OPEN, NO UNRESTRICTED PROOF.** Results herein concern ORIGINAL finite simple k-uniform families. The three-way collision inequality, its aggregated form, tensor scalar-weight LP exactness, finite-rank density boundary and one-time matching-hit-set identity are PROVED below. The tempting inference that these deliver C_s^k is FALSE. A general nonvacuous high-density original point-link theorem, exponential entropy savings and full conjecture remain OPEN. Mathematical-literature novelty is NOT asserted.

## 1. Three distinct traces and a collision-energy inequality — PROVED

Let F be 3-sunflower-free, E in F, and U subset E with n_U>0, where F_U={B in F:B intersect E=U} and R_U={B\U:B in F_U}. The residue classes are simple but can have different ranks k-|U|. For x outside E set d_U(x)=|{R in R_U:x in R}| and p_U(x)=d_U(x)/n_U.

Suppose three **pairwise distinct nonempty traces** U,V,W themselves form a 3-sunflower as subsets of E (so U intersect V=U intersect W=V intersect W=T, possibly empty). If R in R_U, S in R_V and Q in R_W are pairwise disjoint, their three distinct ORIGINAL lifts U union R, V union S, W union Q form a 3-sunflower with core T. Impossible. Stronger: if their three outside pairwise intersections are all equal (possibly nonempty), the lifts ALSO form a sunflower; hence no original residue triple may have equal pairwise intersections.

For independent uniformly sampled R,S,Q, every triple has at least one pair of nonempty intersections, so by expectation / union bound,

  1 <= E[|R intersect S|+|R intersect Q|+|S intersect Q|]
    = sum_(x outside E) [p_U(x)p_V(x)+p_U(x)p_W(x)+p_V(x)p_W(x)].  (CT1)

No pairwise constraint is assumed for overlapping distinct U,V; the *third* sunflower trace is essential. Multiplying by n_U n_V n_W yields the exact integer inequality

  n_U n_V n_W <= sum_x [d_U(x)d_V(x)n_W+d_U(x)d_W(x)n_V+d_V(x)d_W(x)n_U]. (CT2)

Summing CT2 over all unordered distinct trace-sunflower triples is a rigorous *aggregate collision-energy certificate*. For s>=4, the analogue with s distinct traces which form an s-sunflower is a sum over all binom(s,2) outside pair-collision expectations >=1. For s=3, the earlier proper exact-trace residue intersection lemma ALSO constrains equal traces separately. CT2 alone does not impose any exponential saving: the right-hand side may be supplied by a single compulsory outside vertex.

Additional intersecting-family pair restriction: if F is intersecting and U intersect V is empty, EVERY R in R_U intersects EVERY S in R_V. This also holds for equal proper traces for s=3 by the original-anchor residue lemma, but does NOT extend to two distinct overlapping traces.

Counterexamples (all actual original petals, all 3-free):
- **Disjoint trace triangle**: E=012, A=034, B=135, C=245; traces 0,1,2 are pairwise disjoint, but A intersect B=3, A intersect C=4, B intersect C=5. All four originals are pairwise intersecting, yet the trace sunflower does not lift.
- **Overlapping trace triangle**: E=0123, A=0145, B=0246, C=0356; traces 01,02,03 sunflower with common 0, while A intersect B=04, A intersect C=05, B intersect C=06. Again all originals are intersecting, 3-free, and there is no original lifted sunflower.
- **No pairwise overlapping-trace implication**: E=0123, A=0145, B=0267, a 3-free intersecting family; traces 01 and 02 overlap but the outside residues 45 and 67 are disjoint. Thus a two-class collision lower bound for all overlapping U,V is FALSE.

**Entropy mechanism / qualified no-go:** In I_m=T_triangle tensor Q^m with anchor triangle edge 01, the alternative triangle components 02 and 12 both contain outsider 2. In particular, every residue of each trace class with a fixed alternative triangle component contains x=2. Consequently every three-sunflower of distinct traces drawn entirely from one alternative triangle arm has p_U(2)=p_V(2)=p_W(2)=1 and CT1 is trivially paid by that vertex. Such distinct trace triples exist at central coordinate levels of T_triangle tensor P(2,1)^m. This alone is an explicit **no-go for any argument asserting uniform savings from CT1 for every trace triple**; it does NOT imply all eligible trace triples lie in one arm. For the binary q=2 tensor specifically, one can check the remaining cases: any eligible trace triple with >=2 classes from one alternative arm already has an unavoidable pair collision at 2; a trace triple with one class in each alternative arm is impossible from triangle trace intersections; a triple using only the anchor's original triangle component and three distinct binary coordinate trace masks must have a coordinate with one mask agreeing and two disagreeing, forcing a shared outside binary symbol between the two disagreeing residues. Thus a single pair collision still pays CT1 without eliminating binomial entropy. For a **general** factor Q (including H54), no assertion about ALL trace triples is made: the arm-pure subcollection already defeats a putative uniform trace-wise improvement.


## 2. Full overlap-potential / LP normalisation — PROVED

For 0<z<=1 consider the nonnegative symmetric incidence kernel M_z(E,B)=z^{|E intersect B|}; this is a scalar rank-discount weight, NOT a claim that one local link resolves other traces. If F has **anchor-regular** overlap polynomial W_E(z)=W(z) for all E, symmetry gives column sum W(z) too. Define p(z)=W(z)/N for N=|F|. Every fractional cover lambda_E>=0 with sum_E lambda_E M_z(E,B)>=1 for all B satisfies, on averaging over B,

  sum_E lambda_E >= 1/p(z).                                     (SC1)

The uniform assignment lambda_E=1/W(z) attains equality for every B. So the exact minimum total fractional anchor weight is

  OPT_F(z)=N/W(z)=1/p(z).                                      (SC2)

For I_m=T_triangle tensor P(q,1)^m, k=m+2, N=3q^m,

  W(z)=z(2+z)(q-1+z)^m,
  OPT_q,m(z)=3/[z(2+z)] * [q/(q-1+z)]^m.                       (SC3)

For J_m=T_triangle tensor H54^m (published Abbott–Hanson 54-edge rank-4 factor), k=4m+2, N=3*54^m,

  W(z)=z(2+z)A(z)^m,  A(z)=27+12z+10z^2+4z^3+z^4,
  OPT_54,m(z)=3/[z(2+z)] * [54/A(z)]^m.                        (SC4)

For any **fixed** 0<z<1, both optima grow exponentially in m: q/(q-1+z)>1 and 54/A(z)>1. At z=1 the exact cost is 1; z=0 yields no cover at all in the intersecting tensor family. At z=1/2,

  OPT_q,m(1/2)=(12/5)*(2q/(2q-1))^m,
  OPT_54,m(1/2)=(12/5)*(864/577)^m.                           (SC5)

This includes the actual rank-sensitive scalar penalty z^u, not merely a low-overlap threshold. It is a **no-go for obtaining a free strict contraction from scalar spectrum after enforcing per-edge normalisation**, NOT for every correlated scheme: the weight can still be split among exponentially many anchors with exactly unit coverage per edge, and a successful proof might exploit vector-valued trace interactions or separately bounded link costs.

The separate low-overlap indicator |E intersect B|<=1 has previously proved exact optima (3/2)(q/(q-1))^m and (3/2)2^m. It is NOT the kernel z^u, so do not conflate these figures. For H153 only the averaged ordered polynomial is known from our diagnostics; (SC2) is not claimed there without anchor regularity. The exact H153 averaged polynomial is (14210+7350z+1696z²+153z³)/23409 and its half-energy for T_triangle tensor H153^m is (5/12)*(2875/3672)^m. For q and H54 the exact normalized half-energies are (5/12)*((2q-1)/(2q))^m and (5/12)*(577/864)^m.

The coefficient/entropy obstruction persists: a typical q-block trace agrees in fraction 1/q of coordinates, and h(1/q)+(1-1/q)log(q-1)=log q. Hence CT1/SC1 do not improve the factorial upper-envelope recurrence i_3(k)<=sum_(u=1)^k binom(k,u)i_3(k-u).

## 3. Quantified original point-links: strict tensor constraints and a genuinely nonvacuous *restricted* case

Write Delta(F)=max_x deg_F(x)/|F| for nonempty F. For an s-free Q of rank w, tensor powers Q^m are s-free: an s-sunflower of globally distinct product choices would force each coordinate to have either all s factor choices identical or all s distinct and forming a factor sunflower. Since Q is s-free, all coordinates must be identical, contradiction. Every vertex of Q^m lies in its one factor coordinate, so Delta(Q^m)=Delta(Q). Its cardinality is |Q|^m, rank wm. Therefore, for each D<|Q|^(1/w), ANY unrestricted proposed link theorem

  |F|>D^k implies Delta(F)>=phi                            (DL1)

is FALSE whenever phi>Delta(Q). This is a rigorous counterexample with exponential original density, with **strict D** only. For P(s-1,k), |F|=(s-1)^k and Delta=1/(s-1). For the 54-edge 3-free factor Delta=12/54=2/9, so D<54^(1/4) and phi>2/9 is FALSE. For published 153-edge six-free rank-three factor Delta=27/153=3/17, so D<153^(1/3) and phi>3/17 is FALSE. The 39-edge four-free rank-three factor yields a separate strict density floor D<39^(1/3) (without asserting a vertex-degree calculation in this note). None of these forbids a sufficiently smaller phi or addresses densities above their respective floors.

For a family on n<=3k ground vertices (an ADDITIONAL restriction), incidence counting yields Delta>=k/n>=1/3, so DL1 holds for s=3 with EXPLICIT D_3=2, phi_3=1/3 on this restricted class. The premise is NONVACUOUS: at k=2, two disjoint triangles have six original edges, no 3-sunflower, n=6=3k, and 6>2^2; their maximum vertex fraction is 1/3. This is a genuine quantified but **ambient-linear-only** lemma; it does not yield the unrestricted conjecture. An unrestricted nonvacuous DL1 at any fixed D>1 and phi>0 remains OPEN and would itself imply a fixed-base bound by link induction, so it must NOT be adopted as an assumption disguised as a theorem.

Finite ranks: f_3(1)=2, i_3(1)=1; f_3(2)=6 (two disjoint triangles), i_3(2)=3 (triangle); at rank 3 published f_3(3)=20 and i_3(3)<=10, and no exact i_3(3) is asserted here. The 54/39/153 constructions are prior art, not new extremal witnesses.

## 4. Matching charged once; common-core trap — PROVED / FALSE inference

Let F be s-free of rank k and M a maximal matching of t<=s-1 edges. Put C=union M, |C|<=tk. Every B in F has nonempty trace U=B intersect C. Partition ONCE by these disjoint exact trace classes. In each class, deleting fixed U preserves simplicity and s-freeness and drops rank |U|. Consequently

  |F| <= sum_(u=1)^k binom(|C|,u) f_s(k-u)
       <= sum_(u=1)^k binom((s-1)k,u) f_s(k-u).           (MH1)

This is a correct, one-time matching-hit-set charge, but substitution f_s(j)<=C0^j has u=1 coefficient (s-1)k/C0 times C0^k, so MH1 still does NOT close a fixed-base induction. A maximal matching cannot be repeatedly charged *as if* a rank-independent support survived deletion.

Indeed take H as two disjoint triangles (a 3-free graph with matching number 2), and F={ {x} union A:A in H }. F is simple, 3-free, rank 3, with matching number **one** because of common x; deleting common x returns H with matching number **two**. Thus a proposed recursion preserving matching-number index under core deletion is FALSE. The proper anchor U=empty class in the earlier E-trace theorem has matching number <=s-2 but has **no rank drop**; MH1 avoids empty trace only because the maximal matching union C is a hitting set.

## 5. Random-restriction and witness certificates: limitation

If U,V,W form a sunflower of traces and three outside residues are disjoint, the lift is an original sunflower, independently of shifting. This is a *valid certificate* rather than an existence theorem. Selecting random colours for outside vertices cannot force one surviving residue from each of three classes in the triangle-tensor example when a mandatory outside vertex must occupy three incompatible colours. Assuming independent residue survival probabilities without handling these correlations is FALSE. The remaining promising direction is to prove that large trace density must force **many compatible classes with low cross-collision energy**, or alternatively show an original heavy link in a genuinely nonvacuous density range above known tensor floors.

## 6. Finite validation and status

The independent script and unit tests: enumerate all 387 three-free subfamilies of the ten triples on five vertices; validate CT2 for every available distinct trace-sunflower triple; check both overlapping/disjoint ORIGINAL obstruction families and disjoint overlapping-trace residues; independently enumerate every H54 anchor and its 27,12,10,4,1 overlap counts and point degree 12; check exact rational q/H54 spectra and normalised covers; test common-core matching increase and two-disjoint-triangle nonvacuous boundary; check H153 average only, not homogeneous-anchor equality. The exhaustive five-vertex sample is finite evidence for the independently proved symbolic assertions, not an all-rank proof.

**PROVED:** CT1–CT2, SC1–SC5 under explicit anchor regularity, fixed-tensor Delta obstruction, restricted n<=3k point-link, MH1 and the common-core matching counterexample.
**FALSE:** equal outside traces of a sunflower automatically lift; all overlapping trace pairs must collide; spectral contraction is free after normalisation; matching index survives deleting a common core; DL1 at the explicit refuted (D,phi) pairs.
**CONDITIONAL:** compatible trace families with a noncircular, quantitatively cheap low-collision extraction might yield rank descent.
**OPEN:** a nonvacuous unrestricted density-dependent point-link theorem and an exponential original-family sunflower bound.

Source versions: Mishra v1 2606.02667v1 is not a valid unrestricted solution; Mishra v2 2606.02667v2 is about SHIFTED families only. Axante et al. 2609.06175 finite factors are PUBLISHED PRIOR ART. No new external novelty priority or solved claim is made.