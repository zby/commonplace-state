---
description: "Pre-ingest connection discovery for archcheck's agent-wiki A/B measurements, summary substitution, access costs, and freshness limits."
type: types/connect-report.md
source: kb/sources/.snapshots/archcheck-agent-wiki-economics.md
source_has_frontmatter: true
date: "2026-11-09"
depth: standard
---

# Connection Report: When does an agent wiki pay for itself?

**Source:** [When does an agent wiki pay for itself? A/B measurements on archcheck](../../../../sources/.snapshots/archcheck-agent-wiki-economics.md)

Purpose: pre-ingest discovery. These are candidate edges, not authored library links. The snapshot is immutable. Its matching ingest is absent; a future `kb/sources/archcheck-agent-wiki-economics.ingest.md` would own outbound connections. Reverse-edge candidates must wait for that tracked surface and must never cite the ignored snapshot as durable authority.

The source reports a small-repository comparison: 28 derived mirror pages did not beat code search, while a single dense, directly routed map reduced lookup and reconnaissance costs. It attributes the change to aggregation, short entry paths, and query-time reliance backed by separate staleness checks. The evidence is one Sonnet agent per cell, with a map shaped during the experiment. Reported answer-time savings do not establish lifecycle break-even or independently identify every factor in its proposed formula.

## Discovery Trace

### Setup and breadth

- Read the connect skill, global connect-report type and schema, the full snapshot, and the sources and reports collection contracts before discovery. Sources authorizes theory, reference, historical agent-memory-systems, agentic-systems, tags, other sources, and already-known external targets. Work and instructions were excluded from prospecting.
- The snapshot carries frontmatter but no `tags:`. No inherited-tag search or completeness shortcut applied. Read additional topic heads deliberately for the source's substantive questions.
- Read all six destination landings: `kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/README.md`.
- Generated the full fresh title surface once per destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Used scoped description filtering and focused bodies to reduce the title candidates. No semantic-search service, MCP, external browsing, or delegation was used; no relevance scores were available.

### Theory

- Description scan: `rg -n '^description:.*(compress|freshness|wiki|routing|amortiz|retrieval|cache|overhead)' kb/{theory,reference,agent-memory-systems,agentic-systems,sources}/ --glob '*.md'` surfaced the recompute ledger, addressability grain, insufficient-summary, and end-to-end evaluation notes. Those four were retained after full reads because they explain different parts of the observed cost change.
- Body search: `rg -n 'compression|re.verif|last_checked_commit|mirror pages|archcheck' kb/theory/ --glob '*.md'`, followed by `rg -l 'compression|re.verif|last_checked_commit|mirror pages|archcheck' kb/theory/ --glob '*.md'`. Hits included addressability, summary substitution, reverse compression, and general context notes. Broad compression matches were not automatically promoted to candidates.
- Read the context-engineering head and followed its grain and recompute-ledger links. From the recompute note followed the insufficient-summary, checked-copy, and segmentation notes; from checked-copy followed the make-like staleness note. Fully read these candidates and the theory outbound contract before proposing reverse edges.
- Read the evaluation head, then its experimental-contrast note. Kept that note as a comparison for the bundled single-map intervention rather than as evidence that the source tested each causal factor.
- Kept make-like staleness for the source's eight same-day flags and file-granularity review burden. Kept checked-copy only as a comparison: dependency-change detection is not deterministic claim verification.
- Rejected the generic context-efficiency match as less useful than the concrete cost and stopping ledgers. Existing theory already captures the principal economic mechanisms; discovery did not establish a need for a new synthesis note.

### Reference

- The same scoped description query highlighted freshness architecture and its accepted-input boundary. Body search: `rg -n 'staleness|source.*chang|derived cop' kb/reference/{freshness-architecture.md,navigation.md,content-routing.md}`.
- Followed the reference landing to freshness architecture and read it fully. Retained it as a narrow adjacent companion distinguishing input-version applicability from truth. Navigation and content-routing did not offer as discriminating a reader benefit for this source, so no broad reference links were retained.

### Historical agent-memory-systems

- The title and description surfaces identified OpenWiki, llm-project-wiki, and many general wiki implementations. Focused body query: `rg -n 'freshness|stale|trust|AGENTS' kb/agent-memory-systems/reviews/openwiki.md`.
- Read the OpenWiki review fully. Kept a comparison on generated-map shape, root instruction pointers, and update discipline. The source uses an OpenWiki-inspired pattern; it is not a benchmark of the reviewed OpenWiki package.
- The landing states that this survey is frozen historical evidence. Do not interpret a new source as permission to revise the historical review or its matrix.

### Agentic-systems

- Read the landing and followed its Agent Memory topic. Description refinement: `rg '^description:' kb/agentic-systems/ --glob '*.md' | rg -i 'memory|wiki|context' | cut -c1-230`.
- Body search: `rg -n 'wiki|freshness|compression' kb/agentic-systems/{topics,comparisons}/ --glob '*.md'`. The generated comparison table points to current OpenWiki and wiki-system records outside this source's named prospecting collections. Did not expand this run into a separate system analysis or treat the table as outcome evidence.
- Fully read `topics/memory.md`: its controlled-improvement question is relevant, but it is frontmatter-free and supplies general navigation rather than a new explanatory target. Routed the optional research-navigation suggestion to Raw Text Candidates. No typed outbound candidate from this destination survived the specificity test.

### Tags

- Description query: `rg '^description:' kb/tags/ --glob '*.md' | rg 'context|memory|maintenance|evaluation'`.
- Body query: `rg -n 'wiki|freshness|compression' kb/tags/{context-engineering,kb-maintenance,agent-memory,evaluation}-README.md`.
- Fully read context-engineering, agent-memory, and evaluation heads and the tags collection contract. They supplied routing to the cost, retention, and experiment neighborhoods. The heads are selective, not `complete: true`; the source had no tags, so no by-tag completeness claim or by-tag search skip was made.
- Sources is not a participating collection. A future ingest may use source-scoped tags under these definitions, but this does not create generated tag membership. The sources label table supplies no formal outbound label to tags; do not manufacture a `see-also` edge to a head.

### Other sources

- Full title scan and the shared scoped description query found the Karpathy manifesto, self-correcting OpenWiki report, and Anthropic components-of-memory experiments. All three were read fully.
- Body queries: `rg -n 'archcheck|OpenWiki|re.verif|wiki.*cost' kb/sources/ --glob '*.md'` and `rg -n 'wiki larger|maintenance costs|Answer-time savings|claim.*version|scope' kb/sources/{components-of-agent-memory,building-self-correcting-memory-in-openwiki-2092280107033616451,karpathy-llm-wiki}.ingest.md`.
- Kept components-of-memory for its large-corpus wiki/search comparison and unresolved offline costs; self-correcting OpenWiki for claim-level rather than whole-file invalidation; Karpathy for the original corpus/synthesis use case that the source distinguishes from code mirroring.
- Followed the self-correcting OpenWiki ingest's links back to the historical OpenWiki review and Commonplace freshness architecture, confirming that different revisions and validation scopes must remain separate.
- `test -e kb/sources/archcheck-agent-wiki-economics.ingest.md` found no matching ingest. No same-basename durable record is available yet.

### External

- External prospecting skipped as required. The original GitHub source URL is supplied in snapshot metadata and qualifies as the future ingest's provenance target. Other cited systems or discussions were not browsed or independently verified.

## Connections Found

All local edges below are recommendations for the future ingest, not edits to the snapshot.

- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — **is-evidence-for**: the source supplies a reported, bounded case where a derived representation loses when it adds reads and wins when it displaces multi-file reconstruction. This illustrates and bounds the economic comparison; it does not establish that all model-facing caches pay or demonstrate lifecycle net savings.
- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) — **is-evidence-for**: the verify arm reportedly read wiki pages and then opened code, leaving source-path work in place. This is a bounded observation of failed full substitution, not an independent measurement of required reliability or proof that verification always eliminates savings.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../theory/addressability-grain-sets-a-matched-selective-read-floor.md) — **compares-with**: compare the wiki entry-plus-source-map cost with a small source file, then distinguish the consolidated map's multi-file fan-out reduction from the note's one-unit selective-read condition. The source's compression formula should not be imported as a universal grain theorem.
- [Opposed recompute factors do not decide documentation segmentation](../../../../theory/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) — **compares-with**: the source measures per-use savings and observes rapid staleness, while this note supplies the missing horizon, reuse, and upkeep ledger. It helps the ingest distinguish cheaper queries from a demonstrated investment break-even.
- [Knowledge-access architecture must be evaluated end to end](../../../../theory/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: physically separated arms, audited reads, correctness checks, marginal token accounting, and staleness observations expose separate access, consumption, outcome, and upkeep boundaries. The case illustrates those checkpoints but leaves long-run upkeep and construction cost unpriced.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — **is-evidence-for**: cited-source change checks instantiate dependency-aware review prompting, while eight same-day flags after unrelated file changes give a concrete reason to price coarse dependency detection's review load. A flag indicates possible staleness, not a false claim.
- [A derived copy of recomputable truth must be checked or absent](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) — **compares-with**: both address safe reliance on derived material, but the source's path-existence and source-change lint does not re-derive and compare every fact. This link prevents calling its entire natural-language map a deterministically verified copy.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: collapsing 28 pages to one also changes aggregation and entry structure. The observed bundle comparison cannot identify compression, hop count, and trust-plus-freshness as independently necessary multiplicative factors.
- [OpenWiki historical review](../../../../agent-memory-systems/reviews/openwiki.md) — **compares-with**: compare small generated maps, root AGENTS/CLAUDE pointers, and update scoping with archcheck's one-page adaptation. Keep the historical package revision distinct from an inspired workflow built separately in archcheck.
- [The components of agent memory](../../../../sources/components-of-agent-memory.ingest.md) — **compares-with**: compare a small greppable codebase with the reported large heterogeneous corpus, lookup with cross-document work, and query-phase gains with offline construction cost. The different tasks and populations preclude a pooled effect estimate.
- [Building Self-Correcting Memory in OpenWiki](../../../../sources/building-self-correcting-memory-in-openwiki-2092280107033616451.ingest.md) — **compares-with**: contrast whole-file source-change invalidation with reported claim-evidence versioning and affected-page reconciliation. This identifies a precision-versus-maintenance question without asserting that finer invalidation is cheaper or more reliable.
- [Karpathy's LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) — **compares-with**: compare persistent synthesis over heterogeneous source material with per-entity mirroring of already-small code files. The link recovers the original pattern's purpose rather than treating one small-repo null as its refutation.
- [Original archcheck write-up](https://github.com/blurman-ai/archcheck/blob/master/docs/research/agent_wiki_economics.md) — **derived-from**: the future ingest would analyze this supplied external source; preserve capture provenance and checksum rather than treating the moving branch URL as a pinned implementation record.
- [Freshness architecture](../../../../reference/freshness-architecture.md) — **see-also**: a narrow companion explaining why matching accepted input versions means retained evidence remains applicable, not that a derived claim is true. It is not a claim that Commonplace ships archcheck's map-maintenance loop.

## Bidirectional Candidates

None. The independently useful return directions are listed below; no reciprocal link is justified merely by the outbound edge.

## Reverse-edge Candidates

These candidate theory-to-source edges are authorized by the fully read theory collection contract. Their target must be the future tracked ingest, not this snapshot. They are deferred, not broken links to a nonexistent file.

- [An insufficient summary precedes the source rather than replacing it](../../../../theory/an-insufficient-summary-precedes-the-source-rather-than-replacing.md) → future ingest — **evidenced-by**: add the reported verify-arm trace as an illustration of retained fallback reads and the distinction between full and partial substitution. The context phrase must state that the case illustrates or bounds the claim, not claim independent corroboration without establishing evidence independence.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) → future ingest — **evidenced-by**: a named external losing-and-winning materialization case could make the existing substitution boundary concrete. Preserve n=1 per cell, bundled changes, unpriced maintenance, and untested on-demand symbolic derivation.
- [Link graph plus timestamps enables make-like staleness detection](../../../../theory/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) → future ingest — **evidenced-by**: the same-day stale-page flags illustrate that source-change detection can work while still generating review work for changes that do not invalidate a claim. It bounds the note's qualitative claim that redundant rereading is cheap rather than measuring a general false-positive rate.

## Off-authorisation Candidates

None. Tag heads were used as navigation, not forced into the sources label table. No needed candidate edge justified extending that table.

## Raw Text Candidates

- [Agent Memory research topic](../../../../agentic-systems/topics/memory.md) — potential **see-also**: its question “What evidence establishes that memory improves performance?” gives a future ingest reader a route from this bounded experiment to the broader research agenda. The file is frontmatter-free; retain this only if that navigation is useful to the ingest's reader, not as a typed claim or measured comparison.

## Rejected Candidates

- [Context engineering tag head](../../../../tags/context-engineering-README.md) as a regular outbound edge — useful discovery hub, but sources has no authorized formal label to tags. Source-scoped tag use is a separate mechanism and needs no extra edge.
- [Agent memory tag head](../../../../tags/agent-memory-README.md) as generated index membership — sources is outside the participating collections. Retention-topic fit does not authorize adding the ingest to generated membership.
- [A derived copy of recomputable truth must be checked or absent](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) as **is-evidence-for** a fully checked map — rejected that stronger interpretation. Staleness lint and path existence do not validate semantic correctness; only the scoped comparison above survives.
- [OpenWiki historical review](../../../../agent-memory-systems/reviews/openwiki.md) as a product benchmark target — archcheck describes an inspired local implementation, not controlled execution of this pinned package. Keep the architectural comparison, reject product-performance attribution.

## Index Membership

None. Do not index the immutable snapshot. Sources does not participate in generated tag membership; a future ingest can use source-scoped `context-engineering`, `agent-memory`, and `evaluation` tags if its actual analysis substantively retains the cost, cross-session retention, and experiment-design contributions. The corresponding heads were read, but no assignment is made here.

## Synthesis Opportunities

None. The existing summary-substitution, addressability, and total-cache-value notes already separate the principal mechanisms. The source adds a bounded external case and experimental questions, not a demonstrated missing higher-order claim.

## Maintenance Observations

None. A differing historical OpenWiki review and later claim-versioning account are already explicitly version-scoped in the loaded ingest; this run does not establish a new contradiction or license refreshing the frozen survey.

## Flags

- **Pre-ingest dependency:** matching tracked ingest absent. All durable source citations and reverse edges must await its creation and appropriate quote retention or an explicit snapshot-required citation. Do not promote report-local snapshot links into library artifacts.
- **Formula overreach:** the source proposes `(compression > 1) × (zero-hop entry) × (trust + freshness lint)`. Its arms do not independently vary each factor or establish universal necessity. Treat this as a design hypothesis motivated by one repository, not a proven law.
- **Trust is not truth:** equal reported correctness on four lookups and one five-part probe does not establish unrestricted query-time reliance. The harder grep arm found a missing attribution detail and the map was corrected. Keep reconnaissance and modification uses distinct.
- **Marginal is not lifecycle cost:** subtracting the 24.3k null-agent baseline clarifies the reported incremental comparison but does not price map construction, refresh effort, or actual billing/cache behavior. Do not call the query results a measured break-even horizon.
- **No split recommendation for this capture:** multiple candidates concern one coherent wiki-economics mechanism across access, stopping, maintenance, and evaluation. Preserve the immutable source intact; a future ingest should separate observation, proposed explanation, and limits rather than split the snapshot.
