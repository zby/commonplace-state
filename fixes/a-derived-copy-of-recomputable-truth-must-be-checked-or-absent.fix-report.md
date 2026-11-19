# Fix report: a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md

Source review: job 6573, pair `sentence/clause-packing` (outcome `warn`, partition `claude-opus-4.8`, 2026-07-17). Result file: `kb/reports/review-jobs/review-job-6573/pair-1-clause-packing.md`.

| Finding | Strategy | Fix | Status |
|---|---|---|---|
| WARN: line-20 framing sentence (~90 words, four ideas: dependence, derived/abstracted distinction, staleness machinery, two-branch repair) | `sentence-split` (new strategy — not yet in taxonomy) | Split into three sentences along the reviewer's suggested seams: dependence + distinction; the three-part machinery; the regime-following repair. One parenthetical trimmed ("recoverable by re-derivation" — redundant with "derived copy" and restated by the repair sentence). No claim changed. | fixed |
| WARN: "What enforcement buys" sentence (~50 words, four moves) | `sentence-split` | Split after the third-class placement; mechanism and check-time contrast carried by a second sentence ("Here a machine watches…"). No claim changed. | fixed |
| INFO: "That machinery stops at *review*…" (borderline, cohesive) | — | Left as is per the reviewer's own judgment (single thesis). | deferred (not actionable) |

New-pattern note: `sentence-split` — review warning `sentence/clause-packing`, fix = split at idea boundaries, trim redundancy only where a clause restates an adjacent clause; never drop a distinct idea. Propose for the taxonomy if it recurs (this is instance 1).
