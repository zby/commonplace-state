---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
criterion-sha256: 59235341a958e65294c4656bfe1d2699b38544cfae3d4297cc2df141a8e10345
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: a5dde6c71f7a46d999de0b947b1027aa
completed-at: '2026-11-12T08:26:21Z'
---
### Summary

The note explains the need to retain in-flight work and connect it to durable knowledge. Its value-consumption framing misidentifies the mechanism behind that distinction: resolving work can end a document’s operational role without progressively reducing the document’s usefulness.

### Findings

- WARN: “Workshop documents consume value over time” and “A task becomes less useful as it progresses — its value is transferred into code, decisions, or actions on the world” frame workshop membership around declining document utility. The mechanisms described elsewhere are changing work state, dependencies, and eventual completion or disposal. A task or decision thread can become more useful during execution as it gathers context and alternatives, then lose its immediate operational role when the work resolves. The framing excludes such accumulating in-flight documents even though the proposed workshop layer covers them. The Scope section’s description of a repeatedly used runbook as “consumed like a workshop document” repeats the conflation: use does not itself imply depletion. Calling these documents hybrids does not resolve the mismatch between usefulness and work state.

### Suggested Revision

Describe the distinction in terms of the document’s role: library documents retain knowledge for reuse; workshop documents coordinate or record unresolved work and may be archived when that work resolves. Explain that completion transfers results into actions or durable artifacts, while the working document’s usefulness may rise or fall during execution. Update the value-trajectory row and runbook example to use the same distinction.

## Result: WARN
