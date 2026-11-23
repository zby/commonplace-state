---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "and commissioning follow-up work such as a rewrite remains a separate decision"
    reason: "The bullet maps ADR 138 onto the note's three decisions. The first two fit the ADR: a stop ends the run with a continuation record, and kept answers are carried over so later runs do not re-ask. The third clause is a looser fit. The note's third decision is 'the operator should act now'. ADR 138 supports it differently: the operator acts later, by naming an answers file or a run in a new command, and continuation is taken up in an interactive session. Rewrite commissioning is not the ADR's framing of that separation. The attribution holds in substance, but stating the ADR's own mechanism (the operator acts later by naming the stop's output) would match the target more closely."
    level: info
outcome: pass
---

# Review

The note identifies its concepts with linked concepts in several places. Each was checked against the target:

- "the oracle asymmetry analyzed in" the guard note: the target names oracle asymmetry as the factor that sets the direction of over-guarding. Valid.
- "the [unresolved frontier]—Commonplace's discoverable field of possible further work": matches the definition's opening sentence verbatim. Valid.
- "under unsafe substitution", grounded in the insufficient-summary note: the target defines unsafe substitution as trusting an insufficient summary and skipping the source path. The note's use, misclassifying severity from an uninformative blocker, matches. Valid.
- "context efficiency binds first on per-window feasibility": the target says "feasibility binds first" and names the per-window face. Valid.
- The traversal-logging note "separates noticing a defect during reading from prioritizing and fixing it": the target says "separate noticing from fixing" with a one-line log entry. Valid.
- The objectives sentence citing the epistemic-layer note: the target says the layer "improves allocation under a goal, not the goal" and does not choose the objective. Valid.
- The ADR 138 three-decision mapping holds for two of three clauses directly and for the third in substance; see the info finding.

All targets resolved.
