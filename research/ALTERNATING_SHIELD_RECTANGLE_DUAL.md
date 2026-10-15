# Alternating original trace shields and exact rectangle-cover obstruction (15 October 2026)

**Verdict: PROVED elementary finite and all-rank negative controls; unrestricted Erdős–Rado Sunflower Conjecture OPEN.** Every witness below is an ORIGINAL edge, not a reverse image under shifts. No literature-priority or complete-proof claim.

## AS1. Exact rectangle certificate loads (PROVED; PM1/PB1 must not be double-counted)

Fix an actual original anchor E of an s-free simple k-uniform family F, s>=3, and s distinct equal-rank traces T_1,...,T_s forming an s-sunflower inside E. Put R_i={A\E:A in F, A cap E=T_i}, n_i=|R_i|>0, N=product_i n_i. Each selection of s original residues B_i in R_i is INCOMPATIBLE with an original sunflower. For an outside vertex x define d_i(x)=#{B in R_i:x in B}. The number of actual selections for which x has partial multiplicity 2,...,s-1 is EXACTLY

    L_x = sum_{J subset [s], 2<=|J|<=s-1}
                 product_{i in J} d_i(x) * product_{i notin J} (n_i-d_i(x)).        (AS1)

This is a restatement in integer form of the earlier PM1 occupancy polynomial, NOT a new inequality. Since every selection has at least one defect, N<=sum_x L_x. A nonnegative vertex weight cover of THIS PARTICULAR rectangle is

    minimize sum_x w_x,  w_x>=0,
    subject to sum_{x: 2<=#{i:x in B_i}<=s-1} w_x >=1
               for EVERY (B_1,...,B_s) in R_1 x ... x R_s.                       (AS2)

Weak duality allows nonnegative weights y_{B_1,...,B_s} on selection tuples subject to sum_{tuple certified by x} y_tuple <=1 for each x. No normalization across *different anchors* is implicit. The precise per-vertex capacity L_x can equal N; a unit weight on such a vertex pays for N different selections. Conversely each original edge participates in up to product_{j!=i}n_j tuple selections at a fixed position i. This distinction also persists globally: a single edge belongs to one trace packet per fixed anchor (PL1), but can be reused under many anchors. AS1 does not replace the different PB1 pair-certificate capacity M_v=binom(|F|-2,s-2)-binom(deg(v)-2,s-2).

## AS2. Exact characterisation of a permanent single-vertex shield (PROVED)

Let s finite nonempty original residue packets R_1,...,R_s be any Cartesian box, irrespective of freeness. For x let I_i(x)={1_{x in B}: B in R_i} subset {0,1}. Define u(x)=#{i:I_i(x)={1}} and z(x)=#{i:I_i(x)={0}}. Then

    x has partial multiplicity in EVERY selection from product_i R_i
       iff u(x)>=2 AND z(x)>=1.                                                  (AS3)

Proof: the minimum attainable multiplicity is u, and the maximum is s-z, since packet choices are independent. Every attainable multiplicity lies in [2,s-1] iff u>=2 and s-z<=s-1. If either inequality fails, choices achieving the respective extreme give a selection not certified by x. This is an exact criterion for a SINGLE permanent witness; absence of such a vertex gives no information on whether a *union of alternative witnesses* covers every tuple.

If at least two packets force x inside and each packet has size between a and R a, then the subfamily consisting of those s packets (and no other edges) has a genuine original point link of size >=2a, hence fraction >=2/(sR). Adding arbitrary further edges invalidates the fraction; neither packet balance nor cover of a fixed fraction of the GLOBAL family has been proved above a density threshold. This elementary conditional positive observation does NOT yield a general rank recurrence.

## AS3. Smallest anchor-plus-singleton-traces alternating shield (PROVED, all s>=3)

Use pairwise distinct vertices e_1,...,e_s,a,b,c,u_3,v_3,...,u_s,v_s, and private padding points p_{i,t} as needed. Let E={e_1,...,e_s}. Define the following s-uniform ORIGINAL petals, using PRIVATE, pairwise-disjoint padding of length s-3 for EVERY listed petal (when s=3, no padding):

    A_1   = {e_1,a,b}       + private padding;
    A_2^a = {e_2,a,c}       + private padding;
    A_2^b = {e_2,b,c}       + private padding;
    A_i   = {e_i,u_i,v_i}   + private padding       for 3<=i<=s.

Let F_s^alt = {E,A_1,A_2^a,A_2^b,A_3,...,A_s}, of cardinality s+2, rank s. In the s nonempty trace packets T_i={e_i}, all packet sizes are 1 except |R_2|=2; the s singleton traces form an empty-core sunflower. The two possible ORIGINAL rainbow tuples are

    (A_1,A_2^a,A_3,...,A_s): exactly one partial defect a,
    (A_1,A_2^b,A_3,...,A_s): exactly one partial defect b.                       (AS4)

All private padding and u_i,v_i occur only once; c occurs once per tuple; all e_i occur once. Thus NO vertex is a permanent partial-multiplicity witness. But no rainbow choice is a sunflower.

The FULL original F_s^alt is s-free, not merely its displayed rainbow box. Among s selected edges that omit E, choosing BOTH A_2 variants gives a repeated trace e_2 while another selected petal has a different singleton trace: their pairwise intersections cannot all agree. Selecting at most one A_2 variant forces precisely one petal per trace, which fails by AS4. With E included, if any two chosen petals have different traces, their intersections with E differ; if every selected petal has the same trace, this is possible only for s=3 with both A_2 variants, but A_2^a cap A_2^b contains {e_2,c} whereas each meets E in {e_2}. This rules out ALL s-tuples. The family is simple and even has empty overall intersection.

Minimality, carefully scoped: for an actual original anchor E plus s NONEMPTY singleton-trace packets, if there are only s+1 total edges, every packet has one member, hence an incompatible unique rainbow tuple has a fixed defect vertex. Therefore any such example with no permanent single-vertex defect needs >=s+2 edges, and the displayed construction attains equality. Singleton traces require |E|>=s; the construction also attains rank k=s. This is NOT a classification of arbitrary s-free families or a global minimal counterexample to every possible rank lemma.

For s=3 the five original edges are

    E={e1,e2,e3}, A1={e1,a,b}, A2a={e2,a,c},
    A2b={e2,b,c}, A3={e3,u3,v3}.

Here the two original tuples have defects {a} and {b}. This explicitly falsifies "no permanent defect vertex implies a compatible rainbow original sunflower", already at rank 3.

## AS4. Tensor amplification without a permanent vertex; exact LP value 2 (PROVED)

Let Q be any nonempty simple s-free d-uniform ORIGINAL family with anchor D and an empty-trace original residue packet of cardinality h>=2. For every m>=1 set

    G_m=F_s^alt tensor Q^m,    anchor=E tensor D^m.

The s distinct trace packets T_i={e_i} (no auxiliary anchor point) have sizes

    (h^m, 2 h^m, h^m,...,h^m).                                             (AS5)

Their traces form a true s-sunflower. Every original selection of one edge from each packet retains in the seed factor one of the two incompatible tuples (AS4), so none is an original sunflower. Tensor freeness follows from the projection argument in TS4: equal pairwise intersections of s uniform tensor edges force every factor projection to be all identical or s distinct sunflower edges; since factors are s-free, all projections would be identical, contradicting distinctness. Rank of G_m is s+md and |G_m|=(s+2)|Q|^m.

The defect loads from AS1 for the TWO seed witnesses are exact:

    N=2 h^{ms},     L_a=L_b=h^{ms}=N/2.                                    (AS6)

Any selection certifies EXACTLY ONE of a,b in the seed block; other auxiliary defects may occur, but need not occur. In AS2, w_a=w_b=1 (all other weights zero) is feasible, giving objective 2. For the matching lower bound, choose the SAME auxiliary residue from the empty-trace packet in all s original petals; with the two different A_2 choices, the resulting s-tuples have defect sets exactly {a} and exactly {b}. Every feasible fractional cover must therefore satisfy w_a>=1 and w_b>=1. Thus

    OPT(AS2 for this s-packet rectangle)=2                                      (AS7)

for EVERY m, although every packet grows exponentially and N grows as 2 h^{ms}. No single outside vertex is permanent because the two displayed choices have disjoint defect sets. The obstruction persists after banning the earlier TS3 single-vertex shields. The bound 2 is a LOCAL rectangle cover, not a global multi-anchor bound; it is NOT evidence of independent rank savings.

Explicit factors: for s=3 choose the classical quadratic ternary cap Q9={(x,y,x^2+y^2 mod3)} with tagged coordinates, nine rank-three ORIGINAL edges and 4 empty-trace residues at anchor (0,0,0). Then G_m has rank 3+3m, size 5*9^m and packets (4^m,2*4^m,4^m). For s>=4 choose Q=P(s-1,1), singleton transversal factor with s-1 edges and h=s-2 at any chosen anchor. Then G_m has rank s+m, size (s+2)(s-1)^m and packets ((s-2)^m,2(s-2)^m,(s-2)^m,...). All density bases here are LOWER constructions, not upper bounds, and Q9 / P are prior art.

## AS5. Fixed-base rank-induction attempt and failure point (OPEN)

A proposed "permanent shield or lift" dichotomy is FALSE by AS3. Replacing it with "a bounded fractional defect cover or lift" is also insufficient: AS7 gives bounded cover 2 for an arbitrarily large shielded box with no compatible selection. A high-density theorem could still exploit a *large GLOBAL original link* (note that the seed a,b,c vertices each have seed degree 2, not high density), but to derive f_s(k)<=C_s^k it must quantitatively show that the selected link captures a fixed fraction of the entire original family at EVERY recursive step, or assign an explicitly bounded globally charged *nonseparable* potential. Merely quoting this assertion assumes a result essentially as strong as the conjecture.

A correct conditional implication is worth stating exactly: if constants D_s>=s-1 and phi_s>0 satisfy **for every** k>=1 and s-free ORIGINAL F of rank k with |F|>D_s^k some vertex x has deg_F(x)>=phi_s |F|, then induction on links gives |F|<=C_s^k with C_s=max(D_s,phi_s^{-1},s-1), including k=1 and the threshold equality by weak <=. This is a CONDITIONAL reformulation, NOT established. The previous maximal-matching link has only phi=1/((s-1)k), which does not close. Empty-trace packets retain rank k; for s>=4 proper traces have matching number <=s-2 but need not intersect. There is no derived unconditional rank recurrence.

A bounded-VC shortcut also remains blocked: Ge–Wang–Xu–Zhao (arXiv:2609.18995, Theorem 1.1) give (50ds)^k at VC dimension <=d, and Shangguan (arXiv:2609.30263) gives base O(s log(d+1)); for P(2,k), VC dimension is k and a large exponential subfamily must have d=Omega(k) by TS5. Neither theorem removes k from the base in that regime. Do not infer original petals from shifted-only Mishra v2.

Mandatory source/control check: classical P(s-1,k) has size (s-1)^k; Q9 is 3-free with nine triples; triangle tensor and prior-art Abbott–Hanson H54 (s3/rank4, 54, degree fraction 2/9), Axante et al. H39 (s4/rank3, 39, 3/13) and NONREGULAR H153 (s6/rank3, 153, 3/17) remain distinct adversarial density floors at 54^(1/4),39^(1/3),153^(1/3), with STRICT trigger inequalities and no upper-bound assertion. This study did not re-run full H54/H39/H153 enumerations or all earlier standalone repository audits because a full network checkout was unavailable.

## Reproducibility and status

Run `python3 scripts/alternating_shield_audit.py` and `python3 -m unittest tests.test_alternating_shield_audit -v` (or full discovery). The standalone finite audit checks the complete (s+2)-edge seeds for 3<=s<=9, exact defect switches and non-permanence; checks tensor packet counts and selected higher-rank s-free tensors, and independently checks small low-rank cases. Arbitrary s,m results are SYMBOLIC proofs above. Hosted repository CI must be green at the exact PR head before merge; no local clone of this public GitHub repository was available in the execution container.

**Final classification:** AS1 integer occupancy/capacity = PROVED earlier PM1, not new; AS3 criterion and example, AS4 all-rank tensor and local LP = PROVED deductions / no priority claim; "no single permanent shield suffices" = FALSE route; unrestricted original C_s^k induction = OPEN. This is a further negative diagnostic, not a resolution of the conjecture.
