---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/how-to-organise-a-project-s-knowledge-for-a-2113681318852600222.md"
source_has_frontmatter: true
date: "2026-10-24"
depth: standard
---

# Connection Report: How to organise a project's knowledge for AI coding agent and an engineer

**Source:** [How to organise a project's knowledge for AI coding agent and an engineer](../../../../sources/.snapshots/how-to-organise-a-project-s-knowledge-for-a-2113681318852600222.md)

The source is an immutable snapshot (X thread, @sermakarevich, 2026-10-23). The
snapshot is never a link author. Every candidate below is for the matching
tracked ingest, `kb/sources/how-to-organise-a-project-s-knowledge-for-a-2113681318852600222.ingest.md`.
That ingest did not exist when this report was written. Under the sources
contract, the ingest's `derived-from` edge goes to the external `source` URL
(`https://x.com/sermakarevich/status/2113681318852600222`).

**Source claim summary.** The source describes a practitioner design for a
project knowledge base with two readers: an acting agent and an engineer who has
to understand the system. It is one Markdown tree, organised project first, with
three folders: `raw`, `facts` and `artifacts`. Each fact is one chunk ending at a
complete thought, with the original span stored beside a self-standing rewrite.
Artifacts are summaries in per-folder generated indexes, views (digest, user,
developer and on-request) and specs. Every artifact links to the facts it was
built from, and those links are the only dependency record.

The mechanisms are:
- per-page guardrails (a link-resolution script, then one model check against the linked facts only);
- hash-triggered update: a script walks the links backward, rewrites dependents nearest-first in one run, stops early when a rebuilt page has the same meaning, and re-checks each hop;
- progressive-disclosure retrieval, with BM25, embeddings and a graph added only after logged misses;
- top-down and bottom-up human reading paths ("the summary is a map");
- specs written from views at the engineer's request;
- the root index kept in the harness's always-loaded instruction file.

Its quantitative support is relayed from cited papers (several 2026 arXiv IDs,
ClashEval, Vercel, Melumad and Yun). The snapshot does not verify those figures.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` § Outbound links.
- Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources and external.
- Excluded: `kb/work/` and `kb/instructions/`.
- Labels:
  - `derived-from`: external only.
  - `is-evidence-for`: theory, agent-memory-systems.
  - `abstracted-from`: theory.
  - `rests-on`: theory.
  - `compares-with`: theory, sources, agent-memory-systems, agentic-systems.
  - `defined-in`: theory/definitions.
  - `see-also`: theory, reference, sources, agent-memory-systems, agentic-systems, external.
- Postures: the snapshot is never the link author; links go on the ingest; `see-also` is sparing. Tags are listed as a scan destination, but no label row names tags.

**Description listing scan:**
- Theory titles: `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (427 titles), filtered by `grep -i -E 'fresh|stale|deriv|progressive|index|summar|chunk|always|skill|gate|error|compound|spec|human|reader|provenance|rebuild|depend|instruction|distill|condens|retriev|search|navig|hierarch|load|memory|file|cache'`. Flagged candidates:
  - lineage-at-source;
  - link-graph-plus-timestamps;
  - derived-copy-checked-or-absent;
  - stale-self-description;
  - pointer-design-tradeoffs;
  - insufficient-summary-precedes-source;
  - always-loaded-context-mechanisms;
  - keep-compiled-views-aligned;
  - serve-multiple-consumers;
  - indexes-lower-recall;
  - knowledge-access-end-to-end;
  - commitment-not-derivation;
  - import-external-knowledge;
  - design-for-first-time-human;
  - error-correction-decorrelated-checks;
  - semantic-review-vs-structural;
  - holistic-rewrite;
  - agents-navigate-by-deciding;
  - instruction-specificity-loading-frequency.
- Theory descriptions were read for the flagged set and for second-pass hits: fluid-resolution-switching, addressability-grain, changing-requirements-conflate, exact-implementation, human-llm-differences, opposed-recompute-factors, criteria-vs-process-edits, agent-statelessness-routing and title-as-claim.
- Reference titles: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '!kb/reference/adr/**'`, filtered by `fresh|stale|index|source|ingest|snapshot|navigat|lineage|deriv|review|control-plane|always|skill`. Flagged: freshness-architecture, collection-as-artifact-freshness (proposal) and navigation.
- ADR titles, filtered by `fresh|stale|derived|lineage|index|snapshot|checksum|hash|digest`. Flagged: ADR 025 (complete generated indexes are build-time only), ADRs 032, 052 and 065 (freshness) and ADR 072 (snapshots are local).
- Sources: `ls kb/sources/ | grep -i -E 'wiki|karpathy|knowledge-base|...|build-system|dagster|spec|chunk|memory'`, then a description read for 10 ingests. Flagged: karpathy-llm-wiki, llm-knowledge-bases (Karpathy X post), how-we-built-our-knowledge-base (Cerebras), build-systems-a-la-carte, dagster-asset-versioning, openwiki self-correcting memory and the-spec-is-the-new-code.
- Agentic-systems: `rg '^description:' kb/agentic-systems/` (excluding reports and archive), filtered by `wiki|index|stale|fresh|lineage|provenance|spec|chunk|summar|progressive|hash|derived|rebuild`. Only semantic-engine matched.
- Agent-memory-systems: `rg -l -i "dependency walk|dependents|reverse (dependency|link)|rebuild.*(hash|source)|source hash|content hash"` gave 19 reviews. A description plus `hash|stale|dependen` line read was done for openwiki, LLM-Wiki-v3, sage-wiki, TheKnowledge, okf-harness, browzy-ai, llm-wiki and semiont.

**Topic indexes:**
- Tag heads read (description and `complete:` only): kb-maintenance (`complete: true`), document-system, context-engineering and agent-memory. `kb/tags/COLLECTION.md` `participating:` does not include `sources`, so a source ingest takes no tags. Tag membership does not apply.
- `kb/agentic-systems/README.md` authored-accounts list. Semantic Engine is the only ingest-adjacent system and is not a KB design.

**Body search:**
- The cited studies were searched across `kb` (excluding work and reports):
  - `rg -l -i "Vercel"`: only agent-memory and system reviews, plus one software-factories ingest. No theory note holds the always-loaded-vs-skill result.
  - `rg -l -i "ClashEval|2404.10198"`: none.
  - `"2607.17598|Progressive Disclosure All You Need"`: none.
  - `"2607.26637|Filesystem-Based Memory"`: none.
  - `"Planfence|2609.03340"`: none.
  - `"Snowball|2608.14588"`: one unrelated ingest (software-design-model-use).
  - `"Specification Gap|2603.24284"`: phrase-level matches in theory on underspecification, but not the cited paper.
  - `"Salsa|Adapton|early cutoff"`: build-systems-a-la-carte (both ingests) and dagster.
  - `"expertise reversal"`: none.
  - `"Melumad"`: none.
  - `"context rot"`: four ingests and fractal analyses.
  - `"LLM-Wiki|2605.25480"`: many agent-memory-systems wiki reviews, none citing the paper.
  - `"sermakarevich"`: none, so there is no prior ingest of this author.
- `rg -l -i "progressive disclosure" kb/theory kb/tags` gave 17 files. Pointer-design-tradeoffs, fluid-resolution-switching, addressability-grain and instruction-specificity were kept for evaluation.
- `rg -l -i "hallucination|error(s)? compound|compounding error|cascad" kb/theory` gave 9 files. Changing-requirements-conflate was kept. The others treat cascades in requirement or loop contexts, not per-stage gates.
- `rg -l -i "content hash|by hash|hash of|checksum" kb/theory` gave criteria-vs-process-edits (kept) and runtime-structure (rejected, about governance).
- `rg -l -i "two readers|human and agent|humans and agents|both readers|dual audience"` gave opposed-recompute-factors (kept), human-llm-differences and metacircular-interpreters.
- `rg -l -i "never invoked|not invoked|fail(s|ed)? to invoke|..."` gave only skill-discovery-re-fires, which is about sub-agent re-discovery, not invocation rate. Rejected.

**Link following:**
- Body of `artifacts-produced-from-sources-need-lineage-recorded-at-the-source` read. It links to link-graph-plus-timestamps and derived-copy-checked-or-absent, and it names three record placements (source-side, database, artifact-side). The source design is the artifact-side option plus a script-derived forward index plus a hash-triggered change surface.
- Body of `link-graph-plus-timestamps` read. Its review-prompt "rebuild" and its false-positive filter section are the points where the source diverges: the source rewrites automatically and stops early when the meaning is unchanged.
- Body of `commitment-not-derivation` read. Its derivation/commitment table classifies "kept generated code" and accepted decisions as commitments, which the source's spec rebuild does not distinguish.
- Body of `an-insufficient-summary-precedes-the-source` read. It links to pointer-design-tradeoffs and addressability-grain. The source's "path must end at the chunk" reaches a similar structural conclusion from learning evidence.
- Bodies of `fluid-resolution-switching`, `opposed-recompute-factors` and `criteria-vs-process-edits` were read for their first sections. `criteria-vs-process-edits` links to the build-systems-a-la-carte ingest, which confirms that ingest as the source-side build-systems anchor.
- Heads of `freshness-architecture` and ADR 025 read.

## Connections Found

All candidates are for the future ingest at `kb/sources/how-to-organise-a-project-s-knowledge-for-a-2113681318852600222.ingest.md`.

**Theory**

- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../../../../theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) -- **compares-with**: the shared axis is where lineage lives and how the forward query fires.
  - The source keeps only artifact-side links ("the links are the only record").
  - It derives the reverse map by script whenever a source hash changes. This is the note's artifact-side record plus forward index plus change-handling surface, and the note says that combination is needed for the interruption-first signal.
  - The source removes the human from the interrupt entirely: dependents are rewritten without a worklist.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -- **compares-with**: both describe a make-like rebuild over the existing link graph, with three differences.
  - The source keys on content hash, not timestamp.
  - Its "recipe" is automatic rewrite, not "re-read and decide".
  - Its same-meaning early cutoff answers the note's false-positive and filtering section with a concrete stop rule.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- **compares-with**: the shared axis is which artifacts may be auto-rebuilt.
  - The source treats views and specs alike as derived and rewritten on any upstream change.
  - The note predicts that a spec carries resolutions the facts do not determine: what is to be delivered, decided by the engineer. Under the note, recompute is the wrong repair for that content. See Flags.
- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../../theory/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) -- **compares-with**: the shared axis is what belongs in the rebuild key.
  - The source's recorded inputs are source hashes and links only.
  - A change to the slicing, rewrite, summary or view prompts triggers no rebuild. The note predicts this as an omitted-process-input failure: old artifacts stay "fresh" though produced by the superseded method.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) -- **compares-with**: both keep the authoritative unit in the reading path under every summary.
  - The source argues "the summary is a map … a path that ends at the summary is not a reading path" from learning evidence (Melumad and Yun).
  - The note derives the same structural position from reliability and read-cost accounting.
  - The comparison shows two independent justifications for one design rule.
- [A knowledge base should support fluid resolution-switching](../../../../theory/a-knowledge-base-should-support-fluid-resolution-switching.md) -- **is-evidence-for**: the source is a practitioner design built around cheap switches in both directions.
  - Top-down: abstract, then source summaries, then chunk summaries, then the chunk.
  - Bottom-up: from the chunk a ticket names, climbing to see where it sits.
  - Angle views are also provided.
  - It bears on the criterion as an independently arrived-at instance. It is not a test.
- [Serve multiple consumers, not one retrieval interface](../../../../theory/agent-memory-requirements/serve-multiple-consumers.md) -- **is-evidence-for**: the source builds distinct surfaces from one fact layer for three consumers.
  - Index files and chunks serve the acting agent.
  - Role views serve the engineer.
  - Specs serve the coding agent.
  - It argues that most published designs serve only the agent.
- [Indexes lower recall when they suppress retrieval that would find more](../../../../theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) -- **is-evidence-for**: the source relays He et al. (arXiv 2607.17598): a second routing layer with misleading group summaries fell to 0.267 "because the agent picked the wrong group and never came back".
  - That is a measured instance of index-induced fallback suppression.
  - The source's repair is keyword search across all index files when no line fits.
  - The figure is second-hand and should be checked before a note relies on it.
- [Instruction specificity should match loading frequency](../../../../theory/instruction-specificity-should-match-loading-frequency.md) -- **compares-with**: the shared axis is what belongs in always-loaded context.
  - The source puts the root or project index, and nothing else, in the harness instruction file.
  - It justifies this with the relayed Vercel result: an always-loaded 8 KB index passed all cases, while the same content as a skill passed 53% and went uninvoked in 56% of cases.
  - The note ranks always-loaded content by generality and attention competition.
- [Opposed recompute factors do not decide documentation segmentation](../../../../theory/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) -- **compares-with**: the source fixes an audience segmentation by default (digest, user and developer views, plus on-request feature views). The note argues that per-audience splitting is a separate decision from whether to maintain the cache at all, and that recompute factors alone do not decide it. The source offers no cost argument for its split.
- [Changing requirements conflate genuine change with disambiguation](../../../../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- **compares-with**: the source's update path propagates every requirement revision the same way, by hash diff and rewrite. The note separates world change from late discovery of a wrong interpretation. The second kind can leave specs built on a resolved ambiguity that the hash walk rewrites without surfacing the interpretation change.

**Reference**

- [Freshness architecture](../../../../reference/freshness-architecture.md) -- **see-also**: Commonplace's own accepted-input freshness substrate is the closest shipped counterpart to the source's hash-plus-links update. It keys targets on role-labelled inputs with accepted versions and says freshness is not truth. The source collapses freshness and rewrite into one run.

**Sources**

- [Karpathy LLM wiki](../../../../sources/karpathy-llm-wiki.ingest.md) -- **compares-with**: the shared axis is the raw-to-compiled wiki architecture with index files.
  - Both separate immutable raw material from model-written pages under generated indexes.
  - The source adds a fact layer that stores original spans beside the rewrites, statement-level citations, a dependency-driven update and specs.
  - The ingest can state which additions are new relative to the Karpathy pattern.
- [Build Systems à la Carte](../../../../sources/build-systems-a-la-carte.ingest.md) -- **compares-with**: the source explicitly borrows early cutoff from Salsa and Jane Street Incremental and dependency walks from Adapton. This ingest is the KB's anchor for that framework, so the ingest can classify the source's rebuilder: verifying traces keyed on source hash, with semantic rather than exact early cutoff.
- [Dagster asset versioning and caching](../../../../sources/dagster-asset-versioning-and-caching.ingest.md) -- **compares-with**: in both, output identity stops a cascade. Dagster uses output fingerprints. The source uses a same-meaning classifier with exact text as a free first pass. The comparison makes visible that the source's cutoff is probabilistic.
- [Building self-correcting memory in OpenWiki](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md) -- **compares-with**: the shared axis is the response to an evidence change. OpenWiki versions claim-level code evidence and marks wiki beliefs stale. The source rewrites dependents automatically in the same run.
- [The spec is the new code](../../../../sources/the-spec-is-the-new-code-a-guide-to-spec-driven-development.ingest.md) -- **compares-with**: the shared axis is where specs come from.
  - SDD runs a spec, plan, task, implement cascade driven by the author.
  - The source derives each spec from a fact-cited view and puts it under the same update walk.

**Agent-memory-systems**

- [sage-wiki](../../../../agent-memory-systems/reviews/sage-wiki.md) -- **compares-with**: the shared axis is invalidation of derived outputs when cited source hashes change. sage-wiki demotes confirmed outputs back to review. The source rewrites them and gates each hop with a per-page check.
- [TheKnowledge](../../../../agent-memory-systems/reviews/TheKnowledge.md) -- **compares-with**: both keep hashed, immutable raw sources and validate citation grounding at page level. TheKnowledge's validator is the closest reviewed system to the source's guardrail 1 (link resolution). It is a reference point for the source's guardrail 2 (model check against cited facts only).

**External**

- External prospecting was skipped by rule. The only external target in hand is the source URL itself, which is the ingest's `derived-from` edge (noted above). The cited papers are known from the snapshot but are not candidate link targets for the ingest. Citing them is the source's job.

## Bidirectional Candidates

- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) <-> source -- **compares-with**: the return path is useful because the note's "What would defeat this claim?" and false-positive sections lack a practitioner instance of hash-keyed, semantically cut-off rebuilding. The note would gain a contrast case through the ingest.

## Reverse-edge Candidates

These follow the theory `COLLECTION.md` labels. `evidenced-by` is allowed into sources, and its context phrase must say "qualifies" or "bounds", because this practitioner design is not a refutation test of the target claims.

- [Source changes should surface downstream review targets](../../../../theory/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) → ingest -- **evidenced-by**: qualifies the claim. It is a deployed design in which artifact-side links plus a script-derived forward map replace source-side pointers. The design also removes the human from the forward interrupt.
- [Indexes lower recall when they suppress retrieval that would find more](../../../../theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) → ingest -- **evidenced-by**: bounds the claim with the relayed He et al. measurement of misleading group summaries stranding the agent. Retain a verbatim quote via `cp-skill-ground`, or go to the primary paper.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) → ingest -- **evidenced-by**: qualifies the claim with a worked practitioner case that auto-rebuilds a commitment-like artifact (the spec) as if it were derived. It shows that the misfiling the note warns about occurs in real designs.

## Off-authorisation Candidates

- [ADR 025: complete generated indexes are build-time only](../../../../reference/adr/025-complete-generated-indexes-are-build-time-only.md) -- passes the articulation test as a contrast.
  - Both answer the agent's whole-read cost of complete listings with different remedies. The source adds levels so that every generated index stays short enough to read whole. ADR 025 retires committed generated listings in favour of curated heads plus scoped `rg`.
  - Only `see-also` is authorised from sources into reference, and a contrast is not an adjacent companion. Suggest extending `compares-with` to the `reference` destination in `kb/sources/COLLECTION.md`, or leave the contrast to a theory note that links both.

## Raw Text Candidates

None

## Rejected Candidates

- [A derived copy of recomputable truth must be checked or absent](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) -- the note concerns mechanically recomputable copies. The source's views and summaries are judgment-checked derivations. The relevant distinction is already carried by the commitment-not-derivation candidate.
- [Stale self-description conceals its own staleness](../../../../theory/stale-self-description-conceals-its-own-staleness.md) -- the note is about reflexive drift (the detector consults the drifted artifact). The source's "agents trust the page in front of them" is ordinary drift, so this would be a keyword match.
- [Pointer design tradeoffs in progressive disclosure](../../../../theory/pointer-design-tradeoffs-in-progressive-disclosure.md) -- relevant, but the source uses only one pointer kind (generated summaries) and does not trade among the kinds. Fluid-resolution-switching and insufficient-summary carry the useful contact.
- [Always-loaded context mechanisms in agent harnesses](../../../../theory/always-loaded-context-mechanisms-in-agent-harnesses.md) -- a survey of mechanisms. Instruction-specificity is the note that makes a claim the source's always-loaded-index rule can be compared with.
- [Llm knowledge bases (Karpathy X post)](../../../../sources/llm-knowledge-bases-something-i-m-finding-very-useful.ingest.md) -- duplicates the karpathy-llm-wiki contrast at lower resolution. Keep one Karpathy edge.
- [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md) -- shares source chunking only, with no dependency or reader-path mechanism, so it is a keyword-level overlap.
- Theory notes on error correction and semantic review (`error-correction-works-above-chance-oracles-with-decorrelated-checks`, `semantic-review-catches-content-errors-that-structural-validation`) -- the source's script-then-model guardrail order matches them in outline. The source adds no new mechanism beyond relayed per-stage gate figures, so a link would be only "related".
- Reference proposals `collection-as-artifact-freshness` and ADRs 032, 052 and 065 -- these are internal freshness implementation details. `freshness-architecture` is the one sufficient reference companion.

## Index Membership

None. `sources` is not a tag-participating collection (`kb/tags/COLLECTION.md` `participating:`), and `kb/sources/` has no curated topical index for ingests.

## Synthesis Opportunities

- The source, sage-wiki, OpenWiki and Dagster each respond differently when a derived artifact's input changes:
  - automatic rewrite with semantic early cutoff (source);
  - demotion to review (sage-wiki);
  - stale marking (OpenWiki);
  - fingerprint-cut rebuild (Dagster).

  `link-graph-plus-timestamps` (review prompt) and `commitment-not-derivation` (the repair depends on derived vs committed) together suggest a claim: the right response to an input change is selected by the artifact's derivation regime, and auto-rewrite is safe only for the derived zone. No current note states that selection rule across the observed responses.

## Maintenance Observations

- Collection-contract gap: `kb/sources/COLLECTION.md` lists `kb/tags/` as a scan destination but authorises no label for it, and tags do not include `sources` as participating. Either drop tags from the scan list or state that tag links from ingests are out of scope.
- Collection-contract gap: no `compares-with` from sources into reference (see Off-authorisation Candidates). Contrasts with shipped Commonplace design (ADRs) recur for KB-design sources like this one.
- Evidence hygiene: the source's figures come from a dense cluster of 2026 arXiv citations (2603.24284, 2604.06861, 2605.25480, 2607.17598, 2607.26076, 2607.26637, 2608.00824, 2608.14588, 2609.03340). None is ingested in the KB. Any theory note that cites them through this ingest gets second-hand evidence only. The ingest should say this.

## Flags

- Tension: the source puts specs under the automatic rebuild walk. `commitment-not-derivation` classifies such engineer-decided, deliverable-fixing content as commitment, repaired by supersession rather than recompute. The ingest should record the tension without resolving it.
- Gap in the source's rebuild key: production-process changes (prompts and slicing method) do not trigger rebuilds (see `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts`).
- Split candidate for the ingest's analysis, not the snapshot: the source makes several independent assertions across at least four areas: fact representation, update and freshness, retrieval ladder and always-loaded index, and human reading paths and specs. It connects to more than five notes. The ingest may want to separate its analysis by mechanism.
