---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "an absence of that kind is a validator's result rather than a reviewer's finding"
    reason: "This is stated as an established fact about the system, but the only validator the note describes (ADR 046) resolves quotations that are present and marked verbatim; it does not detect that a claim lacks a retained passage. The sentence carries the counterfactual of a proposed artifact-side bound with the confidence of the reported experimental findings next to it, so those findings appear to show more than they do."
    level: warn
  - scope: passage
    quotes:
      - "on this evidence it is not a reviewer capacity exhausted at current corpus sizes"
    reason: "The observation (uncapped reviewers read up to 22 artifacts and the three largest offers passed) is presented as supporting a conclusion about reviewer capacity. A PASS on the largest notes has no ground truth to compare against, so the observation cannot distinguish 'no loss' from 'undetected loss'. 'On this evidence' marks the source but not the gap, so support for one claim is presented as covering another."
    level: warn
  - scope: passage
    quotes:
      - "the bound is held by a validator that fails the note, not by a reviewer that stops reading"
    reason: "The artifact-side bound and its enforcing validator are the note's own proposal (the Scope section says it decides neither N nor a validator rule), but this section describes them in a present-tense declarative register. A reader can recover the proposal status only from the distant Scope section."
    level: info
outcome: warn
---

# Review

Much of the note keeps its statuses recoverable. Corpus counts and the paired experiment are reported observations and are bounded in Scope. The relativity claim is derived from linked premises. The Descartes and Lamport material is marked as analogy, and the open questions are labelled.

Two passages blur status. In the first, the remark about the four uncapped findings goes beyond reinterpreting them: it states that an absence of retained support "is a validator's result". That presents a capability the described validator lacks, as if it followed from the experiment. In the second, the absence of divergence among the largest-offer notes is presented as evidence about reviewer capacity, but the experiment could not observe loss in those cases. The artifact-side bound is written in present tense throughout its section. Because Scope marks it as undecided, that is informational only.
