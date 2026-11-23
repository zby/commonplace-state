---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: The Writing Shape instruction 'Link to adjacent notes where the relationship
    helps traversal' goes unmet. The note has no inline links and no Relevant Notes
    footer, although the template includes one. Its subject is incident-driven review,
    transfer of lessons and fixed versus changing review rules, and it carries the
    continual-learning tag, so adjacent KB notes clearly exist. A reader who reaches
    this note cannot traverse to the notes it qualifies or extends.
  level: warn
- scope: document
  quotes: []
  reason: 'No `## Scope` section is present. The type permits omission only when no
    limit is known. The note''s own example implies a limit it leaves unstated: the
    argument depends on a reviewer who can abstract the relevant feature (shared origin
    under an independence assumption) from an incident with different surface details.
    A known failure case is a reviewer who retrieves incidents only by surface match.
    This is borderline because the body partly addresses it inline (''A lookup by
    source name would miss that connection''), so it is recorded as info rather than
    as an unmet instruction.'
  level: info
outcome: warn
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/types/note.md
contract: verdict
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/types/note.md
note-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/9700cd01fa04439a8165fe7de390428c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/75b869bb58f5e90aa558e248/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 9700cd01fa04439a8165fe7de390428c
completed-at: '2026-11-23T11:40:34Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/9700cd01fa04439a8165fe7de390428c/outputs/review.md
raw-output-sha256: bc8c00574ac26e7393b71c27fa66f890c6ddf08c834b3a900b261358910abbf9
format: 2
---

# Review

The note mostly follows the `note` type's authoring instructions. The title works as a compressed handle and states a proposition. The main claim appears in the first paragraph: a standing rule says where to look, not which earlier failure bears on the case. The body is explanatory rationale, not imperative procedure, so it respects the split between notes and instructions. The wiki-citation example makes the mechanism concrete, and the final paragraph states the test the claim implies.

The unmet instruction concerns traversal. The template ends with a Relevant Notes footer, and the Writing Shape section asks for links to adjacent notes where the relationship helps traversal. This note has no outbound links at all. Its topic sits among other KB material on review rules, incident lessons and continual learning, so the relationship is not hypothetical. With no links, the note is isolated from the material it refines.

Scope is a lesser concern. The note leaves its dependence on the reviewer's ability to abstract features implicit. The instruction allows the Scope section to be omitted, and the body gestures at the failure case, so this does not raise the outcome.
