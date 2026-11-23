---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '- [Bounded-context orchestration model](./bounded-context-orchestration-model.md)
    — extends: the two-view split applies bounded-call scheduling to the trade-off
    between execution focus and global prioritization'
  - '- [Decomposition heuristics for bounded-context scheduling](./decomposition-heuristics-for-bounded-context-scheduling.md)
    — extends: carries clean-frame isolation and interface preservation from within-task
    scheduling to cross-task triage and blocker compression'
  - '- [Unattended work needs the functions that interaction supplied](./unattended-work-needs-the-functions-that-interaction-supplied.md)
    — extends: identifies local context isolation as one structural reason stopping
    and redirection fail when interactive oversight is removed'
  reason: These three footer links reverse the asymmetric `extends` label defined
    in `kb/theory/COLLECTION.md`, whose reader-need at the source is 'wants the argument
    developed further' (the target develops this note's argument). All three targets
    are upstream notes that this note builds on or instantiates, and each context
    phrase describes what this note adds rather than what the target develops beyond
    it; `unattended-work-needs-the-functions-that-interaction-supplied.md` already
    carries `extends` in the forward direction toward this note. Re-label from this
    note's reader need (for example `grounds` or `exemplifies`) or drop any edge that
    only mirrors an upstream `extends`.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/theory/COLLECTION.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/theory/COLLECTION.md
note-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
criterion-sha256: 95ad0d6ce3828b25282f7610268c4e1aca006fa34526bc2b4e4056f3e271cccd
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/3de7643799364a4a90192b97b70d875e/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/122cd0ff7216edcbc893ee10/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: 3de7643799364a4a90192b97b70d875e
completed-at: '2026-11-19T13:45:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/3de7643799364a4a90192b97b70d875e/outputs/review.md
raw-output-sha256: 4156e32144677eee83c835c1294f1584690b4652ca5cbca8f4082c82bb5f3c13
format: 2
---

# Review

The note conforms overall to `kb/theory/COLLECTION.md`, with one unmet outbound-linking convention.

## Placement, scope, and claim formulation

Placement in `kb/theory/` is sound. After scoping the motivating practitioner account and the three Commonplace design illustrations (`traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md`, ADR 138, and `unresolved-frontier`), a substantive design-space claim remains and stands independently of any single cited description. The note states its boundaries in `## Scope`, names genuine gaps in `## Open Questions`, declares universal claim modality with explicit boundary conditions and refuters, carries `title-as-claim`, and keeps its body composable around one trade-off.

## Source grounding and outbound links

Source grounding meets the collection contract: the note cites one tracked source (`nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md`), hosts it in the body rather than footer-only, repeats the `(..., verbatim)` citation after each of the four quotations matching uniquely in the ingest's `## Quotes` section, and treats the account strictly as origin (`abstracted-from`), not corroboration. No links target `kb/work/` or local snapshots.

The remaining footer links (`grounds`, `contrasts`, `mechanism`, `enables`, `defined-in`, `abstracted-from`) match their authorized destinations and reader-need directionality. Only the three `extends` entries in `Relevant Notes` reverse that label's asymmetric direction, as recorded in the finding above.
