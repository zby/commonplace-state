---
description: "Connections from the full Concept Bottleneck Models v3 paper to intervention evaluation, addressability, and the existing partial-source ingest"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/concept-bottleneck-models-paper-v3.md
source_has_frontmatter: true
date: "2026-09-18"
depth: standard
---

# Connection Report: Concept Bottleneck Models, full v3 paper

**Source:** [Concept Bottleneck Models](../../../../sources/.snapshots/concept-bottleneck-models-paper-v3.md). This is local workflow context. All outbound suggestions below belong on the future paired ingest, never on the immutable snapshot. That ingest did not exist during discovery; no link to it is fabricated.

Method: repository-only standard discovery under `cp-skill-connect`, performed by GPT-6. Candidate edges remain unauthored.

## Discovery Trace

The source collection permits notes, reference, agent-memory-systems, agentic-systems, and sources. Instructions and work are excluded. The source has frontmatter but no tags, so no source-tag completeness mark or by-tag sweep applies.

- **Notes:** read `kb/notes/README.md`, plus the curated `observability-README.md` and `learning-theory-README.md`. Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`; re-read the compact title-only output after an initial path-heavy result was truncated. Scanned descriptions with `rg '^description:' kb/notes/ kb/reference/ kb/sources/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md' | rg -i 'concept|interven|opacity|inspectab|faithful|causal|bottleneck|readab'`. Read the rationale-faithfulness, opacity, inspectable-artifact, explicit-retention, and theory-refinement candidates. These supply the strongest target-side distinctions; the paper does not directly test retained natural-language theories.
- **Sources:** read `kb/sources/README.md`; generated its complete title surface with the same title query, then compacted titles and inspected a middle slice after truncation. Description search identified the earlier concept-bottleneck ingest, ROME, faithful interpretability, and causal representation learning. Read those candidate ingests. Followed links from the older concept-bottleneck ingest to the current addressability and rationale notes, and from the theory-refinement note to the actual `rome-locating-and-editing-factual-associations-in-gpt.ingest.md` path. Retained the three comparisons below; ROME adds a useful but lower-priority persistence comparison whose current capture limits counsel against expanding this ingest around it.
- **Reference:** read `kb/reference/README.md`; generated all titles, then searched descriptions with `rg '^description:' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md' | rg -i 'interpret|concept|correct|edit|causal'`. Review and gate-learning hits concern Commonplace's chosen machinery, not the paper's experiment. No reference edge passed the articulation test.
- **Agent-memory-systems:** read its `README.md`, generated all titles, and used the shared description query. The broad body query `rg -n 'concept bottleneck|Concept Bottleneck|intervenab|inspectab|blackbox' kb/notes/ kb/reference/ kb/sources/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` produced generic inspectability hits. Tightened to `rg -n 'concept bottleneck|concept accuracy|intervenability' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`, with no results. Persistent harness-edit and memory-governance systems lack the paper's supervised concept interface; no specific comparison justified a retained candidate.
- **Agentic-systems:** read its `README.md`, generated all titles, and applied the same description and focused body queries. Runtime control and permission surfaces are too distant from an instance-level concept correction channel to warrant a link here.
- **External:** no external search. The exact versioned paper URL is already supplied by the snapshot and qualifies for `derived-from`; no other external target needs an edge.

Full title generation used `rg -N --no-heading -m1 '^# ' <destination>/ --glob '*.md'`, with `sed 's/^.*:# /# /'` to keep complete listings readable. Additional broad body search used `rg -n -i 'concept bottleneck|concept accuracy|ground.truth|test.time intervention'` across the five destinations; the many generic ground-truth hits were rejected, and narrow searches and linked neighborhoods carried the final selection. No semantic scores were available. Source/notes collection contracts and the snapshot, note, and connect-report type contracts were inspected.

## Connections Found

- [Revision guided by rationale needs faithfulness, not just legibility](../../../../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) — **is-evidence-for**: Section 6 supplies the worked concept-interface analogy already used by this note. Similar pre-intervention task/concept accuracy does not establish similar correction benefit. Keep the distinct low-concept-loss misalignment failure separate; neither result directly tests retained prose rationales.
- [Theory refinement may improve sample efficiency under structured shifts](../../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — **is-evidence-for**: supplies the note's bounded example of installing a named concept interface during training. Per-inference correction does not establish persistent theory revision or the note's cross-task sample-efficiency conjecture.
- [Explicit retention provides direct targets for selective revision](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — **compares-with**: separates a directly editable concept activation from a durable writable commitment. This paper gives the first without demonstrating the second, making the note's operation-relative distinction concrete.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — **compares-with**: the paper qualifies a categorical neural-versus-readable contrast by supervising an inspectable and correctable intermediate inside a neural predictor. It does not make arbitrary weights independently readable or editable.
- [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md) — **is-evidence-for**: architecture and supervision provide an inspection surface even when the surrounding parametric computation remains opaque; this supports the structural-affordance qualification, not a measured universal scale threshold.
- [Concept Bottleneck Models, earlier ingest](../../../../sources/concept-bottleneck-models.ingest.md) — **compares-with**: same paper under a different captured observation. The full v3 paper can check dataset preprocessing, separate intervention protocols, and the two distinct intervention failures without silently reusing the older summary as primary evidence.
- [Towards Faithfully Interpretable NLP Systems](../../../../sources/towards-faithfully-interpretable-nlp-systems.ingest.md) — **compares-with**: distinguishes explanation plausibility and faithfulness, while the bottleneck paper measures correction utility through a designed interface. Improved prediction after correction should not be promoted into proof of faithful historical reasoning.
- [Towards Causal Representation Learning](../../../../sources/towards-causal-representation-learning.ingest.md) — **compares-with**: contrasts discovering world-causal variables with using supplied predictive concepts. Section 2 explicitly permits concept correction without claiming that changing that concept in reality changes the label.
- [Concept Bottleneck Models, arXiv v3](https://arxiv.org/pdf/2007.04612v3) — **derived-from**: exact primary paper underlying the new ingest analysis.

## Bidirectional Candidates

None. Useful inbound authoring is specified separately below, without assuming mirrored links.

## Reverse-edge Candidates

- [Revision guided by rationale needs faithfulness, not just legibility](../../../../notes/revision-guided-by-rationale-needs-faithfulness-not-just-legibility.md) could cite the eventual full-paper ingest with **evidenced-by**, authorized by the notes contract, for its Section 6 analogy and its explicit limitation to typed intermediates. Re-evaluate the existing older-ingest citation rather than add a redundant evidence chain.
- [Theory refinement may improve sample efficiency under structured shifts](../../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) could cite the eventual full-paper ingest with **evidenced-by** for the installed interface and nonpersistent correction example. This supports that paragraph only, not the overall conjecture.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Locating and Editing Factual Associations in GPT](../../../../sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md): meaningful comparison between activation replacement and persistent parameter editing, but lower priority than the existing operation-profile note and bounded by this ingest's acknowledged abstract-level capture. Do not import its detailed model-editing claims into a fresh paper ingest.
- Generic memory-system inspectability and reference review-gate matches: a shared word does not establish a common intervention mechanism. No system-specific edge retained.

## Index Membership

None. Existing note links offer a more selective route than adding this source directly to broad tag heads.

## Synthesis Opportunities

None. The existing rationale and addressability notes already carry the useful distinctions; discovery does not establish a new cross-domain claim.

## Maintenance Observations

- The earlier concept-bottleneck ingest's Extractable Value item 2 attributes competitive concept accuracy to the low-concept-loss intervention failure. Section 6.1 of the full paper instead describes worse concept alignment for that control. Similar pre-intervention accuracy belongs to the separate linear/nonlinear ablation. Future correction should keep those findings separate.
- The older ingest's quoted snippets include summary-style text rather than exact wording of the full paper. They may be literal extracts of its older captured summary, but must not be treated as verbatim full-paper evidence. The new observation needs its own source support.
- The older ingest describes the explicit-retention note as asserting a flat addressability exclusion and names an old title. The current note instead compares operation profiles and explicitly permits numerical representations with tested editing interfaces. These descriptions are stale; the new ingest should use the current claim.

## Flags

- Keep empirical results scoped to OAI and CUB, with annotated concepts and oracle corrections. CUB uses processed class-level concepts and random group intervention order; OAI uses an order selected on held-out validation data. Do not merge their protocols.
- Correction benefit, semantic concept alignment, world-causal validity, and durable learning are separate claims. The paper does not prove their equivalence.
- Five note candidates occupy the connected interpretability/addressability area, not three independent topic areas; no split is proposed.
