---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '- [The Flawed Ephemeral Software Hypothesis](https://www.blackhc.net/essays/future_of_software/)
    — evidenced-by: supplies the production-knowledge pressures motivating durable
    carriers'
  reason: 'Violates the Origin is not corroboration and evidenced-by conventions:
    an evidenced-by link must either report a refutation attempt stating what the
    claim risked and whether the evidence was recorded after or independently of how
    the claim was built, or state in its context phrase how the evidence qualifies
    or bounds the assertion. Describing Kirsch''s critique as motivating durable carriers
    states neither corroboration nor qualification/bounding.'
  level: warn
- scope: passage
  quotes:
  - '[Codification](./definitions/codification.md) assigns an operation to a symbolic
    consumer.'
  - The [codification–relaxing account](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)
    addresses when to move operations between interpretation and assigned execution
  reason: 'Unfaithful representation of linked theory notes: codification.md defines
    codification as moving a rule or operation into symbolic form by holding consumers
    to a governing semantic reference (either via a formal-semantics language or by
    adopting a consumer such as a pinned model package, not by assigning to a ''symbolic
    consumer''), and codification-and-relaxing-navigate-the-bitter-lesson-boundary.md
    specifically concerns code extraction versus relaxing to a more general method
    (which can itself be codified by adoption) across exact-spec and proxy-theory
    regimes, not moving between interpretation and ''assigned execution''.'
  level: warn
- scope: passage
  quotes:
  - '- [Retained system-definition artifacts enable persistent deployment-time adaptation](./retained-artifacts-enable-persistent-deployment-time-adaptation.md)
    — extends: describes one useful retention path'
  reason: 'Footer link text uses an outdated title rather than the target note''s
    current title (''Deployed systems can learn from feedback with fixed model weights''),
    departing from the ''- [title](path) — label: context phrase'' footer convention.'
  level: info
- scope: passage
  quotes:
  - The house may keep the failure it exposed, a corrected dependency account, or
    a test for later scripts.
  - 'A house can combine both choices: keep a theory and examples, generate a short-lived
    implementation, test it, then retain the result that matters.'
  reason: Introduces 'The house' / 'A house' without scoping what entity it names,
    blurring whether the retaining actor is the deployed system established in the
    opening or an external organization.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/theory/COLLECTION.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/theory/COLLECTION.md
note-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/42d0703b0ac445f98de8cedf93dce431/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/b63123346a143e1306f9540d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: 42d0703b0ac445f98de8cedf93dce431
completed-at: '2026-11-20T15:01:45Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/42d0703b0ac445f98de8cedf93dce431/outputs/review.md
raw-output-sha256: 71fb09f48ef2fe3e2fdf6a18d5cfa8c512a2cb8c81f9264dbca16beda740cf78
format: 2
---

# Review

The note is properly placed in `kb/theory/`: it states a transferable, truth-apt claim about cross-run accumulation across deployed systems rather than recording Commonplace-specific selections or state. Its universal modality and explicit `## Scope` conditions map the assumptions under which the no-accumulation conclusion holds, the body remains composable as a single premise about artifact lifetime versus surviving state, and external source use is hosted in the body within the collection's source-grounding bound.

Two collection conventions go unmet in its outbound links and representation of linked notes. First, the `evidenced-by` footer entry for Kirsch's essay treats a motivating critique as evidential support without framing it under `kb/theory/COLLECTION.md`'s rule for `evidenced-by` (either a refutation test with stated risk and independence, or an explicit statement of how the source qualifies or bounds the note's claim). Second, the section contrasting retention and codification mischaracterizes both `definitions/codification.md` and `codification-and-relaxing-navigate-the-bitter-lesson-boundary.md`, breaching the collection's obligation to represent linked notes faithfully. Two lower-severity issues—an outdated title in one footer link and the unintroduced term "the house" / "a house"—are recorded as informational notes.
