---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "## What \"checked\" requires — and its limits"
    reason: "The type spec asks that a claim's known limits be stated under their own `## Scope` heading, omitted only when no limit is known. This note knows its limits: the rule applies only at the deterministic end of derived knowledge, and judgment-verified dependents remain hand-maintained. It also names four enforcement preconditions and failure cases, such as execution-produced evidence and judgment-based derivation rules. These limits are spread across `## Where the rule applies: the deterministic end of derived knowledge` and this section, mixed with the argument. There is no `## Scope` section that a rescoping edit could narrow or that scope-testing gates could find."
    level: warn
outcome: warn
---

# Review

## Summary

The note conforms to the `note` type overall. It misses one authoring instruction: its known limits are not collected under a `## Scope` heading.

## Assessment

- **Title as handle; main claim near the top.** The opening paragraph states the claim right away. A copy of recomputable truth must either be checked by a validator or be absent. Hand-maintained-and-trusted copies are ruled out.
- **Links to adjacent notes.** The note links inline where a link helps traversal. Its footer gives each relationship a short gloss.
- **Rationale in notes, procedure in instructions.** The body is design rationale. It covers the failure-mode asymmetry, the regime boundary set by check cost, the enforcement preconditions and instances. The imperative-sounding consequence ("Never write the unenforced natural-language version…") follows from the claim. It is not an operational procedure.
- **Open Questions.** This section is present and follows the template.
- **Scope.** The note has substantive known limits but no `## Scope` section. It states its applicability boundary and its preconditions and failure cases in two argumentative sections. The spec asks for these limits under their own `## Scope` heading. That would let a rescoping edit narrow the claim without rewriting it, and would let scope-testing gates find the limits. This is the one unmet instruction. The limits themselves are stated clearly, so this is a WARN rather than a FAIL.
