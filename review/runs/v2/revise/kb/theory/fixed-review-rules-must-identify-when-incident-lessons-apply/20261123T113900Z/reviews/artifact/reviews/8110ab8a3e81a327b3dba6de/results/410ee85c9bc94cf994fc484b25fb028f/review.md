---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The incident shows what the review must distinguish, not that the review rule
    must change.
  reason: UNSUPPORTED — the note generalizes from one constructed example to the claim
    that incidents never require changing the rule. It does not show that recognizing
    a lesson needs no change to the rule. Its own title makes use conditional on the
    rule identifying when lessons apply, which, read literally, suggests the rule
    should encode that applicability. The conclusion is asserted, not derived.
- scope: passage
  quotes:
  - A reviewer following the original instruction could still recognize it.
  reason: UNSUPPORTED — the note never says how the reviewer recognizes the connection.
    The first paragraph says the instruction 'does not tell the reviewer which earlier
    failure bears on the page at hand', so whatever makes recognition possible lies
    outside the instruction. The note does not name that source (reviewer competence,
    how the incident is recorded, or something else). 'Could still' therefore leaves
    open whether the fixed rule did any work.
- scope: passage
  quotes:
  - It does not tell the reviewer which earlier failure bears on the page at hand.
  reason: THIN — this establishes a gap in the instruction. It does not establish
    the title's 'only if', that use of new lessons depends on identifying applicability.
    The title also makes the rule the subject that must identify ('a fixed review
    rule can use lessons … only if it can identify'), while the body places identification
    in the reviewer. The joint between the two subjects is never stated.
- scope: passage
  quotes:
  - The test is not whether the reviewer retrieved the incident. It is whether the
    reviewer distinguishes apparent corroboration from independent support on the
    new page.
  reason: 'THIN — the example supports applying the distinction as the deciding step.
    The contrast overstates it: retrieval remains a precondition, since a reviewer
    who never consults the incident cannot apply its lesson. ''Not retrieval'' needs
    to be ''not retrieval alone''. The test is also stated for one incident type,
    and the note does not show it generalizes.'
- scope: passage
  quotes:
  - The lesson still applies if the new sources also share an origin and the claim
    relies on their independence. A lookup by source name would miss that connection.
  reason: HOLDS — the example states its applicability condition explicitly (shared
    origin plus reliance on independence). The new page shares no source names with
    the old one, so a name-keyed lookup cannot match. Both steps follow from the construction.
outcome: report
description: Retained report review of kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
target-sha256: a7d8f78490c6408db95d26b89cf898e260f17eba96f51d3c586e69911bc78a71
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/410ee85c9bc94cf994fc484b25fb028f/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/artifact/reviews/8110ab8a3e81a327b3dba6de/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews
launch: 410ee85c9bc94cf994fc484b25fb028f
completed-at: '2026-11-23T11:42:40Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply/20261123T113900Z/reviews/calls/launches/410ee85c9bc94cf994fc484b25fb028f/outputs/review.md
raw-output-sha256: 4466b4b20e83d410cc1862ac00f0a843e4eaf208d440b0bee043686cb0836388
format: 2
---

# Friction check: fixed review rules and when incident lessons apply

**Central claim (one sentence):** A fixed instruction to consult past incidents can stay unchanged as incidents accumulate, but a new incident helps only when the reviewer recognizes which distinction it teaches applies to the case at hand, so incidents change what the review must distinguish rather than the rule.

## Filter
**Filter:** SURVIVES

The note asks for three things at once: the rule stays fixed, new lessons get used, and applicability is judged case by case. These can coexist if the applicability judgment comes from something other than the rule text. The note implies that but does not name it. The claim concretizes to one thing. There is a strain, not a contradiction: the title makes the rule responsible for identifying applicability, while the body says the rule cannot do that and gives the job to the reviewer.

## Thinnest joints

The two UNSUPPORTED joints rank first because they carry the note's conclusion. One is the claim that the rule need not change. The other is the claim that a reviewer following the unchanged rule could still recognize the connection. Neither names the mechanism that turns an unchanged rule plus an incident record into a recognized applicability. The note's first paragraph rules out the instruction as that mechanism. The THIN joints come next. The "only if" in the title is motivated by a gap but not shown to be necessary, and it shifts subject from rule to reviewer. The retrieval/distinction contrast is directionally right but phrased as exclusive. The example's internal logic is the strongest part and holds.

## For the human
Start with the closing sentence: name what lets a reviewer under the unchanged rule recognize applicability. If that capability depends on how incidents are recorded, it may undercut "the review rule need not change".
