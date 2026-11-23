---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/sep-practical-reason.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: Practical Reason (Stanford Encyclopedia of Philosophy, Wallace and Kiesewetter)

**Source:** [Ingest: Practical Reason](../../../../sources/sep-practical-reason.ingest.md)

The ingest already authors seven outbound edges, all of which resolve. They
were carried over from the earlier snapshot-level connect report
(`sep-practical-reason.connect.md`). This run checks those edges and adds the
candidates that appeared after that run, mainly the sibling ingests created in
the same workshop session.

## Discovery Trace

**Collection contract:** `kb/sources/COLLECTION.md` outbound section. Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting skipped: no web search; the `source` URL is already the external anchor.

**Existing outbound links verified:** all seven targets plus `epistemic-stance.md` and `definitions/tentative-theory.md` resolve (`ls` loop).

**Topic indexes:**
- `kb/tags/goal-prioritization-README.md` (source carries `tags: [goal-prioritization]`). Its listed members include the objective-revision and intent notes, both already linked from the ingest. The head links sources by hand and does not list this ingest (see Index Membership).

**Titles listing (theory):**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md' | rg -i "goal|objective|choice|choos|judg|intent|commit|belief|end|measure|prefer|decid|decision|trade|value|weigh|plan|fallib|revis|stop|criteri"`. Flagged: Commitment, not derivation, creates new ground truth; Productive deferral; Information value is observer-relative; Self-improvement is relative to a declared objective; Technical constraints turn KB objective-function choice into engineering; Ad hoc explanation can be rational when error is cheap. All are evaluated under Rejected Candidates. Already-linked titles reappeared: on-balance, capacity-building commitment, superseded choices, objective revision, intent.

**Body search:**
- `rg -n -i "deliberat|practical reason|direction of fit|satisfic|incommensurab|exclusionary|bootstrapping|maximiz|plural values|value plural" kb/theory kb/reference kb/sources kb/agentic-systems kb/agent-memory-systems -l` -- broad and mostly substring noise in reviews ("maximize" and similar).
- `rg -n -i "practical reason|direction of fit|satisfic|incommensurab|exclusionary reason|bootstrapping|expected utility|plural values|value plural|weigh(ing)? (the )?(considerations|reasons)|on balance|on-balance|deliberati" kb/theory kb/sources` -- hits: the on-balance note (known); russell-wefald ingest (known); `information-value-is-observer-relative.md` (Simon satisficing, one line); `soft-bound-traditions...` (Simon satisficing in a table); `self-improvement-is-relative-to-a-declared-objective.md` (incomparability under a partial order); the Gödel-machine and open-ended-improvement notes (expected utility as a switching criterion); `intern-s2-mobius` ("internalized deliberation", LLM sense). "Direction of fit" has no KB hit outside this ingest.
- `rg -n "sep-practical|practical-reason" kb` -- inbound: only `kb/work/learning-method-name/draft-definition.md` (workshop, excluded as a link target), the Fishkin–Mansbridge ingest (prose mention, no link), and connect reports. No library artifact links this ingest yet.
- `rg -n -i "deliberat|on-balance|practical" kb/reference/vocabulary-collision-ledger.md kb/reference/epistemic-stance.md` -- no ledger record for "deliberative"; epistemic stance links the on-balance note at line 45.
- `rg -n -i "deliberati" kb/agentic-systems/reviews kb/agent-memory-systems/reviews -l` -- one hit (crewai-memory), keyword-only.

**Sources sweep (sibling ingests from the same occasion):**
- Untracked ingests in git status: `fishkin-mansbridge-deliberative-democracy-intro.ingest.md` (group sense of deliberation; its Extractable Value 3 says a necessarily-social claim "needs the individual sense from a practical-reason source as its contrast"), `minton-utility-of-ebl-aaai88.ingest.md` (utility-based rule admission), `wooldridge-jennings-intelligent-agents.ingest.md` (known).
- `rg -n "practical|deliberat|fishkin|sep-" kb/sources/wooldridge-jennings-intelligent-agents.ingest.md` -- Wooldridge does not link this ingest or Fishkin–Mansbridge.

**Link following:**
- On-balance note footer (`Relevant Notes:`) -- links only the self-improvement note; no source ingest attached. That makes a reverse edge to this ingest more useful than the prior report estimated.
- Self-improvement note "What follows" -- links on-balance for choosing between incomparable viable configurations. This is the same position the ingest situates, so it adds no new target.
- Prior snapshot connect report (`kb/reports/state/connect/sources/sep-practical-reason.connect.md`) -- its Connections Found match what the ingest now carries; its rejections were rechecked and still hold.

### Candidate origins

- kb/sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md — known, body-search
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — known, body-search
- kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md — known, titles, body-search, link-following
- kb/theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md — known, titles
- kb/reference/epistemic-stance.md — known, body-search

## Connections Found

- [Introduction to Deliberative Democracy (Fishkin and Mansbridge)](../../../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md) -- **compares-with**: the individual versus group sense of deliberation. This entry gives joint deliberation one parenthesis and otherwise treats one agent weighing reasons for and against action. Fishkin and Mansbridge define deliberation as group weighing of competing arguments under good information, civility and diversity, and never consider a single deliberator. A reader checking which sense "deliberative learning" uses needs both ingests side by side. This also closes the gap the ingest's own Extractable Value 2 names (grounding a joint sense here "is not" safe).

## Bidirectional Candidates

- [Introduction to Deliberative Democracy (Fishkin and Mansbridge)](../../../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md) <-> source -- **compares-with**: that ingest's Extractable Value 3 says a necessarily-social claim needs "the individual sense from a practical-reason source as its contrast". It names this source in prose but does not link it. A return link would turn that prose mention into a link.
- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) <-> source -- **compares-with**: this ingest already links Wooldridge for the sense of "deliberative". Wooldridge's Extractable Value 1 ("architectural, not about the choice standard") and 5 ("learning ... outside the deliberative definition") are exactly the contrast this entry supplies, so the return path helps a reader starting from the architectural sense.

## Reverse-edge Candidates

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) → source -- **evidenced-by** (theory label): the note's footer cites no source. §§5–6 show that choosing without a single measure is a recognized position, with known objections and maximizers' replies. The note's "known requirements need not be weighed afresh" also corresponds to exclusionary reasons. This is the strongest reverse edge: it qualifies the note as well as corroborating it.
- [Theory building and capacity building make the same kind of fallible commitment](../../../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md) → source -- **evidenced-by** (theory label): the note could name its explanatory/constructive split "direction of fit" and cite §2 through this ingest. That would expose the literature and its critique (Frost 2014).
- [Epistemic stance](../../../../reference/epistemic-stance.md) → source -- low priority. Its "Judgment under uncertainty" section already links the on-balance note, which is the better carrier. Check the reference collection's own labels before authoring.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Minton, The utility of explanation-based learning](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md) -- its single utility formula for admitting control rules is a maximizing measure, but the entry does not discuss rule learning. [Russell and Wefald](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md), already linked, carries the maximizing comparison; adding Minton would duplicate it.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- Bratman's plans-as-commitments overlap, but the capacity-building note carries the direction-of-fit comparison more precisely (unchanged from the prior run).
- [Productive deferral requires option evidence and convergence](../../../../theory/productive-deferral-requires-option-evidence-and-convergence.md) -- about the timing of commitment under option value. The entry's Bratman material concerns plans as defeasibly fixed constraints, not when to defer. A link would rest on the word "commit" only.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- cites Simon's satisficing as background; the entry attributes satisficing to Slote's normative argument, not to bounded computation. The link would rest on the shared term only.
- [Self-improvement is relative to a declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) -- its incomparability-under-partial-order point is close to §6 incommensurability. However, it routes the choice to the on-balance note, which is already linked and is the better carrier.
- [Technical constraints turn KB objective-function choice from philosophy into engineering](../../../../theory/technical-constraints-make-kb-objective-choice-engineering.md) -- keyword overlap; the objective-revision note carries the ends comparison.
- [Ad hoc explanation can be rational when error is cheap and local](../../../../theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) -- concerns the cost of explanatory error; the entry says nothing on cost (its Limitations section says so).
- Gödel-machine and open-ended-improvement notes -- use expected utility as a formal switching criterion; the entry's §5 objections bear only indirectly, and Russell–Wefald already carries the maximizing axis.
- `intern-s2-mobius-arxiv-v1.ingest.md` -- "internalized deliberation" names LLM latent reasoning, a different sense; keyword-only.
- agentic-systems and agent-memory-systems -- one keyword hit (crewai-memory); no candidates.

## Index Membership

- [Goal prioritization tag head](../../../../tags/goal-prioritization-README.md) -- the ingest carries `tags: [goal-prioritization]`, but the head links sources by hand and does not list it. A future head edit could list it under "Objectives, requirements and who sets them", noting that it surveys weighing without a single measure, exclusionary reasons and specification of inchoate ends.

## Synthesis Opportunities

The prior run's synthesis still stands and is now better evidenced. The on-balance note, the capacity-building commitment note and the superseded-choices note all use the practical/theoretical reason split without naming it. With three sibling ingests in place (this entry's single-agent weighing sense, Fishkin–Mansbridge's group sense, Wooldridge–Jennings's architectural sense), a definition note could state which sense of "deliberative" Commonplace uses. That is the workshop's job and should not be done here.

## Maintenance Observations

- No library artifact links this ingest yet. All inbound value currently flows only through the workshop draft, which is excluded as a link target.
- "Direction of fit" still has no KB hit outside this ingest; it remains an unnamed mechanism in at least two theory notes.
- The prior snapshot-level report (`sep-practical-reason.connect.md`) says the on-balance note has "six source ingests attached as formal tools". The note's current `Relevant Notes:` footer lists none, so that observation is stale or refers to links elsewhere in the body.
- No vocabulary-collision record exists for "deliberative", although three ingests now record three different senses (single-agent weighing, group weighing, symbolic architecture). If the workshop adopts the term, it is a candidate for the ledger.

## Flags

- Not a split candidate: the ingest's connections span several topic areas, but it serves one occasion (anchoring "deliberative") and makes no independent assertions of its own.
- Tension, not resolved here: the ingest supports a single-agent sense; Fishkin–Mansbridge supports a group sense. The draft definition must choose one sense or state both.
