---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/theory/COLLECTION.md
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
note-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
criterion: kb/theory/COLLECTION.md
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: ed4b6fdf80024520be3c128d5bde5a32
completed-at: '2026-11-23T11:41:10Z'
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  - A reviewer following the original instruction could still recognize it.
  reason: 'The collection treats qualifiers and the subject of the title, description,
    opening claim and main argument as obligations, and asks that someone could say
    exactly how the claim is wrong. The title puts the identifying capacity on the
    rule (''it can identify''), but the description and body put it on the reviewer:
    the instruction ''does not tell the reviewer which earlier failure bears on the
    page'', and the reviewer, not the rule, recognizes the shared-origin case. A reader
    therefore cannot tell what the claim forbids — a fixed rule that does not encode
    applicability conditions, or a reviewer who cannot recognize them. State the claim
    once, with one bearer of the condition, across title, description and opening.'
  level: warn
- scope: document
  quotes: []
  reason: Explanatory-reach asks the note to account for where the pattern works and
    fails and to keep real boundaries explicit in the claim or in `## Scope`/`## Open
    Questions`. The title is an 'only if' condition, but the body works through only
    the case where the condition is met (the reviewer recognizes the shared origin).
    It never shows the failure side — what happens to a fixed rule when the reviewer
    cannot identify which feature of an earlier incident applies, or when the rule
    must change — and it names no gap. Because the collection calls explanatory-reach
    a direction rather than a gate, this is advisory.
  level: info
- scope: document
  quotes: []
  reason: The note has no outbound links. The contract does not require them, so this
    is no violation, but a claim about reusing incident lessons under a fixed review
    rule probably has premise or contrast neighbours in kb/theory/ (for example, continual-learning
    and review-rule notes) that a reader would want. A connect pass could find them.
  level: info
contract: verdict
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/ed4b6fdf80024520be3c128d5bde5a32/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/1551b8a9c131cd0eb18ecc39/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/ed4b6fdf80024520be3c128d5bde5a32/outputs/review.md
raw-output-sha256: bbb6a111be9dc139e605fd4b6c36f1f74ec453397251ce53218b2524e558da55
---

# Review

The note belongs in `kb/theory/`. It makes a transferable, truth-apt claim about review rules and incident learning. It names no Commonplace system choice that would need scoping, and it is not a procedure or a design record. Its read is universal by default, which the contract allows. It cites no sources, so the source-grounding bound does not apply. It does not link into `kb/work/`, and nothing it says is defensive padding.

The main gap is in how the claim is stated. The title says the *rule* must be able to identify when a lesson applies. The description and the body say the rule leaves that identification to the *reviewer*, and they show the reviewer doing it. The collection's explanatory-reach guidance treats the claim surfaces as obligations and asks for a claim whose failure can be stated exactly. Here, which party carries the condition changes what would refute the claim, so the mismatch is a WARN.

Secondary points are advisory. The note shows only the side of its "only if" where the condition holds. It has no boundary or open-question section for the case where the condition fails. It also has no links to neighbouring theory.
