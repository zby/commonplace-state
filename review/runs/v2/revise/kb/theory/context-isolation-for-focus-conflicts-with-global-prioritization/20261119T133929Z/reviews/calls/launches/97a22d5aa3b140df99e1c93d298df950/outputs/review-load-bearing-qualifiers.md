---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Solving a hard problem in a bounded LLM context pushes an agent system toward **context isolation**: load deep task-relevant material and exclude unrelated work so the task stays within the model's usable attention budget"
    reason: "The core information-and-capacity conflict generalizes to any bounded-memory stateless worker whose task state excludes competing workload state, not exclusively to LLM contexts and agent systems. Because the note is plainly scoped to LLM agent orchestration and builds on per-window LLM attention feasibility, this is intentional LLM-domain scoping and is reported as INFO rather than WARN. (Separately, 'hard' in 'Solving a hard problem' is a colloquial stand-in for context-heavy work, but it does not narrow the title, description, Claim mode, or Scope.)"
    level: info
outcome: pass
---

# Review

Every qualifier in the title, description, opening claim, and Scope preconditions is load-bearing under the deletion test. In the title (`Context isolation for focus conflicts with global prioritization`), `context` distinguishes information exclusion from process isolation; `for focus` is load-bearing because the conflict depends on excluding unrelated work specifically to preserve task-solving attention budget (isolating a verifier for decorrelation, for instance, does not require excluding portfolio priorities); and `global` is load-bearing because local technical assessment and purely intrinsic checks continue to work inside an isolated context.

In the formal claim statement, `bounded effective context`, `live` competing state (distinguishing changing workloads from previously named static rules), `stateless`, and `relational` prioritization each do direct work in the argument and correspond to explicit counterexample boundaries. The LLM/agent wording is intentional domain scoping per the gate's special case, warranting an informational finding only.
