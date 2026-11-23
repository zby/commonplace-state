---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - a competing workload whose comparison-sufficient live summary cannot sit beside
    deep task context without degrading focus
  reason: 'Leaves the threshold for "without degrading focus" unresolved between two
    materially different readings: (1) any measurable drop in local task-solving quality
    compared to a purely isolated window (strict zero-degradation under soft attention
    decay), versus (2) degrading task performance past the task''s usable-window feasibility
    ceiling or past the point where local quality loss outweighs prioritization gain.
    Choosing between them changes the truth conditions of Condition 2 (under soft
    degradation, reading 1 triggers the conflict for almost any nontrivial live summary
    while reading 2 permits compact summaries inside a usable window), the evidence
    needed to test whether a workload qualifies (any accuracy dip versus feasibility
    failure or net utility loss), and the architectural consequence (whether co-loading
    a compact summary remains viable or splitting into a separate triage pass is forced).
    Nearby context does not resolve the choice: lines 10 and 58 use a usable-window
    threshold ("usable attention budget", "fits inside one usable window"), whereas
    lines 14, 30, and 54 use absence-of-degradation wording ("without degrading focus",
    "without eroding focus").'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/189779dada5e12efb7922e6d/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 1ae1638229e54e44b7812a2a1ae91aa4
completed-at: '2026-11-19T15:54:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/outputs/review-underspecified-assertions.md
raw-output-sha256: fb4d42f84d649d182fc9c01259711e45ad9e03c965d9e1488e080397151b01a9
format: 2
---

# Review

Most load-bearing assertions in the note are cleanly operationalized in place: **context isolation**, **global prioritization**, **task-internal** technical assessment, **locally calibrated scale** (numeric latency budget, token cap, metered dollar cost), **scale-bearing local facts**, the three unbundled decisions, and **unsafe substitution** are each defined with enough specificity to fix their truth conditions and architectural consequences.

One load-bearing threshold remains materially unresolved: Condition 2 of the universal claim (and the identical trigger for splitting execution from triage in line 30) turns on whether a comparison-sufficient live summary can sit beside deep task context "without degrading focus", without choosing between zero measurable degradation versus staying inside a feasibility/net-value ceiling. Under the KB's soft-degradation model of LLM context windows, those two thresholds classify different workloads into the conflict regime and imply different architectural triggers.
