---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the frozen model does not need to keep track of budgets, traces, or regression
    suites in its head
  reason: '"In its head" attributes a private working memory to the model. The technical
    claim is that the model need not hold budgets, traces or regression results in
    its context window or reproduce them from its own outputs, because harness code
    records and supplies them. A literal phrasing such as "the frozen model does not
    need to track budgets, traces, or regression suites within its context" states
    the mechanism without implying internal mental bookkeeping.'
  level: warn
- scope: passage
  quotes:
  - The model must read natural-language procedures, hypotheses, and constraints that
    have not yet been codified into code and let them govern its behavior
  reason: '"Read" and "let them govern its behavior" are close to agency language,
    but the sentence is defining a functional competence and links operative change,
    which specifies behavioral dependence on loaded text. The verbs describe observable
    conditioning of outputs on context, not a claim about comprehension, so no change
    is required.'
  level: info
- scope: document
  quotes: []
  reason: The competence labels (interpreting, diagnosing, judging, recognizing missing
    evidence) and the phrase "overclaiming certainty" name output-level capabilities
    that the note proposes to test through transfer tests. The note is explicitly
    arguing about which functions a model must perform, so these are functional descriptions
    rather than unsupported claims about cognitive internals.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/prose/anthropomorphic-framing.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/prose/anthropomorphic-framing.md
note-sha256: 820039b4e5489ee918668713c3d374ff4a183f4f5dea68f1babef3c07d1ccd2f
criterion-sha256: 292f7c4bfb6506b864f941203c574f8d8fd7e0ecf63ad5d4bc27d6c4405907e3
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/bf629145019e4715bdce2f1a9fbea1c3/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/f318a48a0b65ea32d582e971/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: bf629145019e4715bdce2f1a9fbea1c3
completed-at: '2026-11-24T13:15:30Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/bf629145019e4715bdce2f1a9fbea1c3/outputs/review-anthropomorphic-framing.md
raw-output-sha256: 01bb7ad0e5d833356ab0ab0873e786c11fde7e450353a6ee540131fb8c698faa
format: 2
---

# Review

The note is about which semantic functions a frozen base LLM must perform in an autonomous loop, so most cognitive-sounding verbs are functional competence labels tied to testable behaviour (operative change, transfer tests). Those are acceptable.

One idiom goes beyond that: "in its head" implies an internal mental store. The intended contrast is between harness-maintained records and the model's own context, and a literal phrasing would state that more precisely.
