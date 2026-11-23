---
type: types/edit-result.md
outcome: changed
changes:
- 'hedge-strength-mismatch (finding 1, fail): opening sentence now attributes to the
  linked note only what it says (an English instruction permits a set of readings
  an LLM executor resolves; code extraction is a separate intervention to assess)
  and states the bidirectional constrain/relax movement as this note''s own extended
  premise; link text changed to ''English account of prompting'', target unchanged.'
- 'hedge-strength-mismatch (finding 2, warn): typed-callables sentence now reports
  the target''s limited claim (skills, tasks and workflows are callable in a limited
  sense with document-type signatures, not conventional functions), marks the extension
  to tools as this note''s own, and replaces ''type-theoretic view'' with ''this callable
  view ... across the neural-symbolic boundary''.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
input-sha256: 8db07906b7690ad43932741f4438eef6fbe093630e3b77637fbbf6c85354489e
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/calls/launches/f4784f4c832c470f8829229710c44b53/outputs/candidate.md
candidate-sha256: 8a68d80eb4f779b8b90de828142f985e323d8b319154afbec7167b005296cd46
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/artifact/edits/4cdf228e3129d533efccece8/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z
launch: f4784f4c832c470f8829229710c44b53
completed-at: '2026-11-20T09:58:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/calls/launches/f4784f4c832c470f8829229710c44b53/outputs/result.md
raw-output-sha256: 3d507a0597be6616c4db9bd5b27828e90ce0fa8f1b690d9b2a9c38cdb405e511
---

# Report

Two changes, both by `fix-strategy-taxonomy.md#hedge-strength-mismatch`: the source's weaker claim is stated, and the note's stronger claim is marked as its own extension ("The source describes X; we extend this to Y").

- Passage: "The [underspecified instructions framing](…) says components should move between … relax rigid code back to LLM. But the framing doesn't say how …" — the attribution now matches the target's English account and code-extraction remark; the bidirectional premise is kept unnarrowed as the note's own; "the framing" became "that premise".
- Passage: "[Instructions are typed callables](…) argues that prompts, skills, and tools share a callable structure … type-theoretic view practical rather than just analogical." — attribution narrowed to the target's actual scope; extension to tools made explicit; "practical rather than just analogical" kept.

Relied-on claims from kb-role (shared interface, local refactoring, reversibility, llm-do hybrid VM, scheduler contrast, local scope) and all must-keep items are untouched.

Findings not touched:

- Finding 3 (info, llm-do claims rest on an un-ingested external repository): outside the supplied scope, and it calls for a source ingest rather than a text edit.

Noticed but not applied (outside scope): the footer gloss for `instructions-are-typed-callables` still says "the type-theoretic view that llm-do operationalises", which carries the same overstatement finding 2 names.
