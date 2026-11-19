---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the second precept sizes the parts to the solution and rests long chains on simple links"
      - "proof-step detail is set by the reader who checks it, and structured proofs make error-finding possible rather than inevitable"
    reason: "The Descartes and Lamport footer entries come closest to inflation. Their context phrases paraphrase what the body already quotes and states: the parts are sized to the solution, step detail depends on the reader, and structured proofs make error-finding possible. Only the typed label is new, so the entries pass the gate's second question narrowly."
    level: info
outcome: pass
---

# Review

## Summary

No footer entry fails both of the gate's questions, so the Relevant Notes footer is not inflated.

## Entry-by-entry assessment

Two entries supply navigation that the body does not:

- **ADR 079** has no body link. The body mentions only "the review-side budget currently in force". The footer names the decision and labels it as the review-side placement.
- **Title as claim enables traversal as reasoning** is not linked in the body. It adds an `enables` edge that no other part of the note supplies.

Most other entries repeat a body link. Each adds a typed relation that the inline citation does not state:

- The linked-note-discharges, warranted-autonomy, boundary-of-automation, derived-copy and citation-fidelity entries mark these links as `grounds`. In the body, they appear as "an instance of the general rule" or as a "because" clause.
- The short-composable-notes entry marks its link `contrasts`. That relation is the role the linked note plays in the opening's two-bound distinction.
- The five-link-cap report entry adds `evidenced-by`. It also says the note rereads the report rather than accepts it, so the reader can decide whether to load the record.

The Descartes and Lamport entries are the weakest, as the info finding records. They do not fail the test, because the `evidenced-by` label is relationship semantics that the body's inline citations do not carry.
