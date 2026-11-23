---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Crucially, this split unbundles two decisions that naive agent workflows collapse into one, while keeping a third workflow-memory policy orthogonal:"
      - '- **"This finding or answer should survive"** — an orthogonal workflow-memory policy ensuring later runs do not re-ask the same question, independent of whether triage routes the item to immediate action.'
      - "an operator's answer to a stop can be recorded so the next run does not re-ask"
    reason: "Cross-run answer persistence ('ensuring later runs do not re-ask the same question') is explicitly orthogonal to the conflict between context isolation and global prioritization. Recording scale-bearing local facts for later triage is already covered by step 1 and the following paragraph; elevating an ADR 138 workflow-memory policy to a third co-equal bullet dilutes the two-way unbundling of local stopping from global operator-attention allocation. Remove the orthogonal third bullet (and its lead-in clause) and trim the matching answer-carryover clause from the ADR 138 illustration, leaving that policy in ADR 138."
    level: warn
outcome: warn
---

# Review

The note's core commitment is well-bounded: isolating an agent's context for task focus removes the live comparison set required for relational global prioritization, explaining priority flattening under action-biased defaults and the trade-off in splitting narrow-deep execution from wide-shallow triage. Its boundary conditions, objections handled (standing priority rules and non-calibrated scalar cutoffs), contrast with oracle asymmetry, residual interface friction, and open questions all directly support that argument.

The one branch that dilutes the argument is the workflow-memory policy imported from ADR 138 into the unbundling taxonomy. The narrow-deep versus wide-shallow split directly unbundles two decisions—whether a local run should stop on a hard blocker or rule, and whether the operator should act now given competing work. Recording an operator's answer so future stateless runs do not re-ask the same question is a separate persistence concern, as the text itself concedes by calling it orthogonal and independent of triage routing. Because ADR 138 already houses that carry-over policy and the note already states that the isolated worker preserves scale-bearing local facts on a shared surface or stop record, removing this side branch sharpens the execution-versus-triage interface without losing anything the main claim requires.
