---
description: "Pre-ingest connections for AHOIS: causal criticism, experimental state, and limits of scientific autonomy"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/socratic-agents-autonomous-scientific-discovery.md"
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: Socratic agents for autonomous scientific discovery

**Source:** [AHOIS snapshot](../../../../sources/.snapshots/socratic-agents-autonomous-scientific-discovery.md).

These are candidates for the matching ingest, not edits to the immutable snapshot. Produced under cp-skill-connect for pre-ingest discovery; model identity was not exposed to this worker.

## Discovery Trace

- Read the source collection contract and connect-report type before discovery. Permitted local destinations are notes, reference, sources, agent-memory-systems, and agentic-systems. Instructions and work are excluded. No external search was performed; the source's own arXiv URL is already known.
- Read the destination README heads and the notes learning-theory head. The snapshot has no tags, so there was no matching source-tag traversal or complete-tag shortcut. No semantic search or scores were used.
- Generated titles with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`; the broad output exceeded the tool display budget. Repeated the notes title scan and supplemented it with focused descriptions. This is standard discovery with a display-limited complete-title pass, not a claim of exhaustive candidate review.
- Scanned descriptions with `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | rg -i 'scientific|falsif|critic|hypothes|independent|theory builder|experiment'`. Notes surfaced explanatory-reach, diagnostic richness, autonomy definitions, and experimental attribution. Sources surfaced AutoRA, MDA, the scientific-method perspective, and FALSIFYBENCH. Read the selected claim and ingest bodies to separate mechanism comparisons from stronger evidence claims.
- Ran `rg -n -i 'socratic|falsification|causal.probing|scientific state' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Sources supplied direct inquiry-loop comparisons. Reference hits concerned unrelated proposal and schema policy, so none justified an outgoing reference edge. Agent-memory hits concerned harness debugging and benchmark selection, which are broader analogies than the direct scientific sources. Agentic-system titles and README entries did not identify a comparably direct physical-discovery system; none retained.
- Followed the learning-theory head to explanatory-reach; followed the diagnostic-richness neighborhood to its oracle-strength distinction; followed the autonomous-theory-builder definition to the external-outcome boundary. AutoRA and MDA connect the shared-state and intervention-selection mechanisms without implying that their fixed decompositions match AHOIS.
- Rejected turning every five-agent architecture resemblance into a memory or orchestration connection. The paper reports shared experimental state and logs, but does not establish long-term memory admission, cross-task transfer, or self-revision of the five-agent machinery.

## Connections Found

- [First-principles reasoning selects for explanatory-reach](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — **is-evidence-for**: AHOIS reports a comparison of a Socratic critic with a generic reviewer, a non-Socratic critic, and no reviewer. Its causal probing and counterexamples provide a bounded experimental case for making premises and failure conditions criticizable. This does not establish general explanatory reach or isolate all four questioning operations.
- [Autonomous theory builder](../../../../notes/definitions/autonomous-theory-builder.md) — **compares-with**: the paper's epistemic-autonomy claim can be assessed against the KB's role boundary. Human correction of interpretations and scientific reasoning remains material; pilot acquisition and researcher-run bulk acquisition must also be reported separately.
- [Externally tested theory builder](../../../../notes/definitions/externally-tested-theory-builder.md) — **compares-with**: physical measurements provide consequences beyond linguistic agreement, while human and agent interpretation still determine their significance. The distinction helps prevent treating hardware access as sufficient evidence that all three external-interface requirements are met.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) — **compares-with**: AHOIS records hypotheses, assumptions, expected observations, uncertainties, actions, and acquired results, and distinguishes calibration, detector, and modality failures. This is a concrete diagnostic-state comparison, not a controlled test of retaining those fields.
- [AutoRA](../../../../sources/autora-automated-research-assistant.ingest.md) — **compares-with**: both separate proposal, measurement, and inference over shared research state. AHOIS adds a constrained causal-questioning role and physical-integrity monitoring, allowing an operator to compare what is explicit in the interface and what remains supplied by people.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **compares-with**: both couple explicit hypotheses to intervention selection. MDA supplies formal Bayesian selection in authored simulator domains; AHOIS relies on natural-language causal interrogation and real optical measurements. Their evidence and representation boundaries differ.
- [LLMs in the scientific method](../../../../sources/llms-scientific-method-hypothesis-to-discovery.ingest.md) — **compares-with**: AHOIS is an implemented physical-loop case for the perspective's hypothesis–experiment–observation agenda, with measured outcomes but continuing human supervision and a known physical domain.
- [Original paper](https://arxiv.org/abs/2606.26722) — **derived-from**: source identity for the future ingest analysis.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md): useful as an assessment discipline, but a direct outgoing edge adds less than stating the missing budget, evaluator, and ablation details alongside each result.
- [Agent memory collection](../../../../agent-memory-systems/README.md): shared state alone does not establish persistent memory learning; broad collection linkage would conceal the missing mechanism.

## Index Membership

None. The eventual ingest remains a source record, not a new system analysis or tagged theory note.

## Synthesis Opportunities

None. The existing explanatory-reach, diagnostic-state, and autonomy distinctions already express the useful abstractions; the new material supplies a bounded comparison case.

## Maintenance Observations

None

## Flags

- The paper explicitly leaves the underlying model configuration, prompts, permissions, trajectories, and several statistical details to Supplementary Information. The present snapshot contains the main paper, not those supplements. Do not infer the fixed-model configuration or budget matching from silence.
- Natural-language criticism of physical hypotheses is demonstrated more directly than reflective revision of the agent system's own machinery. These are distinct learning claims.
- The paper states that humans can correct hardware-incompatible plans and uncertain interpretations; Figure 5 also assigns supervision factual correction and convergence guidance. Preserve these qualifications beside the autonomy claim.
- The report offers more than five local edges, but they remain within scientific-inquiry methodology and its evaluation boundary. It does not recommend splitting the immutable source or drafting multiple ingests.
