---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - re-examine the support where it exceeds it
  reason: 'Two pronouns in a row: the intended reading is ''where the content exceeds
    the source'', but the nearest noun is ''the support'', so ''where the support
    exceeds the source'' is a plausible first parse. Naming the nouns (''where the
    content exceeds the source'') removes the doubt.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/8a302f071403e3e8b876f680/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/8a302f071403e3e8b876f680/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 6a33452f49e5477b8099d126092706ac
completed-at: '2026-11-16T22:21:23Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/6a33452f49e5477b8099d126092706ac/outputs/review-parsing-ambiguity.md
raw-output-sha256: 9a83369a95dfcf3495115a2e8718c49e2b09a0d9f15fece1f48773835033cb46
format: 2
---

# Review

Checked negation scope ("is not forbidden; it is unavoidable", "never correctness"), modifier attachment on the when/where/since clauses, and pronoun reference across the note. The only plausible misparse is the double pronoun in the managed-staleness repair sentence; the surrounding contrast with "recoverable from the source" makes the intended reading recoverable, so it is INFO.
