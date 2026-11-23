---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The qualifier 'between neural and symbolic' in the title is not used by the central mechanism. A shared interface with name-based resolution hides the implementation from callers for any pair of interchangeable implementations. The deletion test leaves the argument intact. The note is plainly scoped to the LLM/code boundary, though: it is framed by constraining and codification, which concern that boundary. So this is intentional domain scoping rather than a narrowing that obscures a broader theorem."
    level: info
outcome: pass
---

# Review

Qualifiers in the title, description and opening:

- **"Unified"** (calling conventions). Load-bearing. The argument depends on both kinds of component presenting the same interface.
- **"Bidirectional"**. Load-bearing. The note argues both directions: codification (steps 1–3) and relaxing (step 4, and the routing-rule test run).
- **"Between neural and symbolic"**. The mechanism does not use any property specific to neural or symbolic components. It is ordinary interface substitution. The application to constraining and codification needs the qualifier, and the note is domain-scoped to that boundary. INFO under the LLM-domain-scoping rule.
- **"Name-based dispatch"** (description and mechanism). Load-bearing for the LLM-caller case: the LLM emits a string, and the runtime must resolve it to either kind of implementation.
- **"llm-do demonstrates"** (description). Marks llm-do as an instance rather than a condition of the claim. It does not narrow the claim.

No qualifier narrows the central claim in a way that warrants WARN.
