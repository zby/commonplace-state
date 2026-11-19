---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/types/note.md
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
note-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
criterion: kb/types/note.md
criterion-sha256: e111a08a6571349949088c99b6e0f61f50c60864f83079bdfc22a2ebcbb17a4b
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261115T132933Z
launch: df541799550743eb99a583f595c2b88a
completed-at: '2026-11-15T13:30:00Z'
findings:
- scope: passage
  quotes:
  - '## What "checked" requires — and its limits'
  reason: 'The type spec asks that a claim''s known limits be stated under their own
    `## Scope` heading, omitted only when no limit is known. This note knows its limits:
    the rule applies only at the deterministic end of derived knowledge, and judgment-verified
    dependents remain hand-maintained. It also names four enforcement preconditions
    and failure cases, such as execution-produced evidence and judgment-based derivation
    rules. These limits are spread across `## Where the rule applies: the deterministic
    end of derived knowledge` and this section, mixed with the argument. There is
    no `## Scope` section that a rescoping edit could narrow or that scope-testing
    gates could find.'
  level: warn
contract: verdict
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/f580055429393bc7dd7c04c1/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/20261115T132933Z/artifact/reviews/f580055429393bc7dd7c04c1/observation.json
contract-sha256: 9969d7db1b8228822ac807fdc50483981fc6d62c7effbe601a7de3fac2e131a0
raw-output: kb/reports/state/review/runs/v2/20261115T132933Z/calls/launches/df541799550743eb99a583f595c2b88a/outputs/review.md
raw-output-sha256: 098d930f98f316d499a5c6a57084e871a80083bff39a82951049d83223beef83
---

# Review

## Summary

The note conforms to the `note` type overall. It misses one authoring instruction: its known limits are not collected under a `## Scope` heading.

## Assessment

- **Title as handle; main claim near the top.** The opening paragraph states the claim right away. A copy of recomputable truth must either be checked by a validator or be absent. Hand-maintained-and-trusted copies are ruled out.
- **Links to adjacent notes.** The note links inline where a link helps traversal. Its footer gives each relationship a short gloss.
- **Rationale in notes, procedure in instructions.** The body is design rationale. It covers the failure-mode asymmetry, the regime boundary set by check cost, the enforcement preconditions and instances. The imperative-sounding consequence ("Never write the unenforced natural-language version…") follows from the claim. It is not an operational procedure.
- **Open Questions.** This section is present and follows the template.
- **Scope.** The note has substantive known limits but no `## Scope` section. It states its applicability boundary and its preconditions and failure cases in two argumentative sections. The spec asks for these limits under their own `## Scope` heading. That would let a rescoping edit narrow the claim without rewriting it, and would let scope-testing gates find the limits. This is the one unmet instruction. The limits themselves are stated clearly, so this is a WARN rather than a FAIL.
