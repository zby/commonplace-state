---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/structural/compound-bullet.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/structural/compound-bullet.md
criterion-sha256: 21f452393fa553aa0a6e6cd65cb858499bb281d2dffc82d4c90e000c0cb6344f
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 675b9e98a7a84713856bda833f41d987
completed-at: '2026-11-16T22:19:21Z'
findings:
- scope: passage
  quotes:
  - The sweep pattern is hand-authored, but it executes as a strict mechanical extraction
  reason: 'The `complete`-mark bullet makes two separable points. The first is that
    the mark is enforced: a validator re-derives membership and fails mismatches.
    The second, joined by `but` and a dash, is that the hand-authored sweep pattern
    does not reopen the regress because of precondition 4''s amortization argument.
    That second point stands on its own as a claim about validator trust, and readers
    scanning the instance list are likely to miss it. It could be its own bullet or
    sentence, or move to precondition 4.'
  level: warn
- scope: passage
  quotes:
  - A derivation rule that is itself a judgment call rather than a strict mechanical
    extraction does not meet this precondition
  reason: 'Precondition 4 argues that a central validator ends the regress through
    amortization. Its closing sentence adds a separate disqualifying condition: a
    validator whose derivation is a judgment call is the forbidden state moved down
    a layer. The two points are related, and the second can be read as the boundary
    of the first, so this is borderline. It is reported for awareness only.'
  level: info
- scope: passage
  quotes:
  - currently resolved by omission (read the contract live)
  reason: The hot-path-skills bullet states its current state (omission) and then
    recommends enforcement as the dominant alternative. The bullet is short, and the
    recommendation follows from the current state, so this reads as one point with
    elaboration. It is noted only as a mild case.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/e5e06c1f502bd9e40a6c0237/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/e5e06c1f502bd9e40a6c0237/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/675b9e98a7a84713856bda833f41d987/outputs/review-compound-bullet.md
raw-output-sha256: d6017c0bbdeaca89af742ee9bf80f5994ed3223b128a17b52631adc156b4cc60
---

# Review

Most long list items develop one idea with supporting detail. Examples are the Consequences bullets, the bullets for compiled views and duplicated build artifacts, and preconditions 1–3. Elaboration such as "Machine-followable suffices" or the ADR 025 and skill-edit examples supports the item's own claim and is not a second claim.

The clear case is the `complete`-mark instance bullet. After describing the enforced validator, it appends a separate argument about why a hand-authored sweep pattern is still acceptable. That argument concerns validator trust, and it repeats precondition 4. Embedded in an instance bullet, it gets lost when readers scan the list. Precondition 4 and the hot-path-skills bullet are borderline and recorded as INFO.
