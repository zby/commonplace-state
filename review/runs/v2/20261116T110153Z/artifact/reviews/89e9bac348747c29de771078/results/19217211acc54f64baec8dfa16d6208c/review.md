---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: 'Feasibility and commitment scope go unmet. None of the three options presented
    in the design space gets its own feasibility argument or witness with named unresolved
    obstacles. Option 1 has only a cost remark, and option 2 has only an entrenchment
    risk. The note also never says what kind of commitment it requests: a bounded
    probe, a reversible trial, routine reliance, or a choice that creates costly dependencies.
    Options 1 and 2 would create a shared layer that other kinds come to depend on,
    yet no option says what would depend on it, what reversal would disturb, or what
    would warrant it. The Forces section names the entrenchment warrants only in general
    terms.'
  level: warn
- scope: passage
  quotes:
  - No consumer yet. What would consume **G** is a second kind of knowledge work run
    on Commonplace by an operator who is not its author
  reason: The type spec asks for an operativity path for each option that changes
    behaviour-determining organization. The note gives one path for G as a whole.
    Option 1 promotes the refinement interface as the declared G, and option 2 allows
    bespoke additions and extracts G later. These options would reach consumers at
    different times and through different channels, for example a promoted interface
    or type specs versus extraction after the fact. The note does not distinguish
    those paths.
  level: warn
- scope: passage
  quotes:
  - The trigger for an adoption decision is the first completed second-kind run with
    the comparison recorded.
  reason: 'The choice among the options is deferred for evidence, and the note names
    a trigger and some outputs: reuse counts, K_P needed, G maintenance and the outcome
    comparison. It does not meet the remaining productive-deferral conditions. It
    gives no cost for the probe and no stop condition other than completion. It does
    not account for the cost of waiting or for any expiry of the alternatives. It
    does not say which option the trial run would follow. If the run follows option
    1 or option 2, it may create the shared-layer dependency the run is meant to evaluate,
    and the note does not say how the probe avoids that.'
  level: warn
- scope: passage
  quotes:
  - Three options for how **G** comes to exist. The proposal does not choose.
  reason: The option space varies how G comes to exist but takes the borrowed configure(G,
    K_P) decomposition as given. That decomposition is consequential here, because
    it splits what is shared from what each kind acquires. The note offers no rival
    decomposition under the same boundary commitments, for example shared per-family
    layers or shared K across kinds. It also does not state that none has been found.
    Option 3 rejects any shared layer; it is not a rival way to decompose one.
  level: info
outcome: warn
description: Retained verdict review of kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
  against kb/reference/types/design-proposal.md
contract: verdict
note: kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
criterion: kb/reference/types/design-proposal.md
note-sha256: 756b823f38fd3e59583f849f7dff5410799fdfe37375cc6e92a6873c008573d1
criterion-sha256: ecf1501289ea51492dbed7d976f50816f6344643e805d5dc5355659696d5730e
target-sha256: 756b823f38fd3e59583f849f7dff5410799fdfe37375cc6e92a6873c008573d1
target-capture: kb/reports/state/review/runs/v2/20261116T110153Z/artifact/reviews/89e9bac348747c29de771078/inputs/target/kb/reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md
observation: kb/reports/state/review/runs/v2/20261116T110153Z/artifact/reviews/89e9bac348747c29de771078/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T110153Z
launch: 19217211acc54f64baec8dfa16d6208c
completed-at: '2026-11-16T11:02:42Z'
raw-output: kb/reports/state/review/runs/v2/20261116T110153Z/calls/launches/19217211acc54f64baec8dfa16d6208c/outputs/review.md
raw-output-sha256: a8ae939b12f42c28b02d1e29dc3cd869cdb61dd0230ed2ea1461733c578896ec
format: 2
---

# Review

## Summary

The note conforms to the design-proposal type overall. It has a dated current-state anchor. The current state separates held facts from the claim that is not held, which is that transfer has not been demonstrated. The note states the problem and the conjecture with an explanatory case. The case rests on cited theory: machinery amortization, the cost of acquiring K_P, and routinization. The note declares a universality axis and sets out three materially different options with their distinguishing consequences. It explicitly declines to choose. Option 2 is called "a reason to expect it to be chosen, not a decision", which satisfies the no-adoption-decision clause. The forces are relevant and cited. The adoption criteria give supporting evidence and defeating evidence as cost comparisons within the second kind, and they limit what one run can establish. The description leads with "Proposal:". The note never presents proposed behaviour as shipped.

The note falls short of the type spec where the spec asks for support to match the commitment. First, it does not classify the requested commitment, and it gives no option a feasibility argument or witness. Second, it gives one operativity path for G as a whole, not a path for each option. Third, its deferral to a second-kind run omits the probe's cost and stop condition, the cost of waiting, and how the probe avoids creating the dependency it is meant to evaluate. The `configure(G, K_P)` decomposition also has no rival and no statement that no rival has been found. This is recorded as an info finding, not a warn.

The conjecture itself is close to a transferable claim, but it is stated about Commonplace's own machinery and is framed as the subject of the proposed test. Its general premises are cited from `kb/theory/` notes. Keeping it in the proposal is therefore acceptable under the "transferable theory stays in notes" clause.
