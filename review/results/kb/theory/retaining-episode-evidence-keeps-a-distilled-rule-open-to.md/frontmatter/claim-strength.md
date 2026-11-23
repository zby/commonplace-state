---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
note: kb/theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md
note-sha256: 30fa18584a5acd182f343f3ea2533b54464d7533ee5dde76e7538165e6795d36
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
outcome: fail
profile:
  harness: codex
  launch-model: gpt-6.2-sol
  effort: medium
model: gpt-6.2-sol
run: kb/reports/state/review/runs/v2/20261120T143951Z
launch: e0b31f397423453ba3247ba5f10e188c
completed-at: '2026-11-20T14:41:15Z'
findings:
- scope: passage
  quotes:
  - Retaining episode evidence keeps a distilled rule open to re-examination
  reason: In the note's bounded sense, keeping a rule open to re-examination means
    preserving the option to consult the evidence behind it. Once the title assumes
    that the retained material is evidence for the rule, that consequence is nearly
    automatic. The sharper claim is that distillation can discard evidence needed
    to correct a rule when one of its assumptions breaks.
  level: fail
contract: verdict
target-sha256: 67f476310a098e4b3923f6ad45fe9efe90df2f77c0f37d339d8935781c81115e
target-capture: kb/reports/state/review/runs/v2/20261120T143951Z/calls/launches/e0b31f397423453ba3247ba5f10e188c/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T143951Z/artifact/reviews/4abfe9f6435dcd075de05621/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T143951Z/calls/launches/e0b31f397423453ba3247ba5f10e188c/outputs/review.md
raw-output-sha256: fe5dc657ac42f120b17260b35c218a162034ea379d47c4651fbb821efa7d10b1
---

# Review

An informed maintainer could favor storing rules alone on the grounds that the omitted observations rarely change a correction or that independent evidence costs less to obtain. The note proposes comparing these choices, but the title leaves their practical disagreement unstated.
