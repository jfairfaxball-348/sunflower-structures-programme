# Coupled original physical cores: exact Turán rigidity and a dense near-equality obstruction

16 October 2026. CC1–CC6 **internally proved**; source/prior-art priority **NOT CHECKED**. Unrestricted Erdős–Rado sunflower conjecture remains **OPEN**. All owners below are literally physical ORIGINAL sets; no shifted lift.

## CC1 — a genuinely coupled, all-core intersection statistic (PROVED)

For two nonempty disjoint owner packets P,Q, draw independently A,A' from full-support mu on P, B,B' from full-support nu on Q (with replacement *within* each packet). The core c(A,B):=A∩B is an ACTUAL physical set, possibly empty. Set

    J(P,Q) = Pr[c(A,B) ≠ c(A',B)] + Pr[c(A,B) ≠ c(A,B')].       (CC1)

The same B (respectively A) is retained in the paired comparisons, so this probes correlations of changing cores, rather than a linear weighted sum of independent fixed-D Turán defects. If p_D=Pr[c(A,B)=D], then

    1−sum_D p_D² ≤ J(P,Q),               max_D p_D ≥ 1−J.   (CC2)

**Proof:** Compare independent c(A,B) and c(A',B') through c(A',B), using the union bound. The independent mismatch has probability 1−sum_D p_D². Since sum p_D²≤max p_D the second inequality follows. In particular J=0 iff ALL original cross pairs have exactly ONE common physical intersection D, by full support.

For J<1, a modal D has cross probability ≥1−J. Both packet laws individually give ≥1−J mass to owners containing D: any owner missing D cannot participate in an equality c(A,B)=D. On independently conditioning on D-containing original owners, the probability that cross intersections differ from D is at most J/(1−J)²; the corresponding expected number of extra intersection points is at most kJ/(1−J)². This is a true approximate structural certificate with a quantified error, not an exact rank reduction.

## CC2 — exact K_s-free Turán equality really separates physical supports (PROVED)

Let F be simple original s-sunflower-free k-uniform, r=|F|≥s and q=s−1. Fix physical D. Let G_D have one vertex for each ACTUAL original edge and AB an edge iff A∩B=D. Since a K_s would be an actual s-sunflower, G_D is K_s-free. If e(G_D)=ex(r,K_s), the classical Turán **equality characterization** forces a complete balanced q-partite graph with all q classes nonempty.

Each original owner has a cross-class neighbour, so contains D. For any two distinct classes, their physical residual ground supports outside D are disjoint: a shared real vertex x outside D would contradict cross intersection exactly D. Any two distinct owners in one class have residual intersection nonempty, or they would have formed a G_D edge. All classes are inherited s-free. Conversely, taking ≤q disjoint-support, pairwise-intersecting s-free original residual families and adding a common physical D gives an s-free family (within one class inherited; across ≥2 classes pigeonhole forces both a within-class and a cross-class pair, with different intersections). Balanced class sizes make G_D extremal. No universal marker inside any class is required.

**Gap:** the classes' true original residual sizes remain unconstrained by anything other than the unresolved extremal bound. Exact splitting alone is NOT a proof that |F|≤C_s^k.

## CC3 — near-equality yet large exact-purification loss at every nonvacuous density (PROVED)

Fix s≥3, q=s−1, n≥3 and any original simple s-free d-uniform seed H of size M≥2. For m≥1 take true physical group markers x_g (g∈[q]), shared true index points y_i (i∈[n]), distinct group-specific pairpoints p_(g,{i,j}) (i<j), and private physically disjoint copies H_(g,i)^{⊗m} of H on dm vertices per member. All vertices named above are distinct unless explicitly identical. The g,i labels are metadata, never fictitious ground vertices. The original edges are

    A_(g,i,E) = {x_g,y_i} ∪ {p_(g,{i,j}):j≠i} ∪ E,
    E in H_(g,i)^{⊗m}.                                   (CC3)

Then the family is simple and uniform, with

    k=n+1+dm,   |F|=qnM^m,   L=M^m.                      (CC4)

For different groups, the actual intersection is {y_i} iff indices agree, otherwise EMPTY. Within one group, different indices i,j meet in exactly {x_g,p_(g,{i,j})}; two owners with the same index share x_g,y_i and possibly private suffix points.

**S-free proof:** A purported s-sunflower using ≥2 groups has a repeated group (only q=s−1 available); the repeated-group intersection contains x_g while some cross-group intersection does not. If all s owners lie in one group and there are ≥3 distinct indices, the distinct physical pairpoints p_(g,{i,j}) exclude a common intersection. With exactly two indices and a repeated index, a within-index pair contains y_i but a cross-index pair does not. With one index, s-free tensor H^{⊗m} forbids s distinct owners: each tensor coordinate must be all-equal or project to s distinct sunflower petals, and some coordinate differs if full owners differ. Thus NO original s-sunflower, including empty-core cases.

At D=empty, G_D consists of q balanced classes of nL original owners, complete across classes EXCEPT for n matching-index L×L blocks between every two classes. Therefore

    ex(qnL,K_s) − e(G_empty) = binom(q,2)nL²,
    [ex−e]/ex = 1/n.                                      (CC5)

But ANY refinement respecting the original q group parts in which EVERY cross-group intersection is empty retains at most nL owners total: for each index i, its y_i prevents retention from two different groups. At least (q−1)/q of ALL original owners must be discarded. This refutes an (1−o(1))-owner exactification from o(1) relative Turán deficit. It does NOT rule out constant-factor deletion or genuinely approximate rank arguments.

For independent uniform owners in different original groups, c(A,B) is empty except when indices agree, in which case it is the physical singleton {y_i}. Direct counting of the event exactly one of I,I' equals J gives

    J(P_g,P_h) = 4(n−1)/n² →0.                            (CC6)

Even this nonlinear cross-core heterogeneity signal has no uniform positive bonus at high density. Indeed let beta_s=sup_d f_s(d)^{1/d} (possibly infinite). For every T with 1<T<beta_s choose genuine s-free H with M>T^d, and set n=floor(sqrt(m))≥3. Then n=o(m) and

    |F|/T^k = qn T^{−n−1}(M/T^d)^m →∞,

while both relative deficit 1/n and J tend to zero. The full conjecture is NOT refuted; no hypothetical larger C_s is excluded.

## CC4 — independently enumerated finite checks and higher intersections

The stdlib auditor scripts/coupled_cross_core_audit.py creates literal vertices, enumerates EVERY s-subset and tests actual pair-intersection sets, exact missing Turán edges, and J as Fraction. It verifies

| s | n | m | original edges | rank | deficit | J |
|---|---|---|---|---|---|---|
| 3 | 3 | 1 | 12 | 5 | 12 | 8/9 |
| 3 | 4 | 1 | 16 | 6 | 16 | 3/4 |
| 3 | 3 | 2 | 24 | 6 | 48 | 8/9 |
| 4 | 3 | 1 | 27 | 5 | 81 | 8/9 |

Every tested sunflower count equals ZERO, using private actual H=P(q,1) singleton seeds. The H54 prior-art seed is used SYMBOLICALLY only: T=5/2, M=54, d=4, M/T^d=864/625>1, so the original correlated construction beats T^k when m≫n; its 54 source edges are NOT newly reconstructed.

## CC5 — two independent attempted fixed-base routes and quantitative failure

**Peel perfect parts, charge original residuals.** CC2 gives disjoint support classes, but q copies of H^{⊗m} may each exceed a trial base T^{dm}; TC3 already gives real rank-one markers with Kraft cost q/T≤1 and unbounded actual residual ratio (M/T^d)^m when q≤T<M^{1/d}. An alleged global recurrence that inserts |H^{⊗m}|≤T^{dm} is circular (and false at these trial bases). NW1 gives an even stronger all-physical rank-3t, 9^t four-free example with Z_2=(3/4)^t; it invalidates Kraft-budget-only closure. This is not a proof no sufficiently large C_s exists.

**Regularise approximate cores to bounded VC.** Pick any genuine seed H with at least two distinct edges and choose a ground vertex v present in one and absent in another. One physical packet H_(g,i)^{⊗m} shatters the m coordinates of copies of v because all 2^m membership words occur. Thus VCdim(F)≥m while rank k=n+1+dm, so VCdim(F)/k≥1/d−o(1) when n=o(m). Ge–Wang–Xu–Zhao and Shangguan bounded-VC bounds still have dimension-dependent bases. This regularisation does NOT yield bounded VC dimension for all original dense families.

**Higher-order intersection Venn atoms:** For s distinct true original edges, write t_x for the number containing physical x. They form a sunflower iff every x has multiplicity 0,1,or s. Hence in an s-free family sum_x 1_{2≤t_x≤s−1}≥1. This simultaneously couples all cores including empty D, but is the programme's already-known partial multiplicity certificate; its mere positivity has not beaten the old (s−1)k factor.

## CC6 — scope, source audit and remaining challenge

Positive CC1 and CC2 are mathematically exact; CC3 rules out near-total exact purification from small Turán/J energy, not approximation tolerant of exceptional crosses. A useful next result must charge actual residual owner capacity NONCIRCULARLY, perhaps by approximately retaining a constant proportion at a provably amortised physical rank reduction.

Mishra v1 https://arxiv.org/html/2606.02667v1 has invalid cumulative original-source attribution and false O_s(2^k) unrestricted consequence for s≥4; Mishra v2 https://arxiv.org/html/2606.02667v2 remains shifted-only. Original finite H54/H39/H153 factors from Axante et al. https://arxiv.org/abs/2609.06175 and earlier work are PRIOR ART. General background Bell–Chueluecha–Warnke https://doi.org/10.1016/j.disc.2021.112367 and Rao https://doi.org/10.1112/jlms.70380; dimension-sensitive Ge et al. https://arxiv.org/abs/2609.18995 and Shangguan https://arxiv.org/abs/2609.30263 do not prove a k-independent original result. Do NOT claim exact unverified LP values: only 16≤V_3(T²)≤34 and 11≤V_3(S⊗Q9²)≤26. **No full proof, no paper, no external priority claim.**
