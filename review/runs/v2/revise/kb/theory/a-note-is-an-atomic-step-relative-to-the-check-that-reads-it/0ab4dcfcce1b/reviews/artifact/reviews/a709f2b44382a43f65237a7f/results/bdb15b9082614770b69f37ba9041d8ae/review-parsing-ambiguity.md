---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the audit the bound buys is of the step the validator did not do, not of the one
    it cannot
  reason: 'The elliptical ''the one it cannot'' leaves the reader to reconstruct which
    step each phrase names. The validator neither performs the support judgment nor
    checks the qualifying context, so ''did not do'' and ''cannot'' can each be read
    as naming either step. On a plausible reading, the audit covers the context check,
    which is the opposite of the intended meaning. Name the steps: ''the audit covers
    the support judgment, not the context check that only the source can settle''.'
  level: warn
- scope: passage
  quotes:
  - now archived, identified when it concluded
  reason: Garden path. After 'the hazard the review-side proposal *...*,' the reader
    meets 'now archived, identified' and can take both participles as adjectives on
    the proposal ('archived and identified'). The reduced relative clause ('the hazard
    that the proposal identified') is recovered only on rereading. Make the relative
    pronoun explicit or restructure.
  level: warn
- scope: passage
  quotes:
  - which is the behaviour an artifact-side bound depends on
  reason: Modifier attachment. 'which' can attach to the reviewer honouring its cap,
    to the notes putting their support beyond the cap, or to both. The artifact-side
    bound plausibly depends on reviewers honouring a limit. It cannot depend on notes
    putting support out of reach. Name the antecedent, e.g. 'a reviewer that honours
    its cap is the behaviour ...'.
  level: warn
- scope: passage
  quotes:
  - one was missing retained support for
  reason: '''one was missing retained support'' can first be read as the finding itself
    lacking support (progressive ''was missing''), not as the finding''s content.
    Context resolves it quickly, but ''one found missing retained support'' would
    avoid the momentary misreading.'
  level: info
- scope: passage
  quotes:
  - each grounded in one quoted passage, is one step for the grounding check
  reason: The plural subject 'two independent claims' takes 'is'. The intended reading
    is a note holding two such claims, but the agreement mismatch makes the reader
    look for a different singular subject. Write 'a note holding two independent claims,
    each grounded ..., is one step ...'.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
contract: verdict
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
note-sha256: 9f4b59c685bd7691939707105b2c28566eba9bd82afa0d514c7729a24430f305
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/a709f2b44382a43f65237a7f/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/artifact/reviews/a709f2b44382a43f65237a7f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews
launch: bdb15b9082614770b69f37ba9041d8ae
completed-at: '2026-11-16T22:39:20Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/reviews/calls/launches/bdb15b9082614770b69f37ba9041d8ae/outputs/review-parsing-ambiguity.md
raw-output-sha256: 6ad2ed34d9f2f52c3152549db9c574dbb130cef8edc1334f98894736975a7973
format: 2
---

# Review

The note mostly avoids syntactic ambiguity. Negation scope is handled carefully in sentences such as "Its cost is not links, and not bytes" and "N is not the point at which ...". Pronouns such as "them" in "is not one of them" have clear antecedents.

Three places allow a plausible unintended reading. The first is the elliptical contrast at the end of the auditability paragraph, which can reverse which step the audit covers. The second is a reduced relative clause after an italic title, which reads first as a pair of participles. The third is a "which" whose antecedent can be either half of the preceding coordination, and one of those readings does not make sense. Two smaller cases are recorded as info.
