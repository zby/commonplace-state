---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (anthropomorphic framing: a held mental state stands in for the technical
  mechanism of working-context content); ''risks losing structure the agent already
  had'' -> ''risks losing structure already present in the working context''.'
- new-pattern (same); evaluation question 'while understanding was live?' -> 'while
  they were still in the working context?'.
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/agent-memory-requirements/create-memory-directly.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 5bdf06d24d0664420feac8e70a75fb36927d4ec64e40f8bcc9679ca67c0f3e9f
note: kb/theory/agent-memory-requirements/create-memory-directly.md
input-sha256: a4fdf4354bc61827ef815e0304ac1293f8919b458c3fd9ec73f13e4f0f4393e9
candidate: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007/artifact/edits/d3ef100983fde1403536fe47/results/394fdd1b6cca43158d97ac777cfea952/candidate.md
candidate-sha256: df76b4a5a6e353b691bd8f13146ceca02eea258bad516a969f879d973f0946df
observation: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007/artifact/edits/d3ef100983fde1403536fe47/observation.json
contract-sha256: 7b4286ecd718091de931c46cef9b78f7bf0a7c91e01340492ee25d734bf888fb
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007
launch: 394fdd1b6cca43158d97ac777cfea952
completed-at: '2026-11-16T14:06:32Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/agent-memory-requirements/create-memory-directly/cc1a38038007/calls/launches/394fdd1b6cca43158d97ac777cfea952/outputs/result.md
raw-output-sha256: 3a98981379bd9f0877a4c4cd4a7dd9c21c17f4fc4f5b394c979cd126f20ee325
---

# Report

- `new-pattern` — anthropomorphic framing, where a held mental state ("had", "understanding was live") stands in for the technical mechanism, the content of the agent's working context. Passage: "risks losing structure the agent already had". Changed to "risks losing structure already present in the working context".
- `new-pattern` — same pattern. Passage: "while understanding was live?" in the first evaluation question. Changed to "while they were still in the working context?". Here "they" refers to the listed context, provenance, caveats and intended use.

Noticed but not applied:

- The finding's first quote, "understanding is already available during work", appears in the opening sentence. The `defend` input protects that sentence verbatim. Replacing "understanding" with "the needed context is already loaded" could narrow or shift the protected claim, so it stays unchanged. The operator can reword it if the defended claim is restated.
- The frontmatter `description` says "preserves live understanding". The finding does not name it, so it is outside this fix's scope.
