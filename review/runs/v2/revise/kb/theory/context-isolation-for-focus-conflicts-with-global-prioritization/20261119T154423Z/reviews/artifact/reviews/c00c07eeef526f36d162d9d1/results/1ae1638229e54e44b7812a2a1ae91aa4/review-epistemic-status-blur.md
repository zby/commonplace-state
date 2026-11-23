---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - The *direction* of the failure comes from a separate mechanism when relative priority
    is unknown—most visibly the workflow's or policy's default action, reinforced
    by model-level thoroughness and salience biases.
  reason: Combines a structural derivation (that missing competing-work context yields
    indiscrimination rather than a specific failure direction, so a separate mechanism
    sets direction) with an unsupported empirical/mechanistic proposal ("most visibly
    the workflow's or policy's default action, reinforced by model-level thoroughness
    and salience biases") in the same flat declarative register. Neither cited evidence
    nor derivation establishes that defaults are "most visibly" responsible or that
    model-level thoroughness and salience biases reinforce them; the following bullet
    explicitly notes that the cited practitioner account does not isolate workflow
    defaults from worker behavior.
  level: warn
- scope: passage
  quotes:
  - compounding the oracle asymmetry—tests reward a present guard but rarely penalize
    an unneeded one—analyzed in [a guard against a conjectured requirement removes
    the experiment that would test it](./a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md).
  reason: Presents both the linked note's conjectural oracle-asymmetry account and
    its compounding with missing global context declaratively without marking the
    conjectural status of the compounding claim, though this occurs inside an illustrative
    manifestation rather than the central thesis.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/review-gates/semantic/epistemic-status-blur.md
contract: verdict
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
criterion: kb/instructions/review-gates/semantic/epistemic-status-blur.md
note-sha256: 85cbcfe326d277692709341f08caaf89c7ab697c484c93caf5c194a9f8f11c50
criterion-sha256: ec58b5e74b81528409483b42dd9a8c11730792eda308bab8ce72f962b0d6974f
target-sha256: 12b4e84afd1ccba61d007e12cebfe51c89523d6cb19be7f64b14e46ecc61fa78
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/artifact/reviews/c00c07eeef526f36d162d9d1/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: gemini-4-neon-high
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews
launch: 1ae1638229e54e44b7812a2a1ae91aa4
completed-at: '2026-11-19T15:54:36Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T154423Z/reviews/calls/launches/1ae1638229e54e44b7812a2a1ae91aa4/outputs/review-epistemic-status-blur.md
raw-output-sha256: f0773b940088699d86f81d32dccadec26ff4aad434c27a2c20c343045de2e265
format: 2
---

# Review

Most of the note separates epistemic statuses carefully: the central claim is marked as a conditional structural derivation (`Claim mode: universal` under three stated conditions), the practitioner quotes from Nostalgebraist/Anthropic are explicitly scoped as motivating origin rather than corroboration (including their confounding factors), the Commonplace mechanisms are explicitly scoped as local design examples rather than comparative evidence, and Scope disclaims controlled measurement of execution quality, triage error, or saved operator attention.

The main status collapse occurs in the transition from structural indiscrimination to the observed failure direction, where an uncorroborated empirical attribution (identifying workflow defaults as "most visibly" the mechanism and citing model-level thoroughness and salience biases) is stated with the same declarative confidence as the structural derivation immediately preceding it.
