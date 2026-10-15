# All-physical ORIGINAL nested wreath packet theorem and conditional s-way compatibility

15 October 2026. **AP1–AP5 PROVED internally; PRIORITY NOT CHECKED.** Exhaustive exact rational checks are independent verification, not replacements for proofs. This strengthens NW2 from shell-only anchors to **every actual physical anchor** for *q-ary private product leaves*. It does NOT hold as stated for arbitrary private seed H and does NOT prove the unrestricted Erdős–Rado sunflower conjecture, which remains **OPEN**. Mishra v1's cumulative full-shift original-owner attribution is invalid; its proposed universal base-2 bound is false for s>=4. Mishra v2 is SHIFTED-only. No image sunflower is claimed to lift.

## AP1. Genuine ORIGINAL construction and the exact unrestricted physical-anchor optimum (PROVED)

Take integers s>=3, 2<=q<=s-1, m>=1 and N_1,...,N_t>=3. In the physically disjoint hierarchical shell construction NW1, use at EACH leaf its own PRIVATE copy of the genuine q-ary product P(q,m) (one of q real vertices in each of m disjoint private coordinate blocks). Denote the resulting simple original family F. It is s-free by NW1, for empty as well as nonempty cores, with

    k=m+sum_h(N_h-1),      |F|=q^m prod_h N_h.                    (AP1)

Each leaf has its own private physical vertex names; tuple labels are indexing metadata, NOT physical ground vertices.

Partition ALL original edges into nonempty packets F_a. An anchor B_a must be a NONEMPTY subset of the actual physical intersection of all edges in its packet and can use ANY shell or private ground points. The cost is Z_C=sum_a C^(-|B_a|) for fixed real C>1; each original edge is owned exactly once. This allows arbitrary adaptive, overlapping-in-label, split-fibre, all-private and non-prefix packets. Every packet residue, after deleting its actual B_a, is still an injective original s-free family of uniform rank k-|B_a|.

Define the PRIVATE terminal factor

    Q= min{1,(q/C)^m},                                       (AP2)

and the backwards recurrence for h=t,...,1:

    U_(t+1)=Q,
    a_h=C^(-(N_h-1)) U_(h+1),
    V_h=min_{0<=j<=floor(N_h/2)} [ j/C + (N_h-2j)a_h ],
    U_h=min{1,V_h}.                                          (AP3)

**THEOREM AP1:** The exact minimum Z_C over ALL nonempty actual-PHYSICAL anchored packet partitions of F is **V_1**, not U_1. At the root an empty ancestor anchor is forbidden. At a nonroot node the min-with-one means stop at its ALREADY NONEMPTY physical ancestor shell; it is NOT an empty-anchor packet. AP3 is an exact restricted-class partition theorem, not a recurrence for f_s(k).

**Proof: terminal leaf.** Fix a leaf v and let its actual shell S_v have size K=sum(N_h-1)>=2. A nonempty anchor used exclusively in this leaf may be enlarged by the entire physical S_v with no loss of supported original edges and with weakly lower cost. Its remaining private part selects l distinct q-ary coordinates, 0<=l<=m, and consequently is present in EXACTLY q^(m-l) of the q^m real original edges in that leaf; two vertices in one private block are never simultaneously present. If these cylinder supports cover the leaf, counting original owners divided by q^m gives sum_a q^(-l_a)>=1. Their normalized anchor cost is sum_a C^(-l_a) >= min_{0<=l<=m}(q/C)^l sum_a q^(-l_a) >=min(1,(q/C)^m)=Q. Equality holds EITHER by the one true shell packet S_v (l=0), OR by q^m singleton original-edge packets each anchored by its whole S_v plus its m true private points (l=m). At the leaf the optimal cost is exactly C^(-K)Q. This argument is a linear covering dual on actual physical vertices and does not assume the conjecture for the suffix.

**Proof: internal nodes.** At node u with physically common ancestor shell S_u, any packet meeting three distinct child groups has no physical anchor outside S_u; if |S_u|>0, replacing it by a single anchored packet of the ENTIRE subtree does not increase cost, and renders other subnode packets redundant. It cannot exist at root because then the anchor is empty. A packet meeting exactly two child groups i,j has common physical points outside S_u consisting precisely of the ONE actual pairpoint p^(u)_{ij}; all descendant/private vertices live in disjoint grounds. It can therefore be enlarged to the full union of those two child subtrees, anchored by S_u union {p^(u)_{ij}}, at normalized cost 1/C. A packet contained in one child is no better than the optimal child cover, with the full N_h-1 shell A^(u)_i added, normalized cost a_h. Thus the minimum support cover of child labels is a weighted edge/singleton cover of the N_h vertices, cost j/C+(N_h-2j)a_h for some disjoint j pairs; crossing/duplicating supports can be replaced by full child supports and redundant supports deleted, and a_h<=1/C because N_h>=3 and U_(h+1)<=1. At nonroot nodes include the ancestor stop option 1. At root exclude it. Inducting from the exact private leaf dual proves (AP3), including all split or private-point packet choices. A set cover of owner edges may be converted to a disjoint packet partition by assigning each owner once and deleting empty packets, without raising cost; the named anchors remain true common physical subsets. QED.

## AP2. Trial-base-two rigidity under ALL physical anchors (PROVED)

For C=2 and q>=2, Q=1, so the complete all-physical optimum equals the earlier *shell-only* optimum. For every N_h>=3,

    min Z_2 = prod_h N_h / 2^(N_h-1).                        (AP4)

Proof: U_(h+1)<=1; 2a_h <=2/2^(N_h-1)<=1/2, so pairing two child groups at cost 1/2 never beats two singleton child costs 2a_h. Therefore j=0 is optimal at every level, U_h=V_h<=1, giving (AP4). This is NOW an assertion about **every physical private-point anchor** for genuine q-ary suffixes, rather than the shell-only theorem NW4.

With q=3, s=4, N_h=3 for h<=t and m=t, the four-free ORIGINAL family has k=3t and 9^t distinct ORIGINAL members >2^(3t). Its exact cost optimum over ALL physically anchored partitions is (3/4)^t ->0. The leaf-shell packets achieve it and have actual rank drop r=2t<3t; their honest original residual occupancies are n_v / 2^(k-r) = 3^t/2^t = (3/2)^t, *unbounded*. No base-2 residual capacity theorem follows from cheap anchored partition labels, even using all private anchors. The general full conjecture can choose C_s much larger than 2; no contradiction to it is asserted.

## AP3. Private points can REALLY help at other trial bases (PROVED)

For N_h=3, C=3, q=2, the recurrence has a_h=U_(h+1)/9; j=0 beats j=1 because 3a_h <=1/3+a_h for U_(h+1)<=1. Thus

    min Z_3=(1/3)^t (2/3)^m.                                (AP5)

The old shell-only minimum was (1/3)^t, so allowing private points improves it by an EXACT factor (2/3)^m. Examples of honest exhaustive all-anchor searches: (N)=(3),q=2,m=1,C=3 gives 2/9; (3),q=2,m=2,C=3 gives 4/27; (3,3),q=2,m=1,C=3 gives 2/27. For q=3,C=3,(3,3) it instead gives 1/9. C=2,(3,3),q=2,m=1 gives 9/16. These are rational equalities, not estimates.

## AP4. Exact conditional ORIGINAL s-petal compatibility certificate (PROVED)

Fix s disjoint NONEMPTY packets (disjoint in ownership), independently sample one actual ORIGINAL edge E_i from each, and fix any genuine physical set D. Put

    delta_ij(D)=Pr[E_i intersection E_j != D | packet labels i,j].

If sum_{i<j} delta_ij(D)<1, the union bound shows positive probability that EVERY actual pair intersection is exactly D, furnishing s distinct actual ORIGINAL sunflower petals (the packets enforce distinctness). Thus for EVERY s-free original family and EVERY choice of s disjoint nonempty packet distributions, EVERY physical D satisfies

    sum_{i<j} delta_ij(D)>=1.                               (AP6)

This is a valid rank/n-independent NONCIRCULAR conditional original compatibility inequality, but its hypothesis is a very strong actual s-way intersection concentration, not an upper bound for residual owner counts. The threshold 1 is sharp: take s distinct equal-rank original sets of which only the first two share a special point x, while every other pair is disjoint. With deterministic one-owner packets and D=empty, exactly one delta is 1 and all others 0; there is no s-petal sunflower. This example needs no invented original owners.

AP6 explains why collision of two UNRELATED pairs, even a high collision probability, is not a sunflower: all binom(s,2) pairs of the SAME distinct ORIGINAL tuple must have exactly the same actual D. For nested wreaths the first different child groups carry physical intersections S_u union {p_ij}; three different groups give three distinct points; a repeated group gives within-group intersection containing the full shell A_i, which differs from the cross pairpoint since N>=3. Thus no mixed-label tuple can satisfy AP6 at any level. All-same leaf labels reduce to private P(q,m), which itself is s-free because q<s.

## AP5. Weighted core-overlap obstruction (PROVED; standard graph-theoretic argument)

For any fixed physical D and ANY probability distribution mu on original edges containing D, assume every residual E\D is nonempty and the family is s-free. Then

    Pr_{E,E' independently drawn from mu}
       [(E\D) intersection (E'\D) != empty] >= 1/(s-1).   (AP7)

Indeed the graph joining two distinct edges exactly when their residues are disjoint is K_s-free (a K_s would be an actual s-petal sunflower with core D). For an arbitrary probability mass on its vertices, merging mass between any two nonadjacent positive-mass vertices cannot decrease the quadratic disjointness-edge weight if we choose the better endpoint; repeat until the support is a clique of size <=s-1. For a clique with masses w_i, the ordered disjointness probability is 1-sum w_i^2<=1-1/(s-1), proving (AP7). For q=s-1 pairwise disjoint singleton ORIGINAL sets, uniform mu attains exact equality. The same theorem applies to any mixture of packet laws supported on the same fixed D, giving a measured quadratic matrix constraint. It is a conditional noncircular energy certificate, but does not bound rank-normalized residual occupancy and alone recovers only the usual maximal matching / link-scale barrier.

Specifically by union bound Pr(nonempty intersection of two residues) <=sum_{x outside D} (deg(x)/n)^2 <= (k-|D|) (max_x deg(x)/n), so AP7 implies max_x deg(x)>=n/[(s-1)(k-|D|)]. This is precisely the old point-link bound and closes NO fixed-base recurrence. The private wreath may have overlap probability 1 through its shell points, making AP7 far from demanding a useful gain.

## AP6. Independent finite audit, old controls and remaining gap

`scripts/all_physical_wreath_compatibility_audit.py` constructs ALL actual shell and private point sets using the existing NW1 independent builder. It enumerates every NONEMPTY physical anchor contained in an original edge (not only shells), builds its actual owner-support subset and uses exact Fraction set-cover dynamic programming with dominated-support elimination. It compares the results to (AP3) across t=1,2, q=2,3, m=1,2 and C=2,3; checks actual s-freeness and AP6 exact sharp witness. This enumeration proves only the checked finite cases; AP1–AP7 have independent symbolic proofs above. It does not certify priority.

Mandatory controls preserved: P(s-1,k), f_3(2)=6, H54/H39/H153 are prior-art seeds; AS3/Q9 and correlated partial fibres still have uncertified LP optima V_3(T^2) in [16,34] and V_3(S tensor Q9^2) in [11,26]; alternating shields, original pair-stars, one-level W(N,m) and nested NW1 remain adversaries. None supplies an unrestricted original fixed C_s. Source check 15 October: [Mishra v1](https://arxiv.org/html/2606.02667v1), [v2](https://arxiv.org/html/2606.02667v2), [Axante et al.](https://arxiv.org/abs/2609.06175), [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367), [Rao](https://doi.org/10.1112/jlms.70380), [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995), [Shangguan](https://arxiv.org/abs/2609.30263); the last two are bounded-VC results, not unrestricted solutions. **PRIORITY NOT CHECKED** for AP1–AP7; no complete original-family theorem, publication or author contact.

**OPEN CENTRAL GAP:** prove a uniform-in-rank original residual-capacity inequality tied to a nontrivial actual s-way cross-packet intersection distribution. AP3 now solves the entire all-physical nested-q-product anchor optimisation problem but is not such a general inequality. AP6 is genuine s-owner compatibility but needs a quantitative reason its premise appears in sufficiently dense arbitrary original families. No fixed-base f_s(k)<=C_s^k has been proved.
