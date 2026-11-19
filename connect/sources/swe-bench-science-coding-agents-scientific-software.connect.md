---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/swe-bench-science-coding-agents-scientific-software.md"
source_has_frontmatter: true
date: "2026-08-25"
depth: standard
---

# Connection Report: SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?

**Source:** [SWE-bench Science: Can Coding Agents Resolve Engineering Tasks in Science?](../../../../sources/.snapshots/swe-bench-science-coding-agents-scientific-software.md)

## Discovery Trace

**Source contract and scope:**
- Read `kb/sources/COLLECTION.md`. The snapshot is immutable, so the matching ingest is its authored connection surface. Authorised local destinations are `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`; `work` and `instructions` are excluded. The useful labels for this pass are `is-evidence-for` and `compares-with`.
- Read the complete snapshot. Its main candidate-bearing assertions are the public/private-test distinction, four audited failure mechanisms, and the paired scientific-guidance ablation. The snapshot contains the paper abstract followed by an AlphaXiv `AI Overview`, so claims outside the abstract have a capture-fidelity limitation.

**Curated heads and title surfaces:**
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/notes/evaluation-README.md`, `kb/notes/llm-reliability-README.md`, `kb/notes/context-engineering-README.md`, and `kb/notes/failure-modes-README.md`. The evaluation, reliability, and context-to-action clusters produced the strongest prospects.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for all five authorised local destinations: 360 titled Markdown artifacts in notes, 144 in reference, 173 in agent-memory-systems, 12 in agentic-systems, and 302 in sources at the time of discovery.

**Description listing scan:**
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` across each authorised destination, yielding 357 note descriptions, 143 reference descriptions, 171 agent-memory-system descriptions, 10 agentic-system descriptions, and 302 source descriptions.
- Ran `rg -n -i '^description:.*(scientific|benchmark|evaluation|oracle|hidden test|repair|guidance|anchoring|context contamination|irrelevant context|generaliz)' kb/notes/ --glob '*.md'`. Kept the exact-implementation, contextual-activation, context-contamination, and diagnostic-richness notes; rejected generic oracle and retained-memory matches whose claims did not touch scientific repair or guidance uptake.
- Ran the analogous focused description queries over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` using `(scientific|benchmark|evaluation|repair|guidance|context|coding agent|agent reliability|hidden)`. Source comparisons survived; no agent-memory or whole-agentic-system artifact passed the articulation test.

**Body search:**
- `rg -n -i 'visible tests|public tests|private tests|hidden tests|surface[- ]level|overfit|generaliz(e|ation)|repair coverage' kb/notes/ kb/sources/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` — surfaced local-conformance, held-out-test, and transfer candidates.
- `rg -n -i 'anchoring|misaligned guidance|scientific guidance|auxiliary information|guidance.*(hurt|harm|worse)|context contamination|irrelevant context' ...` — kept the contextual-activation and context-contamination notes plus the Agents Explore and GSM-DC sources; GSM-DC was ultimately rejected because controlled irrelevant distractors are less specific than the solution-integration comparison.
- `rg -n -i 'scientific software|scientific coding|coding agents?|repository-level.*(repair|engineering)|software repair|executable (engineering )?context|execution feedback' ...` — kept Harness-IF, SlopCodeBench, DiscoverPhysics, and CRUX as named-axis comparisons.
- `rg -n -i 'tests?.*(requirement|objective|decomposition)|requirement.*tests?|oracle.*(public|private|hidden)|knowledge.*(loaded|context|action)|context.*knowledge' ...` — confirmed the exact-implementation and contextual-activation articulations.
- `rg -n -i 'scientific contract|scientific invariant|scientific knowledge|science.*software|software.*science|private test|public test|held-out.*test|black-box tests' ...` — found no pre-existing source or note that already owns the paper's specific scientific-software contract claim.

**Link following:**
- Read the complete candidate notes [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md), and [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md), then followed their one-hop neighborhoods through the exact-implementation, oracle, process-vs-output, soft-degradation, and fixed-decomposition notes.
- Read the complete comparison ingests for [Agents Explore but Agents Ignore](../../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md), [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md), [SlopCodeBench](../../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md), [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md), and [CRUX shadow evaluation](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md). Each supplies a distinct comparison axis rather than keyword adjacency.
- Read `kb/notes/COLLECTION.md` before proposing return edges. Its `evidenced-by` label authorises the note-to-source direction.

## Connections Found

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) — **is-evidence-for**: public tests check visible engineering behavior while private tests target broader scientific correctness, giving a repository-level instance of local conformance failing to settle the requirement-to-objective link.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: the scientific-guidance ablation separates information being supplied from correct uptake and downstream benefit; guidance can fail to improve exact repair and can steer agents through anchoring.
- [Context contamination operates below an agent's compliance reasoning](../../../../notes/context-contamination-operates-below-an-agents-compliance-reasoning.md) — **compares-with**: both sources report unwanted steering from loaded content, but SWE-bench Science concerns alignment of task guidance and does not test explicit detection or refusal, so it is a boundary comparison rather than direct evidence for below-compliance influence.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **is-evidence-for**: the paper begins from aggregate task success being diagnostically coarse and gains information by auditing failures into four mechanisms; this supports the diagnostic-insufficiency half of the note without testing a subsequent learning loop.
- [Agents Explore but Agents Ignore](../../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental.ingest.md) — **compares-with**: solution injection shows context-to-action non-use, while SWE-bench Science reports that domain guidance can be useful, inert, or actively anchoring; together they separate presence, uptake, direction, and benefit.
- [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) — **compares-with**: both are coding-agent benchmarks that preserve failures hidden by aggregate task pass, but Harness-IF decomposes atomic rule compliance across instruction surfaces while SWE-bench Science decomposes scientific-repair failures and public/private correctness.
- [SlopCodeBench](../../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.ingest.md) — **compares-with**: both use held-out black-box checks to expose defects ordinary task success misses; SlopCodeBench stresses evolving maintainability across checkpoints, whereas SWE-bench Science stresses scientific invariants and repository integration across real scientific projects.
- [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — **compares-with**: the benchmarks isolate different meanings of scientific competence—law discovery in counterfactual worlds versus maintenance and repair of real scientific software—and therefore offer complementary oracle and failure surfaces.
- [Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) — **compares-with**: CRUX tests autonomous research engineering plus open-ended judgment, while SWE-bench Science tests bounded repository repair; their failure taxonomies help distinguish scientific software execution from project-level scientific judgment and backtracking.

## Bidirectional Candidates

- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) ↔ source — **evidenced-by**: a future note edit could cite the paper's public/private-test separation as a bounded scientific-software instance, while preserving the distinction between visible conformance and scientific validity.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) ↔ source — **evidenced-by**: a future note edit could use the guidance ablation to sharpen the final rung from behavioral uptake to beneficial, correctly directed uptake.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) ↔ source — **evidenced-by**: a future note edit could use the paper's aggregate-score critique and failure audit as bounded evidence for diagnostic granularity, without claiming that the paper tested outer-loop improvement.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [How Is LLM Reasoning Distracted by Irrelevant Context?](../../../../sources/gsm-dc-llm-reasoning-distracted-irrelevant-context.ingest.md) — rejected because controlled irrelevant distractors and poorly aligned scientific guidance are not the same intervention; Agents Explore provides the more discriminating uptake comparison.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — relevant methodological caution, but the AlphaXiv capture does not expose enough of the paired ablation design to make a specific source-side connection beyond a generic reminder.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — the four failure mechanisms imply trajectory inspection, but this capture does not state a trajectory-aware judging protocol or the output-only comparison the proposal requires.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) — both involve coding benchmarks and failure evidence, but Meta-Harness is a retained trace-driven harness-learning system; SWE-bench Science evaluates fixed agent configurations and does not establish a memory or harness-evolution pathway.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — repository engineering is shared subject matter, but no particular execution-loop, orchestration, or control-surface mechanism is common enough to help traversal.

## Index Membership

None

## Synthesis Opportunities

The guidance result, Agents Explore, and the contextual-activation note together suggest a four-stage evaluation ladder: information is present, it is consulted or behaviorally taken up, its influence is correctly directed, and downstream performance improves. The existing [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) already states essentially this ladder, so the appropriate action is bounded evidence integration rather than a new synthesis note.

## Maintenance Observations

- The local reading copy is an AlphaXiv abstract page plus an `AI Overview`, not the full paper. Exact benchmark construction, model labels, failure counts, and the scientific-guidance ablation should not be promoted into load-bearing claims without capturing and checking the primary paper PDF or another author-controlled full-text source.

## Flags

- Potential downstream split: benchmark construction, the four failure mechanisms, and the guidance ablation are independent result clusters. The ingest should preserve them separately; any later note promotion should avoid collapsing them into one broad claim about scientific coding agents.
