---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
contract: verdict
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/14d7985adde83e1b09805b0c/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/14d7985adde83e1b09805b0c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 1fcb6fe423b6419ba77c67a498edd3eb
completed-at: '2026-11-16T17:38:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/1fcb6fe423b6419ba77c67a498edd3eb/outputs/review-concept-attribution.md
raw-output-sha256: fa192b332ead1e677ae97ce113eb617b9a13861ffaa235759fd251e2cf66a888
format: 2
---

# Review

## Summary

The note identifies its concepts with concepts from linked sources in three places. All three match their targets.

- **Popper, §84 (truth vs corroboration).** The note says truth is timeless, while corroboration is relative to statements accepted up to a particular time and so carries a date. The linked ingest retains quotes from §84 on "the difference between truth and corroboration" and on corroboration not being a truth value. Its summary describes corroboration as "a dated appraisal ... relative to the basic statements accepted so far". The attribution matches.
- **§82 (sincere attempt to refute).** The note says "evidence corroborates only when it reports a sincere attempt to refute (§82 of the same work)". The ingest retains a §82 starred footnote that requires derived basic statements to be "accepted as the results of sincere attempts to refute the theory". It also retains the matching Appendix *ix passage. The concept matches. The section citation points to a starred footnote, a later layer of the text, rather than the 1934 main text. That does not change the concept.
- **Footer edges.** The two system-use notes cite this note as their premise. Each develops the claim the footer attributes to it: fit evidence from live use is not an independent test, and live use acts as a selection environment without a fixed oracle. The epistemic stance page states the fallibilism the footer names, under which corroboration is a survived attempt at refutation.

Every target resolved.
