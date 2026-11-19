---
description: Distillation produces artifacts of a different kind — transformation into a new shape, not lossy selection from the source. Memory distillation is the concrete case in hand (traces → preferences, ADRs, skills), reframing memory primitives as an inventory of shapes rather than denser traces.
type: kb/types/note.md
traits: [title-as-claim, has-comparison]
tags: []
status: seedling
---

# Distillation is transformation, not selection

The intuitive framing of memory [distillation](./definitions/distillation.md) (directed context compression) is lossy compression — a trace contains some material, and distillation picks the subset worth keeping. The framing misses what distillation actually does when it works: produce an artifact of a different kind.

The examples below are all memory distillation — the richest concrete case in hand — but the claim applies to distillation generally.

## Distilled artifacts are not subsets of the trace

The same trace distills to different kinds of output, none of which are reducible to a subset of the trace's tokens:

| Trace | Distilled artifact | What's new |
|---|---|---|
| Debugging a flaky test | Preference rule: *always reproduce before attempting a fix* | A universally-quantified claim — the trace contained one incident, the rule covers all future cases |
| Choosing between frameworks | ADR: motivation / alternatives / consequences | Structure (three roles) that wasn't in the trace; alternatives articulated more crisply than they were discussed |
| Recurring corrections | A linting rule in the codebase | A change of medium: natural-language correction becomes an executable check |
| A successful procedure | A runbook, a skill, or code | Generalization from one run to a reusable operator; sometimes a change of medium |

Each artifact introduces structure absent from the trace — universal quantification, condition clauses, rationale, sometimes a new medium entirely. [Codification](./definitions/codification.md) (committing a procedure to a symbolic medium) is the extreme case, but shape-change happens within a single medium too. Calling this "capture the important parts" misses the shape-change that did the work.

## Implication for memory-system design

The lossy-compression frame suggests better trace-to-summary pipelines — as if the job were to produce a shorter trace. But no amount of trace compression produces a preference, an ADR, or a skill. Those are different shapes; the work is in the shape-change.

Memory primitives, then, are not denser traces but different kinds of objects. Each has its own structure, invariants, retrieval affordances, and lifecycle. A preference is a rule with scope and rationale that can be invoked, overridden, or retired — not a compressed trace. Designing a memory system is largely designing the inventory of shapes it supports, and recognizing that "traces → memory primitives" is not a single arrow but a family of transformations (trace → preference, trace → ADR, trace → skill, trace → convention, ...) each with its own target structure, each potentially applicable to the same trace, none subsuming the others.

## The substrate must persist

If distillates are transformations rather than subsets, they don't subsume their source — the raw trace contains material that no single distilled shape preserves. The inventory of shapes also evolves. A shape that captured something well at one point may be wrong later — not because the content changed, but because the operating context has shifted enough that a different form is now more useful. Three consequences follow:

- The raw trace is what can't be re-derived. Losing a distillate means redistilling; losing a trace means the underlying material is gone.
- Storage is finite, so perfect retention isn't possible — but the asymmetry argues for biasing toward trace retention over eager pruning.
- Distilled artifacts are not permanent products. They are current-best representations under the shape inventory in force at the time, and may need to be re-derived as the inventory evolves.
