---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: The preference for self-correction in the organization of repair in conversation

**Source:** [Ingest: The preference for self-correction in the organization of repair in conversation](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md)

## Discovery Trace

**Authorisation (kb/sources/COLLECTION.md, "Outbound links"):** prospect theory, reference, agent-memory-systems, agentic-systems, tags, sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from`/`rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting skipped: no external target supplied beyond the ingest's own `source` URL.

**Existing ingest connections verified (all paths exist):** acceptance-authority, silent-disambiguation, error-messages-that-teach, revision-guided-by-rationale, the-bug-that-shipped ingest, Dittrich Suchman ingest. All six already carry `compares-with` with a named axis; none re-proposed below.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "repair|clarif|ambigu|underspec|interpret|dialog|convers|meaning|semantic|error|self-correct|self-repair|feedback|detect|locat|handoff|ask|question|correct"` -- flagged: natural-language-meaning-is-coordination-among-learned-approximations, conversation-vs-prompt-refinement-in-agent-to-agent-coordination, changing-requirements-conflate-genuine-change-with-disambiguation, elicitation-requires-maintained-question-generation-systems, agentic-systems-interpret-underspecified-instructions, specification-strategy-should-follow-where-understanding-lives (found later via body search), plus already-linked notes.

**Description reads:** `rg -N '^description:'` on each flagged theory note, with `rg -n -i "repair|clarif|conversation|ask"` inside each to test whether conversational repair is treated substantively.

**Body search:**
- `rg -n -i -l "repair|clarification|grounding in conversation|conversation analysis|Clark|common ground|misunderstand"` over theory, reference, agentic-systems, agent-memory-systems, tags, sources -- too broad; "repair" mostly matches code/program repair. Discarded as a recall surface.
- `rg -n -i "clarifying question|clarification|ask(s|ing)? (the user|for clarification)|conversation analysis|Schegloff|conversational repair|turn-taking|Suchman|other-initiated|Herbert Clark|common ground"` -- hits: pd-of-hci-suchman summary ingest (copier breakdowns, "adjacent pairs", repair-locus synthesis), Dittrich ingest (already linked), purver-ginzburg-healey ingest (sibling, same occasion), specification-strategy note (line 14, interactive clarification), design-for-the-first-time-human note (line 63), dense-mem review (clarification instead of silent overwrite), socratic-agents ingest (clarification as reasoning step).
- `rg -n -i "schegloff" kb` -- only the source itself and the excluded workshop file cite the paper; no inbound edge exists.
- `rg -n -i "humans can't rewind|append corrections"` in conversation-vs-prompt-refinement -- confirms the note's claim (line 18) that humans "can only append corrections".

**Link following:**
- Purver ingest: its Connections Found already link conversation-vs-prompt-refinement, Dittrich and the PD of HCI summary; it does not link this paper. Confirms a two-source repair cluster (structure + frequency) forming around the same occasion.
- PD of HCI summary ingest: its Extractable Value item 3 explicitly names a "repair-locus synthesis already flagged in the Dittrich ingest"; this paper is the primary CA source that synthesis lacks.
- natural-language-meaning note: read lines 8-40; it names "other speakers" as the weak, distributed checker but describes no mechanism by which speakers check each other.
- theory COLLECTION.md labels table read for reverse edges: theory -> sources uses `evidenced-by` (corroborates, qualifies or bounds) or `see-also`.

**Tags:** sources carry no `tags:` and are outside tag participation; no tag head read for routing. Considered llm-reliability / failure-modes heads by name only; the paper is not about LLM reliability.

## Connections Found

- [Natural-language meaning is coordination among learned approximations, not approximation of a target](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **compares-with**: on how "other speakers" act as the checker. The note posits speakers as a weak, distributed checker but gives no mechanism. The paper supplies one for conversation: a repair-initiation opportunity space attends every turn, other-initiators mostly only locate trouble, and adequate understanding is shown by producing the implicated next turn rather than by explicit checking. This sharpens "weak" (the check is mostly implicit and producer-deferring), but the paper says nothing about lexical meaning drift, so it is a comparison, not evidence for the hypothesis.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- **compares-with**: on append-only versus rewinding repair. The note says humans "can only append corrections". The paper shows that append-only repair is organized (ordered positions, producer-first) and that most self-repair succeeds inside the trouble-source turn, before the recipient responds, which is the closest conversational analogue of a rewind. The Purver ingest already compares on locality; this paper adds the ordering and who repairs.
- [On the Means for Clarification in Dialogue (Purver, Ginzburg, Healey)](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) -- **compares-with**: on other-initiated repair devices. This paper gives the structural organization of next-turn other-initiation and its graded device set ("Huh?", question words, partial repeats, "Y'mean X?"); Purver et al. measure frequency, eight forms and four readings in the BNC. The Extractable Value item 3 of this ingest already defers the meaning-layer separation to Purver's readings, so the link is load-bearing for the occasion.
- [PD of HCI - Plans and Situated Actions (summary of Suchman)](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) -- **compares-with**: on who detects and repairs a communicative breakdown. The summary's copier breakdowns (false alarm, garden path) and its repair-locus synthesis lack a primary account of human repair; this paper is that primary CA baseline. Parallel to the existing Dittrich edge; the summary's "adjacent pairs" garbling is also a reason to point readers at a CA primary.

## Bidirectional Candidates

- [On the Means for Clarification in Dialogue (Purver, Ginzburg, Healey)](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) <-> source -- **compares-with**: the Purver ingest should return the edge; its readings and frequency data are argued against an unnamed background of CA repair, and this paper is the standard citation for that background.
- [PD of HCI - Plans and Situated Actions (summary of Suchman)](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) <-> source -- **compares-with**: its flagged repair-locus synthesis would cite this paper for the human side.
- [Re-re-reading Lucy Suchman's Plans and Situated Actions](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) <-> source -- **compares-with**: already linked from this ingest; the Dittrich ingest asks for primary grounding of its repair-asymmetry synthesis and could return the edge.

## Reverse-edge Candidates

- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) → source -- **evidenced-by** (theory COLLECTION.md, qualifies/bounds sense): the line 18 claim "we can only append corrections" is qualified by same-turn self-repair, which corrects before the turn completes. Qualification, not corroboration; the paper did not test the note's claim.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source -- **evidenced-by** (bounds): §6.3 says a recipient with adequate understanding proceeds with the next turn without visible repair, which bounds when unmarked resolution is a defect rather than normal competence. The note currently has no human-interaction baseline.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- mentions interactive clarification only to exclude it from scope (durable artifacts); the paper says nothing about durability of resolutions.
- [Design for the first-time human except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- one-sentence mention that a maintainer "would ask for clarification"; too incidental to carry a label.
- [Changing requirements conflate genuine change with disambiguation](../../../../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- a locality analogy (three-turn repair window vs short iterations limiting propagation) is possible but speculative; Purver's measured locality is the better source for it.
- [Elicitation requires maintained question-generation systems](../../../../theory/elicitation-requires-maintained-question-generation-systems.md) -- about activating model knowledge through questions, not repair of trouble in a prior turn.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- underspecification theory without an interactional repair axis; reachable through silent-disambiguation.
- [dense-mem](../../../../agent-memory-systems/reviews/dense-mem.md) -- "clarification instead of silent overwrite" is memory-conflict resolution, a keyword match only.
- [Socratic agents ingest](../../../../sources/socratic-agents-autonomous-scientific-discovery.ingest.md) -- "clarification" is a reasoning step in scientific explanation revision, not interactional repair.

## Index Membership

None. Sources are outside tag participation; `kb/sources/README.md` is not a curated topical index.

## Synthesis Opportunities

This paper, the Purver ingest, the Dittrich and PD of HCI Suchman ingests, and the silent-disambiguation note together imply a "repair locus" claim already flagged twice in source ingests: human conversation places repair initiation visibly and gives the producer first opportunity; classic machines (Suchman's copier) detected no breakdown; LLM agents repair others' gaps silently and self-initiate weakly (The Bug That Shipped). A theory note would need to establish which of the conversational mechanisms (sequential position, disagreement avoidance, competence norms) operate for agents before treating the human pattern as a design baseline.

## Maintenance Observations

- The repair-locus synthesis is now flagged in three source ingests (Dittrich, PD of HCI, this one) without a durable owner. A candidate for promotion to the log or a workshop.
- "Self-repair" carries two unrelated senses in the KB: the CA sense here and LLM code regeneration under an oracle in several ingests. The ingest notes this locally; the vocabulary collision ledger may want an entry if a theory note adopts the CA sense.

## Flags

- Tension (not resolved): the error-messages-that-teach note recommends the detector supply the fix, while acceptance-authority allows code to state a determined value; the paper's other-initiators withhold the known correction. The existing ingest already frames this as a setting difference.
- Split candidate: no. The ingest makes one main assertion with several sub-findings.
