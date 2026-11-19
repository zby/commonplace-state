---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - already enforced, stated but unenforced, resolved by omission, and not yet applied
  reason: The instances section introduces a four-state classification and says the
    spread across states shows generalization, but the bullets do not use it consistently.
    Only the tag-README mark ('enforced and shipped') and the hot-path contract values
    ('currently resolved by omission') are labelled. The compiled-views bullet is
    never marked 'stated but unenforced', and the duplicated-template bullet never
    says the byte-identity check is 'not yet applied'; it says only that the files
    must be byte-identical. A reader cannot confirm the claimed spread from the bullets,
    so the classification promises more than the section delivers. Either label each
    bullet with its state or drop the four-state framing.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/complexity/framework-decoration.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/complexity/framework-decoration.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 6862f312ec9a6ff6914176d6d8a51f0eaaaebcbac2639a1b9cf1c632ab93dc67
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/634b87b9d90225c17280aafb/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/634b87b9d90225c17280aafb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 3b670c1b79434ce5b130a3f35ab8a0ea
completed-at: '2026-11-16T22:18:30Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/3b670c1b79434ce5b130a3f35ab8a0ea/outputs/review-framework-decoration.md
raw-output-sha256: 8cb667376696a76a73e87c532af42b9679e36c972ec08379400bbed22e5fd239
format: 2
---

# Review

## Summary

Most of the note's structures do real work:

- **Checked/absent dichotomy.** This is the rule itself; each branch has distinct consequences.
- **Level A/B check-cost distinction.** Borrowed from the text testing pyramid, it locates where the regime changes from managed staleness to enforce-or-omit. It supports a decision about which rule applies.
- **Arbitrary / situational / recomputable-and-checked.** The third class resolves a stated conflict between two notes, so the categories enable an inference.
- **Four numbered preconditions.** Each is a decision rule or boundary condition. Precondition 4 is cited again in instance 1, and preconditions 1 and 3 are cited in the footer's contrast with the history note. The list cannot be reduced to one sentence without losing exclusions.

The exception is the four-state labelling of the instances section. It is presented as the evidence of generalization, but two of the four states are never attached to their bullets. The instance list is load-bearing as evidence; the state vocabulary over it is partly decorative as written.
