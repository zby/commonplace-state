---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "current task pointers, unresolved gates, directional dependencies, and a success state"
    reason: "The list of active-work-state contents drifts across the note. The definition gives goal, next action, blockers, still-binding decisions, open evidence gates and closure criteria. This later list adds directional dependencies, which are absent from the definition, and drops decisions. The final paragraph's design list (project scope, resume pointer, explicit gates, lifecycle closure, extraction) is a third variant. The lists are compatible rather than contradictory, but a reader cannot tell which set is constitutive."
    level: info
  - scope: passage
    quotes:
      - "The stronger design is a workshop surface"
    reason: "The note says 'workshop surface' here and 'workshop layer' in the next paragraph. The context makes them read as the same thing, but the shift is a likely terminology drift that needs confirmation."
    level: info
outcome: pass
---

# Review

The title, description and body agree. Active work state is memory in a broad sense but not retrospective memory or chat history, and it needs pointers, gates and closure. The opening concession ("memory in the broad sense") does not contradict the title, because the title qualifies the memory it excludes as retrospective. The handling of decisions is also consistent: still-binding decisions belong to active state, and durable notes receive extracted decisions after closure.

There is no contradiction. The only drift is in which component lists are constitutive and in a minor workshop surface/layer wording shift.
