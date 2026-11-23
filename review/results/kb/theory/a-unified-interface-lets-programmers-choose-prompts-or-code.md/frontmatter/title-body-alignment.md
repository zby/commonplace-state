---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
note: kb/theory/a-unified-interface-lets-programmers-choose-prompts-or-code.md
note-sha256: bb646d7330643de2b6d2af657596559185f541277c08fd0b08cae1bb6fd18afa
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261120T110829Z
launch: 3520e864e524489aa2b8264997528ccc
completed-at: '2026-11-20T11:09:20Z'
findings:
- scope: passage
  quotes:
  - The practical consequence is that interface parity alone is not enough for safe
    swapping.
  reason: 'Claim drift by omission. The body establishes a qualified claim: a unified
    interface keeps a prompt–code swap local to the binding at the call site, but
    the abstraction leaks asymmetrically. Prompt-to-code breaks LLM callers that relied
    on lenient interpretation. Code-to-prompt breaks code callers'' latency, cost
    and error-handling assumptions. Caller-free swapping therefore holds only when
    schemas are enforced before codification and call sites have headroom for fallible,
    slower model execution. The unqualified H1 says choice is possible ''without changing
    callers'', which the body explicitly limits. The title should carry the leak or
    its condition, for example that the interface keeps swaps local only where callers
    were written for both regimes.'
  level: warn
contract: verdict
target-sha256: 8e57196c80dac6c3d6baa51a246e3526a3a7664d76399e42781b02f1f5d43c05
target-capture: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/3520e864e524489aa2b8264997528ccc/inputs/note.md
observation: kb/reports/state/review/runs/v2/20261120T110829Z/artifact/reviews/5a0c5cc3b1e1e2ca5f3e41f8/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/20261120T110829Z/calls/launches/3520e864e524489aa2b8264997528ccc/outputs/review-title-body-alignment.md
raw-output-sha256: 123f8b9295c7a78ab7ec3188856f5b525329180cbd14bc549d3ddf2a5b345bfa
---

# Review

## Summary

The body supports the title's core mechanism. The llm-do binding, the `ticket_classifier` walkthrough and the three swap moves all show implementation changes that stay local to the binding without call-site edits.

However, about half of the body sets limits on that claim. The opening paragraph ends by saying the abstraction "leaks asymmetrically". The "What the interface hides and what leaks" section shows how each swap direction breaks callers. The Scope section says call invariance is not behavioral invariance and that bidirectional swapping needs call-site headroom. The body therefore establishes a qualified claim, while the H1 states an unqualified one. The drift is not severe, because the call text truly stays unchanged. Still, a reader who links on the title alone would take away a stronger promise than the body delivers.
