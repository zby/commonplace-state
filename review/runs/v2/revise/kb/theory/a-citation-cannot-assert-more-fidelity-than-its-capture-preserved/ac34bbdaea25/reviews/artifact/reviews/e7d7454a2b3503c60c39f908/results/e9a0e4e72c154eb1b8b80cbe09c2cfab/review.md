---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/branch-bloat.md
contract: verdict
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/branch-bloat.md
note-sha256: e5082eaa9e2fe39e27d5276d72f9db01332ad4033eafbf1f7db6564f8ef626ad
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
target-sha256: ac34bbdaea25fa16536b2df33276f11f72c262a476a35f167202ccd2fab44a16
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/e7d7454a2b3503c60c39f908/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/artifact/reviews/e7d7454a2b3503c60c39f908/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews
launch: e9a0e4e72c154eb1b8b80cbe09c2cfab
completed-at: '2026-11-16T22:10:08Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/ac34bbdaea25/reviews/calls/launches/e9a0e4e72c154eb1b8b80cbe09c2cfab/outputs/review.md
raw-output-sha256: 673c964e9f10760a8667975497b2879b559481073e10939f25edf3b3f96307a7
format: 2
---

# Review

## Summary

The main claim, stated in the title, description and opening paragraph, is that a citation's fidelity is fixed by the capture layer holding the passage. It cannot rise downstream through notation; only re-capture raises it. Every side section either supplies a premise for this claim or bounds it. No branch needs removal, demotion or rehoming.

## Side material checked

- **Fidelity versus authority.** This paragraph separates the claim from the linked complementary note about authority earned per operation. Without it, a reader could take the note as contradicting that note. It is a trust-building contrast that bounds the claim, so it stays.
- **Forced layering.** The context-window and copyright constraints are the premise that capture of long sources must be lossy and layered. The aside on provider output filters is one clause. It marks the filters as provider-contingent rather than inherited, so it limits the premise rather than adding a new claim.
- **Why notation cannot repair it.** This section is the core argument for the non-increasing step. The follow-on paragraph on "history has one chance" is two sentences. It places the claim under a general rule without arguing a separate thesis.
- **Locator corollary.** This is the strongest candidate for a branch, because it makes a design claim about span locators. But it follows directly from the main claim and makes that claim concrete: two spans at the same offset can differ by a full layer. The Scope section relies on it to state where the bound goes vacuous. It applies the main claim without competing with it, and it is short.
- **Scope and practical consequence.** These set the boundary condition (lossless short sources) and state what the claim changes in practice (decide provenance quality at ingest). Both strengthen the claim.
- **Open Questions.** The two questions, about transcript grain and about fidelity versus usefulness, are the kind of side ideas this gate would otherwise flag. They are already demoted to open questions, which is the correct destination.
- **Evidence footer.** The ADR 046 audit figures support the claim that naive `verbatim` marking fails.
