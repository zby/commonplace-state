---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Inside one module or diff, guarding a hypothetical edge case looks prudent when
    system-wide complexity budgets and accepted product tolerances are absent, compounding
    the oracle asymmetry—tests reward a present guard but rarely penalize an unneeded
    one
  reason: The title and opening claim generality over bounded-context LLM agent systems,
    and the two preceding bullets separate the general failure mode from their framed
    coding-agent examples, whereas this bullet states its general claim directly in
    unframed software-engineering vocabulary ('module or diff', 'accepted product
    tolerances', 'tests reward a present guard'). Generalize the statement or mark
    the coding case explicitly as an example.
  level: warn
- scope: passage
  quotes:
  - selecting from compressed frontier summaries
  reason: Reuses Commonplace's local 'unresolved frontier' term inside a general open
    question after the body explicitly scoped 'unresolved frontier' as a Commonplace-specific
    illustration. Use a domain-general phrase such as 'compressed candidate summaries'
    or 'compressed triage summaries'.
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/prose/source-residue.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/prose/source-residue.md
note-sha256: cd5d2711b477e1ec78f936b01b02ebf0f7c6e2b760aca5a01631094f2eff367b
criterion-sha256: ff78dee7dcb8b6594356929cf84d0f9283fcfe0a077f93e62e51dee809b4f480
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/cbd318117d3442b0ab04feebafe5ce5b/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/d272fdab45021db75a3e5ded/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: cbd318117d3442b0ab04feebafe5ce5b
completed-at: '2026-11-19T15:48:01Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/cbd318117d3442b0ab04feebafe5ce5b/outputs/review-source-residue.md
raw-output-sha256: 353faa2cb90dbeb62200c76578dcfd4920e93aa9efa9387b9a8dc0d8b7c0804d
format: 2
---

# Review

The note generally separates its agent-systems claim from its motivating coding-agent source and local Commonplace illustrations, framing both explicitly in most places. Two spots still leak narrower source vocabulary into unframed general prose—software-diff terminology in the third failure-mode bullet and Commonplace's `frontier` label in the final open question.
