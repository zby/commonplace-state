---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '## What "checked" requires — and its limits'
  reason: 'The type spec asks that a note state its known limits under their own `##
    Scope` heading, so that rescoping edits and scope-testing review gates can find
    them. This note knows its limits: the rule applies only where a mechanical derivation
    rule exists, where ground truth exists at validation time, and where the validator
    bottoms out rather than recursing. It also names a failure case, a judgment-call
    derivation rule that relocates the forbidden state. But these limits sit inside
    a section titled `What "checked" requires — and its limits` and are mixed with
    the enforcement preconditions, so no `## Scope` section exists. The regime boundary
    in `Where the rule applies` (managed staleness where verification is judgment)
    is a second applicability condition that is also outside a Scope section.'
  level: warn
outcome: warn
description: Controller-only revalidation of retained worker output; no new judgment
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/types/note.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/d9afba1f7ccbc253a4856928/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T123635Z/artifact/reviews/d9afba1f7ccbc253a4856928/observation.json
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
launch: a5810bff8eaf4679b97aae35cff37aba
completed-at: '2026-11-15T13:09:37.622554+00:00'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/a5810bff8eaf4679b97aae35cff37aba/outputs/review.md
raw-output-sha256: 52b3e5370fc9518098233736ebee4c7d381378eccd7db7c753be16fb9deef1cb
format: 2
---

# Review

## Summary

The note mostly follows the `note` type spec's authoring instructions. One instruction is unmet: its known limits do not appear under a `## Scope` heading.

## Assessment

**Main claim near the top.** The first paragraph states the rule: a derived copy of recomputable truth is either checked by a validator or absent. It also rules out the hand-maintained-and-trusted middle. The title works as a compressed handle for that claim.

**Linking.** Inline links connect the note to its adjacent mechanisms: indexes that suppress recall, lineage, make-like staleness detection, the text testing pyramid, frontloading and fix-what-the-executor-can't-determine. The Relevant Notes footer gives each link a relation and a reason, following the template's footer form.

**Rationale, not procedure.** The note keeps to design rationale. The imperative-sounding consequence ("Never write the unenforced natural-language version of a checkable claim") is a consequence derived from the rule, not an operational procedure.

**Open Questions.** This section follows the template and lists unresolved points worth tracking.

**Frontmatter use.** The note has no `user-verified` field, so it does not claim human verification. The `title-as-claim` trait fits the title.

**Scope.** This is the unmet instruction, recorded as the finding. The type spec says to omit the section only when no limit is known. Here the limits are known and explicit, but they are folded into the preconditions section and the regime discussion. A rescoping edit would have to rewrite those sections rather than narrow a dedicated Scope section, and scope-testing gates will not find the limits under the expected heading. A fix would move or restate the applicability conditions and failure cases under `## Scope`, leaving the preconditions section to describe what enforcement requires.
