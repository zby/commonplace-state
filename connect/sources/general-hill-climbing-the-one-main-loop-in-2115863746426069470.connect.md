---
description: "Connection discovery for Miessler's General Hill-Climbing: specification fidelity, evaluator revision, and limits of monotone search"
type: types/connect-report.md
source: "kb/sources/.snapshots/general-hill-climbing-the-one-main-loop-in-2115863746426069470.md"
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: General Hill-Climbing: The One Main Loop in AI

**Source:** [General Hill-Climbing](../../../../sources/.snapshots/general-hill-climbing-the-one-main-loop-in-2115863746426069470.md)

The source proposes purpose → task-specific ideal-state articulation → evaluation → construction → iteration. Its distinct assertions concern intent capture, measurement, score-based candidate selection, and revising both goals and evaluators. It is a practitioner conceptual essay, not an experiment establishing universal applicability or the prevalence of specification failures.

All edges below are candidates. The snapshot is immutable. Outbound candidates belong on a future name-paired ingest; no such ingest existed during this pass. Durable inbound citations must also wait for that ingest and must never target the local snapshot.

## Discovery Trace

**Setup and authorisation:**
- Read the complete source, sources collection contract, reports collection contract, connect-report type and schema. Sources permits theory, reference, agent-memory-systems, agentic-systems, tags, and other sources; instructions and work are excluded. Tags is a prospecting destination but has no corresponding authorised outbound label. External authorisation applies only to targets already in hand.
- Read theory's collection contract for reverse-edge authorisation. Its `evidenced-by` may qualify or bound a claim; a conceptual essay is not automatically corroborating evidence.
- No agents, external searches, semantic-search services, or MCP tools were used.

**Curated heads and title surfaces:**
- Read `README.md` in all six local destinations. Theory routes through tags; reference separates shipped-system explanations from transferable claims; the two system landings distinguish frozen historical reviews from current accounts; sources explains the snapshot/ingest split.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each destination: theory 432 entries, reference 237, agent-memory-systems 175, agentic-systems 148, tags 34, sources 556. The combined display exceeded the tool output limit; inspected the theory title surface and reran filtered title queries for reference, both system collections, and tags using `rg -i 'goal|eval|improv|harness|intent|control'`. This is a standard selective pass, not a claim to have read every listed document.
- Read the improvement-loop and evaluation tag heads. The first supplies search/evaluation/retention and diagnostic-quality candidates; the second supplies evaluator validity and experiment-scope cautions. The source has no tags, so no source-tag membership search was required. No by-tag search was run for the `complete: true` improvement-loop head.

**Description scans and body queries, by destination:**
- For each of the six destinations ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'eval|ideal state|hill.climb|objective|specification|feedback|improvement.loop|optimization|telos'`. Selected theory candidates distinguish specification fidelity from execution, and objective revision from proxy revision. Sources yielded Weco's evaluator guidance and practitioner calibration reports. Historical memory reviews yielded auto-harness. Reference yielded control-plane goals and a repository loop trace; these are less useful than transferable theory for this source. Agentic-system descriptions yielded benchmark and archived runtime analyses, without a distinctive TELOS or ideal-state match.
- For every destination ran `rg -n -i 'hill.climb|ideal.state|TELOS' kb/<destination>/ --glob '*.md'`. Theory returned the verifiability gradient; sources returned FORTE's local-maxima discussion and DGM's explicit departure from hill-climbing. Other destinations had no matches. DGM was kept because it supplies a concrete alternative to retaining only score improvements; FORTE was not promoted because its specialised repair setting adds less than DGM here.
- For every destination ran `rg -n -i 'judge calibration|specification.*intent|cheap.*check|eval.*revision|local (maximum|optima)|scor.*user' kb/<destination>/ --glob '*.md' | head -35`. These bounded displays were used as a supplementary pass, not exhaustive body recall. Sources highlighted evaluator validity and practitioner diagnosis; the system archives mostly returned case-specific route records. Those archival hits were not promoted merely for mentioning scores or revisions.

**Candidate reads and link following:**
- Fully read the proposal-selection loop, debugging triage, objective-revision, evaluation-comprehension, exact-implementation, and specification-strategy notes, Weco's good-eval ingest, DGM's ingest, and the auto-harness review.
- Followed the loop note's evaluator discussion to its oracle-quality neighborhood, then used the evaluation head to select the comprehension gate. This distinguishes having an evaluator from demonstrating that it discriminates.
- Followed Weco's explicit connection to exact implementation versus objective validity and read that note. It explains the source's all-evals-pass-but-still-wrong case without treating dissatisfaction as a complete diagnosis.
- Followed the comprehension note to specification strategy and read it. This qualifies the source's heavy upfront-articulation posture when understanding only emerges through execution.
- Checked the name-paired ingest path: absent. Candidate files linked below were checked to exist. No numeric similarity scores were produced by these repo-local searches.

## Connections Found

These recommendations are for the future ingest's authored surface, not edits to the snapshot.

- [Proposal-selection improvement loop](../../../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **compares-with**: the source's generate/test/keep-better cycle can be compared with search, reject-capable evaluation, and operative retention. The distinction prevents a general work loop from being mistaken for demonstrated improvement of the system's own machinery.
- [LLM debugging separates specification gaps, instruction violations, and variation](../../../../theory/llm-debugging-starts-with-retry-versus-rewrite-triage.md) — **compares-with**: the source foregrounds incomplete intent capture; the target supplies separate checks for specification adequacy, executor conformance, and run-to-run variation. Readers gain a diagnostic alternative to assuming every disappointing result calls for more articulation.
- [Evaluation automation is phase-gated by comprehension](../../../../theory/evaluation-automation-is-phase-gated-by-comprehension.md) — **compares-with**: both require meaningful evaluators before optimization, but the target requires observed failure analysis and measured judge discrimination. This adds an operational prerequisite missing from the source's menu of evaluator types.
- [Revising an improvement objective is licensed from outside it](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **compares-with**: the source allows both ideal state and evals to evolve; the target distinguishes proxy repair, surfaced underspecification, and terminal-objective change. Readers can identify which kind of change an iteration actually made and what can assess it.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) — **compares-with**: the source prioritises thorough upfront ideal-state capture while conceding later discovery. The target explains when spec-first, live specification, or observation-based extraction can truthfully carry the missing knowledge; longer initial dictation is not a substitute for unavailable understanding.
- [Weco: How to Build a Good Eval](../../../../sources/weco-how-to-build-good-eval.ingest.md) — **compares-with**: both treat high scores that disagree with user judgment as a reason to reconsider evaluation. Weco separates fidelity, discriminatory signal, cost, and held-out checks, giving concrete dimensions for inspecting the source's proposed evaluator-revision step. Neither essay demonstrates autonomous evaluator criticism.
- [Darwin Gödel Machine](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) — **compares-with**: the source defines hill-climbing as keeping score improvements; DGM retains viable lower-scoring branches that can produce later improvements. Its reported greedy-parent ablation and stepping-stone lineages bound the claim that monotone local improvement is the universal search mechanism. This comparison does not establish equal-budget superiority or deny the broader usefulness of feedback loops.
- [auto-harness historical review](../../../../agent-memory-systems/reviews/auto-harness.md) — **compares-with**: the conceptual keep-better rule becomes an inspectable file guard, regression suite, best-score gate, and accepted executable agent in this reviewed system. The comparison also exposes what stays fixed: benchmark choice and outer-loop policy, plus a stochastic-score risk. Preserve the review's June 2026 source boundary; it is not evidence about current upstream behavior.
- [Original X post](https://x.com/DanielMiessler/status/2115863746426069470) — **derived-from**: a future ingest analyses this captured external source. The URL was already in the snapshot; no open-web discovery was performed.

## Bidirectional Candidates

None. No return link is recommended merely to mirror a comparison, and the immutable snapshot is never a durable backlink target.

## Reverse-edge Candidates

- [Exact implementation does not validate a requirement against its objective](../../../../theory/exact-implementation-does-not-validate-a-requirement.md) → future name-paired ingest — potential **evidenced-by**, as a qualifying conceptual case, not corroboration: the source explicitly describes an output passing every eval while still failing the user's judgment. A future writer could use it to illustrate the requirement–objective gap, while preserving the target note's warning to rule out integration and execution causes. This is conditional on a tracked ingest existing and adequate source support being retained; do not cite the snapshot or claim an experiment was run.

## Off-authorisation Candidates

- [Improvement-loop head](../../../../tags/improvement-loop-README.md) — its candidate-selection, rejection, and retention distinctions directly help classify the source's loop. Sources authorises scanning tags but provides no sources → tags label. Reject a formal head link for now rather than inventing `see-also`; the authorised link to the establishing theory note already serves the main need. Extend the contract only if direct source-to-head traversal becomes a deliberate collection policy.

## Raw Text Candidates

None.

## Rejected Candidates

- [Verifiability gradient](../../../../theory/verifiability-gradient.md) — the literal hill-climbing hit is relevant, but the evaluator-comprehension comparison gives a more discriminating next read than another broad statement that verifiable tasks admit iteration. Not retained in this selective report.
- [Control-plane goals](../../../../reference/control-plane-goals.md) — a possible analogy to TELOS, but a shipped KB inclusion frame is not a general personal-purpose artifact or a complete ideal-state specification. The README-level match does not warrant implying equivalence.
- [Tag-readme trace as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) — surfaced by descriptions and reference navigation; its repository-specific trace is not necessary once the general loop note and executable auto-harness comparison are available.
- Agentic-systems archived benchmark-route hits — not promoted from search excerpts. Their task-specific evidence/admission details do not, by themselves, supply a distinctive comparison with intent articulation or evolving evals. No candidate in that destination passed full-read promotion during this pass.

## Index Membership

None. Do not add the immutable snapshot to a library index. A future ingest may carry source-scoped topic tags after its own authoring assessment; sources is outside tag participating collections, so it would not become a generated head member.

## Synthesis Opportunities

None. The apparent synthesis—retain explicit intent, assess candidates, and revise inadequate checks—is already divided among the loop, specification-strategy, objective-revision, and evaluator-comprehension notes. No new higher-order claim was established here.

## Maintenance Observations

- The sources contract names tags as a discovery destination but supplies no authorised sources → tags label. This does not block discovery or theory links; see the off-authorisation disposition above.

## Flags

- **Authored-surface prerequisite:** the name-paired ingest is absent. Keep these recommendations in this report until a separately authorised ingest operation creates it. This connect run does not create that artifact.
- **Multi-claim/split signal:** the source reaches more than five notes across specification, evaluation, and search-control concerns. Preserve the snapshot whole; organise a future analysis by these independent assertions rather than treating the essay as one load-bearing premise. No library split is authorised here.
- **Unresolved tensions:** the source's broad claim that articulation is today's primary limitation is not prevalence evidence; its own later allowance for evolving ideal states qualifies the upfront-capture posture. Its monotone hill-climbing definition is narrower than feedback-driven search in general, as the DGM comparison shows.
- The source ends its experimentation paragraph abruptly after “The best thing about putting in the work on Ideal State and Evals is that you”. Treat that span as incomplete capture evidence, not an implied argument. No recapture or snapshot edit was attempted.
