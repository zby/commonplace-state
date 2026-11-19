---
type: types/edit-result.md
outcome: proposed
proposals:
- quote: The two failure modes are not symmetric, and the rule rides entirely on that.
  change: The two failure modes are asymmetric, and the rule depends entirely on that.
  reason: negation-first contrast made positive; figurative verb 'rides' made literal
- quote: that is why hand-maintained-and-trusted is *forbidden* rather than merely
    risky.
  change: that is why hand-maintained-and-trusted is *forbidden*.
  reason: redundant exclusion; 'forbidden' already rules out 'merely risky'
- quote: with nothing watching
  change: with no check in place
  reason: figurative phrase made literal
- quote: the hand-maintained dependent artifact is not forbidden; it is unavoidable
  change: the hand-maintained dependent artifact is permitted and unavoidable
  reason: negation-first construction stated positively
- quote: Omission is the fallback, not the optimum.
  change: Omission is the fallback; enforcement is better where it is available.
  reason: '''X, not Y'' construction replaced by a positive statement'
- quote: what keeps the pattern's authorship acceptable instead of a quiet regress
  change: what keeps the pattern's authorship acceptable
  reason: redundant exclusion; 'quiet' is a manner word with no content
- quote: applied not only to caches but to every derived copy of recomputable truth
  change: applied to every derived copy of recomputable truth, caches included
  reason: '''not only X but Y'' construction stated positively'
- quote: quietly stand in for a checkable one
  change: stand in for a checkable one
  reason: manner adverb adds no content
description: Retained proposed result of kb/instructions/simplification-passes/plain-wording.md
  on kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
format: 1
operation: kb/instructions/simplification-passes/plain-wording.md
operation-sha256: 808b0b64f50a46bde4e3e9bbf440aa81291f3d25ea8488e6ce78a90f0a3261dd
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
input-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
candidate: null
candidate-sha256: null
observation: kb/reports/state/review/runs/v2/20261115T222349Z/artifact/edits/30f546ac56d8550d02690e3d/observation.json
contract-sha256: 7f577dba87ec6e78e7e231d2dc16d3bf36bf687b80b00dffa134973588e84c79
profile:
  harness: claude-code
  launch-model: sonnet
  effort: medium
model: claude-sonnet-5-5
run: kb/reports/state/review/runs/v2/20261115T222349Z
launch: 22965d8e6f3f4a34a6b4f4a21d518ef8
completed-at: '2026-11-15T22:24:23Z'
raw-output: kb/reports/state/review/runs/v2/20261115T222349Z/calls/launches/22965d8e6f3f4a34a6b4f4a21d518ef8/outputs/result.md
raw-output-sha256: 32df625fe663fb8e6d0451c89470ca2ddf148a4f6fe096947d74281474c8168d
---

# Report

Eight proposals above; none applied.

## Kept candidates

- "Enforce-or-omit stops being aspirational": keep. The negated word "aspirational" names the status the rule previously had; it states a change of state, not a denial.
- "Checked copies degrade gracefully": keep. "Degrade gracefully" is the field's standard term.
- "the interrupt-placement problem dissolves": keep. Conventional figure; the literal form needs more words ("no longer needs solving").
- "bottom out, not recurse" (precondition 4 heading): keep. "Bottom out" is a standard technical phrase for terminating recursion, and the contrast is the precondition's point; the following text already explains it.
- "Dropping one costs consumers a recomputation, never correctness": keep. The negative states the distinction the claim relies on, and readers might otherwise infer correctness risk.
- "There is no safe middle where the copy is maintained by hand and trusted": keep. This denial is the note's core finding and the positive form is already stated in the preceding sentence.
- "Machine-followable suffices; human visibility is not required": keep. The note defines the requirement, and readers would otherwise assume the usual human-visibility requirement for lineage.
- "silently wrong snapshot": keep. "Silently" carries content here: the failure gives no signal, which is the note's asymmetry argument.
- "the 'complete' mark ... enforced and shipped", "managed staleness", "Level A/B", "recomputable-and-checked", "frontloading": registered or defined terms; preserved.
- "make-like", "hot-path", "ground truth": field terms; kept.

## Questions

None.
