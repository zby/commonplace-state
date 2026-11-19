---
description: "Discovery report for possible KB connections from Kieras 1980 ingest"
type: types/connect-report.md
source: kb/sources/kieras-initial-mention-as-a-signal-to-thematic-content.ingest.md
source_has_frontmatter: true
date: "2026-02-28"
depth: standard
---

# Connection Report: Initial mention as a signal to thematic content in technical passages

**Source:** [Ingest: Initial mention as a signal to thematic content in technical passages](../../../../sources/kieras-initial-mention-as-a-signal-to-thematic-content.ingest.md)

## Discovery Trace

**Collection:** `kb/sources/`
**Authorized outbound labels (from COLLECTION.md):**
- `derived-from` → external
- `is-evidence-for` → theory, agent-memory-systems
- `abstracted-from` → theory
- `rests-on` → theory
- `compares-with` → theory, sources, agent-memory-systems, agentic-systems
- `defined-in` → theory/definitions
- `see-also` → theory, reference, sources, agent-memory-systems, agentic-systems, external

**Source collection posture:** No frontloading declaration; `kb/work/` excluded from destinations.

### Destination: theory

**Titles listing scan:**
- Full title scan over `kb/theory/` completed (100+ notes)
- Flagged for deeper inspection: `agents-navigate-by-deciding-what-to-read-next.md`, `knowledge-storage-does-not-imply-contextual-activation.md`, `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md`, `llm-context-is-composed-without-scoping.md`

**Scoped `rg` description listing:**
- `rg '^description:' kb/theory/ --glob '*.md'` — reviewed all descriptions for position/comprehension/cue relevance
- No additional candidates surfaced beyond those identified through body search

**Body search:**
- `rg -n "position effect|primacy|initial mention|prose comprehension|reading cue|thematic" kb/theory/ --glob "*.md"` — hits:
  - `agents-navigate-by-deciding-what-to-read-next.md:14` — "a cue predicts relevance rather than revealing it" (core concept match)
  - `knowledge-storage-does-not-imply-contextual-activation.md` — cites Tulving-Pearlstone and Gick-Holyoak as human cue studies (cluster match)
  - `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md:20` — mentions "primacy and recency bias in long-context retrieval" (phenomenon overlap, but different mechanism)
  - `llm-context-is-composed-without-scoping.md:30` — mentions "primacy/recency effects" (phenomenon overlap)

**Link following:**
- From `agents-navigate-by-deciding-what-to-read-next.md`: follows link to Pirolli ingest — confirms the note already draws on human cue research; Kieras would complement Pirolli with prose-comprehension-specific evidence
- From `knowledge-storage-does-not-imply-contextual-activation.md`: existing citations to Tulving-Pearlstone and Gick-Holyoak — confirms the note has a human cue studies cluster that Kieras could extend

**Evaluation:**
- `agents-navigate-by-deciding-what-to-read-next.md` — **passes articulation test**: Kieras provides empirical grounding for the claim that surface features guide relevance judgments; complements Pirolli's information-scent cues with prose-comprehension-specific evidence. Label: `is-evidence-for` (reader-need: this source bears materially on the target claim). Strength: moderate — background support for cue-diagnosticity claims, not primary grounding.
- `knowledge-storage-does-not-imply-contextual-activation.md` — **passes articulation test**: Kieras extends the human cue studies cluster with a prose-comprehension-specific mechanism (initial mention as thematic cue). Label: `is-evidence-for`. Strength: moderate.
- `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` — **rejected**: mentions primacy/recency as context-dilution phenomenon; Kieras is about thematic signaling, not context competition. Different mechanism, weak connection.
- `llm-context-is-composed-without-scoping.md` — **rejected**: already cites Freebody & Anderson for primacy/recency; Kieras's thematic-cue angle is a different claim. The note invokes position effects as a phenomenon that ordering conventions exploit; Kieras documents a specific causal mechanism for one position effect. Too indirect.

### Destination: sources

**Titles listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` — reviewed for position/reading/comprehension relevance
- Flagged: `position-bias.ingest.md`, `freebody-anderson-serial-position-rated-importance-1981.ingest.md`

**Body search:**
- `rg -n "position-bias|order.*flip|initial mention|thematic cue" kb/sources/ --glob "*.md"` — confirmed both flagged sources

**Evaluation:**
- `position-bias.ingest.md` — **passes articulation test**: Both document surface-position effects on importance/relevance judgments. Kieras = human comprehension cue (initial mention shifts thematic identification); position-bias = LLM judgment-order artifact (44.8% median flip). Shared axis: position influences judgments, independent of content. Different mechanisms and genres. Label: `compares-with` (reader-need: compare on named shared axis). The ingest's own "Connections Found" section already identifies this.
- `freebody-anderson-serial-position-rated-importance-1981.ingest.md` — **passes articulation test**: Both are human cognitive science on position effects in reading. Freebody & Anderson: serial position and rated importance independently predict recall (primacy stronger than recency). Kieras: initial mention functions as thematic cue, challenging the "important content happens to appear first" explanation. Different angles: Freebody & Anderson confirms position effects exist alongside importance; Kieras proposes a mechanism (cue-based signaling) for why position matters. Label: `see-also` (reader-need: adjacent companion). Both share the occasion "What human-reader evidence can inform the planned Commonplace note about position, proportion, and what readers retain?"

### Destination: agent-memory-systems

**Description listing scan:**
- `rg '^description:' kb/agent-memory-systems/ --glob '*.md'` — reviewed for relevance to reading cues, position effects, comprehension
- No candidates with plausible match for Kieras's claim

**Evaluation:**
- No genuine connections. The agent-memory-systems collection covers external system reviews and comparisons; Kieras is human cognitive science on prose comprehension, not directly applicable to memory system design.

### Destination: agentic-systems

**Description listing scan:**
- `rg '^description:' kb/agentic-systems/ --glob '*.md'` — reviewed for relevance
- No candidates with plausible match

**Evaluation:**
- No genuine connections. Agentic-systems covers external agent runtime/orchestration reviews; no overlap with Kieras's human reading comprehension domain.

### Destination: reference

**Description listing scan:**
- `rg '^description:' kb/reference/ --glob '*.md'` — reviewed for relevance
- No candidates with plausible match

**Evaluation:**
- No genuine connections. Reference collection covers Commonplace system documentation; Kieras is external source material, not system-relevant.

### Destination: external

**Evaluation:**
- Skipped. The `external` destination is authorization for already-known targets, not a prospecting surface. The ingest's `source` field (https://doi.org/10.3758/BF03198274) already provides the external link. No additional external targets were supplied or present in loaded context.

## Connections Found

- [position-bias](../../../../sources/position-bias.ingest.md) -- **compares-with**: Both document surface-position effects on importance/relevance judgments in different reading systems. Kieras shows initial mention shifts what human readers treat as thematic, independent of content importance (cue-based signaling). Position-bias shows LLM judges flip their winner 44.8% of the time under order swap (judgment-order artifact). Same phenomenon, different mechanisms and genres; citing both strengthens any claim that position effects are not platform-specific.

- [agents-navigate-by-deciding-what-to-read-next](../../../../theory/agents-navigate-by-deciding-what-to-read-next.md) -- **is-evidence-for**: Kieras provides empirical grounding for the general claim that surface features guide what readers treat as relevant. The note models navigation as follow/skip decisions where "a cue predicts relevance rather than revealing it"; Kieras documents one concrete surface cue (initial mention) and its effect on thematic identification. Complements the information-scent cues drawn from Pirolli. Evidence strength: moderate — background support for cue-diagnosticity claims, not primary grounding for the note's core argument.

- [knowledge-storage-does-not-imply-contextual-activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: Kieras extends the human cue studies cluster this note already draws on (Tulving-Pearlstone, Gick-Holyoak) with a prose-comprehension-specific mechanism: initial mention as a thematic cue. The note argues that cue presence and cue quality determine whether stored knowledge affects processing; Kieras provides evidence that surface-level features (initial position) can guide macrostructure construction. Evidence strength: moderate — supports the broader cue-diagnosticity claim, not direct evidence for the note's specific assertions about LLM activation.

- [freebody-anderson-serial-position-rated-importance-1981](../../../../sources/freebody-anderson-serial-position-rated-importance-1981.ingest.md) -- **see-also**: Both are human cognitive science on position effects in reading, ingested for the same planned note on position, proportion, and what readers retain. Freebody & Anderson confirms that serial position and rated importance independently predict recall (primacy stronger than recency); Kieras challenges the received interpretation of primacy by proposing initial mention as an active thematic cue rather than a byproduct of content placement. Different angles on related phenomena; useful to cite together when discussing the human evidence base for position effects.

## Bidirectional Candidates

None. The source's outbound connections do not suggest strong return-path needs beyond what the target notes already carry or would carry through their own connect runs.

## Reverse-edge Candidates

- [Planned note: position, proportion, and what readers retain](../../../../theory/position-proportion-and-what-readers-retain.md) → source -- **compares-with**: The ingest's "Recommended Next Action" identifies this as the primary consumer. The note should use Kieras as the human-reader evidence anchor and include a `compares-with` link back to this ingest, paired with a `compares-with` link from this ingest to position-bias. This would make the cross-system comparison traceable in both directions. (Note: the target note does not yet exist; this is a forward-looking candidate.)

- [agents-navigate-by-deciding-what-to-read-next](../../../../theory/agents-navigate-by-deciding-what-to-read-next.md) → source -- **is-evidence-for**: The note would benefit from citing Kieras as empirical support for the cue-diagnosticity claim, alongside its existing Pirolli citation. This would ground the abstract "cue predicts relevance" claim in a concrete human study.

- [knowledge-storage-does-not-imply-contextual-activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **is-evidence-for**: The note could extend its human cue studies cluster to include Kieras, strengthening the prose-comprehension dimension of its cue-quality argument.

## Off-authorisation Candidates

None. All candidates that passed the articulation test had an authorized label available.

## Raw Text Candidates

None. The source is an ingest report with frontmatter, not a raw text file.

## Rejected Candidates

- `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` -- mentions primacy/recency bias in long-context retrieval (Liu et al. 2023); Kieras is about thematic signaling via initial mention, not context dilution. Different mechanism, weak connection. Rejected.

- `llm-context-is-composed-without-scoping.md` -- invokes primacy/recency effects and already cites Freebody & Anderson for that claim. Kieras's thematic-cue mechanism is a different claim; connecting would be indirect. Rejected.

- Agent-memory-systems candidates -- no plausible match for Kieras's human prose-comprehension domain.

- Agentic-systems candidates -- no plausible match.

- Reference candidates -- no plausible match.

## Index Membership

None identified. The source is a tracked ingest, not an index entry.

## Synthesis Opportunities

None identified. The source connects to existing notes on cue diagnosticity and position effects but does not imply a higher-order claim that would warrant a new synthesis note.

## Maintenance Observations

- The source's "Connections Found" section already identifies the position-bias `compares-with` link and the two theory `is-evidence-for` links. This connect run independently verifies those candidates and adds `freebody-anderson-serial-position-rated-importance-1981.ingest.md` as a `see-also` candidate.
- The source's "Recommended Next Action" identifies a planned note on position, proportion, and what readers retain as the primary consumer. That note does not yet exist; when it does, it should be connected via `compares-with`.
- The source and freebody-anderson share the same occasion ("What human-reader evidence can inform the planned Commonplace note about position, proportion, and what readers retain?") and were ingested on the same date (2026-02-28). They form a natural pair for the planned note's human-evidence section.

## Flags

None. The source makes a single primary claim (initial mention functions as a thematic cue in human readers) with moderate reach; it connects to fewer than five notes across two topic areas (cue diagnosticity, position effects). Not a split candidate.
