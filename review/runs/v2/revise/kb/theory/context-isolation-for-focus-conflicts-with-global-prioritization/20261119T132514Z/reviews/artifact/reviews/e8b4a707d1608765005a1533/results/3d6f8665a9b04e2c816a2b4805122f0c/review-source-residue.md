---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Inside one module or diff, guarding a hypothetical edge case looks prudent when
    system-wide complexity budgets and accepted product tolerances are absent
  reason: This bullet states a general failure mode of isolated agent workers. It
    frames that failure mode only in software terms ('module or diff', 'product tolerances'),
    and nothing marks those terms as an example. The other two manifestations use
    domain-general wording. Writing 'Inside one artifact or change (for example, a
    code module or diff)' would match the bullet to the note's general claim. The
    residue is confined to one illustrative manifestation and does not narrow the
    title claim, so it is a weak signal.
  level: info
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/3d6f8665a9b04e2c816a2b4805122f0c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/artifact/reviews/e8b4a707d1608765005a1533/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews
launch: 3d6f8665a9b04e2c816a2b4805122f0c
completed-at: '2026-11-19T13:26:47Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T132514Z/reviews/calls/launches/3d6f8665a9b04e2c816a2b4805122f0c/outputs/review-source-residue.md
raw-output-sha256: db26a5f891bcc0a43455d89038019a58533aac1950791e5755d651caa2cd0edf
format: 2
---

# Review

## Summary

The title and opening make a general claim about agent systems that work under
bounded context. The note was abstracted from a practitioner account of coding
agents. Most of that origin is handled explicitly:

- The Nostalgebraist and Anthropic quotations, including the babysitting
  imagery, are introduced as a practitioner account and attributed in place.
  The Scope section and the footer mark them as origin, not corroboration.
- The core vocabulary is domain-general: worker, operator, triage, comparison
  set, tolerances, stop record. The Commonplace mechanisms are labeled as "local
  design examples".

The only unmarked coding vocabulary is the over-specification bullet recorded
above. It does not narrow the note's claim.
