---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: 19df0882d6cddf5bd469e386aa4d02fbf9a4556f9672375b0ca96d7745f16e25
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: 2214be116a950b1be4016de0633a69bd6e3df247b8c6750c25d37d0ef7013038
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/artifact/reviews/32ff04f26bf4d6dc709d618f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews
launch: 003e070dff914169869d6e081eac041e
completed-at: '2026-11-22T21:54:06Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/reviews/calls/launches/003e070dff914169869d6e081eac041e/outputs/review-unearned-generality.md
raw-output-sha256: 265f838cd1147d946d2252af9664bdc61d74c8b6e2085b579be18baed792baa9
format: 2
---

# Review

## Summary

The central claim's abstract terms are "behaviour-changing writes", "storing content", "governing" and "representational forms". Each is earned by argument:

- **Downgrade test.** Replacing "behaviour-changing writes" with "prompt edits" breaks the argument. The note explicitly ranges over three instance classes: weights and adapters, prompts and rules, and code, schemas and tests. It argues that an updater restricted to one class leaves consequential choices outside its reach.
- **Forbids test.** The general wording rules out a weights-only updater counting as a complete continual-learning account when prompts, tools or validators also determine behaviour. A narrower "prompt" or "weights" wording would permit that.
- **Explanatory reach is argued.** The mechanism (authority comes from a consumption path, not from stored bytes) belongs to the operation, not to any one form. The linked definitions apply it to natural-language, symbolic and parametric artifacts alike.
- **Distribution.** Abstraction concentrates at the load-bearing sites: authority, consumption path and form. Concrete examples anchor each.

No finding.
