---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/sep-practical-reason.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Practical Reason (Stanford Encyclopedia of Philosophy)

**Source:** Practical Reason, `kb/sources/.snapshots/sep-practical-reason.md` (local snapshot; not linked because snapshots are Git-ignored and no paired ingest exists yet)

The source is an immutable snapshot (Wallace and Kiesewetter, SEP, revised 2024-07-31). No `sep-practical-reason.ingest.md` exists yet, so every outbound candidate below is a recommendation for that future ingest, which carries the snapshot's authored surface under `kb/sources/COLLECTION.md`. The external citation target is <https://plato.stanford.edu/entries/practical-reason/>.

Source content used for judging: §1 practical vs theoretical reason as two systems of norms (practical vs epistemic) that issue in intentions vs beliefs; §2 direction of fit (Anscombe's blueprint, Searle), expressivism, realism, Kantian constructivism; §3 internalism vs externalism about reasons; §4 instrumental and structural rationality, wide-scope requirements, the bootstrapping objection; §5 the maximizing conception and its critics (Slote's satisficing, Bratman's plans as defeasibly fixed constraints, Buchak's risk attitudes), desire laundering, the perspectivist "ought"; §6 specification of inchoate ends (Kolnai, Wiggins, Richardson), value-based and hybrid reasons under incommensurability (Chang), agent-relative and exclusionary reasons (Raz).

## Discovery Trace

**Setup:**
- Source collection `sources`; read `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded: `kb/work/`, `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external).
- External prospecting skipped; the only external target already in hand is the SEP URL itself (the ingest's `derived-from`/`source` target, not a connection candidate).
- Workshop context read for relevance only (not linkable): `kb/work/learning-method-name/README.md` and `draft-definition.md` are naming "deliberative learning" and rest on the on-balance note; the companion untracked ingest `wooldridge-jennings-intelligent-agents.ingest.md` was made for the same draft.

**Curated heads:**
- `kb/tags/goal-prioritization-README.md` (not `complete: true`) — linked theory members scanned; flagged `intent-controls-choices-by-distinguishing-live-alternatives.md`, `revising-an-improvement-objective-is-licensed-from-outside-it.md`, `lightweight-search-control-does-not-license-adoption.md`.
- `kb/tags/evaluation-README.md` description read; no new candidates beyond the on-balance note.
- Tag-head file list scanned (`ls kb/tags/`); `goal-prioritization`, `evaluation` and `learning-theory` are the plausible topical heads.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (442 titles), filtered with `rg -i "judg|reason|decid|decision|goal|value|norm|weigh|balance|improv|criteri|measure|evaluat|choice|choos|action|commit|deliber|intent|plan|rational|theory|belief|epistem"`. Flagged: "On-balance judgments can guide improvement without a global measure", "Intent controls a local choice only when it distinguishes its live alternatives", "Revising an improvement objective is licensed from outside it or is not improvement", "Theory building and capacity building make the same kind of fallible commitment", "Superseded choices need a historical witness; refuted beliefs lose subject-matter standing", "Commitment, not derivation, creates new ground truth", "Self-improvement is relative to a declared objective", "Reasoning production is not reasoning evaluation", "Ad hoc explanation can be rational when error is cheap and local", "Technical constraints turn KB objective-function choice from philosophy into engineering", "Lightweight search control allocates further search without licensing adoption". Paths resolved with `rg -l -F -x '# <title>' kb/theory/` and descriptions read.

**Body search:**
- `rg -l -i "practical reason|on-balance|on balance|weigh(ing)? (of )?reasons|deliberat|satisfic|instrumental rational|akrasia|direction of fit|bratman|reasons for action|pro tanto|exclusionary" kb` (excluding work, reports, snapshots) — broad; mostly incidental "deliberate" hits in reference/ADRs. Surfaced the on-balance note.
- `rg -l -i "on-balance|on balance|practical reason|satisfic|instrumental rational|akrasia|direction of fit|bratman|pro tanto|exclusionary|wide-scope|structural rational|decision theory|expected utility|incommensurab|weigh(s|ing)? (the )?(reasons|considerations)" kb/theory kb/sources` — surfaced the on-balance decision-analysis source cluster (`mustajoki-interval-smart-swing`, `greco-ordinal-regression-revisited`, `angilella-ordinal-regression-smaa-choquet`, `the-price-of-robustness`, `baudrit-joint-propagation-probability-possibility`, `making-reflective-equilibrium-precise`), plus `russell-wefald-principles-of-metareasoning`, `provably-bounded-optimal-agents`, `wooldridge-jennings-intelligent-agents`.
- `rg -n -i "direction of fit|anscombe|world-to-mind|mind-to-world" kb` — no KB artifact uses the direction-of-fit vocabulary (only an Anscombe citation inside a Sutskever list chapter). The concept is present unnamed in the explanatory/constructive commitment note.
- `rg -n -i "binding requirement|exclusionary|pre-empt|weighed afresh" kb/theory kb/reference` — on-balance note line 63 ("Known requirements need not be weighed afresh … an on-balance judgment does not override a binding requirement") is the KB's unnamed counterpart of Raz's exclusionary reasons in §6.
- `rg -l -i "practical reason|BDI|belief-desire|satisfic|bratman|akrasia" kb/agentic-systems kb/agent-memory-systems kb/reference` — hits in `Agent-S.md`, `cobusgreyling--llm-wiki.md`, `agentic-systems/COLLECTION.md` checked: substring matches in URLs/hashes, not content. No candidates in agentic-systems or agent-memory-systems.
- `rg -n -i "normative|reasons for belief|epistemic norm|ought" kb/reference/epistemic-stance.md`, then read lines 38-60 ("Judgment under uncertainty").
- Per-ingest checks: `rg -n -i "practical reason|on-balance|satisfic|bratman|intention|deliberat|incommensur|weigh"` over each flagged source ingest.

**Candidate evaluations:**
- On-balance note: read in full. Kept (`is-evidence-for`).
- `theory-and-capacity-building-make-the-same-kind-of-commitment.md` (lines 1-40 read): explanatory commitment "remains answerable to the object it describes"; constructive commitment "changes the object". Kept (`compares-with`, direction of fit).
- `superseded-choices-are-retained-superseded-beliefs-are-not.md` (lines 9-40 read): belief answers to independent evidence; choice event answers to the act of choosing. Kept (`compares-with`, epistemic vs practical norms under revision).
- `revising-an-improvement-objective-is-licensed-from-outside-it.md` (lines 1-25 read): "every objective approves of itself"; under-specification surfacing. Kept (`compares-with`, rational criticism of ends).
- `intent-controls-choices-by-distinguishing-live-alternatives.md` (lines 1-30 read): a high-level purpose compatible with every live option cannot select; a bridge derives a specific purpose. Kept (`compares-with`, specification of inchoate ends).
- `wooldridge-jennings-intelligent-agents.ingest.md`: architectural definition of "deliberative agent", IRMA, intention reconsideration listed as unaddressed. Kept (`compares-with`, sense of "deliberative").
- `russell-wefald-principles-of-metareasoning.ingest.md` (lines 80-92 read): value of computation as expected-utility benefit to the next action. Kept (`compares-with`, maximizing conception).
- Others rejected; see Rejected Candidates.

**Link following:**
- On-balance note → `self-improvement-is-relative-to-a-declared-objective.md` (its only footer link) → `revising-an-improvement-objective-is-licensed-from-outside-it.md` (already flagged).
- On-balance note → `a-better-factory-claim-compares-operative-states.md` (binding requirement fixed before development) — the exclusionary-reasons parallel lands on the on-balance note's own paragraph, so no separate candidate.
- `theory-and-capacity-building…` → `commitment-not-derivation-creates-new-ground-truth.md`; considered for Bratman's "plans as defeasibly fixed constraints", rejected as redundant with the capacity-building note.
- `epistemic-stance.md` "Judgment under uncertainty" → on-balance note (it restates the note's investigate-only-if-reversing rule).
- Decision-analysis ingests each link the on-balance note; they form a formal-tools cluster around it.

### Candidate origins

- kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md — known, body-search, titles, curated-head
- kb/theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md — titles
- kb/theory/superseded-choices-are-retained-superseded-beliefs-are-not.md — titles
- kb/theory/revising-an-improvement-objective-is-licensed-from-outside-it.md — titles, curated-head, link-following
- kb/theory/intent-controls-choices-by-distinguishing-live-alternatives.md — titles, curated-head
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — known, body-search
- kb/sources/russell-wefald-principles-of-metareasoning.ingest.md — body-search
- kb/reference/epistemic-stance.md — body-search, link-following

## Connections Found

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) -- **is-evidence-for**: §5 surveys the standing objections to treating practical rationality as maximization of one utility function: rational agents satisfice (Slote 1989), treat prior plans as defeasibly fixed constraints rather than re-maximizing (Bratman 1987), and adopt differing risk attitudes (Buchak 2013). §6 adds incommensurable values and Chang's hybrid view, and Raz's exclusionary reasons that enter deliberation without being weighed. These bear on the note's claims that a choice needs no global measure and that "known requirements need not be weighed afresh". The perspectivist "ought" (§5, Kiesewetter) bears on the rule to investigate only unknowns that could reverse the choice. Caveat for the ingest: this is a survey reporting live disputes (maximizers reply that the model accommodates these cases, Pettit 1984), so it qualifies and situates the note; it does not test it.
- [Theory building and capacity building make the same kind of fallible commitment](../../../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md) -- **compares-with**: direction of fit. §2 contrasts belief, which must fit the world, with intention, which is "more like an architect's blueprints" (Anscombe, Searle). The note's split between an explanatory commitment that "remains answerable to the object it describes" and a constructive commitment that "changes the object" is the same distinction applied to retained KB and software changes. The source supplies the established name and the literature (including Frost 2014's critique of the metaphor) that the note currently lacks.
- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../theory/superseded-choices-are-retained-superseded-beliefs-are-not.md) -- **compares-with**: epistemic vs practical norms under revision. §1's second conception treats theoretical and practical reason as two systems of norms, issuing in belief and intention respectively. The note's asymmetry (a refuted belief loses standing; a superseded choice keeps an event-fact) is a retention consequence of that split. A reader can check whether the note's asymmetry depends on any one of the §2 metaethical positions (expressivist, realist, constructivist); it appears not to.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- **compares-with**: whether ends can be rationally criticized. The note's "every objective approves of itself" parallels the bootstrapping objection in §4 (adopting an end cannot by itself create reasons, Bratman 1981, Broome 2001). Its "under-specification surfacing" subtraction parallels §6's specificationist view that inchoate final ends are refined by reasoning (Kolnai, Wiggins, Richardson). Its residue corresponds to the Humean position that there is no reasoning about final ends. The comparison shows which of the note's moves are already positions in the practical-reason literature.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) -- **compares-with**: specification of indeterminate ends. §6 says ends like career success or loyalty "will not provide effective starting points" for means-end reflection until specified. The note says a high-level purpose compatible with every live option cannot select among them without a bridge that derives a more specific purpose. Same mechanism; the source places it as a task of practical reason outside instrumental and maximizing reasoning.
- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) -- **compares-with**: the sense of "deliberative". The SEP entry defines practical reason as the capacity to settle what to do through reflection on reasons, concluding in intention or action. Wooldridge and Jennings define a deliberative agent architecturally (symbolic world model plus logical reasoning) and give no choice standard. Both draw on Bratman's intentions; the survey lists intention reconsideration as unaddressed, while SEP §5 cites Bratman's plans as defeasibly fixed constraints. A reader checking a borrowed use of "deliberative" needs both senses.
- [Russell and Wefald, Principles of Metareasoning](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md) -- **compares-with**: the maximizing conception. Russell and Wefald value a computation by its expected-utility benefit to the next action. SEP §5 presents that conception as the dominant formal account of practical rationality and lists the objections to it (satisficing, plan stability, risk attitudes, the vacuity of revealed preference). The comparison shows which philosophical objections a decision-theoretic metareasoning account inherits.

## Bidirectional Candidates

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) <-> source -- **evidenced-by** (theory label): once the ingest exists, the note could cite it in its footer as bounding and situating its claim. The note currently treats on-balance judgment as if introduced fresh; the source shows it is a recognized position against the maximizing conception, with known objections. This qualifies the note rather than corroborating it, since nothing in the source tests the note.
- [Theory building and capacity building make the same kind of fallible commitment](../../../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md) <-> source -- **evidenced-by** (theory label): the note could name direction of fit and cite the ingest for it, giving the explanatory/constructive split its established vocabulary.

## Reverse-edge Candidates

- [Epistemic stance](../../../../reference/epistemic-stance.md) → source -- **see-also** (reference label): its "Judgment under uncertainty" section declares on-balance judgment as part of Commonplace's stance. A see-also to the future ingest would point readers to the tradition behind that commitment. Low priority; the section already links the on-balance note, which is the better carrier.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Mustajoki et al., interval SMART/SWING](../../../../sources/mustajoki-interval-smart-swing.ingest.md), [Greco et al., ordinal regression revisited](../../../../sources/greco-ordinal-regression-revisited.ingest.md), [Angilella et al., SMAA-Choquet](../../../../sources/angilella-ordinal-regression-smaa-choquet.ingest.md), [The price of robustness](../../../../sources/the-price-of-robustness.ingest.md), [Baudrit and Dubois, joint propagation](../../../../sources/baudrit-joint-propagation-probability-possibility.ingest.md) -- each supplies a formal test for the on-balance note's break-even or reversal examples. The SEP entry contains no formal weighting method, so a direct compares-with would have no shared axis beyond "both concern the on-balance note". The on-balance note is the hub that already connects them.
- [Making reflective equilibrium precise](../../../../sources/making-reflective-equilibrium-precise.ingest.md) -- philosophical method in the same tradition, but the SEP entry does not discuss reflective equilibrium; a link would be topical only.
- [Provably bounded-optimal agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) -- bounded optimality is absent from the SEP entry; Russell-Wefald is the better comparison for the maximizing conception.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- Bratman's plans-as-commitments overlaps, but the capacity-building note carries the direction-of-fit comparison more precisely; adding both would duplicate.
- [Self-improvement is relative to a declared objective](../../../../theory/self-improvement-is-relative-to-a-declared-objective.md) -- the ends-criticism comparison lands on the objective-revision note, which builds on this one.
- [Reasoning production is not reasoning evaluation](../../../../theory/reasoning-production-is-not-reasoning-evaluation.md) -- concerns LLM review validity; the source's "reasoning as inference" (Harman) is only a keyword overlap.
- [Ad hoc explanation can be rational when error is cheap and local](../../../../theory/ad-hoc-explanation-can-be-rational-when-error-is-cheap-and-local.md) -- about the cost of explanatory error; the source does not discuss computational cost or bounded rationality.
- [Lightweight search control allocates further search without licensing adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) -- the source does not distinguish deliberative steps by authority.
- [Technical constraints turn KB objective-function choice from philosophy into engineering](../../../../theory/technical-constraints-make-kb-objective-choice-engineering.md) -- its "philosophy vs engineering" framing is a keyword overlap; the objective-revision note carries the substantive ends comparison.
- agentic-systems and agent-memory-systems -- no content hits (only substring matches in URLs); no candidates.

## Index Membership

- [goal-prioritization tag head](../../../../tags/goal-prioritization-README.md) -- the future ingest could carry `tags: [goal-prioritization]` if its analysis treats trade-offs among incommensurable reasons, exclusionary reasons and satisficing substantively, which §§5-6 support. Sources do not affect the head's member listing.
- [evaluation tag head](../../../../tags/evaluation-README.md) -- weaker fit; apply only if the ingest's analysis centres on how changes are judged (the on-balance connection) rather than on the theory of practical reason.

## Synthesis Opportunities

The on-balance note, the explanatory/constructive commitment note and the superseded-choice note together use, without naming it, the practical/theoretical reason split: on-balance judgment is practical reasoning about what to keep; explanatory commitments and beliefs answer to epistemic norms; constructive commitments and choices answer to practical norms. A note could state that Commonplace's retention decisions are practical judgments whose inputs include epistemic findings, and that confusing the two norm systems produces the errors these notes each guard against. Record as a possibility; do not write it during connect.

## Maintenance Observations

- No `sep-practical-reason.ingest.md` exists yet for this snapshot. All outbound candidates wait on that ingest; a concurrent ingest run may be creating it.
- "Direction of fit" is a mechanism the KB uses in at least two theory notes without naming it (`rg "direction of fit"` returns no KB artifact). Candidate for the vocabulary-collision ledger or a glossing link once the ingest exists.
- The on-balance note now has six source ingests attached as formal tools (Mustajoki, Greco, Angilella, Bertsimas-Sim, Baudrit, Beisbart et al.) but no source for the philosophical position itself. This ingest would fill that gap.

## Flags

- Tension to keep visible: SEP §5 reports that defenders of maximization claim it accommodates satisficing, plan stability and risk attitudes (Pettit 1984). An ingest citing §5 as support for "without a global measure" should record that rejoinder rather than present the objections as settled.
- The workshop `kb/work/learning-method-name/` (excluded destination) is the likely consumer: the SEP's sense of deliberation (settling what to do through reflection on reasons, issuing in intention) bears on the draft name "deliberative learning". That bearing should reach the workshop through the ingest, not through a link from sources into work.
