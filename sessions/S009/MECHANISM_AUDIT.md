# SUN-PARENT-S009 — ONE fractional two-link LP-collapse lemma: FALSE for all r,k
2026-10-14. **STOP_NO_ACTIVE_CHILD**. Same-assistant symbolic reasoning, no independent referee or originality clearance.

## Definitions and quantified structural L
Fix arbitrary integers r>=3, k>=2; q=r-1. Let F be a finite simple k-uniform original family. For every (k-2)-set C, the original two-link graph G_C(F) has edges A\C for all A in F containing C. Define its fractional matching number nu*(G) by maximising the total nonnegative edge weight with vertex incident weight sums <=1. By graph LP duality it equals the fractional vertex-cover minimum tau*(G) = min sum y_v, with y_v>=0 and y_u+y_v>=1 for each edge uv.

**L(r,k) (proposed; FALSE):** For every such F that has NO r-sunflower, VC(F)>=k-1 and |F|>=q^k, and for EVERY (k-2)-set C with |F_C|>=q^2, tau*(G_C(F))<=q. The parameter C is the full ORIGINAL family link, not a selected H, with quantified original size. The premise and conclusion are independently checkable graph/VC numerical properties, not a restatement of existence of a sunflower or a BSEL/HDSE3, full-link moment or low-VC mass-selection condition.

### Exact conditional mathematical transfer
For k=2, a sunflower-free graph has max degree Delta<=q (otherwise r incident edges make a common-vertex sunflower) and ordinary matching number nu<=q (otherwise r disjoint edges make an empty-kernel sunflower). Any graph with >q^2 edges has VC>=1: VC=0 would imply that all vertices occur in either every edge or no edge, forcing at most one distinct 2-edge. Thus L applies with C=empty to any hypothetical >q^2-edge r-free graph. Take its optimal fractional vertex-cover y. Then
|E| = sum_edges 1 <= sum_edges(y_u+y_v) = sum_vertices deg(v)y_v <= q sum_vertices y_v = q tau*(G) <= q^2,
contradiction. So L would force the all-r **strict improvement** f(2,r)<=q^2 on the elementary 2q^2 bound obtained from endpoints of a maximal matching of <=q edges and Delta<=q. This would be a rank-2 improvement only, NOT a solved variable-rank Erdős–Rado transfer. L is false at k=2 and every k.

## Exact all-r cyclic graph counterfamily
Let n=2q+1 vertices indexed modulo n. For even q=2t take edges {i,i+d} for each i modulo n and d=1,...,t. For odd q=2t+1 take these edges for d=1,...,t AND q vertex-disjoint additional chords {i,i+q}, i=0,...,q-1. Chords are distinct from cyclic edges. Call this graph G_q.

It has maximum degree <=q, and precisely M_q=floor((2q+1)q/2)=q^2+floor(q/2)>q^2 edges (q even: n*q/2; q odd: n*(q-1)/2+q). On n=2q+1 vertices every matching has <=q edges. An r=q+1 petal sunflower of distinct 2-edges would necessarily be r disjoint edges or an r-star; both are impossible. Thus G_q is r-free. Every edge uv shatters the vertex pair {u,v}: min degree >=2 gives traces {u} and {v}; the edge uv gives {u,v}; and |E|>2q-1>=deg(u)+deg(v)-1 ensures a disjoint edge giving empty. As any 2-family has VC<=2, VC(G_q)=2.

Give EVERY edge weight 1/q. At any vertex the total incident weight is deg(v)/q<=1, hence a directly verified fractional packing gives
nu*(G_q)>=M_q/q=q+floor(q/2)/q>q.
This is an explicit certificate, not a conjectural matching-polytope optimum.

### All-rank tensor lifting, original F and real link
For s>=0 let P(q,s) be the q-ary one-symbol-per-coordinate product, P(q,0)={empty}. Define F_{q,k}=G_q tensor P(q,k-2) on disjoint vertex universes; each edge is a union of one graph edge and one q-ary word edge. Then F_{q,k} is simple k-uniform with M_q*q^(k-2)>q^k edges. VC(F_{q,k})=k: concatenate a shattered pair from G_q with one distinguished symbol in each of k-2 independent blocks, and k-uniformity is the upper bound.

No r sunflower appears: in an r-tuple whose pair intersections agree, projected edges of any equal-rank factor must either be all identical or all r DISTINCT sunflower edges; if two projected edges coincide, their full common intersection forces all others to coincide. Both G_q and P(q,s) are r-sunflower-free (P has only q<r choices per coordinate), so each factor projection is constant, forcing all global edges identical, impossible for a distinct sunflower tuple.

Pin C to exactly one selected symbol in EACH of the k-2 product blocks. Its FULL original link has M_q>=q^2 edges and exactly graph G_q as residual rank-two link. Then tau*(G_C)=nu*(G_q)>=M_q/q>q, violating L at ALL r>=3, ALL k>=2. q=2 gives C5 with 5 edges and fractional weight total 5/2>2; q=3 gives C7 plus three disjoint distance-3 chords, 10 edges and weight total 10/3>3. Finite degree/cardinality/VC spot checks for q=2,...,9 accompany the exact symbolic proof. The ordinary q-ary product alone has two-coordinate link K_(q,q) with tau*=q and DOES NOT refute L: genuinely distinct from the S008 Q-moment example.

## Original hub / P001A S051 adversarial stress
Coning F_{q,k-1} by a common new hub h (k>=3) creates a k-uniform sunflower-free original family with VC=k-1 and a G_q residual two-link when C consists of h and the k-3 coordinate choices. Its fractional capacity >q persists despite the original heavy hub; however its size is only M_q*q^(k-3)<q^k, so it is NOT a second full L counterexample. P001A S051's genuine normalized heavy-hub original-mass family has rich hub links but ordinary singleton J_x matching number 2<m and a near-complete SAME-F valid repair. Neither original hub richness nor fractional rank-two LP capacity establishes that a single FINAL H of adequate mass has all five exact in-H kernel certificates. Our proposed L never supplies final-H witnesses and is not a backdoor TIK theorem. See original P001A S051 proof.

## Targeted source priority and binary exit
Earliest classical matching-polytope competitor: Edmonds (1965); odd-cycle fractional matching integrality context predates this audit (see 1981 Integer and Fractional Matchings). BCW 2021 all-rank (Cr log k)^k remains the general benchmark, Ge–Wang–Xu–Zhao 2026 preprint already proves fixed-VC (50dr)^k, ECCC TR26-220 already O(w)-wise robust derandomisation; JJSW original-F is not final-H; Naslund–Sawin D-dependent is not the D-independent ASU implication. See S009_SOURCE_REGISTER and older registers. No-hit searches are not novelty checks.

**STOP_NO_ACTIVE_CHILD.** Exactly one L was rejected by a fully quantified all-r/all-rank counterfamily. No new sunflower upper bound, novel publishable intermediate, independent mathematical review, Lean, Palomar, manuscript, outreach, child proposal or reactivation. Next S010 is FUTURE-ONLY tenth programme audit, separate owner invocation.
