# Physical near-Turán packet stability, exact exceptional matching, and unpaid residual rank (CSM1–CSM6)

16 October 2026. All set systems in this note are **literal simple ORIGINAL physical sets**; no shift, fictitious label vertex, or changed owner. **INTERNALLY PROVED, EXTERNAL PRIORITY NOT CHECKED.** Graph degree sums, Mantel, and König are classical; the special application and audit are not an originality assertion. The full unrestricted Erdős–Rado sunflower conjecture remains **OPEN**.

## CSM1. Quantitative three-petal fixed-core stability (PROVED)

Let F be a finite simple **3-sunflower-free** k-uniform family of r>=3 ORIGINAL edges, and D any actual set of physical ground points. Let G_D on the r ACTUAL owners have uv iff E_u intersect E_v is **exactly D**. G_D is triangle-free: a triangle would be three distinct original petals with equal pairwise intersections. Write e=|E(G_D)|>0 and Delta=r²/4-e>=0 (the last step is Mantel).

There exist two disjoint packets A,B of original edges, determined by one ACTUAL adjacent pair u,v, and a remainder R=F\(A union B), such that, with a=|A|, b=|B|,

    |R| <= 4 Delta / r;
    every owner in A union B contains the physical set D;
    each of A and B has no distinct pair with intersection exactly D;
    bad_D(A,B):=|{(U,V) in A×B:U∩V != D}| <= 5 Delta;
    |a-b|² <= 20 Delta.                                      (CSM1)

In particular A\D and B\D are separately pairwise-intersecting ORIGINAL (k-|D|)-uniform, three-sunflower-free residual families (whenever packets have at least two members). This does *not* assert that all cross pairs intersect in D, that D is nonempty, or that either residual capacity is bounded by C^(k-|D|).

**Full elementary proof.** For any triangle-free graph, sum_{uv in E}(deg u + deg v) = sum_v deg(v)² >= (2e)²/r (Cauchy). Hence some actual adjacent u,v have deg(u)+deg(v) >= 4e/r. Set A=N(u), B=N(v). Triangle-freeness says A and B are disjoint independent vertex sets: a common neighbour would be a triangle and an internal neighbour of N(u) or N(v) likewise. Thus |R|=r-a-b <= r-4e/r=4Delta/r. All neighbours of u/v contain D since their real pair intersection equals D. Two owners in either packet cannot intersect exactly D because the packet is independent in G_D. Since both contain D, each such pair's physical residual intersection is nonempty.

All graph edges not joining A to B touch R (there are no edges inside A or B). There are at most r|R| graph edges touching R, so e_G(A,B)>=e-r|R|. Since ab <=(a+b)²/4<=r²/4, the count of *missing* A×B graph edges is

    ab-e_G(A,B) <= r²/4-e+r|R|
                 = Delta+r|R| <= 5Delta.

Moreover ab>=e-r|R|>=r²/4-5Delta, and (a-b)²=(a+b)²-4ab<=r²-4(r²/4-5Delta)=20Delta. Every assertion uses original owner sets and real intersections. QED.

When e=0 no positive structure is claimed; this is indispensable (e.g. the four-owner physical pair-star at core empty). Note Delta may be a quarter-integer when r is odd, so all statements retain exact rational meaning.

## CSM2. The exact price of cleaning exceptional crosses (PROVED)

With A,B chosen as in CSM1, construct the bipartite **bad-cross graph** H with original owners A and B, joining U in A and V in B iff their ACTUAL intersection is not D. Deleting owners to make **every retained cross intersection exactly D** is equivalent, without approximation, to choosing a vertex cover of H. Thus the exact smallest deletion cost is

    tau(H) = nu(H)                                            (CSM2)

by classical bipartite König, with nu the maximum matching of bad owner pairs. Any minimum cover gives surviving packets A',B'; the ACTUAL physical supports of A'\D and B'\D are disjoint (otherwise a shared real vertex outside D witnesses a still-bad cross). Internal residual families stay intersecting and three-sunflower-free. An honest ORIGINAL cardinality certificate is therefore

    r <= |R| + nu(H) + 2 i_3(k-|D|)                            (CSM3)

where i_3(h) is the TRUE maximum cardinality of an intersecting original simple h-uniform three-sunflower-free family. In fact the stronger **approximate** inequality

    r <= |R| + 2 i_3(k-|D|) <= (4 Delta/r)+2 i_3(k-|D|)       (CSM4)

already follows before exact purification. Formulae CSM3/4 are noncircular *identities/inequalities reducing to an independently named extremal function*, but they are NOT a fixed-base bound: i_3(h) is not known to obey a bound C^h with C independent of h. For empty D, they do not even reduce rank. The matching cost nu is a rigorous missing obstruction variable: the edge count of H alone does not control it relative to r.

## CSM3. Correlated original construction saturates neighbourhood leakage and defeats edge-density payment (PROVED)

Specialise CC3 to s=3, q=2 and the physically original seed H=P(2,1). For integers n>=3,m>=1, let L=2^m and physically distinct ground points x_g (g=0,1), y_i (0<=i<n), p_(g,{i,j}) (i<j), and h_(g,i,t,b) (t<m,b in {0,1}). The ACTUAL original sets are

    U_(g,i,w) = {x_g,y_i} ∪ {p_(g,{i,j}):j!=i}
                ∪ {h_(g,i,t,w_t):0<=t<m},   w in {0,1}^m.

Ground names, unlike g,i,w metadata, are genuine vertices. CC3 already proves this simple family has rank k=n+1+m, size r=2nL, and contains NO three-sunflower (including empty core). For D=empty, G_D is complete bipartite between the two original physical group packets except for n disjoint blocks K_(L,L) with matching index. Exact numbers:

    e=n(n-1)L²,   Delta=nL²,   Delta/(r²/4)=1/n.            (CSM5)

EVERY G_D-adjacent uv has endpoints of different group/index and degrees (n-1)L. Thus the canonical neighbour packets CSM1 have sizes a=b=(n-1)L, |R|=2L=4Delta/r **with equality**. Among these two packets, there are exactly (n-2)L² bad original cross pairs, forming n-2 disjoint copies of K_(L,L). Their exact minimum vertex cover is

    nu=tau=(n-2)L,   |A'|+|B'| = nL = r/2.                    (CSM6)

Therefore even relative missing-Turán-edge density 1/n->0 and bad-cross density (n-2)/(n-1)²->0 are compatible with having to delete HALF of the original owners (including R) to make the CSM1-selected cross packets exact. The all-group purification bound in CC3 gives the same half limit without using the neighbour selection. This explicitly refutes any proposed generic nu/r=o(1) obtained solely from Delta/r²=o(1); it does *not* disprove rank-amortised approximate arguments.

The displayed |R| bound is sharp **for the CSM1 neighbourhood rule**, not for all partitions: the pre-existing two whole original group packets form independent classes with R=empty but still carry the full cross matching cover nL.

At fixed m, exact finite enumerations check n=3,4 and m=1,2. For larger m and n=o(m), the owner-count-to-rank density relative to any 1<T<2 is

    r/T^k = (2n/T^(n+1))*(2/T)^m -> infinity

when n increases sufficiently slowly, e.g. n=floor(sqrt m). For stronger seeds H of true rank d and size M, the same construction gives r=2nM^m, k=n+1+dm and the previous CC3 argument covers any nonvacuous 1<T<beta_3 with M>T^d. The finite audit below reconstructs the P(2,1) original sets; published H54 remains only a symbolic prior-art control.

## CSM4. Two attempted fixed-base original rank recurrences; precise failures

**Attack A — the nonempty physical core neighbourhood contraction.** Fix trial C>=2 and Delta<=delta r² with delta<1/4. If the CSM1 physical core D were nonempty, and an induction independently guaranteed i_3(h)<=C^h for all h<k, then CSM4 would yield

    (1-4delta)r <= 2 C^(k-|D|) <= 2 C^(k-1).

Thus C>=2/(1-4delta) would close that *particular* inductive step. This algebra is correct. The universally necessary premise that some NONEMPTY D has near-Turán e(G_D) is FALSE for the original P(2,k) product: at any nonempty actual D of size t<k, e(G_D)=2^(k-t-1), compared with r²/4=4^(k-1), and it tends to zero relatively with k; at D containing points from both values of one coordinate e(G_D)=0. At D=empty, P(2,k) has e=r/2, still far below r²/4 for large k. The positive inequality is only a conditional/local rank reduction, not an all-F base-C theorem.

**Attack B — pay exceptional-owner matching by physical rank.** Suppose a hypothetical independent physical complexity theorem, not proved here, gave BOTH a nonempty common D, Delta<=delta r² and nu(H)<=lambda r, with 4delta+lambda<1, whenever an original family threatened C^k. Then CSM3 and induction at smaller rank would imply

    r <= 2 C^(k-|D|)+(4delta+lambda)r,

so a C>=2/(1-4delta-lambda) would suffice. However in the actual high-density correlated original family nu/r=(n-2)/(2n)->1/2 although Delta/r²=1/(4n)->0. At the same time physical rank k=n+1+dm contains an unpaid tensor residual of size M^m. No bound lambda=o(1) can be inferred merely from tiny relative exceptional edge-count/J; and setting lambda=1/2 without independently bounding M^m is not a global recurrence. The exact König theorem is a **price certificate**, NOT a certificate that the rank actually funds that price.

The alternate high-VC route does not bridge the gap: an original private H^m fibre in CC3 shatters m named physical points, so bounded-VC results with bases depending on the dimension are not unrestricted fixed-base bounds.

## CSM5. Original adversarial controls and audit boundary

- P(s-1,k): original product rank k, cardinality (s-1)^k and no s-sunflower. At s=3 it invalidates universal nonempty fixed-core near-Turán density (even before any shifting).
- s=3 f_3(2)=6: take two disjoint original triangles. G_empty is exactly K_(3,3), Delta=0, no exceptional crosses, all six original edges are retained. No improvement below six is claimed.
- Original pair-star: rank n-1 with n edges; all intersections are distinct real pairpoints, so G_empty has zero edges. This tests the zero-edge exclusion.
- CC3 correlated: two groups, n shared index vertices, private P(2,1)^m fibres, exact matching cost above. General s>=4 retains CC3/TC3/Turán controls but CSM1 uses triangle-freeness and is **NOT** proved at s>=4.
- TC3 q=s-1 private seed tensor shield and high-density AP7 equality; W(N,m) and NW1 nested all-physical suffix anchors with Z_2=(3/4)^t; H54/H39/H153 published finite factors; alternating shields and AS3/Q9 exact LP intervals only 16<=V_3(T²)<=34 and 11<=V_3(S tensor Q9²)<=26. No CSM theorem upgrades any of those original residuals to fixed-base capacity.
- The Python stdlib auditor scripts/original_core_stability_matching_audit.py creates actual original edges (two triangles, q-product, physical pair-star, CC3 seed), exhaustively enumerates all 3-sunflower triples, forms every actual intersection graph, computes an augmenting-path matching **and a separately checked König alternating-path vertex cover**, tests exact rank/support assertions and rational constants. Unittests call it independently. CI must execute all old scripts as well.

## CSM6. Sources, novelty, and definitive status

Classical triangle-free Mantel/Turán, Cauchy degree-sum, and bipartite König are **PRIOR ART**. Physical CC3 construction and all-core J are from [CC1–CC6](COUPLED_CROSS_CORE_NEAR_TURAN_OBSTRUCTION.md); current neighbour/matching quantitative packaging is programme-internal, **external priority NOT CHECKED**. Mishra v1 https://arxiv.org/html/2606.02667v1 has invalid cumulative shifted-source owner transfer and an O_s(2^k) consequence false for s>=4; v2 https://arxiv.org/html/2606.02667v2 proves shifted families only. Original finite H54/H39/H153 factors are published PRIOR ART https://arxiv.org/abs/2609.06175; general bounds Bell–Chueluecha–Warnke https://doi.org/10.1016/j.disc.2021.112367 and Rao https://doi.org/10.1112/jlms.70380 do not imply fixed C_s here. Ge et al. https://arxiv.org/abs/2609.18995 and Shangguan https://arxiv.org/abs/2609.30263 are VC-dimension sensitive. **NO unrestricted original fixed-base rank recurrence. NO solution. OPEN.**
