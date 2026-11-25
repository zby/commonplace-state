---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "routing and loading the relevant artifacts"
    reason: "The framework splits loop work into harness-code functions and three irreducible semantic LLM competences. Selecting which artifacts are relevant to a novel failure or task falls between the two columns. The note assigns routing and loading to harness code, but in open-ended work, the note's own stated condition, a relevance decision about a new case is meaning-dependent. Neither interpreting text into action (1), diagnosing and synthesizing (2) nor trade-off judgment (3) clearly names it. Under the note's own criteria, this case falls outside both columns."
    level: warn
  - scope: passage
    quotes:
      - "three irreducible semantic competences remain on the frozen base LLM"
    reason: "Choosing what to work on next is a semantic loop function: which failure to pursue, which store region to revisit, when to stop a search. The scheduler note the article follows assigns this choice to the model. It maps onto competence 3 (weighing consequences) only by stretching that competence from judging candidates to prioritizing work. Coverage is possible but strained."
    level: info
outcome: warn
---

# Review

## Summary

The enumeration under test is the harness/LLM split and its three competences. The note's own framing defines the space: the semantic work an autonomous selection-based learning loop needs in open-ended work, once harness code takes over mechanical and structural work.

Boundary cases tried:

- **Simplest instance.** A loop whose checks are all codified needs none of the three competences. The open-ended-work restriction excludes this case, so it is not a counterexample.
- **Candidate evaluation without a fixed check.** This maps cleanly onto competence 3.
- **Store refactoring and criterion revision.** The note explicitly reduces these to competences 2 and 3, and the mapping holds.
- **Relevance selection for context assembly.** This case falls between the columns, as recorded in the WARN finding. The harness list claims it, but in novel cases it is semantic, and no competence names it.
- **Prioritizing which work the loop does next.** This fits competence 3 only if that competence is stretched.

The Scope section admits that bottlenecks found in practice can be added. That makes the list open, but the WARN still stands: the note currently claims routing for harness code. Placing relevance selection on one side of the split explicitly would resolve the WARN without adding a fourth competence, if it can be folded into competence 1 or 2.
