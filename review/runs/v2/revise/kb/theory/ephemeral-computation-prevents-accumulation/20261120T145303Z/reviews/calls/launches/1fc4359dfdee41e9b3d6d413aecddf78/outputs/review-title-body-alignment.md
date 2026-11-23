---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "# Discarding all experience-dependent state prevents cross-run accumulation"
    reason: "Claim-focus and scope drift: the H1 title states only the narrow boundary condition that discarding all experience-dependent state prevents cross-run accumulation, whereas the body actually establishes a broader contrastive claim about ephemeral computation—that discarding a generated artifact removes only that artifact's reuse path and prevents cross-run learning only when no experience-dependent state survives elsewhere in the deployed system to affect later work (while retaining unused artifacts is storage alone)—and devotes most of its length (`What discarding saves and costs` and `Retention and codification are different choices`) to the maintenance, testing, auditability, safety, production-knowledge, and codification-vs-retention tradeoffs of discarding generated artifacts."
    level: warn
outcome: warn
---

# Review

The body does support the H1 title's literal statement as a boundary condition (under `What must survive` and `Scope`: when no experience-dependent causal path reaches a later run, cross-run accumulation cannot occur). However, the title has drifted narrower than and off-center from what the body actually argues and covers.

The note opens with ephemeral computation—generating, using, and discarding an artifact—and its central claim is contrastive: discarding an intermediate artifact removes one reuse path rather than all learning, because cross-run accumulation persists whenever another carrier in the deployed system retains a causal effect for later work, whereas retaining unused scripts yields storage without learning. Beyond that core claim, roughly two-thirds of the body (`What discarding saves and costs` and `Retention and codification are different choices`) specifically examines generated-artifact disposal—maintenance savings versus regeneration cost, pre-disposal review and exact-byte auditability, safety and purity, Kirsch's production-knowledge requirements, and the orthogonality of artifact retention and codification. A title naming ephemeral computation or discarding generated artifacts alongside the surviving-state condition (or trimming the body to the narrower state-retention boundary) would restore alignment.
