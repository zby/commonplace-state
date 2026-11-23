---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The same edit hand-authored in reaction to an incident is maintenance: the system learned, and people outside its loop did the selecting."
    reason: "The note's discriminator is binary: either the system's own loop selects (continual learning) or people outside the loop select (maintenance). A common case falls between the two: the system's loop proposes and evaluates a candidate from deployment evidence, and an operator approves or rejects it before installation. Under the stated criteria the reader cannot tell whether the approving operator is inside the system's loop (continual learning) or outside it (maintenance). The case is not exotic; it is the usual shape of governed artifact-revision loops, so the dichotomy leaves a central boundary unmapped."
    level: warn
  - scope: passage
    quotes:
      - "Parametric continual learning keeps its own plasticity-stability and catastrophic-forgetting problems"
    reason: "Extreme case: online gradient continual learning updates weights directly from each batch, with no candidate that could be rejected and no separate authorization step. The note names it continual learning, but its criteria (choosing, validating against regression, assigning an authority path) map onto it only strainedly; the 'for retained candidates' qualifier in the last paragraph suggests direct updates are handled differently without saying how."
    level: info
  - scope: passage
    quotes:
      - "when consumed as evidence or advice"
    reason: "Adjacent case: an autonomously written memory record retrieved later as advice does change behaviour, and behavioral authority counts advice as a force. The note contrasts 'storing content' with 'behaviour-changing writes' but does not say whether such advisory writes are ungoverned storage or low-force behaviour-changing writes that also need governance. Coverage is possible but strained."
    level: info
outcome: warn
---

# Review

## Summary

The note's two frameworks are the three representational forms and the governance functions (select, validate, authorize, coordinate), plus a binary split between continual learning and maintenance. The three-form enumeration is inherited from the linked definition and its boundaries hold here; the note also says a write need not touch all three forms.

The weak boundary is the learning/maintenance split. It is drawn by who selects — the system's own loop or people outside it — and a human-approval gate on system-proposed candidates sits between the two without a stated rule. Direct parametric updates and advisory memory writes are coverable but strained. A sentence placing operator approval relative to "the system's own loop" would resolve the main case; no new category is needed.
