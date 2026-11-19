---
description: "Discovery report for possible KB connections from the Epistemic Case Study Competition brief"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/epistemic-case-study-competition.md"
source_has_frontmatter: true
date: "2026-08-24"
depth: standard
---

# Connection Report: Lab Leaks, Black Holes, and Eggs: Epistemic Case Study Competition

**Source:** [Lab Leaks, Black Holes, and Eggs: Epistemic Case Study Competition](../../../../sources/.snapshots/epistemic-case-study-competition.md)

## Discovery Trace

**Curated heads:**

- Read the source artifact and `kb/sources/COLLECTION.md`, then read the curated heads for all five authorised local destinations: `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Read `kb/notes/tags-README.md` and the evaluation, discovery, links, agent-memory, document-system, and KB-maintenance topic heads. The source tags `epistack`, `epistemology`, and `knowledge-bases` have no matching destination tag heads or tagged-artifact surfaces, so no tag-specific complete head could replace discovery.

**Full title and description surfaces:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` separately over `kb/notes/`, `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/`. The strongest title and description matches concerned claim-level provenance and warrant, reasoning evaluation, causal compounding, interoperability, claim-graph memory systems, source-first ingestion, knowledge-centric transfer, and analysis dispersion.

**Body searches:**

- Notes: ran focused searches for `compound|reusab|interoperab|refinable|living knowledge|evolv.*time|multiple (people|teams)|shareable`; `claim.*provenance|provenance.*claim|attribut.*claim|source.*claim|inference structure|discourse structure|crux|correlated evidence|rhetorical|epistemic status|caveat|uncertaint`; `adversarial|calibrat.*confidence|confidence.*calibrat|missing (source|perspective)|oracle|assessment|evaluation|reasoning production|reasoning evaluation`; and `flatten|preserv.*detail|resolution.switch|granular|nuance|interoperab|living knowledge|updateable|evolv.*time`.
- Reference: searched for `epistem|knowledge base|compounding|interoperab|provenance|source.*claim|assessment|evaluation|case stud|living|adversarial|trustworthy`. `Commonplace as an instrument` was the only shipped-system companion whose unresolved evaluation boundary materially intersects the brief.
- Agent-memory systems: searched for `research|scient|epistem|claim|provenance|evidence|trust|adversarial|interoperab|temporal|event-sourced|living|source.*relationship|inference|review`. Quicky Wiki and Secure LLM-Wiki passed because they expose different implemented boundaries across provenance, structure, assessment, and adversarial trust.
- Agentic systems: searched for `research|knowledge|ingest|evaluation|review|provenance|scient|source|workflow|agent`. Semantic Engine passed as a concrete implementation of the ingestion layer; broader execution harnesses lacked the source-to-claim and belief-assessment focus.
- Sources: searched for `epistem|knowledge base|knowledge-base|compounding|flywheel|interoperab|shared.*context|research workflow|scientific review|investigation|analyst|disagreement|provenance|claim graph|evidence base|trustworthy|adversarial`. The Karpathy digest, Knowledge-Centric Self-Improvement paper, and Many AI Analysts experiment each supplied a distinct named comparison axis.
- External destinations are authorised, but open-web prospecting is forbidden. The source URL was already present as provenance and no additional already-known external target was needed.

**Link following:**

- Followed the raw-accumulation note through provenance, trust, and composability neighbors. This retained the broad ingress transformation rule and rejected a separate production-time history edge as duplicative for this requirements brief.
- Followed the compounding notes into Knowledge-Centric Self-Improvement and Knowledge Flywheels. The paper provides the stronger controlled transfer result; the brief and public flywheel framing do not themselves establish causal compounding in a later improvement episode.
- Followed the interoperability note into resolution-switching and schema neighbors. The brief's explicit “interoperability without flattening” problem is better matched by the authority-and-compatibility distinction than by any one content taxonomy or note-granularity choice.
- Read the Quicky Wiki, Secure LLM-Wiki, Semiont, and AutoSci reviews and followed their relevant provenance, trust, lifecycle, and research-workflow connections. Quicky Wiki and Secure LLM-Wiki retained direct comparison axes; Semiont and AutoSci did not cover enough of the requested assessment surface.
- Read the Karpathy LLM Wiki, Knowledge-Centric Self-Improvement, Knowledge Flywheels, GitHub for Context, and Many AI Analysts ingests. The retained sources respectively cover the named personal-wiki baseline, controlled reusable-knowledge transfer, and residual disagreement after auditing.

## Connections Found

- [Raw accumulation does not create usable memory](../../../../notes/raw-accumulation-does-not-create-usable-memory.md) -- **rests-on**: the brief's ingestion layer turns a messy evidence base into attributed claims, cross-source identities, metadata, and relationships; those are the handles and scope transformations that distinguish usable memory from stored material.
- [Theory warrant should be tracked at the finest granularity evidence licenses](../../../../notes/theory-warrant-tracked-at-the-finest-granularity-evidence-licenses.md) -- **rests-on**: representing support, caveats, and uncertainty without transferring warrant to neighboring claims requires the claim- or bundle-level scope discipline this note specifies.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- **rests-on**: the proposed assessment layer must inspect whether evidence supports conclusions, distinguish rhetoric from warrant, find cruxes, and detect performed settling; accepting a polished answer cannot perform those evaluations.
- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) -- **compares-with**: the brief calls reusable and refinable analyses “compounding,” while the note reserves compounding for evidence that an earlier retained gain causally improves a later improvement episode; reuse, transfer, and sequential accumulation should therefore be measured separately.
- [A universal knowledge framework demotes content taxonomies to defaults](../../../../notes/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md) -- **compares-with**: the brief asks for interoperability without flattening diverse investigations, while the note argues that interoperability needs shared authority or enforced compatibility at the exchange boundary rather than one universal content taxonomy.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- **see-also**: the brief supplies an external task profile for composing retrieval, representation, review, and validation across ambiguous cases, precisely where the instrument report says Commonplace still lacks outside-system and transfer evidence.
- [Quicky Wiki](../../../../agent-memory-systems/reviews/quicky-wiki.md) -- **compares-with**: Quicky Wiki implements a document-derived claim graph with provenance, evidence, confidence events, dependency and contradiction edges, red-team checks, and lifecycle operations, but its missing exact source spans and heuristic confidence illustrate why the brief's full assessment layer remains harder than graph construction.
- [Secure LLM-Wiki](../../../../agent-memory-systems/reviews/secure-llm-wiki.md) -- **compares-with**: its atomic claims, provenance, trust tiers, quarantine, and independent adversarial review directly address scrutiny-resistant ingestion, while its coarse read-back and limited argument structure expose the tradeoff between claim-level control and navigable discourse or inference structure.
- [Semantic Engine as ingest infrastructure](../../../../agentic-systems/reviews/semantic-engine.md) -- **compares-with**: its source-first chunking, offset tests, embeddings, querying, and visualization implement a bounded ingestion and exploration workbench; it deliberately stops before the claim relationships and belief assessment that would complete the brief's stack.
- [Ingest: Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) -- **compares-with**: the controlled system lets stateless agents contribute, critique, synthesize, retrieve, and transfer scoped typed knowledge across held-out tasks and models, making it the closest empirical realization of reusable multi-agent knowledge here; fixed benchmarks and symbolic oracles leave the brief's open-ended epistemic cases and causal compounding claim untested.
- [Ingest: LLM Wiki](../../../../sources/karpathy-llm-wiki.ingest.md) -- **compares-with**: this is the richer local account of the Karpathy personal-wiki approach named by the brief, moving from raw agent logs to curated pages, schemas, indexes, and linting; the competition asks for the additional multi-user interoperability, disagreement, and assessment machinery that the personal workflow does not establish.
- [Ingest: Many AI analysts, one dataset](../../../../sources/many-ai-analysts-one-dataset-agentic-data-science-multiverse.ingest.md) -- **compares-with**: compliant agents given the same data, hypothesis, and estimand still produced widely divergent results, and auditing reduced invalid work without removing persona steering; this is a concrete stress case for the brief's requirements around correlated evidence, cruxes, confidence, missing perspectives, and comparative assessment.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) -- rejected as a separate durable edge because the brief states a provenance requirement but does not supply an observed production-time capture failure; the broader ingress transformation connection already carries the actionable requirement.
- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) -- rejected because its structural and maintenance proxies assess KB health, not whether evidence warrants belief across contested case studies.
- [Semiont](../../../../agent-memory-systems/reviews/semiont.md) -- rejected despite its source-grounded annotations and event-sourced history because it supplies little belief assessment; Quicky Wiki and Secure LLM-Wiki provide more discriminating comparisons to the three-layer stack.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) -- rejected because the reviewed branch is primarily an empty structured-research scaffold and does not demonstrate the full scientific lifecycle needed to evaluate the brief's workflow claims.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected because its retained-learning loop is specific to software delivery, and the causal distinction between accumulation and compounding is already reached directly through the theory note.
- [Ingest: Knowledge Flywheels](../../../../sources/knowledge-flywheels-2085043769297277114.ingest.md) -- rejected because it is the coauthor's public agenda framing; the Knowledge-Centric Self-Improvement paper is the stronger empirical comparison and states the relevant experimental bounds.
- [Ingest: The GitHub for Context Doesn't Exist Yet](../../../../sources/the-github-for-context-doesn-t-exist-yet-2077772169455530152.ingest.md) -- rejected because it concerns portability and governance of executable organisational context rather than source, claim, inference, and belief assessment for epistemic disputes.
- [Ingest: LLM Knowledge Bases](../../../../sources/llm-knowledge-bases-something-i-m-finding-very-useful.ingest.md) -- rejected because the longer LLM Wiki digest covers the same Karpathy lineage with more specific architecture and maintenance detail.

## Index Membership

None

## Synthesis Opportunities

- The brief, Quicky Wiki, Secure LLM-Wiki, Semantic Engine, and Knowledge-Centric Self-Improvement support a comparative matrix for an epistemic stack: ingestion, structure, and assessment crossed with provenance unit, support model, uncertainty representation, authority, update lifecycle, interoperability boundary, and available oracle. This would distinguish implemented components from claimed end-to-end trustworthiness.
- The brief, the interoperability note, the accumulation-versus-compounding note, and Knowledge-Centric Self-Improvement expose three claims that should not be collapsed: an artifact can travel across systems, improve a later task, or make a later improvement episode more productive. Each requires a different test.

## Maintenance Observations

None

## Flags

- The target is an immutable snapshot and no matching `kb/sources/epistemic-case-study-competition.ingest.md` exists. All outbound candidates belong on that future authored ingest surface, never on the snapshot; durable reverse edges must likewise wait for an authored target.
- Split candidate: a future ingest should separate the brief's ingestion, argument/discourse structure, belief assessment, interoperability, and compounding propositions rather than treating the “full epistemic stack” as one claim.
- Evidence-status limit: this is an official competition brief and design agenda. It is authoritative about FLF's requirements, cases, and judging intent, but it does not demonstrate that the proposed layers are sufficient, that existing work is generally single-user, or that reusable analyses causally compound.
