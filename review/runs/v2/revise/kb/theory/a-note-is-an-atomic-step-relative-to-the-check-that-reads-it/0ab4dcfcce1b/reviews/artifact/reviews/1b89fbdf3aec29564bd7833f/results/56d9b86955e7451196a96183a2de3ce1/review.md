---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Sizing a step to its checker rather than to the material is old. Descartes'
  reason: The Descartes paragraph is the weakest-fitting branch in the note. By the
    note's own reading, Descartes sizes the parts 'to the solution', which is closer
    to material-relative sizing than to the checker-relative sizing the main claim
    needs. It adds a second external source to ground, and the note concedes that
    it is analogy, not evidence. The Lamport paragraph makes checker-relativity explicit
    and bounds the transfer, so it does the precedent work alone. The Descartes material
    could shrink to a clause or move to a separate lineage note. Destination unclear,
    so INFO.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/1b89fbdf3aec29564bd7833f/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/1b89fbdf3aec29564bd7833f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 56d9b86955e7451196a96183a2de3ce1
completed-at: '2026-11-16T22:37:53Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/56d9b86955e7451196a96183a2de3ce1/outputs/review.md
raw-output-sha256: 1a96e66a767609d34196fdc0434dced592acd69d9b072bcdaef50532e12d1473
format: 2
---

# Review

## Main claim

The note claims that atomicity is relative to the check that reads a note. It
also claims that, for Commonplace's grounding check, the unit of step size is
the unquoted source. The independence of the co-loading bound from the checking
bound frames the argument. The artifact-side placement is the note's practical
proposal.

## Side material that stays

Most side material supplies a premise, boundary or concession that the
argument needs:

- **Artifact-side versus review-side placement.** This section motivates the
  bound. It names the silent-failure mode, which explains why the placement
  matters.
- **Occurrence-versus-representativeness limits and the `(snapshot required)`
  case.** These set the boundaries of the unquoted-source unit.
- **Joint-support paragraph.** It answers the obvious objection to bounding the
  artifact. It also states where the two bounds couple, which qualifies the
  independence claim.
- **Corpus counts and the paired-experiment rereading.** These are the note's
  evidence that the two bounds diverge in practice.
- **"What kind of number a step size is."** This section reads like a branch,
  because the Scope section says the note does not decide N. It is still needed:
  the experiment showed uncapped reviewers coping, which invites the reply that
  no bound is needed. The section answers that reply by moving the justification
  from reviewer capacity to auditability. Without it, the evidence section
  would undercut the proposal.
- **Open Questions.** These are already demoted correctly. They do not compete
  with the main claim.

## Branch worth trimming

The historical-precedent passage is the only material with weak support for the
main claim. Lamport's reader-relative proof-step detail directly shows checker
relativity. The note also bounds that transfer explicitly. Descartes adds an
older lineage, but the note itself describes his parts as sized to the
solution. That is a different axis from sizing by checker. The passage adds
grounding surface and length but no premise. Its best destination is unclear,
so this is INFO, not WARN.
