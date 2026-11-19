---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["A human approval required for adoption is part of the process that selected the revision."]
    reason: "UNSUPPORTED — the note moves from approval being formally required to approval helping select the revision. Requirement establishes that the judgment sits on the adoption path, not that it discriminates. A rubber-stamp approval that would pass any proposal is required yet changes no outcome; the opening sentence says the evaluator 'controls whether a proposed change enters use', but the note never states the counterfactual condition (the evaluator could and sometimes would refuse) that makes a required gate a contribution rather than a formality. The later 'Whether approval was required for that adoption is a fact about the process' repeats the same substitution of requirement for control."
  - scope: passage
    quotes: ["This matters when deciding whose contributions explain a system's improvement."]
    reason: "THIN — the opening establishes that a controlling judgment helps determine which revision results; this sentence treats that as a contribution to the improvement. Selecting among proposals explains the improvement only when the selection excludes worse alternatives. The Scope section concedes 'Approval does not establish quality', so the note itself shows that contributing to which revision entered use is not yet contributing to its being better. The bridge from selection to explaining improvement is not stated."
  - scope: passage
    quotes: ["A test available to the proposing system can be optimized without improving the capability it is meant to assess; human approval does not remove the need to justify the assessment."]
    reason: "THIN — the two clauses are joined by a semicolon offered as an inference, but the first concerns a proposer gaming an available test and the second concerns human approval. The note does not say whether the human approver relies on that gamed test (in which case approval inherits its weakness) or on independent judgment. Without that link the sentence reads as two separate cautions rather than a reason why approval needs justification."
  - scope: passage
    quotes: ["An externally supplied selection judgment must still be acknowledged as a contribution."]
    reason: "THIN — the 'must' follows from the opening claim only if the judgment actually helped determine the result, so it inherits the unsupported requirement-to-control step above. It also leaves unstated whom the acknowledgement is owed in and why boundary-independence holds; the Open Question shows the reporting form is still unresolved, so the obligation is asserted ahead of its mechanism."
  - scope: passage
    quotes: ["A favorable assessment of a proposal that is never adopted does not establish an improvement of the deployed system."]
    reason: "HOLDS — given the linked operative-change definition (a change needs a consumer path to affect later behavior), an unadopted proposal does not reach the deployed system, so a favorable assessment of it cannot show the deployed system improved. The joint is sound, though its placement in a section about one episode containing both roles leaves its relevance to that section implicit."
outcome: report
---

# Friction check: Evaluation that controls adoption helps determine the change

**Central claim (one sentence):** A judgment contributes to which system revision results when it controls whether that revision is adopted, and an assessment of an already-adopted change does not make that contribution to its adoption, regardless of who or what makes the judgment.

## Filter
**Filter:** SURVIVES

The note wants three things at once: the distinction is role-based rather than agent-based, one episode can contain both roles, and redescription cannot move a judgment between roles. These coexist. Roles attach to particular judgments relative to a named transition, so one maintainer can approve and later assess, and the process facts fix which judgment controlled adoption. The concession that later assessment may cause a different transition (rollback or future revision) keeps the claim scoped to one transition rather than splitting it.

## Thinnest joints

The weakest joint is the step from "approval was required" to "approval helped select". The central claim is stated in terms of control, but every worked inference uses requirement. These come apart exactly in the rubber-stamp case, and the note's description-invariance argument depends on the stronger notion it never states. The second joint is related: even granting control, the note treats selection as contributing to improvement. Its own Scope disclaimer ("Approval does not establish quality") weakens that link. The Goodhart sentence and the acknowledgement obligation are thinner as inferences than as claims. Each reads plausibly, but the note does not supply the connecting premise. The unadopted-proposal joint holds because the linked definition carries it.

## For the human
Look first at whether "controls adoption" needs a counterfactual condition (the evaluator could and sometimes would refuse) so that required-but-nondiscriminating approval is not counted as selection.
