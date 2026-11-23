---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 85cbcfe326d277692709341f08caaf89c7ab697c484c93caf5c194a9f8f11c50
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
outcome: pass
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 1ae1638229e54e44b7812a2a1ae91aa4
completed-at: '2026-11-19T15:54:36Z'
findings: []
contract: verdict
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/251647041dcf9950e0c1063e/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/outputs/review-unearned-generality.md
raw-output-sha256: 81fbb2470425b8c24119be0b01864c8258683df4a0082a399592a565f090fdc4
---

# Review

The central claim's vocabulary sits at the same level of generality as its argument and worked instances:

- **`context isolation` and `focus`:** The mechanism operates directly on excluding unrelated context to preserve a bounded attention budget, not on a narrower sub-agent or coding-only convention. Downgrading to a narrower term such as "sub-agent scoping" would allow standalone isolated sessions or single-artifact revision runs that the general wording forbids from performing relational global prioritization.
- **`global prioritization`:** Operationalized immediately into effort allocation across branches, stopping/deferring on opportunity cost, and escalation triage, and worked across three distinct manifestations (uncalibrated escalation, earnest low-value tangents, local over-specification). Downgrading to one manifestation (e.g., escalation triage) would drop the other instances covered by the same comparison-set mechanism.
- **`agent` / `agent system`:** Supported by mechanism (bounded LLM context and statelessness) and worked across two distinct instance classes—coding agents (Nostalgebraist/Anthropic, diff over-guarding) and KB-maintenance agents (traversal logging, unattended note revision under ADR 138, unresolved-frontier queueing).

The body prose stays concrete throughout, with no distributed abstraction.
