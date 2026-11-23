---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/review-gates/sentence/misleading-link-text.md
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
note-sha256: cdb8512f21f243e70a61d47000e51e2c94317bf77ed9003bee8be4cde99005b8
criterion: kb/instructions/review-gates/sentence/misleading-link-text.md
criterion-sha256: 29771fdb3d02cdf416ad3b68c38b2ae29bb69fe4332f316cc9475de3aa4508c2
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews
launch: 765fee9a50524c84b74692bd14c7d801
completed-at: '2026-11-20T09:44:02Z'
findings:
- scope: passage
  quotes:
  - The [underspecified instructions framing](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md)
    says
  reason: 'The link text promises a note that presents an ''underspecified instructions
    framing'' and, from the sentence around it, prescribes moving components between
    LLM interpretation and code in both directions. The target''s title and opening
    paragraph cover something else: two accounts of prompting, with the semantic reference
    deciding how a failure is diagnosed. The target does not use the term ''underspecified''.
    Its English-execution section (an instruction permits a set of behaviors) is related,
    but a reader who follows the link finds neither the named framing nor the constrain/relax
    prescription. The footer gloss for the same target (''the English account, under
    which an instruction permits several readings'') describes it more accurately.'
  level: warn
- scope: passage
  quotes:
  - 'Abstracted into: [RLM, Tendril, and llm-do place symbolic work at different persistence
    boundaries]'
  reason: The link text uses what looks like an older title. The target is now titled
    'RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence' and treats
    control-language restriction as a second axis alongside persistence boundaries.
    The target still discusses persistence boundaries, so the reader is not misdirected,
    but the link text understates the target.
  level: info
- scope: passage
  quotes:
  - 'extends: extract-function and inline refactoring transfer directly when calling
    conventions are unified'
  reason: The link text is the target's title and matches. The gloss says the refactorings
    'transfer directly'. The target's thesis is that programming practices transfer
    only with evidence matched to the question, and that recurrence alone establishes
    neither adequacy nor equivalence for extraction. The gloss sits uneasily with
    that caution, though it is framed as this note's extension of the target.
  level: info
contract: verdict
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/765fee9a50524c84b74692bd14c7d801/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/artifact/reviews/1a9f7a0c10a30328abe03e38/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/reviews/calls/launches/765fee9a50524c84b74692bd14c7d801/outputs/review-misleading-link-text.md
raw-output-sha256: 27a912b8fbe644e5dd9f69d12070054e6343d8a4cfe788505137decd62f6d50f
---

# Review

## Summary

I checked each link once against its target's title and opening. The following match their targets: the constraining and codification definitions, spec-mining-as-codification, instructions-are-typed-callables (as link text), the programming-practices title, and operational-signals-that-a-component-is-a-relaxing-candidate. The `llm-do` GitHub link is external and was not fetched. Its text names the repository, which is plausible, but the target was not resolved within this review's reading scope.

The main problem is the opening link. Its text names a framing the target does not present, so the reader gets the wrong idea of what the motivating premise rests on.
