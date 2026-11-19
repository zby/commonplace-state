---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "when the claim, the material it cites, and the inference from that material to the claim can be checked in one pass by the check that will be applied to it"
      - "a note can satisfy one and fail the other"
    reason: "Claim drift. The H1 reads as an unconditional statement that a note is an atomic step, qualified only by which check is meant. The body defines atomicity as a condition a note may fail: a note is an atomic step only when its claim, cited material and inference fit one pass of the applied check. It then shows notes that fail it, such as the eight single-claim notes citing six to nine sources. What the body establishes is that whether a note is an atomic step depends on the check that reads it, and that a note can fail that bound while satisfying the co-loading bound. A title such as 'Whether a note is an atomic step depends on the check that reads it' would match."
    level: warn
  - scope: passage
    quotes:
      - "This note states the rule for one check, Commonplace's grounding check, because that is where the unit of cost is clear"
    reason: "Scope drift, minor. The title states the general relativity claim. Most of the body argues narrower and prescriptive claims for the grounding check: the size bound belongs on the artifact rather than as a review budget; the unit of cost is the unquoted source; and N is a convention chosen for auditability. The body asserts the general relativity and backs it by linking to the oracle-domain and automation-verification notes. The description signals the grounding-check focus, so this is informational, not a mismatch."
    level: info
outcome: warn
---

# Review

## Summary

The title "A note is an atomic step relative to the check that reads it" is broadly supported. The body says explicitly that "a step is atomic relative to a particular check". Two alignment issues remain.

First, the title's wording asserts that a note *is* an atomic step. The body treats atomic-step status as a conditional property that a note may lack, and the corpus section rests on notes that are not atomic steps for the grounding check. A reader linking the title as a premise could take it to say that every note is one step for its check. The body denies that. This is a warn-level claim drift, fixable by rephrasing the title around dependence ("whether a note is an atomic step depends on…").

Second, most of the body develops grounding-check-specific and prescriptive claims (artifact-side placement, the unquoted source as unit, N as an auditability convention). The general title does not foreshadow them. The note scopes itself explicitly and the description carries the grounding-check focus, so this is recorded only as information.
