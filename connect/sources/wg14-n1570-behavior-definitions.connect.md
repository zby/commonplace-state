---
description: "Connection candidates for N1570's bounded behavior definitions and the KB's reference-governed semantics claims."
type: types/connect-report.md
source: kb/sources/.snapshots/wg14-n1570-behavior-definitions.md
source_has_frontmatter: true
date: "2026-11-02"
depth: standard
---

# Connection Report: WG14 N1570 behavior definitions

**Source:** [N1570 sections 3.4.1–3.4.4](../../../../sources/.snapshots/wg14-n1570-behavior-definitions.md)

## Discovery Trace

The source collection's outbound rules authorize theory, reference, other sources, historical agent-memory accounts and current agentic accounts. Tag heads are navigation inputs, not an authorized outbound destination. The external PDF is already supplied; no external prospecting was performed. The immutable snapshot's prospective authored surface is its name-paired ingest.

- Read `kb/sources/COLLECTION.md`, `kb/types/connect-report.md`, the complete excerpt, and the theory collection's reverse-link rules. Read the theory, reference, sources, tags, agent-memory-systems and agentic-systems landing READMEs.
- Generated and scanned complete first-H1 listings with `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`, the same query over reference and tags, and `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.ingest.md'`. The strongest titles concerned shared semantics, the conformance bracket and symbolic-form definitions. No other C-standard ingest appeared.
- Ran `rg -n 'unspecified|implementation-defined|undefined behavior|formal semantics|reference defect' kb/theory kb/reference --glob '*.md'`. Kept shared-semantics and conformance-bracket candidates because they explicitly distinguish permitted variation from implementation failure. Evaluated symbolic-form and codification definitions for the same distinction; their current wording is under revision, so do not take the old criterion as a source claim.
- Ran `rg -n 'N1570|undefined behavior|implementation-defined|formal semantics' kb/sources --glob '*.ingest.md'` excluding two unrelated newly untracked ingests from body reads. Evaluated Plotkin's SOS ingest after its description and full text: it is a comparison on formal specification versus implementation, not evidence for these C definitions. Rejected the ephemeral-software essay at description resolution because its topic is artifact durability, not behavior categories.
- Ran `rg -n 'implementation-defined|undefined behavior|N1570|locale-specific' kb/agent-memory-systems kb/agentic-systems kb/tags --glob '*.md' --glob '!memory-systems-table.md'`. No matches. Their landing contracts and subjects supply no system-specific C behavior connection. Skipped deeper historical/current external-system prospecting; a general word such as “unspecified” in an inventory is not a C-semantics connection.
- Scanned scoped descriptions for the kept theory definitions, shared-semantics and conformance notes, three-way diagnosis, execution-indeterminism note, Plotkin and ephemeral-software ingests, and ADR 124. Read the artifact-analysis, constraining and computational-model tag heads. Artifact-analysis is `complete: true`; no by-tag rg was needed. The heads supplied navigation to the semantics definitions, not a reason for an ingest-to-tag edge.
- Followed links from the conformance-bracket note to the diagnosis and execution-indeterminism notes. Read both. The diagnosis's compiler example is useful but peripheral; no automatic reciprocal link is proposed for it. Execution sampling is not what these definitions establish.

## Connections Found

- [Representational form](../../../../theory/definitions/representational-form.md) — **is-evidence-for**: bounds any equation of symbolic form with one required result; N1570 explicitly distinguishes several permitted possibilities from an absence of requirements.
- [Codification](../../../../theory/definitions/codification.md) — **is-evidence-for**: gives a concrete language-reference case in which implementation documentation supplies a choice without the language standard requiring one result for every instance.
- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) — **is-evidence-for**: supplies a source-side vocabulary for the note's claim that differing results can both conform when the reference permits variation.
- [Traditional software can bracket executor conformance](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) — **is-evidence-for**: qualifies its scope paragraph by separating undefined behavior, where this standard imposes no requirements, from actual compiler non-conformance.
- [The Origins of Structural Operational Semantics](../../../../sources/plotkin-origins-of-sos.ingest.md) — **compares-with**: mathematical transition-rule specification versus a committee draft's definitions of which choices are left to implementations or unconstrained. These are different specification surfaces, not rival definitions of the same concept.

## Bidirectional Candidates

None. Useful inbound evidence links are listed separately below; an outbound link alone does not justify reciprocity.

## Reverse-edge Candidates

- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) → the eventual name-paired ingest — **evidenced-by**: bounds the shared-semantics discussion with a concrete reference that allows differing results. This is definitional evidence, not an empirical conformance test.
- [Traditional software can bracket executor conformance](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) → the eventual name-paired ingest — **evidenced-by**: qualifies the undefined-behavior caveat; do not use the excerpt to infer actual compiler-bug rates.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Execution indeterminism](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md): C's permission to choose among possibilities is not evidence of a sampling mechanism or distribution.
- [The flawed ephemeral software hypothesis](../../../../sources/the-flawed-ephemeral-software-hypothesis.ingest.md): formal-semantics wording overlaps, but the artifact-durability argument gives no concrete reader need here.
- ADR 124: an execution decision already has its theoretical premises; adding a C-definition source would be weaker than linking the semantics claims themselves.

## Index Membership

None. Sources do not participate in tag completeness, and no new index entry is required by this bounded ingest.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

- Scope is an intentional excerpt of committee draft N1570 dated April 12, 2011, not the complete standard or a capture of the final published C11 text.
- The four section numbers include locale-specific behavior at 3.4.2. They do not establish a category called reference defect. No completeness claim about all C behavior categories follows from this excerpt.
