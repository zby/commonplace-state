---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: f2419977ea2ca2adc64b5e1cec80307125cef1c3ddcd35727b8c85310517f854
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:29Z'
findings:
- scope: passage
  quotes:
  - A long source cannot be captured verbatim into markdown at full fidelity, because
    the consumer's context window is finite and because copyright forces trims.
  reason: The description and section heading claim that layering is forced for every
    framework 'whose consumer is an LLM and whose sources are real documents'. The
    two premises cover only part of that class. A finite context window limits what
    a consumer reads at once, not what the snapshot stores, since a full verbatim
    snapshot can be read in chunks. Copyright forces trims only for sources whose
    licence forbids full reproduction, and long public-domain or openly licensed documents
    are outside that. The note states no transfer relation from the premises' domain
    (long, reproduction-restricted sources stored under a single-read budget) to the
    claimed class. The surplus is not marked conjectural, and the rival-absence claim
    that would close the gap is asserted without a presented search.
  level: warn
- scope: passage
  quotes:
  - The claim bites exactly where capture is lossy, which is to say wherever the sources
    are long.
  reason: The Scope section equates 'lossy' with 'long'. Under the note's own premises,
    however, lossiness also requires a reproduction restriction or a storage constraint.
    That makes the boundary statement broader than the support, since it includes
    long, freely reproducible sources. It is a supporting claim, but it defines the
    area of reliance the note invites.
  level: info
contract: verdict
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/dfd8f33cb827770b6f8dc882/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/dfd8f33cb827770b6f8dc882/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-unwarranted-scope.md
raw-output-sha256: f5e072ceb2dbe0382a500c7f55ba6f2522c8f7470a93031bc8e0a0d4efa27ebf
---

# Review

**Claimed scope.** Two scopes are in play. (1) Citations to lossy captures can assert no more fidelity than the capture preserved, and no downstream notation, locator or gate can raise it. (2) Per the description and the layering section, capture is necessarily layered for any LLM-consumer framework over real documents.

**Presented support.** Claim 1 is derived from the layer definitions and the derived-copy rule's mechanical-derivation precondition. Its exercised domain matches its claimed domain: wherever a passage lacks a mechanical rule back to its source, notation cannot supply one. The Scope section correctly withdraws the claim for lossless sources. Claim 1 passes.

Claim 2 is derived from two premises, a finite context window and copyright trims, plus an unreported rival search, and is backed by one corpus observation (ADR 046's casebook run). Those premises hold for long sources under reproduction restrictions and for designs that store only what one read can consume. The claim is phrased for all frameworks with an LLM consumer and real sources. The note neither argues why the premises reach freely licensed long sources or chunked full-text snapshots, nor marks that reach as conjecture. Because claim 2 appears in the description and frames the note, this is a WARN rather than INFO.
