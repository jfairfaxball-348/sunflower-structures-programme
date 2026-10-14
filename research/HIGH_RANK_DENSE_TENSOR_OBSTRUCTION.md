# Higher-rank original-witness tensor obstruction (14 October 2026)

**Verdict:** symbolic counterexamples to density-restricted *full-shift sunflower-number transfer* for s=3 and s=4; exact shadow-saturation obstruction for s=3. These are NOT upper bounds and do NOT prove the unrestricted sunflower conjecture. The finite factors below are **published prior art**, not discoveries of this programme. The present analysis applies the previously proved collision-safe partial-spoke lemma to those factors.

Sources: Abbott and Hanson, *On finite Delta-systems* (1974), as reported and reconstructed by Axante, Budala, Chitic, Dumitru and Nacu, *Sunflower-Free Uniform Families: Recursive Constructions and Explicit Bounds*, arXiv:2609.06175 (5 September 2026), Sections 5.1 and 6.3–6.4. Original shifting lemma: [DENSE_ANCESTOR_OBSTRUCTION.md](DENSE_ANCESTOR_OBSTRUCTION.md), Lemma 3.

## 1. General anchored-factor tensor lemma (proved)

Let s>=3, w>=2, and let H be a **nonempty simple s-sunflower-free w-uniform** family of h original sets on a finite ground set. Suppose there is B in H and r>=1 **distinct vertices** x_1,...,x_r outside B, such that for each x_i some v_i in B has B-{v_i}+{x_i} in H. No assumption that the v_i are distinct.

For every m>=1, the disjoint-coordinate tensor F_m=H^(tensor m) has rank K=wm, |F_m|=h^m=(h^(1/w))^K, and is s-free. **There is an ordering of its ground set** for which one complete lexicographically ordered Frankl compression pass yields a family G_m with

    tau(G_m) >= rm+1.

This lower bound survives any subsequent sequence of elementary shifts. Indeed tensorization preserves the sunflower number (Lemma 2 of the previous note). Label all copies of B consecutively 1,...,K, then place the mr pairwise distinct copied outsiders x_i after K, and place all other vertices after those. The tensor baseline is [K]. Independently replacing v_i in any coordinate produces mr initial one-spoke edges with **distinct high labels**; Lemma 3 of the previous note produces mr+1 image members with common core [K-1]. Crucially, the conclusion does not assert unique ancestors or preserve final outer labels.

Thus for every 1<D<=h^(1/w), no bound tau(G)<=A_s(D) K/log(K+2) can hold for **all** s-free original families of size at least D^K in the prescribed lex order: use K=wm and let m tend to infinity. This is a *conditional construction principle for factors with an adjacent edge*, not a theorem that all extremal factors possess such a pair. It does not rule out other algorithms, different orderings, or any density D>h^(1/w).

## 2. s=3: rank-four 54-edge factor (proved)

Take two disjoint copies indexed c=0,1, each with three mutually disjoint three-point groups X_(c,0), X_(c,1), X_(c,2). Inside one copy, for each unordered pair of **different** groups i<j choose independently a 2-subset of each and take their union (rank four). There are three choices of group-pair, three 2-subsets in each group, hence 3*3*3=27 edges per copy; the union H_3 contains h=54 rank-four edges on 18 vertices.

Every two edges in one copy intersect: any two group-pairs share a three-point group, and two 2-subsets of a 3-point group intersect. To see that one copy is 3-sunflower-free, compare three edge types. If all have the same group-pair, the 2-subset projections in each participating group must be all identical (three distinct 2-subsets of a 3-set have three different singleton pairwise intersections). Hence all three edges coincide. If exactly two have the same type, their mutual intersection meets a group omitted by the third edge, unlike the other intersections. If all three types are different, their pairwise intersections lie in three distinct groups and are all nonempty. Two copies have disjoint support; any mixed triple has two members from the same copy, which intersect, and a third member disjoint from both. Therefore H_3 is 3-free, has maximum sunflower number 2, and size 54.

Choose B as any four-set obtained from two 2-subsets of the first two groups of copy 0. The **third vertex** of each of these two groups is an outsider x, and replacing one selected vertex of its group by x gives an original edge. The outsiders are distinct: w=4, r=2. Apply section 1:

    K=4m, |F_m|=54^m=(54^(1/4))^K, tau(F_m)=2,
    tau(lexshift(F_m))>=2m+1=K/2+1.

In particular, the previous D<=sqrt(6) restriction floor for s=3 improves to the strictly larger D<=54^(1/4) (approximately 2.7108). The known finite construction comes from Abbott–Hanson; the use of the anchored tensor lemma is a separate compression analysis.

**Exact shadow obstruction.** Every 3-subset in the shadow of one copy consists of a 2-subset in one group and a singleton in another. Its original extension multiplicity is **exactly two**, since the singleton can pair with either of the other two vertices in its group; conversely all such shadows arise. There are 54 distinct shadows per copy and 108 over both copies; every shadow codegree is two. For a tensor power on disjoint blocks, a (K-1)-shadow specifies exactly one coordinate block where a vertex is missing, together with a shadow in that block and full original edges in the other blocks. Thus

    |partial F_m| = m*108*54^(m-1),
    K*|F_m| = 2*|partial F_m|,    K=4m.

Every (K-1)-shadow still has codegree exactly two. Hence the universal shadow-incidence inequality k|F|<=tau(F)|partial F| holds **at equality at exponential base 54^(1/4)** for arbitrarily large K. A proposed strictly positive shadow slack at density D<=54^(1/4) is therefore FALSE for s=3.

Each point in H_3 lies in 12 edges (two choices of partner group, two 2-subsets in its own group containing the point, three 2-subsets in the other group). Thus maximum original degree for F_m is 12*54^(m-1), fraction 2/9 of |F_m|. This factor does not refute a constant-fraction link bound if its permitted loss B_3>=9/2; it only imposes this necessary loss at this density.

## 3. s=4: rank-three 39-edge factor (proved)

Take three disjoint 3-point groups V_0,V_1,V_2, and four further points a,l_01,l_02,l_12. Form H_4 as follows:

- 3 group triples V_i;
- 9 triples {a} union P where P ranges over the three 2-subsets in each V_i;
- 27 triples {l_ij,x,y} for each i<j and x in V_i, y in V_j.

It contains 39 distinct 3-edges on 13 points (Axante et al., Section 5.1). Its pair degrees are at most 3. Each vertex link has matching number at most 3: at a it is three disjoint triangles, at l_ij it is K_(3,3), and at x in V_i it consists of one triangle and two disjoint three-edge stars. An empty-core four-sunflower is also impossible. If a matching contains g group triples: for g=3 no fourth fits; for g=2 at most one more fits; for g=1 the remaining nongroup members avoiding that group must use a or the unique l joining the two remaining groups, so at most two more fit. If g=0, four disjoint nongroup triples must use a,l_01,l_02,l_12 exactly once. The a-triple uses two members of some V_i, and the two l-triples incident to i need two more distinct points of V_i, impossible in a 3-set. Thus H_4 is 4-sunflower-free. There is a 3-star through an l_ij and a vertex in V_i, so tau(H_4)=3.

Choose B=V_0. Replacing one vertex of V_0 by a produces a member of the 9-edge second class; w=3, r=1. Section 1 yields

    K=3m, |F_m|=39^m=(39^(1/3))^K, tau(F_m)=3,
    tau(lexshift(F_m))>=m+1=K/3+1.

Therefore the density-restricted false transfer is now refuted for every D<=39^(1/3) (approximately 3.3912), improving the earlier sqrt(10) baseline for s=4.

For diagnostics: |partial H_4|=63, with shadow-codegree histogram 27 faces of codegree 1, 18 of codegree 2, and 18 of codegree 3; maximum original point degree 9, fraction 3/13. Tensor powers have exact shadow counts m*63*39^(m-1) and maximum point degree 9*39^(m-1). Unlike s=3, the shadow incidence inequality is **not** saturated.

## 4. Attempted original rank reductions and failure modes

1. **High-density arbitrary-link extraction.** Every s-free rank-K family has a maximal matching of at most q=s-1 members, whose union hits all edges. Therefore |F|<=qK*max_x |L_x(F)|. For a fixed D>C>1, |F|>=D^K implies max_x|L_x|>=D^K/(qK)>=C^(K-1) for sufficiently large K. This is a **proved but insufficient** density-decay step: the exponential base drops from D to C. Iterating without new structural control loses a factorial factor; a bound on high-density inputs that already assumes the sought finite C_s would be circular.
2. **Exact traces around an original edge.** Fix E in an s-free rank-K family; for each nonempty proper T subset E, let C_T={A\T : A in F, A cap E=T}. This residue family is (K-|T|)-uniform, s-free, and has matching number at most s-2: s-1 pairwise disjoint residues together with E would form an s-sunflower with core T. This is a sound original-witness statement and generalizes a trace argument appearing in Axante et al. (Section 6.2). It **does not** by itself bound the whole family: the class disjoint from E retains rank K, and summing up to 2^K trace classes gives no constant per-rank loss.
3. **A strict shadow-improvement route.** False for s=3 at all exponential density bases D<=54^(1/4), even when K tends to infinity, by exact equality above.
4. **Universal final-source colour palette.** The manufactured shifted star above has at least cm members, but original tau is only s-1. Any partition of the entire star into classes whose inverse ancestors themselves form original sunflowers requires at least ceil((rm+1)/(s-1)) classes. This does not prove that *every* inverse-compatibility technique has large loss; it falsifies constant-palette claims with that exact class property.

No universal bound |F|<=B_s max_x |L_x|+E_s(K) with an absorbable error was derived above the new floors. No inverse transfer or full C_s^K induction was proved.


## 4a. Exact status of the proposed heavy-link criterion (logical equivalence, not progress by itself)

Consider the statement Q_s: there exist fixed real D>1, B>=1 and integer k0 such that **every** s-free simple k-family with k>=k0 and |F|>D^k has some original vertex x with |L_x(F)|>=|F|/B. Then **Q_s is logically equivalent to the full sunflower conjecture for fixed s**:

- If Q_s holds, let C be at least max(D,B,1) and at least f_s(j)^(1/j) for each 1<=j<k0 (finite by the classical sunflower lemma). Induct on k. An extremal s-free family has either |F|<=D^k<=C^k, or a link with |F|/B<=|L_x|<=f_s(k-1)<=C^(k-1), whence |F|<=B*C^(k-1)<=C^k. This is a valid exact per-rank reduction, with no n dependence and the correct base ranks.
- Conversely, if f_s(k)<=C_s^k, choose D>C_s. Then no s-free family meets |F|>D^k; Q_s holds *vacuously*, for any B.

Consequently merely **postulating** unknown D and B or proving a statement under a threshold already known to be above all possible s-free families is not progress; the quantifier structure can conceal the full conjecture. A future useful theorem must prove Q_s by genuinely independent structure (preferably with a grounded explicit threshold and nonvacuous applications), or attack another precise sufficient condition. The density floors above restrict proposed *shift-transfer* premises, but do not disprove Q_s at those floors.

## 5. Executable corroboration and next obligation

scripts/high_rank_tensor_audit.py and tests/test_high_rank_tensor_audit.py independently enumerate the finite 54-edge and 39-edge factors and check forbidden sunflowers, degrees, shadows, tensor cardinality, tensor shadow formula and original-ancestor star in lex-shifted tensor powers m=1,2. These tests are finite checks only. The all-m consequences follow from the symbolic factor proofs, product lemma and partial-spoke lemma.

**Next:** seek a rank-reducing **original** certificate that does not rely on a strict shadow deficit or on a bounded number of sunflower-lifting classes. Challenge every proposed density condition against D=54^(1/4) for s=3, D=39^(1/3) for s=4, and general H_q products. A new positive result must supply genuinely rank-uniform constants independent of the ground-set size, not a weakening of the target.
