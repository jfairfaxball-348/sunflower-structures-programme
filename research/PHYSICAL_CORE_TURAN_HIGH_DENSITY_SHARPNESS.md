# Arbitrarily dense ORIGINAL families saturate multi-packet physical-core Turán energy

16 October 2026. **TC1–TC4 PROVED internally**, finite physical-original cases audited independently by exact rational enumeration. The quantitative Turán theorem is CLASSICAL PRIOR ART. The shielding/tensor formulation is programme-local, with **EXTERNAL PRIORITY NOT CHECKED**; no new universal sunflower upper bound. The full unrestricted Erdős–Rado Sunflower Conjecture is **OPEN**. Mishra v1's cumulative shifted ancestor transfer remains invalid and its claimed universal O_s(2^k) conclusion is false for s>=4; v2 treats SHIFTED families only. No shifted sunflower is lifted to an original witness.

## TC1. A sharp many-packet ORIGINAL physical-core inequality (PROVED)

Let F be a finite simple s-sunflower-free ORIGINAL k-uniform family, s>=3, and let r>=s. Choose r pairwise ownership-disjoint nonempty packets P_1,...,P_r of actual original edges. Independently draw A_i from an arbitrary probability law mu_i supported on P_i. Every sampled A_i is a distinct ACTUAL original edge. Fix ANY genuine physical set D (empty D allowed), and put

    delta_ij(D) = Pr[A_i intersect A_j != D].

Then

    sum_{1<=i<j<=r} delta_ij(D) >= binom(r,2) - ex(r,K_s),     (TC1)

where ex(r,K_s) is the exact Turán maximum number of edges in an r-vertex K_s-free graph. For q=s-1 and r=qa+b, 0<=b<q,

    ex(r,K_s) = (r^2 - [b(a+1)^2 + (q-b)a^2])/2.            (TC2)

**Proof:** Condition on ONE actual independent draw (A_1,...,A_r). Form the graph G_D on label vertices [r] with ij an edge exactly when the ACTUAL pair intersection equals D. If G_D contained K_s, those s distinct original edges would be an actual s-sunflower with core D (the petals are distinct k-sets, hence nonempty residues), contrary to the hypothesis. Therefore e(G_D)<=ex(r,K_s) for every sampled tuple. The number of complementary pairs is at least binom(r,2)-ex(r,K_s). Taking expectations gives TC1. No matching of abstract trace classes, shifting, single common packet distribution, or unproved rank recurrence is involved. QED.

When r=s this recovers predecessor AP6. Averaging AP6 over s-subsets only gives binom(r,2)/binom(s,2), generally weaker than TC1 for r large. As r grows, TC1 forces an approximately 1/(s-1) share of bad pair intersections. This is a genuine, independent, original-owner many-label statement but it is an extremal-graph consequence, not a cardinality bound.

## TC2. High-density SHARPNESS simultaneously for TC1 and AP7 (PROVED)

Let q=s-1. Let H be ANY nonempty finite simple ORIGINAL s-free d-uniform family (d>=1, M=|H|), and let m>=1. Take q physically disjoint labelled copies H_g^{tensor m} of its true set-family tensor product; denote the physical ground of each copy X_g, with all X_g pairwise disjoint. For every g introduce an additional distinct real point x_g absent from all X_h. Optionally fix an independently disjoint real physical set D_0 of d_0>=0 points, shared by all edges. Define

    F_m(D_0,H) =
      union_{g=1}^q { D_0 union {x_g} union E : E in H_g^{tensor m}}.  (TC3)

Its members are ACTUAL physically named original sets, of rank k=d_0+1+dm and cardinality r=qM^m. The g-index is metadata and not a ground vertex; x_g really IS a ground vertex.

**Tensor fact:** The product of finite simple s-free uniform set families on disjoint physical coordinate grounds is s-free. Indeed in each coordinate, if s projected edges admit the same pair intersection, either all coordinate edges are identical or they are all distinct and form an s-sunflower. A mixed repeated/nonrepeated coordinate cannot have equal pair intersections because its equal pair intersects in the entire rank-d edge, while a distinct pair intersects in a proper subset. At least one coordinate is all-distinct if the full s product edges are distinct. This would force an s-sunflower in H. Therefore each H_g^{tensor m} is s-free.

**Sunflower-free proof:** Suppose s distinct edges from TC3 formed an original sunflower. If all are from one group g, deleting common physical D_0 and x_g would yield an original s-sunflower in H_g^{tensor m}, contradiction. Otherwise, since there are only q=s-1 groups, at least two sampled edges share some group g; their actual pair intersection contains x_g. At least one pair lies in different groups and has intersection EXACTLY D_0; these cannot be equal. Thus F_m is s-free for empty or nonempty sunflower cores, with genuine original owners. QED.

For the physical core D=D_0, each CROSS-group actual pair intersection is EXACTLY D_0, and each WITHIN-group actual pair intersection CONTAINS x_g and is not D_0. Taking r singleton packets with deterministic owner choices, G_D is therefore the COMPLETE BALANCED q-PARTITE TURÁN GRAPH, each class of size M^m. Hence

    sum delta_ij(D_0) = q binom(M^m,2)
      = binom(r,2)-ex(r,K_s).                               (TC4)

TC1 is exactly SHARP for arbitrarily large r, not merely asymptotically; all r packets are distinct original owners. In the i.i.d. uniform distribution on all r original edges, for the same physical D_0 every residue includes its real group marker x_g, while different group residues are disjoint. Consequently

    Pr[(A\D_0) intersect (B\D_0) != empty] = 1/q = 1/(s-1).  (TC5)

This exactly saturates predecessor AP7 for arbitrarily large, genuinely original, sunflower-free families. No strictly positive dimension-free or rank-free bonus can follow merely from many packet labels, pair-intersection graph/Turán energy, or conditional fixed-core AP7 energy, EVEN WHEN cardinality is exponentially high in rank.

Define beta_s=sup_{d>=1} f_s(d)^(1/d), where f_s(d) is the maximum cardinality of an original simple s-free d-uniform family, possibly unbounded. For EVERY real density D>1 with D<beta_s, choose d,H with M>D^d. With D_0 of any FIXED cardinality, the families TC3 satisfy

    |F_m| / D^(rank F_m)
      = [q / D^(d_0+1)] * (M/D^d)^m -> infinity.            (TC6)

They simultaneously have TC4 and TC5 equality at all m. This is a rigorous NONVACUOUS high-density counterexample to any hypothesis demanding UNIFORM STRICT TC1/AP7 improvement above a threshold D<beta_s. If D>=beta_s, a high-density premise is vacuous. This negative quantification does NOT show beta_s infinite and does NOT refute the main sunflower conjecture; it only eliminates a tempting route to it.

## TC3. Honest packet rank and an explicit high-density residual failure (PROVED)

With D_0 empty, take just the q genuine group packets, each anchored by its true PHYSICAL marker {x_g}. These own every original edge exactly once and delete rank r_a=1, giving

    Z_C = sum_{g=1}^q C^(-1)=q/C,
    |P_g| / C^(k-r_a) = (M/C^d)^m.                            (TC7)

Whenever q<=C<M^(1/d), these packets have budget Z_C<=1, but each actual original residual has arbitrarily large base-C occupancy; even an AP7 overlap probability exactly 1/q does not repair the induction. This noncircular demonstration falsifies a mechanism, not any candidate conjectural bound for larger C_s.

**Numerical previously published seed control:** for s=3 take the PRIOR-ART H54 original 3-free rank-four family with M=54, q=2 and C=5/2. Then k=4m+1, n=2*54^m, Z_(5/2)=4/5, and

    |P_g| / (5/2)^(4m) = (864/625)^m -> infinity.
    |F_m| / (5/2)^(4m+1) = (4/5)*(864/625)^m.

Every individual actual group pair intersects at least in x_g; every cross-group original pair is disjoint, so TC1 and AP7 are sharp at the same time. f_3(2)=6 is recovered as an equality case of TC1 from two disjoint physical triangles (rank-two pair-stars of size three); no claim of priority for this known finite factor. The H54 seed source is PRIOR ART, not a newly found extremal construction.

## TC4. Independent exact finite control, failed strategies and OPEN gap

The script scripts/physical_core_turan_sharpness_audit.py constructs actual points and distinct uniform original edges for seed H=P(2,1) or P(3,1), physically disjoint tensor copies, optional true D_0. It exhaustive-checks every s-subset for NO sunflower, computes every ACTUAL pair intersection for TC4, and verifies TC5 as an exact Fraction. Tested cases include (s,m,d_0,r,k)=(3,1,0,4,2), (3,2,0,8,3), (3,2,1,8,4), (4,1,0,9,2), (4,1,2,9,4). The rational H54/C=5/2 budget and exponential ratio are arithmetically checked but H54's original s-free property is inherited from the cited published seed and earlier project tests; this is NOT a new independent reconstruction of all 54 edges.

Rejected routes: (1) strengthen AP6 by averaging many labels and hope for a strict extra conditional-core defect at every high density; TC1 is the best universal Turán lower bound and TC6 attains it. (2) force overlap probability >=1/(s-1)+epsilon at a fixed D whenever |F|>D^k for nonvacuous D; TC5/TC6 disprove this for EVERY D<beta_s. (3) combine Z_C<=1 and exact AP7 as if original residual occupancies were <=1; TC7, including concrete base 5/2, refutes the inference. (4) use only i.i.d./uniform packet conditional variance: deterministic singleton packets already attain TC4, and uniform owner law attains TC5. All alternative approaches must couple DIFFERENT physical cores, use high-order original intersection structure, or independently control within-shield original residual capacity.

Mandatory adversaries remain P(s-1,k), H54/H39/H153, AS3/Q9 unresolved LP ranges 16<=V_3(T^2)<=34 and 11<=V_3(S tensor Q9^2)<=26, alternating shields, original pair-stars, W(N,m), nested NW1/AP1 all-physical anchors, and original ownership under shifts. No original-family f_s(k)<=C_s f_s(k-1), fixed-base multirank recurrence, or complete proof obtained.

Sources checked 16 October: Mishra https://arxiv.org/html/2606.02667v1 and https://arxiv.org/html/2606.02667v2; Axante et al. https://arxiv.org/abs/2609.06175; Bell–Chueluecha–Warnke https://doi.org/10.1016/j.disc.2021.112367; Rao https://doi.org/10.1112/jlms.70380; bounded-VC Ge–Wang–Xu–Zhao https://arxiv.org/abs/2609.18995 and Shangguan https://arxiv.org/abs/2609.30263. The latter two have dimension-dependent bases; they are not full original-family fixed-C_s solutions. Prior research AP1–AP7 in research/ALL_PHYSICAL_WREATH_COMPATIBILITY.md remains intact. **NO complete unrestricted proof. PRIORITY NOT CHECKED.**
