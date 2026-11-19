---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A model may need several reads to check a source that exceeds its context budget.
  reason: 'This three-sentence paragraph makes one boundary point: an exact excerpt
    can omit the context needed to judge support, so the checker must retrieve that
    context. The opening setup about a context budget and the closing remark that
    the full source can stay outside the model''s context are operational detail.
    The point could be one sentence attached to the preceding paragraph on retained,
    accessible and used material. It is flagged INFO, not WARN, because the paragraph
    is short and links the four-question split to a concrete checking situation.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/detail-overhang.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/detail-overhang.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/bdb46bb578ab8bfc185509b3/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/bdb46bb578ab8bfc185509b3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 3648e2f54e4c43149ad721a3c4a478c6
completed-at: '2026-11-18T16:03:37Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/3648e2f54e4c43149ad721a3c4a478c6/outputs/review.md
raw-output-sha256: 208e2e011fa084f7e9c15fb68323451b2adc62d4104db3f0b65f6e31a82b28e5
format: 2
---

# Review

## Summary

The note is dense, and most of its detail carries a premise or a boundary condition for the main claim: a quote check certifies wording only relative to the evidence it used. No detail clearly needs compressing in place. One paragraph is probably a little long; it is reported as INFO.

## Non-obvious passes

- **The source-identity paragraph** has many sentences: checksum binding, failure on mismatch, the binding stopping at the capture, pins, and context changes going undetected. Each sentence sets a separate limit on what a pass establishes, which is the title claim. Compressing it would remove boundaries rather than restate them.
- **The casebook corpus sentence** under normalization is a single sentence. It explains why a permissive rule is dangerous, so it is a grounding premise, not an illustration that has grown too long.
- **The semantic-hops sentences** in the second-hand provenance paragraph go slightly beyond exact quotes. They contrast exact chains, where each check covers only its own pair, with semantic chains that compound judgment. They end in a practical recommendation and take only two sentences, so their length fits their role.
- **The Scope list** gives one line per exclusion or open question. That length is proportionate.
