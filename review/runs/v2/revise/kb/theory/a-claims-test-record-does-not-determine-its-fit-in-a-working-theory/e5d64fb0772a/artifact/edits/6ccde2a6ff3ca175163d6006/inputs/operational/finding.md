---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/semantic/completeness-boundary-cases.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 38f8db3bc86fa1eaa16a1a1fa1652779f9371be9baa68043c721172d2bcd8543
criterion: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
criterion-sha256: b46ca399a83da384b7f5217f86945cff08f0ae3c084711ab6fec66a558192323
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 5fe4f6eb46b546179c20385ffc39bbac
completed-at: '2026-11-16T17:39:09Z'
findings:
- scope: passage
  quotes:
  - A claim that has survived every test so far is still a conjecture.
  reason: The opening explicitly admits formal claims, whose test is 'a derivation'.
    A formal claim that has a valid derivation from accepted premises has its truth,
    relative to those premises, established by that test. So the boundary case of
    a derived formal claim falls outside the section's rule that a test record is
    never truth and every surviving claim is still a conjecture. The opening's universal-claim
    qualifier ('for a universal claim it is never established') does not cover the
    case either, because a theorem can be universal and still be proved. Either the
    three-question framework or the 'test record is not truth' section does not hold
    across the full range of claim kinds the note lists.
  level: warn
- scope: passage
  quotes:
  - A test is independent when its outcome could have gone against the claim and does
    not presuppose the working theory.
  reason: 'Boundary case between the categories: a use of the claim inside the system
    that could have gone against it but relies on neighbouring retained claims or
    the current implementation. It meets the first condition and fails the second.
    The ''Fit is not an independent test'' section seems to count such a use as a
    test, but the definition excludes it. Classification is possible only by choosing
    which condition governs, so the case is strained rather than clearly outside.'
  level: info
contract: verdict
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/7698ffaf7df326ac99d0e460/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/7698ffaf7df326ac99d0e460/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/5fe4f6eb46b546179c20385ffc39bbac/outputs/review-completeness-boundary-cases.md
raw-output-sha256: 9cbb035216da7eec1da785b42cfab37baf4e5d79303a176e64342b84ab1bbccb
---

# Review

## Summary

The note's framework is three questions about a claim (truth, test record, fit), together with a definition of an independent test and a four-part definition of fit. The note does not claim that the three questions exhaust what can be asked, so the test concerns whether each listed category handles its own boundary cases.

Boundary cases tried:

- **Simplest instance:** a new claim with no tests. It has an empty test record, an open truth value and a fit that can be assessed. It maps cleanly.
- **Extreme instance:** a formal claim with a completed derivation. The note lists derivation as the test for formal claims, but then says every claim that survives its tests is still a conjecture. A proved theorem is not a conjecture relative to its premises, so the case breaks the "test record is not truth" section (WARN).
- **Between categories:** a use of the claim inside the system that could have failed but that presupposes other parts of the working theory. The two conditions in the independence definition pull in opposite directions (INFO).
- **Adjacent concept:** a methodological convention, such as a type definition, kept in the working theory. "Is it true?" arguably does not apply to it. However, the note's Scope already places objectives and commitments outside what tests settle, so this case is strained but can be handled. It is not raised as a finding.
- **Fit and contradiction:** a well-tested claim that contradicts the retained claims fails the "agrees with the other retained claims" condition of fit. The contradiction section handles this explicitly by treating the repair as a decision, so the case maps.

The framework is not overweighted for its role. A repair would be to scope the claim kinds or to clarify the boundary, not to add another question.
