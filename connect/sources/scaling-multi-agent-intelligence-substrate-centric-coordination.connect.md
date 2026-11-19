---
description: "Discovery-only connections for ScaleMAS: bounded reads, citation-ranked reuse, dependency navigation, and the limits of task-local coordination evidence."
type: types/connect-report.md
source: "kb/sources/.snapshots/scaling-multi-agent-intelligence-substrate-centric-coordination.md"
source_has_frontmatter: true
date: "2026-10-18"
depth: standard
---

# Connection Report: Scaling Multi-Agent Intelligence with Substrate-Centric Coordination

**Source:** [Scaling Multi-Agent Intelligence with Substrate-Centric Coordination](../../../../sources/.snapshots/scaling-multi-agent-intelligence-substrate-centric-coordination.md)

Discovery only. All edges below are candidates, not authored library links. The snapshot is immutable. Its prospective authored surface is a matching ingest; no name-paired ingest or other ingest mentioning its arXiv identifier was found. Durable citations must eventually target that tracked surface, not this local snapshot. Source claims below are first-party paper reports, not independently reproduced results.

## Discovery Trace

### Setup and recall surfaces

- Read the complete snapshot, including experimental details, prompts, and eight case studies; read the source collection's outbound rules, the connect-report contract, and the reports collection contract. Consulted the notes collection contract for reverse-edge authorization and the tags collection contract for membership eligibility.
- Read curated landings: `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/tags/README.md`, and `kb/sources/README.md`.
- Generated and scanned the complete title surface once for each of those six destinations with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Recovered the truncated listing from the tool's saved output. Brief hits were treated as belonging to their documents; no brief is a proposed target.
- Description scan for every destination: `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'coordinat|citation|retriev|shared|curation|context efficiency|provenance|blackboard'`. This selected the quality-score, activation, navigation, coordination-guarantee, Agora, DeLM, CORAL, and Tracecraft neighborhoods for closer inspection.
- The source has no `tags:`. Read additional topic heads by subject: curation, links, context-engineering, and agent-memory. Curation and links declare `complete: true`; skipped by-tag searches for those heads. The source supplied no tags requiring a by-tag scan for the other heads. No semantic-search services, external browsing, or agents were used. No retrieval scores were available.

### Notes

- Broad scoped body query: `rg -n -i 'citation|stigmerg|blackboard|bounded.*(read|retriev)|shared (context|memory|store)|substrate' kb/notes/ --glob '*.md'` as part of a multi-destination scan. Follow-up: `rg -n -i 'citation (count|weight)|bounded.*read|append.only|referenced by' kb/notes/ --glob '*.md'`.
- Read the quality-score note fully, then checked `rg -n 'citation|inbound|exploration slice' kb/notes/notes-need-quality-scores-to-scale-curation.md`. Kept its specific link-count ranking hypothesis; retained its low-degree exploration caution rather than equating popularity with truth.
- Fully read context efficiency, raw accumulation, activation, coordination guarantees, link-following versus search, inbound/outbound asymmetry, and cross-run ephemerality. Kept specific connections to bounded intake, structured publication, reusable dependencies, navigation modes, and missing correctness guarantees. Ephemerality supplies a scope comparison rather than evidence of cross-run learning.
- Link following: navigation-mode note → inbound/outbound asymmetry neighborhood; backlink proposal → inbound/outbound note; Agora → coordination-guarantee note, DeLM, and Tracecraft. These passes separated citation ranking, reverse-link traversal, and admission verification instead of treating them as one mechanism.

### Reference

- After landing/title/description scans, queried `rg -n -i 'backlink|citation.weight|bounded.*retriev' kb/reference/{navigation.md,proposals/backlink-surfacing.md,commonplace-agent-memory-gap-plan.md}` and `rg -n 'inbound|Agents in the repo' kb/reference/proposals/backlink-surfacing.md`.
- Fully read the backlink-surfacing proposal and followed its theoretical requirement link. Kept one sparse companion edge: ScaleMAS has a concrete reverse-link reuse trace relevant to the proposal's agent-facing delivery question. General storage and navigation architecture were not retained merely because both systems keep data outside context.

### Historical agent-memory systems

- Scoped query: `rg -n -i 'citation|rank|bounded|quality' kb/agent-memory-systems/reviews/{CORAL,tracecraft,HippoRAG}.md`.
- Read CORAL and Tracecraft fully. Kept comparisons on discovery/ranking and work ownership/failure coupling. CORAL's reviewed CLI limits qualify the paper's broad filesystem characterization. HippoRAG surfaced through PageRank terminology but was not promoted: graph retrieval alone is less discriminating than the task-local multi-agent comparisons, and its full review was not evaluated.
- The landing identifies this corpus as frozen historical coverage. Candidates do not propose updating those historical reviews or their matrix.

### Agentic systems

- Title/description scans and `rg -n -i 'claim|duplicate|transaction|retriev|rank' kb/agentic-systems/reviews/{beads-rust,semantic-engine}.md`, followed by `rg -n 'no token budget|not an agent runtime|atomic claim|no claim'` over the same files.
- Rejected Semantic Engine as a primary comparison: it is an ingest workbench without a coordination loop. Deferred beads_rust: atomic work ownership is a possible comparison, but Tracecraft already supplies that axis alongside shared memory. No current authored whole-system review was selected for a source edge in this pass; archived generated reviews were not substituted for current authority.

### Tags, sources, and external

- Queried `rg -n -i 'ranking|citation|navigation|bounded' kb/tags/{links,curation,context-engineering,agent-memory}-README.md`. The heads route to the selected notes. Sources are not participating tag members; no snapshot membership is proposed. The sources outbound prose permits prospecting tags but its label table authorizes no sources→tags relation.
- Sources body query: `rg -n -i 'self.cit|citation|diversity|verification|Pass@|shared context' kb/sources/{agora-git-as-shared-memory-for-collective-autoresearch,decentralized-multi-agent-systems-with-shared-context,towards-a-science-of-scaling-agent-systems}.ingest.md`. Fully read all three. Kept named comparisons; the DeLM ingest introduces a baseline-fidelity question rather than a resolved contradiction.
- Checked companion identity with `test -f kb/sources/scaling-multi-agent-intelligence-substrate-centric-coordination.ingest.md` and `rg -l '2610\.16120|Scaling Multi-Agent Intelligence' kb/sources/ --glob '*.ingest.md'`; neither found a companion.
- External prospecting skipped. The already-loaded primary arXiv URL is eligible for `derived-from`; no open-web candidates were sought. Excluded `kb/work/` and `kb/instructions/` from candidate discovery.

## Connections Found

These recommendations belong on a future authored ingest, not on the snapshot.

- [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) — **is-evidence-for**: ScaleMAS directly varies citation-weighted ranking against BM25-only ranking. At eight agents it reports BrowseComp-Plus accuracy of 60.0% versus 40.8%. This materially tests the narrower proposal that reuse-linked ranking can improve which relevant results receive bounded attention, not the note's complete composite score or long-lived KB quality.
- [Context efficiency is the central design concern in agent systems](../../../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **is-evidence-for**: capped search/visit operations and the group-size experiments bear on the cost of routing shared work into finite contexts. Distinguish bounded intake per read from bounded total context; repeated reads and local history remain separate costs.
- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) — **is-evidence-for**: publication requires a searchable subtask, artifact, rationale, and existing references; ranking and cross-agent versus private-store ablations test structured reuse beyond merely keeping outputs. The paper does not establish all the note's lifecycle or trust requirements.
- [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) — **is-evidence-for**: the prompt explicitly distinguishes wording-based search from address-based visit, and Case 6 traces discovery through a message's reverse references to a reusable lemma. This supplies an agent case for the distinction currently introduced partly through human search evidence; it does not isolate each metadata prescription experimentally.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) — **compares-with**: ScaleMAS specifies immutable message identity, immediate publication visibility, bounded reads, and failure-independent access, but its admission checks establish reference existence and rationale coverage rather than claim correctness. This helps readers separate operational guarantees from semantic adjudication.
- [Discarding all experience-dependent state prevents cross-run accumulation](../../../../notes/ephemeral-computation-prevents-accumulation.md) — **compares-with**: Appendix A explicitly says the datastore is created for one task and discarded with it. Within-task reuse and tolerance of departing producers must not be reported as persistent learning across runs.
- [DeLM ingest](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) — **compares-with**: compare bounded pull retrieval over immutable messages with verified, compact shared gists, a recoverable summary hierarchy, and a dependency-aware work queue. This also identifies which baseline adaptations must be checked before attributing the reported gap to blackboard coordination generally.
- [Agora ingest](../../../../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) — **compares-with**: both use immutable contribution DAGs and downstream reuse to rank attention. Agora excludes self-citation from its downstream evidence and adds diversity views over sustained research; ScaleMAS permits self-citation, decays citation weight, and discards the task datastore. The comparison exposes differences in credit assignment, exploration, and retention horizon.
- [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — **compares-with**: compare architecture-dependent scaling and context overhead under different benchmarks and aggregation rules. ScaleMAS's Pass@N outcome measures whether any agent finds a correct answer, not whether the group can select that answer for commitment; do not treat its gains as a universal rebuttal of task-contingent scaling limits.
- [CORAL historical review](../../../../agent-memory-systems/reviews/CORAL.md) — **compares-with**: compare task-local shared work discovery through citation-ranked bounded messages with filesystem notes, limited CLI views, score-ranked attempts, and heartbeat prompts. The reviewed CORAL already has some bounded views; the useful contrast is the retrieval/ranking contract, not files versus databases.
- [Tracecraft historical review](../../../../agent-memory-systems/reviews/tracecraft.md) — **compares-with**: compare independently reusable completed work with explicit claims, dependency waits, and direct inbox/key reads. ScaleMAS avoids waiting on assigned peers but does not provide exclusive task ownership; Tracecraft's S3 claim guarantee has a weaker HuggingFace fallback. These solve different coordination problems.
- [Backlink surfacing](../../../../reference/proposals/backlink-surfacing.md) — **see-also**: Case 6 offers a concrete use of bounded automatically displayed reverse references to reach a proved lemma. It is a companion case for the proposal's agent-facing inbound-view question, not authorization to adopt generated committed backlink footers.
- [Original ScaleMAS paper](https://arxiv.org/abs/2610.16120v1) — **derived-from**: the already-captured external primary source from which a future ingest would be worked out.

## Bidirectional Candidates

None. Independently justified note→ingest candidates are listed below; no reciprocal edge may target the ignored snapshot.

## Reverse-edge Candidates

Conditional on creation and grounding of the tracked ingest. Under the notes collection's `evidenced-by` authorization, each edge would qualify or bound the note rather than claim universal corroboration.

- [Notes need quality scores to scale curation](../../../../notes/notes-need-quality-scores-to-scale-curation.md) → future ingest — **evidenced-by**: use the citation-weight ablation as bounded evidence for one graph-ranking input; keep the task-local horizon, self-citation allowance, and missing orphan-exploration test explicit.
- [Link-following and search impose different metadata requirements](../../../../notes/link-following-and-search-impose-different-metadata-requirements.md) → future ingest — **evidenced-by**: Case 6 supplies an observed LLM-agent navigation chain involving search, reverse references, and address visits, while leaving causal attribution to the link display unisolated.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → future ingest — **evidenced-by**: Section 3.4 traces correct answers using peer-discovered gold evidence the submitter never opened; Table 2 varies shared versus private access. Together they distinguish stored work, exposure, reuse, and task benefit without proving that every citation is faithful uptake. Case 6 also records verbatim reuse without complete citation.

## Off-authorisation Candidates

None. No useful source→tag formal edge survived the membership check; no label extension is needed just to tag a nonparticipating source.

## Raw Text Candidates

None.

## Rejected Candidates

- [Semantic Engine](../../../../agentic-systems/reviews/semantic-engine.md) — lexical/vector retrieval overlap is not enough: the workbench lacks the multi-agent coordination and bounded prompt-delivery contract at issue.
- [beads_rust](../../../../agentic-systems/reviews/beads-rust.md) — deferred rather than judged incompatible. Its atomic-claim distinction is already represented by the more directly comparable Tracecraft candidate; interface-parity details would distract from this source's main contribution.
- [Agent memory tag head](../../../../tags/agent-memory-README.md) — reject direct membership: the snapshot is outside participating collections, and its datastore does not persist across tasks. A later durable-memory comparison could earn this tag on its own contribution.

## Index Membership

None for the snapshot or a future source ingest: sources are outside the tag collector's participating collections. The context-engineering, links, and curation heads are discovery routes, not recommendations to insert ignored snapshots into curated indexes. No standalone system review was authored or scheduled.

## Synthesis Opportunities

The [quality-score note](../../../../notes/notes-need-quality-scores-to-scale-curation.md), [coordination-guarantee note](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md), and [Agora analysis](../../../../sources/agora-git-as-shared-memory-for-collective-autoresearch.ingest.md), read alongside ScaleMAS, suggest a testable distinction: **dependency uptake may allocate attention without licensing acceptance**. A future synthesis could separate retrieval priority, evidential admission, and exploration protection. ScaleMAS supplies a ranking ablation; Agora supplies sustained concentration and a human diversity intervention; neither establishes a general policy for durable KB curation. This remains a candidate research claim, not a new note.

## Maintenance Observations

- Missing authored connection surface: no matching ingest or same-identifier ingest was found. Any durable source citation requires that surface and appropriate retained quotes or an explicit snapshot-required dependency. Creating it is outside this invocation.
- Baseline characterization needs a bounded follow-up: the retained DeLM analysis describes admission verification and hierarchical recoverability that disappear from a simple “all agents read shared context” characterization. The CORAL review documents CLI limits despite the paper's broad filesystem critique. These are comparison-boundary questions, not demonstrated source errors; inspect the exact adapted baselines before promoting claims about those families.
- The coordination-guarantee note calls Tracecraft task claiming non-atomic, whereas the historical Tracecraft review distinguishes atomic S3 conditional creation from a racy HuggingFace fallback. The apparent disagreement needs backend/commit scoping in a separate maintenance pass; no artifact was changed.

## Flags

- **Multiple extraction lanes:** this source connects to at least five notes across ranking/curation, bounded-context design, navigation, coordination guarantees, and retention horizon, and makes independent assertions. Flag a split candidate for future source-derived theory work; do not split or edit the immutable capture.
- **Bounded read is not bounded run context:** k caps messages per read; reference displays, rationales, repeated reads, and history policy affect actual token intake. The paper caps subtask-plus-artifact length, not an independently specified total token bound for every displayed field.
- **Quality proxy is not correctness:** citation chains partly define the paper's answer-use metric. Its independent gold-document association and ranking ablation are stronger checks, but do not exclude popularity lock-in, adversarial citation, or incorrect high-uptake work. Self-citations can raise weight.
- **Evaluation limits:** third-party tasks use Pass@N; answer selection is explicitly outside scope. Contradiction Audit gives credit when a reported pair includes the edited snippet and does not penalize extra reports, so its recall does not establish precision or sound contradiction adjudication. Selected case studies illustrate mechanisms rather than estimating their prevalence.
- All candidate paths were checked during traversal and are verified again before completion. The snapshot and all library artifacts remain unchanged by this invocation.
