---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Any framework whose consumer is an LLM and whose sources are real documents faces
    both
  reason: 'The LLM-consumer condition carries the finite-context-window argument for
    why layering is forced. The central claim, that a citation cannot assert more
    fidelity than its capture preserved, does not use it: the derivation-rule argument
    in ''Why notation cannot repair it'' applies to any citation of a lossy capture,
    including human scholarship. The title and opening are already stated generally,
    so the qualifier does not narrow the central claim. It is intentional domain scoping
    of a supporting argument, recorded as INFO.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: f2419977ea2ca2adc64b5e1cec80307125cef1c3ddcd35727b8c85310517f854
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/d110f248a67fa47cbad66cde/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/d110f248a67fa47cbad66cde/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: 18e371f2e4dd4f359f55388cdce4b4f5
completed-at: '2026-11-16T22:12:29Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/18e371f2e4dd4f359f55388cdce4b4f5/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: b4aac575c0c26954bef6356f1a68c2a995c9df12713fd0d5cefeb8f45afdf477
format: 2
---

# Review

Qualifiers extracted from the title, description, opening and main argument:

- **"at capture" / "at ingest".** This is load-bearing. The claim locates where fidelity is fixed, and the argument relies on the absence of downstream derivation rules.
- **"by forced constraints" (description).** The deletion test leaves the non-increase argument intact: even if layering were a design choice, a paraphrase would still lack a derivation rule. The phrase explains why layers exist but does not narrow the central claim. Its scope adequacy is a matter for other gates.
- **Long or lossy sources.** This is load-bearing. The Scope section shows that removing the qualifier makes the bound vacuous for lossless captures, so it marks a true boundary.
- **LLM consumer.** It is used only to support "forced" and does not appear in the title or the central claim. INFO.

The title-level claim is not narrower than its argument. No qualifier artificially restricts the central claim's reach.
