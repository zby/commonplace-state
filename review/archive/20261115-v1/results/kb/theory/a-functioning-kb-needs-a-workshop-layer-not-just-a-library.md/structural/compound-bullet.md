---
note: kb/theory/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md
note-sha256: 69550b9aa320f6c0200baf5efdd2222b48aa5f8276f6ce43065c56f3cff23ea0
criterion: kb/instructions/review-gates/structural/compound-bullet.md
criterion-sha256: b9a07becb3b4ccdba9898051d02a681e020acb5e0296f97f355fa183418c474f
outcome: warn
profile:
  harness: codex
  launch-model: gpt-6.1-sol
  effort: medium
model: gpt-6.1-sol
run: kb/reports/state/review/runs/20261112T082159Z
launch: 9b8728aaed3646ef9be9a64d26a30d96
completed-at: '2026-11-12T08:27:06Z'
---
### Summary

The note has one compound bullet in “Open questions.” The other long bullets develop a single example, question, or link relationship with supporting detail.

### Findings

- WARN: The first “Open questions” bullet combines two independently useful design points: temporal subsystems should retain their own conventions because their state machines and lifecycles differ; all temporal subsystems need links into the shared library. The second point is buried inside a long answer to the type-system question. Each point can stand as a separate bullet without losing its meaning.

### Suggested Revision

Split the first “Open questions” item into two bullets:

- Should workshop and library share a type system, or remain parallel hierarchies? One library may support many temporal subsystems with different state machines, relationships, and lifecycles. Local conventions per subsystem are likely the right default, as [why directories despite their costs](./why-directories-despite-their-costs.md) already argues for tasks.
- How should temporal subsystems link into the shared library? Tasks, decision threads, experiments, and queues all depend on library content: notes, prompts, and established claims.

## Result: WARN
