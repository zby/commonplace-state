---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - natural-language summaries and judgments do not — there is no comparison a machine
    can run, so they stay as live reads or are omitted
  reason: Precondition 1 applies the omission resolution to natural-language summaries,
    which must be live reads or omitted. The regime section says that where verification
    is judgment, 'the hand-maintained dependent artifact is not forbidden; it is unavoidable',
    and places it under managed staleness. A derived summary is a dependent artifact
    whose verification is judgment, so one passage forbids keeping it and the other
    permits it. The Consequences bullet 'When a copy can't be checked, the resolution
    is omission' sharpens the conflict.
  level: warn
- scope: passage
  quotes:
  - There is no safe middle where the copy is maintained by hand and trusted by consumers.
  reason: The opening says a copy has 'exactly two valid states'; the next sentence
    restricts the forbidden middle to copies that are both hand-maintained and trusted.
    This leaves open whether a hand-maintained, untrusted copy is invalid (per the
    first sentence) or permitted (per the second). This is likely drift needing confirmation.
  level: info
- scope: passage
  quotes:
  - When this precondition fails, the value was never a recomputable copy in the first
    place
  reason: Precondition 3 is listed as a condition under which enforcement of a recomputable
    copy is available. Its own text says that when it fails the value was never a
    recomputable copy, so it is a definitional exclusion rather than a precondition
    on enforcement. The framing shifts between the two roles.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/internal-consistency.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/semantic/internal-consistency.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: 05676960f5c1c2a28267be3f8abb77474788e9d59110a62827124e0061e06523
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/b8fecd70393097495b476043/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/b8fecd70393097495b476043/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-internal-consistency.md
raw-output-sha256: 69cb288aac1d1895a3d084b172b82f0423fe3dd68a93a6856008b5b4246f8c48
format: 2
---

# Review

The main line is coherent. The asymmetry, the check-price flip, the enforcement-as-third-class section and the consequences agree that recomputable copies must be checked or absent, and that omission is the costlier fallback.

The contradiction lies at the regime boundary. The note works hard to separate the deterministic end, where enforce-or-omit holds, from the judgment end, where a hand-maintained dependent artifact is "unavoidable". Precondition 1 and the third Consequences bullet then assign judgment-verified summaries to omission or live reads, which applies the deterministic-end rule to cases the regime section had placed outside it. A reader cannot tell whether an uncheckable derived summary may be kept under managed staleness or must be removed.
