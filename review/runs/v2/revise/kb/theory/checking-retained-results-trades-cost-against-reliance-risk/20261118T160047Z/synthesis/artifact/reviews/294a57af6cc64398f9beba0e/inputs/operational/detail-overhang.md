---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/compression-bundle/detail-overhang.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/compression-bundle/detail-overhang.md
criterion-sha256: e38e03f9aa6d4ecefdd4674ce0acc478dab89aa53e86ceb02e0438670fac7187
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 24602c8d4cff490785feb5984ffaeb41
completed-at: '2026-11-18T16:02:59Z'
findings:
- scope: passage
  quotes:
  - The suppression mechanism is conditional. It makes no claim about how often consumers
    stop on a copy or how often the fallback search finds more.
  reason: This Scope bullet restates the condition already attached to the suppression
    mechanism in the opening section ('This requires that the consumer actually stops
    and that the suppressed search would find more task-relevant material'). The added
    prevalence disclaimer is useful, but the restated condition could shrink to a
    clause. It is probably slightly long rather than overgrown, because Scope sections
    conventionally collect limits in one place.
  level: info
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/cb234d646d8d2a42f7f45355/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/cb234d646d8d2a42f7f45355/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/24602c8d4cff490785feb5984ffaeb41/outputs/review.md
raw-output-sha256: 6fe051161372daed232f5e84f1f1f2cf23bade2289f8d0210a47cee80c51860f
---

# Review

The note's details are mostly proportional to their argumentative jobs. The opening section states the saving, the risk and its condition in three short paragraphs. Each worked example (the completeness mark and the connect report) runs to about two paragraphs. Each example carries premises the general claim depends on. For the mark, these are a defined rule, named inputs, reactive enforcement and the boundary with semantic review. For the connect report, they are judgment-dependent assessment and broad dependencies. The four-item list of conditions for a mechanical check is terse, and the note uses it immediately to say which conditions the mark's contract supplies.

Two places look like overhang but are not:

- In the completeness-mark section, the parentheticals "one-hop reach over tagged artifacts" and "the participating collections and nothing else" instantiate conditions 1–3 of the later list. Without them, the claim that the mark's contract supplies those conditions would rest on nothing.
- In the connect-report section, the aside about mechanically checkable properties (link resolution, required sections) heads off a likely objection in one sentence. Its length matches its job.

The only candidate for compression is a small overlap in caveats. The opening section states the conditions under which suppression occurs, and the Scope section repeats them before adding the prevalence disclaimer. This is recorded as INFO, not WARN, because the duplication is a single sentence and Scope sections are expected to gather limits.
