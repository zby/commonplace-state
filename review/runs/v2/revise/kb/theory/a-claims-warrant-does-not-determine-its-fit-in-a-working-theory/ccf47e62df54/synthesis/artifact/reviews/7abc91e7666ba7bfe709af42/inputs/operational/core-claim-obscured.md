---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
  against kb/instructions/compression-bundle/core-claim-obscured.md
note: kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
note-sha256: 971c8f5432f48a0220ce73b0af03ebf07d41624a648304f63b01ede1bf00a723
criterion: kb/instructions/compression-bundle/core-claim-obscured.md
criterion-sha256: a2fc5e1fd3f2f8b89cd19437e27f066e633e69db26084950ba25e5bebdd150a5
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews
launch: 5d2730e53830400993c86807621fe1b7
completed-at: '2026-11-16T11:28:51Z'
findings:
- scope: passage
  quotes:
  - The distinction also changes how contradiction should be interpreted.
  reason: 'This paragraph sits inside the opening argument but adds two further claims:
    contradiction need not be resolved by rejecting the new claim, and fit is relational.
    Both serve the core claim, but placing them before the section that states the
    core rule most crisply ("The prohibition is substitution") delays that restatement.
    The claim stays findable. The simplest repair is to move this paragraph after
    the substitution section, or to cut it to one sentence presented as a consequence
    of the core claim.'
  level: info
contract: verdict
target-sha256: ccf47e62df54def14a7c62b61ea4adebf32d2e5357a1f6b868651d162afa1092
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/cb93f2f7cf4d906273c4beda/inputs/target/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/artifact/reviews/cb93f2f7cf4d906273c4beda/observation.json
contract-sha256: 51160927a1a6a1ab75b5816a18aae4fb5a75347eedf7c08240605699f9cd90ec
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-claims-warrant-does-not-determine-its-fit-in-a-working-theory/ccf47e62df54/reviews/calls/launches/5d2730e53830400993c86807621fe1b7/outputs/review.md
raw-output-sha256: 2b7b09c22c47d1a68c68f335dd62f054d126743226e177ccae5034c484ec3b32
---

# Review

## Summary

Core claim in one sentence: whether a claim is independently warranted and whether it fits a working theory are separate evaluations, and evidence for one does not settle the other. The evaluations may exchange evidence, but neither may substitute for the other.

The note makes this prominent. The title states it. The first paragraph ends with "Evidence for one question does not settle the other." The next two paragraphs cover each direction of the claim in turn: warranted but poorly fitting, then fitting but unwarranted. The section "The evaluations can inform but not substitute for each other" sharpens the claim into an explicit rule. The Scope list stays subordinate and limits the claim's terms without competing with it.

The only shape issue is minor. The contradiction and relational-fit paragraph comes before the clearest wording of the rule, so the opening section ends on a secondary point. That makes the core claim slightly less memorable, but it does not hide it. The finding recommends moving or compressing that paragraph. The finding is information only, so the outcome remains pass.
