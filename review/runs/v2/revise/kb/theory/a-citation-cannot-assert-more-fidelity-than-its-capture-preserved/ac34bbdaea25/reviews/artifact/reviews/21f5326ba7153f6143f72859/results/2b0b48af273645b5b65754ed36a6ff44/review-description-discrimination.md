---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
note-sha256: 49154998ac085aabbdec63bbf03a1a656de38cc6532af9de3ee22a4eabb1a351
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/21f5326ba7153f6143f72859/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/21f5326ba7153f6143f72859/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 2b0b48af273645b5b65754ed36a6ff44
completed-at: '2026-11-16T22:08:51Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/2b0b48af273645b5b65754ed36a6ff44/outputs/review-description-discrimination.md
raw-output-sha256: b26441ed03c11db0acc1273a120c2d75f447e538f0a8d324527345dfd9ab0e7f
format: 2
---

# Review

The description adds retrieval value well beyond the title:

- **Mechanism:** forced constraints make capture layered into verbatim, paraphrase and second-hand layers, and a citation's fidelity is bounded by the layer that holds the passage.
- **Implication:** no notation can raise fidelity; only re-capture can.

An agent comparing a short result list of provenance, citation or grounding notes could use the layer vocabulary and the "only re-capture" consequence to choose this note. A title-only reading would not give it those cues. The description does not just paraphrase the title.
