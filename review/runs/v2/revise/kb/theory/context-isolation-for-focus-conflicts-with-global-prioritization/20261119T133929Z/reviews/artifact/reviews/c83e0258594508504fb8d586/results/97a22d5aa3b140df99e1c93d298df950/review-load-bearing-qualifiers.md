---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - 'Solving a hard problem in a bounded LLM context pushes an agent system toward
    **context isolation**: load deep task-relevant material and exclude unrelated
    work so the task stays within the model''s usable attention budget'
  reason: The core information-and-capacity conflict generalizes to any bounded-memory
    stateless worker whose task state excludes competing workload state, not exclusively
    to LLM contexts and agent systems. Because the note is plainly scoped to LLM agent
    orchestration and builds on per-window LLM attention feasibility, this is intentional
    LLM-domain scoping and is reported as INFO rather than WARN. (Separately, 'hard'
    in 'Solving a hard problem' is a colloquial stand-in for context-heavy work, but
    it does not narrow the title, description, Claim mode, or Scope.)
  level: info
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
note-sha256: 82a9737f62ea90df05da18f1a7e0418c651fa2d6b64c3037af8645fbc824298f
criterion-sha256: 1e1f9e2efcdcbd278fbaac47775704be52b0891d84e248189ac81fba3bf802e9
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/c83e0258594508504fb8d586/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: 97a22d5aa3b140df99e1c93d298df950
completed-at: '2026-11-19T13:47:07Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/outputs/review-load-bearing-qualifiers.md
raw-output-sha256: 41ac0a4ee423f043654b2b96881313c1c6b7cbf71a2ab1fd5c565523bb406b27
format: 2
---

# Review

Every qualifier in the title, description, opening claim, and Scope preconditions is load-bearing under the deletion test. In the title (`Context isolation for focus conflicts with global prioritization`), `context` distinguishes information exclusion from process isolation; `for focus` is load-bearing because the conflict depends on excluding unrelated work specifically to preserve task-solving attention budget (isolating a verifier for decorrelation, for instance, does not require excluding portfolio priorities); and `global` is load-bearing because local technical assessment and purely intrinsic checks continue to work inside an isolated context.

In the formal claim statement, `bounded effective context`, `live` competing state (distinguishing changing workloads from previously named static rules), `stateless`, and `relational` prioritization each do direct work in the argument and correspond to explicit counterexample boundaries. The LLM/agent wording is intentional domain scoping per the gate's special case, warranting an informational finding only.
