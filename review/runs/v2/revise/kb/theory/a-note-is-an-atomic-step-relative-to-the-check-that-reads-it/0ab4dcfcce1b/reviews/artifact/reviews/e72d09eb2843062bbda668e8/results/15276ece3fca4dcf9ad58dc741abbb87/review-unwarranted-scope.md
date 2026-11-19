---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - A knowledge base written and reviewed by agents bounds note size twice
  reason: The opening invites reliance over any agent-written and agent-reviewed knowledge
    base. The support exercised is Commonplace's own grounding check, validator and
    corpus. The relativity part has a stated transfer relation (the oracle-domain
    rule), and Scope says the corpus evidence is local. The claim that such knowledge
    bases in general apply a checking bound to note size is a supporting framing claim
    that is broader than its support.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/semantic/unwarranted-scope.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/semantic/unwarranted-scope.md
note-sha256: 93d1bb6d6123b6874693cda7fb7f196669f4741d3d823e54b124df0bb4ef25af
criterion-sha256: d4e59ae95b01188e37f82dcf05610e18712daa7bf913af37ce3f115ed14b0fc9
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/e72d09eb2843062bbda668e8/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/e72d09eb2843062bbda668e8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 15276ece3fca4dcf9ad58dc741abbb87
completed-at: '2026-11-16T22:40:10Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/15276ece3fca4dcf9ad58dc741abbb87/outputs/review-unwarranted-scope.md
raw-output-sha256: a079791752b669d07f0320ea4caa3c582d4b1bf84ddfd520fd467162d9a823a1
format: 2
---

# Review

The central claim is that a note is atomic relative to the check that reads it, and that for Commonplace's grounding check the unit is the unquoted source. Its scope has two parts:

- **Relativity.** The general part is derived from the linked rule that warranted autonomy is bounded by oracle domain. That rule is an articulated transfer relation covering any check.
- **Unit.** The specific part is explicitly limited to the grounding check and to systems with a mechanically validated verbatim quote. The note says the unit would have to be derived again for any other check.

The empirical support consists of the corpus counts and the paired experiment. Scope bounds it to "one knowledge base at one time", and the note claims only that the bounds are independent there. The note does not decide N or a validator rule. The claimed scope therefore matches the exercised domain, or else is covered by a stated transfer relation or explicit scoping. Only the opening's general framing about agent-reviewed knowledge bases goes further than its support, and that framing is not the central claim.
