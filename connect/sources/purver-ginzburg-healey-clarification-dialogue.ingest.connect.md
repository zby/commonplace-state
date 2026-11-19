---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/purver-ginzburg-healey-clarification-dialogue.ingest.md"
source_has_frontmatter: true
date: "2026-11-01"
depth: standard
---

# Connection Report: Ingest: On the Means for Clarification in Dialogue

**Source:** [Ingest: On the Means for Clarification in Dialogue](../../../../sources/purver-ginzburg-healey-clarification-dialogue.ingest.md)

The ingest already carries six footer links: `derived-from` the paper, `is-evidence-for` the natural-language-meaning note, and `compares-with` to the silent-disambiguation note, the conversation-vs-prompt-refinement note and the two Suchman ingests. This report lists only edges it does not have yet. It also checks the existing edges.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md`, Outbound links. Allowed destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources and external. Excluded: `kb/work/` and `kb/instructions/`. So the occasion's workshop target, `kb/work/formal-semantics-and-codification/where-meaning-is-settled.md`, gets no candidate. Labels: `is-evidence-for` (theory, agent-memory-systems); `compares-with` (theory, sources, agent-memory-systems, agentic-systems); `abstracted-from` and `rests-on` (theory); `defined-in` (theory/definitions); `see-also` (sparingly); `derived-from` (external). External prospecting was skipped. The only external target is the paper URL, and the ingest already links it.

**Topic indexes:**
- `ls kb/tags/`. No tag head covers dialogue, natural-language semantics or conversational repair. The candidates `llm-reliability` and `failure-modes` are about LLM or system behaviour. This source is about human dialogue, so no tag applies (source tags are optional).

**Description listing and body search:**
- `rg -l -i "clarification|clarify|repair|disambiguat|misunderstand|grounding in conversation|common ground|ginzburg|schegloff|conversation analysis|dialogue"` over theory, sources, agentic-systems, agent-memory-systems, reference and tags. The hits were broad and mostly incidental: "repair" in the software or review sense, and "clarify" as an ordinary verb. Used for triage only.
- `rg -n -i "clarification request|clarifying question|ask(s|ing)? (a )?clarif|conversational repair|dialogue repair|other-speaker|speaker meaning|natural language meaning|ginzburg|schegloff|purver|interactive stance|common ground|ask instead of guess|ask rather than"` over the same scope. Real hits: the target itself; the sibling ingest `schegloff-jefferson-sacks-self-correction-repair.ingest.md` (untracked, same occasion); and `program-synthesis-gulwani-polozov-singh-2017.ingest.md` (only through "underspecified instructions", rejected).
- `rg -n -i "clarif|ask the user|asks? (the )?(user|human)|escalat.*ambigu|ambigu.*(ask|question)" kb/theory`. Real hits: `specification-strategy-should-follow-where-understanding-lives.md:14`, which says interactive clarification does not yield a durable artifact (kept), and `design-for-the-first-time-human-except-on-access-cost.md:63`, which says an agent may resolve where a maintainer would ask (rejected, a passing remark).
- `rg -l -i "clarifying question|clarification question|asks? clarif"` over agentic-systems/reviews, agent-memory-systems/reviews and sources. Two hits, `hacker-news-llm-voice.ingest.md` and `the-spec-is-the-new-code...ingest.md`. Both mention clarification only incidentally (rejected). No reviewed system has a clarification-dialogue mechanism, so agentic-systems and agent-memory-systems yield nothing.
- reference: only `see-also` is allowed, and no reference doc covers dialogue repair. Skipped.

**Link following:**
- `natural-language-meaning-is-coordination-among-learned-approximations.md`. Read lines 16-34 and the footer. Line 22 names "other speakers" as a weak, distributed checker and predicts that meaning is sharpest where correction is cheap and frequent. The existing `is-evidence-for` edge fits. The footer leads to `oracle-strength-spectrum.md`, `llm-output-deviation-requires-three-way-diagnosis.md` and `out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md`. Each was judged and rejected (see below).
- `silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md`. Its body is about agents and specs. The existing `compares-with` axis (is a wrong reading made visible?) is specific. Kept as is.
- `conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md:18`: "humans can't rewind ... can only append corrections". The existing edge's locality axis fits.
- `schegloff-jefferson-sacks-self-correction-repair.ingest.md` footer. It links silent-disambiguation, acceptance-authority, error-messages-that-teach, revision-guided-by-rationale, the-bug-that-shipped and Dittrich. It does not link this ingest. Its silent-disambiguation edge overlaps with ours: it covers §6.3, unmarked proceeding as adequate understanding. The target's ingest also uses silence as acceptance, so the two are complementary.
- `jan-dittrich-rereading-suchman-plans-actions.ingest.md:46`: the "interpretive asymmetry" synthesis asks for primary grounding on repair. The existing edge fits.

## Connections Found

- [Schegloff, Jefferson and Sacks, preference for self-correction](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) -- **compares-with**: on where repair is initiated and what it targets. Schegloff et al. give the qualitative organization: positions, self- versus other-initiation, the preference for self-repair. This paper counts one slice of it: other-initiated, next-turn clarification requests, sorted by form and reading, with a measured distance to the trouble source. Both ingests were made for the same workshop claim. Both find the same gap: neither source separates conventional expression meaning from speaker intent. A reader of either one needs the other. *Caveat:* the target is untracked in git, so this link should go in only once both are committed.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- **compares-with**: on the durability of disambiguation. The note puts interactive clarification outside its scope, because clarification "does not by itself produce something later sessions can inspect and inherit". This paper measures that in-band channel. It is frequent (3-4% of sentences), it is local (over 96% of CRs target a sentence within four), and it needs only about ten utterances of retained surface form. So the paper quantifies the case the note sets aside. Weaker than the Schegloff edge. Include it only if the ingest's analysis keeps a durable-versus-in-band point.

## Bidirectional Candidates

- [Schegloff, Jefferson and Sacks, preference for self-correction](../../../../sources/schegloff-jefferson-sacks-self-correction-repair.ingest.md) <-> source -- **compares-with**: the return edge is just as useful. That ingest's footer has no other source on clarification requests, and this paper gives figures for the other-initiation position it describes.

## Reverse-edge Candidates

Under `kb/theory/COLLECTION.md`, a theory note may link a source with `evidenced-by`. The phrase must say whether the source corroborates the claim or only qualifies or bounds it. This one is descriptive, so a test the claim could have failed is not available.

- [Natural-language meaning is coordination among learned approximations](../../../../theory/natural-language-meaning-is-coordination-among-learned-approximations.md) → source -- **evidenced-by**: qualifies the "other speakers as checker" claim (line 22). The paper shows the checker working in-band at about 3-4% of dialogue sentences. But only about 15% of those requests (constituent readings) ask what an expression refers to, so most of this checking is about hearing the words and identifying the move. Not corroboration: the hypothesis did not risk failing here.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → source -- **evidenced-by** (optional, weak): bounds the human contrast case. In dialogue the initiator's next move exposes a wrong reading ("spunyarn"). The annotation method counted silence as acceptance, so it cannot see misunderstandings that neither party noticed, which is exactly what the note is about. Add only if the note grows a human-dialogue comparison.

## Off-authorisation Candidates

- `kb/work/formal-semantics-and-codification/where-meaning-is-settled.md` -- this is the ingest's occasion and its main consumer, but sources may not link into `kb/work/`. Correctly off-scope. The workshop should link this ingest from its own side; it is not a contract gap.

## Raw Text Candidates

None

## Rejected Candidates

- [Oracle strength spectrum](../../../../theory/oracle-strength-spectrum.md) -- the natural-language-meaning note already does the work of placing speakers at the weak end. A direct edge would add nothing beyond the existing `is-evidence-for` link.
- [LLM output deviation requires three-way diagnosis](../../../../theory/llm-output-deviation-requires-three-way-diagnosis.md) -- the lexical, constituent and clausal readings look a little like the note's three questions, but the axes differ (transmission, reference and move versus V/I/D). An edge would mislead.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- settling readings by uptake is close to that note's "competent reader" test only by keyword. Not specific enough.
- [Design for the first-time human except on access cost](../../../../theory/design-for-the-first-time-human-except-on-access-cost.md) -- mentions asking for clarification once, in passing. Not a claim the paper bears on.
- [Agentic systems interpret underspecified instructions](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) and [Changing requirements conflate genuine change with disambiguation](../../../../theory/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- these are about the semantics of agent specs. The paper is about spoken human dialogue and gives them no mechanism or evidence beyond what the natural-language-meaning note carries.
- [Acceptance authority does not require a separate repair session](../../../../theory/acceptance-authority-does-not-require-a-separate-repair-session.md) -- the Schegloff ingest links it on who repairs. This paper counts clarification requests, not who repairs, so the axis does not carry over.
- `hacker-news-llm-voice.ingest.md`, `the-spec-is-the-new-code-a-guide-to-spec-driven-development.ingest.md`, `program-synthesis-gulwani-polozov-singh-2017.ingest.md` -- keyword-only hits.

## Index Membership

None. No tag head covers dialogue or natural-language semantics, and source tags are optional.

## Synthesis Opportunities

The two sibling ingests, this one and Schegloff et al., plus the two Suchman ingests, give primary support for the repair asymmetry that the Dittrich ingest proposes as a synthesis. In human dialogue, repair is organized, frequent, local and settled by uptake. Classic machines do not detect breakdowns. The open question is whether LLM agents' silent disambiguation is a third case. Both primary sources share a limit: they cannot see misunderstandings that neither party noticed, which is the case silent disambiguation is about. That limit should travel with any synthesis. Do not write the synthesis from connect. It belongs to the workshop.

## Maintenance Observations

- The target ingest and its sibling `schegloff-jefferson-sacks-self-correction-repair.ingest.md` were written for the same occasion, and neither links the other. This is a sibling-ingest coordination gap. It is a candidate edge, not a defect, until both are tracked.
- Every existing footer path in the target resolves.

## Flags

- No split candidate. The ingest makes one analytical contribution (a CR taxonomy plus frequency) and links into one topic area.
- Tension, not resolved here: the ingest's `is-evidence-for` edge to the natural-language-meaning note, set against its own Extractable Value item 3. Most CRs are not about expression meaning. The context phrase already says "qualified by the small constituent-reading share", so the label and phrase agree. A reviewer may still ask whether `compares-with` is the more honest label.
