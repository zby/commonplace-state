---
description: "Candidate connections from ABA benchmark auditing to specification diagnosis, evaluator validity, and trajectory evidence"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/automated-benchmark-auditing-ai-agents-llms.md
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: Automated Benchmark Auditing for AI Agents and Large Language Models

**Source:** [Automated Benchmark Auditing for AI Agents and Large Language Models](../../../../sources/.snapshots/automated-benchmark-auditing-ai-agents-llms.md)

The snapshot was read in full. All outbound recommendations belong on its future matching ingest, never on the immutable snapshot. Reverse citations must also target that tracked ingest after it exists, with quotes or the snapshot-required marker appropriate to the eventual claim.

## Discovery Trace

- Read the sources collection contract and report type before prospecting. Permitted local destinations are notes, reference, agent-memory-systems, agentic-systems, and sources. Instructions and work are excluded. No external search was performed; the paper's source URL is already known.
- Read the five destination README heads and the notes evaluation tag head. The snapshot has no tags, so no source-tag lookup or complete-tag shortcut applied.
- Generated the fresh full title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The combined output was truncated, so repeated it with `| sed 's/.*:# /# /'` to inspect the compact claim-title surface.
- Searched description candidates with `rg -n '^(description:.*(evaluat|benchmark|audit|oracle|specification|verif))'` over those five collections. This foregrounded exact implementation, debugging, diagnostic richness, semantic-gate calibration, SWE-bench Science, eval engineering, auto-harness, and AI Agents in Depth. Large discovery outputs were used for candidate routing, followed by focused reads rather than treated as full artifact evidence.
- **Notes:** focused body query `rg -n 'benchmark|grader|underspecif|trajectory'` over the four retained note candidates. Read each fully. Followed exact implementation to commitment-created ground truth, and debugging to three-way output diagnosis. The author/executor note adds a particularly direct hidden-acceptance-condition case; the broader diagnosis note overlaps the more operational debugging destination. Retained four bounded relationships below.
- **Reference:** body query `rg -n 'benchmark|rubric|calibrat|oracle'` included the calibration proposal; read its substantive proposal text. Its distinction between known-case detection and field calibration makes it a useful adjacent companion for ABA's PR overlap and sampled finding confirmation. No claim that ABA validates Commonplace's gates is proposed.
- **Agent-memory-systems:** the same body query inspected auto-harness's trace access, train/test separation, and promotion gates. Rejected the connection: score optimization has a relevant vulnerability, but ABA does not evaluate this implementation, and the generic oracle warning is better carried by the exact-implementation note.
- **Agentic-systems:** the same query inspected AI Agents in Depth's evaluation material, verifier distinctions, and chapter-level comparison. Rejected this broad whole-book match because the notes provide a more direct route without importing unrelated system characterization. No narrower system analysis was identified by the head/title scan.
- **Sources:** the same query inspected SWE-bench Science, eval engineering, and scientific-review automation. Read SWE-bench Science and eval engineering fully. Followed SWE-bench Science's existing links back to exact implementation and diagnostic richness; this confirms an existing source-to-theory cluster rather than requiring a new broad synthesis. Retained the two named comparison axes below. Scientific-review automation was rejected as a weaker task-domain analogy.
- **External:** no prospecting; retained only the original paper as the known derivation source. Website and code links describe additional material, but neither was inspected and no code-grounded claim is proposed.
- Read the notes outbound rules for the reverse candidate. Paths in this report were checked before validation.

## Connections Found

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **is-evidence-for**: ABA's narrow, broad, and misaligned graders supply benchmark cases where executable conformance can diverge from the stated task objective. This bears on the distinction, not on the correctness of every ABA flag or the general prevalence of bad oracles.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — **is-evidence-for**: the human-aligned QEMU case requires a hidden socket path, transport, and protocol that competent execution cannot infer from the authorized prompt. It concretely illustrates an omitted acceptance condition rather than legitimate implementation discretion.
- [LLM debugging separates specification gaps, instruction violations, and run-to-run variation](../../../../notes/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — **compares-with**: both distinguish task/specification faults from agent mistakes; ABA adds environment and grader inspection to that diagnostic problem. ABA's three categories must not be equated with the note's three diagnostic relations, and it does not estimate sampling variation through controlled reruns.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: ABA's static-versus-trajectory comparison shows that supplying execution traces changes which benchmark defects are surfaced. This supports the narrower evidence-access mechanism; ABA does not test whether these diagnoses improve subsequent revisions or isolate an optimal context policy.
- [Calibrating semantic gates against labelled fixtures](../../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — **see-also**: independent maintainer fixes, incomplete gold sets, and manual confirmation illustrate why known-defect recovery and confirmation of flagged findings cannot establish population false-negative rates. The proposal remains unadopted and targets KB gates rather than benchmark tasks.
- [SWE-bench Science full paper](../../../../sources/swe-bench-science-arxiv-2608-19799.ingest.md) — **compares-with**: SWE-bench Science separates public test success from hidden scientific correctness; ABA asks whether the task and its hidden or visible grader are themselves fair and aligned. Together they expose two distinct places where benchmark scores can mislead without assuming hidden tests are automatically authoritative.
- [Towards Automating Eval Engineering](../../../../sources/towards-automating-eval-engineering-2079976006644072796.ingest.md) — **compares-with**: both inspect instruction, environment, and verifier evidence alongside trajectories. The announcement constructs evals from production failures with user input, while ABA audits existing benchmark tasks and reports cross-benchmark findings with partial external validation.
- [Original ABA paper](https://arxiv.org/abs/2605.26079) — **derived-from**: the retained observation supplies the ingest's source-side claims and reported results.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → future tracked ingest — **evidenced-by**: consider a body-level QEMU example grounding why hidden acceptance choices must be disclosed or the grader relaxed. The source's human-aligned case supports this narrow claim; it does not validate the note's entire delegation framework. Read and retain the necessary source support before authoring the edge.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) — benchmark-driven promotion is a plausible consumer of auditing, but no source evidence ties ABA to this implementation; the theoretical oracle distinction is the better destination.
- [AI Agents in Depth](../../../../agentic-systems/reviews/ai-agent-book.md) — its evaluation chapter overlaps, but the whole-system review is a less precise route than the directly relevant theory notes.
- [LLM output deviation requires three-way diagnosis](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) — valid conceptual proximity, but the operational debugging note is more immediately useful and avoids duplicating the same route.
- [Towards Automating Scientific Review with Google's Paper Assistant Tool](../../../../sources/towards-automating-scientific-review-google-paper-assistant.ingest.md) — shares agentic criticism and validation concerns, but scholarly-review task decomposition is less specific than the eval-engineering comparison.

## Index Membership

None

## Synthesis Opportunities

None. The existing exact-implementation and diagnostic-richness notes already provide the principal higher-order claims.

## Maintenance Observations

None

## Flags

- Keep reported findings distinct from independently established defects. Static audits flag 25.7% of 34,285 tasks as Major; validation samples do not establish that corpus-wide proportion as ground truth.
- The source's static Major manual-review sample is internally inconsistent: section 4.3 and Table 3 report 56, while Appendix D.3 says 54. Prefer attributing Table 3 explicitly and preserve the discrepancy.
- Appendix C.4 says every audit used Opus 4.7, while section 4.2 and Table 2 explicitly use Opus 4.6 for matched comparisons. Describe the exception rather than copying the blanket reproducibility claim.
- Appendix C.2 makes the collection mechanism more specific than a purely deterministic collector: an agent writes and executes a collector script whose outputs are subsequently validated. The standardized representation and deterministic ordering do not make the agent's acquisition/mapping decisions deterministic.
- Appendix E.2 presents outcome cross-tabs, not a controlled causal test proving the auditor independent of observed agent failures. Its nonzero passed-and-flagged cells rebut only the strongest failure-only explanation.
- Ranking changes after excluding flagged tasks are sensitivity analyses under stated exclusion rules. They neither demonstrate improved agent capability nor establish a uniquely corrected leaderboard. Preserve the distinction between percentage-point changes and relative percentages when copying results.
- The report crosses specification, diagnosis, and evaluator-validation topics. The snapshot is one immutable paper and should not be split; any later theory extraction should be scoped to separate claims rather than inherit all eight recommendations as one premise.
