---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/composition-friction-gate.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
criterion: kb/instructions/composition-friction-gate.md
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: 1f4f59ca76dd47a191c580d2658e83fc
completed-at: '2026-11-16T22:39:46Z'
findings:
- scope: passage
  quotes:
  - Both are absences of a retained passage, and an absence of that kind is a validator's
    result rather than a reviewer's finding.
  reason: UNSUPPORTED — The verbatim-quote validator the note describes (ADR 046)
    checks quotes that exist against their source; it does not detect an attribution
    that carries no quote. An absent retained passage becomes a validator result only
    under a further rule requiring a quote for every attributed detail, which the
    note neither states nor shows exists. The next sentence ('Had the details been
    quoted, either the quote would match or the note would have failed validation')
    assumes the quoting happened, which is the step in question. The reinterpretation
    of two of the four experimental findings rests on this joint.
- scope: passage
  quotes:
  - N is a convention, chosen so that a second checker — including a person — can
    redo the step.
  reason: 'UNSUPPORTED — The conclusion is reached by eliminating two of ''three candidates'',
    but the note does not show that the three exhaust the options; cost or latency
    budgets, for example, are not considered. The auditability rationale is a difference
    of degree, not kind: a verdict on three sources and six passages also costs about
    as much to audit as to produce, and a verdict on fourteen artifacts can still
    be redone, despite the claim that ''an unbounded one cannot be redone''. The final
    warrant, the measurement that LLM verdicts disagree with themselves, is unlinked
    and unquantified. That instability argues as much for repeated review as for small
    steps.'
- scope: passage
  quotes:
  - An artifact-side bound does not have that failure mode, because a conforming artifact
    fits by construction
  reason: THIN — The comparison sets an artifact-side bound held by a validator against
    a review-side budget that 'returns a pass' when it stops reading. It omits a review-side
    rule that withholds a pass or fails the review when the budget binds, which would
    be equally loud. The silent failure therefore belongs to the pass-on-exhaustion
    policy, not to review-side placement as such. The artifact-side validator is also
    hypothetical; the Scope section says the note 'does not decide N, a validator
    rule that would enforce it'.
- scope: passage
  quotes:
  - Two limits follow, and both are prices already paid elsewhere in the system.
  reason: THIN — The paragraph names where the second limit is handled, the '(snapshot
    required)' marking. It names no mechanism that pays for the first limit, occurrence
    versus representativeness; it only says a suspicious reader must open the source.
    That residual cost is reviewer-side and unbounded. It weakens the earlier claim
    that the remaining judgment 'requires opening nothing', which the auditability
    argument later depends on.
- scope: passage
  quotes:
  - They are not atomic steps for the grounding check, because checking one means
    opening six to nine artifacts and finding the claimed support in each.
  reason: 'THIN — The note''s own unit is the unquoted source, so the eight notes
    fail the step only if their six to nine sources are unquoted and the threshold
    N is at most five. The paragraph establishes neither: it counts distinct cited
    sources, not unquoted ones, and N is explicitly left undecided. The demonstration
    that the two bounds ''come apart'' therefore depends on an unstated quoting status
    and an unstated threshold. The corpus is also cited as `kb/notes/`, while the
    note lives in `kb/theory/`, so the count''s current referent is unclear.'
contract: report
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/0ad7878c461e6a4f20e4e24d/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/0ad7878c461e6a4f20e4e24d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/1f4f59ca76dd47a191c580d2658e83fc/outputs/review.md
raw-output-sha256: 96b18c46b996c3721edf0e3a3784d308c3fd36eda5962d2db4c8873ab3bd947c
---

# Friction check: A note is an atomic step relative to the check that reads it

**Central claim (one sentence):** A note's size is bounded both by co-loading and by the check that reads it, so atomicity is check-relative; for Commonplace's grounding check, the unit is the unquoted source, and placing that bound on the artifact rather than the review turns a silent budget failure into a loud validation failure and makes the review auditable.

## Filter
**Filter:** SURVIVES

The properties the claim holds together are two independent bounds, quoting as the remedy for jointly supported claims, and an artifact-side bound with no silent failure. They could conflict, because quoting spends against the co-loading bound. The note names this coupling ("independent as constraints but coupled through this remedy") and states the residual cases: the snapshot route or a split by claim. A second tension sets "requires opening nothing" against the representativeness limit. The note concedes this limit instead of hiding it. The claim keeps one consistent form.

## Thinnest joints

The two `UNSUPPORTED` joints rank highest because each carries a section's conclusion, and the stated reason does not reach that conclusion. The first claims that the validator would have caught findings it is not built to detect. The second reaches N-as-convention by elimination over an unproven set of three, then justifies it by an unlinked measurement. The three `THIN` joints are real but narrower. The loud-versus-silent comparison holds against the review-side policy the note describes, but not against review-side placement in general. The "prices already paid" claim is half-supported. The corpus demonstration is plausible but depends on quoting status and on a threshold the note leaves open. The co-loading bound, the check-relativity framing and the Descartes and Lamport precedents hold. The note explicitly limits the precedents to analogy.

## For the human
Look first at the reading of the paired experiment (lines 131–140). Decide whether a rule requiring quotes for attributed details exists or is being proposed. Without one, the claim that these absences are "a validator's result" has nothing beneath it.
