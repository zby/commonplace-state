---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/figma-agent-security-review-thread-2081739292859421118.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Thread by @frgx

**Source:** [Thread by @frgx](../../../sources/figma-agent-security-review-thread-2081739292859421118.md)

## Discovery Trace

**Description listing scan:**
- Read the curated heads for `kb/notes/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`, then scanned descriptions across `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`.
- Candidate notes retained after articulation: `raw-accumulation-does-not-create-usable-memory`, `constraining-during-deployment-is-continuous-learning`, `knowledge-storage-does-not-imply-contextual-activation`, and `agent-memory-requirements/evaluate-memory-by-effects`.
- Reviews were checked for adjacent system comparisons; no external-system review was specific enough to carry this source's Figma case as a primary connection.

**Topic indexes:**
- Read `kb/notes/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- The notes surface routed the source to agent-memory, context-engineering, learning-theory, and evaluation material; the external-system indexes supplied comparison context but no stronger target.

**Body search:**
- `rg -l -i "precision and recall|threat model|institutional knowledge|policy that catches|security review|agent review|precedent|latent vulnerabilities|auto.?fix"` over the permitted collections.
- Follow-up searches for `institutional knowledge`, `threat model`, `precision and recall`, `agent review`, `policy that catches`, and `security review` were evaluated against the source's concrete claims: precedent-writing, threat-model codification, daily testing, repo-wide auditing, and policy-driven remediation.

**Link following:**
- Followed the relevant notes' `Relevant Notes` sections to distinguish the ingress, constraining, activation, and evaluation claims. No additional target survived the articulation test.

## Connections Found

- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- **is-evidence-for**: the thread describes raw institutional security knowledge becoming usable only after it was shaped into generic precedents, a threat model, and a tested artifact used by several workflows.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) -- **is-evidence-for**: the Figma account is a concrete deployment case in which policy-like symbolic artifacts accumulated outside model weights and changed review, audit, and code-generation capacity.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: the source distinguishes merely writing down knowledge from making the artifact power agent review, repo-wide audits, and secure code generation, with daily testing as an activation check.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) -- **is-evidence-for**: the reported findings, bug corpus, and repeated testing make downstream security outcomes the relevant evidence rather than the existence of a policy document alone.

## Bidirectional Candidates

None. The source's strongest durable role is as evidence for existing theoretical claims; a reciprocal edge from the ingest report is sufficient if the report uses the case.

## Reverse-edge Candidates

- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) → source -- **evidenced-by**: the thread provides a concrete instance of ingress work adding handles, scope, authority, and repeated testing to accumulated institutional knowledge.
- [Constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) → source -- **evidenced-by**: the thread reports symbolic security precedents and policy as durable behavior-shaping artifacts in a deployed engineering workflow.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidenced-by**: the thread reports the artifact entering multiple action paths rather than remaining stored reference material.
- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → source -- **evidenced-by**: the thread names audit findings, eval-corpus composition, and daily testing as effects and evidence surfaces.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Figma's linked blog post and the quoted bug-bounty post were not prospecting targets: they are external URLs carried by the source, not already-captured local artifacts, and connect does not browse the open web.
- Individual agent-memory reviews matching generic terms such as `agent review`, `policy`, or `precision` were rejected because they describe different implementations and do not give an agent a concrete traversal benefit for this Figma case.

## Index Membership

- [Agent memory systems](../../../../agent-memory-systems/README.md) -- the source is a practitioner case about retained policy and agent activation, but it is not a review of an inspectable memory-system implementation; keep it in `kb/sources/` unless a later synthesis needs a lightweight comparison entry.
- [Context engineering](../../../../tags/context-engineering-README.md) -- the source contributes a concrete example of codified security knowledge being routed into multiple action paths.

## Synthesis Opportunities

The thread, [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md), and [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) jointly suggest a stronger worked case: ingress quality and downstream behavioral evaluation are coupled, because Figma's useful artifact emerged through precision work and earned trust through repeated operational testing. This is a possible future synthesis, not a new claim created by connect.

## Maintenance Observations

None.

## Flags

- The source is a multi-claim practitioner thread. If promoted beyond source-only evidence, split the security-policy case from the bug-bounty/evaluation case rather than treating the whole thread as one general mechanism.
