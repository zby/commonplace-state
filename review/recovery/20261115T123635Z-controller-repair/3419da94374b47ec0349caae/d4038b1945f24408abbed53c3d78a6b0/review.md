---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - It is the general form of "a cache must never be the only copy" — applied not
    only to caches but to every derived copy of recomputable truth.
  reason: 'This closing sentence uses the elevation move ("not only to caches but
    to every derived copy"). It fails the deletion test. The title, description and
    opening paragraph already scope the rule to every derived copy of recomputable
    truth, and the four instances just listed show that it generalizes. The cache
    maxim is the only new element, and it is loose: "never the only copy" is a different
    rule from "checked or absent". Without the sentence, the section ends cleanly
    on the fourth instance and the reader loses nothing.'
  level: warn
outcome: warn
description: Controller-only revalidation of retained worker output; no new judgment
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/sentence/stock-phrases.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 6e2bd9a71d2685b71fc1641640e684574da24f3115f005263a75367c0dc6c29c
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/3419da94374b47ec0349caae/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/3419da94374b47ec0349caae/observation.json
contract-sha256: 5a084df09d1b0de08e2dcd8e2316c8ae5af96860a9ebdfc00fb62dd34597653e
profile:
  harness: claude-code
  launch_model: opus
  effort: medium
  flags:
    allowed-tools: Read,Grep,Glob,Edit(kb/reports/state/review/runs/**),Write(kb/reports/state/review/runs/**)
    disallowed-tools: Bash,NotebookEdit
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T123635Z
launch: d4038b1945f24408abbed53c3d78a6b0
completed-at: '2026-11-15T13:09:37.182037+00:00'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/d4038b1945f24408abbed53c3d78a6b0/outputs/review.md
raw-output-sha256: 01efd5b52075a8368192b7e4dd434a8f618f1785c840f91597140259238e7eb0
format: 2
---

# Review

## Summary

One sentence fails the deletion test. Most of the note's rhetorical sentences carry content specific to the note.

## Assessment

I applied the deletion test to every sentence matching or resembling the criterion's patterns. Apart from the closing sentence recorded as the finding, these candidates were considered and kept:

- **"A bounded, recoverable downside on one side; a silent, unbounded one on the other — that is why hand-maintained-and-trusted is *forbidden* rather than merely risky."** This recaps the asymmetry from the previous paragraph. It is kept because it is the only sentence that moves from that asymmetry to the strength of the rule ("forbidden" rather than "risky"). Without it, the section would not justify its own heading.
- **"This looks like it reopens the regress, but it doesn't:"** This anticipates an objection and then answers it with specific mechanisms: centralization, versioning and amortization. It is substantive, not filler.
- **"Omission is the fallback, not the optimum."** This closely restates the preceding clause ("pay a … cost that enforcement would have avoided"). It is short and does not match a listed pattern, so it is not reported. It is the next candidate if the author tightens the bullet.
- **"The spread is what shows it generalizes:"** and **"Two things change."** These are signposts that introduce lists. Deleting them would make the following lists harder to read, so they pass.

No "It's worth noting", "At its core", "The key insight" or "In other words" constructions appear.
