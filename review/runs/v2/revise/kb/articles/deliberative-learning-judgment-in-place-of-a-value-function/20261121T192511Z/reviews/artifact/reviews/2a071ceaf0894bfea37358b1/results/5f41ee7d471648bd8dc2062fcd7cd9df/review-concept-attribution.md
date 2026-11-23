---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Worse, legibility does not guarantee faithfulness:'
  reason: 'The article uses ''faithfulness'' for whether a written rule is what actually
    drove the model''s behavior. The linked note defines faithfulness for a rationale:
    whether it accurately tracks the basis a theory rests on, as an aid to locating
    a failed premise during repair. The target does cite the artifact-grounding result
    in passing, so its treatment partly supports the identification, but its core
    concept is narrower and differently placed.'
  level: info
- scope: passage
  quotes:
  - inspectability as a property of form
  reason: The article attributes inspectability to representational form. The linked
    note grounds it in the inspection route of a readable artifact at affordable cost
    and states that symbolic form alone does not supply it. The weights-versus-readable-rules
    contrast is shared, so the attribution is partly supported; a reader may still
    take away a stronger form-based claim than the target makes.
  level: info
outcome: pass
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/5f41ee7d471648bd8dc2062fcd7cd9df/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/2a071ceaf0894bfea37358b1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: 5f41ee7d471648bd8dc2062fcd7cd9df
completed-at: '2026-11-21T19:29:47Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/5f41ee7d471648bd8dc2062fcd7cd9df/outputs/review-concept-attribution.md
raw-output-sha256: 7f7fd72abe8681799ec7155a5a0e31636ebebf0f361553d98c9ecba78f5ff497
format: 2
---

# Review

## Summary

I checked every sentence that identifies an article concept with one in a linked note. These were deployment-time adaptation, the deployed system as the unit of learning, deliberative learning and its two conditions, the Gödel machine as the proof-governed extreme, PRODIGY's targeted correction and single-loop status, EURISKO's criterion revision, the definition of an on-balance improvement as one that every reasonable measure favors, reversibility, proxy revision under a fixed objective, the production-method reading of the Bitter Lesson, the bootstrap condition, compounding, false-positive acceptance, and operative change. Each target's core treatment supports the identification.

Two attributions read the target slightly more broadly than it states: faithfulness, and inspectability as a property of form. In both cases the target's treatment partly supports the article's use, so they are recorded as info. External URLs (Sutton's essay and the interview) were not fetched; the KB note on the Bitter Lesson describes both consistently with the article's use.
