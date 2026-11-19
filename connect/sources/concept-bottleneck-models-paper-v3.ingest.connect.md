---
description: "Post-ingest discovery distinguishing existing concept-bottleneck citations from new addressability and inspectability connection candidates"
type: kb/reports/types/connect-report.md
source: kb/sources/concept-bottleneck-models-paper-v3.ingest.md
source_has_frontmatter: true
date: "2026-09-18"
depth: standard
---

# Connection Report: Concept Bottleneck Models, accepted full-paper ingest

**Source:** [Concept Bottleneck Models, full v3 paper](../../../../sources/concept-bottleneck-models-paper-v3.ingest.md).

This standard repository-only discovery pass follows ingest acceptance and citation reconciliation. It was produced by GPT-6 under `cp-skill-connect`. It considers the current ingest with seven retained extracts, not the earlier snapshot-only report. All connection entries below are proposals, not new authored links.

## Discovery Trace

**Contracts and curated heads.** Reused the already-loaded connect-report type, source and reports collection contracts, notes collection contract, and base note type; read the ingest-report contract for this authored target. The five permitted destinations are notes, reference, agent-memory-systems, agentic-systems, and sources. Their README heads, plus the notes observability and learning-theory heads, were read during the immediately preceding snapshot pass and remain available as routing context. The ingest has `domains`, not `tags`; no matching source-tag sweep or completeness-mark skip applies. Instructions and work are excluded. No external prospecting was performed.

**Fresh title and description coverage.** Generated the complete title surface again for each permitted destination with `rg -N --no-heading -m1 '^# ' <destination>/ --glob '*.md'`, displaying compact titles through `sed 's/^.*:# /# /'`. Notes ran separately; sources, reference, agent-memory-systems, and agentic-systems ran together. Scanned path-bearing descriptions with `rg '^description:' kb/notes/ kb/reference/ kb/sources/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md' | rg -i 'concept|interven|opacity|inspectab|faithful|causal|bottleneck|readab'`. No ranking scores were available.

- **Notes:** read the current rationale-faithfulness note and the revised concept-bottleneck paragraph and footer in the theory-refinement note, including its final correction from “before” to “during” training. Read current explicit-retention, inspectable-artifact, opacity, and fixed-decomposition candidates. Followed explicit-retention's link to reflection/addressability; that neighbor concerns retained commitments and gives no better landing than the explicit-retention note. New candidates concern the operation and scope distinctions, not a claim that correcting concepts trains the model.
- **Sources:** the new title/description sweep shows both the full-paper ingest and the older superseded capture. Read the older ingest's current supersession notice and searched its remaining concept-bottleneck analysis. Reconsidered the already-read faithful-interpretability and causal-representation-learning ingests, with a fresh full read of the former. These are useful comparisons on explanation evaluation and world causality. Rejected treating the earlier capture as an independent evidence source or a missing inbound link.
- **Reference:** title/description coverage returned review-system and related generic evaluation material. Ran `rg -n 'concept bottleneck|concept accuracy|intervenability' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`; no matches. No reference artifact has a sufficiently specific relation to the concept-correction experiment.
- **Agent-memory-systems:** the same fresh title, description, and focused body coverage found no matching concept-interface mechanism. Generic memory repair or harness-edit workflows concern durable updates; they would obscure this source's per-inference limit.
- **Agentic-systems:** the same coverage found no candidate beyond generic runtime inspectability. No comparison passed the articulation test.
- **External:** the known versioned primary paper already has a `derived-from` edge in the ingest. No additional external edge is needed.

**Existing-edge audit.** Ran `rg -n 'concept-bottleneck-models-paper-v3|concept-bottleneck-models.ingest' kb/notes/ kb/sources/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`. Both the rationale-faithfulness and theory-refinement notes already cite the full-paper ingest in their bodies and footers. The superseded older ingest also links to it. These are existing paths, not missing inbound candidates. The accepted ingest already links to the rationale, explicit-retention, theory-refinement definition, and fixed-decomposition notes. Candidate-side searches for `interven|concept|correct` checked whether the proposed new comparisons were already expressed.

## Connections Found

- [Towards Faithfully Interpretable NLP Systems](../../../../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) — **compares-with**: distinguishes accurate explanation of a model's reasoning from useful correction of a supervised intermediate. This helps prevent interpreting the bottleneck intervention gains as proof of faithful historical explanation. Optional; the accepted ingest already states that limit without requiring another source.
- [Towards Causal Representation Learning](../../../../sources/towards-causal-representation-learning.ingest.md) — **compares-with**: separates interventions inside a predictive model from interventions on real-world causal variables. The concept-bottleneck paper explicitly permits useful concepts that do not cause the target in reality.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — **compares-with**: a supervised, editable activation layer inside a neural model qualifies a broad readable-versus-parametric contrast without making arbitrary weights individually interpretable.

## Bidirectional Candidates

- [Explicit retention provides direct targets for selective revision](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) → [full-paper ingest](../../../../sources/concept-bottleneck-models-paper-v3.ingest.md) — **evidenced-by**, authorized by the notes contract: add a bounded example distinguishing an instance-level edit target from a durable revised commitment. The ingest already links outward to this note; the proposed return path independently supplies a concrete operation profile. It must say that the correction changes a prediction and that learning from corrections is future work. This is the strongest new inbound candidate.

## Reverse-edge Candidates

- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) → [full-paper ingest](../../../../sources/concept-bottleneck-models-paper-v3.ingest.md) — **evidenced-by**: qualify substrate-wide language using a tested concept interface built into a neural computation. A useful citation requires a corresponding scope sentence distinguishing activations from weights; adding a footer alone would imply more agreement than exists.
- [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md) → [full-paper ingest](../../../../sources/concept-bottleneck-models-paper-v3.ingest.md) — **evidenced-by**: provide a concrete architectural affordance that makes selected neural intermediates inspectable despite opaque surrounding computation. This bears on the structural-affordance qualification, not the note's claimed scale threshold, which the paper does not measure. Lower priority than the explicit-retention example.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Revision guided by rationale needs faithfulness, not just legibility](../../../../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) and [Theory refinement may improve sample efficiency under structured shifts](../../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md): rejected as *new* inbound candidates because the intended full-paper citations already exist and retain the per-inference/prose-transfer limits.
- [Concept Bottleneck Models, superseded capture](../../../../sources/concept-bottleneck-models.ingest.md): already redirects to the full-paper ingest. An outbound link from the new evidence record to the flawed historical capture offers little reader value and risks importing unsupported wording.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md): the ingest already uses this comparison. A new evidence edge from that note would add little because the bottleneck experiments do not demonstrate an unrepresentable correction or test vocabulary redesign. Fixedness alone is not evidence of a mistaken decomposition.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md): per-inference correction does not show a retained improvement becoming available to a reflective learner. Explicit-retention is the more precise comparison.

## Index Membership

None. Existing note citations already supply useful discovery paths; no broad index addition is needed.

## Synthesis Opportunities

None. The useful operation and evaluation distinctions already have note homes.

## Maintenance Observations

None requiring a new maintenance action. The earlier capture now explicitly declares its evidence defect and points to the full-paper ingest; the two active citing notes have been reconciled. Their existing links must not be reported as outstanding work.

## Flags

- Candidate support remains bounded to a supervised concept vocabulary, oracle correction, and fixed test-time predictors. It does not establish durable learning, world-causal validity, or effective correction of retained natural-language rationales.
- The accepted ingest's recommended citation update has now been carried out by the parent workflow. It is not an unfinished prerequisite for this report.
- No split candidate: the proposed additions occupy one connected interpretation/addressability area and do not justify expanding the ingest into a general synthesis.
