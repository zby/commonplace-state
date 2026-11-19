---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: On the Means for Clarification in Dialogue

**Source:** [On the Means for Clarification in Dialogue](../../../../sources/.snapshots/purver-ginzburg-healey-clarification-dialogue.md)

The source is an immutable snapshot (Purver, Ginzburg and Healey 2001, ACL W01-1616). It cannot author links. No tracked ingest exists yet: `kb/sources/purver-ginzburg-healey-clarification-dialogue.ingest.md` is absent at report time. Every outbound candidate below is meant for that future ingest, which is the authored surface under `kb/sources/COLLECTION.md`. A durable link must point to the ingest or to the external URL `https://aclanthology.org/W01-1616.pdf`, never to the snapshot.

**Source content used for judging:** The paper reports a BNC corpus study of about 150,000 words. It defines eight clarification request (CR) forms: non-reprise, literal reprise, wh-substituted reprise, reprise sluice, reprise fragment, gap, gap filler and conventional. It defines four readings: clausal, constituent, lexical and correction. CRs make up about 3-4% of sentences. Readings split roughly as clausal 46.5%, lexical 35%, constituent 14.5% and correction 2.4%. Some forms, especially the reprise fragment, allow every reading, so the hearer has to work out which one is meant. When the reading was ambiguous, the annotators decided it from how the other participants responded and whether the initiator accepted that response (examples 17 and 18). Most CRs clarify the sentence immediately before; 96% clarify one within 4 sentences, and the longest gap seen was 15. The authors conclude that a record of about ten utterances would be enough. The paper's motivating case is the "Paris?" exchange: the system answers (d) by treating a CR as an answer to its own question, and the authors say no reading makes that acceptable. Limits: one expert did all the annotation, with no reliability check; the rarer forms have few examples.

## Discovery Trace

**Collection contract:** I read the `kb/sources/COLLECTION.md` "Outbound links" section. Prospecting is allowed in theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. External links are authorized only through `derived-from`, which here means the ACL URL. I did no open-web prospecting. Theory can take `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in` and `see-also`. Sources and agentic-systems can take `compares-with` and `see-also`.

**Context (not link targets):** The snapshot is cited in `kb/work/formal-semantics-and-codification/where-meaning-is-settled.md`, line 50, as an open stand-in for Ginzburg's *The Interactive Stance*. That workshop note uses it to support "repair is a channel built into the language". The workshop is excluded as a destination. I used it only to understand why the source was captured.

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "underspec|ambigu|interpret|natural language|clarif|ask|question|intent|dialog|convers|meaning|semantic|codif|human|operator|spec|reader|vocab|term"` returned about 70 titles. Flagged: natural-language-meaning-is-coordination..., silent-disambiguation..., agentic-systems-interpret-underspecified-instructions, conversation-vs-prompt-refinement..., changing-requirements-conflate..., elicitation-requires..., underspecification-and-indeterminism..., writing-styles-are-strategies..., intent-controls-choices..., specification-strategy-should-follow...

**Description listing:** I read the descriptions of the ten flagged theory notes with `rg -m1 '^description:'`. For each, I also ran `rg -n -i "clarif|dialog|convers|repair|ask"` on the body.

**Topic indexes:**
- I listed the tag heads in `kb/tags/`. I read the descriptions of `llm-reliability-README.md` and `constraining-README.md`. Neither tag fits: the paper does not cover LLM output deviation or narrowing the interpretation of an artifact. I did no tag-filtered rg, because the snapshot carries no `tags:`.

**Body search (scoped to theory, reference, agentic-systems, agent-memory-systems, sources, tags; snapshots excluded):**
- `rg -l -i clarif`: 15+ files, mostly incidental uses of "clarify". The hits checked were `specification-strategy-should-follow-where-understanding-lives.md` (line 14 scopes interactive clarification out of the note) and `design-for-the-first-time-human-except-on-access-cost.md` (line 63 is a single aside). Both rejected.
- `rg -l "grounding in"`, `rg -l "common ground"`: hits are KB-internal uses of "grounding" (source support). None uses Clark/Traum conversational grounding. Rejected as keyword collisions.
- `rg -l -i dialogue`: hits are memory-system reviews and unrelated ingests about chat-history storage. None concerns clarification or repair.
- `rg -l "Clark"`, `"Traum"`, `"Ginzburg"`, `"Purver"`, `"HPSG"`, `"QUD"`: Ginzburg, Purver, HPSG and QUD return nothing outside the workshop. The Clark and Traum hits are unrelated people or systems.
- `rg -l "short-term"`, `rg -l -i "verbatim|gist|surface (form|information)" kb/theory`: memory-system retention hits. None concerns how long surface form must be kept to support repair. Rejected (see Rejected Candidates).
- `rg -n -i "repair|clarif|mutual intelligib|conversation analysis" kb/sources/*suchman*.ingest.md`: matches in both Suchman ingests. They frame human repair of breakdowns as a baseline for silent disambiguation. Kept as source comparisons.
- `rg -l -i "ask_user|askuserquestion|clarifying question|clarification question|asks? the user"` over agentic-systems, agent-memory-systems, reference and theory: hits are system reviews that mention ask-user tools in passing (for example `claude-code-dynamic-workflows.md`). None analyzes the forms or readings of clarification. Not kept.

**Link following:**
- From `silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md`, I followed its Relevant Notes to final-task-success, agentic-systems-interpret-underspecified-instructions, changing-requirements-conflate... and out-of-spec-output... This confirmed the cluster where "the agent resolves a reading without surfacing it" is the shared axis.
- From `natural-language-meaning-is-coordination-among-learned-approximations.md`: its claim that "other speakers ... play the checker's role" and that meaning is sharpest "where correction is cheap and frequent" is what the corpus frequencies bear on.
- From the Suchman ingests: both already link silent-disambiguation, so the source would join an existing human-repair-baseline neighbourhood.

## Connections Found

All of these are for the future `purver-ginzburg-healey-clarification-dialogue.ingest.md`.

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **is-evidence-for**: The hypothesis says other speakers act as natural language's weak, distributed checker. The corpus shows that checker working in-band and often, with CRs at 3-4% of dialogue sentences. It also qualifies the hypothesis: most checks concern the speech act or the words themselves, not what a term means. Lexical and clausal readings make up about 80% and constituent readings about 15%. That bears on the claim that term meaning is held by checks. It is not a test the hypothesis could have failed.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: The shared axis is whether a wrong choice of reading becomes visible. In the corpus, one CR form can carry several readings. A wrong pick is exposed by the initiator's next move (example 17: "Spunyarn?" is answered clausally, then followed by "What's spunyarn?"). The paper's response (d) in the "Paris?" exchange is the machine failure the note describes: an ambiguous move silently taken as an answer.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- **compares-with**: The shared axis is in-band repair versus rewinding. The note argues that humans append corrections because they cannot rewind. The paper measures how that append-only repair actually behaves: it is local (most CRs target the previous sentence and 96% one within 4), and it needs only a short record of about ten utterances, including their surface form. This gives a measured human baseline against which to judge the cost of the note's conversational Q&A option.
- [Dittrich, re-reading Suchman's Plans and Situated Actions](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) -- **compares-with**: The shared axis is who repairs a breakdown in communication. Dittrich's ingest names an asymmetry: humans repair, classic machines do not. This paper lists the actual means humans use (eight forms, four readings). The paper also shows the machine side of the asymmetry: a 2001 dialogue system had to be built specifically to process user CRs.
- [Suchman's Plans and Situated Actions (PD of HCI summary)](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) -- **compares-with**: Both describe breakdowns in human-machine communication. The copier study names breakdowns the machine could not detect, such as false alarm and garden path. This paper's "Paris?" case (d) is a garden path of the same kind in a spoken-dialogue system, and its CR taxonomy is the detection vocabulary the copier lacked.
- [On the Means for Clarification in Dialogue (ACL W01-1616)](https://aclanthology.org/W01-1616.pdf) -- **derived-from**: This is the ingest's provenance edge to the original paper.

## Bidirectional Candidates

- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) <-> source -- **compares-with** (source side) / **evidenced-by** (theory side, under `kb/theory/COLLECTION.md`): The note's only evidence today is a practitioner observation (Goedecke). This paper is a corpus-backed case of the human counterpart: wrong readings get repaired because the initiator reacts. That bounds the note's scope. Silent disambiguation is a problem specific to settings that have no initiator's follow-up.

## Reverse-edge Candidates

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) → source ingest -- **evidenced-by** (theory label: "qualifies, or bounds"): The note names "other speakers" as one checker but gives no evidence of how often or at what level they check. The corpus frequencies and the reading distribution (mostly lexical and clausal, not constituent) would bound that claim. The note should cite the ingest, not the snapshot. Under its own contract it would be qualification, not corroboration.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) → source ingest -- **evidenced-by**: The claim that conversation is append-only repair currently rests on intuition ("humans can't rewind"). The CSS distance data supports it and adds that the repair is local. This is weaker than the previous candidate; author it only if the note is revised.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- This is the foundation note for underspecification. The paper's ambiguity is about what kind of request a CR is, not how much a specification admits. The source reaches this note through silent-disambiguation, so a direct `see-also` would be a spray.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- The note explicitly scopes interactive clarification out (line 14). Linking would contradict its stated boundary.
- [Design for the first-time human, except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- It mentions maintainers asking for clarification in one aside only. That is mention, not substance.
- [Elicitation requires maintained question-generation systems](../../../../theory/elicitation-requires-maintained-question-generation-systems.md) -- It is about questions that activate the model's knowledge, not repair of a previous utterance. The match is keyword only.
- [Changing requirements conflate genuine change with disambiguation](../../../../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- It concerns late discovery across iterations, not repair within the conversation. Reachable through silent-disambiguation.
- Memory-retention hits (`short-term`, `verbatim|gist`) -- The paper's ten-utterance surface-form record could suggest a claim about how much context a dialogue agent must keep. No theory note makes a claim about the retention horizon repair needs, so there is no target. See Synthesis Opportunities.
- Agentic-systems reviews that mention ask-user tools -- These are passing mentions of a tool. None analyzes which clarification readings a system supports, so a `compares-with` axis would be invented.

## Index Membership

None. Sources sit outside the participating collections. I considered `llm-reliability` and `constraining` as optional source tags and rejected both, because the paper's contribution is human dialogue repair, not LLM deviation or artifact narrowing.

## Synthesis Opportunities

The two Suchman ingests, this paper and silent-disambiguation together suggest a higher-order claim. Human communication catches misreadings through a fast, local, initiator-driven repair loop: CRs are frequent, usually target the previous utterance, and are confirmed by the initiator's reaction. A one-shot delegated agent run removes that loop, so silent disambiguation is the default rather than a defect. The claim would be "silent disambiguation is what remains when the repair loop is removed." Whether it belongs in `kb/theory/` or stays in the formal-semantics workshop (`where-meaning-is-settled.md`) is a call for the workshop owner. Do not create it from this report.

## Maintenance Observations

- The tracked ingest is missing for a snapshot the workshop already cites (`where-meaning-is-settled.md`, line 50). Until the ingest exists, any promotion of that workshop claim into theory would have no authored source surface to link.
- A sibling snapshot, `kb/sources/.snapshots/schegloff-jefferson-sacks-self-correction-repair.md`, also has no ingest. When ingested, it is a likely `compares-with` partner for this source: conversation-analysis repair versus formal-semantic clarification, on the axis of whether self-repair is preferred over other-initiated repair.

## Flags

- Tension to keep visible: the workshop uses this paper to support "repair is a channel built into the language". The paper supports that frequency and structure exist. It does not support a claim about meaning settlement in general: most CRs are about hearing (lexical) or the speech act (clausal), and only about 15% ask what a term refers to. The ingest should state this limit.
- Evidence quality: one expert annotator, no kappa check, and few examples of the rarer forms. Any `is-evidence-for` edge should mention this.
- Split candidate: no.
