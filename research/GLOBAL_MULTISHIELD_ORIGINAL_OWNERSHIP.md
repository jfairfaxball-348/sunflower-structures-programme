# Global original multishield incidence, exact product-cover dual, and cross-anchor ownership (15 October 2026)

**Status:** PROVED elementary, all-rank ORIGINAL-family certificate theorem and exact linear-rank barrier; finite tests passed separately. The full Erdős–Rado Sunflower Conjecture remains **OPEN**. No novelty priority claim. The motivation and AS1/PM1 precede this investigation; the exact GLOBAL (not anchor-local) LP and its tight product calculation are the contribution of this note.

## 1. Precise global bipartite incidence and what is really being charged (PROVED)

Fix s >= 3 and a simple ORIGINAL k-uniform, s-sunflower-free family F. For each actual anchor E in F, a *rectangle* b is an unordered collection of s DISTINCT, NONEMPTY, equal-cardinality traces T_1,...,T_s subset E that themselves form an s-sunflower. Each trace packet is the SET of original edges

  R(E,T) = {A in F \ {E}: A intersect E = T}.

A left vertex is a LABELLED record (E,b,A_1,...,A_s) with A_i in R(E,T_i); label the s trace packets canonically by an ordering of traces. (Other choices of ordering give equivalent records; fix one to avoid artificial s! factors.) Different anchors and rectangles may yield the same unlabelled s-tuple, but are different actual left vertices; do NOT silently count them as one.

Its defect set is D(A_1,...,A_s) = {x outside E: 2 <= sum_i 1[x in A_i] <= s-1}. Because the s trace sets are a sunflower, all x in E have multiplicity either 1 or s. Thus the original A_i are a sunflower if and only if D is empty. Since F is s-free, every left vertex has a nonempty D.

Let B be any chosen set of such (E,b) rectangles, and let n_i(E,b)=|R(E,T_i)| and N(E,b)=product_i n_i. The right vertex x is an ACTUAL ground vertex, not an anchor-dependent copy. Write L_x(E,b)=number of tuples having x in D, given exactly by prior AS1/PM1 using d_i(x)=|{A in R(E,T_i):x in A}|. Consequently

  sum_(E,b) N(E,b) <= sum_x sum_(E,b) L_x(E,b).                 (G1)

There is a canonical global fractional vertex-cover LP:

  V(F,B) = min sum_x w_x  subject to w_x>=0 and
              sum_(x in D(A_1,...,A_s)) w_x >=1
              for EACH actual anchored original selection.          (G2)

Its exact dual assigns y_record>=0, maximizing sum y_record, subject to
sum_(record: x in D(record)) y_record <=1 for every actual vertex x.
Unlike an independent (E,x) copy of a right vertex, G2 explicitly
REUSES a vertex certificate across ALL actual anchors, all trace
sunflowers, and all packet selections. Weak/strong finite LP duality is
standard; no claims of global rank savings follow from G1.

Define actual-edge *incidence*, NOT a valid defect certificate, by

  r_H = sum_(E,b) sum_(i:H in R(E,T_i)) N(E,b)/n_i(E,b).

This counts how often edge H is used in the s selected positions,
with other positions varied. Exactly

  sum_(H in F) r_H = s sum_(E,b) N(E,b).                       (G3)

Per fixed (E,b), an original edge belongs to at most one of its s
packets, but it can recur in MANY b at the same anchor and MANY
different anchors. G3 and G1 concern different resources; replacing
vertex-defect certificates with edges alone would be logically invalid.
In particular G1 is not a fixed-base rank recurrence and G3 provides
no universal bound r_H=O_s(1).

A positive *local* sufficient condition, included with correct scope:
if independent uniform choices from a particular rectangle satisfy
sum_(x outside E) Pr[2<=mult_x<=s-1] < 1 (the exact AS1 expectations),
then a compatible ORIGINAL selection exists; hence no s-free F admits
such a rectangle. This is exact finite averaging, NOT a new result
beyond PM1, and tensor shields may have expectation >=1.

## 2. Exact global multishield fractional-cover theorem on P(s-1,k) (PROVED)

Put q=s-1 >=2 and let P(q,k) be the ORIGINAL k-uniform family of all
transversals of k disjoint q-symbol coordinate blocks. It has q^k
members and is s-free. Its ground vertices are pairs (j,a) with
j in [k], a in [q]. Fix an integer t>=1. Let B_t consist of ALL actual
anchor rectangles whose trace sunflower has equal-size nonempty
private trace parts, EACH of cardinality exactly t; the common
trace core can have arbitrary cardinality. No hypothetical shifted
witness is used.

**Theorem G4.** For all s>=3, t>=1 and k>=0,

  V(P(s-1,k), B_t) =
       0                       if k < s*t,
       (s-1)*k / (s*t)         if k >= s*t.                      (G4)

For B_all = union of all admissible equal-trace-rank rectangles over
all E, B_all is empty when k<s; for k>=s,

  V(P(s-1,k), B_all) = (s-1)*k/s.                                (G5)

Proof. Distinct equal-rank traces T_i form a sunflower with common
core C and disjoint private parts P_i=T_i\C. If they have equal
cardinality, the P_i all have the same cardinality t>=1. Thus the
s*t coordinates in their disjoint union are distinct. On every such
coordinate j, exactly ONE selected original petal uses the anchor
symbol a_j. The OTHER s-1 petals must choose among q-1=s-2 other
symbols. By pigeonhole some outside symbol appears in at least two
of these s-1 petals and at most s-1 petals: an outside partial-
multiplicity defect (j,b). Different active coordinates give different
ground vertices. Every global left vertex in B_t consequently has
at least s*t defects. This proves feasibility of uniform weights
w_(j,a)=1/(s*t), total q*k/(s*t).

The estimate is tight at a real anchored ORIGINAL selection. Choose
any anchor word a in [q]^k and s*t distinct coordinates split into
labelled disjoint t-subsets S_1,...,S_s. For each i choose original
petal A_i that agrees with a on all coordinates OUTSIDE the s*t
active coordinates and on S_i, and changes a_j to a fixed other
symbol b_j != a_j in ALL OTHER active coordinates. Then traces
T_i consist of the common k-s*t inactive anchor points together
with S_i; all have equal size k-s*t+t and their private parts have
size t. There are exactly s*t defect vertices (j,b_j): at each
active coordinate b_j occurs in s-1 petals and a_j in one; inactive
coordinates have the common anchor point in all s petals.
The A_i are s distinct ORIGINAL edges and none equals the anchor.

To certify OPTIMALITY rather than just give an upper bound, use the
finite automorphism group that permutes coordinates and alphabet
symbols independently at each coordinate. It acts transitively on all
q*k ground vertices, and preserves the entire anchored-rectangle
incidence instance with fixed t. Average the orbit of one tight
anchored selection. Every defect vertex then appears in exactly the
same fraction s*t/(q*k) of these records (counting an orbit as a
multiset is legitimate). Giving every record in that orbit total
fractional dual mass (q*k)/(s*t) yields load exactly 1 at each
vertex, and achieves dual objective q*k/(s*t). Finite LP duality or
weak duality matching the primal proves G4. For k<s*t,
equal-rank s-sunflower traces would need s disjoint nonempty
t-private parts and are impossible, so the instance has no
constraints and optimum zero. In B_all, every rectangle has t>=1,
so w=1/s is feasible, and t=1 exists exactly when k>=s.
Use the same tight orbit to get the matching lower bound, G5. QED.

**Essential nuance:** If one permits UNEQUAL trace ranks, the minimum
number of active coordinates becomes s-1 rather than s; the
corresponding all-ranks global product-cover optimum changes to k
for k>=s-1. G4/G5 explicitly concern the EQUAL-rank trace rectangles
of AS1. Do not substitute the unequal-rank variant without changing
the allowed left-vertex class.

A point of P(q,k) belongs to exactly q^(k-1) edges, a GLOBAL fraction
1/q. Thus a strong point link and a linearly growing global defect LP
coexist. An LP upper bound O_s(1) cannot be a necessary invariant of
high-density s-free families near their known lower product base.
The LP is a diagnostic, not an implication ruling out independent
high-density link/rank-descent arguments.

## 3. Exact cross-anchor original edge reuse (PROVED)

Write b=floor(k/s) and partition the first b*s coordinates into b
disjoint ordered blocks of length s. For EVERY one of q^k original
anchors a and EVERY block, choose the tight t=1 s-tuple above,
with the alternative symbol b_j=a_j+1 modulo q. All other coordinates
are unchanged. Thus there are exactly q^k*b ACTUAL (anchor,block)
left records, each with s original petal edges and exactly s defect
vertices in its active block.

For any fixed original edge H and fixed block, there are EXACTLY s
incidences of H among these records: for each petal position i the
map from anchor word a to the corresponding petal word is a bijection
of [q]^k (coordinatewise alphabet shift or identity). Therefore

  r_H = s*floor(k/s)    for EVERY ORIGINAL H in P(q,k).        (G6)

At each used coordinate j and each symbol x=(j,a), the defect
vertex x appears in exactly q^(k-1) selected (anchor,block) records;
unused coordinates never appear. These numbers independently
satisfy G3: q^k*s*b total petal incidences and q^k*s*b defect
incidences, respectively. This is a controlled, explicit
cross-anchor recurrence of OWNED ORIGINAL EDGES even when there
is a single tuple per anchor/block. Edge ownership at a fixed
anchor does not imply cross-anchor constant reuse. It does not
claim exponential reuse for THIS sparse selected class.

## 4. Rank recurrence and density-sensitive route: where proof stops (OPEN)

G4 gives an exact linear-rank certificate-cover obstruction, not
f_s(k)<=C_s^k. P(q,k) has |P|=q^k, so it is a lower construction:
the linear LP cost is compatible with the desired conjecture.
Attempting to charge one unit of rank gain per anchored box to
a globally bounded vertex-cover budget is FALSE in this test case.
Conversely no theorem says that a large GLOBAL link of fraction
phi_s follows from a small or large V(F,B). On the product the
point fraction is 1/q, but a fixed-base link descent is available
for elementary coordinate reasons not encoded in G4.

An unrestricted noncircular recurrence would need a mechanism that
either (a) extracts a point/link or owned lower-rank FAMILY covering
a provable fixed fraction of all original F, or (b) proves a
nonseparable density-sensitive entropy/correlation decrement that
pays for the rank reduction. At present neither is proved.
A family-specific bound on r_H alone cannot produce a density bound
without a theorem linking it to a controlled number of selected
rectangles per unit of |F| and rank. The exact product counterexample
does not address hypothetical regularisation above a genuinely
proved high-density threshold D_s^k with D_s greater than product
bases, nor does it refute any general C_s^k bound.

## 5. Hostile finite audit and source controls

The standalone scripts/global_shield_audit.py and
tests/test_global_shield_audit.py use only Python stdlib:
- Exhaust ALL original anchor/equal-rank trace sunflower selections
  for P(2,k), k=2,3,4; k=2 has NO rectangle, k=3 has 8
  distinct defect sets of min size 3, k=4 has 32 sets min size 3.
- Check explicit tight original tuples at s=3,4,5 and t=1,2;
  construction and rank assertions are checked rather than inferred
  from count alone.
- Count actual original edge position reuse G6 at s=3 k=3,5;
  s=4 k=4,8; s=5 k=5; also independent defect-vertex occurrence
  counts at every active coordinate.

All FIVE standalone unit tests passed in the execution environment.
The unbounded-rank assertions are SYMBOLIC proofs, not inference
from the finite tests. The whole repository validator and complete
unit suite require hosted checks at the exact PR head; do not
misrepresent this local standalone run as the complete suite.

Classical P(s-1,k) fixes the necessary lower floor (s-1)^k.
Q9, triangle tensors, Abbott--Hanson 54 (s=3,k=4, 2/9
point fraction), Axante 39 (s=4,k=3, 3/13), and NONREGULAR
Axante 153 (s=6,k=3, 3/17) are retained as separate
previously audited ORIGINAL-family lower-bound controls;
this session did NOT re-enumerate their full incidence tables.
The v1 original-source full-shift transfer remains invalid and
its proposed O_s(2^k) universal conclusion is false for s>=4.
Mishra v2 establishes a SHIFTED-family bound only. The published
Bell--Chueluecha--Warnke O(s log k) base and Rao's 2026 survey
do not establish an s-only base. Ge--Wang--Xu--Zhao
(arXiv:2609.18995) and Shangguan (arXiv:2609.30263)
are bounded-VC results; P(2,k) has VC dimension k and does
not fall under a fixed-d extraction theorem.

**Classification:** G1/G3 exact incidence = PROVED accounting (not a
new asymptotic upper bound); G4/G5 exact global LP and explicit
dual = PROVED; G6 exact original edge reuse = PROVED; globally
bounded multishield vertex-cover strategy = FALSE in this model;
original high-density global rank descent = OPEN. Literature
novelty and priority have NOT been established.
