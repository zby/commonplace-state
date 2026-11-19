---
description: "Discovery report for possible KB connections from the Freebody & Anderson 1981 serial position paper snapshot"
type: types/connect-report.md
source: kb/sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md
source_has_frontmatter: true
date: "2026-02-28"
depth: standard
---

# Connection Report: Serial Position and Rated Importance in the Recall of Text

**Source:** [Serial Position and Rated Importance in the Recall of Text](../../../../sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md)

## Discovery Trace

**Source analysis:**
- Target is a 1981 technical report by Freebody & Anderson (Technical Report No. 219, Center for the Study of Reading, University of Illinois)
- Claims: Both rated importance and serial position predict recall of text propositions; quadratic of serial position is a significant predictor indicating recency effect; importance and position contribute independently; no significant interaction between importance and position
- Method: Multiple regression on recall protocols from ~228 sixth-grade students reading 8 passages; importance rated by separate 110 students on 3-point scale
- Key finding: primacy effect (strong) and recency effect (moderate but significant) in text recall; importance predicts recall independently of position

**Collection determination:**
- Source is in `kb/sources/` → collection is `sources`
- Read `kb/sources/COLLECTION.md`: snapshots are immutable; authored connection surface is the matching `.ingest.md` (none exists for this snapshot)
- Authorized outbound destinations: theory, reference, agent-memory-systems, agentic-systems, sources, external (authorized labels vary by destination)
- Authorized labels for sources→theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`
- Authorized labels for sources→agent-memory-systems: `is-evidence-for`, `compares-with`, `see-also`

**Description listing scan — kb/theory/:**
- Full titles listing generated via `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`
- Flagged candidates based on title/description relevance to serial position, recall, primacy/recency, memory, text structure:
  - `llm-context-is-composed-without-scoping.md` — description mentions "ordering conventions...exploits primacy/recency effects"
  - `knowledge-storage-does-not-imply-contextual-activation.md` — description discusses recall, memory storage vs. retrieval

**Scoped `rg` description listing — kb/theory/:**
- `rg '^description:' kb/theory/ --glob '*.md'` — scanned all theory descriptions
- `rg -n "primacy\|recency\|serial.position\|recall" kb/theory/ --glob "*.md"` — found direct primacy/recency mention in llm-context-is-composed-without-scoping.md

**Body search — kb/theory/:**
- `rg -n "primacy\|recency" kb/theory/ --glob "*.md"` — confirmed primacy/recency appears in llm-context-is-composed-without-scoping.md line 30
- `rg -n "Tulving\|availability.*accessibility\|memory.*storage.*retrieval" kb/theory/ --glob "*.md"` — found Tulving & Pearlstone references in knowledge-storage-does-not-imply-contextual-activation.md

**Topic indexes:**
- `kb/tags/learning-theory-README.md` — `complete: true`, skip by-tag rg; tag covers memory architecture
- `kb/tags/context-engineering-README.md` — relevant tag; llm-context-is-composed-without-scoping.md is a member

**Link following:**
- From `llm-context-is-composed-without-scoping.md`: links to `flat-memory-predicts-specific-cross-contamination-failures-that-are.md`, `context-contamination-operates-below-an-agents-compliance-reasoning.md`
- From `knowledge-storage-does-not-imply-contextual-activation.md`: links to multiple source ingests including `tulving-pearlstone-availability-versus-accessibility.ingest.md`, `gick-holyoak-analogical-problem-solving.ingest.md`
- No existing links to this Freebody & Anderson snapshot found in any KB artifact

**Agent-memory-systems prospecting:**
- `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` — scanned titles
- `rg -n "primacy\|recency\|serial.position" kb/agent-memory-systems/ --glob "*.md"` — found recency mentioned in multiple reviews (clawvault, AI-Context-OS, cortex, REM, MemoryOS, continuity) as a ranking signal
- Recency and importance are used as ranking signals in agent-memory-systems reviews, but no existing connection to this specific paper found

**Sources comparison prospecting:**
- `rg -n "serial.position\|recall.*text\|text.*recall" kb/sources/ --glob "*.md"` — found related sources:
  - `tulving-pearlstone-availability-versus-accessibility.ingest.md` — availability vs. accessibility in memory
  - `skill-and-working-memory.ingest.md` — skilled memory and recall
  - `gick-holyoak-analogical-problem-solving.ingest.md` — analogical problem solving, recall

## Connections Found

- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) — **is-evidence-for**: This note explicitly states that ordering conventions in LLM context assembly "exploit primacy/recency effects but provide no isolation." The Freebody & Anderson paper is the classic empirical demonstration of primacy and recency effects in text recall specifically — it provides the human cognitive science evidence base for the phenomenon the theory note invokes. The paper's finding that both primacy (early-position) and recency (late-position) effects operate in text recall, with primacy stronger than recency, directly supports the note's characterization.

- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: This note discusses the distinction between knowledge storage, retrieval (read-back), and contextual activation, drawing on human memory research including Tulving & Pearlstone's availability vs. accessibility work. The Freebody & Anderson paper provides complementary evidence about what affects recall — specifically that both proposition importance and serial position independently predict recall probability. This human evidence about recall determinants is relevant to the note's broader argument that storage does not guarantee use.

- [Psychology-to-agent-transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — **see-also**: This note establishes a methodology for evaluating whether cognitive science findings transfer to agents. The Freebody & Anderson paper is an instance of the type of human cognitive psychology research this methodology would evaluate — it's a controlled study of serial position and importance effects on text recall that could be cited in discussions of agent memory design, but the transfer-testing note's framework would require per-principle failure-mode analysis before assuming the findings apply to LLM agents.

## Bidirectional Candidates

None. The theory notes do not currently link to this source, and the connection direction is source→theory (the source provides evidence/context for the theory claims).

## Reverse-edge Candidates

- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → source — **evidence**: This note cites human memory studies (Tulving & Pearlstone, Gick & Holyoak) as historical antecedents. The Freebody & Anderson paper would be a relevant addition to the human-evidence base for the storage-to-retrieval distinction, specifically regarding what factors affect recall probability. The note's author could consider citing this paper in the "Two human studies supply historical antecedents" section.

- [Psychology-to-agent-transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → source — **evidence**: This note discusses how to evaluate cognitive science transfer; the Freebody & Anderson paper would be a concrete example of the type of research the methodology applies to. Could be cited as an example human-recall study that would need per-principle testing before agent-application claims.

## Off-authorisation Candidates

None. All candidates that passed articulation had authorized labels available from the sources COLLECTION.md outbound section.

## Raw Text Candidates

None. The source has YAML frontmatter (type: types/snapshot.md).

## Rejected Candidates

- `kb/theory/title-as-claim-enables-traversal-as-reasoning.md` — rejected: mentions "memory notes" as an anti-pattern example ("Don't name notes like topics ('thoughts on memory')"), but this is a writing-style point unrelated to the Freebody & Anderson paper's content about serial position effects
- `kb/agent-memory-systems/reviews/clawvault.md` and other agent-memory reviews mentioning recency/importance ranking — rejected: these use recency and importance as engineering ranking signals, but the connection would be too indirect. The Freebody & Anderson paper is about human text recall, not about ranking algorithm design. Any connection would require the transfer-testing framework from psychology-to-agent-transfer note to establish relevance

## Index Membership

- `learning-theory` tag — the paper concerns human learning and memory (recall of text), which is adjacent to the learning-theory tag's scope. Would require a theory note to cite it as evidence before tag membership makes sense.
- `context-engineering` tag — indirect relevance via the primacy/recency mention in llm-context-is-composed-without-scoping.md, but the paper itself is about human text recall, not context engineering. Not a direct fit.

## Synthesis Opportunities

None identified. The source is a single empirical study; synthesis would require multiple connected notes.

## Maintenance Observations

- **Missing ingest:** This snapshot (`kb/sources/.snapshots/freebody-anderson-serial-position-rated-importance-1981.md`) has no matching `.ingest.md` file. Per `kb/sources/COLLECTION.md`, snapshots are immutable and their authored connection surface is the matching ingest. Any durable outbound connections from this source would need to be authored in an ingest report, not in the snapshot itself.
- **Snapshot capture quality:** The snapshot has OCR artifacts (e.g., "137A /51w?", scrambled headers, corrupted figure text). The abstract and main text are readable, but figure captions and some passages have garbled characters. This affects quote fidelity if quotes are later retained.
- **No existing citations:** No KB artifact currently links to this source. The paper is captured but not yet integrated into the KB's analytical discourse.

## Flags

- **Split candidate assessment:** The source makes multiple independent assertions (primacy effect exists; recency effect exists; importance predicts recall independently; no interaction between importance and position). However, these are all part of one coherent study with a single research program. Not flagged as split.
- **No-connections finding:** Not applicable — genuine connections exist to theory notes.
