---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/structural/general-before-specific.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/structural/general-before-specific.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/7936332c4bacdee4218fb9b7/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/7936332c4bacdee4218fb9b7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 158ea5fee8014c809a5e1c55575df95c
completed-at: '2026-11-16T22:37:23Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/158ea5fee8014c809a5e1c55575df95c/outputs/review-general-before-specific.md
raw-output-sha256: ab4421be84ec6acf9781b0429c090f45afe235025b7b7bddef4be681b133e068
format: 2
---

# Review

## Summary

In every pair of adjacent sections, the general section comes before the specific one, or neither section states a rule the other exemplifies.

- The unheaded opening states the general rule: two independent bounds, and atomicity is relative to a check. It also says the note will work this out for the grounding check.
- "Placing the bound on the artifact rather than the review" compares two general placements of the bound. It comes before "Mechanism: for the grounding check, the unit is the unquoted source", which applies the rule to one check. The order runs general to specific.
- "The two bounds come apart in the corpus" is a specific case: corpus counts and one experiment. It exemplifies the independence claim, which the opening already stated. The next section, "What kind of number a step size is", does not state a rule that the corpus section exemplifies. Instead, it asks a further question about N, so the pair is not inverted.
- "Scope" and "Open Questions" are closing sections that qualify the note. They come after all the substantive sections.

No pair puts a specific case before the general rule it exemplifies.
