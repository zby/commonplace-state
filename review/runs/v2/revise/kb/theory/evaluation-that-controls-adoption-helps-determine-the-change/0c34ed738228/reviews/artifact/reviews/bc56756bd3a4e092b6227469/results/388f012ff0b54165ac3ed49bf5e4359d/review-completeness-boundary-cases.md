---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Both cases involve reading results and forming a verdict. Only the first verdict
    controls the adoption being examined.
  reason: 'The note''s two roles are judgment that controls adoption (required approval)
    and assessment of an already-adopted change. A non-binding pre-adoption review
    falls between them: a maintainer reads the test results before adoption and recommends
    acceptance or rejection, but approval is not required and the agent may adopt
    anyway. Under the note''s criterion (whether approval was required), this judgment
    does not control adoption. But it is also not assessment after adoption, and it
    can still shape which instruction enters use. The Scope bullet about other influence
    covers only a later evaluator. The note''s stated purpose is deciding whose contributions
    explain an improvement, so this common case (advisory code review, non-blocking
    comments) falls outside the claimed coverage.'
  level: warn
- scope: passage
  quotes:
  - The difference is what the judgment controls, not whether a person or a program
    makes it.
  reason: Delegated gating is a strained case. Suppose a maintainer writes the acceptance
    criteria in advance and an automated check applies them to each proposal. The
    program's judgment controls adoption. The maintainer made no judgment about this
    change, yet the maintainer fixed what could pass. The framework can map this case
    if the account names the program's verdict as the controlling judgment and treats
    the criteria as a separate contribution. The note does not say how a judgment
    that sets the gate relates to one that applies it.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
contract: verdict
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note-sha256: 246a2a1d3426a58305107f38e39cd30d2d491f21651f608785af0c536429b317
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
target-sha256: 0c34ed73822892addd39d721e7c2a296545f39f429a56c0f2cbb2fb9621bdb04
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/bc56756bd3a4e092b6227469/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/artifact/reviews/bc56756bd3a4e092b6227469/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews
launch: 388f012ff0b54165ac3ed49bf5e4359d
completed-at: '2026-11-17T07:22:53Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/0c34ed738228/reviews/calls/launches/388f012ff0b54165ac3ed49bf5e4359d/outputs/review-completeness-boundary-cases.md
raw-output-sha256: f54ce65ac655338d147fff076e229f43c8ff133c15c505c132369d126a5f9722
format: 2
---

# Review

## Summary

The note sets out a two-way distinction: judgment that controls whether a change enters use, and assessment of a change that is already adopted. It defines control by whether approval was required for adoption. I tested five boundary cases against that criterion.

- **Simplest case: required approval that is granted.** It maps cleanly to control.
- **Post-adoption assessment that triggers a rollback.** The note explicitly treats this as a causal role in a different transition.
- **One evaluator who approves and later assesses.** The section on one episode containing both roles handles this.
- **Advisory pre-adoption review.** This case falls between the two roles. The judgment comes before adoption and can influence it, but it is not required. The note's binary does not cover it, and its scope caveat covers only later evaluators. This is the warning finding.
- **Criteria authored in advance and applied by a program.** This case can be mapped, but only with difficulty.

The taxonomy is short and fits its argumentative role. Adding a third category may not be the right fix. The note could instead say that judgments which are not required but come before adoption fall outside its claim.
