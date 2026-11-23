---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The type spec asks notes to state the claim's limits under their own `## Scope` heading and to omit that section only when no limit is known. This note has no `## Scope` section, yet it states several known limits inline: it restricts itself to the code-extraction case ('This note concerns the code-extraction case'), says retaining a prose convention alone is not codification, marks the scale-selection link as 'conjectural, not established', calls the bitter lesson 'a trajectory, not a law of nature', notes that most codification happens in a 'blurry zone' where the regime cannot be told, and relies on Ebrahimi et al. only for 'calculator-class' state tracking. Because these limits are spread through the body, a rescoping edit would have to rewrite claim paragraphs, and scope-testing gates will not find them under the expected heading."
    level: warn
outcome: warn
---

# Review

## Summary

The note mostly follows the `note` type's authoring instructions. The title gives a compact handle. The opening paragraph states the main claim: the regime is unknowable before scale tests it, so systems end up as hybrids. Adjacent notes are linked inline and in a Relevant Notes footer that states each relation. External sources are listed, consistent with the declared `has-external-sources` trait.

The "Working heuristics" section uses imperative phrasing. Each heuristic, however, comes with the design reasoning that justifies it, such as the arithmetic versus vision-feature regime and what-versus-how specs. It reads as design rationale, not as an operational procedure that belongs in `kb/instructions/`, so it does not break the rule to keep procedure in instructions.

One instruction is unmet: the Scope convention. The note knows and states real limits, but only inline across several sections. The type spec asks for these limits under a `## Scope` heading, so they can be narrowed without rewriting the claim and so scope-testing gates can find them. The fix is to gather those limits into a `## Scope` section. They are the code-extraction restriction, the conjectural status of scale selection, the blurry-zone caveat and the calculator-class bound on the Ebrahimi evidence.
