---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A proposed per-artifact write brief would add another named input
  - A write brief, if ever adopted, would require an additional explicit read in every
    consuming procedure.
  - A write brief becomes another named role only if its companion proposal is adopted
    first or in the same decision.
  reason: The 'Unmistakably proposed' instruction says a proposal never presents shipped
    behavior as open. The note's own current-state anchor says write briefs were adopted
    through ADR 092 as validated sidecars read by cp-skill-write. Yet the opening
    calls the write brief 'proposed', Option 1 says 'if ever adopted', and Option
    3 makes a write-brief role conditional on a 'companion proposal' being adopted.
    These passages present shipped behavior as still open and contradict the anchor.
    They should be rewritten so the role question is about delivering the already-adopted
    brief through the assembler, not about adopting briefs.
  level: warn
- scope: document
  quotes: []
  reason: 'The ''Feasibility and commitment scope'' instruction asks the proposal
    to state, for each candidate presented as adoptable, whether the requested commitment
    is a bounded probe, reversible trial, routine reliance, or a choice that creates
    costly dependencies, and to match support to that scope. Options 2 and 3 are presented
    as adoptable, but neither states its commitment scope. Their feasibility rests
    on implicit analogy: the commonplace-review criterion-selection precedent appears
    in Current state but is never argued as a witness for either option. Risks list
    obstacles such as tool dependency and moved complexity, but the note does not
    say whether adopting Option 3 is a reversible trial or a routine dependency of
    every writing path. If it is the latter, the note also lacks the entrenchment
    argument: what would depend on the command, what reversal would disturb, and the
    warrant for it.'
  level: warn
- scope: passage
  quotes:
  - A new-note pilot shows that mode-specific information prevents repeated discovery
    or lost task intent without asking code to choose the note's contribution.
  - The multistage experiment can be reconsidered after its own behavior has been
    tested.
  reason: The 'Adoption criteria and unresolved choices' instruction requires a probe
    to name its knowledge gap, cost, output, and stop condition. It also requires
    a deferred choice to name the observation that could change it, the condition
    that returns it to decision, and the cost of waiting. The pilot names a knowledge
    gap and a success shape, but not its cost, its output artifact, its stop condition,
    or how it avoids building the full assembler it is meant to evaluate. The deferred
    multistage-consumer choice is a bare promise of later testing. The note nowhere
    accounts for the cost of waiting while skill prose keeps growing, although its
    Problem section motivates the proposal by that growth.
  level: warn
outcome: warn
description: Retained verdict review of kb/reference/proposals/deterministic-write-context-assembly.md
  against kb/reference/types/design-proposal.md
contract: verdict
note: kb/reference/proposals/deterministic-write-context-assembly.md
criterion: kb/reference/types/design-proposal.md
note-sha256: 8d88aca21af4908f63fe4ec46f324a084aed32be1466710c9e3125caa2fef62d
criterion-sha256: ecf1501289ea51492dbed7d976f50816f6344643e805d5dc5355659696d5730e
target-sha256: 8d88aca21af4908f63fe4ec46f324a084aed32be1466710c9e3125caa2fef62d
target-capture: kb/reports/state/review/runs/v2/20261116T105440Z/artifact/reviews/b37b913747f470fa2091a46b/inputs/target/kb/reference/proposals/deterministic-write-context-assembly.md
observation: kb/reports/state/review/runs/v2/20261116T105440Z/artifact/reviews/b37b913747f470fa2091a46b/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261116T105440Z
launch: cc12cbc3645a491cb88c959b5a2674b4
completed-at: '2026-11-16T10:55:26Z'
raw-output: kb/reports/state/review/runs/v2/20261116T105440Z/calls/launches/cc12cbc3645a491cb88c959b5a2674b4/outputs/review.md
raw-output-sha256: e558f4b55cf361a92ea72cd436605c07b3d8edeb23158b51034a5c482bf8282f
format: 2
---

# Review

## Summary

The proposal largely does what the design-proposal type asks. The description leads with "Proposal:". The opening states the problem: deterministic resolution mechanics are accumulating in skill prose. It names the outcome sought, a clearer ordinary writing path with semantic judgment kept in the skill, and explains why code could deliver it. The current-state anchor is dated, and it separates shipped facts (ADR 018, 086, 088, 092, the review-side precedent) from conjecture.

The option space is inspectable. It covers four materially different alternatives: prose-only composition, a path resolver, a closed mode-aware assembler and an open provider mechanism. The note explicitly separates the two independent axes, coding the assembly and opening it to providers. Forces, free choices and risks expose the consequences that distinguish the options. Each option carries an operativity path, as required for a proposal anchored after 2026-07-24. Option 4's path correctly shows that provider registration would change writing behavior without edits to the consuming skills. Transferable rationale is cited through rests-on edges rather than inlined. Concrete detail, such as the write-brief recursion rule, answers a named design question and is not presented as settled implementation. The note recommends no adoption.

Three instructions are partly unmet:

- **Write-brief status.** The note treats write briefs as unadopted in several places, while its own anchor records them as adopted. This is a stale inconsistency that presents shipped behavior as open.
- **Commitment scope.** The adoptable options do not say what kind of commitment adoption would be. A writing path that depends on a package command could become costly to reverse, so the missing scope matters here.
- **Probe and deferral conditions.** The pilot and the deferred multistage choice lack the cost, output, stop and return-to-decision conditions that the type requires for productive deferral.

None of these undermines the proposal's overall structure, so the outcome is WARN rather than FAIL.
