# Fractional ORIGINAL point-link rigidity: exact LPs, arbitrary tensor subfamilies, and an entropy counter-control

15 October 2026. **Status: internal mathematical proofs with exact rational certificates; literature novelty/priority NOT CHECKED. The full Erdős–Rado Sunflower Conjecture is OPEN.** Source factors H54 (Abbott–Hanson, as reproduced by Axante et al.), H39 and H153 (Axante et al.) are **PUBLISHED PRIOR ART**. The elementary fractional LP analysis below is programme-local; we make no mathematical-literature novelty claim.

## FL1. Fractional point-link minimax (PROVED; no shifting)

Let H be a nonempty finite simple ORIGINAL d-uniform family of actual sets. Define

    t(H) = min_{probability p on H} max_{actual x} sum_{E in H:x in E} p(E).

Define its fractional matching/packing LP and dual actual-point covering LP:

    nu*(H)=max sum_E y_E,
       y_E>=0, sum_{E:x in E} y_E<=1 for each ACTUAL x;
    tau*(H)=min sum_x z_x,
       z_x>=0, sum_{x in E} z_x>=1 for each ORIGINAL E.

Exact finite LP duality yields nu*=tau*. Scaling y=p/t gives **t(H)=1/nu*(H)**: for each probability p, its maximum point incidence t_p yields a feasible packing p/t_p; conversely any optimal packing y gives a distribution y/nu*. Positivity holds for nonempty positive-rank H. This is the point-link LP, **NOT** the different anchored-defect V_s LP.

For finite ORIGINAL d_i-uniform H_i on disjoint actual vertex blocks, their complete product H=H_1 tensor ... tensor H_m consists of distinct original unions, rank sum d_i. For any probability measure on the ORIGINAL product edges, take its marginal p_i on factor i. The maximum ORIGINAL point probability equals max_i max_x p_i(x in E). Every p_i has maximum >=t(H_i); choosing independent optimal p_i attains equality. Hence the exact tensor identity is

    t(H_1 tensor ... tensor H_m)=max_i t(H_i),        (FL1a)
    nu*(H_1 tensor ... tensor H_m)=min_i nu*(H_i).    (FL1b)

**Stronger arbitrary-deletion corollary (PROVED):** for every nonempty ORIGINAL subfamily G of this product, write the *uniform* measure on G. Each marginal lies on H_i, so

    theta(G):=max_{actual x} deg_G(x)/|G|
       >= max_i t(H_i).                             (FL1c)

This survives arbitrary cross-coordinate correlations, adversarial deletions, nonproduct selections and size-dependent conditioning: no independence assumption on G. It is NOT a theorem that theta(G) is bounded above, nor a high-density link theorem for arbitrary F.

For any s>=3, if each H_i is ORIGINAL s-sunflower-free then the product and its subfamilies are s-free. Proof: for an s-tuple with equal pairwise intersections in the product, within each block the coordinate sets must be either all identical or pairwise distinct. Indeed two equal coordinate sets A=B force A cap C=A for every remaining coordinate set C, and equal rank forces C=A. If some coordinate is pairwise distinct it would be an ORIGINAL s-sunflower in the corresponding H_i; if all coordinates are equal the product petals coincide. Both possibilities contradict a genuine s-sunflower. Empty and nonempty cores are both covered.

## FL2. Three flagship high-density factors have sharp rational ORIGINAL certificates

In the table, y is a feasible ORIGINAL-edge packing and z is a feasible actual-point cover. Equality of total y and total z proves exact optimality, with NO numerical solver or inferred shifted owner.

| s, original factor | (rank,edges) | packing y_E | vertex cover z_x | nu*=tau* | t(H)=theta(H) |
| --- | --- | --- | --- | --- | --- |
| 3: H54 | (4,54), two disjoint 27-edge intersecting components, 18 actual points | y_E=1/12 every edge | z_x=1/4 all 18 points | 9/2 | 2/9 |
| 4: H39 | (3,39), 13 actual points | y_E=1/9 every edge | z_x=1/3 all 13 points | 13/3 | 3/13 |
| 6: H153 | (3,153), 126 cyclic triples on first 14 points and 27 cone triples on disjoint support with apex c=25 | y_E=1/27 every edge | z_x=1/3 for x in first 14; z_c=1; zero elsewhere | 17/3 | 3/17 |

For H54 all 18 actual points have original degree 12, every original edge has size four, so packing loads are 12/12=1 and cover costs 4/4=1; both objectives equal 54/12=18/4=9/2. For H39 all 13 points have degree nine, each original edge has size three; both objectives equal 39/9=13/3. For H153, 14 cyclic-support vertices and c each have original degree 27; other cone-support points have degree at most five (thus packing load <=5/27). Every original triple belongs to exactly one of the two physical components: either it has three vertices among the first 14, costing 3/3=1, or contains c, costing one. Both objectives equal 153/27=14/3+1=17/3. These are **explicit exact rational primal/dual certificates**, not numerical LP guesses. The independent stdlib auditor reconstructs all original edges and checks every constraint.

**Corollary (arbitrary correlated deletion rigidity):** for EVERY nonempty G subset H54^m, theta(G)>=2/9; EVERY nonempty G subset H39^m has theta(G)>=3/13; EVERY nonempty G subset H153^m has theta(G)>=3/17. Uniform full products attain each bound exactly. This proves that deleting or entropy-conditioning original product words, however correlated, CANNOT lower these point-link fractions. It is a quantified barrier to one strategy for constructing sharper high-density link counterexamples; it does not demonstrate a positive link theorem outside the products.

The certificates provide *newly explicit within this programme* explanations for the earlier recorded theta factors, and complement (not replace) the balanced **defect** LPs. Because both LPs are distinct, the quadratic pair-star V_s obstruction and lambda_opt=1 do not imply these conclusions.

## FL3. Uniform factor distributions are NOT always minimax: fully original entropy/type-class example

Let H4 consist of the four original rank-three pair-stars E_i indexed i=0,1,2,3, on the six ACTUAL points {i,j} for i<j. Adjoin a fifth original rank-three edge Z on **three new private actual points**, disjoint from all pair-stars. Call the resulting rank-three family B. B is 3-free: triples from three different pair-stars have three different singleton intersections; any triple containing Z and two pair-stars has one nonempty pair intersection and two empty ones. There is just one Z, so no other triple types. Thus both empty/nonempty 3-cores are actually excluded.

| quantity | exact |
| --- | --- |
| |B|, rank | 5, 3 |
| theta(B), uniform | 2/5 |
| fractional packing | y(E_i)=1/2 for i=0..3; y(Z)=1 |
| fractional cover | z({i,j})=1/3 at all six pair-points; z at one private point of Z =1, zero at the other two |
| equal LP optima | nu*(B)=tau*(B)=3 |
| minimax point fraction | t(B)=1/3 < 2/5 |

Take m=6h product coordinates (disjoint actual copies of the seven? **nine** physical B points: six pairpoints and three private points). Retain just the ORIGINAL product words with exactly h copies of each E_i and 2h copies of Z. These are **distinct original sets**, not shifted images, of rank 18h; the count is exactly

    M_h=(6h)! / ((h!)^4 (2h)!).

Every coordinate has marginal probabilities p(E_i)=1/6, p(Z)=1/3 by permutation symmetry. Each pairpoint belongs to exactly two E_i; each Z point belongs to Z; therefore every actual point has degree exactly M_h/3, and

    theta(B_type,h)=1/3,   B_type,h is 3-free.

For h=1, M_1=360 original rank-18 edges, every physical point belongs to exactly 120 members. Stirling proves

    lim_(h->infty) M_h^(1/(18h))
       = exp([ (2/3)log 6+(1/3)log 3 ] /3)
       = 108^(1/9) >1.                                      (FL3a)

Therefore for EVERY 1<D<108^(1/9), the concrete s=3 family above has arbitrarily large ranks, |F|>D^k, and theta=1/3. An asserted density-conditioned implication with this D and phi>1/3 is FALSE. This is a *genuine exponential-density* control, but it is weaker than the previously known H54 factor (density base 54^(1/4)>108^(1/9), theta 2/9<1/3). Its value is methodological: it demonstrates why checking only uniform factor distributions is insufficient for **other** nonregular seeds.

More generally, for any finite original s-free d-uniform H and rational probability p on its actual edges, exact constant-composition original product subfamilies at arbitrarily large m have

    lim |F_m|^(1/(dm))=exp(H(p)/d),
    theta(F_m)=max_x p({E:x in E}).

Thus any proposed pair (D_s,phi_s) with D_s<exp(H(p)/d) and phi_s>max_x p(x in E) is refuted by actual ORIGINAL s-free families, with strict threshold directions. This is an **entropy frontier necessary condition**, not an upper bound.

## FL4. Nonvacuity, rank recursion, and negative strategic tests

Set beta_s=sup_k f_s(k)^(1/k). Exactly as in PS3, the promise |F|>D_s^k is nonvacuous at arbitrarily large rank iff D_s<beta_s, using ORIGINAL tensor powers; for D_s>=beta_s it is vacuous. Certified prior-art floors are beta_3>=54^(1/4), beta_4>=39^(1/3), beta_6>=153^(1/3). The following concrete proposed test premises are demonstrably NONVACUOUS but entirely **UNPROVED**:

    s=3: (D,phi)=(5/2,1/5) because 5/2<54^(1/4), 1/5<2/9.
    s=4: (D,phi)=(10/3,1/5) because 10/3<39^(1/3), 1/5<3/13.
    s=6: (D,phi)=(21/4,1/6) because 21/4<153^(1/3), 1/6<3/17.

These inequalities simply avoid the listed counterexamples; they are NOT evidence that the premises hold. Arbitrary F outside these product classes is untouched. The noncircular conditional link recurrence remains

    f_s(k)<=max(D_s^k,phi_s^(-1)f_s(k-1))
    => f_s(k)<=C_s^k, C_s=max(D_s,phi_s^(-1),s-1,1),

provided the real high-density ORIGINAL link premise is independently **PROVED**. Here f_s(0)=1, f_s(1)=s-1, f_3(2)=6 (two disjoint triangles); a claimed original coefficient two from k=1 is FALSE. Both empty-core matchings and nonempty-core stars count.

**Strategy A (owner-sensitive dual):** the defect LP V_s from earlier sessions has quadratic balanced sparse counterexamples; this new vertex-incidence fractional matching LP gives a separate exact minimax invariant. Neither supplies the needed bound nu*(F)<=B_s for exponentially large arbitrary original s-free F. Such a bound, when D_s<beta_s, would imply the missing positive point link; it has NOT been established.

**Strategy B (original shadows/entropy/correlated filtering):** the exact marginal proof FL1c defeats every correlated-subfamily attack on the three flagship tensor powers: even though original blocks can have sophisticated witness correlations, their point-incidence minimax constraints cannot improve. The low-density B example demonstrates nonuniform marginal effects generally. A proof of fixed-base rank descent still requires a theorem about arbitrary high-density families, not tensor factors alone. Bounded VC theorems depend on d and do not yield C_s independent of k when d grows with k.

**Correlated defect LP:** no exact new primal/dual certificate was found for V_3((AS3 tensor Q9)^2) or V_3(AS3 tensor Q9^2). Honest bounds remain 16<=V_3(T^2)<=34 and 11<=V_3(S tensor Q9^2)<=26; no objective/equality or strict excess is claimed. Enumerating all original records of a 2025-edge rank-12 product was not undertaken; random subsets or approximate LPs would not certify the requested strict theorem.

## FL5. Source control / reproducibility

- Mishra [v1](https://arxiv.org/html/2606.02667v1): claimed universal O_s(2^k) FALSE for s>=4 by classical P(s-1,k); unsupported cumulative original-owner shift transfer. [v2](https://arxiv.org/html/2606.02667v2): SHIFTED-only theorem, not an original-family proof.
- Published base regime: Bell–Chueluecha–Warnke, *Note on Sunflowers* (2021), https://doi.org/10.1016/j.disc.2021.112367 ; Rao, *The story of sunflowers* (2026), https://doi.org/10.1112/jlms.70380 . No unrestricted fixed base is supplied.
- H54 attributed to Abbott–Hanson; H39 and H153 published by Axante et al., https://arxiv.org/abs/2609.06175 . The exact factor reconstructions above agree with existing repository scripts; no independent priority claim.
- Ge–Wang–Xu–Zhao, https://arxiv.org/abs/2609.18995 and Shangguan https://arxiv.org/abs/2609.30263 : bounded-VC source bounds depend on dimension, so do not bridge unrestricted families.
- Exact independent executable: scripts/fractional_link_lp_audit.py and tests/test_fractional_link_lp_audit.py . Rational feasibility and dual equality checked for each actual original edge/point; factor source code is reconstructed independently of existing audit imports. Finite checks do not establish the symbolic tensor lemma or unrestricted conjecture.
- **Verdict:** FL1–FL3 PROVED internally; nonvacuity conditional pairs only TEST CASES; universal nonvacuous point-link implication OPEN; V(T^2) exact correlated synergy OPEN; conjecture OPEN. Literature originality PRIORITY NOT CHECKED.
