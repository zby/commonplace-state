---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
note-sha256: 2e630578eddab3da40f0b287d82e285730e62bb53385ce9d7bddc7fd8b9fca81
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: bbe526c49328425f8ae9f1e0b765634e
completed-at: '2026-11-18T16:04:23Z'
findings: []
contract: verdict
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/4cafe144f9b5c4f614eef1b0/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/4cafe144f9b5c4f614eef1b0/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/bbe526c49328425f8ae9f1e0b765634e/outputs/review-grounding-alignment.md
raw-output-sha256: 240ce7fc91d0ee9373df60c01250045839fa3c9c6639bd903f2097cc58395ed4
---

# Review

## Summary

All links are library artifacts. I checked whether each invoked claim matches the target's claim and scope.

- **Frontloading spares execution context.** The note invokes the saving that comes from skipping discovery and derivation computed before an LLM call. The target names "the discovery, derivation, and indirection the call no longer performs" and says that one build-time computation can save many runtime calls from repeating work. The note marks its move to persisted artifacts as its own extension ("extended here"), so it does not overstate the target's scope.
- **Indexes lower recall when they suppress retrieval that would find more.** The note invokes the suppression mechanism for a stale copy that a consumer treats as exhaustive. The target states that "the same mechanism applies to any artifact a consumer treats as exhaustive". It frames the mechanism as conditional, and the note restates its two conditions. The target also attributes staleness to "separate update paths", which matches the note's wording.
- **Tag-readme type (mark).** The type spec says every tagged artifact across the participating collections is reached in one hop, that readers may skip the by-tag `rg` sweep, that enforcement is reactive at next validation, and that assignment fit is judged in semantic review, not by the validator. It also says "a false mark tells exhaustive consumers to stop looking while members are still out there". Every mark claim in the note matches.
- **Connect-report type.** The type spec has readers "treat its contents as suggestions to evaluate, not as state already in the KB". Its quality gates make link resolution and required sections validator-checked, and judging a target calls for its actual claim, evidence, caveats and contract. Its discovery trace reads indexes and runs searches. All of this matches the note.
- **Footer links.** The *LLM recompute cost* link grounds "why recomputation is costly". The target argues that model-side derivation can be unusually expensive, which matches. The *enforced tag-README* link extends the mark example, and the target describes the validator-checked `complete` contract that authorizes a bounded stopping shortcut. The *history* link contrasts with content that has no later source. The target argues that unrecorded production history cannot be recovered later, which fits the note's "condition 3 fails".

No route claims broader or more direct support than its target provides.
