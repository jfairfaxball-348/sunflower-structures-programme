# Correlated ORIGINAL defect witnesses and k-partite entropy bridge — 15 October 2026

**STATUS: PROVED restricted original-family inequalities and exact no-go; full Erdős–Rado Sunflower Conjecture OPEN.** No novelty/priority claim. The classical q-ary product, Konig's bipartite theorem, ternary quadratic cap, and published 54/39/153 factors are prior art.

## 1. Actual ORIGINAL edge-tuple LP: exact optimum m/2 (PROVED)

Let s>=3, q=s-1 and m>=2. Take ORIGINAL finite simple transversal family P(q,m), comprising q^m vectors of m independently labelled q-symbol coordinate blocks; it avoids s original sunflower petals. For a tuple T of s DISTINCT ORIGINAL edges, let D(T) denote coordinates at which at least one symbol has multiplicity j in {2,...,s-1}. At each nonconstant coordinate, s entries chosen from only q=s-1 symbols necessarily contain a partial-multiplicity collision; a constant coordinate has none. Hence D(T) is EXACTLY the set of nonconstant coordinates.

If |D(T)|<=1, the tuple can have at most q distinct vectors, contradicting s=q+1. Thus |D(T)|>=2. Conversely for ANY pair i<j take the q vectors varying over a=0,...,q-1 at coordinate i and taking 0 elsewhere, together with one extra vector with 1 at j and zero elsewhere. These are s actual distinct ORIGINAL edges and their defect support is EXACTLY {i,j}.

Define an edge-tuple indexed coordinate LP:

    (E-LP-P) min sum_(h=1)^m w_h
             w_h>=0, sum_(h in D(T)) w_h >=1 for
             EVERY s-tuple T of distinct ORIGINAL edges.

Uniform w_h=1/2 is feasible, cost m/2. Every coordinate pair gives a real ORIGINAL tuple constraint w_i+w_j>=1; assign dual weight y_{ij}=1/(m-1) to one such tuple for each pair. Every coordinate has dual load exactly 1, and the objective is binom(m,2)/(m-1)=m/2. Thus **OPT=m/2 exactly**, all s>=3,m>=2.

This sharp original-edge tuple obstruction shows that coordinate-additive defect potentials alone cannot force unbounded distinct defect support on exponential-size original s-free families. It does NOT charge *joint rank drops*, dependent witnesses across multiple anchors, or reuse budgets. It does NOT disprove arbitrary nonlinear correlated schemes.

## 2. Original transversal PRODUCT-SUPPORT ENTROPY certificate (PROVED)

Let F be finite, nonempty, simple, ORIGINAL k-partite transversal and s-sunflower-free, s>=3, N=|F|. Identify original edges with distinct words. Let P be UNIFORM on F, p_i(a)=P(X_i=a), and Q=product_i p_i be the artificial independent-coordinate measure (do not assume original P is a product). Put

    theta=Q(F); eta=max_(x in F)Q(x);
    gamma_i=sum_a p_i(a)^s + s! sum_(a_1<...<a_s)prod_(j=1)^s p_i(a_j);
    Gamma=prod_i gamma_i; delta=sum_(x in F) Q(x)^s;
    T=sum_i H(p_i)-log N = D_KL(P||Q).

For s iid draws from Q, coordinate i has no partial-multiplicity defect iff all s symbols agree or all s are DISTINCT; this has probability gamma_i. Independence across coordinates holds for Q, so the all-coordinate no-defect probability is Gamma. A full s-word tuple without defects is either s identical words or s DISTINCT original sunflower petals: if some but not all words repeat, any coordinate distinguishing a repeated word from another has a partial multiplicity. Since F forbids distinct s sunflowers, the no-defect event inside F^s consists EXACTLY of diagonal tuples (x,...,x), Q^s-mass delta. Therefore

    (E3) theta^s <= 1-Gamma+delta
    (E4) theta^s <= 1-Gamma+eta^(s-1).

KL log-sum (restrict Q to F) yields theta>=exp(-T), hence

    (E5) exp(-s T) <= 1-Gamma+eta^(s-1).

A partial defect includes an equal pair at some coordinate, so by Q-union bound,

    1-Gamma <= binom(s,2) sum_(i,a)p_i(a)^2,

and

    (E6) exp(-sT) <= binom(s,2)sum_(i,a)p_i(a)^2+eta^(s-1).

E5/E6 can give a positive lower bound on total coordinate dependence T when the RHS is <1, a genuine original-family high-entropy/diffuseness alternative. Also P^s[no defects]=N^(1-s) exactly; data-processing KL yields the further correct

    (E7) sT >= d_bin(N^(1-s) || Gamma).

This does NOT prove any all-rank k-partite bound B^k. **Exact equality obstruction:** on P(q,k), q=s-1, P=Q uniform, theta=1,T=0,Gamma=delta=N^(1-s),eta=1/N, so E3, E4, E5 hold as EQUALITIES. There can be no uniform strict saving in this support/entropy certificate at the mandatory classical product floor.

## 3. Partite ranks 1–3 and obstruction to naive induction (PROVED, classical)

An s-free rank-1 simple family has at most s-1 edges. A k=2 partite transversal family is a bipartite graph with maximum degree<=s-1 (no s-edge original star) and matching number<=s-1 (no s-edge original empty-core sunflower). Konig's theorem gives a vertex cover of size <=s-1, so edges <=(s-1)^2, with equality at K_(s-1,s-1)=P(s-1,2): **f_s^partite(2)=(s-1)^2.**

The classical nine-point quadratic cap

    F9={(x,y,x^2+y^2): x,y in F_3}

is 3-partite 3-free with N=9>2^3. Over F_3, coordinate values are all equal or all distinct exactly when their sum is 0; three distinct sunflower words would therefore form an affine line. A line contained in this quadratic graph forces a^2+b^2=0 for its nonzero first-two-coordinate direction (a,b), impossible since -1 is nonsquare in F_3. Thus a naive all-partite product cardinality bound (s-1)^k and its rank induction are FALSE. Cap sets are pre-existing mathematical prior art.

## 4. Failed global routes and tensor guards

E-LP-P is a fully original-edge-tuple LP but lacks joint rank-drop costs. No rigorous original multi-anchor rank-drop budget was obtained. Matching once via a maximal matching gives previous MH1 with (s-1)k one-rank cost; after deleting a common core the matching number may increase, so no persistent matching index is claimed. For s>=4, proper exact-trace residues have matching number<=s-2, NOT necessarily intersecting.

The unrestricted density-sensitive point link |F|>D^k => max_x deg(x)/|F|>=phi with fixed positive explicit D,phi would itself prove C_s^k by link induction, so **no unrestricted nonvacuous such pair is established**. Required strict tensor tests: H54 (s3) has density root 54^(1/4), point fraction 2/9; H39 (s4) root 39^(1/3), without claiming anchor regularity; H153 (s6) root 153^(1/3), point fraction 3/17 and NOT anchor regular. All s>=3 have P(s-1,k) density base s-1. For D strictly below the respective base, any phi above the corresponding verified point-degree fraction is refuted by tensor powers. No extra spectral/rank gain is inferred.

## 5. Audit and research ledger

Standard-library script scripts/correlated_partite_audit.py enumerates original tuples for s=3..6 small k, verifies exact pair witnesses, rational E3/E6 inequalities and q-product equality, the nine-point cap, and all 512 subfamilies of the 3x3 rank-two grid (max 3-free size 4). Five independent unit tests include deliberate rejection of a true sunflower. Finite evidence is not a universal proof; the symbolic arguments above carry the all-rank claims.

**PROVED:** actual-edge LP m/2 primal/dual; original transversal entropy-support E3–E7; classical rank-two partite bound; cap-set original witness.
**FALSE:** >2 necessary defect coordinates per s-tuple of original q-product edges; universal all-partite bound (s-1)^k; strict E3/E5 entropy savings at classical product equality.
**CONDITIONAL:** a different, nonadditive, globally charged multi-anchor original rank-drop potential might close an induction, but no such theorem is established.
**OPEN:** unrestricted fixed-base C_s^k, nonvacuous unrestricted original density-sensitive point link, original all-rank partite B^k, compatible joint rank-drop amortisation.

Source audit: Mishra arXiv:2606.02667v1 has invalid cumulative original-source lifting and a false O_s(2^k) universal bound for s>=4; v2 is SHIFTED only. Abbott–Hanson and Axante et al. arXiv:2609.06175 finite factors credited as prior art; Rao, *The story of sunflowers* (JLMS, 2026), and Bell–Chueluecha–Warnke (2021) provide robust-sunflower context and the reliable O_s(log k)^k unrestricted baseline. No novel-priority or solved claim.
