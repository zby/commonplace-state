---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Holding model weights fixed while updating a store of procedures, hypotheses,
    and code does not remove dependence on the base model's weights.
  reason: The body opens with an abstract negation (dependence is not removed) rather
    than the split the title states. The sentence that names the core claim — three
    semantic competences remain on the frozen base LLM — arrives only at the end of
    the second paragraph, after the three harness bullets and the tool-building aside.
    The title and description carry the claim plainly, so it is findable, but an opening
    sentence stating the split (harness code takes the mechanical loop functions;
    three semantic competences stay on the model) would make it more memorable. The
    harness bullets could then follow as support.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/e1f5dd6781624a3997025981fb7e066c/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/8512350f2932a35406fe287d/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: e1f5dd6781624a3997025981fb7e066c
completed-at: '2026-11-24T13:17:11Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/e1f5dd6781624a3997025981fb7e066c/outputs/review.md
raw-output-sha256: 15e4813904b9d46b5191fce259b104457a16c1ad572a3c436ed325e3e89d2f1b
format: 2
---

# Review

## Summary

Core claim, stated from the note's own commitments: as a working hypothesis, harness code can take over much of an autonomous selection-based learning loop's machinery, but three semantic competences remain on the frozen base LLM — interpreting unformalized text into action, diagnosing novel failures and synthesizing candidates, and judging unformalized trade-offs while recognizing missing evidence.

The title and description state this claim directly, and the numbered list makes the three competences easy to recall. Later material stays subordinate: the criterion-revision paragraph folds store maintenance into competences 2 and 3, the independence paragraph explains why the split matters, the source illustration supports a base-model floor, and Scope and Open Questions bound the hypothesis. None of these competes with the main claim.

The one shape issue is in the opening. The body's first sentence is an abstract negation about weight dependence, then three bullets of harness duties and a sentence about LLMs building harness tools come before the sentence that names the three competences. A reader skimming the body gets the offload half first and the retained-competence half only after the setup. This is an INFO, not a WARN: the claim is in the title and appears within the first two paragraphs. The simplest fix is to open the body with a single sentence stating both halves of the split, then present the harness bullets as the offload half's support.
