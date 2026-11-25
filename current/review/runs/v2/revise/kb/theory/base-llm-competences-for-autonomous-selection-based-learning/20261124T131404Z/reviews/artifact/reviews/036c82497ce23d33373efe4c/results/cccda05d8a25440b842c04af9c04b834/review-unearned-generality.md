---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Harness code may offload much of a selection loop, leaving three base LLM competences
  reason: '''Selection loop'' is broader than the case the argument works from: a
    frozen LLM updating a store of procedures, hypotheses and code, with harness evolution
    as the evidence. Downgrading to ''store-updating harness loop'' leaves the argument
    unchanged. However, ''selection-based learning'' is a registered KB term, and
    the competences map onto its proposal and reject-capable evaluation stages, so
    the abstraction has a load-bearing site.'
  level: info
outcome: pass
description: Retained verdict review of kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: 65eb6e50ebf86671e73830336dd77216ac6bc4d37b1e89d6318d431fed96442b
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: 2995eb9053be7afa1d84d3f0989e6751a44919eec5a76a1574508655eba2882c
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/artifact/reviews/036c82497ce23d33373efe4c/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews
launch: cccda05d8a25440b842c04af9c04b834
completed-at: '2026-11-24T13:17:58Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131404Z/reviews/calls/launches/cccda05d8a25440b842c04af9c04b834/outputs/review-unearned-generality.md
raw-output-sha256: cb873b21a2d0b5d7cb149bed8bd067cfde7d59c562e3ce5ccd58e887d055e4b7
format: 2
---

# Review

## Summary

The central claim's vocabulary sits at the level the argument uses. "Harness code," "base LLM," "frozen" and the three named competences are concrete. "Selection-based learning" is the most abstract term. It is a defined KB term, and the note uses its structure: proposal maps to competence 2 and selection to competence 3. The abstraction is concentrated in one load-bearing place rather than spread across most nouns.
