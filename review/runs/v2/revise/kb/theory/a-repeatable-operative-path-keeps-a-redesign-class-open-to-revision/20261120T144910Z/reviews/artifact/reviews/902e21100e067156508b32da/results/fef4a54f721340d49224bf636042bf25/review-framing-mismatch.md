---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Continuity therefore requires more than complete addressability.
  reason: The sentence presents repository-wide addressability as a prerequisite and
    then adds a further requirement. The mechanism only depends on addressability
    of the successor and its authority path, plus continued applicability of the revision
    functions for that class. The example shows that repository-wide addressability
    is insufficient on its own.
  level: warn
- scope: passage
  quotes:
  - Formal semantics make this condition inspectable, at the price of excluding useful
    rewrites whose benefit the incumbent formalization cannot prove.
  reason: The sentence frames the exclusion as a cost of using formal semantics. The
    operative restriction is the admission rule that requires an obtained proof under
    the incumbent formalization. That rule excludes useful rewrites with an unavailable
    proof, including cases where a proof exists but the search fails to find it.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 262a9537a6926e166413d8374fba9fcc51250a45a076d4cfb5e01be4f2a8d865
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: 46c98f5baca1726ff50158d3e2686e47463e9cfad32119a42e037c2fc2c96445
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261120T144910Z/reviews/calls/launches/fef4a54f721340d49224bf636042bf25/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261120T144910Z/reviews/artifact/reviews/902e21100e067156508b32da/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: codex
  launch-model: gpt-6.2-sol
  effort: medium
model: gpt-6.2-sol
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261120T144910Z/reviews
launch: fef4a54f721340d49224bf636042bf25
completed-at: '2026-11-20T14:52:12Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision/20261120T144910Z/reviews/calls/launches/fef4a54f721340d49224bf636042bf25/outputs/review-framing-mismatch.md
raw-output-sha256: 31753219e09e01d426cecf89f88ef1b0e5a2874ff54ff42f134165f645c746bb
format: 2
---

# Review

The causal test is scoped to a named redesign class. Two explanatory sentences give the reader a different account of what makes a revision available.
