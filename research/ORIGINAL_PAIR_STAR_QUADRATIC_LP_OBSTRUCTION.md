# Original pair-star obstruction: balanced quadratic defect LP but vanishing point links

**15 October 2026. Verdict: PROVED (general symbolic argument plus independent finite original-record tests); novelty/priority NOT CHECKED. No unrestricted sunflower proof.** This note continues [OPTIMAL_ORIGINAL_OWNER_BALANCING.md](OPTIMAL_ORIGINAL_OWNER_BALANCING.md), specifically the missing implication from balanced actual-witness duals to original point links. All edges, traces, anchors and defect vertices here are ORIGINAL; there are no shifted ancestors.

## PS1. A family with quadratic optimal V_s and theta -> 0 (PROVED, every fixed s>=3)

Let n>=s+1 and put X=binom([n],2), the **actual physical ground vertices**. For i in [n], define the original (n-1)-set

    E_i = { {i,j} : j in [n], j != i };
    H_n = { E_1, ..., E_n }.

Thus k=n-1, N=n, |X|=binom(n,2). For i!=j, E_i intersect E_j in exactly the one physical vertex {i,j}. For any THREE distinct indices i,j,l, the three intersections {i,j}, {i,l}, {j,l} are distinct. Thus no triple has equal pairwise intersections; in particular H_n is s-sunflower-free for EVERY s>=3, with empty as well as nonempty cores excluded. Every x={i,j} has original degree 2, giving

    theta(H_n) := max_x deg_Hn(x)/|H_n| = 2/n = 2/(k+1) -> 0.   (PS1a)

Recall the exact all-anchor actual-record definition of NC1: anchor E_i; choose s distinct nonempty, equal-cardinality traces on E_i that form an s-sunflower; select one genuine original petal from each trace packet; defect D is the actual ground points appearing in at least two but fewer than s chosen petals, outside the anchor. For H_n, the nonempty trace packet for each j!=i is the singleton {E_j}, with trace {{i,j}}. Any s distinct such traces are disjoint singletons and therefore form a trace sunflower with EMPTY core. Hence there is exactly one actual record for each (i,J), i notin J, |J|=s, where J is an unordered s-set of original petal owners. There are exactly

    R = n*binom(n-1,s) = (n-s)*binom(n,s)                      (PS1b)

labelled original records. The defect of (i,J) is **exactly**

    D_(i,J) = { {a,b} : a,b in J and a!=b },                  (PS1c)

the binom(s,2) edges of K_J as actual vertices of X; it is nonempty, disjoint from anchor E_i, and attained by the s distinct ORIGINAL petals indexed by J. Conversely there are no additional records because every anchor trace packet is a singleton.

Consider the vertex-defect covering LP (primal) min sum_(x in X) z_x under z_x>=0 and sum_(x in D_r) z_x>=1 for every record r; its dual maximizes Y=sum_r y_r under y_r>=0 and sum_(r:x in D_r)y_r<=1 at every actual physical x.

An exact feasible primal is z_x=1/binom(s,2) for EVERY x in X, objective binom(n,2)/binom(s,2). An exact feasible dual is

    y_(i,J) = 1 / [(n-s)*binom(n-2,s-2)]

for EVERY labelled actual record. Each physical x={a,b} lies in exactly (n-s)*binom(n-2,s-2) such record defects: select J containing {a,b} then select anchor outside J. Thus ALL  physical dual constraints hold at equality. The dual objective is

    Y = (n-s)*binom(n,s) / [(n-s)*binom(n-2,s-2)]
      = binom(n,2)/binom(s,2) = n(n-1)/[s(s-1)].

Primal and dual feasible objectives coincide, so by weak duality,

    V_s(H_n) = n(n-1)/[s(s-1)] = k(k+1)/[s(s-1)].            (PS1d)

Every original owner E_i participates symmetrically; as EVERY record owns exactly s+1 ORIGINAL edges, its load is exactly

    m_(E_i) = (s+1)*Y/n = (s+1)(n-1)/[s(s-1)]
             = (s+1)*k/[s(s-1)].                            (PS1e)

It follows that M=(s+1)Y/N and **lambda=1** for an OPTIMAL feasible actual-record dual. This is not just existence of an arbitrary fractional feasible witness; the LP value is exact, dual optimal, and ownership optimally perfectly balanced.

**Consequence (proved negative theorem).** No universal statement of the form "for all original s-free families, optimal lambda=1 together with V_s(F)>=c_s k^a (any fixed a<=2) forces theta(F)>=phi_s>0" can hold. Even V_s/k grows unboundedly while theta tends to zero. The constructed family is SPARSE: N=k+1; it proves NOTHING against a link premise restricted to N>D_s^k for constant D_s>1.

## PS2. Disjoint intersecting copies nearly saturate the maximal-matching link denominator (PROVED)

For 1<=r<=s-1, take r disjoint physical copies of H_n and let U_(n,r) be their disjoint union (no shared vertices, all edge labels distinct). Inside any copy, every pair of original edges meets at one unique ground vertex, and no three edges form a sunflower. Across copies intersections are empty. An s-tuple spanning >=2 copies cannot be a sunflower: with at most s-1 copies, two petals belong to the same copy and have a nonempty intersection, whereas cross-copy intersections are empty. An s-tuple contained in one copy also fails. Thus U_(n,r) is genuinely s-free for all s>=3.

It has k=n-1, N=rn, every ground vertex original degree exactly 2, and

    theta(U_(n,r)) = 2/(rn).                                   (PS2a)

Since every actual trace to the anchor must be nonempty, each anchored record belongs wholly to ONE copy, and no cross-copy records occur. The ground-vertex covering LP decomposes into r independent copies, and symmetrically translated PS1 optimal primal and duals remain feasible and optimal. Consequently

    V_s(U_(n,r)) = r*n(n-1)/[s(s-1)]
                = k*N/[s(s-1)],   lambda_opt=1.              (PS2b)

In particular for r=s-1, theta=2/[(s-1)(k+1)], within a factor tending to 2 of the general maximal-matching bound theta>=1/[(s-1)k]. Thus even the maximal-matching link fraction is essentially sharp up to factor two on sparse sunflower-free originals despite an exactly balanced LP of order k*N. Each U has only (s-1)(k+1) sets, below any D_s^k eventually for D_s>1.

For a uniformly selected original owner I in H_n and a uniformly selected vertex X from E_I, X is uniform on binom([n],2); H(I|X)=log 2, while H(I)=log n. Equivalently the link at every physical vertex has probability 2/n and the mutual information I(I;X)=log(n/2). This is a second, entropy/shadow description of the same concrete failure: enormous symmetric cross-anchor record supply does not force a constant fraction of original owners at any ground point. In U_(n,r) the entropy deficit grows further as log(rn/2).

## PS3. Conditional density-link recurrence is valid but demands genuinely new high-density input

If explicit D_s>1 and phi_s>0 satisfy:

    for all k>=1, all s-free ORIGINAL k-families F,
    |F|>D_s^k  implies there exists ACTUAL x with deg_F(x)>=phi_s|F|,

then the genuine rank-(k-1) original link F_x is s-free, hence

    f_s(k) <= max(D_s^k, phi_s^(-1) f_s(k-1));               (PS3a)
    f_s(k) <= C_s^k, C_s=max(D_s,phi_s^(-1),s-1,1).         (PS3b)

Base cases: f_s(0)=1, f_s(1)=s-1. For s=3, f_3(2)=6 (two disjoint triangles), so a coefficient-two original one-step recurrence from k=1 is FALSE. Nonempty and empty sunflower cores are equally forbidden. The inequality uses the strict >D_s^k threshold exactly, with equality in the easy branch.

**Non-vacuity lemma.** Write beta_s=sup_(k>=1) f_s(k)^(1/k), possibly +infinity. Tensor products of original s-free uniform families are themselves s-free: for any purported s original product petals, the coordinatewise intersections must be equal and each coordinate's distinct factors, when >=s, would give an s-sunflower; a valid standard proof uses the first block in which the petals differ to partition them into either equal or pairwise-disjoint coordinate choices, and induction on products (see WORKING_PROOF). More directly for our use, H^m is known s-free for any s-free H, by looking at every coordinate: equal intersections among product petals imply each coordinate either all same or all pairwise distinct, and some coordinate must be pairwise distinct. Consequently f_s(dm)>=|H|^m for any rank-d original s-free H. If D_s<beta_s, by definition there exists finite H with |H|^(1/d)>D_s, so H^m witnesses |F|>D_s^(dm) for arbitrarily large m. If D_s>=beta_s, NO family exceeds D_s^k and the proposed link premise is entirely vacuous. Therefore showing nonvacuity ABOVE the presently certified factor bases requires stronger actual ORIGINAL lower constructions; choosing large D_s and checking no examples is not evidence for the conjecture.

Hostile known controls for the exact theta premise (factor values from prior source/earlier audited work, not re-enumerated here):

| s | ORIGINAL factor | d,N | proven/literature theta | necessary if D_s below N^(1/d) |
|---|---|---|---|---|
| 3 | binary product P(2,d) | d,2^d | 1/2 | phi_3<=1/2 |
| 3 | two disjoint triangles tensor powers | 2,6 | 1/3 | phi_3<=1/3 |
| 3 | Abbott-Hanson H54 tensor powers | 4,54 | 2/9 | phi_3<=2/9 |
| 4 | Axante et al. H39 tensor powers | 3,39 | 3/13 | phi_4<=3/13 |
| 6 | Axante et al. H153 tensor powers | 3,153 | 3/17 | phi_6<=3/17 |
| all s>=3 | P(s-1,d) | d,(s-1)^d | 1/(s-1) | phi_s<=1/(s-1) |

The earlier H54/H39/H153 factors are PUBLISHED PRIOR ART. The table asserts no complete incidence-table re-enumeration here. The bound on phi applies for D_s **strictly below** the displayed factor's exponential base. Tensoring preserves theta exactly: for a product with disjoint physical coordinate blocks, max original point-link fraction equals the maximum of the factor fractions. Equality thresholds D_s=base are NOT ruled out by this strict > premise.

## PS4. Two attempted routes and honest barriers

**Route A: weighted owners -> point links.** OB1–OB6 provide exact balanced actual-original defect duals and survival under deletion. PS1/PS2 prove an *unbounded*, genuinely original counterexample to any density-FREE implication from perfect balance plus even quadratic LP mass to a fixed fractional point link. Tensor powers of H_n inherit a balanced feasible dual by OB5, giving masses at least m*n(n-1)/[s(s-1)] at rank m(n-1) and N=n^m, but the underlying per-rank exponential base n^(1/(n-1)) tends to 1 as n grows. To salvage Route A one MUST include an explicit nonvacuous exponential density hypothesis or a new structurally restrictive functional. Balancing alone is finished as a proposed bridge.

**Route B: shadow/codegree/entropy -> density increment.** PS1 is an intersecting original family with EVERY original pairwise intersection a distinct singleton; all C(n-1,s) equal-size disjoint trace choices at each anchor are physically attainable, and all produce explicit original cross-petal defects. Yet every physical point lies in just two original owners. A nontrivial entropy or shadow argument must detect the EXPONENTIAL density, not just high trace multiplicity, disjoint trace geometry or conditional vertex entropy. The Sauer-Shelah/VC route still requires a fixed bound on VC dimension; the classical binary product has VC dimension proportional to rank. No bound phi_s for N>D_s^k has been established.

For the previous exact 45-edge rank-six T=S tensor Q9, its optimal balanced dual gives V_3(T)=8 and theta(T)=max(theta(S),theta(Q9))=3/5; hence V_3(T^m)>=8m and theta(T^m)=3/5 at rank 6m, N=45^m. This only supplies linear-in-rank V with base 45^(1/6)<2. PS1 proves that **quadratic** V and perfect balancing still do not force theta constant when size is sparse. Neither construction reaches the required exponential threshold.

Correlated tensor excess is unresolved: superadditivity proves

    16 <= V_3(T tensor T) <= 34,
    11 <= V_3(S tensor Q9 tensor Q9) <= 26.

The upper bounds are the number of actual ground vertices (all-vertex cover); the lower bounds use NC1+OB3 and V_3(Q9)=3. These are rigorous but crude. NO exact claim that V(T^2)>16 or V(S Q9^2)>11 is made; exhaustive all-anchor 2025-edge enumeration was NOT completed. Even if strict extra defect LP synergy is later proven, converting it into a multiplicative, high-density rank saving remains an independent open step.

## Original small-rank / baseline audit

k=0 has at most the one empty ORIGINAL set and f_s(0)=1. k=1 has s-1 original singleton sets. For k=2,s=3, an s-free graph has maximum degree 2 and maximum matching number 2; the union of two triangles has six edges and standard counting gives f_3(2)=6. In PS1/PS2 pairwise intersection points are genuine 2-element labels {i,j}, and all petals are distinct original E_i. No shifted source is used. Both empty and nonempty cores are checked by the distinct pairwise intersections. The classical q-product requires C_s>=s-1; PS1/PS2 give no stronger cardinality lower bounds.

## Reproducibility, source scrutiny and verdict

- Exact general proof: PS1a–PS1e and PS2a–PS2b above. Machine: scripts/original_pair_star_quadratic_audit.py, independent tests/test_original_pair_star_quadratic_audit.py (stdlib, exact integer counts; s=3,4,5,6 n<=9 plus disjoint copies; the test independently compares the repository's general ORIGINAL rectangle-record enumerator).
- Mishra [v1](https://arxiv.org/html/2606.02667v1): claims full O_s(2^k), FALSE for s>=4 by P(s-1,k), and multi-shift original-owner transfer invalid. Mishra [v2](https://arxiv.org/html/2606.02667v2): shifted-family theorem only. Neither contains the needed ORIGINAL high-density implication.
- [Bell–Chueluecha–Warnke](https://doi.org/10.1016/j.disc.2021.112367), [Rao survey](https://doi.org/10.1112/jlms.70380): O_s(log k) base general regime, no C_s.
- [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995) and [Shangguan](https://arxiv.org/abs/2609.30263): SOURCE CLAIMS bounded-VC bounds (50ds)^k and (C s log(d+1))^k respectively; when d~k, neither is a rank-independent base. [Axante et al.](https://arxiv.org/abs/2609.06175) owns the published H39/H153 construction; H54 is attributed to Abbott–Hanson.
- **PROVED internally:** PS1/PS2 full all-original constructions and exact LP; PS3 conditional recurrence and exponential-density nonvacuity criterion. **FALSE:** unconditional implication 'balanced superlinear LP -> constant original point-link'. **CONDITIONAL:** PS3 link-to-rank recurrence. **OPEN:** any nonvacuous high-density original-family density-to-link theorem, T^2 exact excess, full Erdős–Rado conjecture. **PRIORITY NOT CHECKED** for PS1/PS2 as literature originality; they are elementary line-graph dual star constructions and may already be known.
