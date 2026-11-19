---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/complexity/claim-to-section-ratio.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 4488fb59279bf0b9950ea54f8bb89c1f399c1638f40ddab82b94101170b40786
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/37901b3a01dba32eff802cdb/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/37901b3a01dba32eff802cdb/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 45267bdcbd6447768c1c7cae94f1790a
completed-at: '2026-11-16T22:09:16Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/45267bdcbd6447768c1c7cae94f1790a/outputs/review-claim-to-section-ratio.md
raw-output-sha256: ec61e7d346b03dc643ab0415a4ad71d6a92f5fb2357c23e463a2e35d0237ffcb
format: 2
---

# Review

## Summary

The note's five body units each carry a distinct claim or a separately necessary support unit; none restates the framing of another.

## Claims and sections

Distinct non-obvious claims:

1. Citation fidelity is fixed at capture and non-increasing downstream; only re-capture raises it. Fidelity is distinct from authority, and capture sets a ceiling beneath which authority is earned (lead section).
2. Capture of long sources is forced into layers by finite context and copyright, so a snapshot is an extraction rather than a copy (`Capture is layered because it is forced to be`).
3. Notation cannot repair fidelity because a paraphrase has no mechanical derivation rule, so a `verbatim` mark on a paraphrase creates a trusted unchecked copy (`Why notation cannot repair it`).
4. A source-span locator must encode the layer as well as the position (`Corollary`).

Support units:

- `Scope` carries the boundary condition (lossless capture of short sources collapses the layers and restores position as the binding constraint) plus the practical consequence that provenance quality is decided at ingest. Both are boundary and consequence material the argument needs.
- `Open Questions` is a conventional, short unresolved-frontier list, not a restatement.

Five headed or lead units against four claims plus one boundary section and one open-questions list: the sections do not outnumber the claims plus their separately necessary support units. The `history has one chance` paragraph inside the notation section links the claim to a general rule rather than repeating earlier framing, and it is not a section of its own.
