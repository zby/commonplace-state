---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '# Discarding all experience-dependent state prevents cross-run accumulation'
  reason: 'Claim-focus and scope drift: the H1 title states only the narrow boundary
    condition that discarding all experience-dependent state prevents cross-run accumulation,
    whereas the body actually establishes a broader contrastive claim about ephemeral
    computation—that discarding a generated artifact removes only that artifact''s
    reuse path and prevents cross-run learning only when no experience-dependent state
    survives elsewhere in the deployed system to affect later work (while retaining
    unused artifacts is storage alone)—and devotes most of its length (`What discarding
    saves and costs` and `Retention and codification are different choices`) to the
    maintenance, testing, auditability, safety, production-knowledge, and codification-vs-retention
    tradeoffs of discarding generated artifacts.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/ephemeral-computation-prevents-accumulation.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/ephemeral-computation-prevents-accumulation.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: f18648d7f9cb21126515c1f6596dbd77ae1d301b1cd78e359a3cded55203a826
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: 0be9a9fbf93b59ec891c5c638f434164720b6ca8c02f813dda875127938c49d1
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/1fc4359dfdee41e9b3d6d413aecddf78/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/artifact/reviews/c06e3066253d33eaf03a1b2a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews
launch: 1fc4359dfdee41e9b3d6d413aecddf78
completed-at: '2026-11-20T14:55:34Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/ephemeral-computation-prevents-accumulation/20261120T145303Z/reviews/calls/launches/1fc4359dfdee41e9b3d6d413aecddf78/outputs/review-title-body-alignment.md
raw-output-sha256: e1f544651154a0cc6fb5a4cc5079715562fadd844da9c20b186b0008f4a5d2f4
format: 2
---

# Review

The body does support the H1 title's literal statement as a boundary condition (under `What must survive` and `Scope`: when no experience-dependent causal path reaches a later run, cross-run accumulation cannot occur). However, the title has drifted narrower than and off-center from what the body actually argues and covers.

The note opens with ephemeral computation—generating, using, and discarding an artifact—and its central claim is contrastive: discarding an intermediate artifact removes one reuse path rather than all learning, because cross-run accumulation persists whenever another carrier in the deployed system retains a causal effect for later work, whereas retaining unused scripts yields storage without learning. Beyond that core claim, roughly two-thirds of the body (`What discarding saves and costs` and `Retention and codification are different choices`) specifically examines generated-artifact disposal—maintenance savings versus regeneration cost, pre-disposal review and exact-byte auditability, safety and purity, Kirsch's production-knowledge requirements, and the orthogonality of artifact retention and codification. A title naming ephemeral computation or discarding generated artifacts alongside the surviving-state condition (or trimming the body to the narrower state-retention boundary) would restore alignment.
