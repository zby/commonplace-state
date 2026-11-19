---
description: "Discovery-only connections for ScaleMAS: citation-ranked attention, bounded reads, within-task reuse, and limits on durable learning and acceptance."
type: types/connect-report.md
source: "kb/sources/scaling-multi-agent-intelligence-substrate-centric-coordination.ingest.md"
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: Scaling Multi-Agent Intelligence with Substrate-Centric Coordination

**Source:** [ScaleMAS ingest](../../../../sources/scaling-multi-agent-intelligence-substrate-centric-coordination.ingest.md)

Discovery only. All edges below are recommendations, not authored library state. The ingest was read in full; neither its snapshot nor the implementation was inspected. Numerical results and mechanism descriptions below inherit the ingest's first-party-paper evidence boundary. Produced by the current assistant using `cp-skill-connect`; no agents were spawned.

## Discovery Trace

### Authorization and scope

- Read `kb/sources/COLLECTION.md`, `kb/types/connect-report.md`, and `kb/reports/COLLECTION.md`. Prospected all six named local destinations: notes, reference, agent-memory-systems, agentic-systems, tags, and sources. Excluded work and instructions from candidate discovery.
- Read `kb/notes/COLLECTION.md` before judging note-to-ingest candidates. `evidenced-by` is authorized for this direction, including evidence that qualifies or bounds a claim. No candidate below asserts independent replication or universal corroboration.
- The source has `domains`, not `tags`; no automatic matching-tag pass applied. Read curation and context-engineering heads through topical routing. Curation declares `complete: true`; skipped its by-tag `rg`. Its curated links, not an absent generated tail, supplied the local candidates.
- External authorization permits `derived-from` to the original URL already in the ingest. No external prospecting or browsing was performed.

### Curated heads and title surfaces

Read `README.md` in each of the six destination collections. Also read `kb/tags/curation-README.md` and `kb/tags/context-engineering-README.md`.

For each destination, generated a fresh complete title surface with:

```bash
rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'
```

The combined tool output was truncated; recovered its earlier portions using the read tool. No title index was saved as a project artifact. Titles surfaced the quality-score, context-interface, activation, ephemerality, and experimental-contrast notes; source titles surfaced Agora, DeLM, and SwarmWorld. Reference titles surfaced the memory gap plan. Legacy review titles surfaced HippoRAG; current authored system-review titles surfaced beads_rust. Archived generated reviews were not preferred over authored accounts or tracked source ingests.

### Description and body queries

For each of the same six destinations, ran this description-resolution scan:

```bash
rg '^description:' kb/<destination>/ --glob '*.md' |
  rg -i 'rank|citation|bounded|shared|coordina|substrate|retriev|ephemeral|attention|decomposition|blackboard|stigmer'
```

Recovered the truncated notes-description portion through the read tool. Then ran this focused body-search query in each destination:

```bash
rg -l -i 'citation.weight|inbound.link|stigmerg|blackboard|shared.context|bounded.read|ranking.*truth|attention.allocation' kb/<destination>/ --glob '*.md'
```

A secondary vocabulary pass used:

```bash
rg -l -i 'search.*rank|rank.*search|shared.*store|per.call|cross.task|cross.run' kb/<destination>/ --glob '*.md' | wc -l
```

This was a breadth diagnostic, not a candidate-quality score: notes 57 matches; reference 8; agent-memory-systems 142; agentic-systems 87; tags 4; sources 90. Broad legacy matches reinforced using discriminating descriptions rather than opening every retrieval system. No semantic scores were available.

### Per-destination evaluations and link following

- **Notes:** Curation head → quality-score note → its inbound-link and exploration-slice argument. Kept bounded support for ranking, not the composite score or truth assessment. Context-engineering head → context-operation interface note → knowledge-access synthesis and experimental-contrast note. Read each in full. Kept the fixed-interface/ranking distinction and qualified end-to-end evaluation example. Read activation and ephemerality notes in full to identify useful inbound cases. Read coordination-guarantee note to distinguish available shared information from verified acceptance or final answer commitment.
- **Notes, search-control neighborhood:** Followed lightweight-search-control → search-controller-evaluation and read both. The distinction helps interpret ranking, but ScaleMAS does not supply a stronger acceptance stage for every retrieved message. Rejected a direct empirical endorsement of that acceptance architecture.
- **Reference:** Descriptions and titles singled out the memory gap plan; read it fully. Its ranking step has a concrete consumer for a bounded ranking experiment. Backlink-surfacing hits concern navigation mechanics rather than citation-weighted ranking; not promoted.
- **Agent-memory-systems:** Descriptions singled out HippoRAG's PageRank and top-k passage access; read the review fully. Kept a comparison of graph-mediated bounded retrieval, explicitly distinguishing document-association edges from agent citation/reuse edges. The collection README identifies this corpus as frozen historical evidence; proposed no edits or reciprocal additions there.
- **Agentic-systems:** Read beads_rust fully after its description exposed dependency-aware recommendation ranking and transactionally enforced claims. Rejected the direct connection because work ownership and issue scheduling are not message retrieval; the coordination-guarantee note already supplies the more useful distinction. Broad archived-result hits were not treated as fresh analyses of ScaleMAS.
- **Tags:** Read the tags index and the two topical heads. They route to relevant claims, but sources→tags has no authorized label in the sources contract. No formal tag-head edge proposed. No source tag assignment or membership addition proposed.
- **Sources:** Read Agora, DeLM, and SwarmWorld ingests fully. Agora's existing connections led one hop to DeLM and the coordination-guarantee note, both fully read. Kept Agora and DeLM as precise comparisons: reuse-ranked attention versus durable lineage/diversity, and retrieval ranking versus verification-gated admission. Rejected SwarmWorld as too broad for an additional direct edge: environmental artifact portfolios and agent-free simulator scoring would distract from the ranking/read-interface contribution.
- **External:** Evaluated only the original `https://arxiv.org/abs/2610.16120v1` already present in source metadata. It supplies provenance, not a newly discovered target.

Checked existing inbound links with:

```bash
rg -n -F 'scaling-multi-agent-intelligence-substrate-centric-coordination.ingest.md' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/tags kb/sources --glob '*.md'
```

No matches. Candidate paths were checked for existence before inclusion. Existing outbound references in the ingest are distinguished from new proposals below.

## Connections Found

- [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) — **is-evidence-for**: Existing outbound connection worth retaining, not a missing edge. Removing citation weight inside the fixed ScaleMAS pipeline lowers eight-agent BrowseComp-Plus accuracy from 60.0% to 40.8%. This supports testing dependency reuse to rank already-relevant candidates; it does not validate the full composite score, truth estimation, or low-degree exploration protection.
- [A context-operation interface bounds the projections its policy can realize](../../../../notes/context-operation-interface-bounds-context-policy.md) — **compares-with**: ScaleMAS changes ranking over a fixed message schema and capped search/visit interface. Comparing it with this claim prevents mistaking improved selection inside one interface for evidence that alternative operations or representations are unnecessary.
- [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) — **is-evidence-for**: The paper connects retrieval changes to benchmark outcomes and selected peer-evidence uptake traces, but Pass@N omits single-answer commitment and task-local storage omits durable upkeep. It is a bounded case of which checkpoints were measured and which remain open, not a direct test of the entire architectural synthesis.
- [Discarding all experience-dependent state prevents cross-run accumulation](../../../../notes/ephemeral-computation-prevents-accumulation.md) — **compares-with**: The shared store survives individual agents but is discarded after the task. The comparison distinguishes within-task adaptation and producer-failure availability from cross-task accumulation without implying that ephemeral computation cannot improve within a run.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — **compares-with**: Append-only messages, bounded access, and citation checks address availability and trace structure, while claim truth, adversarial publication, and committed-answer selection remain unestablished. The reader gains a guarantee-by-guarantee comparison rather than a blanket endorsement of shared state.
- [Agora ingest](../../../../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) — **compares-with**: Both use downstream reuse to allocate attention without establishing truth. Agora retains durable Git lineage, excludes self-citation from its evidence score, and adds diversity views after concentrated exploitation; ScaleMAS supplies a controlled citation-weight ablation in a task-local store, allows self-citation weight, and does not test protection for neglected material. These differences delimit a Commonplace ranking experiment.
- [DeLM ingest](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) — **compares-with**: Both coordinate asynchronous workers through shared intermediate results. DeLM tests verification-gated gist admission and recoverable representation layers; ScaleMAS tests citation-ranked selective reads without equivalent truth verification. Admission, visibility, representation, and read prioritization should remain separate comparison axes.
- [HippoRAG historical review](../../../../agent-memory-systems/reviews/HippoRAG.md) — **compares-with**: Both use graph structure and bounded ranked retrieval instead of loading the full store. HippoRAG ranks imported passages through entity/fact graph diffusion; ScaleMAS adds decaying citation weight to lexical relevance over agent messages. The comparison prevents treating every graph-based access method as the same reuse signal or as governed knowledge acceptance.
- [Commonplace agent memory gap plan](../../../../reference/commonplace-agent-memory-gap-plan.md) — **see-also**: Step 9 names ranking and quality-signal work. ScaleMAS offers a bounded experiment input for that work, not an implementation prescription or authorization to replace promotion checks with citation counts.
- Original paper, `https://arxiv.org/abs/2610.16120v1` — **derived-from**: Existing `source` metadata already supplies provenance; no redundant footer edge recommended.

## Bidirectional Candidates

None. Useful new note-to-ingest edges are listed as reverse-edge candidates below rather than duplicated here. No reciprocal edits to frozen historical reviews are proposed.

## Reverse-edge Candidates

These are inbound-link candidates under the notes collection's authorized **evidenced-by** label. A future writer should place the evidence use in body prose and retain the stated limits.

1. [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) → source — **evidenced-by**: Add the citation-weight ablation beside the inbound-link ranking hypothesis. Independently reported ranking evidence could have shown no downstream gain; the reported 60.0% versus 40.8% result supports only this reuse signal inside the fixed pipeline. It does not corroborate the composite score or durable-library transfer. Highest-priority inbound candidate.
2. [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source — **evidenced-by**: Selected successful answers use evidence discovered by peers that the answering agent never opened directly. This supplies a positive within-task uptake example alongside the note's failure cases. Citation-chain membership is partly circular, and selected traces neither estimate prevalence nor independently identify causal semantic uptake.
3. [A context-operation interface bounds the projections its policy can realize](../../../../notes/context-operation-interface-bounds-context-policy.md) → source — **evidenced-by**: Qualify the ranking-ablation result as improved prioritization within fixed message fields, search/visit operations, and read caps. This is a concrete comparison-boundary example, not an experiment testing alternative interfaces or proving that any useful projection is excluded.
4. [Knowledge-access architecture must be evaluated end to end, not by retrieval alone](../../../../notes/knowledge-access-architecture-must-be-evaluated-end-to-end.md) → source — **evidenced-by**: Supply a worked evaluation boundary: ranking ablation plus task scores and selected uptake traces, but no single committed-answer selector, cross-task persistence, or maintenance evaluation. The evidence bounds what an apparent end-to-end gain establishes; it does not directly corroborate every checkpoint in the synthesis.
5. [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) → source — **evidenced-by**: Use ScaleMAS as a bounded case separating append-only availability and citation-structure checks from semantic acceptance and final answer adjudication. Failure tests do not cover plausible misinformation or corrupted shared state. Do not describe untested protections as failed guarantees.

## Off-authorisation Candidates

None. Tag heads were used as routing surfaces, not forced into the absent sources→tags label set. A new authorization is not justified merely to add topical pointers already served by the connected notes.

## Raw Text Candidates

None.

## Rejected Candidates

- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) — The conceptual separation is useful, but ScaleMAS's ranking is not evidence that every read passes a separate stronger acceptance gate. A direct empirical-support edge risks implying an unimplemented guarantee; the quality-score connection carries the practical attention-allocation use more precisely.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — The ranking ablation is compatible with this evaluation advice, but adding it would duplicate the quality-score and evaluation-boundary connections without establishing the stronger acceptance architecture.
- [SwarmWorld ingest](../../../../sources/swarmworld-stigmergic-technological-evolution.ingest.md) — Shared artifacts and collective gains alone are insufficient for another direct connection. Its portfolio and agent-free simulation endpoints answer different questions from bounded citation-ranked message retrieval; Agora and DeLM provide tighter comparisons.
- [beads_rust](../../../../agentic-systems/reviews/beads-rust.md) — Dependency-aware work recommendation and transactionally enforced claims are distinct from retrieving peer messages. The match is not worth an additional direct edge despite a shared ranking vocabulary.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — Valid interpretive context, already reached through the context-interface note. Not retained as another generic methods edge; the report states the ablation boundary explicitly.

## Index Membership

None. No new system-review roster entry is warranted by a paper ingest. The source has no tags; no tag assignment or curated-head membership change was evaluated for authoring.

## Synthesis Opportunities

None requiring a new note. The quality-score proposal already hosts the immediate experiment, and the coordination-guarantee and knowledge-access notes already host the main architectural distinctions. Agora plus ScaleMAS suggest testing reuse ranking alongside low-degree exploration, but the former's diversity intervention and the latter's ranking ablation do not jointly establish a new general claim about durable curation.

## Maintenance Observations

- The sources contract explicitly names tags as a scan destination but gives sources→tags no authorized relationship label. This did not block discovery because the heads served as routing surfaces; revisit only if a concrete source-to-head reader need arises. No contract change is requested by this report.

## Flags

- **Grounding prerequisite for future evidence use:** The source's Quotes section is empty. Before a load-bearing note edit, use the grounding workflow to retain the minimum exact supporting quotes, or explicitly require the pinned snapshot according to the sources contract. This discovery pass does neither and does not claim to have checked the primary paper.
- **Scope tension:** Citation reuse can improve attention allocation while also amplifying errors or excluding low-degree material. The ingest reports no adversarial-citation or durable-library exploration test. Keep that uncertainty beside any transferred ranking recommendation.
- **Split signal, not a source-edit request:** The source connects to at least five notes across curation, context access, learning horizon, and coordination, and makes several independent assertions. If extracting durable theory, separate ranking utility, read-interface bounds, and retention horizon. A multi-claim ingest remains an appropriate faithful analysis; no ingest split or modification is recommended here.
- Existing source links to the theory-builder definition and fixed-decomposition note were observed, not counted as newly discovered edges. No edits, quote appends, index changes, or library mutations were performed.
