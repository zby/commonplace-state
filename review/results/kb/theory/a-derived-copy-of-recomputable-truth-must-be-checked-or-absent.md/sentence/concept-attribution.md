---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/concept-attribution.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 6a33452f49e5477b8099d126092706ac
completed-at: '2026-11-16T22:21:22Z'
findings:
- scope: passage
  quotes:
  - wants the same value left out, since anything the situation determines goes stale
    by drift or ignorance
  - (safe to pin)
  reason: The note identifies its recomputable value with the target's 'situational'
    class and casts the target's 'arbitrary' class as 'safe to pin'. The target defines
    a situational choice as one that task intent and live or actively produced execution
    evidence can distinguish; its 'Search cost and frontloading' section explicitly
    says to frontload a known value that remains valid for the call and only forbids
    freezing a situational value that execution evidence could overturn. A value recomputable
    from a ground-truth source before the call is not situational in that sense. The
    target's arbitrary class is one no evidence selects, which 'need not be fixed'
    unless coordination requires one selection, not a class that is 'safe to pin'.
    The asserted tension between the two notes, and the 'third class between arbitrary
    and situational', therefore rest on a reading the target does not support.
  level: warn
- scope: passage
  quotes:
  - recompute being dear to a model is what makes a checked derived copy worth keeping
    in the first place
  reason: The context phrase attributes to the target the claim that costly model-side
    recomputation is what makes a checked copy worth keeping. The target (now titled
    'LLM recompute cost shifts the store-vs-recompute balance') says expensive model-side
    derivation 'does not by itself justify persistence' and compares three paths,
    including external on-demand derivation. Readable as a necessary rather than sufficient
    condition, so INFO.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/b0f9617cfeabe62fe3bb4e09/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/b0f9617cfeabe62fe3bb4e09/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/6a33452f49e5477b8099d126092706ac/outputs/review-concept-attribution.md
raw-output-sha256: 71cf849f869abc0bd5b00a09f5357da153c30d02bbb32979640154501325cd66
---

# Review

Checked identity claims against: indexes-lower-recall (the false copy as the sharpest case of suppressed retrieval matches the target's control-flow mechanism, which it extends to any artifact treated as exhaustive); tracked lineage and the lineage definition (both match); make-like staleness detection (cheap detection plus re-read-and-decide review matches); the text testing framework (Level A deterministic/cheap and Level B LLM rubric graders match); keep-compiled-views-aligned (provenance, regeneration rules and staleness detection match its source-of-truth rules); the tag-readme spec (the `complete` mark as a validated cache, enforced-or-omitted, matches); and the frontloading note (inlining known values to spare execution context matches). All targets resolved.

The one substantive mismatch is the use of the executor-determinability note: the note builds its "third class" on a tension the target already resolves, by placing pre-call recomputable values in the target's situational class.
