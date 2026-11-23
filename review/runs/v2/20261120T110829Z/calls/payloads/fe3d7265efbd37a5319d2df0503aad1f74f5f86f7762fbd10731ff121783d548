---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Ordinary information hiding swaps two implementations that share the same execution substrate and caller model"
    reason: "This section opening repeats the opening paragraph's contrast ('Unlike ordinary code-to-code information hiding ... this boundary crosses two different execution regimes ... so the abstraction leaks asymmetrically'). The opening states it as a thesis; the section develops it and leads into the two bullets, so the paragraph cannot be deleted outright. This is setup followed by development, which is a weak signal."
    level: info
  - scope: passage
    quotes:
      - "Moving code back to a prompt behind an unchanged call site works only where the caller's latency budget, cost budget, and error handling can absorb model execution"
    reason: "The Scope bullet repeats the closing paragraph of the previous section ('call sites that may move back to prompts must be written for fallible, higher-latency calls'). The two sit at a section boundary in different roles: one is a prescription, the other a scope limit. The bullet adds the examples of tight inner loops and deterministic paths, so the overlap is partial."
    level: info
outcome: pass
---

# Review

## Summary

No section opens with a full re-explanation that could be deleted, and no
closing paragraph previews a later section's enumeration in full.

- "The mechanism" opens with new content: the llm-do runtime.
- "Scope" opens directly with its bullets.
- "Why this matters for constraining" opens with the friction argument that
  separate invocation surfaces create, which is new.
- "The connection to typed callables" opens by summarising the linked note,
  which is new to this note.

Two partial overlaps sit at section boundaries. Both are setup-plus-development
or prescription-plus-limit pairs, so they are recorded as info. The opening
paragraph also previews the three swap moves in one sentence, but that is a
thesis sentence, not a paragraph at a section boundary, and the gate does not
flag it.
