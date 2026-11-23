---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A fixed review rule can use lessons from new incidents only if it can identify
    when they apply
  - A reviewer following the original instruction could still recognize it.
  reason: The title assigns the identifying capacity to the rule, but the body locates
    it in the reviewer. The rule cannot identify anything; the reviewer's recognition
    does the work. Read literally, the title's condition is never met by 'Check past
    incidents before publication', so the claim either collapses into the codification
    position (the rule must encode the applicability condition) or should be restated
    as a claim about the reviewer plus a fixed rule. State which bearer carries the
    applicability judgment and make the title agree with it.
- scope: passage
  quotes:
  - The incident shows what the review must distinguish, not that the review rule
    must change.
  reason: This conclusion is asserted against the codification alternative without
    engaging it. An informed opponent (checklist practice after incidents; the KB's
    own codification move) holds that recognition by an unaided reviewer is unreliable
    as incidents accumulate and that the lesson should be promoted into an explicit
    check such as 'when a claim relies on independent sources, verify they do not
    share an origin'. The note needs a condition stating when leaving the rule fixed
    is adequate and when the applicability test should instead be written into the
    rule, or it should narrow the conclusion to the single-reviewer, few-incident
    case its example shows.
- scope: passage
  quotes:
  - The lesson still applies if the new sources also share an origin and the claim
    relies on their independence.
  reason: 'The example works only because the incident has already been abstracted
    into a feature-level lesson (shared origin plus reliance on independence). That
    abstraction is a change somewhere: in the incident record, the reviewer''s training,
    or the rule. The note does not say where it lives or who produces it, so the claim
    that only recognition is needed hides the step that makes recognition possible.
    Name where the abstracted applicability condition is stored and how it is produced
    from a raw incident.'
- scope: document
  quotes: []
  reason: The description frames the fixed rule as a deficit ('leaves the reviewer
    to determine which feature ... matters'), while the body concludes the rule need
    not change. Align the description with the body's actual conclusion so a reader
    retrieving the note knows whether it argues for or against keeping the rule fixed.
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/critique-note.md
note-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/cb97078ad4394a5c92c6b6cd290c77ed/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/613e2b750d10eb391002be35/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: cb97078ad4394a5c92c6b6cd290c77ed
completed-at: '2026-11-23T11:42:56Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/cb97078ad4394a5c92c6b6cd290c77ed/outputs/review.md
raw-output-sha256: bc99a1db8584830381c9e87b04b959e46dd0a405a352885d356c50ec62064b9d
format: 2
---

# Critique: fixed review rules and when incident lessons apply

**Note:** kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
**Central commitment:** A fixed instruction such as "check past incidents before publication" can keep absorbing lessons from new incidents without being rewritten, provided the review can identify the feature that makes an earlier failure bear on the page at hand.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opposing stance is the codification position, as in post-incident checklist practice in aviation and medicine and as in this KB's own move of turning observed failures into explicit checks. Its argument has three steps.

First, the note's condition has the wrong bearer. The title says the *rule* must "identify when they apply", but "Check past incidents before publication" identifies nothing. The note concedes this: the instruction "does not tell the reviewer which earlier failure bears on the page at hand." All of the identifying work is done by the reviewer. So if the rule stays fixed, the title's condition is unmet. If the condition is met, it is met by something other than the rule.

Second, the example hides a change. The double-citation lesson transfers only after someone has stated it as "the sources share an origin and the claim relies on their independence." That feature-level formulation is not in the raw incident ("these two citations copied one report"). Someone has to produce and store it. Wherever it lives (an incident log entry, reviewer training, an appended check), something other than the bare rule changed. The rule stays fixed only because the change has moved elsewhere.

Third, recognition by an unaided reviewer does not scale. As incidents accumulate, a reviewer told only "check past incidents" must hold every abstracted lesson and match it against every page. That is the recall-and-match load checklists exist to remove. The codification position says the reliable remedy is to write the applicability test into the rule: "when a claim depends on independent sources, verify they do not share an origin." On that view the note's final sentence, "not that the review rule must change", is wrong as a general claim. It holds only where the incident load is small and the reviewer is strong.

## How the note engages it

**Partially engaged.** The note grants the first step's premise: the instruction "tells the reviewer where to look" but not which failure applies. It also anticipates surface lookup failing ("A lookup by source name would miss that connection"). Its proposed test, whether the reviewer "distinguishes apparent corroboration from independent support", correctly puts the success criterion on recognition rather than retrieval.

The note does not engage the remaining steps. It does not say where the abstracted applicability condition lives or who produces it. It does not consider the alternative of writing that condition into the rule. It also gives no condition for when unaided recognition is adequate. Its conclusion that the rule need not change is asserted, not argued against codification. The title compounds this by assigning the identifying capacity to the rule, which the body then shows the rule lacks.

The attack does not fully land. The note's narrower point survives: retrieving an incident is not the same as applying its lesson, and an incident's value lies in the distinction it teaches, not its surface particulars. A fixed pointer rule plus a capable reviewer can work in the single example given.

## Constructive findings

- Make the title and body name the same bearer. Either the claim is about the reviewer ("a reviewer under a fixed rule can use new incidents only if it recognizes the feature that makes them apply"), or it is about the rule, in which case the rule must carry the applicability condition.
- State where the feature-level formulation of an incident is stored and how a raw incident becomes one. That is the step that makes recognition possible, and it is currently implicit in the example.
- Engage codification directly: give the condition under which leaving the rule fixed is adequate (few incidents, a reviewer able to abstract) and the condition under which the applicability test should be written into the rule (many incidents, weaker or varied reviewers, a high cost of a miss).
- Align the description with the body's conclusion. The description presents the fixed rule as a burden on the reviewer; the body presents it as sufficient.

## Secondary objections (optional)

- The note's claim risks tautology: "a lesson can be used only if one can tell when it applies" is true of any lesson under any rule. Its non-trivial content is the further claim that the rule need not change. That claim is the one the note argues least.
- One example supports a general "can remain the review rule" claim. A second case would show whether the result depends on the incident being as cleanly abstractable as citation independence, for instance one where the applicable feature is contested.
