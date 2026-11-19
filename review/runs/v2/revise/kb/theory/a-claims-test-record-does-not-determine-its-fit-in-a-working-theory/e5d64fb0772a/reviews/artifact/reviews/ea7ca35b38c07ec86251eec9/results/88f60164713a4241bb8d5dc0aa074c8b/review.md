---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - So use of a claim inside the theory can be a test, and often it is not. What decides
    is whether the use could have gone against the claim, not where the evidence was
    produced.
  reason: 'UNSUPPORTED — The note defines an independent test with two conditions:
    its outcome ''could have gone against the claim and does not presuppose the working
    theory''. This conclusion keeps only the first condition and says the place of
    production does not matter. Use inside the theory is the clearest case of evidence
    that presupposes the working theory, so the definition seems to exclude it while
    this sentence admits it. The note does not say whether the second condition is
    dropped, is implied by the first, or fails to apply to in-theory use. As written,
    the section''s conclusion and the opening definition give different answers for
    a use that could have failed but relies on the theory.'
- scope: passage
  quotes:
  - A claim that repeatedly fails to predict, to guide recovery or to transfer has
    not been refuted by that alone, but it has earned a new independent test.
  reason: THIN — The note does not show why repeated failure to predict is not itself
    a test result. If the claim made a prediction that turned out wrong, that outcome
    could have gone against the claim, which meets the note's own condition for a
    test. The sentence needs to separate failing to yield a useful prediction (a fit
    problem) from yielding a wrong one (a possible refutation, subject to the contradiction
    section's caveat about which claim to give up). It also asserts without reason
    that the failure 'earns' a new test, rather than, for example, a loss of fit and
    removal.
- scope: passage
  quotes:
  - 'A new test result can likewise force a change of fit: a claim that survives a
    severe test may require restructuring the working theory, even when the restructuring
    makes the theory less convenient.'
  reason: THIN — The mechanism is missing. Surviving a test is said to force restructuring,
    but by the note's own fit section a well-tested claim can simply be irrelevant
    or redundant and be left out. The implied route is that the surviving claim contradicts
    retained claims, which the later contradiction section treats. That section says
    a contradiction leaves the repair to a decision, so 'force' and 'require' are
    stronger than the note supports.
- scope: passage
  quotes:
  - 'It adds to the claim''s test record only where the agreement was an outcome the
    claim could have failed: evidence corroborates only when it reports a sincere
    attempt to refute (§82 of the same work).'
  reason: THIN — The colon presents Popper's sincerity condition as the ground for
    the could-have-failed condition, but the two differ. Sincerity is about the tester's
    attempt; the linked passage says the requirement 'cannot be formalized'. Could-have-failed
    is about the outcome space. An agreement in normal use can be an outcome that
    could have failed without being a sincere attempt to refute. The citation supports
    a stricter condition than the one the note states, so the note's criterion is
    adapted from Popper's, not given by it, and the inference does not say so.
- scope: passage
  quotes:
  - Three things can be asked about a claim in it, and no answer to one settles another.
  reason: 'HOLDS — Under skeptical reading the joint might clash with the ''inform
    each other'' section and the Scope bullet on correlation. The note heads off that
    clash: it says separate, not statistically independent, and it keeps ''inform''
    (sending a claim for testing or forcing reconsideration) distinct from ''settle''.
    The three subsections each give a concrete case where one answer leaves another
    open. One residual gap: the test record counts only survived tests, so the note
    does not say how a failed test bears on truth. Its contradiction section''s point
    about which claim to give up covers this in part.'
outcome: report
description: Retained report review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/ea7ca35b38c07ec86251eec9/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/ea7ca35b38c07ec86251eec9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 88f60164713a4241bb8d5dc0aa074c8b
completed-at: '2026-11-16T17:39:15Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/88f60164713a4241bb8d5dc0aa074c8b/outputs/review.md
raw-output-sha256: ff82e58ef9743351b8ccb6f8deaea662be26e074187dd3af5c5518452ca78776
format: 2
---

# Friction check: A claim's test record does not determine its fit in a working theory

**Central claim (one sentence):** Truth, test record and fit are three separate standings of a claim in a working theory, so none settles another, and agreement with the theory counts toward the test record only where the claim could have failed.

## Filter
**Filter:** SURVIVES

The note wants three things together: the standings are separate, they inform each other, and they are correlated. These can coexist because the note separates "settles" from "informs" and from "is statistically correlated with". Concretization does produce one internal tension, shown as the first finding: the definition of an independent test and the "what decides" rule disagree about evidence that presupposes the working theory. That is a defect in one joint, not a split of the central claim. Either condition could be chosen and the claim would still state one consistent thing.

## Thinnest joints

The definition-versus-rule mismatch ranks first because the note's thesis about fit and tests depends on the definition of a test, and the note states that definition two incompatible ways. The next two rank below it because each is a transition in "The two kinds of evidence inform each other". There the note asserts a directional effect (earns a test; forces restructuring) without its mechanism. Each also partly conflicts with what the note says elsewhere about prediction failures and contradiction repair. The Popper citation ranks fourth: the source supports the direction of the point, but the note states a weaker condition than the source's without marking the adaptation. The opening separation claim holds, because the Scope section and the "inform" versus "settle" distinction carry it.

## For the human
Look first at whether an independent test must "not presuppose the working theory". Keep that condition and revise the "What decides" sentence, or drop it from the definition, because the two disagree about evidence from inside the theory.
