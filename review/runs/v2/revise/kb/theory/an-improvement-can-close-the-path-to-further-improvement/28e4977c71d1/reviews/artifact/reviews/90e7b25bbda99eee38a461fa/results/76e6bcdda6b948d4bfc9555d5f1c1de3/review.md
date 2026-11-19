---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Checking the current gain does not check that the revision mechanism survives.
  reason: 'DOUBTFUL — universal: a check of the current production gain never checks
    survival of the revision mechanism — counterexample: when declared production
    performance itself depends on the revision mechanism during the evaluated episode
    (an agent whose task set requires adapting instructions to new task variants mid-run,
    or a production pipeline that reuses the same evaluator the revision workflow
    uses), removing the mechanism degrades the measured gain, so the production check
    does detect the loss; the premise holds only when production and revision are
    decoupled, which the hypothetical stipulates but the general sentence does not
    state. The same case dents the necessity reading of the description''s ''only
    when'' — coupled revision is protected without being separately included in the
    checked scope, unless ''checked scope'' is read to absorb it — LOCAL — instance'
- scope: passage
  quotes:
  - a successor that destroys the only applicable revision path fails the requirement
    even if its production performance improves
  reason: 'DOUBTFUL — universal (implied sufficiency, carried by the heading ''When
    non-regression protects the revision path''): including the revision capability
    in the checked scope makes non-regression protect the path — reason: the successor
    fails the requirement in fact, but the check that enforces it may not detect the
    failure at transition time; a revision path can pass a pre-adoption test (the
    workflow runs, a dummy change installs) and still be unable to carry a real later
    revision through adoption and use, e.g. an evaluator broken only for the kinds
    of proposals that later arise. Inclusion is necessary but not sufficient; protection
    also needs a check that exercises the full path the note names (evidence → proposal
    → adoption → installation → later use). The note''s description already states
    only the necessary condition, so the commitment survives once the section''s sufficiency
    phrasing is qualified — LOCAL — instance'
- scope: passage
  quotes:
  - The speed gain can be real. The lost revision capability can also be real.
  reason: 'HOLDS — possibility claim: a change can improve a declared production dimension
    while removing the revision capability. The hypothetical agent that installs a
    faster configuration with no revision workflow is a coherent instance, and one
    coherent instance is enough to establish a ''can'' claim; the hunt found no reason
    that production speed and revision capability must move together in general.'
- scope: passage
  quotes:
  - A non-regression requirement protects only the capabilities included in its checked
    scope.
  reason: 'HOLDS — universal, read as a claim about what the requirement enforces:
    an unchecked capability may survive by accident or through coupling (see the first
    finding), but the requirement does not protect it as such. The hunt found no case
    where a non-regression requirement enforces a capability outside what it checks;
    the coupled case is protection by the checked capability, not by the requirement
    reaching an unchecked one.'
- scope: passage
  quotes:
  - A successor can replace its revision workflow and preserve the capability, provided
    the replacement can carry another revision through to use.
  reason: 'HOLDS — functional identity of the capability: the revision capability
    is individuated by what it can do (carry a revision through to use), not by the
    component or files that implement it. Hunted cases where a replacement with equal
    reach still counts as loss (e.g. provenance or audit trail lost) bear on other
    capabilities, not on the revision capability as the note defines it.'
- scope: document
  quotes: []
  reason: 'HOLDS — unstated: whether a revision capability is lost is fixed relative
    to a declared system boundary and kind of revision, so a maintainer-held path
    does not count as the agent''s path. Counterexample hunted: systems where all
    revision is maintainer-driven and agent self-revision was never expected, where
    calling its absence a ''loss'' would mis-sort; the Scope section fences this (''The
    loss is relative to the declared system boundary and kind of revision'') and the
    deliberate fixed-deployment case, so the premise survives at its stated scope.'
outcome: report
description: Retained report review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/90e7b25bbda99eee38a461fa/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/90e7b25bbda99eee38a461fa/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews
launch: 76e6bcdda6b948d4bfc9555d5f1c1de3
completed-at: '2026-11-17T07:25:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/calls/launches/76e6bcdda6b948d4bfc9555d5f1c1de3/outputs/review.md
raw-output-sha256: 77b097f9ce3a7564d559330d1903035c57ee3619f18fc216ca890f5cb2bfd7b9
format: 2
---

# Premise decomposition: An improvement can close the path to further improvement

**Register:** claim
**Central commitment (one sentence):** A successor can improve a declared production dimension while disabling the machinery that would produce another revision, and non-regression prevents this only when the revision capability is included in the checked scope.

## Premises and counterexamples

The commitment has two parts. The first is a possibility claim. It consumes the premise that production gain and revision capability can separate, and the premise that a production check does not see the revision mechanism. The second is a conditional about non-regression. It consumes the premise that a requirement protects only what it checks. In the section's sufficiency reading, it also consumes the premise that including revision capability in the checked scope is enough to catch its loss. Two background premises let "loss of revision capability" be judged: the capability is identified by its function rather than its component, and loss is relative to a declared system boundary.

The possibility half survives: one coherent hypothetical establishes "can". Both dents fall on the non-regression half and are local. The general sentence that a production check never sees the revision mechanism needs the decoupling condition that the hypothetical quietly supplies. The sufficiency phrasing in "When non-regression protects the revision path" exceeds what the description commits to, because a checked scope can include the capability and still miss a latent break. Each dent can be repaired with a qualification in `## Scope` without changing the claim. No premise failed globally.

## For the human

Look first at "Checking the current gain does not check that the revision mechanism survives". It is stated universally, and it fails when production performance depends on the revision mechanism. Add the decoupling condition, or say that coupled revision counts as being within the checked scope.
