# S001 — Mathematical obligations and dependency audit

The precise TIK target is: for every fixed k there exists c_k>0 such that every ORIGINAL k-uniform F and m>=2 have H subset F with |H|>=c_k m^(-k)|F| and every realised exact pair intersection, including EMPTY, witnessed by m distinct whole FINAL H petals. Historical source Janzer–Jin–Sudakov–Wu 2026 §6. Main target independent of external ambient witnesses.

| Stage | Actually closed | Reduced but not closed | Outstanding |
|---|---|---|---|
| k<=2 | S033 k=2 c2=1/8 (paper proof, originality unconfirmed) | — | Independent correctness/prior art |
| Restricted all k | S042 LINEAR input, bounded pair-codegree fixed B; S045 additionally ORIGINAL density | conflict linearisation factor Q can grow with m | Sparse nonlinear pair-codegree 2..m-1; no universal original-mass guarantee |
| General k=3 | S033 nonspread/rich proper links and robust-core majority; S036 low-degree high-transversal branch | R3 iff 6m-spread/corefree/high-original-degree HDSE3 (assuming S033) | Constant e/m³ valid selection on general HDSE3; equivalently tripartite five-final-certificate original e/m³ selector |
| k>=4 | S033 lower-rank lift handles nonspread conditional on lower ranks | corefree spread remains for every k | NO induction from R3; overlapping link-union can fail |
| Headline | No new unconditional general sunflower upper bound | Full TIK_k -> f(k,r) <= r^k/c_k | Exponential c_k dependence or DIFFERENT genuine (C_r)^k proof |

### Mandatory quantitative proof
If a family F has no r-sunflower, any internally r-valid H subset F has size <=1: otherwise any realised exact pair-kernel requires r petals in H, contradiction. Hence c_k r^(-k)|F|<=|H|<=1 implies f(k,r)<=r^k/c_k. If c_k>=D^(-k), we get f(k,r)<=(Dr)^k, proving the conjectured form. Arbitrary c_k has no such consequence and may not even improve the published bound (C r log k)^k. To beat the log k base by this implication needs r/c_k^(1/k) < C r log k, e.g. c_k^(-1/k)=o(log k) up to universal constants; to close conjecture needs sup_k c_k^(-1/k)<infinity. No uniform/exponential lower bound on c_k is proved.

### Net obligation movement
Resolved low ranks and optional hypotheses; valid equivalence reductions with remaining hard universal cases; numerous precise **method** obstructions. Zero universal rank-three/every-rank/headline obligations eliminated. 51 sessions do NOT imply a fractional percentage of the full theorem. In S052, repairing J_x on the named rich-link examples is a plausible local lemma but NOT a new universal method unless accompanied by quantitative ORIGINAL-mass selection working across all five certificate types. Publication: zero externally scrutinised originality-cleared paper candidates. See P001A_MATHEMATICAL_ASSET_REVIEW.md and S050's ten-session audit.
