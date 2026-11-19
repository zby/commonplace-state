---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - 'What "checked" requires — and its limits'
    reason: "The type spec asks that the claim's limits be stated under their own `## Scope` heading, which review gates that test scope look for. The note has known limits: preconditions 1–4, the judgment-regime boundary in 'Where the rule applies', and the executor-generated-evidence case. These limits are spread across sections with other names, so no `## Scope` section exists. A rescoping edit cannot narrow the claim in one place, and scope gates will not find a Scope section."
    level: warn
outcome: warn
---

# Review

## Summary

The note largely conforms to the `note` type spec's authoring instructions. The title is a strong, compressed handle. The main claim, that a copy has exactly two valid states (checked or absent), appears in the first paragraph. The body is design rationale, not imperative procedure; the "Never write…" bullet is a consequence of the rule, not a workflow step. Adjacent notes are linked inline and in a Relevant Notes footer, and each footer link has a relationship gloss. Open Questions follows the template.

The one unmet instruction is the Writing Shape rule that limits belong under `## Scope`. The note knows its limits and states them at length. The rule applies only at the deterministic end of derived knowledge. Enforcement requires a derivation rule, machine-locatability, ground truth at validation time and a validator that bottoms out. Natural-language summaries and executor-produced evidence fall outside it. But these limits live inside "Where the rule applies" and "What 'checked' requires — and its limits", mixed with mechanism and argument. They are not collected in the dedicated section the spec names. The note does not meet the omission condition, "no limit is known", so the section should be present. Moving or summarizing those applicability conditions into `## Scope` would satisfy the instruction without changing the argument.
