---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/clause-packing.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion: kb/instructions/review-gates/sentence/clause-packing.md
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
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
  - a validator is centralized, versioned, reviewed on every change, and amortized
    across every copy it protects
  reason: 'The sentence beginning ''This looks like it reopens the regress, but it
    doesn''t:'' runs about 45 words and packs a concession, a contrast, a four-item
    property list, a consequence (''so its unit cost...'') and a counterfactual comparison
    against N hand-maintained instances. The reader must hold the regress worry open
    across the whole list before reaching the conclusion. Split after the colon: one
    sentence for the validator''s properties, one for the unit-cost comparison.'
  level: warn
- scope: passage
  quotes:
  - the two tracked `AGENTS.md.template` copies
  reason: 'Distance problem: a two-clause parenthetical (root feeds wheel builds...;
    src/commonplace/_data serves editable installs) separates the subject ''the two
    tracked AGENTS.md.template copies'' from its verb ''must be byte-identical'',
    and a second parenthetical follows the predicate. Reorder so the predicate comes
    first (''must be byte-identical'') and the two roles follow after it, or move
    the roles into their own sentence.'
  level: warn
- scope: passage
  quotes:
  - too costly to run always and too noisy to block on
  reason: The Level B sentence states an identity (deciding invalidation is a Level
    B check), interrupts it with a dash gloss, then appends two cost judgments whose
    subject the reader must recover across the gloss. About 40 words with three ideas;
    tolerable but would read more easily with the cost judgments as a separate sentence.
  level: info
- scope: passage
  quotes:
  - the 2026-06-10 skill edits — logged in `kb/log.md` — chose read-the-contract per
    invocation
  reason: An Either/or sentence carries a parenthetical in each branch, and the second
    parenthetical nests a dash interruption inside it, so two unresolved dependencies
    are open at once. Moving the log location out of the parenthetical (or dropping
    it) would remove the nested interruption.
  level: info
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/fca9c5e9abc9b9c31b8173d5/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/fca9c5e9abc9b9c31b8173d5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/6a33452f49e5477b8099d126092706ac/outputs/review-clause-packing.md
raw-output-sha256: cf11682db2201fee8641d65e662606ca42ef03813cb91b62ec9f0ed77eff92fe
---

# Review

Most of the note's long sentences are front-loaded lists or parallel semicolon structures whose subject and verb resolve early, which the gate tolerates. Two sentences overload the reader: the precondition-4 sentence that defends the validator against the regress packs five ideas into one span, and the duplicated-build-artifacts bullet separates its subject from its verb with a two-clause parenthetical. Both can be fixed by reordering or a single split without losing any relation. The two INFO items are moderate peaks that do not require change.
