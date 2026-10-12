# P001-S034 parent status-only validation (premerge)

The parent's GitHub-hosted programme-integrity workflow runs `python3 scripts/validate.py` and `python3 -m unittest discover -s tests -v`. No separate local clone validator PASS is represented by this premerge record. Check the actual FINAL HEAD parent PR workflow and job before merging; after the two-parent nonforce merge check the actual merged-main PUSH workflow and job. Missing runs/jobs are NOT PASS. No parent mathematical S001, no child S035.

## First PR-head failure and correction
First hosted parent PR #38 head `850a5eb06364d50e893226bd34bea7bb83f864b0`, run `38256511710` / job `114835873053`, FAILED in the unit tests (validator itself SUCCESS). The stale S033 regression test asserted that the newest receipt *must* be S033 and S034 must be FUTURE. This correction updates the test to the S034 receipt, retains the entire historical S026-S033 non-promotion regression suite and checks S034's actual/new S035-future flags. The failed head is NOT a PASS; only a new final-head green run can permit merging.
