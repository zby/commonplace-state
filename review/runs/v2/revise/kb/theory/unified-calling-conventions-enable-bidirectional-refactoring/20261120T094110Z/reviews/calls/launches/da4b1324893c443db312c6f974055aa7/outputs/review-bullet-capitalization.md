---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "[constraining](./definitions/constraining.md) — the mechanism that unified calling makes frictionless"
      - "[codification](./definitions/codification.md) — the phase transition from neural to symbolic"
    reason: "These footer bullets begin with lowercase link text for registered terms. The lowercase mirrors the definition file names and works as an identifier-style label, so it is defensible, but it is inconsistent with sibling footer bullets that use capitalized titles such as \"[Prompting changes failure diagnosis...]\". Capitalizing the term or using the definition titles would make the list uniform."
    level: info
outcome: pass
---

# Review

The Open Questions bullets and numbered steps all begin with capital letters. In the Relevant Notes footer, the bullets that begin with `spec-mining-as-codification`, `instructions-are-typed-callables` and `operational-signals-that-a-component-is-a-relaxing-candidate` use file-slug identifiers as link text. Those are deliberately lowercase forms, so the gate exempts them. The `constraining` and `codification` bullets are borderline. They are ordinary words rather than slugs, but they match the registered term and file names. They are recorded as INFO rather than a failure.
