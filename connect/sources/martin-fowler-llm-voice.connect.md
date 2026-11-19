---
description: "Pre-ingest connection discovery for Fowler's LLM Voice: reader rejection, writing as thinking, and audience-dependent delegation limits."
type: types/connect-report.md
source: "kb/sources/.snapshots/martin-fowler-llm-voice.md"
source_has_frontmatter: true
date: "2026-10-30"
depth: standard
---

# Connection Report: LLM Voice

**Source:** [LLM Voice](../../../../sources/.snapshots/martin-fowler-llm-voice.md)

Pre-ingest discovery only, executed with `kb/instructions/cp-skill-connect/SKILL.md` by `gpt-6.1-sol`, without other agents. All edges below are candidates, not authored links. The snapshot has frontmatter; this is not a provisional raw-text report. Its SHA-256 at discovery was `25fb8ea0a572738a986e31a30d7f01e1d5c83059ca5274ee0a5e714b5c522286`.

Fowler reports aversion to perceived model prose independently of accurate authorship detection. He discourages generated drafts, describes composition as a way to expose confusion, and makes exceptions for accessibility and process communication, with ambivalence about translation. These are practitioner judgments and self-reports, not controlled evidence of detection accuracy, cognitive effects, or prevalence.

The authored connection surface is the future name-paired ingest. It does not yet exist. No recommendation licenses modifying the snapshot or making durable citations to this cache path; future citations of Fowler's words use the external URL, and citations of Commonplace's analysis use the eventual tracked ingest.

## Discovery Trace

### Setup and discovery boundary

- Confirmed and fully read [sources contract](../../../../sources/COLLECTION.md), [reports contract](../../../COLLECTION.md), and [connect-report type](../../../../types/connect-report.md), including its schema. Read the source fully and the snapshot, ingest-report and note types. Read the theory contract to judge reverse-edge authorization and the tags contract to judge index eligibility.
- Sources authorizes local prospecting in theory, reference, historical agent-memory-systems, agentic-systems, tags and sources. It excludes work and instructions as destinations. No excluded collection was prospected. Outbound proposals are for ingests, not snapshots.
- Read all six destination `README.md` landings. Generated a fresh full H1 surface using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for each of those six collections. Recovered truncated theory and combined listing output from the tool's full-output logs. For sources, additionally consumed a complete sorted title-only surface (`rg ... | sort | cut -d: -f2-`) because independently generated positional slices were not stable in traversal order. Brief matches were treated as matches on their document, not separate destinations.
- Snapshot has no tags, so there was no source-tag sweep. Read document-system and prose-readability heads by topic. The latter has `complete: true`; skipped its by-tag `rg`. Sources is not a participating collection, so completeness cannot stand in for source discovery.
- All discovery was repository-local. No semantic-search service, MCP tool, browser or external fetch was used. No scores were produced.

### Theory: writing-as-thinking and audience boundaries

- Description query: `rg '^description:' kb/theory/ kb/reference/ --glob '*.md' | rg -i 'writ|prose|reader|comprehension|metaphor|figurative|human|generat'`.
- Initial bounded body search: `rg -n -i 'writing.is.thinking|LLM.voice|uncanny|delegat.{0,30}(think|writ)|prose' kb/theory/ kb/reference/ --glob '*.md' | head -100`. This was a candidate-search sample, not exhaustive body coverage.
- Fully read the adversarial-loop, hidden-goal-relaxation, human-LLM-differences and cheap-generation notes. Kept the first as a comparison and reverse-edge qualification opportunity, the second as a scope comparison, and the third as an audience-design comparison. Did not treat Fowler as establishing the hidden-relaxation mechanism.
- Followed the adversarial-loop note's link to the hidden-relaxation note and their Borretti source neighborhood. Followed the dual-audience note's references to the source-adoption policy and access-cost refinement at title/description resolution; neither adds a necessary candidate beyond the more direct audience note.
- Followed the AI-blindness ingest's effort-signal connection and fully read cheap-generation. Rejected that extra edge: Fowler reports an aesthetic reaction without supplying the effort-cost mechanism. Likewise rejected reverse-compression as an inferred cause of his aversion.

### Reference: no direct system-policy edge

- Read the reference landing and full title surface; scanned descriptions with the shared query above.
- Ran `rg -n -i 'LLM.voice|writing.is.thinking|passive.assent|authentic|uncanny' kb/reference/ --glob '*.md'`; no direct claim match warranted a policy edge.
- Source-adoption policy and ADR 011 are adjacent to audience/transfer questions, but Fowler does not describe Commonplace's source filter or external-reader vocabulary requirements. Rejected rather than adding a generic `see-also`.

### Historical agent-memory-systems: no retained candidate

- Read the frozen-survey landing and full title surface. Description search over this collection, agentic-systems, sources and tags used `rg '^description:' ... --glob '*.md' | rg -i 'writ|prose|readability|voice|comprehension|draft|human.*read|metaphor'`.
- Ran `rg -n -i 'writing.is.thinking|uncanny|LLM.voice|authorial voice' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'`; no matching argument emerged.
- EchoWiki's voice-transcript compilation appeared in descriptions, but spoken-input capture is not perceived authorial voice. Focused follow-up `rg -n -i 'accessibility|translation|prose' kb/agent-memory-systems/reviews/echowiki.md kb/agentic-systems/reviews/academic-research-skills.md` supplied no shared delegation mechanism. Rejected the lexical match, not a judgment about the systems' quality.

### Agentic-systems: no retained candidate

- Read the landing and full H1 surface, including archive entries exposed by the command. Used the description and exact-phrase body queries above.
- Academic Research Skills was an obvious writing-workflow hit, but its integrity gates do not establish human reader aversion, cognitive delegation loss or accessibility effects. Rejected the topic-level association. No archive or comparison-table entry was promoted as evidence from a generic prose match.
- An earlier broad body query containing `authentic` also matched authentication text. Discarded that search noise and reran the narrower writing/voice query above.

### Tags: routing signal, not membership

- Read the tags landing, complete title surface, document-system head and prose-readability head. Scanned tag descriptions with `rg '^description:' kb/tags/ --glob '*.md' | rg -i 'prose|document|evaluation'`.
- Followed document-system to the dual-audience note and prose-readability to its figurative-wording and reverse-compression neighborhood at title/description resolution. Fowler's “load-bearing tapestries” aside does not establish figurative-inference errors. Rejected it as a theory edge.
- Source collection names tags as a prospecting destination but supplies no source→tags label. No forced unlabeled edge: neither a tag-head link nor membership adds enough beyond the concrete candidates. No source tag was assigned.

### Sources: closest comparisons

- In addition to the complete title scan and shared description query, ran `rg '^description:' kb/sources/ --glob '*.md' | rg -i 'Graham|Grunewald|Borretti|AI.blind|AI;DR|Karlsson|Karnofsky'`.
- Ran `rg -n -i 'uncanny|LLM.voice|writing.is.thinking|passive.assent|AI.blind' kb/sources/ --glob '*.md'`.
- Fully read Borretti, Grunewald, Cymerys, both AI-blind/AI;DR discussion ingests, Graham and Karlsson's writing-to-think ingest. Kept Borretti for composition versus rendering, Grunewald for the scope of drafting prohibitions and exceptions, Cymerys for rejection despite uncertain provenance, and Graham for the composition operation itself.
- Link following: Cymerys → AI;DR discussion → Grunewald; Graham → Karlsson and the adversarial-loop note; Borretti → hidden-relaxation and dual-audience notes. These chains distinguish lost thought-testing from reader reception rather than merging them as “AI style.”
- The discussions add useful false-positive and accessibility boundaries, but were rejected as extra edges because Cymerys and Grunewald already provide the discriminating comparisons. Karlsson adds explicit counterexample procedure absent from Fowler; omitted as a second-hop expansion rather than a necessary source connection. Karnofsky's inquiry-routing mechanism was screened by description and existing link context, not claimed as fully assessed.

### External

- Evaluated only the already-loaded [original article](https://martinfowler.com/bliki/LLM-Voice.html) for `derived-from`. No open-web prospecting. Fowler's links to Say Your Writing and Parkinson's-related material remain source context; neither was read or independently assessed as a connection candidate.

## Connections Found

Candidates below are for the future ingest's authored surface.

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) — **compares-with**: Fowler's resistance to generated drafts confronts the note's proposed separation of rendering and judgment. Following the link lets a workflow designer distinguish reconstruction of thought-testing from removal of an unwanted prose voice; success at one need not establish the other.
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) — **compares-with**: Fowler's account of writing through confusion shares the composition-as-discovery boundary, while his allowance for process letters provides a contrasting settled-output use. His introspection does not establish the note's conjectural dropped-constraint mechanism.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) — **compares-with**: Fowler explicitly distinguishes communicating with people from possible model-only documentation and process communication. The note translates that audience distinction into KB document-design questions, without treating process communication as equivalent to an LLM reader.
- [Human Routers of Machine Words](../../../../sources/borretti-human-routers-of-machine-words.ingest.md) — **compares-with**: both argue that drafting can be the thinking rather than a cosmetic rendering step. Fowler adds explicit accessibility exceptions and a reception complaint that should not be reduced to Borretti's verification-burden account.
- [Why You Should Almost Never Use AI to Write Anything Substantive](../../../../sources/why-almost-never-use-ai-to-write-anything-substantive.ingest.md) — **compares-with**: compare the scope of draft-generation prohibitions, post-editing confidence, translation and disclosure. Fowler is wary even of rephrasing, but accepts accessibility assistance; Grunewald's account foregrounds passive assent and allows some deliberate line edits. The comparison prevents importing one undifferentiated “never use AI” rule.
- [I'm becoming AI-blind](../../../../sources/im-becoming-ai-blind.ingest.md) — **compares-with**: both report withdrawal from perceived AI prose despite uncertain provenance. Cymerys proposes learned suppression from repeated low-yield exposure; Fowler describes an uncanny-valley response. This separates rival explanations for rejection instead of assuming either mechanism or accurate detection.
- [Putting Ideas into Words](../../../../sources/putting-ideas-into-words.ingest.md) — **compares-with**: Graham separates exact-word commitment from neutral-reader rereading, making Fowler's more compact “writing brings coherence” claim operationally inspectable without assuming that physical writing is the unique cause.
- [LLM Voice — original source](https://martinfowler.com/bliki/LLM-Voice.html) — **derived-from**: the future ingest analyzes this already-captured external essay. No network or current-page verification was performed.

## Bidirectional Candidates

None. No reciprocal edge is proposed merely to mirror the outbound comparisons.

## Reverse-edge Candidates

These are conditional future edges to the eventual tracked ingest, never to the snapshot. The future endpoint is absent, so no live link to it is included.

- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../theory/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) → future Fowler ingest — **evidenced-by**: qualify the outcome claim by separating recovered argumentative scrutiny from human acceptance of the resulting voice. Fowler's reported professional-editor exception also limits a categorical “editing can never remove the voice” reading. This is a scope challenge, not a test corroborating or refuting the adversarial loop.
- [Human-LLM differences are load-bearing for knowledge system design](../../../../theory/human-llm-differences-are-load-bearing-for-knowledge-system-design.md) → future Fowler ingest — **evidenced-by**: use the human-reader aversion report to qualify what a dual-audience design must consider, while retaining its anecdotal force. A human's accessibility benefit can warrant tolerating a disliked voice; human readership alone does not settle the delegation rule. The theory contract authorizes `evidenced-by` to sources when its context says the source qualifies or bounds the claim.

## Off-authorisation Candidates

None. Tags were screened but no source→tag connection earned retention without an authorized label.

## Raw Text Candidates

None.

## Rejected Candidates

- [Cheap generation breaks text volume as an effort signal](../../../../theory/cheap-generation-breaks-text-volume-as-an-effort-signal.md) — Fowler's stated aversion does not identify inferred author effort or verification cost as its cause; using it as evidence for that mechanism would overread the source.
- [Reverse compression](../../../../theory/reverse-compression-is-when-llm-output-expands-without-adding.md) — no demonstrated expansion-to-payload comparison in Fowler. Unwanted voice is not equivalent to low informational yield.
- [Figurative wording can suggest relations that the target claim does not justify](../../../../theory/figurative-wording-imports-source-domain-entailments-unless-mapped.md) — the tapestries aside is a style cue, not an analysis of invalid metaphorical entailments.
- [AI;DR discussion](../../../../sources/hacker-news-ai-dr-ai-didnt-read.ingest.md) and [AI-blindness discussion](../../../../sources/hacker-news-im-becoming-ai-blind.ingest.md) — useful boundary inventories, but additional outbound links would duplicate the selected reception and delegation comparisons.
- [How to think in writing](../../../../sources/how-to-think-in-writing.ingest.md) — useful second-hop procedure; Fowler supplies no comparable conjecture/premise/counterexample sequence. Graham is the closer comparison for the operation Fowler actually describes.
- [EchoWiki](../../../../agent-memory-systems/reviews/echowiki.md) — voice transcripts are not authorial prose voice.
- [Academic Research Skills](../../../../agentic-systems/reviews/academic-research-skills.md) — writing-pipeline overlap does not establish a relevant shared mechanism.

## Index Membership

None. Sources is excluded from tag membership under the tags contract. An eventual ingest may use source-scoped search tags after independently checking inclusion conditions; this run recommends no assignment and no edits to curated heads.

## Synthesis Opportunities

A bounded question for later investigation, not a new finding: **Can a drafting workflow recover thought-testing while still failing human reception?** The adversarial-loop note addresses scrutiny; Fowler and the AI-blindness ingest supply distinct reception concerns. A useful experiment would vary review rigor, style, disclosed provenance and reader purpose independently. Existing sources already separate style detection from substance, so another generic anti-AI-writing note would duplicate the neighborhood. Fowler's accessibility exception is a boundary on any proposed optimization for voice, not evidence of a universal workflow ranking.

## Maintenance Observations

- The Borretti ingest's recommended action still names `kb/notes/`, recommends linking to a snapshot, and says the unifying writing-as-thinking note is missing, although the hidden-relaxation and adversarial-loop notes now exist. Future maintenance should reconcile that historical recommendation with current placement, citation rules and retained theory.
- The Grunewald ingest recommends an `evidenced-by` link to its snapshot; current source and theory contracts require the tracked ingest instead. No correction was made.

## Flags

- Preserve two independent issues during ingest: perceived voice can affect reception even when detection is wrong; delegating composition can remove thought-testing even when the voice is undetectable. Neither establishes the other.
- Do not promote the blanket drafting prohibition as tested KB methodology. Fowler's professional-editor, accessibility, translation and process-communication cases materially bound it.
- Seven local candidates span composition, reader reception and audience-dependent delegation, and the source makes multiple independent assertions. Treat the future analysis as a split candidate at the claim level; do not split or alter the immutable snapshot. Separate theory claims only if later promotion is justified.
- Reverse edges await creation and grounding of the durable ingest. No ingest creation, quote retention, source promotion or library mutation was authorized in this run.
