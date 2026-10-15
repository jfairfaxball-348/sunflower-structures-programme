# Nonproduct ORIGINAL witness correlation: strict tensor synergy (15 October 2026)

**Mathematical status.** A universal tensor-superadditivity lemma is PROVED. An exact rank-six original-family certificate gives a STRICT inequality 8 > 3+3 (computer-assisted finite proof with two independent stdlib enumerations). A general original-owner density-transfer lemma is PROVED. No fixed-base original-family rank recurrence has been obtained, and the full Erdős–Rado Sunflower Conjecture remains OPEN. Literature priority NOT CHECKED.

## 1. All-anchor original ground LP and a genuinely nonseparable functional

Let H be an ORIGINAL simple k-uniform s-sunflower-free family. A record is a genuine anchor E in H, s distinct nonempty same-cardinality exact traces T_i=A_i intersect E forming a sunflower, and s distinct ORIGINAL edges A_i in H\{E} with the indicated traces. The defect set D_r consists of actual vertices outside E occurring in between 2 and s-1 of the A_i. Each D_r is nonempty, else the original petals form a sunflower. The LP is

  V_s(H) = min sum_{x in union H} w_x, w_x>=0, sum_{x in D_r} w_x>=1 for EVERY original record r.

The exact dual assigns y_r>=0 with sum_{r:x in D_r}y_r<=1 for EVERY actual ground vertex x, and maximizes sum_r y_r. Actual original edge owners are E,A_1,...,A_s; never replace them by hypothetical shifted witnesses. We use ALL anchors, not a favorable one.

For two disjoint-ground ORIGINAL families H and K define the normalized cross-factor interaction
  J_s(H,K) = [V_s(H tensor K)-V_s(H)-V_s(K)] / (|H| |K|).
All |H||K| actual original product edges occur in this denominator; there is no selected-packet normalizer. J can see coupled defect incidence, is NOT an entropy proxy or a count of fake edge owners, and is nonconstant on s-free tensors (see exact calculation below).

**Theorem NC1 (PROVED).** For any two nonempty ORIGINAL simple uniform s-free families H,K on disjoint ground sets, their tensor family is s-free and V_s(H tensor K)>=V_s(H)+V_s(K), hence J_s(H,K)>=0.

**Proof.** If s distinct tensor edges had common pairwise intersection, then in each factor their projections have equal pairwise intersections. For uniform sets, a collection of s projections with equal pairwise intersections is either all identical or s distinct members of an s-sunflower: if two coincide at A, then all other projections must contain A, so equality of ranks forces all to equal A. As both factors are s-free, all projections in each factor must coincide, contradicting distinct tensor edges. Now lift EACH actual H-record by attaching the SAME actual K-edge to its anchor and s petals. The lifted exact traces remain nonempty equal-rank sunflower traces (each gets the entire fixed K-edge), and the defect set is exactly the H-defect set. Consequently restriction of any feasible tensor-LP weight to H-ground vertices is feasible for the full H LP. Symmetrically its restriction to K-ground vertices is feasible for K. Since the ground blocks are disjoint the total cost is at least their sum. QED.

This theorem does not produce a sunflower: its LP has no established useful upper or lower comparison with f_s(k).

## 2. A strict concrete global example (COMPUTER-ASSISTED EXACT FINITE PROOF)

Put s=3. The alternating seed S has five ORIGINAL rank-3 edges
 E={e1,e2,e3}, A1={e1,a,b}, A2={e2,a,c}, A2'={e2,b,c}, A3={e3,u,v}.
The nine-edge rank-3 quadratic ternary cap is Q={(x,y,x^2+y^2 mod 3):x,y in F_3}, with three tagged coordinate positions. The 45-edge tensor T=S tensor Q has rank six and 17 physical ground vertices. Direct enumeration checks all three families are 3-sunflower-free.

**Theorem NC2 (PROVED finite by exhaustive exact certificates).**

  V_3(S)=3,  V_3(Q)=3,  V_3(T)=8, and J_3(S,Q)=2/45 >0.

For S the only distinct record defects are {a},{b},{c}. For Q exactly 20 all-anchor records produce 7 distinct defect sets including the three singleton defects {(0,0)}, {(1,0)}, {(2,1)}; these three singletons both force a lower bound 3 and hit all 7 defect sets.

For T, enumerate all 45 actual anchors, all NONEMPTY same-size trace-sunflowers, and all combinations of their real original packets. There are exactly 6403 **labelled actual records** and 457 distinct defect sets (6 singleton, 28 doubleton, 100 triple, 171 quadruple, 121 quintuple, 31 sextuple). Here and below A: and B: distinguish factor vertices. A feasible primal hitting set of cardinality EIGHT is

 W={A:a,A:b,A:c,A:e3,A:u, B:(0,0),B:(1,0),B:(2,1)}.

The standalone stdlib audit checks W intersects EVERY one of the 457 actual defect sets. An exact feasible dual with eight unit weights is furnished by the following eight PAIRWISE DISJOINT, ACTUALLY ATTAINED defect sets:

 D1={A:a}; D2={A:b}; D3={A:c};
 D4={B:(0,0)}; D5={B:(1,0)}; D6={B:(2,1)};
 D7={A:u,A:v,B:(0,1),B:(1,1)};
 D8={A:e1,A:e3,B:(0,2),B:(1,2),B:(2,2)}.

The audit finds an actual anchor plus THREE distinct actual original petals with equal nonempty sunflower traces yielding exactly EACH D_i. No vertex appears in two D_i, so dual capacity at every actual ground vertex is <=1. Weak duality yields 8<=V_3(T)<=8, giving equality exactly. The independent test instead directly iterates all (anchor, unordered original edge triple) combinations and confirms the same 6403 records and 457 defects without using the packet grouping enumeration. These finite witnesses show *strict* extra original multi-anchor certificate cost not decomposable into independent factor LPs.

For comparison tensor S with a one-edge uniform family: records correspond exactly to those of S, V does not change, and J=0. Thus J is genuinely nonconstant on s-free product families; unlike HD1's within-coordinate averaging, product factor symmetry DOES NOT make the functional universally additive.

**Iterated nonclosing lower bound.** By NC1, V_3(S tensor Q^m)>=V_3(S tensor Q)+(m-1)V_3(Q)=3m+5 for all m>=1. The rank is 3+3m, cardinality 5*9^m, and every tensor is 3-free; even strict tensor synergy therefore grows only LINEARLY with rank. Counting this cost as an exponential rank saving would be invalid.

## 3. Explicit density-sensitive transfer with actual owner reuse (PROVED)

Fix ANY original s-free family H with N edges. For a feasible dual y, let Y=sum_r y_r and for each ORIGINAL edge h put
 m_h=sum_{r: h belongs to {anchor, selected s petals} of r} y_r,
 M(y)=max_h m_h.
For EVERY ORIGINAL subfamily F subset H of size n, retaining just records ALL of whose s+1 actual owners belong to F preserves defect dual feasibility (same physical right vertices). Deleting a record is charged at most once per missing original edge, therefore

  V_s(F) >= max(0, Y - sum_{h in H\F} m_h)
         >= max(0, Y-(N-n)M(y)).                        (NC3)

If y is optimal Y=V_s(H), then the normalized owner congestion
  lambda(y)=N M(y)/((s+1)Y),  lambda>=1 when Y>0
gives V_s(F)>=V_s(H)*max(0,1-(s+1)lambda(1-n/N)).
The factor lambda, not merely defect mass or entropy, records global original-edge reuse. HD3 is recovered when a full product's canonical dual has perfectly balanced edge-owner load (lambda=1). This is an explicit theorem for all original families; a useful density threshold requires separately demonstrating an adequately balanced dual.

There is also a NO-BALANCE average corollary (NC4): for a uniformly chosen n-subset F of H, if N>=s+1,
  E[V_s(F)] >= ((n)_{s+1}/(N)_{s+1}) V_s(H).
Proof: each actual record has s+1 DISTINCT owners; its survival probability is precisely the indicated falling-factorial ratio, and its restricted dual remains feasible. Therefore at least one n-edge subfamily attains this bound. For n<s+1 it is zero, consistent with no records. This is an existence/mean result, NOT a bound for every chosen F. In the displayed eight-unit T dual, the 32 owner incidences involve 15 original edges and maximum original-owner load is 5, with lambda=225/32; NC3 is weak for arbitrary moderate-density subfamilies. This concrete imbalance demonstrates why the HD3 full-product symmetry argument cannot simply be transferred to T.

## 4. Recurrence and aggressive adversarial controls

The correct ORIGINAL link identity is deg_F(x)=|F_x| <= f_s(k-1) whenever F has rank k>=1, and thus, writing theta(F)=max_x deg_F(x)/|F|,
   |F| <= f_s(k-1)/theta(F).
The elementary maximal-matching bound gives theta(F)>=1/((s-1)k), hence f_s(k)<=(s-1)k f_s(k-1): factorial, NOT fixed base. NC1–NC4 do NOT improve theta(F) for arbitrary original families above a nonvacuous base D_s. Any proposed universal recurrence f_3(k)<=2 f_3(k-1) already fails at k=2: f_3(0)=1, f_3(1)=2, and f_3(2)=6. Proof of the latter: a 3-free graph has max degree<=2 (else a 3-star) and matching number<=2 (else empty-core sunflower). A maximum matching of size nu<=2 covers all graph edges; at most 4nu-nu=3nu<=6 edges have an endpoint in its 2nu matched vertices (subtract the double count of each matched edge). Two disjoint triangles attain six.

For any uniform one-step recurrence f_s(k)<=c f_s(k-1) valid from a fixed rank onward, tensor powers of any rank-d s-free H with M edges force c>=M^(1/d), since f_s(dm)>=M^m. In particular the classical P(s-1,k) demands c>=s-1. Published Abbott–Hanson H54, Axante H39 and nonregular H153 demand c>=54^(1/4), 39^(1/3), and 153^(1/3) for their respective petal counts; the rank-two two-triangle factor demands c>=sqrt(6) for s=3. Such a recurrence has NOT been proved at any admissible coefficient.

Additional approaches checked critically: a balanced-owner bound M=O_s(Y/N) would extend NC3 but is not proved; for T the exhibited dual has lambda=225/32. Weighted dependent random choice on actual owner hypergraphs requires a nonvacuous global degree/rectangle-supply hypothesis not furnished by sunflower-freeness. A certificate bound that merely grows O(k) on tensor products cannot generate an exponential saving; no shift of original petals is licensed by Mishra's shifted theorem. The pairwise LP is not a new source of original-versus-shifted lifting.

## 5. Low-rank and source controls

At rank zero there is only the single empty original edge, hence f_s(0)=1 and no distinct s-petal original sunflower; at rank one f_s(1)=s-1. Empty CORES count; empty or repeated PETALS do not. The script checks zero/one-rank degenerate records, rank-two disjoint triangles, AS3, cap9 and the rank-six tensor. All E, A_i and defects are original and physically grounded, with NO ghost owners. The symbolic P(q,k) obstruction remains valid for s=3,4,6 and k=0..3; no full published-factor enumeration is alleged for H54, H39 or H153.

Verified version-specific inputs: [Mishra v1](https://arxiv.org/html/2606.02667v1) states a universal base-two consequence, contradicted for s>=4 by P(s-1,k), and uses an invalid multi-shift original-ancestor transfer. [Mishra v2](https://arxiv.org/html/2606.02667v2) concerns SHIFTED families only, not an unrestricted original theorem. [Bell–Chueluecha–Warnke](https://arxiv.org/abs/2009.09327) and [Rao 2026 survey](https://doi.org/10.1112/jlms.70380) present the established O_s(log k) base regime. [Axante et al.](https://arxiv.org/abs/2609.06175) are sources for the finite lower constructions, not claimed original here. [Ge–Wang–Xu–Zhao](https://arxiv.org/abs/2609.18995) and [Shangguan](https://arxiv.org/abs/2609.30263) are bounded-VC original-family bounds whose base depends on d, so d~k does not supply a fixed base. Priority of NC1–NC4 beyond programme notes is NOT CHECKED.

**Verdict:** NC1/NC3/NC4 are proved exact elementary lemmas. NC2 is an independently double-enumerated, integer primal/dual certified 45-edge finite original obstruction. Fixed-base f_s(k)<=C_s^k and the unrestricted Mishra v2→original bridge remain OPEN.