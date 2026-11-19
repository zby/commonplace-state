---
description: "S3Gym separates self-scoring from externally measured improvement and tests cross-episode history versus summaries, with weak causal attribution and metric boundaries."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/s3gym-self-testing-self-judging-self-improvement.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: S3Gym

**Source:** [S3Gym snapshot](../../../../sources/.snapshots/s3gym-self-testing-self-judging-self-improvement.md)

## Discovery Trace

Read the complete 2,664-line paper, including result tables, scoring definitions, training results, judgment correlations, summary examples and every game prompt. Reused batch contracts, curated heads and complete title surfaces across all five destinations. Notes-description query for judges, diagnostics, abstraction, scores and contrasts identified diagnostic richness, memory effects and experimental contrast. Read diagnostic richness and memory effects fully; experimental contrast and the linked oracle-strength, fixed-decomposition and episode-abstraction notes were fully read earlier in the batch. Focused S3Gym, score-conditioned summaries, self-judging/improvement and Summary Memory search across reference, agent-memory-systems, agentic-systems and sources returned only a generic SignetAI review match; no direct edge selected from it. No external prospecting; instructions and work excluded.

## Connections Found

- [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **compares-with**: local self-score agreement and later strict-mode performance are separately measured and nearly uncorrelated in the reported aggregate. Retaining a plausible summary or accurately scoring an action is not a demonstrated future capacity gain. The observation does not establish that judge quality has no causal effect.
- [Diagnostic richness](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **compares-with**: summaries sometimes help and sometimes underperform raw cross-episode history. The source supplies concrete strategy examples, but does not isolate retained detail as the cause. Current-episode history and current state remain available in both conditions, and the summary condition also adds a call and duplicates the game prompt.
- [Experimental contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: the observed contrast changes the cross-episode experience representation and associated prompt/call path. It does not separately test self-judgment against verifier labels, causal explanations against other summaries, or diagnosis against score-only memory. Correlations between judging and improvement are not those interventions.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Evaluate memory by effects](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → eventual tracked ingest — **evidenced-by**: a benchmark that keeps self-judgment accuracy separate from later behavioral outcomes and compares two ways of carrying prior experience. Preserve the untested causal uptake and small evaluation samples.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Near-zero judgment/improvement correlation proves better judgments cannot help: the study does not intervene on judgment quality.
- Summary failures establish that abstractions cannot support state-sensitive tasks: the tested summary policy is one treatment and examples are selected.
- Positive area above baseline measures net improvement: negative deviations are clipped to zero.
- The Chess task is ordinary chess: it predicts hidden movement rules and next piece positions on a 15-by-15 board.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

The main seven-model context experiment uses 30 exploration episodes, evaluation every three episodes, three strict-mode episodes per checkpoint, 100,000-token history input and a 14,000-token output cap. Exploration/evaluation seeds are disjoint and evaluation trajectories are not recycled. Verifier step rewards and final scores remain benchmark-side during exploration; action-time self-score predicts immediate reward before the action executes. Observable state changes still give indirect feedback. This is not post-outcome introspection alone.

Appendix A specifies that only previous-episode experience is summarized; the current episode retains raw history. Raw history truncates the tail of older-episode serialization when over budget. Summary makes a separate compression call at episode start, caches Tips, and repeats the game system prompt in its input composition. These details limit a pure representation-only attribution and matter when the prose attributes failures to missing exact state. No matched total-inference-cost result or summary-policy ablation resolves this.

Avg, Max and AUC+ are distinct. AUC+ clips all losses below the initial score and can reward noisy positive excursions; Max selects the best observed checkpoint. NABA further divides by the initial score or a first-positive fallback, so baseline and scale choices matter. Raw game AUCs are not comparable. Explicit concurrency failures are omitted and AUC connects adjacent remaining valid points. Three evaluation episodes per checkpoint and no independent repeat-run uncertainty limit method-level conclusions.

There are 98 model/path/game runs and 116,117 transitions in judging analysis. Positive-event agreement can be inflated by zero rewards; PvZ has .881 agreement but .882 normalized error. Aggregate blockwise correlations are -.010 for agreement and -.018 for negative error versus subsequent gain; these are descriptive associations, not causal tests. No ground-truth-judge replacement or no-self-score control is reported.

Qwen3-8B training is an auxiliary distinct experiment across 20 checkpoints, not the same seven-model controlled pathway comparison. Trust improves, Chess weakly and Snake intermittently, three games remain zero, and PvZ falls from 23 to 6 at every updated checkpoint. Detailed optimizer/data-correction and filtering recipes are underspecified, so do not infer training versus context superiority or a causal reason for regressions. Summary examples provide plausible reusable rules, but no component intervention isolates their semantic contribution. Fixed games, reward definitions and scaffold remain supplied; prospective discovery or general deployment adaptation is not established. No source code inspected or executed for this paper pass.
