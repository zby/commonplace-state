---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - When a copy can't be checked, the resolution is omission
  reason: 'The bullet frames omission as the response to copies that cannot be checked,
    but its own examples, and the hot-path-skills instance later, are copies that
    could be checked and simply were not: ''both pay a build-time or hot-path cost
    that enforcement would have avoided'', and for hardcoded contract values ''Enforcement
    ... would dominate''. The mechanism (an unchecked copy must not be trusted) covers
    every copy that is not currently checked, whether checking is impossible or just
    unimplemented. The ''can''t'' framing excludes the second case, which is the one
    the examples illustrate.'
  level: warn
- scope: passage
  quotes:
  - It is the general form of
  reason: The rule is framed as the general form of 'a cache must never be the only
    copy'. That maxim concerns data loss when the cache is the sole store; this note's
    mechanism is a stale copy being trusted over a source that still exists. The two
    share the derived-copy setting but not the failure mechanism, so the framing points
    the reader at the wrong reason the rule holds.
  level: warn
- scope: passage
  quotes:
  - This is the sharpest case of
  reason: 'The preceding sentence names two harms of a false copy: telling consumers
    to stop looking, and having them follow a snapshot of a world that has moved.
    Framing this as a case of recall suppression covers the first harm but not the
    second, which is acting on stale content rather than missing items. It emphasizes
    one route without excluding the other.'
  level: info
- scope: passage
  quotes:
  - the edit-time surface
  reason: The validator runs at validation time, which the note elsewhere calls 'check
    time'; it is an edit-time surface only when validation runs on every edit. Emphasis
    rather than exclusion.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/sentence/framing-mismatch.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/sentence/framing-mismatch.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: ce0901c0ffaeab91c291cf70e2e86eac0681d8922b4f4fd7e71cd85391e0d46f
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/b2b23a231c169658fde405f8/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/b2b23a231c169658fde405f8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 6a33452f49e5477b8099d126092706ac
completed-at: '2026-11-16T22:21:22Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/6a33452f49e5477b8099d126092706ac/outputs/review-framing-mismatch.md
raw-output-sha256: a4ffadae966cb97cb209e3e061e473ebb54f10f06f4cb6c41641111128aefa46
format: 2
---

# Review

The core mechanism (an asymmetry between a bounded recomputation cost and silent, unbounded wrongness, with the check price deciding between managed staleness and enforce-or-omit) is framed at the right level of generality in most places. Two sentences misdirect. The omission bullet ties the rule's fallback to copies that cannot be checked, though its examples are checkable-but-unchecked copies. The closing line names a cache maxim whose mechanism (sole-copy loss) differs from this note's (stale-copy trust).
