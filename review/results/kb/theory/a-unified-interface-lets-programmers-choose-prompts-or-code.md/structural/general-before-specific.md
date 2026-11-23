---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/structural/general-before-specific.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bdb0c42538f2ee4b5890e78037c08232d17b911f2d2cd10608eebb083bec1c58
criterion: kb/instructions/review-gates/structural/general-before-specific.md
criterion-sha256: 9a0e5698ffe8e1d4c95eaca4fc4cb00fd74fd70f2c9433f1cc1db1a02ffdd767
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: e2cdfda1e7ac43f1a4560729d225a459
completed-at: '2026-11-20T11:10:35Z'
findings: []
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/e2cdfda1e7ac43f1a4560729d225a459/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/b1b73fdb9f88686c1c3f6f8a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/e2cdfda1e7ac43f1a4560729d225a459/outputs/review-general-before-specific.md
raw-output-sha256: 349a8ba38eeb2e3b46c91da3783dfddffac8f7527101ef2e7fa4a5055dfa9e1f
---

# Review

Section order: the untitled introduction, "The mechanism", "What the interface hides and what leaks", "Scope", "Why this matters for constraining", "The connection to typed callables", "Open Questions".

The introduction states the general pattern first: a unified interface acts as information hiding across prompts and code, and it leaks asymmetrically. "The mechanism" is specific because it names llm-do and a concrete binding. The general claim it exemplifies is in the introduction, though, not in the next section. "What the interface hides and what leaks" develops a different point, the asymmetric leaks, and is not the rule that the llm-do description instantiates. So this adjacent pair does not put an instance before its rule.

The remaining pairs also hold. "Scope" qualifies the leak analysis that precedes it. "Why this matters for constraining" states its general argument before its ticket_classifier walkthrough. "The connection to typed callables" relates the note to a linked claim and does not depend on a later general section. No adjacent pair puts a specific case before the general rule it exemplifies.
