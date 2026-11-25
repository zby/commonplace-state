---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - harness code can supply much of an autonomous selection-based learning loop, leaving
    three conjectured semantic competences on the frozen base LLM
  reason: 'The description mostly restates the title''s structure: harness code takes
    over much of the loop and three competences remain. It adds the epistemic status
    (''working hypothesis'') and the qualifiers ''autonomous'', ''semantic'' and ''frozen''.
    It does not name the three competences: interpreting unformalized text, diagnosing
    novel failures and synthesizing remedies, and judging unformalized trade-offs.
    It also does not say which work moves to harness code: enforcement, evidence capture
    and replay, and store bookkeeping. Those details would separate this note from
    nearby notes on scheduler–LLM separation, semantic-work relocation and on-balance
    judgment in a short result list.'
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
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/af7ba71d36384ef4841ef1b63957d40e/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/6b1e28db05c79676b7d74617/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: af7ba71d36384ef4841ef1b63957d40e
completed-at: '2026-11-24T13:15:03Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/af7ba71d36384ef4841ef1b63957d40e/outputs/review-description-discrimination.md
raw-output-sha256: d1d3e88eb51d9f8c7309a83f6f013b7ede13767400de24186a186e20132d0773
format: 2
---

# Review

## Summary

Read with the title, the description adds some context. It says the split is a working hypothesis, the loop is autonomous and the remaining competences are semantic and sit on a frozen model. Its sentence shape still mirrors the title: harness code supplies much of the loop, and three competences remain.

The note's retrieval value lies in naming those three competences and saying which kinds of work move to harness code. The description gives neither. An agent searching for a list of base-model prerequisites, or for where diagnosis and trade-off judgment sit, would get little from it beyond the title. Naming the three competences in compressed form, such as "interpretation, diagnosis/synthesis, and trade-off judgment," would make it discriminating.
