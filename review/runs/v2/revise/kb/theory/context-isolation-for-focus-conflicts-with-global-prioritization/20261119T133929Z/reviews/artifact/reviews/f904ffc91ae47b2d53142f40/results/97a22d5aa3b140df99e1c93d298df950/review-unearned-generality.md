---
type: types/review-result.md
findings: []
outcome: pass
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/unearned-generality.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/semantic/unearned-generality.md
note-sha256: 82a9737f62ea90df05da18f1a7e0418c651fa2d6b64c3037af8645fbc824298f
criterion-sha256: 92ea25015eccd7b14c7d95c647809c487d59e7128d0d1e74129c3f1156127023
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/f904ffc91ae47b2d53142f40/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: 97a22d5aa3b140df99e1c93d298df950
completed-at: '2026-11-19T13:47:07Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/97a22d5aa3b140df99e1c93d298df950/outputs/review-unearned-generality.md
raw-output-sha256: 2e864b81594189b68a793ae3675ca8ae6bd3406e01fb8f34db1ffa703506f743
format: 2
---

# Review

The vocabulary altitude of the central claim matches the level at which the argument operates. Each general term in the title, description, and opening is earned by the mechanism and by multiple worked instance classes rather than adopted defensively for coverage:

- *Agent system / worker* operates across both coding-agent supervision (Nostalgebraist / Anthropic babysitting account, local over-specification in a module or diff) and KB authoring/maintenance workflows (Commonplace traversal logging, ADR 138 unattended note revision, unresolved frontier); downgrading to "coding agent" would demote the second class and allow isolated KB workers to handle global triage.
- *Context isolation* turns on excluding unrelated material from a bounded attention window across parallel chat sessions, sub-agents, and unattended revision runs.
- *Global prioritization* covers three concrete decision classes worked in the body (effort allocation / tangent suppression, stop-or-defer decisions, and escalation triage).

Abstraction is concentrated at these load-bearing structural concepts, while the surrounding prose stays concrete and operational.
