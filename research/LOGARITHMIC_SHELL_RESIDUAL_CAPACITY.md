# Logarithmic physical shells, exponentially small core error, and residual capacity

16 October 2026. **Programme-internal proofs; external mathematical priority NOT CHECKED.** Tensor and substitution constructions, classical triangle/product seeds, graph matching and elementary structural induction are not claimed new in the literature. Every edge below is a literal finite ORIGINAL physical set. The unrestricted sunflower conjecture remains **OPEN**.

## LRC1. A general correlated substitution theorem (PROVED)

Fix s>=3 and q=s-1. Let S={S_1,...,S_n}, n>=3, be a simple **intersecting**, s-sunflower-free a-uniform family. Let H be any nonempty simple s-free d-uniform family, M=|H|>=1. Put L=M^m, m>=0 (the zero-fold tensor is {empty}). Use disjoint physical copies S_i^(g) of the shell ground for each group g in [q], a physical point y_i for each shell index i shared across groups, and mutually disjoint private tensor copies H_(g,i)^m, also disjoint from every shell and y point. Define

    E_(g,i,w) = S_i^(g) union {y_i} union w,
    w in H_(g,i)^m.                                      (LRC1)

Then F is simple, s-free, k=a+1+dm uniform, and r=qnL. Different groups have literal intersection {y_i} for equal indices and empty intersection otherwise. Within one group every pair intersects in the shell. There is **no added group marker**.

**Proof of freeness, including repeated projections.** A putative sunflower using at least two groups has a repeated group because q<s. Its repeated-group pair shares a shell point (S is intersecting), whereas a cross-group pair has no point in that physical shell ground. Their intersections cannot be equal. For a tuple in one group with both a repeated index i and a different index j, its within-i pair contains y_i while its i,j pair omits y_i. If all s indices are distinct, restricting pair intersections to the shell ground gives an s-sunflower in the s distinct ORIGINAL shell edges, impossible. If all indices agree, remove the identical shell and y_i; distinct private owners would give an s-sunflower in H^m. Tensor closure follows because in each uniform factor a sunflower's projections are either all equal or all distinct: a repeated projection forces the common projected pair intersection to be that entire edge, forcing every other equal-size projection to equal it. Some factor must be nonconstant when the full owners are distinct. QED.

The same proof permits different original s-free private fibres F_(g,i) of a common rank b; then rank is a+1+b and size is the sum of their actual cardinalities. Equal fibres are needed only for the balanced formulas below.

## LRC2. Exact core graph, purification, and neighbour matching (PROVED)

G_empty is the complete q-partite graph with q classes of nL actual owners, minus n diagonal-index K_(L,...,L) blocks. Therefore, with ex the classical Turan edge count,

    ex(r,K_s) = binom(q,2)n^2 L^2,
    ex-e(G_empty) = binom(q,2)n L^2,
    (ex-e)/ex = 1/n,
    J(P_g,P_h) = 4(n-1)/n^2.                            (LRC2)

All exceptional cross intersections have size **one**. Every exact empty-cross refinement respecting the original group parts retains at most nL=r/q owners: y_i prevents keeping owners at index i in two different groups. The bound is attained by keeping one whole group; it can also be attained with several nonempty groups by allocating different indices to them. Thus the exact all-group deletion cost is (q-1)nL. The claim concerns these specified group parts; it does not classify every conceivable repartition of F.

At s=3, every G_empty edge has endpoints of different groups and different indices, and every owner has degree (n-1)L. The CSM1 canonical actual neighbour packets consequently satisfy

    Delta=nL^2,  |A|=|B|=(n-1)L,
    |R|=2L=4Delta/r,
    |bad(A,B)|=(n-2)L^2,
    nu(bad)=tau(bad)=(n-2)L,
    retained after R and minimum cover = nL=r/2.        (LRC3)

The matching is explicit: for each of n-2 common surviving indices, pair the L original owners in its two sides bijectively. Different indices have no bad cross edges, and a cover deleting one complete side of each such block has the same size. No abstract bad-pair count is substituted for actual original witnesses.

## LRC3. Triangle tensor shells make the rank cost logarithmic (PROVED)

Let T be the three actual edges of a triangle. Choose S=T^t on t disjoint physical triangle grounds. Then

    n=3^t, a=2t, k=2t+1+dm, r=q 3^t M^m.             (LRC4)

S is intersecting and 3-free, hence s-free for every s>=3; every pair shares a point in each triangle coordinate. Its total common intersection is empty. For t>=2 it **still has empty total intersection after deleting any single shell edge**: each physical triangle point is absent from 3^(t-1)>=3 shell edges. Thus each complete group in F, and each canonical CSM1 neighbour packet when s=3,t>=2, is intersecting with **empty total physical intersection**. Marker peeling cannot reduce its rank. Private grounds and the distinct y_i introduce no common point either.

The shell cost a=2 log_3 n replaces CC3's n-1 pair-star points plus group marker. The same exact matching-loss formulas now hold with exponentially many indices relative to shell rank. For t=1 the full group is core-free, but a neighbour packet excluding one index can have a common triangle point; the t>=2 qualification is essential.

Adjoining an arbitrary fixed physical D to every edge preserves every formula with G_empty replaced by G_D and rank increased by |D|. The residual packets after deleting D still have empty common intersection for t>=2. Thus requiring a nonempty physical D does not itself remove this residual-capacity barrier.

### Exponentially small relative error, linear unpaid residual rank

For any trial density 1<T<beta_s:=sup_d f_s(d)^(1/d), choose a genuine original H with M>T^d. Select a constant alpha>0 such that

    rho := (M/T^d) (3/T^2)^alpha > 1.                  (LRC5)

Such alpha exists: if T^2>3, take alpha<log(M/T^d)/log(T^2/3); otherwise any positive alpha works. Set t=floor(alpha m). Then

    r/T^k = (q/T) (3/T^2)^t (M/T^d)^m -> infinity,
    relative Turan deficit = 3^(-t) = exp(-Theta(k)),
    J <= 4*3^(-t),
    dm/k -> d/(2alpha+d) > 0.                          (LRC6)

At s=3, despite **exponentially** small relative deficit and J, nu/r=(1-2/3^t)/2 -> 1/2. Thus a proposed rank-sensitive purification theorem assuming only exponentially small core-graph error and absence of a common packet point is also FALSE at every nonvacuous trial density. This does not exclude additional structural hypotheses, approximation without exact purification, or a larger-base sunflower theorem. The decay rate depends on H,T and alpha; no arbitrary prescribed rate is asserted.

Choosing t=floor(sqrt(m)) instead gives sublinear shell rank and deficit exp(-Theta(sqrt(k))) while dm/k->1. If H has two different edges, choose a vertex present in one and absent in another; m private coordinate copies are shattered within one original fibre. Hence VCdim(F)>=m, including after the deletion of any complete collection of other fibres. No bounded-dimension reduction follows.

### Required older parameter controls

For the predecessor pair-star CC3, k=n+1+dm and r=q n M^m. At n=floor(sqrt(m)), logarithmic density per m tends to log(M/T^d)>0. At n=floor(gamma m), it tends to log(M/T^d)-gamma log T; density is nonvacuous precisely when this is positive (at equality polynomial prefactors require separate inspection). These formulas apply to every q=s-1. The new shell allows n=3^(floor(alpha m)) while keeping total rank linear in m; directly inserting exponentially large n into the old pair-star construction would not do that.

## LRC4. Intersecting core-free residual capacity is exactly as hard exponentially (PROVED)

Let i_s^0(k) be the largest size of an intersecting original s-free k-family with **empty intersection of all its members**, or zero if the class is empty. Do not confuse this with the weaker condition that a chosen sunflower has empty core.

Given ANY simple original s-free d-family H (including a singleton), substitute three private copies of H behind the triangle edges: U_(i,E)=T_i union E^(i). This is simple, rank d+2, cardinality 3|H|, intersecting and globally core-free. The repeated-index/three-distinct-index proof is LRC1's within-group proof without y_i: a repeated triangle edge has two shell points, whereas its intersection with a different triangle edge has one; three distinct shell edges have unequal pair intersections. For s>3, a nonconstant index tuple must have a repeated index. Consequently

    3 f_s(d) <= i_s^0(d+2) <= f_s(d+2),  d>=0.          (LRC7)

Also f_s(d)<=i_s(d+1) by adding one common physical point. These elementary embeddings give an explicit warning stronger than merely naming i_s: dropping a common core and imposing pairwise intersection do not remove arbitrary original residual growth.

Tensor closure gives f_s(a+b)>=f_s(a)f_s(b). Its exponential growth limit exists in [1,infinity] and equals beta_s; this is CLASSICAL Abbott product/Fekete prior art, also stated in Axante et al., section 2.4. For completeness, for any fixed d and k=md+r, tensor m extremal d-families with a rank-r singleton yields f_s(k)>=f_s(d)^m; taking liminf and then the supremum proves the statement, with no finite-beta assumption. LRC7 then sandwiches the limit for i_s^0(k) between the same shifted f_s sequence and f_s(k). Thus

    lim f_s(k)^(1/k) = lim i_s(k)^(1/k)
                     = lim i_s^0(k)^(1/k) = beta_s.    (LRC8)

For any fixed C>=1, if i_s^0(k)<=C^k for all sufficiently large k, apply LRC7 to H^m: 3|H|^m<=C^(dm+2), then let m grow. It follows that |H|<=C^d for EVERY original H. Conversely an all-rank f_s(k)<=C^k bounds i_s^0 immediately. Therefore an eventual core-free intersecting bound with an unspecified fixed base is an **equivalent unresolved exponential-capacity problem**, not an independent input to CSM4. This is a logical equivalence, not a proof of either bound.

## LRC5. A noncircular fixed-base theorem for a specified construction class (PROVED)

There is a useful positive statement, with its scope made explicit. Supply a finite catalogue A of actual nonempty s-free positive-rank seeds, each independently checked, and put

    B = max(s-1, max_{H in A} |H|^(1/rank(H))).         (LRC9)

Start with A, P(s-1,1), rank-zero singleton {empty}, and all original pair-star shells on N>=3 owners. Close under:

1. Physical relabelling, subfamilies, and adjoining common physical points.
2. Disjoint-ground tensor products.
3. Private substitution: outer S rank a, each inner F_i rank b on mutually private grounds; edges S_i union E with E in F_i.
4. At most q shielded private copies: attach a distinct actual group point to each private rank-b child.
5. LRC1 correlated joins with an **intersecting** outer S and rank-b private children, at most q groups, and the literal shared index point y_i.

Every resulting simple rank-k family is s-free and has |F|<=B^k. This is a genuine **noncircular restricted-class fixed-base theorem**, since every seed inequality is supplied independently, not inferred from f_s.

**Proof.** Pair-stars have N edges of rank N-1 and N<=2^(N-1)<=B^(N-1). The basic singleton/product/catalogue inequalities hold by construction. Tensor counts multiply. Substitution gives sum_i |F_i|<=|S|B^b<=B^(a+b). A shielded join gives at most q B^b<=B^(b+1). A correlated join gives at most q|S|B^b<=B^(a+b+1). Padding and subfamilies preserve the bound. Freeness for substitution uses the repeated uniform projection argument from LRC1; a shielded join uses a repeated group marker; correlated joins use the proved LRC1 case analysis. Structural induction proves all depths, with no ambient-size dependence. QED.

This base is sharp for this class: tensor powers of each catalogue seed attain its density base, and P(q,k) attains q. Arbitrary pair-stars add no larger base. **No theorem that every original s-free family belongs to this class, or has a bounded-cost cover by it, has been proved.** Allowing arbitrary unknown s-free families as catalogue atoms silently replaces (LRC9) by beta_s, exactly the unresolved bound.

For catalogues consisting of the prior published H54 (s=3), H39 (s=4), or H153 (s=6), together with the listed smaller seeds, the sharp class bases are respectively 54^(1/4), 39^(1/3), 153^(1/3). This is a property of these stated closure classes, **not** an upper bound for all originals. Rational trial C=s verifies the necessary finite inequalities without roots. Older wreaths, nested private shells, products and alternating-shield seeds can be included only with their independent seed certificates; no new LP optima are claimed.

## LRC6. Shared-ground attachment defeats a universal finite-catalogue decomposition

**PRIOR-ART operation; independent reconstruction, not a new lower-bound claim.** At s=3, use disjoint grounds X,Z,{x,y}, an intersecting 3-free (k-1)-family A on X and two disjoint copies B of an intersecting 3-free (k-2)-family C on Z. Form

    J(A,C) = {a union {x}, a union {y}:a in A}
             union {b union {x,y}:b in B}.             (LRC10)

Its rank is k and size 2|A|+2|C|. It is intersecting: A supplies intersection within the first type, the second type shares x,y, and cross types share their selected marker. It is 3-free: three first-type edges must share a Y-marker in any sunflower, hence project to three distinct edges of A with equal intersections; three second-type edges would project to a sunflower in B, which is 3-free as a union of two intersecting 3-free families on disjoint grounds. For a mixed triple with two second-type edges, their intersection contains x,y and the first-type edge omits one. With two first-type edges using different markers, their nonempty X-intersection differs from cross-type singleton marker intersections. With the same marker, their intersection has a nonempty X-part because A is intersecting, whereas cross-type intersections have none. Every case is excluded. Distinctness and the absence of any common point follow directly from the disjoint physical grounds and the two marker choices.

Start C_1 with one singleton, C_2 with the triangle, C_3=J(C_2,C_1) (eight triples), and C_4 with the **prior-art** intersecting half of H54 (27 edges). For k>=5 set C_k=J(C_(k-1),C_(k-2)). Exact cardinalities c_k obey

    c_3=8, c_4=27, c_k=2c_(k-1)+2c_(k-2).

Thus c_5,...,c_10 are 70,194,528,1444,3944,10776. Two disjoint physical copies of C_10 give a 3-free rank-ten original family of **21552** edges, and

    21552^4 > 54^10.                                  (LRC11)

This is an explicit obstruction to a decomposition of EVERY original into LRC5's H54-catalogue class with base 54^(1/4): if that decomposition existed, LRC5 would imply the opposite cardinality inequality. Shared-ground reuse of A across the two markers is essential; LRC5's private substitution does not license it. The auditor constructs every rank-ten edge and checks distinctness/rank/count; freeness at high ranks rests on the all-case proof, with exhaustive triple tests through rank five.

The characteristic root is lambda=1+sqrt(3), so this construction has exponential rate lambda>54^(1/4). Its proof and recurrence are reconstructed special cases of the older three-petal block/multiplication constructions discussed by Axante et al., section 3, not new mathematics-literature results. Axante's comparison also reports the stronger classical beta_3>=sqrt(10); that stronger construction is **source-reported and not reconstructed in this audit**. Therefore neither lambda nor 54^(1/4) is labelled the strongest known unrestricted lower rate.

There is a proved repair restricted to construction trees: close the s=3 LRC5 class under J with its two intersecting children, and replace B by B'=max(B,lambda). Indeed

    2(B')^(k-1)+2(B')^(k-2) <= (B')^k

because 2/B'+2/(B')^2<=1. Structural induction remains noncircular, and the base is sharp for this extended grammar by seed tensors and iterating J. This still supplies **no universal decomposition**. Source claims of still stronger rates are a warning that even the extended grammar must not be assumed exhaustive.

## LRC7. Two recurrence attempts, tests, and sources

**Attempt A: purify approximately separated packets and pay loss from rank.** LRC3 defeats inferring a small matching loss even from exp(-Theta(k)) relative error, singleton exceptional intersections, no common packet point, and nonvacuous density. Retaining a constant fraction still leaves an arbitrary original H^m occupying a linear fraction of rank. LRC4 identifies its capacity obligation exactly. A theorem with genuinely additional hypotheses remains possible; none is supplied here for arbitrary originals.

**Attempt B: decompose high-VC originals into rank-paid blocks.** LRC5 proves the recurrence for a supplied construction tree with independently bounded primitive seeds, even when the resulting VC dimension grows linearly. LRC6 gives an actual original counterexample to universality at the H54 catalogue base, then proves a larger-base repair for a grammar admitting shared-ground J. The missing all-F ingredient is a physical decomposition with bounded primitive-seed capacity and paid ownership/overlap; no such universal decomposition at a sufficiently large base is assumed or proved. LRC3's shattering example prevents replacing that ingredient by automatic bounded VC.

The independent stdlib auditor builds triangle-product shells, private original edges, all actual intersections, full small-case sunflower enumerations, explicit bad matchings and separate covers, minimum group-respecting purification by enumerating index choices, common-core and shattering checks. It tests s=3,4,6 on small actual families (enumeration capped by case size); H54/H39/H153 larger density uses independently established seed certificates and exact integer formulas, not an impossible enumeration of every 6-tuple. It checks both predecessor n~sqrt(m), n~m regimes and the new exponential-index formulas. Finite computations corroborate; the all-rank proofs above supply the quantifiers.

Sources rechecked 16 October: Mishra [v1](https://arxiv.org/html/2606.02667v1) (invalid full-shift original attribution, false unrestricted O_s(2^k) consequence for s>=4) and [v2](https://arxiv.org/html/2606.02667v2) (shifted only); [Axante et al.](https://arxiv.org/abs/2609.06175) recursive-construction prior art and finite H54/H39/H153 seeds; [Bell–Chueluecha–Warnke](https://arxiv.org/abs/2009.09327) general O(s log k) base; [Rao survey](https://londmathsoc.onlinelibrary.wiley.com/doi/full/10.1112/jlms.70380); bounded-VC [Ge–Wang–Xu–Zhao](https://arxiv.org/html/2609.18995v1) and [Shangguan](https://arxiv.org/abs/2609.30263), whose constants depend on VC dimension. The publisher DOI endpoints were inaccessible during this check; Bell's primary arXiv abstract and Rao's publisher search record were available. Related substitutions are prior art; **no literature-first claim** is made for this packaging. Earlier exact LP intervals remain 16<=V_3(T^2)<=34 and 11<=V_3(S tensor Q9^2)<=26. **NO complete proof. Full original sunflower conjecture OPEN.**
