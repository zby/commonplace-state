---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (description restates the title): replaced the frontmatter description
  with one that names the harness-side jobs (enforcement, context assembly, evidence
  replay, store bookkeeping) and the three base-LLM competences, keeping the working-hypothesis
  status.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
input-sha256: 419acda77e6b5bc13c399ec9c4b4c5bade6fe32767d75d47c660bb4e1f3526e6
candidate: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/calls/launches/d473fe678ada4c3ba7e1f523555c3331/outputs/candidate.md
candidate-sha256: 2604746e800aa06ad86bbbe89a71eb77ed954d35c96c1ce7c58571a5b3e5632b
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/artifact/edits/62ffd945ecc591f2fd45dcc5/observation.json
contract-sha256: cb15395b5b139f4e2c03d3a8bc974b6cdf52f0a427c623b8341fa6cb0835883a
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z
launch: d473fe678ada4c3ba7e1f523555c3331
completed-at: '2026-11-24T13:29:12Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/calls/launches/d473fe678ada4c3ba7e1f523555c3331/outputs/result.md
raw-output-sha256: 94b26cee6f67c76e12c54e416e153c051deae586279c119f4c75d5fd4be80010
---

# Report

- `new-pattern` — a description that paraphrases the title and adds only qualifiers, so it gives no retrieval value beyond the title. Passage: `description: "Working hypothesis: harness code can supply much of an autonomous selection-based learning loop, leaving three conjectured semantic competences on the frozen base LLM"`. Change: the description now names what harness code takes (enforcement, context assembly, evidence replay, store bookkeeping) and the three competences left on the base LLM (interpreting unformalized text; diagnosing novel failures and synthesizing remedies; judging unformalized trade-offs). It also names the fixed-weight setting. It keeps "Working hypothesis".

Constraints observed: the change is confined to the frontmatter description, as scope requires. The new description does not say "irreducible" and does not cite the Harness Evolution evidence. The relied-on harness-offload split, the three named competences and the working-hypothesis status are kept and now appear in the description. The body, title, H1, links and tags are unchanged.

Findings not touched: none. The result holds one finding, and it was fixed.

Noticed but not applied: the description no longer says "conjectured" or "semantic". "Working hypothesis" carries the conjectural status, and the competences are named explicitly. Adding the reviewer's optional implication, that store maintenance needs no separate competence, would have made the description too long, so it was left out.
