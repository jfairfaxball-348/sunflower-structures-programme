# Central original traces, fractional anchor duality and non-closing rank recurrence (15 October 2026)

**Verdict:** PROVED an exact original-family central-trace theorem, a 3-petal rank recurrence with known factorial-growth upper envelope, sharp fractional anchor-cover lower bounds for tensor examples, and exact overlap/moment diagnostics. FALSE: any inference of a constant-base upper bound from these recurrences, or a bounded *total* anchor budget for these tensor models. OPEN: the full Erdős–Rado Sunflower Conjecture for ORIGINAL petals. No literature novelty priority is asserted.

## A. Exact-trace compatibility at central levels (PROVED)

Let F be a finite simple k-uniform s-sunflower-free ORIGINAL family, s>=3; fix E in F and any proper U subset E, **including U=empty**. Define R_U={B\U : B in F, B intersect E=U}. Then R_U is simple, s-free, (k-|U|)-uniform and has matching number at most s-2. If s-1 residues were disjoint, their original lifts B together with the distinct anchor E would form s sunflower petals with exact core U. This proof is independent of shifting, intersection assumptions, global core or ambient ground-set size. When U=empty the rank does NOT descend.

In particular, for s=3 every R_U is pairwise INTERSECTING. Therefore, with i_s(j) the maximum size of an intersecting original s-free rank-j family and i_3(0)=1,

    |F(E,U)| <= i_3(k-|U|)  for all proper U subset E.        (A1)

For arbitrary s>=4 and t=k-|U|>=1, choosing a maximal matching in R_U and partitioning by first vertex in its <=(s-2)t-point union gives

    |F(E,U)| <= (s-2)t i_s(t).                               (A2)

This is a valid central-trace bound even for |U|=Theta(k); no witnesses or near-face swaps are needed. A2 is not a bounded coefficient for growing t. The U=E class consists only of E itself.

Define the honest exact-trace generating polynomial

    W_E(z)=sum_{B in F} z^|B intersect E|
          =sum_{u=0}^k z^u sum_{U subset E, |U|=u}|F(E,U)|.  (A3)

When F is INTERSECTING and s=3, the zero coefficient vanishes, [z^k]W_E=1, and

    [z^u]W_E <= binom(k,u)i_3(k-u), 1<=u<k.                (A4)

Thus a genuine lower-rank ORIGINAL recurrence is proved:

    i_3(k) <= sum_{u=1}^k binom(k,u)i_3(k-u),  i_3(0)=1.  (A5)

Define b_0=1, b_k=sum_{u=1}^k binom(k,u)b_{k-u}. Its exponential generating function satisfies B(x)=1+(e^x-1)B(x), hence B(x)=1/(2-e^x). Therefore i_3(k)<=b_k, and b_0,...,b_5=1,1,3,13,75,541. Its asymptotics b_k~k!/[2(log 2)^(k+1)] are FACTORIAL, not C^k. Substitution of i_3(j)<=C^j for lower ranks in A5 yields (C+1)^k-C^k, which eventually exceeds C^k. The missing issue is pricing exponentially many different CENTRAL traces, not lack of descent for a *fixed* trace. This bound is weaker than published bounds.

FALSE closure statements have concrete ORIGINAL witnesses. F={{x,a,b},{x,c,d}} is 3-free and intersecting, yet deleting common x gives two disjoint residues. For s=4 the three edges E={0,1}, B1={0,2}, B2={0,3} form a 4-free family; the R_{0}(E) residues {2},{3} are disjoint. Proper residues are guaranteed intersecting specifically for s=3, not s>=4.

## B. Central-trace tensor polynomials and the entropy price (PROVED)

For an arbitrary F set P_E(z)=W_E(z)/|F| and Z_F(z)=|F|^(-2)sum_{E,B in F}z^|E intersect B|. Then Z_F=|F|^(-1)sum_E P_E. For disjoint-block tensor products P factors at each anchor and Z_{Q tensor R}=Z_Q Z_R. DO NOT assume a common anchored profile without checking it.

Let T be the three 2-edges of a triangle, and Q the q=s-1 disjoint singleton edges. I_m=T tensor Q^m is intersecting, s-free, has EMPTY common core, rank k=m+2 and |I_m|=3q^m. For every ORIGINAL E,

    W_E(z)=z(2+z)(q-1+z)^m,
    P_E(z)=z(2+z)/3 * ((q-1+z)/q)^m.                  (B1)

Each fixed trace with j agreeing q-blocks has (q-1)^(m-j) original edges; there are binom(m,j) such coordinate trace patterns for each triangle trace. Typical j=m/q+o(m) is CENTRAL. The exact entropy bookkeeping is

    h(1/q)+(1-1/q)log(q-1)=log q,                      (B2)

where h(p)=-p log p-(1-p)log(1-p). The rank drop from fixing one trace is paid back by exp(m h(1/q)) different central patterns; this is the binomial theorem, not an unpriced 2^k error. |E intersect B|/k -> 1/q in probability uniformly over anchors.

For the PUBLISHED Abbott–Hanson three-free 54-edge rank-four factor H54, an independent all-54-anchor enumeration gives the SAME per-anchor count polynomial

    27+12z+10z²+4z³+z⁴.                                 (B3)

Hence in I_m=T tensor H54^m (k=4m+2, N=3*54^m),

    W_E(z)=z(2+z)(27+12z+10z²+4z³+z⁴)^m,
    Z_{I_m}(z)=z(2+z)/3*((27+12z+10z²+4z³+z⁴)/54)^m.  (B4)

Exact mean overlap is 4/3+(8/9)m. Bounded independent coordinates imply central overlap (8/9)m+O_P(sqrt m), central fraction 2/9 of rank. The H=1 original low-trace reservoir is EXACTLY 2*27^m edges per anchor.

The PUBLISHED Axante et al. six-free H153 factor has ordered overlap histogram (14210,7350,1696,153), total 23409. Consequently

    Z_{T tensor H153^m}(z)=z(2+z)/3
       *((14210+7350z+1696z²+153z³)/23409)^m,         (B5)

and mean overlap 4/3+(11201/23409)m. This is an AVERAGED ordered profile, NOT a claim that every H153 anchor has the same overlap polynomial. For z=1/2 the two exact energy values are

    Z_{T tensor H54^m}(1/2)=(5/12)(577/864)^m,
    Z_{T tensor H153^m}(1/2)=(5/12)(2875/3672)^m.   (B6)

For 0<z<1, Markov on z^X gives Pr(X<=H)<=z^(-H) Z_F(z) for X=|E intersect B| with E,B uniform. Exponential moment decay means LOW trace mass is scarce: it does not generate a positive original opposite-trace reservoir. This distinguishes correlation decay from the mass-transfer direction required for induction.

## C. Sharp fractional anchor cover (PROVED / exact no-go)

For any F and integer H>=0, set M_H(E,B)=1 if |E intersect B|<=H and 0 otherwise. A nonnegative fractional anchor cover consists of lambda_E>=0 with sum_E lambda_E M_H(E,B)>=1 for EVERY B. Put p_E=|{B:M_H(E,B)=1}|/N and pmax=max_E p_E. Averaging the inequalities over B yields

    sum_E lambda_E p_E >=1,  hence sum_E lambda_E >=1/pmax. (C1)

This is fully normalised and ground-set independent. If all anchors have the same p_E=p and M_H is symmetric, the uniform weights lambda_E=1/(Np) meet ALL coverage constraints with equality, and achieve optimal total weight 1/p. This happens for B1 and B4, whose full anchored spectra are constant.

At H=1 the exact optimum totals are

    T tensor q^m:     (3/2)*(q/(q-1))^m,
    T tensor H54^m:   (3/2)*2^m.                         (C2)

These families have empty common core and are ORIGINAL intersecting s-free families. Therefore any bounded-*total-anchor-weight* claim for their H=1 low-trace incidence matrix is FALSE. Importantly, this does NOT disprove bounded **per-edge** assigned charge: uniform weights yield EXACTLY one unit of weighted incidence at each edge, but cost an exponentially large sum. Any induction summing a uniform per-anchor rank-reduction upper bound must account for this total weight, or prove real correlated cost savings. The theorem is not a blanket impossibility for all exponential-anchor schemes.

## D. Rank and density audit: no circular high-density inference

Earlier multiwitness theorem A implies, for h<=H, 1<=r<=s-2, a compatible opposite-trace packet of size >=phi|F|,

    phi|F| <= h^r sum_{u=1}^h binom(h,u) f_s(k-u-r)
           <= H^(s-2)(2^H-1) f_s(k-2).                 (D1)

Monotonicity f_s(j)<=f_s(j+1) follows by adjoining a fixed point. If this packet premise is asserted only for INTERSECTING |F|>D^k, it yields at most

    i_s(k) <= max(D^k, B f_s(k-2)),
    B=H^(s-2)(2^H-1)/phi.                              (D2)

It is INVALID to silently replace f_s(k-2) by i_s(k-2). Applying f_s(j)<=(s-1)j i_s(j) after EVERY rank drop produces unbounded factors. That matching-support reduction may be paid ONCE at the end of an independently achieved exponential i_s bound.

A separately PROVED original point-link lemma with explicit nonvacuous D and phi applying to ALL s-free families |F|>D^k would give f_s(k)<=C_s^k for C_s>max(D,1/phi) with finite base-rank checks. But the bare existence of unspecified D,phi is equivalent to the target (choose D above a conjectural bound, making it vacuous), as already proved in WORKING_PROOF. Here there is no independent such lemma. Low-trace compatible-packet prevalence is already FALSE at every strict density D<54^(1/4)=2.710806... (s=3), D<39^(1/3)=3.391211... (s=4), D<153^(1/3)=5.348481... (s=6) and D<s-1 (q-products). No exact endpoint or higher-density global refutation is claimed.

Exact boundary checks: f_s(1)=s-1; i_s(1)=1; i_s(2)=max(s-1,3), because intersecting simple graphs are stars or triangles. Published statements (see SOURCE_REGISTER) include f_3(3)=20 and an intersecting 3-free triple upper bound 10; do not replace them with our weaker i_3(3)<=13 or invent an exact i_3(3).

## E. Independent structural route and final statuses

Randomly selecting a central trace U cannot avoid paying inverse probability ~exp(m h(1/q)) in B2. Intersectingness, empty global core, linear mean overlap and known exponential lower constructions do not independently yield a fixed-fraction compatible witness packet. Alternative original certificate needed: a genuinely nonvacuous high-density point-link theorem, or a cross-trace invariant reducing the sum in A5 below its entropy cost, without shifting ancestors.

**PROVED:** A1-A5; exact recurrence envelope and EGF; B1-B6; fractional dual and sharp C2; conditional bookkeeping D1-D2.
**FALSE:** point deletion preserves intersectingness; proper traces always intersect for s>=4; central rank descent alone implies a constant base; bounded *total* fractional anchors for the two tensor examples; moment decay supplies opposite-trace prevalence.
**CONDITIONAL:** explicit nonvacuous original link or stronger central compatibility could imply constant-base induction, but is NOT proved.
**OPEN:** full original-family sunflower conjecture and any independently verified rank-uniform induction.

Independent finite corroboration: scripts/central_trace_amortisation_audit.py and tests/test_central_trace_amortisation_audit.py exhaust 387 three-free subfamilies of the ten triples on five vertices, check original trace closure and its failures, every anchored q-product profile with exact primal-dual weights, all H54 anchored profiles and H153 ordered histogram. Finite tests do not certify the universal mathematical claims.
