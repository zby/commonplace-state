---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/provably-bounded-optimal-agents.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Provably Bounded-Optimal Agents

**Source:** [Provably Bounded-Optimal Agents](../../../../sources/.snapshots/provably-bounded-optimal-agents.md)

## Discovery Trace

**Description listing scan:** Scoped description and H1 scans over notes, reference, source analyses, and external-system collections highlighted declared frames, deployed-system evaluation, and oracle scope.

**Topic indexes:** Read `kb/notes/tags-README.md`, the foundations entries it routes to, and external-system indexes; the result is theoretical rather than a system review candidate.

**Body search:** `rg -n -i "bounded optimal|resource.bound|architecture|environment|deployed system|oracle domain" ...` and the broader combined search found the three kept notes. `rg -l -i "resource.bound|warrant|closure" kb/notes` supplied negative checks.

**Link following:** Followed the deployed-system note into declared-scope and evaluation notes, and oracle-domain into verification boundaries. Candidates were retained only where architecture/environment relativity changes the evaluation claim.

## Connections Found

- [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: bounded optimality evaluates programs running on a specified architecture in an environment, directly supporting system-relative rather than ideal-reasoner evaluation.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **compares-with**: the paper's proofs cover explicit architecture and environment classes, paralleling the note's insistence that warranted conclusions remain within the evaluator's declared domain.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- **compares-with**: both require the assessed architecture, task environment, resource limits, and horizon to be part of the claim.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The deployed system, not the model, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → future ingest -- **external source support**: Russell and Subramanian supply the canonical architecture-and-environment-relative formalization.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Factory construction does not establish knowledge acquisition](../../../../notes/factory-construction-does-not-establish-knowledge-acquisition.md) -- rejected because bounded-optimality results assess program performance, not acquisition of knowledge.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Drafting should distinguish the paper's simple-machine/broad-real-time-environment construction and its separate asymptotic bounded-optimality results rather than generalizing to arbitrary agents.

