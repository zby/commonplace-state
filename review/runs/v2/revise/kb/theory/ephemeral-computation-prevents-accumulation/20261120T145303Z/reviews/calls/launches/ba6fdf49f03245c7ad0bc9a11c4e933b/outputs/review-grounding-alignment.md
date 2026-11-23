---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Kirsch's [critique of ephemeral software](https://www.blackhc.net/essays/future_of_software/) identifies production knowledge that must survive replacement: discovered edge cases, integration constraints, interface expectations, and audit-relevant decisions. That motivates retaining the knowledge; it does not require every version of the code to be its sole carrier."
      - "[The Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/) — evidenced-by: supplies the production-knowledge pressures motivating durable carriers"
    reason: "The note gives evidential weight ('evidenced-by') to an untracked external URL with no tracked kb/sources/ ingest, no pinned snapshot, and no verbatim quotation on the page, so the supporting passage is absent and cannot be verified against the four attributed production-knowledge items or the inference drawn from them."
    level: fail
  - scope: passage
    quotes:
      - "[Codification](./definitions/codification.md) assigns an operation to a symbolic consumer."
    reason: "The linked definition defines codification as moving a natural-language rule or operation into symbolic form whose consumers are held to a governing reference (explicitly including adopted model packages, schemas, and human clerks following exact rules), not merely assigning an operation to a 'symbolic consumer'; this misstates the target's criterion even though the contrast with retention still holds."
    level: warn
  - scope: passage
    quotes:
      - "The [codification–relaxing account](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) addresses when to move operations between interpretation and assigned execution; it should not be read as a binary choice between learning and forgetting."
    reason: "The linked note explicitly scopes itself to code extraction versus replacing an extracted component with a more general method under scaling, and states that relaxing reverses extraction rather than symbolic membership and can replace it with an adopted codified package; summarizing it as moving 'between interpretation and assigned execution' overstates its stated scope."
    level: warn
outcome: fail
---

# Review

Three linked library artifacts align with the note's use: `[deployed system](./the-deployed-system-not-the-model-is-the-unit-of-learning.md)` supports setting the learning boundary at the full behavior-determining system rather than one component, and the two adjacent `extends` links in `Relevant Notes` accurately characterize their targets.

Grounding fails on the evidential citation to Kirsch's essay, which links directly to an untracked external URL without an ingest, snapshot, or verbatim quote, leaving material support unavailable for verification. In addition, the two codification citations modestly distort their linked targets' criteria and scope, requiring tighter alignment with the linked definitions.
