---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Plans and Resource-Bounded Practical Reasoning

**Source:** Plans and Resource-Bounded Practical Reasoning — snapshot `kb/sources/.snapshots/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.md` (not linked: snapshots are gitignored and no paired ingest exists yet)

The source is an immutable snapshot. Every candidate below is for the authored surface, the future `kb/sources/bratman-israel-pollack-1988-plans-resource-bounded-reasoning.ingest.md`, which did not exist when this report was written. The snapshot itself must never be linked from durable artifacts.

Source claims used for judging candidates: adopted plans constrain further practical reasoning for a resource-bounded agent in two ways (they pose means-end problems, and a compatibility filter removes options inconsistent with them before deliberation); plans must be stable to do this but revocable because agents are knowledge-bounded; a filter-override mechanism mediates stability against revocability; plans are structurally partial (ends fixed, means deferred until means-end incoherence threatens); filters may be "leaky" or "clogged"; caution (reconsidering) and boldness (not reconsidering) each sometimes pay, deliberation that leaves the plan unchanged does not pay (Situation 2), and an architecture that never deliberates wastefully and never misses worthwhile deliberation is impossible, so the override policy is judged "on balance".

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, Outbound links. Authorised destinations from an ingest: theory, theory/definitions, reference (`see-also` only), agent-memory-systems, agentic-systems, sources, tags (scan), external (`derived-from`, `see-also`). Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from`, `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, `see-also`. Snapshot is never the link author.

**Scope check:** `AGENTS.md` scope includes context engineering and decision-making in KB operation; the source enters through commitment, deliberation cost and reconsideration policy, not as general AI planning.

**Description / titles listing scan:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (444 titles), filtered with `rg -i 'deliberat|on.balance|revers|commit|plan|filter|reconsider|bounded|cost|budget|attention|stop|decid|decision|judg|interrupt|prior|stable|stabil|option|scope|narrow|constrain|cheap|expensive|trigger'`. Flagged: Reasoning limits may select for design commitments; On-balance judgments can guide improvement without a global measure; Productive deferral requires a preserved option...; Theory building and capacity building make the same kind of fallible commitment; Reversibility can favor a change by limiting future loss; Current-task fit alone does not warrant costly structural entrenchment; Commitment, not derivation, creates new ground truth; Lightweight search control...; Checking retained results trades cost against reliance risk; A theory's prototype standing is its revision cost; Reflection makes retained lessons second-order; Cost-sensitive formalisms for tentative theory search; An objection can show where to split an on-balance judgment; Context isolation for focus conflicts with global prioritization.
- Resolved paths and read descriptions for all flagged titles with `rg -l -F -x '# <title>' .` plus `rg -m1 '^description:'`.

**Topic indexes:**
- `kb/tags/goal-prioritization-README.md` (effort allocation, stopping, deferral) — surfaced Productive deferral (already flagged) and Intent controls a local choice only when it distinguishes its live alternatives (new). The head says sources are hand-linked; candidate for Index Membership once an ingest exists.

**Body search:**
- `rg -l -i 'bratman|BDI\b|belief.desire.intention|IRMA|resource.bounded|filter override|reconsideration|bounded rational|Herbert Simon|satisfic' kb --glob '*.md' --glob '!kb/sources/.snapshots/**' --glob '!kb/reports/state/**'` — hits mostly in `kb/work/` (excluded: cognitive-architecture-transfer-scan, open-ended-work-economics) and agentic-system-analyses retained runs (keyword "reconsideration", no BDI content). Also surfaced `reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md` (only "reconsideration of whether shared support merits investment"; rejected).
- `rg -n -i 'bratman|BDI\b|belief.desire.intention|resource.bounded|bounded rational|reconsider|commitment.*plan|plan.*commitment|deliberat|on balance|on-balance|stability' kb/theory -c` — top hits: on-balance judgments (9), theory-and-capacity commitment (8), reasoning-limits (5).
- `ls kb/sources/*.ingest.md | rg -i 'bratman|simon|russell|wefald|metareason|bdi|rao|georgeff|cohen|levesque|pollack|intention|pindyck|kennedy|haasnoot|githens|horvitz|boddy|dean|anytime|plan'` — found russell-wefald-principles-of-metareasoning, plans-and-situated-actions-suchman-1985 (+ two Suchman secondary summaries), pindyck, haasnoot, githens, kennedy-sobek, herbert-simon-architecture-of-complexity, intention-is-all-you-need. `ls kb/sources | rg -i 'bounded|simon|...'` added provably-bounded-optimal-agents.
- `rg -l 'russell-wefald-principles-of-metareasoning' kb` — backlinks surfaced sep-practical-reason.ingest.md and wooldridge-jennings-intelligent-agents.ingest.md, both of which discuss Bratman/IRMA directly.
- `rg -n -i 'bratman|BDI|intention|reconsider|filter|resource.bound|IRMA|pollack'` over those two ingests — SEP ingest cites "Bratman's plans are defeasible constraints"; Wooldridge-Jennings ingest summarizes IRMA and lists intention reconsideration as unaddressed.
- `rg -n -i 'bratman|BDI\b|belief.desire.intention|resource.bounded|intention reconsideration|filter override' kb/agentic-systems kb/agent-memory-systems kb/reference kb/tags` — only a vocabulary-collision gloss; no system review uses BDI.
- `rg -n -i 'plans? (as|are) (commitments|constraints)|...|replan|plan stability|reconsider(ation)? (of|the) plan' kb/theory kb/agentic-systems` — replanning mentions in autogenesis/swarmworld reviews (keyword only) and rolling-wave rows in productive deferral and problem-matches notes.

**Link following:**
- Read reasoning-limits, on-balance judgments, productive deferral, intent controls, checking retained results in full or in their opening sections; scanned theory-and-capacity, reversibility, current-task-fit for reconsideration/commitment passages.
- From russell-wefald ingest outbound links: lightweight search control, cost-sensitive formalisms, information-value, codify-versus-LLM heuristics, provably-bounded-optimal-agents. Only provably-bounded-optimal-agents was evaluated further (rejected below).
- From SEP ingest: confirms the KB already maps direction of fit onto theory-and-capacity, and positions SEP as philosophical background for the on-balance note.

**Candidate evaluations:** see Connections Found and Rejected Candidates.

**External:** no external target supplied; external prospecting skipped. The `derived-from` edge to the `source` URL is a standard ingest field, not a discovery result.

### Candidate origins

- kb/theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md — titles, body-search
- kb/theory/productive-deferral-requires-option-evidence-and-convergence.md — titles, curated-head
- kb/theory/reasoning-limits-may-select-for-design-commitments.md — titles, body-search
- kb/theory/intent-controls-choices-by-distinguishing-live-alternatives.md — curated-head
- kb/theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md — titles, body-search
- kb/sources/russell-wefald-principles-of-metareasoning.ingest.md — body-search
- kb/sources/sep-practical-reason.ingest.md — link-following, body-search
- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — link-following, body-search
- kb/sources/plans-and-situated-actions-suchman-1985.ingest.md — body-search

## Connections Found

- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) -- **compares-with**: axis is when further deliberation is worth its cost. The note's rule "investigate an unknown only if a plausible answer could reverse the choice" matches Bratman's Situation 2 (deliberation that keeps the prior intention does not pay), and the paper judges a filter-override strategy that sometimes loses (Situations 1b, 2, 4a) as "on balance" good, with the impossibility argument that no policy avoids all wasted or missed deliberation. Difference worth recording: Bratman counts deliberation cost inside the comparison (4a vs 4b), which the note leaves to "who bears the loss".
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../theory/productive-deferral-requires-option-evidence-and-convergence.md) -- **compares-with**: axis is controlled postponement of a choice. Structurally partial plans fix ends and defer means; means-end reasoning "must occur" when the plan is in danger of becoming means-end incoherent, which is a convergence rule tied to a return condition. Bratman also justifies partiality by bounded knowledge (detail about the far future is not worth deciding), close to the note's discriminating-evidence condition. Gives the note a classical AI-agent instance alongside real options, set-based design and rolling-wave planning.
- [Reasoning limits may select for design commitments](../../../../theory/reasoning-limits-may-select-for-design-commitments.md) -- **compares-with**: axis is commitments adopted because a bounded reasoner needs them to keep reasoning. Bratman's central thesis is that adopted plans exist partly to make further practical reasoning tractable for a resource-bounded agent, by posing focused means-end problems and filtering incompatible options. The note conjectures the same mechanism for code design commitments; the source is an established precedent for the mechanism, not a test of the human-versus-model conjecture.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) -- **compares-with**: axis is how a prior commitment governs later choices. Bratman's compatibility filter (removes inadmissible options) and means-end role (sets what is worth further search) are two of the note's four control routes, realized as architecture components. Bratman's filter-override adds a route the note lacks: conditions under which an excluded option is readmitted for reconsideration.
- [Theory building and capacity building make the same kind of fallible commitment](../../../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md) -- **compares-with**: axis is the stability/revocability tension in retained commitments. Bratman names the tension explicitly (plans must resist reconsideration to save reasoning but remain revocable because formed on incomplete information) and gives a mechanism (filter override with tunable sensitivity, and footnote 10's agent-adjusted thresholds). The note treats retraction but not the cost of reopening commitments too often. Weaker than the three above; the SEP ingest already supplies the direction-of-fit comparison for this note.
- [Principles of Metareasoning (Russell and Wefald)](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md) -- **compares-with**: axis is deciding whether to spend computation on deliberation. Russell and Wefald compute value of computation decision-theoretically; Bratman, Israel and Pollack cite that line (footnote 2) and instead use a cheap, designer-tuned filter plus override, accepting leaky or clogged filters. Two responses to the same resource-boundedness problem.
- [SEP: Practical Reason](../../../../sources/sep-practical-reason.ingest.md) -- **compares-with**: axis is plans as defeasible constraints on deliberation. The SEP ingest reports Bratman's position second-hand; this paper is a primary architectural statement of it, so a reader can check the SEP summary against the filter-and-override mechanism.
- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) -- **compares-with**: axis is the IRMA architecture and intention reconsideration. The survey summarizes IRMA (filtering, a deliberation process "without a stated criterion") and lists intention reconsideration as unaddressed; this paper is the primary IRMA source and supplies the caution/boldness analysis of reconsideration, though it too leaves the deliberation criterion unspecified.
- [Plans and Situated Actions (Suchman, 1985)](../../../../sources/plans-and-situated-actions-suchman-1985.ingest.md) -- **compares-with**: axis is the role of plans in action. Suchman treats plans as vague resources for situated action, not controllers; Bratman, Israel and Pollack treat adopted plans as commitments that constrain further reasoning yet are partial and revocable. Contemporaneous positions that an ingest analysis comparing plan roles should set side by side.

## Bidirectional Candidates

- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../theory/productive-deferral-requires-option-evidence-and-convergence.md) <-> source -- **evidenced-by** (theory label): the note's convergence-rule condition gains a classical agent-architecture instance (means-end reasoning forced before incoherence); phrase it as qualifying the note, not corroborating it, since the paper does not test the three-part condition.
- [On-balance judgments can guide improvement without a global measure](../../../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md) <-> source -- **evidenced-by** (theory label): bounds the note's "investigate only if a plausible answer could reverse the choice" rule with the caution/boldness trade-off, where a policy that avoids wasted deliberation necessarily risks missed worthwhile deliberation. Qualifies rather than corroborates.

## Reverse-edge Candidates

- [Reasoning limits may select for design commitments](../../../../theory/reasoning-limits-may-select-for-design-commitments.md) → source -- **evidenced-by** (theory label, qualifying): the note's "the need to continue can produce useful structure" section could cite Bratman's thesis that plans constrain further reasoning for resource-bounded agents as established precedent for the mechanism in practical reasoning, while noting it is not evidence for the human-versus-model difference.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md) → source -- **evidenced-by** (theory label, qualifying): the compatibility filter and filter override are a worked architecture of intent changing admissibility and readmission.
- [Wooldridge and Jennings, Intelligent Agents](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) → source -- **compares-with** (sources label): the survey's IRMA paragraph could point to the primary source once its ingest exists.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Checking retained results trades cost against reliance risk](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) -- surface parallel (how often to re-check versus rely), but the object is retained derived results and staleness, not commitments that constrain deliberation; leaky/clogged filters are too loose an analogy to help a reader.
- [Reversibility can favor a change by limiting future loss](../../../../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md) -- concerns which losses correction can stop; Bratman's revocability is about reconsideration cost, not loss after correction.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../theory/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) -- real-options timing of entrenchment; productive deferral already carries the shared axis more directly.
- [Lightweight search control allocates further search without licensing adoption](../../../../theory/lightweight-search-control-does-not-license-adoption.md) -- filter override does allocate deliberation, but the note's adoption/allocation authority split is not what the paper addresses; would read as keyword association.
- [Pindyck, irreversibility under uncertainty](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md) -- irreversible investment and option value; Bratman's plans are revocable, so the shared axis is thin.
- [Provably Bounded-Optimal Agents](../../../../sources/provably-bounded-optimal-agents.ingest.md) -- bounded optimality could frame the paper's "no ideal architecture" argument, but Russell-Wefald already covers the metareasoning comparison more directly.
- [Reusable commitment support across kinds of knowledge work](../../../../reference/proposals/reusable-commitment-support-across-kinds-of-knowledge-work.md) -- matched only on "reconsideration"; concerns Commonplace investment strategy.
- [Herbert Simon, Architecture of Complexity](../../../../sources/herbert-simon-architecture-of-complexity.ingest.md) -- the paper cites Simon (1957) on bounded rationality, not near-decomposability; different Simon work.
- `kb/work/cognitive-architecture-transfer-scan/` and `kb/work/learning-method-name/` -- topically closest (PRS, deliberative learning) but excluded destinations under the sources contract.

## Index Membership

- [Goal prioritization](../../../../tags/goal-prioritization-README.md) -- the head hand-links sources; once the ingest exists it fits "Allocating effort under uncertainty" as a classical account of when reconsideration is worth deliberation cost and of deferring means within partial plans.

## Synthesis Opportunities

The on-balance note, productive deferral and this source jointly suggest a claim not yet captured: a reconsideration policy for retained commitments can only be judged across cases, because any trigger tuned to avoid wasted reconsideration raises the rate of missed worthwhile reconsideration (Bratman's caution/boldness trade-off). Commonplace's review triggers and re-ingest triggers face the same trade-off. Do not write it from this report.

## Maintenance Observations

- The tracked ingest for this snapshot does not yet exist; every candidate here targets that future ingest. The snapshot's PDF extraction loses ligatures ("lter", "ecient") and Tables 1–2 are flattened; quotes for a later Quotes section must be copied with those exact byte forms.

## Flags

- Source carries several independent assertions (filtering architecture, stability/revocability, partiality, caution/boldness taxonomy) across decision, deferral and commitment topics; this is a single paper, so no split, but an ingest should keep these assertions separate when mapping them to KB notes.
