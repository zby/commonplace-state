---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/sentence/parsing-ambiguity.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/review-gates/sentence/parsing-ambiguity.md
criterion-sha256: 07bf4245fd5eb41451cd2a6a79ca6655410dae6cc79b7238bcc82ad3a4799dff
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: c043185d3d9f4a17b0d509c28ec48409
completed-at: '2026-11-19T13:45:04Z'
findings:
- scope: passage
  quotes:
  - Explicit static rules can eliminate *previously named* non-priorities and tolerances;
    they cannot supply live relative scale for novel trade-offs across a changing
    workload.
  reason: Coordinating '*previously named* non-priorities and tolerances' under the
    single verb 'eliminate' produces a plausible unintended reading that static rules
    eliminate tolerances themselves, reversing the note's intended point that static
    rules can encode or enforce known tolerances alongside ruling out named non-priorities.
    Adding a separate verb for 'tolerances' (for example, 'eliminate *previously named*
    non-priorities and fix known tolerances') removes the ambiguity.
  level: warn
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/c043185d3d9f4a17b0d509c28ec48409/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/b70ee27772dafe3654825bc3/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/c043185d3d9f4a17b0d509c28ec48409/outputs/review-parsing-ambiguity.md
raw-output-sha256: 13b2b9f25016c675836173eba3dc8372370de9c3f3117876f0119b9212591335
---

# Review

The prose is generally unambiguous in negation scope, modifier attachment, and pronoun reference. One sentence introduces a plausible unintended reading by placing `tolerances` inside the direct-object coordination of `eliminate`, which literally reads as eliminating tolerances rather than encoding or enforcing them.
