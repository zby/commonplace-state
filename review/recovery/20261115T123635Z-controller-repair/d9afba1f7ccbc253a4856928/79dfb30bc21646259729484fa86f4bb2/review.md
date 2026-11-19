---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - What "checked" requires — and its limits
  reason: 'The type spec asks that the claim''s limits be stated under their own `##
    Scope` heading, which review gates that test scope look for. The note has known
    limits: preconditions 1–4, the judgment-regime boundary in ''Where the rule applies'',
    and the executor-generated-evidence case. These limits are spread across sections
    with other names, so no `## Scope` section exists. A rescoping edit cannot narrow
    the claim in one place, and scope gates will not find a Scope section.'
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
launch: 79dfb30bc21646259729484fa86f4bb2
completed-at: '2026-11-15T13:09:37.720364+00:00'
raw-output: kb/reports/state/review/runs/v2/20261115T123635Z/calls/launches/79dfb30bc21646259729484fa86f4bb2/outputs/review.md
raw-output-sha256: 51ed7f2570f2b9f9a8099415d62c4e7d4e77372d338eb9436c76ef36aa45ddb5
format: 2
---

# Review

## Summary

The note largely conforms to the `note` type spec's authoring instructions. The title is a strong, compressed handle. The main claim, that a copy has exactly two valid states (checked or absent), appears in the first paragraph. The body is design rationale, not imperative procedure; the "Never write…" bullet is a consequence of the rule, not a workflow step. Adjacent notes are linked inline and in a Relevant Notes footer, and each footer link has a relationship gloss. Open Questions follows the template.

The one unmet instruction is the Writing Shape rule that limits belong under `## Scope`. The note knows its limits and states them at length. The rule applies only at the deterministic end of derived knowledge. Enforcement requires a derivation rule, machine-locatability, ground truth at validation time and a validator that bottoms out. Natural-language summaries and executor-produced evidence fall outside it. But these limits live inside "Where the rule applies" and "What 'checked' requires — and its limits", mixed with mechanism and argument. They are not collected in the dedicated section the spec names. The note does not meet the omission condition, "no limit is known", so the section should be present. Moving or summarizing those applicability conditions into `## Scope` would satisfy the instruction without changing the argument.
