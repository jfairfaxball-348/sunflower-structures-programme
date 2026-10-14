# Dense graph tensor obstruction to ancestor-free rank reduction (14 October 2026)

**Status: proved elementary statements, supported by finite tests. Not a proof of the full Sunflower Conjecture; no claim of literature novelty.** The rank-two graph extremal problem with bounded degree and matching was studied well before this project (see SOURCE_REGISTER). This note's purpose is a correctly quantified adversarial test for the particular Mishra compression bridge.

Write q=s-1>=2. A family is s-free when it has no s distinct original edges with identical pairwise intersections, including empty core. The ground-set ordering specified below is part of the compression statement.

## I. Explicit exponential-density factors

**Theorem 1 (graph factors).** For every integer q>=2 there is an explicit simple graph H_q, regarded as a 2-uniform family, such that tau(H_q)=q and

    |H_q| = M_q =
       q(q+1)                  if q is even,
       q^2+(q-1)/2             if q is odd.

Thus b_q=sqrt(M_q)>q. In particular (q,M_q)=(2,6),(3,10),(4,20),(5,27).

**Even q construction.** H_q is the disjoint union of TWO complete graphs K_(q+1). It has 2*binom(q+1,2)=q(q+1) edges and maximum degree q. A matching meets each component in at most q/2 edges, hence its matching number is at most q.

**Odd q construction.** Use vertices u,v, q-1 leaves a_1,...,a_(q-1) attached to u, q-1 disjoint leaves b_1,...,b_(q-1) attached to v, and a spare vertex w. Include uv. These 2q-1 double-star edges use 2q+1 vertices. On the residual vertex set R={a_i,b_i,w} of size 2q-1, place a (q-1)-regular circulant: enumerate R cyclically and join cyclic distances 1,...,(q-1)/2. It has (2q-1)(q-1)/2 edges, and is disjoint from all double-star edges. The graph has q^2+(q-1)/2 edges; u,v and all leaves have degree exactly q; w has degree q-1. There are only 2q+1 vertices, so no matching of size q+1 exists.

In any 2-uniform simple family, an s-sunflower (s>=3) is either an s-star with common one-vertex core or an s-matching with empty core. The common core cannot have size two because original edges are distinct. The degree and matching bounds thus give tau(H_q)<=q in both cases. A degree-q vertex supplies a genuine q-petal star, so equality holds.

## II. Exact tensor preservation of sunflower number

**Lemma 2.** For nonempty simple uniform families F_1,...,F_m on pairwise disjoint ground sets, their tensor product (all unions of one original member from each family) obeys

    |F_1 tensor ... tensor F_m|=product_i |F_i|,
    tau(F_1 tensor ... tensor F_m)=max_i tau(F_i).

**Proof.** The cardinality follows by unique projection to the disjoint coordinate blocks. A sunflower of t>=2 distinct tensor members has constant pairwise intersection *in each block separately*. In a given block, either all t projections are identical or all t are distinct: if two projections coincide at A, their pairwise intersection is A; every further projection B must have intersection A with A, so A subset B; uniformity in that block forces B=A. Hence, if the global tensor petals are distinct, at least one block gives t distinct projections which themselves form a sunflower in F_i; therefore t<=max_i tau(F_i). Conversely fix all but one block and choose a maximum sunflower in a factor. Singleton factors and the t=1 boundary are immediate. QED.

For any m>=1 let F_(q,m)=H_q^{tensor m}. Its uniformity is K=2m and

    |F_(q,m)| = M_q^m = b_q^K,        tau(F_(q,m))=q.

These are ORIGINAL sets and form a legitimate s-free family for s=q+1. For q even this improves on the q^K lower product by the factor ((q+1)/q)^m; for odd q it improves by (1+(q-1)/(2q^2))^m. The explicit formula does NOT assert M_q is the absolute extremal graph size for all q.

## III. A compression lemma that tolerates all extra edges and collisions

**Lemma 3 (partial-spoke propagation).** Let K>=2, n>=K+1 and F be ANY simple K-uniform family on ordered [n]. Assume [K] is a member and X is a set of r distinct vertices greater than K such that, for each x in X, some l_x in [K] satisfies

    ([K]\{l_x}) union {x} in F.

Run all standard simultaneous Frankl C_ij shifts once in lexicographic order: increasing i, then increasing j. After the full pass the shifted image has at least r+1 distinct members containing [K-1], hence an (r+1)-sunflower with that core. The same lower bound persists under ANY subsequent sequence of elementary compressions.

**Proof.** For x with l=l_x<K, set B_t(x)=([K]\{t}) union {x} for t=l,...,K. The original B_l(x) includes [l-1]; shifts with first index i<l cannot change it. At the start of phase i=t, B_t(x) is present by induction and contains [t-1], making previous phases inert. The first shift of phase t is C_(t,t+1), which either changes B_t(x) into B_(t+1)(x), or leaves B_t(x) alone because B_(t+1)(x) was *already present in the old family*. In both situations B_(t+1)(x) is present afterwards and contains t; none of the remaining shifts with first index t can remove it. Therefore B_K(x) is present at the end of phase K-1. When l_x=K, B_K(x) was present initially and, containing [K-1], is unaffected by all phases i<K. Also [K] itself is present throughout these phases. Their r+1 distinct [K-1]-star edges exist after phase K-1. Later shifts have first index i>=K; every move of an edge containing [K-1] still contains that core, and old-family collision handling ensures the shift is an injection on the whole family. Hence the number of core-containing edges cannot decrease. The same argument works for any later shift: if i<=K-1, the core edges contain i and cannot move; otherwise they retain the core. QED.

Note: the star members need not keep the same *last vertices* under later shifts if they do not fill a complete star. The theorem only asserts its cardinality, and is careful not to invent unique original ancestors.

## IV. Explicit labellings and forced shift inflation at exponential density

**Theorem 4.** For each fixed q>=2 and each m>=1 there is an ordering of the (2m)-uniform original family F_(q,m) from Lemma 2 such that its lexicographically shifted image G satisfies

    tau(G) >=
       m(q-1)+1                (q even),
       2m(q-1)+1               (q odd).

**Odd q proof.** In factor t (t=0,...,m-1), label the baseline edge uv by the two central vertices l=2t+1 and l'=2t+2 of [K], K=2m. For a=1,...,q-1 label b_a, which is adjacent to v, by l+aK, and label a_a, adjacent to u, by l'+aK. Label the spare vertices after [qK]. The tensor of all baseline edges is [K]. For each l in [K] and each a, changing the corresponding center to its labelled leaf gives ([K]\{l}) union {l+aK}, an original tensor member. This is precisely the sparse spoke T(q,K) embedded in the original tensor family, so Lemma 3 gives 1+K(q-1) star edges. The other graph edges do not invalidate the argument.

**Even q proof.** In each first K_(q+1) component choose adjacent baseline vertices u_t,v_t and label them 2t+1,2t+2 in [K]. There are q-1 other vertices w_(t,a) in that clique; give all of them DISTINCT labels >K, and place all remaining vertices after them. The original tensor baseline [K] and the m(q-1) one-coordinate replacements of u_t by w_(t,a) all exist. Lemma 3 gives at least m(q-1)+1 core-star edges. The fact that a neighbour of u_t is also adjacent to v_t does not matter; we never identify two different labelled spoke vertices.

Each G contains a sunflower with at least c_q*K+1 petals for positive c_q (=(q-1)/2 for even q, =q-1 for odd q), while tau(F)=q and |F|=b_q^K. All constants and vertex labels are explicit. No such inequality is claimed for every shifting schedule; it is proved for the stated lexicographic schedule.

**Corollary 5 (density-restricted transfer no-go).** Fix s=q+1 and any 1<D<=b_q. There cannot exist a constant A_s(D) bounding the shifted sunflower number by A_s(D)*K/log(K+2) for ALL original s-free K-families of size at least D^K and all even K: the F_(q,m) have that size and produce tau(G)=Omega_s(K). This rules out this particular density-restricted resurrection of H_s through base b_q, NOT a hypothetical density threshold D>b_q, and NOT an ancestor-compatible rank induction.

## V. Inverse compatibility remains a separate mathematical obligation

The r+1 star petals from Lemma 3 are not generally an original sunflower. The q-free original family F_(q,m) has tau exactly q, so any partition of this produced star into classes that each form a genuine sunflower of original ancestors must use at least ceil((r+1)/q) classes. This is linear in K in these examples (not a constant-sized palette). No general graph-colouring theorem or positive inverse transfer follows; this is a sharp limitation for that specific kind of compatibility certificate.

For sparse binary T(2,K), distinct one-coordinate spokes E_i and E_j (i != j) intersect in [K]\{i,j}, a distinct set for each unordered pair; hence even raw original pairwise-intersection labels can involve binom(K,2) patterns.

## VI. Validation and direction

The independently executable program scripts/dense_obstruction_audit.py checks sizes, degrees, forbidden sunflowers in small factors/tensors, exact tensor counts, explicit orderings and full lex compression. The symbolic proofs, not the finite tests, justify arbitrary K.

**Hostile limitations:** This note supplies lower constructions and an obstruction, not a bound for large arbitrary families. No density-sensitive heavy-link theorem, original-witness-compatible rank recursion or unrestricted C_s^K upper bound has been proved. New work should try a quantified structural dichotomy only above the stronger b_q density floor, and independently test any proposal against these tensor factors and partial-spoke collisions.
