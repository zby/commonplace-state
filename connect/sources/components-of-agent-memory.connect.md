---
description: "Connection discovery for Anthropic's agent-memory components report: correction evidence, wiki/search tradeoffs, concurrent ownership, and offline maintenance comparisons"
type: types/connect-report.md
source: kb/sources/.snapshots/components-of-agent-memory.md
source_has_frontmatter: true
date: "2026-11-07"
depth: standard
---

# Connection Report: The components of agent memory

**Source:** [The components of agent memory](../../../../sources/.snapshots/components-of-agent-memory.md)

Discovery only, produced with `cp-skill-connect` using repository-local reads and searches. All edges below are candidates, not authored links. The snapshot is immutable. Its normal authored surface, `kb/sources/components-of-agent-memory.ingest.md`, is absent; outbound suggestions remain here pending separately authorized ingest work. No library mutation is part of this report.

The source separates transcripts, notes, navigational representations, and injected context. Offline work can correct notes against transcripts, build and repair wikis, and select a small injected layer. Its reported experiments also expose model-dependent salience, wiki overhead, and lost concurrent writes. These are vendor-reported observations, not independently reproduced results or proof that the biological analogy determines the architecture.

## Discovery Trace

### Shared method and scope

- Read the source fully, `sources/COLLECTION.md`, the global connect-report type and schema, and `reports/COLLECTION.md` before writing. Read `theory/COLLECTION.md` before judging reverse edges.
- Read all six destination landings: `theory/README.md`, `reference/README.md`, `agent-memory-systems/README.md`, `agentic-systems/README.md`, `tags/README.md`, and `sources/README.md`.
- Generated fresh complete title surfaces for each destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered the truncated command output through file reads. Brief titles were treated as belonging to their documents; no brief is proposed as a destination.
- Scanned description surfaces using `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'memor|dream|consolid|transcript|salien|wiki|injection|ownership'` separately for all six destinations; recovered the truncated output. This is a focused description scan, not a claim of full semantic enumeration.
- First body pass for each destination: `rg -l -i 'dreaming|sleeptime|sleep.time|ground truth|overwrite|overwritten' kb/<destination> --glob '*.md'`. Follow-up queries and candidate judgments appear below. No relevance scores were produced by these lexical searches.
- The snapshot has no tags. No source-tag scan was applicable. Independently read the selective agent-memory and trace-learning heads for routing; neither declares `complete: true`, so no completeness-based search skip was taken.
- `rg -n 'components-of-agent-memory' kb --glob '*.md'` returned no ordinary visible-file matches. The name-paired ingest existence check also failed. Hidden snapshots were not inferred to be absent from that ordinary search.
- Excluded `kb/work/` and `kb/instructions/` as outbound destinations under the source contract. No external discovery or agents were used.

### Theory

- Broad prospecting was warranted by the source's separate correction, salience, representation, injection, and concurrent-write claims. The title surface exposed episode re-examination, access/transformation burden, and coordination guarantees in addition to obvious memory titles.
- Focused queries: `rg -n -i 'transcript|evidence|re.exam|rule'` over `retaining-episode-evidence-keeps-a-distilled-rule-open-to.md` and `trace-extracted-memory-earns-authority-per-operation-not-at-capture.md`; `rg -n -i 'single|ownership|overwrit|concurrent'` over `agent-orchestration-needs-coordination-guarantees-not-just.md`.
- Fully read those candidates, access/transformation burden, promotion economics, raw accumulation, and storage/activation. Kept the first five for distinct mechanisms. Raw accumulation was rejected as a less discriminating route than the specific correction and promotion targets. Storage/activation was kept because the source explicitly separates injection from adherence and reports missed memory reads.
- One-hop following: episode re-examination → preserve-evidence requirement; trace-authority → bounded abstraction; raw accumulation → four use-time memory tests; Karpathy ingest → index recall. Fully read all four follow-up targets. Preserve-evidence and four-test notes mostly duplicate stronger routes here. Index recall is not tested by wiki-plus-search gains. Bounded abstraction informs the caution about treating a tested game heuristic as a general rule, not an additional edge.
- Reverse pass: the episode note has a concrete correction case to inspect; trace-authority has an explicit unresolved source/provenance question to revisit. Neither reverse edge may cite the ignored snapshot durably.

### Reference

- Focused description scan selected `agent-memory-coverage.md` and exposed the gap plan. Fully read coverage; it already maps the relevant trace, activation, authority, and evaluation gaps, so did not add a parallel gap-plan edge.
- Query: `rg -n -i 'trace|automatic|activation' kb/reference/agent-memory-coverage.md` confirmed that automated extraction and behavioral evaluation are described as gaps, not shipped capabilities. Kept a sparse `see-also` operator route to that map. Rejected installation, ADR, and schema hits from the broad body query as incidental uses of overwrite or ground-truth language.

### Historical agent-memory systems

- The landing explicitly freezes this collection's evidence boundaries. Title/description scans selected Letta over a generic spread of wiki implementations.
- Query: `rg -n -i 'sleeptime|transcript|faithfulness' kb/agent-memory-systems/reviews/letta.md`. Fully read Letta: transcripts feed background shared-block edits; core blocks are pushed while archives require tools. Kept comparison on offline write path and later consumption.
- Its one-hop theory neighbor, storage/activation, was read fully. Letta's lack of a behavioral ablation cannot be repaired by importing Anthropic's different-system results. No reverse edit to this frozen review is proposed.

### Agentic systems

- The landing separates authored accounts from historical generated reviews and says the current comparison population is empty until regeneration. Title/description scans and the dreaming body pass selected archived GBrain, which the landing itself links.
- Query: `rg -n -i 'nightly|contradict|synthesis' kb/agentic-systems/reviews-archive/gbrain-garrytan.md`. Fully read that review. Kept it as a historical mechanism comparison: nightly transcript-derived pages and quote repair do not establish semantic correction or downstream benefit. Did not follow external code links or claim current implementation freshness.
- Rejected the commit-bound landscape as a primary destination: its population and date are not evidence about this newly captured source. Did not propose adding this source directly to matrix inputs.

### Tags

- The full title and focused description scans selected agent-memory and trace-learning; read both heads fully after the tags landing. The body pass also surfaced artifact-analysis and claims-and-grounding, but their source/evidence language did not justify additional destinations.
- Query: `rg -n -i 'memory|trace|source|participat|outbound|label|see-also' kb/tags/COLLECTION.md` checked membership context. Sources are outside participating collections; source-scoped tags do not become generated members.
- No label in the source contract authorizes a source → tags formal edge. The two useful navigation-head candidates are therefore off-authorisation, not disguised `see-also` links. No index insertion is proposed for the snapshot.

### Other sources

- Title/description scans selected Karpathy's wiki manifesto and Language Models Need Sleep. Both were read fully.
- Query: `rg -n -i 'consolidat|sleep|wiki|search'` over `kb/sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md` and `kb/sources/karpathy-llm-wiki.ingest.md`.
- Kept Karpathy on compiled wiki versus query-time search: it is the very gist linked by the snapshot, now accompanied by reported benefits and no-gain cases. Kept Sleep on offline schedule versus retained artifact: weight consolidation is not note/wiki correction.
- Karpathy's index-recall neighbor was followed and rejected as direct evidence, as described above. Sleep's other offline-learning comparisons were not expanded into extra edges: the form distinction is already clear without a sleep-themed spray.

### External

- External is authorized only for already-known targets. Evaluated the original Anthropic URL present in snapshot metadata as `derived-from` for a future ingest. No browsing, external search, or external verification was performed. Other article URLs were not prospected.

## Connections Found

These are recommendations for the future authored ingest surface, not changes to the snapshot.

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — **is-evidence-for**: the Mt. Moon case reports transcript-based correction of an erroneous location note followed by changed navigation. It gives a bounded case of re-examination, not a guarantee that transcripts contain ground truth or that all rules reconstruct correctly.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) — **is-evidence-for**: CL-Bench distinguishes stored guesses, checked facts, corrections, and validated rules across models; a memory directory alone does not establish completion of the checking and consultation loop. This bears on the ladder without validating its exact factoring or establishing a general capability trend.
- [Access burden and transformation burden are distinct query dimensions](../../../../theory/access-burden-and-transformation-burden-are-distinct-query-dimensions.md) — **compares-with**: wiki gains differ between multi-document judgment/arithmetic questions and single-document lookups. The distinction helps a designer diagnose whether organization reduces finding work or precomputes answer construction; the experiment does not isolate those causes.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../theory/agent-orchestration-needs-coordination-guarantees-not-just.md) — **is-evidence-for**: the contract-table episode reports agents overwriting shared facts, followed by per-contract single-writer pages. It supplies a concrete shared-memory ownership failure, but the revised instructions also changed quotation fidelity, so the 72% → 100% result does not isolate ownership's contribution.
- [Promote only when future value exceeds maintenance cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) — **compares-with**: indiscriminate game-state recording, a wiki larger than its corpus, and a deliberately small injected layer expose different retention costs. This helps distinguish what deserves durable storage from what deserves always-loaded context; the source does not measure a general promotion threshold.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: missed memory reads and the explicit warning that injected notes need not be acted on distinguish storage, exposure, and use. The reading-plus-theory-testing prompt bundles interventions and cannot isolate either transition's causal effect.
- [Agent memory coverage](../../../../reference/agent-memory-coverage.md) — **see-also**: Commonplace maintainers can map the source's transcript correction, layered activation, and evaluation mechanisms onto documented local gaps without mistaking external demonstrations for shipped Commonplace behavior.
- [Letta](../../../../agent-memory-systems/reviews/letta.md) — **compares-with**: the historical code-grounded review supplies a concrete transcript → background block edit → prompt-push path to compare with Anthropic's offline note/wiki hierarchy. Its June revision and untested behavioral benefit remain separate from the November vendor experiments.
- [GBrain, historical September review](../../../../agentic-systems/reviews-archive/gbrain-garrytan.md) — **compares-with**: compare what offline maintenance actually checks. GBrain repairs quotation spans and synthesizes pages but does not test synthesized claims; Anthropic reports correcting a mistaken note against a transcript and inspecting subsequent navigation. Neither establishes general autonomous correction reliability.
- [LLM Wiki ingest](../../../../sources/karpathy-llm-wiki.ingest.md) — **compares-with**: the cited manifesto proposes persistent compiled pages instead of repeated raw-source rediscovery; the source's wiki-only, search-only, and combined conditions bound that proposal with reported task-specific gains and failures.
- [Language Models Need Sleep ingest](../../../../sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md) — **compares-with**: both move learning work offline, but Sleep changes distributed model weights whereas this source retains editable notes and wiki pages. The comparison prevents a common scheduling metaphor from hiding different inspection and correction surfaces.
- [Original Anthropic article](https://www.anthropic.com/research/components-of-agent-memory) — **derived-from**: the future ingest's source analysis would be worked out from this already-captured original article, not from a local snapshot URL.

## Bidirectional Candidates

None. Inbound needs from other collections are listed separately below; reciprocal edges are not automatic.

## Reverse-edge Candidates

Under `theory/COLLECTION.md`, **evidenced-by** may point to external sources or tracked ingests. Until a matching ingest exists, these candidates target the [original article](https://www.anthropic.com/research/components-of-agent-memory), never the ignored snapshot. Later ingest links require separate source-grounding work.

- [Retaining episode evidence keeps a distilled rule open to re-examination](../../../../theory/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) → original article — **evidenced-by**: add the Mt. Moon episode as a bounded reported case in which rechecking retained evidence corrected a note and changed later navigation. Its case-study scope qualifies the claim; this is not declared corroboration by an independently designed attempt to refute the note.
- [Trace-extracted memory earns authority per operation, not at capture](../../../../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md) → original article — **evidenced-by**: the CL-Bench model comparison can qualify the ladder with observed examples of where memory checking stopped. It does not prove the original source identity of the note's uncaptured paraphrase or warrant a universal model-capability rule.

## Off-authorisation Candidates

- [Agent-memory head](../../../../tags/agent-memory-README.md) — the source's layers and maintenance policies fit this head's architecture and lifecycle scope, but no source → tags label is authorized. Reject a formal edge rather than extend authorization for a redundant navigation route; an eventual ingest may separately assess the existing source-scoped tag convention.
- [Trace-learning head](../../../../tags/trace-learning-README.md) — transcript-based correction and wiki building satisfy the head's substantive raw-to-distilled concern, but the source contract authorizes no source → tags label. Reject a formal edge; do not add the immutable snapshot as an index member.

## Raw Text Candidates

None. All proposed local artifact targets have frontmatter. Frontmatter-free collection landings were used for navigation, not proposed as note connections.

## Rejected Candidates

- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) — plausible but too broad beside the more useful correction, activation, and promotion routes already selected.
- [Indexes lower recall when they suppress retrieval that would find more](../../../../theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md) — wiki-plus-search gains do not show that a plausible completeness signal suppressed a better retrieval route. Do not turn a shared indexing topic into evidence for this specific control-flow mechanism.
- [Preserve evidence without making history the next context](../../../../theory/agent-memory-requirements/preserve-evidence-without-loading-history.md) — compatible, but the episode-re-examination note more precisely directs the reader to the correction mechanism. The source does not compare routine transcript loading against selective evidence loading.

## Index Membership

None. The immutable snapshot should not become a durable index target. Source tags, if later assigned to an ingest, do not insert it into generated participating-collection tag membership.

## Synthesis Opportunities

None. The strongest cross-source inference—offline scheduling does not determine whether retention lives in weights, programs, or editable text—is already explicit in the Sleep ingest. A new note would need added mechanism or evidence, not a renamed repetition.

## Maintenance Observations

- The tracked ingest for this exact snapshot basename is missing. That leaves no authored connection surface or durable local analysis target; resolve only through separately authorized ingest work, not by editing the snapshot.
- The historical GBrain review links `../../notes/definitions/conjectural-learning.md`; resolved from its directory, `kb/notes/definitions/conjectural-learning.md` does not exist. An explicit filesystem check confirmed the broken link. No repair was attempted.
- The trace-authority note's open question asks for capture of an unidentified paraphrased source. This snapshot has strikingly similar stage-by-model examples but does not establish that historical identity. A future maintainer should distinguish new supporting material from restoration of original provenance.

## Flags

- Split candidate for future analysis: this multi-assertion source connects to more than five notes across epistemic checking, retrieval/representation economics, and multi-agent coordination. Preserve the captured article intact; any extracted durable theory should separate those claims rather than inherit the entire experiment bundle.
- Preserve the distinction between a transcript's observations and its agent interpretations. The source calls the transcript ground truth, but the episode itself contains mistaken narration; correction requires interpretation rather than trusting all recorded prose.
- Do not promote the Pokémon timing heuristic or the injunction to leave salience unrestricted into general methodology. They are reported task/model-specific observations; the source itself reports that weaker models benefit from more steering.
- Reported wiki gains must retain baselines and costs: wiki plus search outperforms search alone in the large-corpus example, wiki alone is weaker there, some lookup tasks show no clear gain, and wiki construction consumes substantial offline compute.
