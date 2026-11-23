---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/title-as-claim-makes-overlap-between-notes-visible.md
  against kb/instructions/review-gates/frontmatter/claim-strength.md
contract: verdict
note: kb/theory/title-as-claim-makes-overlap-between-notes-visible.md
criterion: kb/instructions/review-gates/frontmatter/claim-strength.md
note-sha256: 789e324636b99d73eef87112559e0c5e46701a4ae3345883e34f4fc86b0f21bf
criterion-sha256: 93322659c6e738fddffdba181825aadfe4337fd380d31b1fa357f8b747286b7b
target-sha256: ec8775f47b7e1dfaa67f6e5f7dc8796d0df275830360443e5f673ef82e9fb9a0
target-capture: kb/reports/state/review/runs/v2/20261120T133828Z/calls/launches/41db364486bd4b0facc362f120366992/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T133828Z/artifact/reviews/8c33c86c5e06367ce3276b12/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: codex
  launch-model: gpt-6.2-sol
  effort: medium
model: gpt-6.2-sol
run: kb/reports/state/review/runs/v2/20261120T133828Z
launch: 41db364486bd4b0facc362f120366992
completed-at: '2026-11-20T13:39:29Z'
raw-output: kb/reports/state/review/runs/v2/20261120T133828Z/calls/launches/41db364486bd4b0facc362f120366992/outputs/review.md
raw-output-sha256: e5d4bf40fed2a254c4c765aea525bef23853da4827be0dec6248bbcec4cd67a2
format: 2
---

# Review

The title makes a contestable claim about what a maintainer can infer from an index. Its main predicate asserts that claim titles reveal overlap between notes during a scan. Two titles can state different claims even when the notes share an argument, so a maintainer could reasonably expect to need the bodies to detect that overlap. The note's paired titles illustrate the inference the title says a maintainer can make.
