---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Ephemerality also does not imply safety or purity. Temporary code can consume resources, expose data, or change persistent state. Even a pure computation's output may guide a consequential decision. Approval, isolation, and result checking depend on those effects, not on whether the generated file survives."
    reason: "Execution safety, purity, approval, and isolation are orthogonal to the note's main claim about when cross-run accumulation fails. The only learning-relevant clause (changing persistent state) is already stated as a boundary condition in `## Scope`. Remove this branch from the note (or rehome the execution-governance claim to a safety/isolation note; the linked operational-knowledge note already carries a scope caveat against reading disposal as a security guarantee)."
    level: warn
  - scope: passage
    quotes:
      - "Testing and review can happen before disposal. A temporary program can be checked against a retained test suite, inspected before execution, and leave a record of its result. What disposal removes is the ability to inspect or rerun those exact bytes later, unless another record preserves them. Independent regeneration need not reproduce the same program."
    reason: "Pre-disposal quality checks, post-hoc exact-byte inspection, and non-reproducibility of independent regeneration are software-verification and auditability claims rather than premises or boundary conditions for cross-run accumulation. The note already accounts for retained test results and test suites in `## What must survive`, while historical/audit continuity is owned by the linked note `ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md`. Remove this paragraph or rehome any uncaptured auditability point there."
    level: warn
  - scope: passage
    quotes:
      - "Discarding a generated artifact avoids maintaining that particular reusable object: version compatibility, stale assumptions, dependencies, and retrieval need not be managed for it. Reuse instead requires regeneration or a different retained carrier. Which route is cheaper depends on repeated construction cost, validation cost, and the value of preserving what was learned."
    reason: "Noting that discarding avoids maintaining a specific reusable object may work as a brief concession motivating why systems discard generated artifacts, but the closing cost-comparison claim shifts from the causal condition for cross-run accumulation to the retention-vs-regeneration economics owned by `ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md`. Either tighten this to a one-sentence motivation or leave the economic trade-off to the linked note."
    level: info
outcome: warn
---

# Review

## Summary

The note's main commitment—stated in its title, description, and opening—is a causal condition for cross-run learning: discarding an intermediate artifact removes only that artifact's reuse path, whereas cross-run accumulation fails only when no experience-dependent state survives elsewhere in the deployed system to affect later work.

Most of the note stays focused on that claim, including the counterfactual account of what must survive, Kirsch's production-knowledge objection as a source setup, the contrast separating retention from codification, and the boundary conditions in `## Scope`. Branch bloat concentrates under `## What discarding saves and costs`, where the section widens from the accumulation condition into a general survey of ephemeral-code properties—runtime safety and approval, pre-disposal review and exact-byte reproducibility, and the economic trade-off between maintenance and regeneration. Trimming those side branches (and reframing or folding the remaining Kirsch concession into the main argument) will keep the note centered on cross-run accumulation while leaving operational continuity, audit history, and retention economics to the linked companion note.
