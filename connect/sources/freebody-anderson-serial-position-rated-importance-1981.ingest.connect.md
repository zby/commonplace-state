---
description: "Discovery report for possible KB connections from the Freebody & Anderson 1981 ingest analysis"
type: types/connect-report.md
source: kb/sources/freebody-anderson-serial-position-rated-importance-1981.ingest.md
source_has_frontmatter: true
date: "2026-02-28"
depth: standard
---

# Connection Report: Serial Position and Rated Importance in the Recall of Text

**Source:** [Ingest: Serial Position and Rated Importance in the Recall of Text](../../../../sources/freebody-anderson-serial-position-rated-importance-1981.ingest.md)

## Discovery Trace

**Source analysis:**
- Target is an ingest report analyzing Freebody & Anderson (1981), Technical Report No. 219, Center for the Study of Reading, University of Illinois
- The ingest's "Contribution assessment" confirms: both rated importance (r = .191) and serial position (r = -.214) independently predict recall; quadratic of serial position significant indicating recency effect; primacy stronger than recency; no interaction between importance and position
- The ingest's "Learning Claims" section explicitly maps the paper onto Commonplace concepts: evidence about *what is retained from reading*, relevant to context composition and what readers retain
- The ingest already contains three outbound connections in its "Connections Found" section

**Collection determination:**
- Source is in `kb/sources/` → collection is `sources`
- Read `kb/sources/COLLECTION.md`: ingest reports carry the active outbound surface
- Authorized outbound destinations from sources COLLECTION.md outbound section:
  - `theory` (labels: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`, `defined-in`)
  - `agent-memory-systems` (labels: `is-evidence-for`, `compares-with`, `see-also`)
  - `sources` (labels: `compares-with`, `see-also`)
  - `agentic-systems` (labels: `compares-with`, `see-also`)
  - `reference` (labels: `see-also`)
  - `external` (labels: `derived-from`)
- Excluded destinations: `kb/work/`, `kb/instructions/`

**Description listing scan — kb/theory/:**
- Full titles listing generated via `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'`
- Flagged candidates based on title/description relevance to primacy/recency, context composition, memory, human evidence:
  - `llm-context-is-composed-without-scoping.md` — description: "Flat context concatenation lacks local scope... ordering conventions... exploits primacy/recency effects"
  - `knowledge-storage-does-not-imply-contextual-activation.md` — description: "Separates knowledge that exists, knowledge loaded into context (read-back), and knowledge that actually changes behavior (activation)"
  - `psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md` — description: "Brainstorming a methodology for evaluating cognitive-science-to-agent transfer"
  - `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` — description: "For quality-sensitive agent work whose required evidence fits within the provider window, volume, complexity, and interference can silently constrain usable context"
  - `dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md` — description: "Why dependency-locality psycholinguistics licenses a few relation-preserving word-order heuristics for human-read English prose... LLM-reader benefit untested"

**Body search — kb/theory/:**
- `rg -n "primacy\|recency" kb/theory/ --glob "*.md"` — found:
  - `llm-context-is-composed-without-scoping.md` line 30: "Ordering conventions — system prompt first, then context, then user message — exploits primacy/recency effects but provides no isolation"
  - `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` line 20: "The 'lost in the middle' result (Liu et al., 2023) shows primacy and recency bias in long-context retrieval"
- `rg -n "human.*evidence\|human.read\|cognitive.science\|empirical.*recall" kb/theory/ --glob "*.md"` — found relevant content in psychology-to-agent-transfer note and soft-degradation note

**Link following:**
- From `llm-context-is-composed-without-scoping.md`: links to `flat-memory-predicts-specific-cross-contamination-failures-that-are.md`, `context-contamination-operates-below-an-agents-compliance-reasoning.md`, `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md`
- From `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md`: links to `paulsen-maximum-effective-context-window-mecw.ingest.md` for position-effects context
- From `knowledge-storage-does-not-imply-contextual-activation.md`: links to multiple source ingests including `tulving-pearlstone-availability-versus-accessibility.ingest.md`, `gick-holyoak-analogical-problem-solving.ingest.md`, `llm-agents-are-not-always-faithful-self-evolvers.ingest.md`

**Existing connections in ingest:**
The ingest's "Connections Found" section already documents:
- `llm-context-is-composed-without-scoping.md` — **is-evidence-for**
- `knowledge-storage-does-not-imply-contextual-activation.md` — **is-evidence-for**
- `psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md` — **see-also**

**Sources comparison prospecting:**
- `rg -l "primacy\|recency\|serial.position\|position.*recall" kb/sources/ --glob "*.md"` — found related sources:
  - `paulsen-maximum-effective-context-window-mecw.ingest.md` — position effects on LLM context window utility
  - `tulving-pearlstone-availability-versus-accessibility.ingest.md` — availability vs. accessibility in memory
  - `gick-holyoak-analogical-problem-solving.ingest.md` — analogical problem solving, recall
  - `novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md` — adaptive forgetting with recency/importance signals
  - `how-we-built-our-knowledge-base-2077822555159945507.ingest.md` — mentions serial position
  - `autonomous-agent-context-memory-2088234998654472340.ingest.md` — context memory with position effects
  - `kieras-initial-mention-as-a-signal-to-thematic-content.ingest.md` — thematic content signals

**Agent-memory-systems prospecting:**
- `rg -n "primacy\|recency\|serial.position" kb/agent-memory-systems/ --glob "*.md"` — found recency mentioned as ranking signal in multiple reviews (clawvault, AI-Context-OS, cortex, REM, MemoryOS, continuity)
- No existing connection to Freebody & Anderson found in any agent-memory-systems artifact

**Agentic-systems prospecting:**
- `rg -n "primacy\|recency\|serial.position\|recall" kb/agentic-systems/ --glob "*.md"` — found recency mentioned in context ranking and memory selection contexts
- No direct connection to Freebody & Anderson paper found

**Reference prospecting:**
- `rg -n "primacy\|recency\|serial.position\|position.*recall" kb/reference/ --glob "*.md"` — no relevant matches
- Reference collection has minimal relevant content for this source

## Connections Found

### Existing connections (already in ingest's "Connections Found" section)

- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) — **is-evidence-for**: The theory note states that ordering conventions in LLM context assembly "exploit primacy/recency effects but provide no isolation." This paper is the classic empirical demonstration that primacy and recency effects operate in human text recall specifically—both predict recall independently, with primacy stronger than recency. The human cognitive science evidence base for the phenomenon the note invokes. The ingest's "Recommended Next Action" explicitly calls for citing this paper in this note.

- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) — **is-evidence-for**: The theory note draws on human memory research (Tulving & Pearlstone's availability vs. accessibility distinction) to argue that storage does not guarantee retrieval or use. This paper provides complementary evidence about what factors affect recall probability—specifically that both proposition importance and serial position independently predict whether content is recalled. Relevant to the broader argument that what is stored is not what is accessed. The ingest maps this connection explicitly in its "Learning Claims" section.

- [Psychology-to-agent-transfer needs per-principle failure-mode testing](../../../../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) — **see-also**: This note establishes a methodology for evaluating whether cognitive science findings transfer to agents. The Freebody & Anderson paper is an instance of the type of human cognitive psychology research this methodology would evaluate—a controlled study of serial position and importance effects on text recall. Citing it in discussions of agent memory design would require per-principle failure-mode analysis before assuming the findings apply to LLM agents.

### New candidates discovered during prospecting

- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) — **is-evidence-for**: This note discusses "lost in the middle" (Liu et al., 2023) and primacy/recency bias in long-context retrieval, citing Paulsen for position-effects evidence. The Freebody & Anderson paper provides the classic human-text-recall demonstration that primacy and recency effects operate independently, with primacy stronger than recency. The note could strengthen its human-evidence base by citing this paper alongside the LLM-specific "lost in the middle" findings. The ingest's "Learning Claims" section explicitly identifies this note as relevant: "The paper's regression results... give a concrete, quantified basis for the primacy/recency claims used in [LLM context is composed without scoping]."

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) — **see-also**: This note synthesizes seven sources about human reading evidence for word-order heuristics and explicitly states that "the heuristics' value for LLM readers is a separate, untested question." The Freebody & Anderson paper is parallel human-reading-evidence research about position effects on recall—not about dependency locality specifically, but about how position in text affects what readers retain. Both notes concern human reading evidence relevant to ordering claims, and both acknowledge the human→LLM transfer gap. The connection is adjacent: a reader exploring human reading evidence for ordering claims might find both relevant.

## Bidirectional Candidates

None. The theory notes do not currently link to this ingest, and the connection direction is source→theory (the source provides evidence/context for the theory claims). The ingest's "Recommended Next Action" section recommends updating `llm-context-is-composed-without-scoping.md` to cite this paper, which would create the bidirectional link.

## Reverse-edge Candidates

- [Soft degradation can bind before the hard cap even when required evidence fits](../../../../theory/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) → source — **evidence**: This note discusses primacy/recency bias from "lost in the middle" (Liu et al., 2023) and cites Paulsen for position-effects evidence. The Freebody & Anderson paper would strengthen the note's human-evidence base for the claim that position effects are real and operate alongside content-based factors. The note's author could consider adding this paper to the evidence chain for the primacy/recency claim.

- [Paulsen: Maximum Effective Context Window (MECW)](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) → source — **compares-with**: Both examine position effects on recall/retrieval. Paulsen examines position effects on LLM context window utility; Freebody & Anderson examines position effects on human text recall. A comparison would highlight the human→LLM transfer question: do the same serial-position effects observed in human readers apply to LLM context composition? The ingest's "Extractable Value" section notes that "importance and position are independent predictors of recall" is relevant to any system that wants to weight content by importance rather than position.

- [Tulving & Pearlstone: Availability versus accessibility of information in memory](../../../../sources/tulving-pearlstone-availability-versus-accessibility.ingest.md) → source — **compares-with**: Both are human cognitive psychology studies of memory recall. Tulving & Pearlstone establishes the availability/accessibility distinction (storage vs. retrieval); Freebody & Anderson examines what factors affect recall probability (position and importance). Together they provide a richer picture of human recall determinants than either alone. The `knowledge-storage-does-not-imply-contextual-activation.md` note cites Tulving & Pearlstone; adding Freebody & Anderson would complement that citation.

- [Gick & Holyoak: Analogical problem solving](../../../../sources/gick-holyoak-analogical-problem-solving.ingest.md) → source — **compares-with**: Both are human cognitive psychology studies cited in the `knowledge-storage-does-not-imply-contextual-activation.md` note's "human studies supply historical antecedents" section. Gick & Holyoak examines how hints affect analogical problem solving despite comparable story recall; Freebody & Anderson examines how position and importance affect text recall. Both speak to the gap between storage/recall and application.

## Off-authorisation Candidates

None. All candidates that passed articulation had authorized labels available from the sources COLLECTION.md outbound section for the relevant destination.

## Raw Text Candidates

None. The source has YAML frontmatter (type: types/ingest-report.md).

## Rejected Candidates

- `kb/agent-memory-systems/reviews/clawvault.md` and other agent-memory reviews mentioning recency/importance ranking — rejected: these use recency and importance as engineering ranking signals, but the connection would be too indirect. The Freebody & Anderson paper is about human text recall, not about ranking algorithm design. Any connection would require the transfer-testing framework from psychology-to-agent-transfer note to establish relevance. The ingest's "Learning Claims" section already maps this correctly: the paper is evidence about human recall, not direct evidence about agent memory systems.

- `kb/theory/title-as-claim-enables-traversal-as-reasoning.md` — rejected: mentions "memory notes" as an anti-pattern example, but this is a writing-style point unrelated to the Freebody & Anderson paper's content about serial position effects.

- `kb/theory/agents-navigate-by-deciding-what-to-read-next.md` — rejected: discusses agent navigation as follow/skip judgment under bounded context. While adjacent to recall/retrieval concepts, the connection would require transfer-testing framework to establish relevance. The paper's findings about position effects on human recall don't directly bear on agent navigation decisions.

- `kb/agentic-systems/reviews-archive/swarmworld.md` and other agentic-system reviews mentioning recency — rejected: these use recency as a selection signal in memory/recollection systems. The Freebody & Anderson paper is about human text recall, not about engineered memory selection. Connection would be too indirect without transfer-testing.

## Index Membership

- `learning-theory` tag — the paper concerns human learning and memory (recall of text), which is adjacent to the learning-theory tag's scope. Would require a theory note to cite it as evidence before tag membership makes sense. The ingest's "learning_claims: true" frontmatter signals this relevance.

- `context-engineering` tag — indirect relevance via the primacy/recency mention in `llm-context-is-composed-without-scoping.md`. The paper itself is about human text recall, not context engineering. Not a direct fit for tag membership, but the ingest's "Recommended Next Action" to cite this paper in the context-engineering note would create the link.

## Synthesis Opportunities

- **Human→LLM position effects synthesis**: The Freebody & Anderson paper (human text recall: primacy and recency operate independently, primacy stronger) and the "lost in the middle" findings (Liu et al., 2023: LLM long-context retrieval shows primacy/recency bias) together suggest a research question: do the same serial-position effects observed in human readers apply to LLM context composition, or do LLMs show different position-effect patterns? The `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md` note could develop this as a synthesis point.

- **Recall determinants synthesis**: Tulving & Pearlstone (availability vs. accessibility), Gick & Holyoak (hints affect problem-solving despite comparable recall), and Freebody & Anderson (position and importance independently predict recall) together provide a multi-factored picture of human recall. A synthesis note on "what determines what readers retain" could integrate these three sources.

## Maintenance Observations

- The ingest's "Recommended Next Action" recommends updating `llm-context-is-composed-without-scoping.md` to cite this paper. This action item is captured in the Connections Found section above. A future writer should verify the citation was added.

- The ingest's frontmatter includes `learning_claims: true`, signaling that the paper's mechanism can be mapped onto Commonplace learning concepts. This is reflected in the "Learning Claims" section of the ingest, which maps the paper onto the KB's interest in context composition and what readers retain.

- The ingest notes a limitation: "The paper addresses position and what readers retain, but not proportion—the relationship between how much content is presented and how much is retained." This gap is relevant to the KB's interest in "position, proportion, and what readers retain" (from the ingest's `occasion` field). Any synthesis should note this limitation.

## Flags

- **Split candidate check**: The ingest connects to three theory notes across two topic areas (context engineering: `llm-context-is-composed-without-scoping.md`, `soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md`; memory/activation: `knowledge-storage-does-not-imply-contextual-activation.md`; methodology: `psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md`). This is within normal range for an evidence-bearing source. Not flagged as split.

- **No-connections finding**: Not applicable. Connections exist.

- **Tension**: The ingest notes that "importance and position are uncorrelated (r = .006)"—meaning the two effects are separable. This is useful for design (importance-weighted selection can add value beyond position-based selection) but also means the paper doesn't test competing accounts of why position matters (authors clustering important content at ends vs. pure temporal mechanism). This tension is captured in the ingest's "Limitations" section.
