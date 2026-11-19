---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: 3224c054f701239072486cdd66ab3929406feab114650468b44740091b4c875f
outcome: fail
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: f30d85fe3a98495a9b5d8f8638bb893f
completed-at: '2026-11-12T08:22:39Z'
---
### Summary

The note explains its central library/workshop distinction and both bridge directions inline. A few supporting concepts still assume familiarity with Commonplace's document types and agent procedures, so an external reader must infer their meaning or follow links.

### Findings

- Major: The opening paragraph introduces `structured-claim` and “the structured-claim contract” without explaining what distinguishes this document type from a note. “Structural-refinement path” names a progression, but the example does not explain what changes when a note adopts that contract. The link to the current type system does not supply an inline definition.
- Minor: The final open question introduces “Skills” as if readers already know what they are. The linked “type signatures” and `/ingest: source → source-review` example illustrate inputs and outputs, but do not explain that a skill is a reusable procedure an agent follows. This leaves the proposed implementation of extraction bridges dependent on agent-tooling context.

### Suggested Revision

Briefly explain the structured-claim type's defining structure when first naming it, and describe the progression as adopting more explicit document structures. Introduce the last question with “Skills—reusable procedures an agent follows—already have implicit input and output types…” before retaining its example and link.

## Result: FAIL
