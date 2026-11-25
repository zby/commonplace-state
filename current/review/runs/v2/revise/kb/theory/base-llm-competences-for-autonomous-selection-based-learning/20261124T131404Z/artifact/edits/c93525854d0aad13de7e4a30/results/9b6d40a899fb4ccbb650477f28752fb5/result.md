---
type: types/edit-result.md
outcome: changed
changes:
- 'new-pattern (link-only first mention of a KB term the sentence depends on; fix
  adds an inline gloss beside the link): glossed ''selection-based learning'' at its
  first body mention as a loop that proposes each change to the store, evaluates whether
  it makes the work better, and can reject it.'
- 'new-pattern (same pattern): glossed ''scheduler–LLM separation'' as assigning repeated
  bookkeeping and defined workflow transitions to code so they are enforced rather
  than reinterpreted on every run.'
removed-links: []
description: Retained changed result of kb/instructions/fix-warnings/fix-strategy-taxonomy.md
  on kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
format: 1
operation: kb/instructions/fix-warnings/fix-strategy-taxonomy.md
operation-sha256: 12c35f999bb2ce55341fb3b94d9c41240c32efb017c4869250d32b14101a8dac
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
input-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
candidate: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/calls/launches/9b6d40a899fb4ccbb650477f28752fb5/outputs/candidate.md
candidate-sha256: bd5d245e1702392273f36c2c350562dcfcd78a742fc1f43e8720d979679edba9
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/artifact/edits/c93525854d0aad13de7e4a30/observation.json
contract-sha256: cb15395b5b139f4e2c03d3a8bc974b6cdf52f0a427c623b8341fa6cb0835883a
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z
launch: 9b6d40a899fb4ccbb650477f28752fb5
completed-at: '2026-11-24T13:26:54Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/calls/launches/9b6d40a899fb4ccbb650477f28752fb5/outputs/result.md
raw-output-sha256: 315fda93abea3bdecd6291bb543acce4b76fe9388be6e8adaebafdcd065c07aa
---

# Report

Two edits, both in the opening paragraph, both `new-pattern`: a KB-internal
term introduced only by a link, in a sentence that depends on it. The fix adds
a short inline gloss beside the link, with wording taken from each linked
note's own description. No strategy in the taxonomy covers undefined terms.

- Finding 1, passage "an autonomous [selection-based learning](...) loop does
  not need the frozen LLM": added an appositive gloss after "loop" using the
  definition's propose / evaluate / can-reject wording.
- Finding 2, passage "Following [scheduler–LLM separation](...), harness code
  can take over": added a relative clause stating what the principle assigns
  to code and why.

No claim, link, quote, title, description or H1 changed. The terms and claims
that kb-role lists as relied on are unaffected.

Findings not touched (by position in `findings`):

- 3 ("transfer tests") and 4 ("outer-loop learning"): outside the supplied
  scope, which says to leave them untouched.
- 5 ("diagnostic richness") and 6 ("criterion revision"): info-level and
  outside the supplied scope.
