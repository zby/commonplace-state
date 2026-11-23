---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "'Neural' and 'symbolic' in the title stand for 'LLM agents' and 'Python functions', the only instance class the note works with (llm-do). Substituting the concrete terms leaves the mechanism and example unchanged, and the abstract terms forbid nothing extra. The note does argue that the mechanism is independent of llm-do: it rests on interface sameness, not on any llm-do feature. 'Neural/symbolic' is also the KB's conventional vocabulary for this boundary rather than a defensive widening. The note does not develop a second instance class beyond llm-do (it only gestures at Python-specificity in Open Questions), so the abstraction is probably slightly ahead of its evidence."
    level: info
outcome: pass
---

# Review

Central claim: unified calling conventions enable bidirectional refactoring between neural and symbolic components.

- **"Unified calling conventions"**. This stands in for "llm-do's shared namespace with name dispatch". Downgrading to llm-do would cut the argued generality. The note's mechanism ("if neural and symbolic components present the same interface, callers don't need to know") is explicitly independent of llm-do, which serves as a demonstration. This abstraction is earned by argument.
- **"Neural" / "symbolic"**. These stand in for LLM agents and Python functions. The downgrade test leaves the argument unchanged, and the forbids-test finds nothing the abstract wording excludes that the concrete wording allowed. The terms are the KB's standard names for the two sides of the constraining/codification boundary, and the note uses them concentrated in the claim rather than spread across every noun. INFO rather than WARN.

Abstraction is concentrated in the title and opening and is not distributed across the body. The body speaks concretely of `.agent` files, Python functions and `ticket_classifier`.
