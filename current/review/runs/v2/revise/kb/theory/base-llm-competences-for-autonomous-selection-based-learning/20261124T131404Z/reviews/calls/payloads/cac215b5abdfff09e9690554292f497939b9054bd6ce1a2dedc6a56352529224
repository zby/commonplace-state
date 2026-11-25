---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "an autonomous [selection-based learning](./definitions/selection-based-learning.md) loop"
    reason: "Selection-based learning is an active vocabulary term in AGENTS.md. Its first mention has a link but no inline gloss. The reader cannot tell what makes a loop selection-based (for example, that candidates are generated and kept or discarded by a selection step) without following the link. The note's title and argument depend on this term. Add a short gloss beside the link."
    level: warn
  - scope: passage
    quotes:
      - "Following [scheduler–LLM separation](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)"
    reason: "'Scheduler–LLM separation' is a KB-internal principle. Here it is used as the justification for offloading work to harness code, but the sentence does not say what is separated from what or why. A short clause would let the reader follow the argument without the link, e.g. that deterministic code handles scheduling and bookkeeping while the model handles semantic interpretation, because code errors are easier to detect and correct."
    level: warn
  - scope: passage
    quotes:
      - "can block outer-loop learning before the store itself saturates"
    reason: "'Outer-loop learning' is not defined in the note. The reader can roughly infer that it means improvement from updating the store rather than the weights, but the note never states this. Consider glossing the term or replacing it with 'learning through store updates'."
    level: info
  - scope: passage
    quotes:
      - "while transfer tests check each kind of decision on its own"
    reason: "'Transfer tests' is not explained. The reader cannot tell what is transferred, or from where to where. A short phrase saying what such a test checks would make the bootstrap procedure clear."
    level: info
outcome: warn
---

# Review

## Summary

Most of the technical vocabulary is either standard (LLM, harness, token budgets, held-out gains, ablations) or glossed by its surrounding sentence. For example, the list item for competence 1 effectively explains "operative change": prose must "govern its behavior under realistic context loads". "Criterion revision" is also clarified later in the same paragraph as "proposing a revised check". "Human-assisted bootstrap" is explained by the clause that follows it.

The main gaps are in the opening paragraph. The note's central term, "selection-based learning", is an active vocabulary term, and its first mention has a link but no gloss. The note also uses "scheduler–LLM separation" as the reason for its whole split without saying what that separation is. Either gap forces a first-time reader to follow a link before the argument makes sense. Two later terms, "outer-loop learning" and "transfer tests", are less critical but would also benefit from a brief gloss.
