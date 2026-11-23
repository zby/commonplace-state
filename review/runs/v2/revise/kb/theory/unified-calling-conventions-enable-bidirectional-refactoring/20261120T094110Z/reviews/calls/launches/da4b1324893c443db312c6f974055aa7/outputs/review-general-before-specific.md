---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "[llm-do](https://github.com/zby/llm-do) implements this through a hybrid VM"
    reason: "\"The mechanism\" is framed around one system (llm-do, proper nouns, `.agent` files). The following section, \"Why this matters for constraining\", gives the general argument: without a unified interface, codification is a breaking change. The llm-do section partly exemplifies that argument. However, the introduction already states the general rule, that a unified calling convention makes refactoring across the boundary local, before either section. The reader therefore meets the rule first. The order is defensible, but leading with the general rationale is a possible improvement."
    level: info
outcome: pass
---

# Review

Adjacent section pairs:

- **The mechanism → Why this matters for constraining.** The first section is llm-do-specific. The second section is more general. Because the introduction already states the general claim, the llm-do section does not precede the first statement of the rule. It is recorded as INFO, not WARN.
- **Why this matters for constraining → The scheduler layer.** This pair moves from general to specific, which is the correct order.
- **The scheduler layer → The connection to typed callables.** The second section links llm-do to a separate theory note. It does not state the general rule that the scheduler exemplifies, so no reordering is indicated.
- **The connection to typed callables → Open Questions.** This pair is not a specific-to-general pair.
