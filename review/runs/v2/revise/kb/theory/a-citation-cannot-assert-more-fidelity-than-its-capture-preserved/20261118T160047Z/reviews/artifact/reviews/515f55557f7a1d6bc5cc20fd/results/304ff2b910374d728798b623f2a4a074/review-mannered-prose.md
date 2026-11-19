---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/prose/mannered-prose.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/prose/mannered-prose.md
note-sha256: 0c8882156a815b8c3c218a4fb796cf97c1112fcbd23137a8a3688c3d3f958eb0
criterion-sha256: b05df7f0063f8adb050393bf45776930c5e3154d9c3e4e6bf31000fe963c4a90
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/515f55557f7a1d6bc5cc20fd/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/515f55557f7a1d6bc5cc20fd/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 304ff2b910374d728798b623f2a4a074
completed-at: '2026-11-18T16:02:23Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/304ff2b910374d728798b623f2a4a074/outputs/review-mannered-prose.md
raw-output-sha256: 0aea9cf41be2125103b6bee22c4cadc2f37bc24614b73ba6f7461ccea79a5e76
format: 2
---

# Review

## Summary

The note is mostly literal. I checked each figurative candidate against the gate's test:

- "rests on the author's word" is a conventional idiom. Its literal meaning is "is supported only by the author's assertion", and it adds no unsupported connotation.
- "a failure, not an invitation to find another copy" uses a mild idiom to set up a contrast. The literal version ("the checker must not search for another copy") is about as clear. The figurative version is concise and introduces no connotation the note does not mean, so this is a matter of preference, not a finding.
- "The binding stops at the capture" builds on the technical sense of binding bytes to a capture, which the previous sentence sets up. It states the limit precisely.
- "Semantic hops compound" names steps in a provenance chain. The same sentence spells out the mapping ("adds a judgment at each hop").
- "ambient cache state" is technical shorthand for whatever cached copies happen to be present.

None of these phrases adds reading effort or connotations the note does not support.
