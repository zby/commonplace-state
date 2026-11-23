---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - '**Claim mode: universal** under three conditions:'
  reason: 'Uses the KB-internal classification label ''Claim mode: universal'' without
    an inline gloss explaining what ''claim mode'' classifies or what ''universal''
    distinguishes it from (such as a structural claim across architectures versus
    a current-model contingency), leaving a reader without KB context to wonder how
    a claim can be ''universal'' yet conditional.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/62ef267b890a4b7f929ae88949223c8c/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/cf1b7c733514e06bc1df58d9/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 62ef267b890a4b7f929ae88949223c8c
completed-at: '2026-11-19T15:48:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/62ef267b890a4b7f929ae88949223c8c/outputs/review-undefined-terms.md
raw-output-sha256: 55982501176bcc74b269c1df4fe2f0f6e6cfe001d039e5c1e389814aad6618c5
format: 2
---

# Review

## Summary

Almost every technical and KB-specific term in the note is clearly defined or glossed inline on first use, including "context isolation", "global prioritization", "task-internal", "oracle asymmetry", "scale-bearing local facts", "ADR 138", "unresolved frontier" (both glossed and linked), "unsafe substitution", and "relational prioritization". The single gap is the KB-internal taxonomy label introducing the scope conditions in the third paragraph, which assumes familiarity with the KB's claim-mode categories; adding a brief inline gloss or phrasing the claim's generality in plain language resolves it.
