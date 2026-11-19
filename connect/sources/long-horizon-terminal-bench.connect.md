---
description: "Discovery for LHTB's deterministic partial-credit grading, false finishes, and budget-limited execution"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/long-horizon-terminal-bench.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Long-Horizon-Terminal-Bench

**Source:** [Long-Horizon-Terminal-Bench](../../../../sources/.snapshots/long-horizon-terminal-bench.md)

## Discovery Trace

- Read the complete 1,883-line snapshot, including references and task appendix, in three bounded reads. Source scope is 46 terminal tasks, deterministic final-state subtask scoring, 17 evaluated models, and failure analyses. The paper does not test an improved memory or planning intervention.
- Read `kb/sources/COLLECTION.md`, the report type, and the README heads of all five authorized local destinations. Fresh complete title listings used `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for notes, reference, agent-memory-systems, agentic-systems, and sources. Large listings were read in complete consecutive sorted segments. The snapshot has no tags; no tag-completeness shortcut applies. Also read the evaluation topic head.
- Description prospecting used `rg -l -i 'dense reward|partial credit|premature|stopping judgment|long.horizon' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | xargs -r rg '^description:'`. It surfaced the diagnostic-richness and autonomy-measurement notes, trajectory evaluation proposal, long-running harness report, and Traverse paper.
- Notes: read diagnostic richness, oracle strength, final-task/path health, and autonomy measurement. Kept the first two as named comparisons. Rejected autonomy measurement because the paper measures fixed-budget task completion, not comparable actor allocation. Rejected final-task/path health as direct evidence: the graders inspect final subtask state, not recovered primary-path failures.
- Reference: the same description scan plus `rg -n -i 'dense|diagnos|partial|timeout|premature' kb/reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md` led to a full proposal read. Kept the proposal as a practical comparison between final-state subtasks and chronological process compliance.
- Sources: the same focused body query over `effective-harnesses-for-long-running-agents.ingest.md` and `locating-hidden-failures-paper.ingest.md` led to full reads. Kept both on stopping/verification and failure-observation axes.
- Agent-memory-systems and agentic-systems: title/description scans and the same focused body query over `reviews/scroll.md` and `reviews/ai-agent-book.md` produced only broad runtime/evaluation overlap. No specific source finding tests those systems; no system edge retained.
- Link following: diagnostic richness → oracle strength and final-task/path health → diagnostic richness exposed why diagnostic discrimination and causal identification must remain separate. Traverse → trajectory-aware evaluation exposed the final-state versus chronological-evidence distinction. The long-running harness ingest's existing state/verification links were evaluated without treating its bundled remedy as tested by LHTB.
- External: only the already supplied paper URL is proposed; no external discovery. Instructions and work are excluded by the source contract. Candidate paths checked before writing.

## Connections Found

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **compares-with**: LHTB's deterministic subtask scores distinguish zero progress, near misses, and false finishes; the note explains why richer proposal evidence is distinct from winner selection. LHTB improves diagnosis resolution without testing later learning quality.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — **compares-with**: a strict pass threshold and dense subtask score can use the same deterministic oracle yet differ in discrimination. This helps separate checker correctness from the amount of progress information exposed.
- [Effective harnesses for long-running agents](../../../../sources/effective-harnesses-for-long-running-agents.ingest.md) — **compares-with**: both report premature completion after partial progress; the practitioner source supplies explicit progress ledgers and end-to-end checking as candidate interventions, while LHTB supplies a possible evaluation setting rather than validating those interventions.
- [Locating Hidden Failures](../../../../sources/locating-hidden-failures-paper.ingest.md) — **compares-with**: LHTB distinguishes partial completion and termination causes through final-state scoring; Traverse distinguishes local trajectory errors and unsafe actions. Their observation surfaces answer different reliability questions.
- [Trajectory-aware evaluation proposal](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: deterministic subtask checks are a concrete intermediate option when a workflow needs progress measurement, while the proposal's ordering, isolation, and process-compliance questions still require chronological evidence.
- [Original paper](https://arxiv.org/abs/2607.08964) — **derived-from**: primary external source for the eventual ingest.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None. No currently loaded theory claim directly acquires causal support from this descriptive benchmark comparison; its strongest uses are comparison and experiment design.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Measuring autonomy](../../../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — fixed-budget completion rates do not resolve the note's cross-system actor-allocation measurement problem.
- [Final task success and intended-path health](../../../../notes/final-task-success-does-not-establish-intended-path-health.md) — final-state subtasks do not expose whether the intended execution route failed and was replaced by a fallback.

## Index Membership

None. The eventual ingest belongs in sources; an evaluation-note index entry would require a separate authored claim.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Author connections in the matching ingest, never in the immutable snapshot.
- The paper's nine-category summary conflicts with a 21-category statement in section 2.4. Figure 4 gives 50 passes among 782 runs, whereas section 3.4 uses 660 unresolved runs; these numbers do not form one reconciled denominator.
- Dense grading is computed from the final container state. Do not describe it as online process reward delivered to agents or as proof of the causal bottleneck.
- Most models use Terminus-2; GPT-5.3 uses Codex. The apparent shared-harness comparison has this stated exception.
