---
description: "AIDE2 separates transferable harness improvements from an inconclusive test of improved self-improvement, with bounded context and inactive-selection evidence."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/aide2-recursive-self-improvement-research-agents.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: AIDE2

**Source:** [AIDE2 snapshot](../../../../sources/.snapshots/aide2-recursive-self-improvement-research-agents.md)

## Discovery Trace

Read the complete 2,019-line paper, restoring the short clipped reference span with a bounded reread. Reused same-batch contracts, curated heads and complete title surfaces across all five authorized destinations. Ran `rg -n -i '^description:.*(compounding|self.improv|context.*efficien|history)' kb/notes --glob '*.md'` and selected compounding, accumulation and context-efficiency candidates. Read compounding fully, followed its accumulation link and read it fully; chose the evaluation-protocol note rather than duplicate the definition edge. The initial guessed memory-requirements efficiency filename was absent; `rg --files kb/notes` filtered for efficiency located the actual context-efficiency note, which was read fully. Experimental contrast and exact-implementation evidence were fully read earlier in this batch. `rg -l -i 'AIDE2|AIDEhuman|ignition test|AIDE85' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources` returned no matches. No additional candidate from those four destinations; no external prospecting or excluded-collection links.

## Connections Found

- [Compounding needs later-episode evidence](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — **is-evidence-for**: the paper separately tests the evolved agent as an outer-loop improver. Its three-seed comparison is inconclusive despite held-out task gains, concretely separating accumulated improvement from demonstrated better improvement production.
- [Context efficiency](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **compares-with**: bounded prompts remove observed context-window failures and shrink per-call input, while fixed-cost tasks permit more search. The paper measures characters at normalized progress and changes multiple harness components; it does not isolate context compression as the cause of every outcome gain.
- [Experimental contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: aggregate held-out gains and reduced proxy-to-downstream failure follow bundled cumulative rewrites. A replay explicitly finds that one proposed robust-selection penalty never changes the selected candidate, so its plausible motivation cannot explain the observed improvement.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Compounding needs later-episode evidence](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → eventual tracked ingest — **evidenced-by**: an explicit evolved-improver comparison that remains inconclusive despite transferable task gains would sharpen the note's distinction between acceptance, transfer and feedback into later improvement. This case is about the comparison actually run, not a claim that no compounding occurred.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Seven accepted rewrites establish accelerating recursive self-improvement: the production outer agent stays human-engineered, while the separate promotion test does not establish superiority.
- Reduced reward hacking is a general safety result: the reported endpoint is a particular isolated-kernel versus training-context mismatch criterion.
- Character reductions directly equal total token-cost reductions: the source measures per-call characters at relative run progress, not all-run monetary savings.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

Main run: AIDEhuman with Opus 4.7 proposes 99 rewrites of a pared-down AIDE0; inner candidates use Gemini 3 Flash. Seven incumbents at steps 2, 6, 28, 39, 47, 63 and 85 raise private selection grade .703 to .778, versus human baseline .749. Two additional complete runs accept two and four changes. Inner candidates optimize public task scores and return a self-selected solution; hidden scores grade that solution. Those grades remain visible and adaptively reused by the outer proposer, so they are not an untouched final evaluation. Outer argmax selection is fixed. Seven accepted modifications do not mean seven autonomous promotions of the outer improver.

Held-out ALE, MLE, FML and one physics-weather task test two checkpoints plus initial/human baselines. Means improve but are not monotone across checkpoints or universally statistically separated from the human baseline. ALE/MLE/weather primarily cap dollars; FML/kernel primarily cap steps. Models also differ across held-out benchmarks, held fixed within comparisons. Five initial FML runs and 48 larger-budget ALE runs hit context limits and use their best available candidate. Weather outcome is relative skill gain from a starting dynamical core, not an absolute WeatherBench leaderboard score. Cross-model appendix uses a common $20 comparison, distinct from the main $5 ALE/MLE budget.

The ignition test fixes the initial inner agent at AIDE47 and compares AIDE47 versus AIDEhuman as outer improver for three seeds of fifty steps. Mean final grades .780 and .782 and earlier mean plateau do not establish superior efficiency, equivalence, sustained compounding or accelerating returns. Final agents from every ignition seed were not independently evaluated on external benchmarks because of cost.

AIDE85 retains UCB1 strategy-arm selection with 30 percent softmax selection, five-step best-node forks, role-specific bounded root/recent summaries, and up to three deduplicated error signatures activated above a 15 percent bug rate. Whole histories are not always loaded. Paper mechanisms are not independently code-verified in this ingest. The robustness-selection penalty preserves ordering and never changes the returned candidate in replay. Another accepted change repairs an evaluator crash caused by one failed case; evaluator repair should not be silently credited as a pure search-policy gain. No component ablations attribute all gains to these mechanisms.

The reward-hacking endpoint covers 38 kernel/training-context pairs, each averaged over three seeds: isolated speedup above 1.02x with less than half surviving downstream or a downstream crash. Reported rates fall 55 to 39 to 32 percent, compared with 39 percent for the human baseline. This is a measured proxy mismatch, not evidence of deliberate intent or broad safety. Twenty-five percent of graded rejected rewrites improve the public signal but fail the private grade. Rejected classical-method analogues and small negative deltas do not prove entire method classes ineffective.
