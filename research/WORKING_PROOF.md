# Working proof notebook — no proof of the full conjecture yet

Status 2026-10-14: **OPEN, proof not obtained.** Single central goal is f(k,s)<=C_s^k for every fixed s>=3 and all k. Work from original-family witnesses, exact sources and adversarial examples.

## Checked elementary controls
1. Coordinate products `P(s-1,k)` are s-sunflower-free and have (s-1)^k members, forcing `C_s>=s-1`.
2. The three-edge graph family `{{2,3},{1,4},{1,5}}` is 3-sunflower-free, but its (1,2)-compression contains a 3-star. Sunflower-free status is not shift-invariant.
3. Complete shifting of the singleton rank-two family `{{3,4}}` on [4] yields `{{1,2}}`; v1's assertion that every shifted set is an original set with merely one source vertex replaced by 1 is false in this elementary instance. It cannot justify an original-source partition across multiple shifts.
4. V1's proposed all-s inequality `(3s^2)^(6s^2-2)2^k` fails for s>=4 for sufficiently large k, by (1).

## Source claims awaiting independent proof audit
- V2 shifted-only theorem with recurrence f'(k,s)<=2f'(k-1,s) for k>=s. Check exact threshold and proof for k=s case, shadow counting and sunflower cardinality consistency.
- V2 one-step shift tau(C_ij(F))<=2tau(F). Composition loses control depending on n; do not extrapolate.
- V1 full-shift tau(SF)<=3tau(F)^2 is **not a validated theorem**; the argument's unique-source mapping breaks down, and, conditional on v2, the entire uniform transfer form is impossible for q>=3.
- Any proposed alternative must be stress-tested against products P(q,k) and the tiny shift counterexample above.

## Pending fundamental obligation
Produce a bridge to **arbitrary**, not necessarily shifted, sunflower-free k-uniform families with a base independent of both k and n. Prove a valid transfer theorem or new direct sunflower theorem with a quantitative rank induction; show the final C_s and all hypotheses. Nothing in the historical child-project material constitutes such a proof. Work until no productive attacks remain in each invoked investigation; carry unresolved proof obligations forward honestly without creating artificial milestones.

See [next direct investigation](../sessions/NEXT_SESSION.md).
