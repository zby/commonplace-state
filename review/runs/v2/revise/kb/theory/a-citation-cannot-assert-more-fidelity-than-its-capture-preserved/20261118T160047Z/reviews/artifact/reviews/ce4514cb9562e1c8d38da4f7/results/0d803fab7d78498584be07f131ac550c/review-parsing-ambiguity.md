---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - does the span occur in that text, once or once inside a stated range?
  reason: '"Once or once inside a stated range" can read on first pass as a duplicated
    word, or with "once" meaning "at least once" rather than "exactly once". The intended
    reading (exactly one occurrence in the text, or exactly one complete occurrence
    inside the stated range) is only fixed by the later sentence "Requiring exactly
    one occurrence, or exactly one complete occurrence inside a checked range". Writing
    "exactly once" here would close the gap.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/ce4514cb9562e1c8d38da4f7/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/ce4514cb9562e1c8d38da4f7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 0d803fab7d78498584be07f131ac550c
completed-at: '2026-11-18T16:03:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/0d803fab7d78498584be07f131ac550c/outputs/review-parsing-ambiguity.md
raw-output-sha256: be6ea959a285051888a7cd265b57938c7f077831713b4bb884ce1e2318a4436a
format: 2
---

# Review

Negation scope, modifier attachment and pronoun reference are clear throughout. "It" in the support-judging sentence and in "since it ran" resolves to the nearest plausible antecedent; "do not" in the arbitrary-path clause clearly negates "bind"; "neither is text that happens to sit in a model's context" attaches to "is not evidence".

The one weak spot is the compressed "once or once inside a stated range" in the opening paragraph, where "once" could be read as "at all". Later text disambiguates it, so it is recorded as INFO.
