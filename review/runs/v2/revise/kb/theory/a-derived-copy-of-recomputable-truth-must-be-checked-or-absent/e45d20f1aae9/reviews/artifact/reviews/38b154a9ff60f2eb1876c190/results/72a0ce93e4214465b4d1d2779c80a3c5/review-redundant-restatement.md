---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A bounded, recoverable downside on one side; a silent, unbounded one on the other
  reason: The closing paragraph of the asymmetry section opens by restating the asymmetry
    that the preceding paragraph has just established. It is a summary of its own
    section rather than a preview of the next, and it goes on to add the conclusion
    (forbidden rather than risky; one missed edit away). Setup followed by summary
    is a weaker signal.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/prose/redundant-restatement.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/prose/redundant-restatement.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 8ac83c3a221e55a6ece3b99917f2f96f145c07d525fd6743b90df87afc272d67
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/38b154a9ff60f2eb1876c190/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/38b154a9ff60f2eb1876c190/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 72a0ce93e4214465b4d1d2779c80a3c5
completed-at: '2026-11-16T22:18:58Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/72a0ce93e4214465b4d1d2779c80a3c5/outputs/review-redundant-restatement.md
raw-output-sha256: ecaa0334f9864555422c826b6565c001364efad04f55e6bf3426ae341c033977
format: 2
---

# Review

Opening paragraphs at section boundaries:

- **The asymmetry that forces the rule** opens with new content (the cost comparison), not a restatement of the introduction.
- **Where the rule applies** opens with the general managed-staleness regime, which is new material.
- **What enforcement buys** opens with the frontloading versus fix-what-the-executor-can't-determine tension, which is new material.
- **What "checked" requires** opens with a one-sentence transition into the enumerated preconditions, which is acceptable.
- **Consequences** opens with "Checked copies degrade gracefully", which reuses the asymmetry's cost of a recomputation but advances it to a lifecycle consequence.
- **Instances across four surfaces** opens with a sentence that names the four application states before the list. It is a one-sentence transition, not a full duplicate of the enumeration.

Closing paragraphs before headings do not preview the following sections. The only near-restatement is the summary line at the end of the asymmetry section, recorded as INFO.
