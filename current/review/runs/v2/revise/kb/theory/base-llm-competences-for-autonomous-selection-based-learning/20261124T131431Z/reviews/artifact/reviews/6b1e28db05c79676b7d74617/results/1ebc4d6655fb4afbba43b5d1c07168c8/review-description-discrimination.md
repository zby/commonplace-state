---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Working hypothesis: harness code can supply much of an autonomous selection-based
    learning loop, leaving three conjectured semantic competences on the frozen base
    LLM'
  reason: 'The description mostly paraphrases the title (harness offloads much of
    the loop, three competences remain on the base LLM). Its additions are thin qualifiers:
    "working hypothesis", "autonomous", "semantic" and "frozen". It names neither
    the three competences (interpreting unformalized text into action, diagnosing
    novel failures and synthesizing candidates, judging unformalized trade-offs) nor
    what the harness takes over (enforcement and context assembly, evidence capture
    and replay, store bookkeeping). Without those, an agent comparing this note against
    neighbours on harness offloading or semantic-work relocation would learn little
    beyond the title.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
note-sha256: 7f5a6048df7dfce343e76ede90fc1a979b32ce55d09dcab04737d767e44ff867
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/1ebc4d6655fb4afbba43b5d1c07168c8/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/artifact/reviews/6b1e28db05c79676b7d74617/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews
launch: 1ebc4d6655fb4afbba43b5d1c07168c8
completed-at: '2026-11-24T13:15:22Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/reviews/calls/launches/1ebc4d6655fb4afbba43b5d1c07168c8/outputs/review-description-discrimination.md
raw-output-sha256: a28205176d6c71e5f10f32fc1e134177324f9ab046302b54fe3a1ff5ca163ec1
format: 2
---

# Review

## Summary

Read together, the title and description say the same thing twice. The description adds epistemic status and minor scope words ("autonomous", "frozen", "semantic") but no mechanism, concrete scope, or implication. The note's most discriminating content is the identity of the three competences and the split of harness-side machinery. That content would let an agent pick this note over related notes such as the scheduler–LLM separation or semantic-work relocation notes. A stronger description would name the three competences briefly, or state the implication that store maintenance and criterion revision need no separate competence.
