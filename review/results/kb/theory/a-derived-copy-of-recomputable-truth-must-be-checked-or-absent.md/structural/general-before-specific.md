---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 675b9e98a7a84713856bda833f41d987
completed-at: '2026-11-16T22:19:21Z'
findings: []
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/bc8c842b42b3fb3193a5e602/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/bc8c842b42b3fb3193a5e602/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/675b9e98a7a84713856bda833f41d987/outputs/review-general-before-specific.md
raw-output-sha256: 197c6a8847113dcdece683c66e1435217a3d974967ea6d26451cf50b2587311f
---

# Review

The section order runs from general to specific. The opening paragraph states the rule. "The asymmetry that forces the rule" justifies it. "Where the rule applies" first describes the general managed-staleness regime and then narrows to the deterministic end. "What enforcement buys" and "What 'checked' requires — and its limits" develop the rule's value and preconditions in general terms. "Consequences" draws general implications. Only then does "Instances across four surfaces" give concrete cases, including proper nouns, ADRs and named files, before Open Questions.

No adjacent pair puts a specific case before the general section it exemplifies. The specific examples in Consequences, such as ADR 025 and the 2026-06-10 skill edits, illustrate a general consequence inside the same item. They are not standalone sections that come before a general one.
