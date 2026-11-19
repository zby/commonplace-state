---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/synthesis
launch: 25ef1722003e4998b5fd5a9c88bec194
completed-at: '2026-11-16T17:43:48Z'
findings:
- scope: passage
  quotes:
  - So use of a claim inside the theory can be a test, and often it is not.
  reason: The could-have-failed condition is half of the note's core claim, yet the
    reader meets it three times in three places (the §82 sentence, this paragraph,
    and 'unless the help was a test it could have failed' in the next section), so
    no single spot reads as its authoritative statement; a revision could state the
    condition once in 'Fit is not an independent test', fold in the one new contrast
    ('not where the evidence was produced'), and let the later section apply it without
    restating it.
- scope: passage
  quotes:
  - When a well-tested new claim contradicts the working theory, logic says only that
    the claims cannot all be kept.
  reason: The closing section introduces a second mechanism (contradiction underdetermines
    which claim to give up) whose role in the note is not stated, so the reader cannot
    tell whether it is a consequence of the three-standing separation or a separate
    claim; a revision could either make its link explicit (a good test record does
    not decide what the theory keeps, so repair is a fit decision) and compress it
    into 'The two kinds of evidence inform each other', or move it to its own note.
- scope: passage
  quotes:
  - This note uses "test record" where it earlier used "warrant".
  reason: All four checks flag this revision-history paragraph, and it sits exactly
    at the join between the three-question frame and the first argued section, where
    it points the reader at a version they never saw; a revision could delete it,
    or keep only a short clause in the test-record bullet if readers arriving from
    links that still say 'warrant' need a bridge.
contract: report
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/synthesis/artifact/reviews/d7566694c3cf19e8e46e5e1c/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/synthesis/artifact/reviews/d7566694c3cf19e8e46e5e1c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/synthesis/calls/launches/25ef1722003e4998b5fd5a9c88bec194/outputs/review.md
raw-output-sha256: 2f86d8bc06901024ce849341595799cac70b33ef920e2dd90342631b491504aa
---

# Simplification synthesis: A claim's test record does not determine its fit in a working theory

The gates agree that the note's structure mostly serves its claim: a three-question frame, then one section per separation, then interaction, contradiction and scope. The opportunities below are about where the second half of the core claim lives, the role of the last argued section, and one paragraph that interrupts the frame.

## Opportunities

### 1. State the could-have-failed condition once

- Location: "Fit is not an independent test", from "It adds to the claim's test record only where the agreement was an outcome the claim could have failed" through "not where the evidence was produced"; and in "The two kinds of evidence inform each other", "unless the help was a test it could have failed".
- Combines: marginal-value-redundancy (the "So use of a claim…" paragraph); the core-claim-obscured statement that this condition is half of the core claim.
- Preserve or decide: Preserve the contrast "not where the evidence was produced", which says that evidence from inside the theory is not disqualified merely because of where it was produced. The author must decide whether section 4's slogan "This claim helped the system…" keeps its condition as a decision rule, or refers back to the condition. One possible resolution: end the §82 sentence with "…could have failed, wherever the evidence was produced", and drop the following paragraph.

### 2. Settle the role of the contradiction section

- Location: "A contradiction does not say which claim to give up" (whole section).
- Combines: branch-bloat (contradiction section, INFO).
- Preserve or decide: The author must choose between two roles. (a) The section is a consequence of the note's claim: when a test record conflicts with the theory, the record does not decide the repair, and fit enters the decision. Then state that link and consider folding the section into the interaction section. (b) It is a separate claim about underdetermined repair, which needs its own grounding. Then rehome it and leave a link. Under either choice, keep the final sentence's point that repair weighs both test records and fit. The synthesis does not choose, because the artifact supports both readings.

### 3. Remove the terminology-history interruption

- Location: the paragraph after the three bullets, "This note uses \"test record\" where it earlier used \"warrant\"…".
- Combines: core-claim-obscured, branch-bloat, detail-overhang, marginal-value-redundancy (all on the same paragraph).
- Preserve or decide: The author must decide whether incoming links or neighbouring notes still use "warrant" in this sense. If so, keep a bridge clause in the test-record bullet, for example "(sometimes called warrant, a word that blurs truth and support)". This is one possible wording. Otherwise, delete the paragraph and record the change of term in commit history.
