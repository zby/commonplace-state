---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/clark-brennan-grounding-in-communication.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Grounding in Communication (Clark & Brennan 1991)

**Source:** [Grounding in Communication](../../../../sources/.snapshots/clark-brennan-grounding-in-communication.md)

The source is an immutable snapshot. No tracked `kb/sources/clark-brennan-grounding-in-communication.ingest.md` exists yet. Every outbound candidate below is a recommendation for that future ingest's footer, not for the snapshot. Links in this report point to the snapshot only because the report is local and regenerable; durable artifacts must link the ingest or the external `source` URL.

Source claims used for judging candidates:

- **Grounding criterion** (snapshot ~l.118): participants seek mutual belief that the partner has understood "to a criterion sufficient for current purposes". Grounding is the collective process of reaching it.
- **Contribution model** (~l.148-200): a contribution needs a presentation phase and an acceptance phase. Contributions nest, so side sequences such as "- have a car?" sit inside the acceptance phase.
- **Positive versus negative evidence** (~l.211-345): accounts that assume understanding by default unless trouble appears accept too much. People seek positive evidence: acknowledgments, a relevant next turn, and continued attention. The regress is avoided because a relevant next turn and continued attention need no separate presentation.
- **Least collaborative effort** (~l.372-435): participants minimize joint effort from initiation to mutual acceptance. This explains the preference for self-repair and the use of try markers, installments and invited completions.
- **Purpose and medium** (~l.439-980): techniques and criteria change with purpose (references, verbatim content). Media differ on eight constraints (copresence, visibility, audibility, cotemporality, simultaneity, sequentiality, reviewability, revisability) and so in eleven costs. In media that are not cotemporal, repair initiated by others becomes expensive, so senders revise before sending or change medium.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` § Outbound links. The authorised destinations are theory, theory/definitions, agent-memory-systems, agentic-systems, reference (see-also only), other sources, tags, and external (`derived-from`, `see-also`). The excluded destinations are `kb/work/` and `kb/instructions/`. The snapshot is never the link author, so all edges are recorded for the future ingest.

**External:** prospecting skipped by rule. The source's own URL is already known, so a future ingest should carry `derived-from` to `https://web.stanford.edu/~clark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf`.

**Title listing scan (theory, 433 titles):**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "convers|coordinat|meaning|ambigu|clarif|repair|shared|understand|interact|dialog|ask|question|human|agent-to-agent|handoff|medium|channel|feedback|acknowledg|underspec|intent|communicat|cost|natural-language|specification|disambig"` returned about 60 titles. Flagged: natural-language-meaning-is-coordination..., conversation-vs-prompt-refinement..., silent-disambiguation..., unattended-work-needs-the-functions..., acceptance-authority-does-not-require..., agentic-systems-interpret-underspecified-instructions, writing-styles-are-strategies..., intent-framed-delegation..., elicitation-requires..., changing-requirements-conflate..., human-llm-differences..., session-history-should-not-be..., frontloading-spares-execution-context.
- Descriptions read for the flagged set with `rg -N '^description:'`.

**Body search:**
- `rg -il "common ground|grounding criterion|clark.{0,5}brennan|mutual belief|mutual knowledge" kb/theory kb/reference kb/sources kb/agentic-systems kb/agent-memory-systems kb/tags` returned only ADR 079 and an archived proposal. Both use "grounding" in the KB's own sense of source support. Neither is a candidate (see Maintenance Observations).
- `rg -n -i "acknowledg(e)?ment|positive evidence|negative evidence|least (collaborative )?effort|back-?channel|mutual(ly)? (belie|understand)|shared understanding|reviewab|asynchron" kb/theory` produced no hits that use the communication sense. `intent-framed-delegation...` l.125 quotes military doctrine on "shared understanding". It is adjacent but not engaged.
- `rg -l -i "clarifying question|asks? (a|the) question|ask back|in-band|repair cost|cheap to correct|correction is cheap" kb/theory` returned natural-language-meaning..., conversation-vs-prompt-refinement..., session-history..., and others. The first two were confirmed by full read.
- `rg -l -i "conversation analysis|common ground|repair|clarification|turn-taking|situated action|grice|speech act" kb/sources --glob '*.ingest.md'` returned about 30 files, mostly ML "repair" hits. Kept for evaluation: the Suchman summary, the Dittrich re-reading, and Norman (found by link following).
- `rg -l -i "common ground|clarifying question|clarification|grounding in communication|ask(s)? the user" kb/agentic-systems kb/agent-memory-systems` returned taxonomy, table and review hits. A spot check of `claude-code-dynamic-workflows.md` found incidental use only, so nothing was kept.

**Tag heads:** read `claims-and-grounding-README.md` (`complete: true`; its "grounding" is source support, a different sense) and `learning-theory-README.md`. No source tag is warranted.

**Link following:**
- Sibling ingests created the same day for the same workshop: [Purver et al.](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) and [Schegloff et al.](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md). Their footers point to natural-language-meaning, silent-disambiguation, conversation-vs-prompt-refinement, acceptance-authority, error-messages-that-teach, revision-guided-by-rationale, the Suchman pair and The Bug That Shipped. Each was re-evaluated against this source's distinct claims: the positive-evidence requirement, least collaborative effort, and the media cost model.
- From unattended-work... to [Norman 1989](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md), whose continual-feedback claim parallels continued attention as evidence.

## Connections Found

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) -- **is-evidence-for**: the note's hypothesis is that meaning is coordination, held by weak checks from other speakers. Clark and Brennan give the checking procedure in detail: presentation and acceptance, with positive evidence sought. Their grounding criterion makes the coordination target purpose-relative ("sufficient for current purposes"). This bounds the note: what speakers coordinate on is local mutual belief for a purpose, not a population-wide meaning. The cost model also gives a mechanism for the note's prediction that meaning is sharpest where correction is cheap. This is supporting description; the source does not test the hypothesis.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: on what counts as evidence of understanding. An agent that silently picks a reading is running the negative-evidence default that Clark and Brennan reject: it assumes the spec was understood because nothing flagged trouble. Their demand for positive evidence explains why final success cannot show that the contract determined the path. No acceptance phase ever exposed the chosen reading.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- **compares-with**: on repair cost by medium. The note says humans "can only append corrections". Clark and Brennan restrict that to cotemporal speech. Letters and email have revisability, and in media that are not cotemporal, senders revise before sending because repair initiated by others is costly. Prompt refinement is the revisable-medium strategy, and conversational Q&A is the cotemporal one. Least collaborative effort supplies a cost criterion that the note's tradeoff section lacks.
- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) -- **compares-with**: on what is lost when interaction is removed. The note lists operator functions. Clark and Brennan give a medium-level account of the same loss: without cotemporality and simultaneity, acknowledgments, relevant next turns and continued attention are no longer available as evidence. Grounding cost moves to formulation, or the parties change medium. This names the communicative channel through which the note's correction and evaluation functions are delivered.
- [On the Means for Clarification in Dialogue (Purver, Ginzburg, Healey)](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) -- **compares-with**: on clarification requests as acceptance-phase moves. Purver et al. measure how often clarification requests occur and classify their forms. Clark and Brennan place them in the contribution model as side sequences that give negative evidence and locate the trouble, nested inside an acceptance phase. Together the two give the theory and the corpus figures for one mechanism.
- [The Preference for Self-Correction in the Organization of Repair (Schegloff, Jefferson, Sacks)](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) -- **compares-with**: on why self-repair is preferred. Schegloff et al. describe the preference as sequence organization. Clark and Brennan explain it by least collaborative effort: repair by the other party costs extra turns and must itself be accepted. They also extend it across media, where that cost rises sharply when the medium is not cotemporal. Clark and Brennan cite the paper directly.
- [Norman, The problem of automation: inappropriate feedback and interaction](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with**: on continual feedback as evidence of shared state. Norman's automation fails because it withholds the continuing feedback a human co-worker gives. In Clark and Brennan's terms, it withdraws continued attention and acknowledgments, so the operator cannot tell whether the shared state still holds.
- [PD of HCI - Plans and Situated Actions (summary of Suchman)](../../../../sources/pd-of-hci-suchman-plans-situated-actions-summary.ingest.md) -- **compares-with**: on undetected breakdowns. The copier's "false alarm" and "garden path" breakdowns are failures of the acceptance phase. The machine takes the user's next action as evidence of understanding without checking whether that action is a relevant next turn. Clark and Brennan's rule that a next turn counts as positive evidence only "unless it shows her understanding to be correct" names exactly what the copier lacked.

## Bidirectional Candidates

- [Purver et al.](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md) <-> source -- **compares-with**: Purver et al. may cite Clark's grounding work, but no tracked ingest exists to link back to. Once the Clark and Brennan ingest exists, the Purver ingest could gain a footer edge giving clarification requests their place in the contribution model.
- [Schegloff et al.](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) <-> source -- **compares-with**: a return edge would give the Schegloff ingest the cost explanation (least collaborative effort) for the preference it documents. Both sibling ingests are untracked work in progress, so the return edge is the ingest owner's call.

## Reverse-edge Candidates

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) → future `kb/sources/clark-brennan-grounding-in-communication.ingest.md` -- **evidenced-by** (theory label): qualifies and bounds the claim. The coordination target is mutual belief to a purpose-relative criterion, and the strength of checking varies with what evidence the medium makes cheap. Under the theory collection's "origin is not corroboration" rule, the context phrase must say this qualifies rather than corroborates. The note is already at three external sources, so watch the unquoted-source bound.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → future ingest -- **evidenced-by** (qualifies): this gives the human-communication account of why negative evidence alone is insufficient. It is weaker than the forward compares-with edge, so author at most one of the two.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Acceptance authority does not require a separate repair session](../../../../theory/acceptance-authority-does-not-require-a-separate-repair-session.md) -- rejected. The shared words "acceptance" and "repair" are homonyms here. Clark and Brennan's acceptance phase is about mutual belief in understanding; the note's acceptance is workflow authority over output. A link would invite a false mapping. The Schegloff ingest already carries the producer-repair parallel.
- [Re-re-reading Lucy Suchman's Plans and Situated Actions](../../../../sources/jan-dittrich-rereading-suchman-plans-actions.ingest.md) -- rejected as redundant with the PD of HCI summary for this source's contribution. Its repair-asymmetry point is about who repairs, which the Schegloff edge covers better.
- [Frontloading spares execution context](../../../../theory/frontloading-spares-execution-context.md) -- rejected. Its claim concerns execution-context budget, not the trade between formulation cost and repair cost. A link would be a surface analogy only.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) and [writing styles are strategies for managing underspecification](../../../../theory/writing-styles-are-strategies-for-managing-underspecification.md) -- rejected. Both are about spec interpretation without interaction. Clark and Brennan add nothing concrete beyond what natural-language-meaning and silent-disambiguation already route.
- [Intent-framed delegation is a control regime](../../../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) -- rejected. "Shared understanding" there comes from military doctrine and is not about grounding procedure. Too indirect.
- [claims-and-grounding tag](../../../../tags/claims-and-grounding-README.md) -- rejected as a source tag. The tag's "grounding" is support for claims from sources, which is a different sense.

## Index Membership

None. `kb/sources/README.md` does not enumerate ingests, and no tag head's inclusion condition fits this source's analysed contribution.

## Synthesis Opportunities

Clark and Brennan, Purver et al., Schegloff et al., Norman and the Suchman summary together suggest a higher-order claim that the theory collection does not yet state. Human communication keeps understanding checkable by requiring positive evidence in-band and cheaply, and the cost of that evidence depends on the medium. Agent handoffs and specs work like a medium that is neither cotemporal nor simultaneous. That would predict the cost shifts the KB observes separately: frontloaded formulation, prompt refinement instead of append-only repair, and silent disambiguation where no acceptance phase exists. The workshop `kb/work/formal-semantics-and-codification/` appears to be assembling this, but connect does not link into it.

## Maintenance Observations

- **Vocabulary collision: "grounding".** The KB uses "grounding" for source support of claims: `cp-skill-ground`, the `claims-and-grounding` tag, ADR 079 and ADR 082. Clark and Brennan's "grounding" means establishing mutual understanding. Neither the [vocabulary collision ledger](../../../../reference/vocabulary-collision-ledger.md) nor the AGENTS.md vocabulary covers it. An ingest of this paper, and the workshop that uses it, will put both senses in nearby text. The writer should qualify the term at first use (for example "conversational grounding (Clark & Brennan)"), or the ledger should record the near collision.
- No tracked ingest exists for this snapshot. All forward edges depend on `cp-skill-ingest` producing `kb/sources/clark-brennan-grounding-in-communication.ingest.md`.

## Flags

- Tension to keep visible: [conversation-vs-prompt-refinement](../../../../theory/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) states that humans "can only append corrections". This source qualifies that statement by medium, since revisable media allow private revision before sending. The report does not resolve the tension.
