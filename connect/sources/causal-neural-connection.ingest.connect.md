---
description: "Post-ingest connection discovery for neural causal identification, emphasizing useful missing inbound citations"
type: types/connect-report.md
source: "kb/sources/causal-neural-connection.ingest.md"
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: The Causal-Neural Connection ingest

**Source:** [Accepted ingest: The Causal-Neural Connection](../../../../sources/causal-neural-connection.ingest.md)

This is a new discovery pass on the accepted analysis. It distinguishes prospective additions from links the ingest already contains. All source-dependent inbound suggestions target the tracked ingest. The source's quote pool is empty, so any future claim using details of the paper must either declare `(snapshot required)` or obtain sufficient retained quotes through the grounding workflow.

## Discovery Trace

**Inputs and contracts:** Read the accepted ingest in full. Applied the already-loaded connect skill, connect-report type, sources collection, reports collection, and notes collection contracts. The accepted ingest foregrounds two different limitations: observational evidence can underdetermine causal effects even for expressive models, and an insufficiently expressive class can falsely make compatible models appear to agree. Its theory-builder assessment is explicitly bounded.

**Curated routing:** Used the collection README entry points already read in this worker context for notes, reference, agent-memory-systems, agentic-systems, tags, and sources. The previously read learning-theory and discovery heads both declare `complete: true`; skipped by-tag sweeps. The source has domains but no tags. No earlier connect report was read or copied as this deliverable.

**Fresh title and description searches:** Ran `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md' | rg -i 'causal|identif|hypothes|learn|world model|reach|decomposition|representation'`. This regenerated the full title surface for the six destinations and selected the relevant title families for reading. Ran `rg '^description:'` over the same destinations, filtered by `rg -i 'causal|identifia|intervention|inductive bias|expressiv|observational|neural|counterfactual'`.

**Per-destination body searches and evaluations:**

- **Notes:** Ran `rg -n 'causal-neural-connection|causal identification|hypothesis.class omission|neural.*causal|causal.*neural'` over the six destinations. This confirmed that competing-causal-theories already links to this ingest and fixed-decomposition does not. Re-evaluated the previously loaded full texts of those notes and the formal-assessment note against the accepted ingest. Kept a missing return citation for fixed-decomposition and a separate inbound candidate for formal-assessment. Read the theory-builder definition fully; the ingest already uses it correctly as an assessment frame, and a return citation from that definition would add a marginal example rather than necessary definition support.
- **Sources:** The title/description scan found the causal hierarchy, causal representation learning, error-centric intelligence, and Model Discovery Agent ingests. Re-evaluated the first three from their full texts already loaded in this worker context. Read Model Discovery Agent in full: it supplies a useful comparison on hypothesis disagreement versus active experiment choice, while retaining its own attribution and synthetic-world limits.
- **Reference:** The reference README and fresh metadata scan gave no specific shipped-system target. Ran `rg -n -i 'structural causal|causal graph|causal model|inductive bias' kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`; no matches. No reference edge retained.
- **Agent memory systems:** The README and fresh metadata scan expose general learning and retention topics, but the focused structural-causal query returned no match. The ingest supplies no evaluated memory mechanism; no candidate retained.
- **Agentic systems:** The README and fresh metadata scan offer adjacent predictive and scientific systems, but no shared causal-identification mechanism appeared in the focused query. Reject broad links based merely on neural learning or scientific activity.
- **Tags:** The tag README and title surface locate learning-theory and discovery. These aid navigation but the source contract authorizes no source-to-tag label. The existing note links give the more specific route, so no off-authorization edge is proposed.
- **External:** No external search. The original versioned arXiv URL is already known from the accepted source identity and the captured version description.

**Link following:** Followed the accepted ingest's competing-theories and fixed-decomposition links and checked the former's existing inbound citation. Followed the causal-assessment neighborhood to the hierarchy and causal-representation ingests. The new Model Discovery Agent read connects through its explicit formal-assessment and fixed-decomposition discussion. This separates a formal identification result from the additional act of acquiring discriminating evidence.

## Connections Found

- [On Pearl’s Hierarchy and the Foundations of Causal Inference](../../../../sources/on-pearls-hierarchy-foundations-causal-inference.ingest.md) — **compares-with**: Compare the general hierarchy and identification conditions with the neural construction that preserves the relevant causal possibilities under graph constraints. This helps the reader distinguish inherited causal limits from the neural paper's contribution.
- [Model Discovery Agent: LLM-assisted Bayesian Experiment Design](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **compares-with**: The accepted ingest diagnoses disagreement among compatible models but does not choose experiments; MDA explicitly maintains alternatives and chooses experiments within supplied domain and likelihood boundaries. Its compound gains and mixed acquisition-policy results prevent treating it as a general validation of the retention conjecture.
- [Towards Causal Representation Learning](../../../../sources/towards-causal-representation-learning.ingest.md) — **compares-with**: Compare the challenge of discovering causal variables and transferable mechanisms with identification after variables and graph are supplied. This makes the accepted ingest's fixed-boundary limitation easier to inspect.
- [Towards Error-Centric Intelligence I](../../../../sources/error-centric-intelligence-beyond-observational-learning.ingest.md) — **compares-with**: Compare parameter fitting and identification inside a supplied causal class with a proposal to revise variables, intervention semantics, and hypothesis spaces. The shared observational limitation does not establish that the broader structural-revision proposal works.
- [The Causal-Neural Connection, arXiv v3](https://arxiv.org/abs/2107.00793v3) — **derived-from**: A version-specific citation would expose the external text underlying the ingest's interpretation; its durable source identity currently appears in frontmatter.

The ingest's existing links to the competing-theories note, fixed-decomposition note, and theory-builder definition need no duplicate outbound entries.

## Bidirectional Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → [accepted ingest](../../../../sources/causal-neural-connection.ingest.md) — **evidenced-by**: Add the missing return citation at the hypothesis-class-omission discussion. Appendix C.3, Examples 6–7, supplies a constructed case in which restricted classes falsely suggest causal identification by excluding compatible rivals. The ingest already points to the note. This would qualify the note through a formal example, not claim an independent test of Commonplace or a general empirical prevalence result.

## Reverse-edge Candidates

- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) → [accepted ingest](../../../../sources/causal-neural-connection.ingest.md) — **evidenced-by**: The accepted analysis's graphical-neural equivalence result can qualify the causal-route discussion by showing that identification can also be realized through constrained neural optimization. The shared guarantee remains assumption-relative; finite training is not given the theorem's certainty. This is optional clarification, since the current note already disclaims an exhaustive taxonomy.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Competing causal theories can guide distinguishing experiments](../../../../notes/competing-causal-theories-can-guide-distinguishing-experiments.md) — Rejected as a new inbound recommendation because it already cites the accepted ingest with `(snapshot required)` for Theorem 1 and Corollary 1. Its existing citation preserves the formal support while leaving retention benefits conjectural.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — A return link would add another partial boundary example without strengthening the definition's stated criteria; the ingest-to-definition direction already serves the reader.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — The accepted ingest does not evaluate action-conditioned world-model shift testing. A general neural-model association would blur the distinct evidence routes.

## Index Membership

None

## Synthesis Opportunities

None. The existing causal-theories note owns the target-side claim about retaining rivals for evidence selection. The MDA comparison offers an evaluated adjacent operation, not grounds for duplicating that note.

## Maintenance Observations

None

## Flags

- Keep causal identification, recovery of a complete mechanism, adequacy of the represented model class, and evaluation of new experiment selection separate.
- A future inbound use must preserve the scope of the accepted analysis: supplied variables and graph, recursive finite-domain results, exact observational consistency and ideal optimization for the formal guarantee, and no demonstrated retention benefit.
- Candidate suggestions remain unapplied. No library artifacts or earlier reports were edited.
