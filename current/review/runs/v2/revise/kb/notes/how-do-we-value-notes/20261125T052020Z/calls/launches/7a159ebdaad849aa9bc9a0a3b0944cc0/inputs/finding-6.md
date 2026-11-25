---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/semantic/epistemic-status-blur.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: bd228e747f9d216fd50fbf3b406d3976f31e2206282036910bee1fac45e1e4a4
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a38acad87c914bb7ae48d968378006fb
completed-at: '2026-11-25T05:23:10Z'
findings:
- scope: passage
  quotes:
  - combine structural maturity (type), review verdicts, recency, and link-strength-weighted
    inbound links
  reason: 'The structural-proxy lens sits under ''Commonplace currently spreads note
    valuation across'' and uses the same declarative register as the shipped answerability
    invariant. That makes a combined quality score read as current practice. The two
    notes it rests on present it as a proposal: one is titled ''Notes need quality
    scores'', and the other calls itself an ''Exploratory question set, not an established
    scoring model''. A proposed mechanism therefore reads with the confidence of an
    established one. The page does not separate the lenses Commonplace actually enforces,
    such as answerability at admission, from lenses it only proposes.'
  level: warn
- scope: passage
  quotes:
  - Structural validation, source grounding, and critique gates check validity more
    strongly than anything checks learning value or reader update
  reason: This comparative observation about Commonplace's gates is stated flatly,
    with no evidence presented or cited. It is the premise to which the next sentence
    applies the explicitly marked conjecture. Placement under Unsettled gives some
    tentativeness, but the reader cannot tell whether this premise is an observed
    fact or the author's assessment.
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/3502efd098cf51c4ee687805/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/outputs/review-epistemic-status-blur.md
raw-output-sha256: ed07ad23f253a6d07f55f3536bc5b2d92e4a0656e3937b07a8c72cec2b0cc2da
---

# Review

## Summary

The note mixes several statuses: a stipulated invariant (answerability), theory claims from linked notes, proposals (quality scores), an explicitly marked conjecture (underselection), and open questions. Most of these are recoverable. The Stakes section gives a clear retirement condition, Unsettled is a named open section, and the underselection argument is flagged with "Under the conjecture that" and "can".

The weak point is the Current answer framing. "Commonplace currently spreads note valuation across five partial lenses" applies one present-tense register to lenses with different standing. Answerability is a stipulated admission invariant that Commonplace ships. The structural-proxy combination is a proposal and a brainstorm in its source notes. The "partial" label signals that coverage is incomplete. It does not signal that some lenses are only proposed. That is the WARN.

The Unsettled premise about which gates check validity more strongly is a plausible assessment, but its status as an observation or a judgment is not stated. Because the section is explicitly unsettled, it is INFO.
