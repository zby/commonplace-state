---
description: "DualGraph uses knowledge gaps to steer research separately from report structure, with evidence, cost and convergence boundaries useful for KB search design."
type: kb/reports/types/connect-report.md
source: kb/sources/dualgraph-knowledge-exploration-outline-structure.ingest.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: DualGraph

**Source:** [DualGraph ingest](../../../../sources/dualgraph-knowledge-exploration-outline-structure.ingest.md)

## Discovery Trace

Read the accepted ingest fully after independent drafting and checksum, capture-metadata, Quotes and full-validation checks. Reassessed the pre-ingest candidates against its selected contribution. The graph-to-query comparison and the cost distinction remain useful; the quality-signals edge remains optional because the ingest already explains its proxy limits. The reverse edge independently serves readers seeking empirical follow-up to the speculative web-search design; it does not arise merely because the ingest links the note.

Read all 2,757 lines of the full v3 paper, including algorithms, search-chain formulas, evaluation supplements and six prompt templates. Reused same-batch contracts, curated heads and complete claim-title surfaces for notes, reference, agent-memory-systems, agentic-systems and sources. Ran `rg -n -i '^description:.*(graph|topolog|navigation|representation|schema)' kb/notes --glob '*.md'`. Read the web-search brainstorming and quality-signals notes fully. The former's link to the latter supplies the relevant one-hop neighborhood; previously read oracle-strength and navigation notes bound the proxy and routing comparison. `rg -l -i 'DualGraph|two graphs|outline.centric|knowledge.gap.*discover' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources` returned no matches. No additional destinations selected from those four collections. No external search or excluded-collection edges.

## Connections Found

- [Enrich web search](../../../../notes/brainstorming-how-to-enrich-web-search.md) — **compares-with**: an incrementally built temporary knowledge graph generates follow-up search directions separately from the final report outline. This gives a concrete implementation and ablation comparison for the note's proposed search/connect/redirect cycle, while stopping short of its durable KB-integration step.
- [Quality signals](../../../../notes/quality-signals-for-kb-evaluation.md) — **compares-with**: weak evidence counts, semantic similarity, community bridges and missing edges prioritize investigation. These are search cues rather than truth or completeness checks; the reported downstream comparisons test a specific hybrid controller instead of certifying structural quality as an oracle.
- [Context efficiency](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **compares-with**: section writing loads selected evidence, while graph maintenance and the resulting broader searches increase aggregate tokens and runtime despite fewer judged refinement rounds. This separates selective per-call context from whole-workflow cost.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Enrich web search](../../../../notes/brainstorming-how-to-enrich-web-search.md) → this tracked ingest — **evidenced-by**: the graph-to-query method and controlled same-initialization ablations offer a bounded empirical comparison for the speculative search/connect/redirect design. Preserve the untested bridge to a persistent KB, additional total cost and model-judged outcomes.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- A separate outline graph guarantees complete knowledge: topology only exposes gaps inside the represented space; outline-driven supplementary queries are still needed.
- More effective citations proves better individual source support: citation count and per-citation accuracy diverge in the reported results.
- Graph reuse alone establishes learning through criticism: extracted relations, merge prompts and one correction example do not isolate criticism as the source of later capacity gains.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

The web-search brainstorming remains a proposal, not the shipped Commonplace workflow. The paper supplies a concrete comparison but does not warrant treating its experimental result as validation of Commonplace's existing connect skill or durable integration step.

## Flags

The captured source is arXiv v3 dated August 25, 2026. Models are pinned GPT-4.1 and GPT-5-chat versions from 2025, with Bing and Crawl4AI; maximum five optimization rounds. Initial outlines, search queries and results are identical across ablation arms. Fine-grained mechanism ablations disable early stopping in every arm and evaluate intermediate outlines and accumulated search/evidence quality, not only final reports. The LightRAG comparison replaces its graph construction within DualGraph; it is not a complete-system comparison against LightRAG's intended workflow.

The evidence bank stores original spans plus query-conditioned summaries under IDs, with URL deduplication. Outline nodes and knowledge relations attach evidence IDs. Section writers load their section's selected evidence. Extraction promotes high-level salient relations, reuses nodes at a prompted 80 percent meaning overlap, and normally creates at most three concept nodes per turn; merge prompts use 85 percent semantic equivalence and protect core entities. These are model instructions, not independently established guarantees. Citation persistence and unioned evidence sets preserve identifiers, not automatically the validity of every changed claim-to-source relation.

Enrich ranks weakly supported existing edges, with zero-evidence edges first. Explore supplies core-entity/concept similarity, smoothed community-pair probabilities and entropy, and structural-hole bridges. Four categories each receive a quarter of the chain quota with refill. LLM chain selection and outline-supplied queries preserve a route to aspects not yet in the graph. A missing edge is an investigation candidate, not a fact that a relation exists. Outline rubric thresholds or round cap stop the process; neither proves epistemic completeness. Appendix D's monotone coverage/convergence discussion assumes permanently resolved gaps, but growing graphs, reprioritization and deletion/correction can change that space. Bounded calls and deduplicated URLs alone do not prove global convergence or sound knowledge.

GPT-5 RACE is 53.08 versus 51.17 without KG; GPT-4.1 is 51.50 versus 49.18. GPT-5 citation accuracy falls 61.15 to 57.55 while effective citations rise 66.06 to 79.65. A twenty-case joint-citation re-evaluation gives 90.51 versus 90.41; this supports a metric-grain hypothesis, not proof that all citation defects are measurement artifacts. DeepResearch Bench II InfoRecall improves 32.18 to 34.21 and total 39.50 to 41.48, below Gemini's 45.89. Scores are not universal state-of-the-art dominance. Several proprietary comparison outputs are reused from prior work, and most judgments are model-based without reported repeated-run uncertainty.

Mean refinement rounds fall 3.88 to 3.23, but a twenty-case cost study rises from 1.798 to 2.490 million tokens and 30.68 to 36.75 minutes. KG maintenance is 224k tokens, nine percent of the full run; that does not equal the total incremental cost, since broader retrieval grows too. The method is not shown at equal total-token or wall-clock budget.

The extraction audit covers 6,014 iteration-one triplets from 100 cases: 2.4 percent anomalous, seven (.12 percent of all) used for query generation before correction. Later validation of a loose relation differs from initial source support; audit does not cover every later edge or final claim. Human judge validation asks five annotators whether already-shown LLM judgments are reasonable over ten reports and 254 criteria: 88.6 percent unanimous and 97.5 percent individual endorsement. This is not a blind independently scored replication and its nested judgments are not 1,270 independent research tasks. Paper-only ingest; source-code analysis remains separate.
