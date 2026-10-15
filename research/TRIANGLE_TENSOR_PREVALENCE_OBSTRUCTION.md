# Triangle-tensor obstruction to bounded-trace witness prevalence (15 October 2026)

**Verdict: PROVED structural counterexample to a specific ORIGINAL-witness prevalence and bounded-anchor-cover mechanism. NOT a proof of the full Erdős–Rado Sunflower Conjecture.** The elementary tensor deduction is checked independently here; neither the classical finite factors nor their literature novelty is claimed. The original compatible trace theorem remains true.

## Definitions and the exact proposed theorem

Let F be a finite simple intersecting s-sunflower-free k-uniform family (s>=3). An anchored compatible packet consists of E=T disjoint_union V and r original witnesses A_i=T disjoint_union W_i, where h=|V|=|W_i|>=1, 1<=r<=s-2, W_i are pairwise disjoint and outside E. The previous Theorem A bounds only the **opposite trace mass**

    D(E,V)=|{B in F : empty != B intersect E subseteq V}|.

Every member counted here has |B intersect E|<=h. Thus for each anchor E and ANY number of compatible packets with h<=H, the union of their covered members lies inside

    L_H(E)={B in F: |B intersect E|<=H}.                 (1)

Our new obstruction applies to (1), whether packets actually exist or not. This is stronger than testing one particular witness geometry.

## Theorem 1 — exponentially dense, core-free intersecting tensor obstruction (PROVED)

Fix s>=3, a finite nonempty simple s-free w-uniform family Q with a>=2 members, and integer m>=1. Let T be the three two-element edges of a triangle on disjoint vertices 0,1,2. Use disjoint copies Q_1,...,Q_m. Define

    I_m = T tensor Q_1 tensor ... tensor Q_m,
    k=2+wm, |I_m|=3a^m.                                   (2)

Then I_m is simple, s-free, pairwise intersecting, and has **empty global intersection** (no point belongs to every edge). Moreover, uniformly for EVERY anchor E in I_m and integer H>=0,

    |L_H(E)|/|I_m| <=
      Pr[Bin(m,1/a) <= floor(H/w)]                         (3)

and a strengthened version holds with floor((H-1)/w) on the right, since every two triangle edges meet in at least one vertex.

For fixed H (or H=o(m)), the right side tends to zero exponentially. For fixed H the explicit bound is

    sum_{j=0}^{floor((H-1)/w)}
        binom(m,j) a^(-j) (1-1/a)^(m-j)
      = O_{a,w,H}(m^H (1-1/a)^m).                          (4)

(For H=0 the left side is zero because I_m intersects.)

**Proof.** Every tensor member chooses a unique edge from T and one from each Q_j, giving (2) and uniformity. Different triangle edges intersect, so all I_m edges intersect; the intersection of all triangle edges is empty, and any global intersection of I_m would have to lie in a coordinate common to every choice. The triangle itself has empty intersection; for each coordinate of Q, if Q happened to have a common vertex this does NOT give empty global intersection. Therefore the empty-global-intersection claim requires Q to have empty global intersection (equivalently intersect all Q_j choices has empty intersection). Under this additional hypothesis, the conclusion holds. In general, delete the common core of Q before tensoring or restrict to Q with empty core. For all factors actually used below, Q has empty global intersection.

T has sunflower number 2: its three pairwise intersections are three different singletons. The disjoint-block tensor lemma proved in DENSE_ANCESTOR_OBSTRUCTION.md gives tau(I_m)=max(2,tau(Q))<=s-1. This uses original distinct sets and permits empty sunflower core. Fix an anchor E and choose B uniformly from I_m. In each block j, B_j equals the fixed E_j with probability 1/a, independently across j. Whenever equality occurs, |B_j intersect E_j|=w. Let X count such blocks: X~Bin(m,1/a). The triangle contributes at least one further intersection point, so |B intersect E| >=1+wX. The stated strengthened binomial bound follows. For H=o(m), a standard binomial lower-tail bound (or its elementary finite sum) gives an exponentially decaying probability; for fixed H, (4) follows termwise. QED.

**Correction to avoid an overstatement:** A universal arbitrary Q need not have empty global core; hence the theorem's core-free conclusion is stated only when Q does. All the 54, 39, 153 and q-ary factors below meet this restriction. The remaining properties and near-trace tail bound hold for any nonempty Q.

**Direct corollary (single-anchor prevalence FALSE).** For any fixed s,H,phi>0, there are arbitrarily high ranks k and intersecting s-free original k-families of exponential density, with empty global core, for which EVERY anchor E and EVERY collection of compatible packets of h<=H covers LESS than phi |I_m| members. It already fails for I_m with Q=P(s-1,1), yielding |I_m|=3(s-1)^m and limiting exponential base s-1. It also fails at every fixed density D<a^(1/w), in the sense |I_m|>=D^k for all sufficiently large m.

If L different anchors E_1,...,E_L each use arbitrarily many h<=H packets and their union covers >=(1-epsilon)|I_m|, then the union bound using (3) forces

    L >= (1-epsilon)/Pr[Bin(m,1/a)<=floor((H-1)/w)].     (5)

For fixed H, L must grow exponentially. This rules out any O_s(1)-anchor, fixed-fraction, bounded-trace cover at those exponential densities. It does **not** rule out highly nontrivial exponentially many-anchor amortisation schemes with per-edge bounded charges, or a theorem only at a higher density.

## Theorem 2 — exact q-product near-trace spectrum (PROVED)

Let q=s-1>=2 and Q be q disjoint singleton edges. Then k=m+2, |I_m|=3q^m, tau(I_m)=q, and the global core is empty. For a fixed anchor E, let N_H(E)=|{B:|B intersect E|<=H}|. Write c_j=binom(m,j)(q-1)^(m-j), with c_j=0 outside 0<=j<=m. Exactly

    N_H(E)= 2 sum_{j=0}^{H-1} c_j + sum_{j=0}^{H-2} c_j.  (6)

To prove (6), the two triangle edges differing from E intersect it in one point, and the identical triangle edge in two; precisely j out of m q-ary coordinates agree with E in c_j choices. In particular N_1(E)=2(q-1)^m and

    N_1(E)/|I_m|=(2/3)((q-1)/q)^m.                        (7)

This EXPLICITLY exhibits an exponentially small one-swap/opposite-singleton-trace reservoir without any common core, including q=2 where its absolute cardinality is just two.

## Theorem 3 — exact Abbott–Hanson 54-factor overlap and stronger s=3 obstruction

Take the PUBLISHED 54-edge, rank-four, three-free family H54, consisting of two disjoint 27-edge copies as documented in HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md. Each copy is intersecting, and two copies are disjoint. Therefore, for every E in H54, exactly 27 of the 54 edges intersect E: P_{B uniform H54}[B intersects E] = 1/2. Put I_m=T tensor H54^m, k=4m+2, |I_m|=3*54^m. Then

    |L_H(E)|/|I_m| <= 2^(-m) sum_{j=0}^{H-1} binom(m,j) (8)

for ALL E and H, since each block that chooses the same 27-edge support copy as E intersects E in >=1 point, and the triangle contributes >=1. For fixed H this is O_H(m^(H-1)2^(-m)), much sharper than the equality-indicator bound (3). All I_m are intersecting, three-free, empty-global-core original families and exceed D^(4m+2) for all large m and every D<54^(1/4). The endpoint D=54^(1/4) is NOT claimed: the prefactor 3/D^2 is below 1.

The ordered intersection polynomial for H54, verified by direct counting, is

    Z_H54(z)=(27+12 z+10 z^2+4 z^3+z^4)/54.            (9)

Indeed cross-copy ordered pairs (1458) have intersection zero; within-copy ordered histogram, over both copies, is 1:648, 2:540, 3:216, 4:54. Sum=2916=54^2. Z_H54'(1)=8/9, consistent with 18 vertices each degree 12. Triangle overlap polynomial is Z_T(z)=(2z+z^2)/3, so

    Z_I_m(z)=((2z+z^2)/3) * Z_H54(z)^m.               (10)

This is a precise moment counterexample to using high mean pair overlap as a *sufficient* indicator for extensive bounded opposite traces: expected overlap = 4/3+(8/9)m, even though the small-overlap reservoir is exponentially small.

## Independent factor baselines and limitations

The same Theorem 1 applies to the published 39-edge, rank-three four-free factor (Q=H39) and 153-edge rank-three six-free factor (Q=H153). Both have empty global intersection and at least two edges, independently checked in the cited factor notes. It gives core-free intersecting s-free counterexamples to fixed-fraction bounded-trace prevalence for ALL D<39^(1/3) (s=4) and ALL D<153^(1/3) (s=6), as well as all D<s-1 from one-coordinate q-ary products for arbitrary s. These are density floors for this *particular prevalence claim*, not claimed optimal sunflower-free densities. Finite factors are credited to Abbott–Hanson and Axante et al.; the tensor and overlap deductions are programme work, with NO external novelty audit established.

An unconditional proposed assertion for high-density input families of the form: for constants D,H,phi>0, all s-free intersecting |F|>D^k have some original E, compatible packet with h<=H and D(E,V)>=phi|F|, would itself **imply the full conjecture**. Indeed local Theorem A yields

    phi |F| <= H^(s-2) * 2^H * f_s(k-2)

using f_s(j) nondecreasing in j and u+r>=2. Thus |F|<=B f_s(k-2) with B=H^(s-2)2^H/phi. Choosing C>=D,sqrt(B), and finite base-rank values closes induction. Conversely a proved fixed-base sunflower bound makes such a high-density premise vacuously true by choosing D above the true base. Mere assertion of an unspecified threshold is therefore equivalent in logical difficulty, not a free novel proof.

**No positive original-family constant-base rank recurrence has been established.** A possible route must control the central (non-small) trace bulk, pay for many anchors with genuine amortisation, or employ a different certificate entirely. An absent common core and exponential input density ALONE do not create bounded-size opposite-trace mass.

## Validation

scripts/triangle_tensor_prevalence_audit.py independently reconstructs H54, verifies the exact ordered-overlap polynomial and per-anchor probability 1/2; enumerates triangle tensor q-products for q=2..5, m=1..5 and H=1..3 and checks (6). Its unittest is tests/test_triangle_tensor_prevalence_audit.py. Finite tests corroborate only the stated finite identities; the all-m claims above have symbolic proofs. No manuscript, novelty announcement, or full conjecture claim.
