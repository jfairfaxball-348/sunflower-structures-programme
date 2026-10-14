# Original intersecting multiwitness trace rank reduction (14 October 2026)

**Verdict: PROVED elementary original-family structural lemma, sharp local examples; full Erdős–Rado conjecture OPEN.** This is an independently derived argument for this programme; no claim of literature novelty or publication priority. It does NOT convert Mishra v2 shifted-only bounds to the unrestricted problem.

## Definitions

Let s>=3; F is a finite simple, pairwise-intersecting, s-sunflower-free k-uniform family. Define f_s(j) as the maximum size of any s-free j-uniform original family, f_s(0)=1. Set f_s(j)=0 for j<0 solely for the formulas below. All sunflowers have distinct originals and exact common pairwise intersection, possibly empty.

For E in F and U subset E, write F(E,U)={B in F:B intersect E=U}. When F is intersecting, F(E,empty)=empty. Every proper trace residue already has matching number <=s-2 by the previous exact-trace lemma; this note adds COMPATIBILITY between separate traces, not merely individual matching bounds.

## Theorem A — disjoint outside witnesses force rank descent (PROVED)

Suppose E=T disjoint_union V belongs to F, where |V|=h>=1 and |T|=k-h>=1. Suppose also that A_i=T disjoint_union W_i belongs to F for 1<=i<=r, where each W_i has size h, lies outside E, and the W_i are pairwise disjoint. Then necessarily 1<=r<=s-2, because E,A_1,...,A_r are an (r+1)-sunflower with common core T.

For each nonempty U subseteq V, with u=|U|, put N_U=|F(E,U)|. If k-u<r, then N_U=0. Otherwise

    N_U <= h^r f_s(k-u-r).                                    (A1)

Consequently the complementary trace mass

    D(E,V) = |{B in F : empty != B intersect E subseteq V}|

satisfies the genuine ORIGINAL-FAMILY rank recurrence

    D(E,V) <= h^r sum_{u=1}^h binom(h,u) f_s(k-u-r),           (A2)

with the convention f_s(negative)=0.

**Proof.** Fix B in F(E,U). Since U subset V=E\T, B misses T. But B must intersect EACH A_i (F is pairwise intersecting). Thus B intersects W_i. Choose one x_i in B intersect W_i for every i. The W_i are disjoint, so all chosen x_i are distinct; there are at most h^r possible ordered tuples (x_1,...,x_r). Partition F(E,U) by a deterministic choice tuple (e.g. first point within an ordering of each W_i). For a fixed tuple, every member contains the fixed disjoint set U union {x_1,...,x_r} of size u+r. Removing it injectively produces a simple original s-free (k-u-r)-uniform family: if residues had an s-sunflower, adjoining this SAME fixed set to all members would create an s-sunflower in F, with the correspondingly enlarged exact core. Each tuple class has at most f_s(k-u-r) members. If k-u<r no member can meet all W_i. Sum the at most h^r classes to get (A1), then sum disjoint exact traces U for (A2). No compression, inverse-source guesses, ambient n, or positivity-of-shadow-slack assumptions occur. QED.

**Important quantifier restriction:** A1 counts only opposite traces U subseteq V for a SPECIFIC compatible witness configuration. There is no proof that most edges lie in these traces, nor a fixed-base recurrence for all F. This conditional bound is not the full sunflower conjecture.

## Theorem B — one-swap sharpness and original two-core (PROVED)

Set h=1, E=T union {v}, A_i=T union {x_i} for r distinct outsiders, 1<=r<=s-2. Any B with B intersect E={v} must contain all r outsiders (by intersecting every A_i) and v. Thus

    |F(E,{v})| <= f_s(k-r-1) when r+1<=k,
    F(E,{v})=empty when r+1>k.                               (B1)

This is a rank-(r+1) drop at coefficient EXACTLY ONE, with genuinely original witness sets.

**Sharp family for every s>=3 and 1<=r<=s-2.** Take k=r+2, a T of r+1 points, v outside T, r distinct x_i outside E, and s-1 distinct additional points y_j. Define

    E=T+{v};  A_i=T+{x_i}  (1<=i<=r);
    B_j={v,x_1,...,x_r,y_j}  (1<=j<=s-1).

These k-uniform edges are all distinct and pairwise intersect: E meets A_i in T and B_j in {v}; A_i meets A_l in T and B_j in {x_i}; B_j meets B_l in {v,x_1,...,x_r}. Each category of repeated intersections has at most s-1 members: the E,A_i sunflower has r+1<=s-1 edges and the B_j sunflower has s-1 edges. A purported s-sunflower mixing categories cannot have equal pairwise intersections: E/B gives {v}, A_i/B gives {x_i}, A_i/A_l gives T, and B_j/B_l gives {v,x_1,...,x_r}; these are distinct when applicable, while any subset with at most one member from each category has too few members for s. Therefore F is s-free. The exact opposite class comprises precisely the B_j and has size s-1=f_s(1)=f_s(k-r-1). Thus coefficient 1 cannot be uniformly improved, even though this provides NO global f_s(k) bound. Exhaustive checks cover s=3,4,5,6 with r=s-2.

## Cross-trace edge energy (PROVED; not sufficient for induction)

For pairwise-intersecting F and any E in F, take two disjoint active traces U,V subset E (U intersect V=empty). For every A in F(E,U) and B in F(E,V), intersection A intersect B lies OUTSIDE E. Let d_U(x)=|{A in F(E,U):x in A}| for x outside E. Counting each cross pair at least once gives

    |F(E,U)| |F(E,V)| <= sum_{x outside E} d_U(x) d_V(x).    (C1)

For each nonempty cross class, any fixed A in F(E,U) supplies the independent bound

    |F(E,V)| <= (k-|U|) f_s(k-|V|-1).                       (C2)

The proof of C2: all B in V-class intersect the (k-|U|)-point outside residue of A, so partition by one of those points and remove that point plus V. For |U|=k-1 the coefficient is one. Both statements are n-independent, but summing C2 over unrestricted traces would reintroduce k-dependent multiplicities; (C1) is a necessary compatibility condition, not an upper theorem of constant exponential base.

## Interaction spectrum / tensor-compatible moment diagnostic (PROVED identity)

For uniform family Q with N>0, define the polynomial

    Z_Q(z)=N^(-2) sum_{A,B in Q} z^(|A intersect B|)

with ordered pairs, including A=B. For disjoint-block tensor products Q tensor R,

    Z_(Q tensor R)(z)=Z_Q(z) Z_R(z).

This follows since intersections add independently across blocks. In particular E|A intersect B|=Z'_Q(1) grows additively over tensor powers, while the coefficients of Z describe exact coincidence classes; no positive gap is inferred from moments alone.

For the **PUBLISHED**, 153-member, six-free rank-three factor P from Axante et al. §7.1, finite independent enumeration gives its ORDERED intersection histogram at sizes 0,1,2,3:

    (14210,7350,1696,153);  sum=153^2=23409,

so

    Z_P(z)=(14210+7350*z+1696*z^2+153*z^3)/23409
    Z_(P tensor m)(z)=Z_P(z)^m
    E|A intersect B|=m*11201/23409.

The point degree histogram (4:1,5:10,27:15) verifies 11201=sum_v deg(v)^2. Shadow histogram (1:27,4:8,5:80) is as previously published in our six-petal audit; unlike the 54 rank-four three-free factor, P does NOT saturate all shadows. This moment diagnostic alone neither separates s-free from sunflower-rich families nor yields a constant-base upper bound.

## Adversarial limitations and small-rank bookkeeping

1. Pairwise-intersecting is ESSENTIAL. For the published P, E={0,1,10} has four distinct one-swap witnesses for each removed vertex v=0,1,10, but ALSO 18 other triples with exact trace {v} for each v. They are allowed because P is not pairwise intersecting. Applying (B1) to P would be invalid: four forced outsiders plus v cannot fit in rank three. Its star-restricted tensor IS intersecting, but opposite trace sets avoiding its common fixed vertex are empty; local compatibility does not give global mass control.
2. At k=1, i_s(1)=1 while f_s(1)=s-1; a one-point family cannot contain two distinct intersecting singleton originals. At k=2, i_s(2)=max(s-1,3): every intersecting simple graph is a star or a triangle. A star has at most s-1 edges, triangle has three edges and is s-free for s>=3. This exact low-rank result is classical and not original research. For k=3, the elementary bound i_s(3)<=3 f_s(2) follows by fixing an original triple E and covering F by its three links; this is NOT an exact formula and does not iterate with fixed coefficient. Published rank-three values and improved bounds are documented in SOURCE_REGISTER.
3. Strong witness-sunflowers have r<=s-2. For h=1 the exciting rank-drop r+1 is at most s-1, but for arbitrarily high k it applies to only ONE complementary singleton trace, potentially of negligible total size. The h^r loss for h growing with k can destroy any fixed-base induction.
4. The star-restricted 54/39/153 factors and q-ary products do not contradict (A1); the theorem speaks about opposite traces disjoint from the witness core, while the star restriction has an unavoidable fixed shared point. No improved global sunflower exponent or novel finite factor is claimed.

## Next decisive question

Can one prove that in a sufficiently dense ORIGINAL intersecting s-free family, **many** edges are controlled by a bounded collection of compatible near-face witness configurations whose A2 errors are globally absorbable (each edge charged O_s(1) times), or build an explicit high-density tensor counterexample to this proposed cover? Find an exact coefficient recurrence, demonstrate honest induction for k=1,2,3, and test density floors 54^(1/4),39^(1/3),153^(1/3). Neither the existence of such a cover nor its balance is currently known.
