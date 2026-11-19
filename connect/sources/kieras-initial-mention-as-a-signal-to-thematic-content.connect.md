---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/kieras-initial-mention-as-a-signal-to-thematic-content.md"
source_has_frontmatter: true
date: "2026-02-28"
depth: standard
---

# Connection Report: Initial mention as a signal to thematic content in technical passages

**Source:** [Initial mention as a signal to thematic content in technical passages](../../../../sources/.snapshots/kieras-initial-mention-as-a-signal-to-thematic-content.md)

## Discovery Trace

**Source collection:** `sources` (snapshot under `kb/sources/.snapshots/`)

**Source collection check:** `kb/sources/COLLECTION.md` exists and was read. Outbound section authorizes links to: theory, agent-memory-systems, agentic-systems, reference, sources, external. Explicitly excludes: `kb/work/`, `kb/instructions/`.

**Snapshot status:** This is an immutable snapshot. No matching `.ingest.md` exists in `kb/sources/`. Per `sources/COLLECTION.md`, snapshots do not carry outbound links — the authored surface lives in the matching ingest report, which is absent. Discovery proceeds from the snapshot's content; recommendations target whichever artifact carries the source's authored surface (a future ingest report).

**Description listing scan — theory:**
- Full titles scan via `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` — 120+ titles reviewed
- Scoped `rg '^description:' kb/theory/ --glob '*.md'` — reviewed for cue/signal/position relevance
- Flagged candidates: `agents-navigate-by-deciding-what-to-read-next.md`, `knowledge-storage-does-not-imply-contextual-activation.md`, `title-as-claim-enables-traversal-as-reasoning.md`

**Description listing scan — sources:**
- Flagged candidate: `position-bias.ingest.md` (direct position-effect parallel)

**Body search — theory:**
- `rg -n "cue|signal|surface feature|initial position|primacy" kb/theory/ --glob "*.md"` — returned hits in `agents-navigate-by-deciding-what-to-read-next.md`, `knowledge-storage-does-not-imply-contextual-activation.md`, `title-as-claim-enables-traversal-as-reasoning.md`, `llm-context-is-composed-without-scoping.md`
- `rg -n "Kintsch|van Dijk|macrostructure|prose comprehension" kb/theory/ --glob "*.md"` — no direct matches

**Body search — sources:**
- `rg -n "position.*bias|order.*flip|position effect" kb/sources/ --glob "*.md"` — returned `position-bias.ingest.md`

**Link following:**
- From `agents-navigate-by-deciding-what-to-read-next.md`: links to `title-as-claim-enables-traversal-as-reasoning.md`, `knowledge-storage-does-not-imply-contextual-activation.md` — confirms thematic cluster around cue diagnosticity
- From `knowledge-storage-does-not-imply-contextual-activation.md`: cites Tulving-Pearlstone and Gick-Holyoak human studies as historical antecedents — Kieras would fit this pattern as another human cue study

**Excluded destination check:**
- `kb/work/prose-readability-notes/position-and-proportion-brief.md` explicitly requests "at least one ingested source on first-mention or serial-position effects in text comprehension" for the human half — strong match, but `work/` is excluded by `sources/COLLECTION.md`

## Connections Found

- [position-bias.ingest.md](../../../../sources/position-bias.ingest.md) — **compares-with**: Kieras (1980) demonstrates that initial mention serves as a cue to thematic content in human readers — a position effect in prose comprehension. The position-bias ingest documents the parallel phenomenon in LLM judges (44.8% median flip rate under order swap). The snapshot provides the human cognitive science background for why position effects exist; the ingest documents the modern computational manifestation. Both show that surface position influences judgments of importance/relevance independent of content.

- [agents-navigate-by-deciding-what-to-read-next.md](../../../../theory/agents-navigate-by-deciding-what-to-read-next.md) — **is-evidence-for**: The note models navigation as follow/skip decisions where "a cue predicts relevance rather than revealing it." Kieras provides empirical evidence that initial mention — a surface-level cue — influences what readers treat as thematic, supporting the general claim that surface features guide attention and comprehension. The note's Pirolli citation covers information-scent cues; Kieras covers positional cues as a specific cue type.

- [knowledge-storage-does-not-imply-contextual-activation.md](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: The note discusses how "prompt context, retrieved notes, tool observations, role assignments, and checklists are the cues that decide what becomes active." Kieras demonstrates that initial mention acts as a cue influencing what readers consider thematic — relevant to the note's broader argument that cue presence and cue quality determine whether stored knowledge affects processing. The note already cites human cue studies (Tulving-Pearlstone, Gick-Holyoak); Kieras would extend this with a prose-comprehension-specific cue mechanism.

## Bidirectional Candidates

None identified. The discovered connections are outbound from the Kieras source; no candidate target requires a return link to this snapshot as a condition of its own argument.

## Reverse-edge Candidates

- [position-bias.ingest.md](../../../../sources/position-bias.ingest.md) → source — **historical-context**: The position-bias ingest documents LLM judge position effects without citing human cognitive science antecedents. A future revision could add a `see-also` or `compares-with` link to the Kieras snapshot (or its ingest) as the human-reading parallel — "LLM judges show position bias; human readers show it too, with initial mention serving as a thematic cue (Kieras, 1980)."

- [agents-navigate-by-deciding-what-to-read-next.md](../../../../theory/agents-navigate-by-deciding-what-to-read-next.md) → source — **evidence**: The note discusses cue diagnosticity but cites Pirolli for information-scent cues. Kieras provides a complementary human-studied cue type (positional/initial-mention) that could strengthen the cue-discussiation argument with empirical grounding from prose comprehension research.

## Off-authorisation Candidates

- [position-and-proportion-brief.md](../../../../work/prose-readability-notes/position-and-proportion-brief.md) — **strong match, excluded destination**: This brief explicitly states it needs "at least one ingested source on first-mention or serial-position effects in text comprehension" for the human reader half. The Kieras snapshot is exactly this source. However, `kb/work/` is excluded by `sources/COLLECTION.md` ("Do not link into `kb/work/`"). Suggestion: the brief's author should ingest the Kieras paper as a tracked source and cite it from the brief; this connect report cannot author that link. The match is noted here because the brief's need is specific and the Kieras content is a near-exact fit.

## Raw Text Candidates

None. The source has frontmatter.

## Rejected Candidates

- [title-as-claim-enables-traversal-as-reasoning.md](../../../../theory/title-as-claim-enables-traversal-as-reasoning.md) — **weak match, retained as see-also consideration**: The note discusses how titles function as signals enabling traversal-as-reasoning. Kieras is about initial mention in prose passages, not KB note titles. The conceptual overlap (position as signal) is real but the domains differ enough that `is-evidence-for` overstates the connection. If the note's "prior work" section is expanded to include cognitive science on positional cues in comprehension, Kieras could become a `see-also` — but as of this discovery run, the fit is too weak for the authorised labels.

- [llm-context-is-composed-without-scoping.md](../../../../theory/llm-context-is-composed-without-scoping.md) — **keyword match only**: The note mentions "primacy/recency effects" in the context of ordering conventions for system prompts. Kieras is about human prose comprehension, not LLM context composition. Rejecting as a keyword-only match without articulation.

## Index Membership

None identified. The source is a 1980 cognitive science paper on prose comprehension; no existing index targets this domain specifically.

## Synthesis Opportunities

None identified in this discovery pass. The source is a single-paper snapshot without multi-claim structure that would suggest synthesis with other notes.

## Maintenance Observations

- **Missing ingest:** This snapshot has no matching `.ingest.md` in `kb/sources/`. Per `sources/COLLECTION.md`, the snapshot is immutable and carries no outbound linking surface. A future ingest report would be the appropriate author of the connections identified here.
- **Workshop brief need:** The `position-and-proportion-brief.md` explicitly requests a human-side source on first-mention/serial-position effects. This snapshot is a near-exact fit. The brief's author should consider ingesting this source (or an equivalent) to satisfy that requirement.
- **Human cue study cluster:** `knowledge-storage-does-not-imply-contextual-activation.md` already cites Tulving-Pearlstone and Gick-Holyoak as human cue studies. Kieras would fit this cluster thematically. If the KB acquires more human cognitive science sources on cueing/position effects, a dedicated note or index may become warranted.

## Flags

- **No-connections finding (partial):** Two theory candidates (`agents-navigate-by-deciding-what-to-read-next.md`, `knowledge-storage-does-not-imply-contextual-activation.md`) pass the articulation test with `is-evidence-for`, but the evidence strength is moderate — Kieras provides background support for cue-discussiation claims rather than directly grounding a specific assertion in those notes.
- **Strong excluded match:** The `position-and-proportion-brief.md` match is the strongest discovered connection but cannot be authored due to destination exclusion. This is a signal that the brief author should address independently.
