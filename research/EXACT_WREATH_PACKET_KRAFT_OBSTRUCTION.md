# Exact ORIGINAL multipoint packet budgets on pair-star wreaths — 15 October 2026

**Verdict: PROVED internally (conditional on the already documented WR1 original wreath construction); external priority NOT CHECKED.** This is a *sharp obstruction and a matching logarithmic-scale extraction on a specific class*, NOT a noncircular recurrence for every original family. The unrestricted Erdős–Rado sunflower conjecture is OPEN. Do not equate shifted images with original owners.

## MP1. Packet definitions and exact optimum (PROVED)

Fix s>=3 and any nonempty finite simple ORIGINAL s-sunflower-free d-uniform H, d>=1. Use the actual pair-star-shell wreath F=W_{N,m}(H) from [WR1](NONVACUOUS_WREATH_POINT_LINK_OBSTRUCTION.md), N>=3,m>=1: its actual distinct edges are A_i union E for E in the physically private copy T_i of H^m, with A_i={p_ij:j != i}, each p_ij a SINGLE physical point, T_i private across indices i. Set W=|H|^m. Then |F|=NW, rank k=N-1+dm, F is s-free for both empty and nonempty cores, and every actual point lies in at most 2W edges.

A *nonempty anchored packet partition* is a disjoint partition F=disjoint_union_{a=1}^L F_a into nonempty subfamilies, together with NONEMPTY physical-point anchors B_a subset intersection_{E in F_a} E. Put r_a=|B_a| and its rank-weighted cost Z_C=sum_a C^(-r_a) for real C>1. Deleting B_a maps the ORIGINAL packet injectively to an ORIGINAL s-free (k-r_a)-uniform residual family: equal residuals would imply equal original edges and an s-sunflower of residuals would lift by reattaching the same B_a. This is not a shift/lift hypothesis.

**Theorem MP1 (exact bounded-anchor Kraft optimum):** If 1<=R<=N-1 and every r_a<=R, then

    min_{all such genuine original packet partitions} Z_C
       = min_{0<=j<=floor(N/2)}
              [ j/C + (N-2j)/C^R ].                        (MP1)

The minimum is achieved by j disjoint *pair-group packets* F_i union F_l with common physical anchor {p_il} of rank one, plus N-2j *single-group packets* F_i each anchored by ANY R distinct points of A_i. This partitions all original owners exactly once, leaves lower-ranked simple s-free residuals, and needs no invented group-index vertices. When C^(R-1)<2, optimal j=floor(N/2); when C^(R-1)>2, j=0; at equality either is optimal.

**Proof of the lower bound (the important part):** A packet touching two distinct groups i,j has nonempty B_a subset A_i intersect A_j={p_ij}, because the private grounds are disjoint. Consequently B_a={p_ij}, r_a=1, and it touches **at most two** groups: a third A_l does not contain p_ij. Every other packet touches exactly one group and costs at least C^(-R). Ignore the number of edges from each group used by a packet: the collection of one- and two-group *supports* of ALL packets covers the entire N-element group-index set. By deleting redundant supports and replacing any pair covering only one previously uncovered group with a singleton (cost C^(-R)<=C^(-1)), a cheapest cover consists of j mutually disjoint pairs and N-2j singles. Its cost is the right side of MP1 and cannot exceed the original partition's cost. Conversely the stated explicit original packets attain every term. This exact set-cover reduction remains true for arbitrary correlated/private s-free inner H^m, not just q-ary words. QED.

In particular, at trial C=2 and N=11, R=3 gives optimal cost 11/8>1 while R=4 gives 11/16<1. There is NO hidden singleton full-rank packet: the displayed optimisers have r<=N-1<k.

## MP2. Sharp mandatory logarithmic rank for bounded packets (PROVED)

For fixed C>1 and any R<=N-1, from MP1,

    Z_C >= min( N/C^R, floor(N/2)/C
                            + (N mod 2)/C^R ).              (MP2)

For any fixed R, the minimum diverges linearly as N grows. Therefore even at EVERY nonvacuous exponential-density threshold D<beta_s, there is NO universal R_s, or R_s depending only on C and s, such that *all* original s-free families |F|>D^k admit a witness-preserving anchored packet partition with 1<=r_a<=R_s and Z_C<=1. Proof: choose H with |H|^(1/d)>D, then N->infinity, m/N->infinity exactly as WR3; MP1 applies at each N.

More precisely, if N>2C+2 (and N sufficiently large that the pair-packet alternative exceeds one), MP1 shows that Z_C<=1 is possible with rank cap R<=N-1 **if and only if** N/C^R<=1. A cap R=ceil(log_C N) is therefore optimal once R>=2 and R<=N-1 (automatically for all sufficiently large N). Constructively, assign every group its own R distinct ACTUAL shell points; their N packets give Z_C=N/C^R<=1. Thus LOGARITHMIC anchor rank, not rank N-1, is both necessary and sufficient on these adversaries, up to integer rounding. This is a genuine fully-original rank drop and not a general all-F lemma.

Small-rank sanity: the wreath construction has k=N-1+dm>=3; base values remain f_s(0)=1, f_s(1)=s-1, f_3(2)=6. The classical s-free P(s-1,k) has (s-1)^k distinct original edges. No candidate C_s below known lower bases is inferred.

## MP3. A sharper ENTROPY lower bound valid without a rank cap (PROVED)

Let I be the packet containing an original E uniform in F. For any nonempty anchored packet, |F_a|<=max_x deg_F(x)=2W, so max_a Pr(I=a)<=2/N. Hence Shannon entropy H(I)>=log(N/2), even for adaptive, variable-rank, non-prefix, non-maximal and arbitrarily subdivided genuine original packets.

Write p_a=Pr(I=a), rbar=sum p_a r_a, and Z_C=sum C^(-r_a). The Gibbs/KL relation from [P2](ORIGINAL_PACKET_KRAFT_AND_ENTROPY.md) says

    log Z_C >= H(I) - rbar log C >= log(N/2)-rbar log C.  (MP3)

Thus EVERY budget-valid partition Z_C<=1 (with no r<=R restriction) must satisfy

    rbar >= log_C(N/2).                                     (MP4)

The explicit one-group partition with R=max(2,ceil(log_C N)) shell anchors has rbar=R and budget <=1 for large N. MP4 is therefore sharp up to at most 1+log_C(2) additive rank units on this construction. This does not derive any new general high-density f_s(k) bound; it rigorously quantifies the packet entropy that a global proof must pay.

## MP4. Independent cross-packet intersection energy obstruction (PROVED)

Draw four independent uniform ORIGINAL members E_1,E_2,E_3,E_4 of F, and record their actual shell-group labels I_t (labels describe private-copy *membership*, NOT new physical vertices). If I_1 != I_2, then E_1 intersect E_2 is EXACTLY the physical singleton {p_(I_1,I_2)}, with no private points; similarly for the second pair. Thus

    Pr( E_1 intersect E_2 = E_3 intersect E_4,
        I_1 != I_2, I_3 != I_4 )
      = binom(N,2)*(2/N^2)^2
      = 2(N-1)/N^3.                                       (MP5)

Conditioned on both pairs being cross-group, their actual intersection label has entropy log binom(N,2), and their collision probability is 1/binom(N,2). A proposed original cross-packet method that requires fixed positive *unconditional* pair-intersection coincidence or a fixed-size collection of physical intersection labels is refuted for every D<beta_s by taking N->infinity and m/N->infinity. It would need a nontrivial NORMALIZED/conditioned compatibility mechanism for s distinct petals, not the equality of intersections of two unrelated pairs. In fact F itself has no s-sunflower by WR1.

## MP5. Two genuine attempted mechanisms and what failed

**Adaptive prefix/decision-tree scheme.** Shell membership can be encoded by choosing R≈log_C N *positive physical points in each group*, so MP2 supplies a constructive sufficient packet CODE on this structured family. However this code is obtained from the exceptionally explicit pair-star group geometry. General original families have no certified low-cost cover of owner groups by anchors, nor an independently bounded packet label set. Enumerating singleton full-edge packets would make the condition Z_C<=1 exactly |F|<=C^k, circular. Restricting to uniformly bounded positive depth is now rigorously ruled out even above all nonvacuous thresholds. No universal noncircular prefix recurrence proved.

**Cross-packet intersection-energy scheme.** MP5 shows a vanishing and exactly calculable unconditional pair-intersection collision probability alongside exponentially many original edges. Any entropy gain must track compatibility of a whole s-tuple of original owners and may need to condition on packet labels and actual residual overlaps. Pair-energy by itself gives no positive rank saving on this family; tensor products P(s-1,k), H54/H39/H153, AS3/Q9 and alternating shield families remain independent controls, not automatically dispatched by wreath packet success.

**Baseline recovered:** for any original s-free k-family, a maximal original matching has at most s-1 edges. Its union covers F and has at most (s-1)k physical points. Some point has degree >=|F|/((s-1)k), so f_s(k)<=(s-1)k f_s(k-1) for k>=1. This is factorial-base recursion, not a fixed C_s. Nothing above upgrades this coefficient for arbitrary F.

## MP6. Reproducibility, source audit and limitations

scripts/original_wreath_packet_budget_audit.py independently constructs actual shell/private original edges and brute-forces all physical anchors of size <=R in small cases. It computes exact rational minimum-weight covers of *all original edges* and agrees with MP1 for N=3,4,5, q=2,3, multiple C,R. tests/test_original_wreath_packet_budget_audit.py verifies the exact formula, nonempty true original anchors, and cross-group intersection/entropy controls. Exact finite checks corroborate, not replace, symbolic proofs.

Mishra [v1](https://arxiv.org/html/2606.02667v1) has invalid cumulative original-owner full-shift transfer and its universal O_s(2^k) is FALSE for s>=4; [v2](https://arxiv.org/html/2606.02667v2) concerns SHIFTED families only. Abbott–Hanson/Axante et al. [finite lower factors](https://arxiv.org/abs/2609.06175) are PRIOR ART; [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367) and [Rao](https://doi.org/10.1112/jlms.70380) retain logarithmic-rank general upper bases; [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995) and [Shangguan](https://arxiv.org/abs/2609.30263) are dimension-dependent bounded-VC results. Online source checking 15 October did not establish literature priority for MP1–MP5; mark it PRIORITY NOT CHECKED, NOT a new unconditional breakthrough.

**OPEN:** noncircular ORIGINAL fixed-base multi-anchor packet construction for every s-free family, despite correlated fibres; original s-petal cross-packet compatibility amortisation; unrestricted f_s(k)<=C_s^k; exact earlier correlated LP gaps V_3(T^2) in [16,34], V_3(S tensor Q9^2) in [11,26]. No new unrestricted theorem or publication assertion.
