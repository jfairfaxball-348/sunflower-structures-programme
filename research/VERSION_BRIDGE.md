# The actual Mishra v1 -> v2 mathematical gap (14 October 2026)

## Conjecture and permitted quantitative shape
Define `f(k,s)` as the greatest cardinality of a finite **simple** k-uniform family containing no s distinct sets whose pairwise intersections are all the same. Conventions in the two source versions vary by +/-1 threshold. The goal is
`for every fixed s>=3 exists C_s<infinity for every k>=1: f(k,s)<=C_s^k`.
MUST allow `C_s>=s-1`; a bound with universal base 2 for s>=4 is impossible.

## What v2 claims (shifted-only)
Frankl (i,j)-compression replaces a set A containing j but not i with `(A-{j})+{i}` if its replacement is absent from the current family. Full shifts preserve rank and family cardinality but can change sunflower number. Mishra v2 Section 3 Lemma 4 gives a **single-compression** bound `tau(C_ij(F))<=2 tau(F)`. Iterating naively across O(n^2) compressions incurs ground-set-dependent exponential loss and does NOT solve the conjecture. V2 Sections 4 and 6 claim a half-mass first-vertex link of a shifted family when tau<=k, yielding shifted recurrence `f'(k,s)<=2 f'(k-1,s)` for k>=s and its source bound `f'(k,s)<=s^(2s-2)2^k`. Check argument assumptions, sunflower sizes and induction thresholds before using these as lemmas.

## What v1 additionally claimed
V1 Section 3 Lemma 3 claimed a strong FULL-shift estimate:
`tau(S(F)) <= 3 * tau(F)^2`, independent of k and ground-set size n.
V1 Section 7 used this and the shifted bound to claim
`f(k,s) <= (3s^2)^(6s^2-2) * 2^k` for ALL families.
A rigorous gap assessment must separate theorem statement, proof gaps and **counterexamples**; preserving the precise v1 formula is not our goal.

## Mathematical obstruction 1: v1 final inequality is false
For s>=4, q=s-1>=3, let
`P(q,k) = { {(i,a_i): i=1..k} : a_i in [q] }`.
It has exactly q^k members, all distinct and k-uniform. In any s=q+1 proposed sunflower, each coordinate's s symbols must either all agree or be pairwise distinct; pairwise distinct is impossible with q symbols, so all coordinates agree and the s sets would coincide. Thus **P(q,k) contains no s-sunflower**.
In particular s=4 gives 3^k > (3*16)^(6*16-2)*2^k for sufficiently large k (e.g. k=1000). This contradicts v1's alleged universal theorem, irrespective of whether the revised shifted result is correct. A valid full-conjecture proof must permit a base at least s-1, not `constant_s*2^k`.

## Mathematical obstruction 2: one shift creates a new sunflower
Let `F={{2,3},{1,4},{1,5}}`. Pairwise intersections of its three sets are {}, {}, {1}; so F has NO 3-sunflower. The `(1,2)` shift yields `{{1,3},{1,4},{1,5}}`, a three-petal sunflower with core {1}. Therefore **shifting does not preserve sunflower-freeness**. Keeping |F| fixed does not imply that a shifted sunflower can be lifted.

## Mathematical obstruction 3: v1 Step A/B 'unique source' argument
V1 §3 Case 2 says that for each set S containing vertex 1 in the fully shifted family, there is a unique **original** F and one source x with `S=(F\{x}) union {1}`. This cannot describe arbitrary compositions: for the singleton family `{{3,4}}` (rank 2), full shifting on [4] yields `{{1,2}}`. The sole original set {3,4} and final {1,2} differ by TWO removals and TWO insertions; no single x satisfies the displayed formula. Thus the claimed partition by one-step original sources is not well-founded without additional structure. This is an exact flaw in the cited proof step; it is NOT by itself a counterexample to every conceivable transfer bound.

## Important further no-go
If v2's shifted bound is valid, any k- and n-independent upper bound `tau(S(F)) <= g(tau(F))` for ALL finite families would be impossible for s>=4. Apply to P(q,k), q>=3, whose tau is exactly q (q-sunflower from varying a single coordinate, no q+1 sunflower). If `tau(S(P(q,k)))<=g(q)` independently of k, then v2's shifted bound implies
`q^k <= (g(q)+1)^(2(g(q)+1)-2)*2^k`
for all k, impossible since q>2. Therefore **the original v1 quadratic full-shift mechanism is untenable conditional on the checked v2 restricted theorem**. The next route MUST exploit more information than tau alone, use partial/adaptive shifting with controllable losses, preserve original witnesses by structure, or develop an altogether different extraction theorem. Do not merely propose another uniform full-shift bound g_s.

## Direct new research targets
(A) audit the v2 restricted proof and v1 failed premise independently; (B) classify explicit source/lifting collisions under complete and partial shifts, testing product, hubs, link-dense and graph families; (C) find a noncircular quantitatively strong transfer from sufficiently large arbitrary sunflower-free F to structured/shifted-compatible original-F subfamily, OR build a new induction reducing rank with a loss `<=C_s` per step; (D) if these fail, seek other genuinely new sunflower arguments. For EVERY proposed route show exact algebra yielding `C_s^k`; no `n` or growing `log k` hidden in C_s.

**Verdict:** Full conjecture NOT solved. Research target remains live. Mathematical obstructions are progress in understanding which v1-to-v2 bridges cannot work.
