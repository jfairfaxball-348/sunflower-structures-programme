# Nested ORIGINAL pair-star wreaths: exact shell-packet recursion and the false Kraft shortcut

15 October 2026. **PROVED internally** for explicitly defined, original-edge nested wreaths and **shell-only** anchors. Exact rational finite instances independently audited. **PRIORITY NOT CHECKED**. This is a new *restricted-mechanism obstruction*, not a proof of the unrestricted Erdős–Rado sunflower conjecture; that conjecture remains **OPEN**. Mishra v1's cumulative full-shift original-owner attribution is invalid and its universal O_s(2^k) claim is false for s>=4; Mishra v2 concerns SHIFTED families only. No shifted-to-original petal lift is used.

## NW1. Physically nested ORIGINAL set construction (PROVED)

Fix s>=3. Let H be any nonempty finite simple d-uniform s-sunflower-free ORIGINAL family, d>=1, of size M. Fix m>=1 and levels t>=1 with integers N_1,...,N_t>=3. At each prefix u=(i_1,...,i_{h-1}) of length h-1 introduce a **separate physical point** p^(u)_{ab} for each 1<=a<b<=N_h. Put A^(u)_i={p^(u)_{min(i,j),max(i,j)}:j!=i}. Each leaf v=(i_1,...,i_t) has an independently relabelled physical copy H_v^m on points disjoint from ALL shells and from every other leaf copy. Let S_v=union_(h=1)^t A^(v_{<h})_{i_h}, and define the actual ORIGINAL family

    F(N_1,...,N_t;H,m)
       = union_(leaves v) { S_v union E : E in H_v^m }.

All points named above are literally distinct unless their shell prefix and pair indices coincide. The leaf index is NOT an additional ground-set point. Every member is ORIGINAL, distinct, and of rank

    k=dm+sum_h(N_h-1),      |F|=M^m prod_h N_h.              (NW1)

At each node, different children have shell intersections exactly {p^(u)_{ij}} at THAT node; child descendants occupy disjoint private grounds. The one-level WR1 proof applies inductively: s distinct sets all from one child would project to a sunflower in that child; two in one child and one in another have unequal pair intersections, since N_h>=3 and the within-child shell A_i contains points missing from its cross-child intersection {p_ij}; s petals in distinct children have three distinct pairwise physical points. All distributions are excluded. Hence F is s-free for BOTH empty-core and nonempty-core s-sunflowers, independently of H's internal common core. No abstract tensor-coordinate identification between private copies is made.

For independent *uniform* leaves and their original suffixes, an outer-cross pair has intersection {p^(empty)_{ij}}, whereas two sets from the SAME first-level group and two different second-level groups have pair intersection A^(empty)_i union {p^(i)_{ab}}. At level h, after conditioning on a common prefix u, the cross-sibling intersection is the fixed ancestor shell S_u plus {p^(u)_{ab}}, with every shared inner-private component absent.

## NW2. The exact shell-only anchored partition functional (PROVED)

A *shell-only partition* consists of disjoint nonempty packets of entire actual ORIGINAL edges, each with a NONEMPTY anchor B contained in every packet edge and made solely from the physical shell points p^(u)_{ij} (never private H coordinates). Cost at trial C>1 is Z_C=sum_B C^(-|B|), counted once PER PACKET. No atom/fibre may be assigned twice. Every residual deletes precisely this actual B, preserves distinct original owners and is s-free.

The shell of a leaf v has exactly K_shell=sum_h(N_h-1) points. A packet that contains some but not all owners of a leaf has the same shell-anchor options as the entire leaf fibre; expanding packet supports to entire leaf fibres turns any partition into an atomic support-cover without increasing costs. Conversely any shell-anchor cover of the leaf labels may be made a disjoint partition by assigning each leaf fibre to one covering anchor (and dropping redundant anchors), never increasing cost. Thus the cost optimum is exactly the weighted shell-support set-cover optimum; NO assumption about a private suffix size or potential sunflower is needed.

Define U_(t+1)=1, and work backwards for h=t,...,1:

    a_h = C^(-(N_h-1)) U_(h+1),
    V_h = min_(0<=j<=floor(N_h/2)) [j/C+(N_h-2j) a_h],
    U_h = min(1,V_h).                                         (NW2)

**Theorem NW2:** For every C>1, the exact minimum Z_C over ALL such nonempty ORIGINAL shell-only anchored packet partitions equals **V_1**. For h>=2, U_h represents the permitted choice to stop descending and cover the entire subtree with the ALREADY NONEMPTY common ancestor shell (normalised cost 1); it is NOT an empty physical anchor. At the root, that stop option is invalid (common shell empty), hence V_1 rather than U_1.

**Proof.** Condition on a node u and factor out the cost C^(-|S_u|) of its fixed ancestor shell (for the root this shell is empty). If a nonempty packet touches two different child groups i,j at this node, any common shell anchor inside this node must be the unique physical point p^(u)_{ij}; it cannot touch a third child, and its cost relative to the ancestor factor is at least 1/C. If it touches just one child, the full A^(u)_i is common there, so its best possible normalised cost is C^(-(N_h-1)) times the cheaper of stopping at that child (cost 1) or partitioning its descendants optimally (cost V_(h+1)); this is exactly a_h. A packet touching >=3 child groups has only the ancestor shell: relative cost >=1. It can be replaced by *one stop packet for the whole node* if stopping is allowed; this is the U_h= min(1,V_h) alternative. If stopping is not chosen, weighted pair/singleton child supports cover N_h children. Since a_h<=C^(-(N_h-1))<=1/C, a minimum cover can be made from j disjoint pairs and N_h-2j single children: select j pair packets of cost 1/C and partition every other child using its optimal cost a_h. To prove the LOWER bound without assuming disjoint supports, suppose there are b pair packets. At most 2b children are touched by these; each untouched child must incur cost >=a_h from packets contained in that child. If b<=floor(N_h/2), total >=b/C+(N_h-2b)a_h. If b exceeds floor(N_h/2), total >= b/C, which is at least the appropriate j=floor(N_h/2) expression since a_h<=1/C. The cost of packets with >=3 supports is handled separately by the stop option: any such packet can be enlarged to the whole node for no greater cost, making all other packets superfluous. Induct upwards and finally exclude the zero-anchor root stop. All optimisers choose actual shell points and partition entire private original fibres, so attainability follows. QED.

At two levels N,L the closed form is

    V_1 = min_j [j/C+(N-2j) C^(-(N-1)) min(1, V_2)],
    V_2 = min_b [b/C+(L-2b)/C^(L-1)].                    (NW3)

This is an exact adaptive-RANK recursion for a concrete genuine-original adversarial hierarchy; **it is NOT a recurrence for f_s(k)**. It must not be claimed for arbitrary anchors that use private H points (those can condition suffixes and reduce cost).

## NW3. Multiscale cost MULTIPLIES; trial-base-two closed form (PROVED)

For C=2 and EVERY N_h>=3, induction in NW2 gives

    V_h=U_h= prod_(ell=h)^t N_ell/2^(N_ell-1),             (NW4)
    Z_2^shell,min = prod_(h=1)^t N_h/2^(N_h-1).

Indeed each factor N/2^(N-1)<=1; hence U_(h+1)<=1. Thus a_h<=2^(-(N_h-1)) and 2 a_h<=1/2 for N_h>=3, so in the minimisation j=0 is no more expensive than any j>0 (the difference per pair is 1/2-2a_h>=0). Therefore V_h=N_h a_h, completing induction. The optimiser uses **one packet per leaf**, anchored by its entire actual shell S_v of rank sum_h(N_h-1); it is strictly smaller than the edge rank k because d m>=1.

For N_1=...=N_t=3 this gives

    Z_2^shell,min = (3/4)^t,    mean original-anchor rank = 2t.   (NW5)

The per-level Kraft costs multiply, while the rank drops ADD and the leaf labels carry t log 3 entropy. They neither create an impossible logarithmic toll nor force an original s-sunflower. This is a definitive two/multilevel result (not a statement that arbitrary original packets have the same optimum).

## NW4. Explicit exponentially dense false induction from a small Kraft budget (PROVED)

Fix **s=4**, H the PRIOR-ART original family of q=3 distinct singleton sets, N_h=3 for h=1,...,t and m=t. Then H^t is the original classical q-product P(3,t), s-free, so NW1 yields an ORIGINAL four-sunflower-free family with

    rank k=3t,      |F|=3^t * 3^t = 9^t > 8^t = 2^k.      (NW6)

Nevertheless it has a disjoint original anchored leaf-packet partition with

    r_v=2t<k,      Z_2=3^t * 2^(-2t)=(3/4)^t <=1,        (NW7)

asymptotically tending to ZERO. Each residual is the actual original P(3,t) with 3^t members, strictly MORE than 2^t, the trial-base-two residual capacity. Consequently the implication

    'actual original packet partition, positive rank drops, Z_2<=1'
          ==> '|F|<=2^k'

is FALSE, even at arbitrarily small Z_2 and exponential family density. The invalid step would be to assume EVERY residual of rank k-r obeys |F_v|<=2^(k-r), i.e. to insert the very original-family theorem one is trying to prove (and at C=2,s=4 an actually false theorem). This is an explicit noncircular counterexample to the Kraft-only *proof mechanism*, not to the conjecture for some larger C_4.

More generally let q=s-1>2. The same choice gives q^t 3^t ORIGINAL edges at rank 3t; whenever 3q>8 the size exceeds 2^(3t). The s=4 case already suffices. All anchors have r<k; NO singleton full-edge packet or shift is used.

## NW5. Conditional ORIGINAL cross-packet pair collisions (PROVED)

At a node with N children, condition on four independent uniformly selected ORIGINAL edges all sharing that node's prefix u. The child indices are independent uniforms on [N] because every leaf has the same suffix multiplicity. For two pairs whose child labels differ within each pair, their physical pair intersections (after removing the deterministic ancestor shell) are the same iff they have the same unordered child pair. Thus

    Pr(pair intersections equal AND both child pairs cross
       | four edges share prefix u)
        = 2(N-1)/N^3.                                      (NW8)

Conditioned FURTHER on both pairs cross, the equality probability is exactly 1/binom(N,2) (the actual unordered physical pairpoint is uniform). This uses no ghost 'group-index point'. At level two, conditioning on all four first-level labels equal and integrating over their common value, the exact unconditional probability of the **within-outer, inner-cross** collision event is

    [N*(1/N)^4] * [2(L-1)/L^3]
      = 2(L-1)/(N^3 L^3).                                  (NW9)

An unconditional fixed positive pair-collision credit at any level is therefore unavailable when N,L grow. A truly useful original s-owner compatibility bonus must be conditional/normalised and distinguish actual common ancestor shells; NW8/NW9 do NOT exclude sophisticated cross-packet methods. The constructed entire family is itself s-free.

## NW6. Independent rational checks; scope and open gap

`scripts/nested_original_wreath_audit.py` builds all actual physical outer/inner shell and private points (never fictitious group vertices), enumerates distinct edges and all s-tuples in small cases, and uses exact `Fraction` weighted set-cover over EVERY nonempty shell-point anchor for (3), (3,3) at C=2,3, agreeing with NW2. Explicit comparisons include (3,3), C=2 optimum 9/16 and C=3 optimum 1/9. It also checks (3,4),(4,3) symbolic NW2, multiplicativity to depth 4, and the rank-3t cardinality counterexample. Corresponding `tests/test_nested_original_wreath_audit.py` checks the standalone assertions. Tests corroborate but do NOT replace the all-level proof.

Baseline controls unchanged: classical P(s-1,k); f_3(2)=6; prior H54(s=3), H39(s=4), H153(s=6), AS3/Q9 correlations, alternating shields, original pair-stars and WR1. All are compatible with NW2 because it is a theorem for this restricted nested family only; it does not claim to classify all s-free families. All numerical source-factor quantities, prior obstruction files, and LP unknown intervals 16<=V_3(T^2)<=34, 11<=V_3(S tensor Q9^2)<=26 remain unchanged.

**OPEN:** fixed-base proof for arbitrary original k-uniform families; a noncircular packet-label/rank mechanism capable of bounding residuals without assuming the target; conditional *s*-way cross-packet compatibility credit, not just equality of unrelated original pair intersections. PRIORITY NOT CHECKED for NW1–NW9. No universal C_s proved, no arXiv/journal release or author contact.

**Sources:** Mishra [v1](https://arxiv.org/html/2606.02667v1), [v2](https://arxiv.org/html/2606.02667v2); [Axante et al.](https://arxiv.org/abs/2609.06175); [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367); [Rao 2026](https://doi.org/10.1112/jlms.70380); [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995); [Shangguan](https://arxiv.org/abs/2609.30263). The latter two require bounded VC dimension, not a k-independent assumption for arbitrary original families.
