---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Any use-shaped artifact depends on its sources — whether its content is worked out from them (a derived copy) or generalizes beyond them (an abstracted rule, answerable to its sources as evidence)."
      - "The repair follows the regime: re-derive and compare where the content is recoverable from the source, re-examine the support where it exceeds it."
    reason: "The managed-staleness background paragraph carries a real boundary condition (judgment-priced Level B verification makes hand-maintained dependents unavoidable), but it also elaborates the general dependent-knowledge taxonomy and the repair split, which the rule does not use. The contrast could likely be made in about half the length; kept at INFO because the paragraph sets the scope against which the Level A flip is argued."
    level: info
  - scope: passage
    quotes:
      - "The sweep pattern is hand-authored, but it executes as a strict mechanical extraction — and precondition 4's amortization argument is what keeps the pattern's authorship acceptable instead of a quiet regress."
    reason: "The instance only needs to show the enforced state; this sentence re-runs precondition 4's regress argument already made in full above. A short clause or a pointer to precondition 4 would do the same work."
    level: info
  - scope: passage
    quotes:
      - "(root feeds wheel builds via `pyproject` `force-include`; `src/commonplace/_data` serves editable installs)"
    reason: "The build-path gloss explains why two copies exist, which the linked ADR 027 already records; the instance's role is only to show the trivially checkable file-identity case. Probably compressible to the ADR pointer, though the gloss is short."
    level: info
outcome: pass
---

# Review

## Summary

Detail is mostly proportional to its argumentative role. The asymmetry section is compact and carries the rule's justification. The four preconditions are long, but each carries a boundary condition or inference step; precondition 4's regress answer is needed to stop the obvious objection that the validator is itself an unchecked claim. The Consequences bullets cite evidence briefly. The four instances each do one job, showing the rule in a different state of application.

Three passages run somewhat beyond their job. None justifies a WARN. The managed-staleness paragraph contains a general taxonomy of dependent knowledge that the rule does not use, although the paragraph as a whole defines the scope. Instance 1 restates precondition 4's amortization argument. Instance 4 includes a build-layout gloss that the linked ADR already holds. Each is a candidate for light compression in place, not a structural problem.
