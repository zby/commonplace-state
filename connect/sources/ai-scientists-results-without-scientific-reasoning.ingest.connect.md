---
description: "Post-ingest Corral connections: measuring evidence uptake without mistaking annotation absence for non-use"
type: kb/reports/types/connect-report.md
source: kb/sources/ai-scientists-results-without-scientific-reasoning.ingest.md
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: AI Scientists ingest

**Source:** [Accepted Corral ingest](../../../../sources/ai-scientists-results-without-scientific-reasoning.ingest.md)

## Discovery Trace

- Read the accepted ingest fully and its pre-ingest discovery. Sources and notes contracts and connect-report type were read in this run; all five authorized destination README heads and the evaluation head supplied routing context.
- Generated the fresh complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`, filtering `activation|trajectory|reasoning.*evaluat|experiment identifies|autoresearch|scientists`. Ran `rg -n 'Corral|epistemic.graph|evidence non.uptake'` over those collections. Exact body hits were concentrated in the accepted ingest.
- Notes: read the contextual-activation note and experimental-contrast argument. The former distinguishes exposure from behavior and already cautions that process proxies do not prove semantic incorporation. This makes Corral useful as a measurement boundary, not a causal estimate of non-use.
- Reference: read the trajectory-aware evaluation proposal, including its AutoResearchEval discussion, adjudication, false-positive tests, and adoption conditions. Its authored comparison supports the specific experimental destination without assuming trajectory access is automatically beneficial.
- Sources: the title pass surfaced AutoResearchEval; the proposal's existing source discussion supplies the same comparator and already bounds artifact-access attribution, so no redundant source edge was needed. Agent-memory and agentic-systems: no cross-task retention or specific runtime intervention is present, so generic memory/harness edges were rejected.
- Followed the activation note's links and the proposal's process-evaluation neighborhood at their authored context level. No external prospecting. Workshops and instructions were excluded. Inbound candidate assessed under the notes contract's `evidenced-by` authorization.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: Corral makes visible evidence-to-judgment linkage a separate measurement, while its omitted uncertain edges and source inconsistencies limit any inference from missing linkage to non-use.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **is-evidence-for**: similarity between two minimal action interfaces cannot settle the effects of excluded planners, retrieval, durable memory, or multi-agent criticism.
- [Trajectory-aware evaluation proposal](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) — **see-also**: its calibrated route-assessment experiment can add hypothesis–contradiction–revision cases, with missing-edge false positives and later reuse measured separately.

## Bidirectional Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → accepted ingest — **evidenced-by**: a source-specific paragraph could contrast evidence exposure with annotated uptake and demonstrate why proxy validation is required. The source cannot establish that every missing graph edge is absent behavioral use; retain that qualification beside the citation.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- Process/output independence: observing both endpoints and traces does not independently manipulate the two prescriptions.
- Persistent reflective-memory failure: prefix replay also reconstructs environment state and is not a cross-task lesson-retention intervention.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Preserve conflicting prevalence and variance decompositions instead of presenting one unambiguous population estimate. Trace analysis covers 626 ReAct-only traces, not all 25,000-plus runs.
- No library links were authored. Source-dependent use needs retained quotes or a snapshot-required link.
