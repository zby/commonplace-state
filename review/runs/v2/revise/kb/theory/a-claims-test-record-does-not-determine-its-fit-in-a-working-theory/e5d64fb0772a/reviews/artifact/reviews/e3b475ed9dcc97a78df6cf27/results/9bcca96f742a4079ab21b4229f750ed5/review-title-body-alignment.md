---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Three things can be asked about a claim in it, and no answer to one settles another.
  reason: 'Scope drift: the H1 states one direction of one separation (test record
    does not determine fit), but the body''s governing claim is that truth, test record
    and fit are three separate standings, none settling another. Two of the five body
    sections (''A test record is not truth'' and ''Fit is not an independent test'')
    argue separations the title does not name. A further section covers how a contradiction
    is resolved by comparing test records and fit. The title is narrower than what
    the body establishes.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 50f5c46b542846c47e97e06e2527d83c13ca5629500e175f3f17b4cca1e2ea61
criterion-sha256: 83397e71fa79e7650e9da8e5e021ce5155fc7e5dc6bd22a80e77e2590f809e91
target-sha256: e5d64fb0772a1c003b89bd45c9634d219a14732a921ba2404ae7da03c0b078bf
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/e3b475ed9dcc97a78df6cf27/inputs/target/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/artifact/reviews/e3b475ed9dcc97a78df6cf27/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews
launch: 9bcca96f742a4079ab21b4229f750ed5
completed-at: '2026-11-16T17:43:00Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-test-record-does-not-determine-its-fit-in-a-working-theory/e5d64fb0772a/reviews/calls/launches/9bcca96f742a4079ab21b4229f750ed5/outputs/review-title-body-alignment.md
raw-output-sha256: 221fec7d4957c03238537328ce8ff9499f3b4f03b10caf3a615f65dcdae669da
format: 2
---

# Review

## Summary

The body supports the title, but the title covers only part of what the body establishes.

## What the body now establishes

The opening sets up three questions about a claim in a working theory: is it true, what is its test record, does it fit. It then states that no answer settles another. The body argues each separation in turn:

- A test record is not truth: survival is dated corroboration, not a guarantee.
- A good test record does not make a claim fit. This section is the one the title names.
- Fit is not an independent test: agreement with the theory adds to the test record only where the claim could have failed.

It closes with how the two kinds of evidence inform each other without substituting for each other, and how a contradiction is resolved by comparing test records and fit.

The description already states the broader claim ("Three standings of a claim are separate..."). The H1 states only the test-record-to-fit direction. A reader linking to the note by its title would expect a single-direction argument. They would not expect the three-way distinction or the condition under which fit counts as a test, which the body treats as central.

## Correction

A title that matches the body would name the three standings, or at least both directions between test record and fit. One example is "A claim's truth, test record and fit in a working theory are separate standings". Alternatively, the note could narrow its body to the test-record-to-fit separation and move the other separations elsewhere. The first option matches the body as it stands.
