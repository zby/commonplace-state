---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - What decides is whether the use could have gone against the claim, not where the
    evidence was produced.
  reason: 'The note defines an independent test by two conditions: the outcome ''could
    have gone against the claim'' and it ''does not presuppose the working theory''.
    This sentence names only the first condition as what decides whether use inside
    the theory counts as a test. Use inside the theory is exactly where the second
    condition is at risk: the previous section says fit can come from the implementation,
    vocabulary or neighbouring claims already assuming the claim. The framing leaves
    out part of the mechanism the note itself defined. A reader could treat any use
    that could have failed as an independent test, even when the outcome is judged
    through the theory''s own assumptions. Name both conditions, or say that the second
    is what ''not where the evidence was produced'' must still respect.'
  level: warn
- scope: passage
  quotes:
  - It adds to the claim's test record only where the agreement was an outcome the
    claim could have failed
  reason: The same narrowing on a smaller scale. The sentence before it says such
    agreement 'measures the theory's own assumptions', which is the presupposition
    condition. The condition this sentence states is only 'could have failed'. The
    two sentences together supply both halves, so the reader is less likely to be
    misled here than in the closing sentence of the section.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/c49bd418c5a329577647ce3e/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/c49bd418c5a329577647ce3e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 1fcb6fe423b6419ba77c67a498edd3eb
completed-at: '2026-11-16T17:38:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/1fcb6fe423b6419ba77c67a498edd3eb/outputs/review-framing-mismatch.md
raw-output-sha256: 3c009fe537e74366f3299902df328461791b973dfd28d85159913af8ef24c92e
format: 2
---

# Review

## Summary

Most mechanism sentences are framed at the right level of generality. The fit definition, the account of why a well-tested claim can fit poorly and the contradiction-repair section each name a mechanism that matches what they claim. None restricts its claim to a narrower domain than the mechanism covers.

The one framing problem is in "Fit is not an independent test". The note's opening defines independence by two conditions: the test could have failed, and it does not presuppose the working theory. The section's conclusion then reduces the deciding question to the first condition alone. Use of a claim inside the theory is the case where the second condition matters most. Framing the decision by possible failure alone therefore leaves out cases the note's own mechanism treats as non-independent.
