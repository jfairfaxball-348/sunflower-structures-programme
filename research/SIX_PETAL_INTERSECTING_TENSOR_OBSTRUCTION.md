# Original intersecting extraction and six-petal dense shifting obstruction (14 October 2026)

**Status: PROVED symbolic consequences of established finite factors and the collision-safe partial-spoke shift lemma. NO proof of the unrestricted sunflower conjecture.** The 153-triple factor is **published prior art**: Axante, Budala, Chitic, Dumitru and Nacu, *Sunflower-Free Uniform Families: Recursive Constructions and Explicit Bounds*, arXiv:2609.06175v1, §7.1. Its anchored lex-shifting and intersecting restrictions are the mathematical analysis performed here; no independent novelty claim has been established. Earlier anchored-factor theorem: [HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md](HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md). Earlier collision-safe shift lemma: [DENSE_ANCESTOR_OBSTRUCTION.md](DENSE_ANCESTOR_OBSTRUCTION.md), Lemma 3.

## 1. An exact original-family reduction to intersecting families

Let f_s(k) be the maximum cardinality of a simple s-sunflower-free k-uniform family, and let i_s(k) be the maximum cardinality among such families that are additionally **pairwise intersecting**. For every s>=3 and k>=1,

    i_s(k) <= f_s(k) <= (s-1) k i_s(k).                           (1)

**Proof.** Take a nonempty s-free family F. Any matching is an empty-core sunflower, so a maximal matching has t<=s-1 edges. The union U of these t edges, of size <=(s-1)k, intersects **every** member of F. Order U and assign each edge of F to its first vertex in U. The class assigned to x is an original subfamily of F, all of whose edges contain x, hence it is intersecting and s-free. Each class has at most i_s(k) edges, yielding (1). Empty F is trivial. QED.

Consequently the fixed-s exponential-growth question is *logically equivalent* in the full and intersecting settings. Indeed i_s(k)<=f_s(k)<=qk i_s(k), q=s-1, so their k-th root limsup and liminf coincide (possibly +infinity). In particular, an independently proved inequality i_s(k)<=A_s^k would imply f_s(k)<=qk A_s^k<=(2q A_s)^k for k>=1. Conversely the full conjecture trivially implies the intersecting bound. **This is NOT a new solved exponential bound; it relocates the central obstruction.** Maximal-matching support and star partitioning are elementary, and literature priority for this observation has not been determined.

**Exact trace refinement.** For any original E in F and EVERY T proper subset E, INCLUDING T=empty, the residue class R_T={A\T : A in F, A∩E=T} has matching number <=s-2. Otherwise s-1 disjoint residues, adjoined to their fixed trace T, form an s-sunflower together with E, with core T. For T=empty this is an empty-core sunflower, and R_empty retains rank k. Every R_T is s-free. Earlier notes unnecessarily restricted the matching assertion to nonempty T. This correction does not by itself lower rank: the empty-trace class is still rank k, and summing all 2^k classes still has prohibitive losses.

## 2. The published 153-member six-petal-free rank-three factor

Work in Z/14Z, with nine triple seeds

    015, 016, 017, 019, 01(10), 0(10)(12), 026, 029, 02(10).

Let H be all 14 cyclic translates of each seed. They lie in distinct translation orbits: |H|=126. On disjoint vertices 14,...,24 representing Z/11Z, form the graph G with edges {i,i+1}, {i,i+2} for every i modulo 11, and {i,i+5} for 0<=i<=4. Add a new vertex c=25 and let J={{c,u,v}: {u,v} in G}. Then |G|=|J|=27 and H,J have disjoint supports. Set P=H union J, a simple 3-uniform family of size 153.

**Complete s=6 exclusion, independent of tensor experiments.**
- An empty-core 6-sunflower is six disjoint triples. H lives on 14 points and has matching number <=floor(14/3)=4; J has matching number <=1 because each member contains c. Thus nu(P)<=5.
- A two-point-core six-sunflower would require pair codegree >=6. In H the pair codegrees are 5 for cyclic distances 1,2,4,5,6, zero for distance 3, and 4 for distance 7. In J, codegree at {c,u} is degree_G(u)<=5; pairs {u,v} have codegree 1. No pair straddles the disjoint supports. Thus all codegrees <=5.
- A one-point-core six-sunflower is a matching of size six in a vertex link. For x in H, its link graph has only 11 non-isolated vertices: x+3 and x-3 are isolated, so matching number <=5. For x=c the link is G on 11 vertices, also matching number <=5; for other x in J all link edges share c, so matching number <=1.

Therefore P contains NO original six-sunflower. Its maximum sunflower number is exactly five, because a pair in H has codegree five.

**Nine original one-swap outsiders.** Choose B={0,1,10} in H. Distinct outsiders

    X={2,3,5,6,7,8,9,11,12}

all occur as one-vertex replacements of B in H, as the following explicit original edges show:

    x : 2       3        5       6       7       8        9        11        12
    A : 1,2,10  1,3,10   0,1,5   0,1,6   0,1,7   0,8,10   1,9,10   1,10,11   0,10,12

Each listed triple belongs to the nine-seed cyclic construction; each meets B in exactly two points, and A\B={x}. This is a finite list of actual original witnesses, not a claim about compressed ancestors. The two outsiders 4 and 13 are not needed.

Apply the already-proved anchored-factor theorem to P, with w=3,h=153,r=9. For m>=1 set F_m=P^(tensor m). Then

    K=3m, |F_m|=153^m=(153^(1/3))^K,
    tau(F_m)=5, tau(lexshift(F_m))>=9m+1=3K+1.             (2)

The prescribed ordering puts all m baseline copies B first, then all nine distinct outsiders per coordinate, then the remaining vertices. Collision-safe propagation, rather than any unique-ancestor assumption, proves (2). The sunflower number five follows by tensor preservation and the five-petal pair core above.

This **refutes** any universal density-restricted estimate tau(lexshift(F))<=A_6(D) K/log(K+2) for every fixed D with 1<D<=153^(1/3) (approximately 5.34848), even though originals are six-free. This improves the earlier rank-two obstruction floor sqrt(27) (approximately 5.19615). It neither refutes a different order nor supplies an upper bound on f_6(K).

**Exact shadow/link diagnostics.** For P, the 2-shadow codegrees have histogram

    codegree 1 : 27 faces (pairs inside G),
    codegree 4 : 8 faces (7 opposite-distance pairs in H; {c,10} in J),
    codegree 5 : 80 faces (70 distance-1,2,4,5,6 pairs in H; 10 {c,u} in J).

Hence |partial P|=115, sum degrees=27+8*4+80*5=459=3*153, and maximal point degree is 27 (14 H vertices degree 27 and c degree 27, others <=5). For F_m, each (K-1)-shadow comes from exactly one coordinate and preserves its codegree:

    |partial F_m|=m*115*153^(m-1),
    histogram=(27,8,80)*m*153^(m-1) at codegrees (1,4,5),
    max_x deg_(F_m)(x)=27*153^(m-1)=(3/17)|F_m|.

In particular 80/115 of all shadows are saturated at the allowed q=5 extension multiplicity, but their mean is 459/115<5. **Do not falsely claim complete shadow-incidence equality** for s=6; that equality was special to the s=3 54-edge factor.

## 3. Intersecting original families also defeat naive density-restricted inverse shifting

**Star-restriction theorem (PROVED).** Let Q be a simple s-free w-uniform factor with h>0 edges, one anchor B, and r>=1 distinct one-swap outsiders as above. Fix x in B and let d=deg_Q(x)>0. For each m>=2, restrict the first coordinate of Q^(tensor m) to the original link-star {A in Q:x in A}; keep all other m-1 coordinates unrestricted. Call the resulting w m-uniform family I_m. Then

    |I_m|=d*h^(m-1)=(d/h) (h^(1/w))^(wm),
    I_m is pairwise intersecting and s-sunflower-free,
    tau(lexshift(I_m))>=r(m-1)+1.                        (3)

**Proof.** All members contain the first-coordinate copy of x; hence intersect. It is a subfamily of the s-free tensor, so is s-free. Counting independent factors gives d*h^(m-1). The baseline B in all m coordinates belongs to I_m because x∈B. The one-swap edges coming from coordinates 2,...,m are still in I_m, giving r(m-1) distinct outsiders, independent of the restricted first coordinate. Order the baseline copies as [wm], their outsiders afterward; the earlier collision-safe partial-spoke lemma yields (3) and persistence under subsequent shifts. QED.

For any fixed 1<D<h^(1/w), and sufficiently large m, |I_m|>=D^(wm) while its shifted sunflower number grows linearly in K=wm. The **strict** D<h^(1/w) is essential: d/h<1 normally means the intersecting restriction falls BELOW the exact endpoint D=h^(1/w). No endpoint claim is made for these restricted constructions.

Applied to P with x=0 in B, d=27 and r=9:

    |I_m|=27*153^(m-1)=(3/17)*153^m, tau(I_m)=5,
    tau(lexshift(I_m))>=9(m-1)+1=3K-8, K=3m>=6.

Applied to the earlier 54-edge s=3 factor (d=12,w=4,r=2), or 39-edge s=4 factor (d=9,w=3,r=1), this independently yields intersecting counterexamples at every fixed density strictly below 54^(1/4) or 39^(1/3), respectively. For s=6 it reaches every fixed density below 153^(1/3).

This obstructs **only** an original-intersecting-to-shifted sunflower-*number* transfer. It does not obstruct independent original-intersecting *size* bounds, nor prove any actual C_s^k theorem. The exact reduction (1) says an independent exponential bound for intersecting families WOULD solve the unrestricted conjecture; this remains the key noncircular problem.

## 4. Finite validation and unresolved central gap

The diagnostic script and tests independently enumerate P, its pair degrees and vertex-link matchings, verify nine original one-swap witnesses, and check a complete rank-three Frankl lex pass has >=10 core-star edges. No finite computation establishes (2) or (3) for arbitrary m: those are consequences of the written symbolic tensor and shift lemmas.

**FALSE paths:** full-shift sunflower-number transfer through the new six-petal floor, even after imposing intersecting originals (strictly below the floor); treating every trace class as a rank drop; bounded inverse-source palette; pretending the heavy-link threshold criterion is independent of the target.

**OPEN:** a ground-set-independent fixed exponential upper bound for *original intersecting* s-free k-families (equivalent by (1) to the full conjecture), or a genuinely compatible original rank reduction with fixed cost. Any proof must retain the original petals and explicitly absorb every loss in C_s^k. No complete proof has been obtained.
