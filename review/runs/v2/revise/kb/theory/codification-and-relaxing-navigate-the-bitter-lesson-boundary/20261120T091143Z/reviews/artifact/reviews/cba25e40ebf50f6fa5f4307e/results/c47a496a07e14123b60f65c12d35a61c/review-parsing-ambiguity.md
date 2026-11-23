---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - separates exact specs (the spec is the problem) from proxy theories
  reason: '''The spec is the problem'' is an idiom for ''the spec is what is wrong''.
    On first reading, the parenthetical can say exact specs are faulty, the opposite
    of the intended ''the spec constitutes the problem to be solved''. The contrasting
    parenthetical that follows and the later capitalized ''the spec IS the problem''
    resolve it. ''The spec defines the problem'' avoids the garden path.'
  level: info
- scope: passage
  quotes:
  - That scale in fact selects on this property is conjectural, not established.
  reason: A sentence-initial 'That scale' first parses as a demonstrative noun phrase
    ('that particular scale') before the reader reaches 'is conjectural'. 'Whether
    scale in fact selects on this property is conjectural' or 'It is conjectural that
    ...' removes the brief misparse.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: f031241f1641e2a22da292c23a64bc0119dd7225a49b5bb887537892b157f1a3
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: 7051fe6740599d8f9eeee0f94c1475344031dd52d15719567621016b0449100b
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c47a496a07e14123b60f65c12d35a61c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/artifact/reviews/cba25e40ebf50f6fa5f4307e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews
launch: c47a496a07e14123b60f65c12d35a61c
completed-at: '2026-11-20T09:15:25Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/reviews/calls/launches/c47a496a07e14123b60f65c12d35a61c/outputs/review-parsing-ambiguity.md
raw-output-sha256: 97ae36500eb494fd564e36510477b54cce788181247b860f069248e14263c14e
format: 2
---

# Review

I checked negation scope, modifier attachment and pronoun reference sentence by sentence. Negations such as "not a partition into codified versus learned" and "what relaxing reverses is the extraction, not symbolic membership" scope correctly. The when-clauses in the relaxing definition and the regime bullets attach to the intended verbs. The "it" in "relaxing is what happens to it later" most naturally refers to the codification. Two idiomatic or garden-path readings are noted as INFO; context resolves both quickly, and neither leaves a durable wrong reading.
