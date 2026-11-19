---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: 6a9c8733d3906b1ae0ad19bb313466b162dbf7388a77276b26d65c5e003a0d8a
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
findings: []
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/3c5917b353cb5395df87ece5/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/3c5917b353cb5395df87ece5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-unearned-generality.md
raw-output-sha256: e2d9dff88557343cccd6b002585fccf9f35ea25d8385d0d73b6d6db9b1d0f262
---

# Review

The central claim's abstract terms are "derived copy", "recomputable truth" and "artifact".

**Downgrade test.** The concrete term the argument would otherwise use is something like "completeness mark" or "index listing". Substituting it removes cases the argument explicitly works: hardcoded contract lists inlined in hot-path skill text, duplicated build files, and compiled memory cues. The mechanism, a trusted stale copy suppressing a recomputation that a cheap deterministic check could perform, is argued as a property of the copy-to-source relation and of the check's price, not of any artifact format.

**Forbids-test.** The general wording forbids an unchecked hand-maintained frontloaded contract list in instruction text. It also forbids an unenforced prose claim such as "This list is complete". A mark-scoped claim would allow both.

**Explanatory-reach argued.** The note states why the mechanism does not depend on the narrower term: the regime flips wherever derivation is mechanical. It also exhibits several instance classes under the general term (marks, file identity, extractable lists in instructions), each in a different state of application.

**Distribution.** Abstraction is concentrated in the claim and the regime section. The instances and consequences speak concretely.

No finding.
