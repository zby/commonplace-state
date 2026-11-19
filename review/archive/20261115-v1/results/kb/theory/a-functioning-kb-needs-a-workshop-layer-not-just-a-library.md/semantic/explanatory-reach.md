---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/semantic/explanatory-reach.md
criterion-sha256: 23694d2061f84a3a3c7330a5eaabd228b2d32bb87d604aa8d82fbce487a3cbdb
outcome: pass
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: 01c7f1c2f603497c825e9c62527e51d8
completed-at: '2026-11-12T08:25:07Z'
---
### Summary

The note offers a plausible mechanism for a workshop layer in a KB that supports active workflows: unfinished work requires state, dependencies, and expiry, while its useful results transfer into durable artifacts or external actions. This explanation is load-bearing within the workflow scope stated in the body, though the title claims a broader necessity.

### Findings

- INFO: The mechanism is present but thin. The note identifies different lifecycle requirements and the transfer of value on completion, but does not trace a concrete case where treating unfinished work as durable knowledge loses necessary state or obstructs completion. The table mostly classifies the difference. Removing the premise that the KB supports active workflows removes the stated reason for requiring a workshop layer; a durable-reference-only KB therefore challenges the unqualified title, while fitting the body's narrower scope.
- INFO: The hybrid-document qualification improves the explanation by allowing reusable procedures and task templates to combine persistent knowledge with temporary work. It does not erase the proposed lifecycle distinction or protect every possible document from counterexample. The open question about shared versus separate type systems also leaves the implementation claim open to challenge.

### Suggested Revision

Qualify the title to KBs supporting active workflows. Add one short example tracing how an unresolved dependency or completed task behaves under durable-artifact conventions, what operational information those conventions fail to express, and how workshop lifecycle handling resolves that failure. Keep the necessity of lifecycle handling separate from the unsettled choice of a shared or separate type hierarchy.

## Result: PASS
