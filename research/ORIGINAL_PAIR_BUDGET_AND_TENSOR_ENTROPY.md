# Actual-original edge-pair certificates, tensor budgets and entropy limits (15 October 2026)

**PROVED**: an all-original tuple/pair/vertex fractional cover and exact capacity dual, a universal quadratic lower bound, and an explicit all-rank binary product upper bound. **FINITE TEST**: factor examples, rank boundaries and optional LP optimisations. **OPEN**: a globally nonovercounting rank-drop recurrence, a nonvacuous high-density original link, and the unrestricted Erdős–Rado Sunflower Conjecture. This work makes no literature-novelty assertion. Published 54/39/153 factors and the nine-point cap are NOT original discoveries.

## 1. A genuine multi-edge witness LP (PROVED, every fixed s >= 3)

Let F be an ORIGINAL finite simple s-sunflower-free family of N >= s sets of rank k, not necessarily partite. For distinct A,B in F and an original ground vertex v in A intersect B define an ORIGINAL pair certificate c=(v,{A,B}). For an unordered s-subset S of F, c **covers** S iff A,B are in S and some C in S misses v. There is no certificate just because a shifted ancestor or a hypothetical residue exists.

An s-subset S is an original sunflower iff each vertex has multiplicity 0,1 or s in its members. Since F is s-free, some v has multiplicity j in {2,...,s-1} in S. Two of its j owners and an original missing edge provide a certificate. Thus every S is covered.

Define the ACTUAL-EDGE pair LP:

    Lambda_s(F) = min sum_c x_c
    subject to x_c >= 0 and sum_{c covering S} x_c >= 1
    for EVERY unordered s-subset S of distinct ORIGINAL edges.

This does **not** double-count a particular certificate: its exact capacity is the number of S it covers. Write d_v=number of edges containing v. A certificate at v has precisely

    M_v = binom(N-2,s-2) - binom(d_v-2,s-2)                 (PB1)

covered s-subsets, with binom(a,b)=0 for b>a. The second term counts s-subsets where all other original edges also contain v. Define M=max_{v:d_v>=2} M_v; then M>0 because F is s-free and N>=s. The explicit dual giving weight 1/M to every s-subset is feasible: each certificate receives total load M_v/M <=1. Hence

    Lambda_s(F) >= binom(N,s)/M >= N(N-1)/(s(s-1)).         (PB2)

The second inequality uses M <= binom(N-2,s-2). This is a **universal quadratic-size lower bound** for this deliberately defined LP, not an upper bound on F. Neither anchor selections nor fictitious shifted petals enter PB1/PB2. If N<s, constraints are absent and Lambda=0; rank-one P(s-1,1) has exactly that case.

**No automatic rank savings:** PB2 grows as N^2 in every s-free family with N>=s. An assertion that this raw LP proves exponential decay after normalising by N^2 is false on the tensor sequence below. To obtain a sunflower theorem, an augmented LP must attach real rank drops, charge each reused original witness in a globally conserved way, and derive an upper bound with a *strictly incompatible* N- and k-dependence. PB1 alone does none of these.

## 2. Sharp-scale all-rank binary-product obstruction (PROVED)

Take P(2,m), the classical 2^m original words (one vertex from each binary part), s=3, m>=2, N=2^m. It is 3-sunflower-free. The certificate c=(i,{A,B}) exists exactly when the two distinct binary words agree in coordinate i.

**Dual.** A pair agreement has d_i=N/2, so exactly N/2 distinct original third words miss its coordinate symbol. Assign y_S=2/N to EVERY triple. It has exactly unit load on EACH certificate and yields

    Lambda_3(P(2,m)) >= (N-1)(N-2)/3.                     (PB3)

**Primal.** For each such certificate c let d(A,B) be the Hamming distance of the actual original words, and set x_c=1/(d(A,B)+1). This weight uses full two-edge geometry, not merely a coordinate-additive constant. To prove feasibility, fix three distinct binary words A,B,C and let a,b,c count coordinates of the respective patterns A=B!=C, A=C!=B, B=C!=A. Their sum t=a+b+c >=2 (all other coordinates are unanimous). Pair distances are b+c,a+c,a+b. The total weight covering this actual triple is

    a/(b+c+1) + b/(a+c+1) + c/(a+b+1).                    (PB4)

For t=2 distinctness implies (a,b,c) is a permutation of (1,1,0), giving 1. For t>=3 Cauchy-Schwarz and sum a^2 >=t^2/3 give

    sum a/(t-a+1) >= t^2/[t(t+1)-sum a^2]
                   >= t/(1+2t/3) >= 1.

Thus PB4 is always >=1. At Hamming distance d there are N binom(m,d)/2 unordered pairs, each with m-d agreement coordinates. Using binom(m,d)(m-d)/(d+1)=binom(m,d+1), the primal objective is exactly

    (N/2) sum_{d=1}^{m-1} binom(m,d+1)
      = N(N-m-1)/2.                                      (PB5)

Combining gives for every m>=2:

    (N-1)(N-2)/3 <= Lambda_3(P(2,m)) <= N(N-m-1)/2.      (PB6)

Consequently the fully original-pair indexed optimum is THETA(N^2), with normalised limits bounded between 1/3 and 1/2 (asymptotically). The LP can amortise reuse across s-tuples but has no intrinsic exponential *per-rank* saving on this real original tensor construction. This is an exact no-go for PB1-PB5 as a standalone bridge, NOT a no-go for a new nonlinear joint-rank-drop dual. The product P(s-1,m) for s>3 also obeys PB1/PB2; binary-specific primal PB4 is not asserted for q>2.

Independent finite checks give the following **solver outputs** for the exact edge-pair LP (SciPy HiGHS; not a universal proof): P(2,2), s=3: 2; P(2,3), s=3: 16; P(2,4), s=3: 256/3; nine-point ternary quadratic cap, s=3: 20; P(3,2), s=4: 9; P(4,2), s=5: 24. The symbolic PB3/PB5 are separately verified with exact Fraction arithmetic for m=2,3,4. Rank 1 has N=s-1<s and empty constraints; rank 2 and rank 3 controls do not presuppose an invalid partite (s-1)^k recurrence.

## 3. Averaged published-factor controls (EXACT identities, not per-anchor regularity)

For any finite original family Q on N members with vertex degrees (d_v), the total number of distinct pair certificates is exactly sum_v binom(d_v,2). For triples, the sum of certificate-to-triple incidences (whether or not Q is 3-free) equals sum_v binom(d_v,2)(N-d_v). Under m disjoint-block tensor powers Q^m, an original vertex (block j,vertex v) has degree d_v N^(m-1), so the total pair certificates are exactly

    m sum_v binom(d_v N^(m-1),2).                         (PB7)

These are GLOBAL averaged spectra. They do not assert each anchor has the same link or charge.

The published Abbott–Hanson 54-edge rank-four factor H54 (s=3) has 18 vertices of degree 12: 1188 certificates, 49896 triple incidences, with tensor vertex fraction 2/9. The published Axante et al. 153-edge rank-three factor H153 (s=6) has degree histogram 15 vertices of degree 27, 10 of degree 5 and 1 of degree 4: 5371 certificates, 679084 triple incidences, with maximal fraction 3/17. H153 is emphatically NOT degree-regular, and its triple incidences are not s=6 sunflower certificates by themselves. At s=6 its PB1 capacity uses binom(N-2,4)-binom(d_v-2,4). H39 has max vertex fraction 9/39=3/13. These verified profiles preserve the strict tensor controls: any universal high-density link D,phi with D below the relevant published tensor root and phi above its maximum vertex fraction is FALSE. At D exactly the tensor root the strict inequality |F|>D^k does not trigger; no endpoint verdict follows.

## 4. Why anchor-entropy and product-support savings do not close (PROVED)

For ANY original finite F of N edges, fix an actual anchor E and put U=A intersect E for A uniform in F; n_U=number of original edges with trace U. Exact entropy chain rule, without independent coordinates, gives

    log N = H(U) + sum_{U} (n_U/N) log n_U.                (PB8)

Each nonempty trace class is an original s-free rank-(k-|U|) residue after removing U. PB8 is a tautological accounting identity, not a decrement. For P(q,k) anchored at the all-zero word, U is a Bernoulli(1/q) mask, n_U=(q-1)^(k-|U|), and equality reduces to

    log q = h(1/q) + (1-1/q)log(q-1)                     (PB9)

per coordinate (0 log 0 interpreted as zero at q=2). No original-witness rank credit appears after including the entropy price of choosing U.

The previously verified artificial-product certificate E3/E5 is exact on q-product but can also become arbitrarily VACUOUS on genuine larger-base factors. For the CLASSICAL quadratic 3-partite cap F9={(x,y,x^2+y^2) over F_3}, tensor powers F9^m have k=3m, |F|=9^m, original P supported on 9^m words, coordinate marginals uniform ternary, theta=3^(-m), total correlation T=m log 3, Gamma=27^(-m), and delta=2187^(-m). Hence E3 reads

    27^(-m) <= 1-27^(-m)+2187^(-m),                      (PB10)

which becomes weaker rather than accumulating a noncircular strict per-block loss. E5 similarly has left side 27^(-m) and right side approaching 1. This does not invalidate the inequalities; it refutes that **alone** they supply a blockwise entropy decrement above the 2^k product floor.

## 5. Maximal-matching MH1 and genuinely open rank induction

A maximal ORIGINAL matching has <=s-1 edges and its union covers F by <=(s-1)k points. Assign each original edge to the first such point: this is a once-counted original partition, but a one-rank link term still costs (s-1)k and gives no fixed-base induction. Moreover deleting a common core does NOT preserve matching number: for F={{x,a},{x,b}} (3-free), original matching number is one; after deleting x, residues {{a},{b}} have matching number two. For s>=4 proper exact-trace residues only have matching number <=s-2, NOT necessarily intersecting.

The natural conditional high-density link assertion |F|>D^k implies some original vertex degree >=phi|F| would, if actually proved with fixed D,phi>0 independent of k, give f_s(k)<=max(D,1/phi)^k by induction (up to the strict boundary). This is essentially a solution, so it MUST NOT be installed as an unproved premise. Rank-one, bipartite rank-two and rank-three cap checks are essential. The H54, H39 and H153 thresholds above refute several candidate numerical constants strictly below tensor floors.

**VERDICT.** A new real-witness LP and correlated binary primal/dual are proved; the result diagnoses one more precise barrier. There is NO all-k original recurrence and NO full sunflower proof. Successor should budget true simultaneous rank drops and entropy across disjoint original trace packets, not recycle PB1 as if it were exponential gain.

Sources: Mishra v1 https://arxiv.org/html/2606.02667v1 (invalid cumulative transfer), v2 https://arxiv.org/html/2606.02667v2 (shifted families); Abbott–Hanson via Axante et al. https://arxiv.org/abs/2609.06175 ; Bell–Chueluecha–Warnke https://doi.org/10.1016/j.disc.2021.112367 ; Rao 2026 https://doi.org/10.1112/jlms.70380. No originality or solution announcement.
