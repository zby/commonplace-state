---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/minton-utility-of-ebl-aaai88.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Quantitative Results Concerning the Utility of Explanation-Based Learning

**Source:** Quantitative Results Concerning the Utility of Explanation-Based Learning — local snapshot `kb/sources/.snapshots/minton-utility-of-ebl-aaai88.md` (not linked: snapshots are Git-ignored and no paired ingest exists yet); original at <https://cdn.aaai.org/AAAI/1988/AAAI88-100.pdf>

The target is an immutable snapshot. No tracked `minton-utility-of-ebl-aaai88.ingest.md` exists yet, so every outbound candidate below is a recommendation for that future ingest's `## Connections Found`, not for the snapshot. Source claims used for judging candidates: (1) learned control knowledge has a hidden match cost paid every time applicability is tested, so EBL can slow problem solving (the utility problem); (2) faster hardware or indexing cannot remove it because learned descriptions are unbounded and matching is NP-complete; (3) PRODIGY scores each rule by `Utility = AvrSavings x ApplicFreq - AvrMatchCost`, admits rules on a training estimate, then validates empirically and discards negative-utility rules; (4) only 19/328, 30/588 and 37/946 analysed examples yielded rules that survived validation; dropping validation made blocksworld performance about 65% poorer; dropping compression stages 2-3 made learning slightly worse than no learning; (5) learned and hand-coded STRIPS rules explored similar node counts, but learned rules cost more per node, while learned scheduling rules were cheaper but less general; (6) learned rules were correct by construction, but the hand-coded rules contained errors.

## Discovery Trace

**Setup reads:**
- `kb/sources/COLLECTION.md` outbound section: destinations theory, reference, agent-memory-systems, agentic-systems, tags, other sources and external; excluded `kb/work/` and `kb/instructions/`. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` and `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). The snapshot itself never authors links; the ingest is the authored surface.
- External prospecting skipped: no external target was supplied or loaded. The future ingest's `derived-from` edge to `https://cdn.aaai.org/AAAI/1988/AAAI88-100.pdf` is the only external edge already known.

**Topic indexes:**
- `kb/tags/learning-theory-README.md` read; it declares `complete: true`, so the by-tag rg for learning-theory was skipped. Its start list surfaced [Learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) and [Constraining and extraction can trade generality for reliability, speed, or cost](../../../../theory/constraining-and-extraction-both-trade-generality-for-reliability.md).
- `kb/tags/continual-learning-README.md` and `kb/tags/agent-memory-README.md` inclusion conditions read for Index Membership only.

**Titles listing (theory, 442 titles):**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'`, filtered with `rg -i 'learn|memory|accumul|retriev|skill|prun|forget|cost|load|growth|bloat|consolidat|compil|compress|utility|speed|evaluat|retire|decay|library|index|always-loaded|instruction|rule'`.
- Flagged and resolved with `rg -l -F -x '# <title>' kb/theory/`: Promote Only When Future Value Exceeds Maintenance Cost; Cheap adoption and weak retirement accumulate cost; Constraining and extraction can trade generality...; Learning is not only about generality; Raw accumulation does not create usable memory; Retire, Redact, Supersede, And Relax Memory; Improvements can accumulate without compounding; Evaluate Memory By Effects, Not By Existence; Instruction specificity should match loading frequency; Cost-sensitive formalisms for tentative theory search; LLM recompute cost shifts the store-vs-recompute balance; Choosing what to learn requires both validity and learning-value gates; Factory-learning mechanisms should be compared on the same causal job; Continual learning requires governing behaviour-changing writes; Current-task fit alone does not warrant costly structural entrenchment; Weight-resident methodologies provide context-efficient behavioral compression.
- Descriptions of all sixteen read; openings of seven read in full (promote-only, cheap-adoption, learning-is-not-only-about-generality, choosing-what-to-learn, llm-recompute, cost-sensitive-formalisms, instruction-specificity).

**Description listing (sources):**
- `rg '^description:' kb/sources --glob '*.ingest.md' | rg -i 'skill librar|skill accum|memory growth|bloat|retriev.*cost|negative transfer|degrad.*memory|too many|library grows|curat|prun|forget'` -- flagged [Novel Memory Forgetting Techniques](../../../../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md) (bounded memory growth); others (geometry of forgetting, price of meaning, DFA-MoE) concern embedding interference or weight forgetting, not cost of applying retained rules.

**Body search:**
- `rg -l -i 'minton|utility problem|explanation-based|PRODIGY|expensive chunks|Tambe' kb --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/state/**'` -- hits: [Chunking in Soar ingest](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md), both EBG ingests ([2026-09-08](../../../../sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md), [original](../../../../sources/explanation-based-generalization-unifying-view.ingest.md)), introspective-multistrategy-learning ingest, quote-verification-migration report. None mention Minton, PRODIGY or the utility problem; the hits are on "explanation-based". The KB has no existing treatment of the utility problem.
- `rg -n -i 'utility problem|match cost|swamp|slow(s|ed)? (down )?(problem solving|retrieval)|skill library (growth|bloat)|retrieval cost grows|prun' kb/theory kb/agentic-systems kb/agent-memory-systems kb/sources kb/reference` -- no match-cost or utility-problem treatment; hits were Swamp (a system name), ai-research-os-workshop's unbounded first-disclosure index (a load-cost analogue, kept as maintenance-free context only), and unrelated "prune" uses.
- `rg -l -i 'utility score|usage (count|statistic)|success rate.*(retire|prune|evict)|(retire|prune|evict).*(low|negative)[- ](utility|value)|helpful.*harmful count|helpful_count|harmful' kb/agent-memory-systems kb/agentic-systems` -- surfaced ACE, cass-memory, and [trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md); follow-up `rg -n -i 'helpful|harmful|utility|prun'` on those files confirmed counter-based helpful/harmful scoring with no applicability-cost term.
- `rg -n -i 'search control|macro-operator|hand-coded rules|hand-written rules|cost of (checking|testing) whether|applicab\w+ (test|check)|per-session cost|every session' kb/theory` -- surfaced [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) and the always-loaded-context cluster (kb-goals, scenario-decomposition, skills-derive-from-methodology).
- `rg -l -i 'soar|chunking' kb/theory` -- only working-memory "chunking" and a loadability mention; no theory note treats Soar chunk cost.
- `rg -l -i 'skill library|skill bloat|too many skills|skill count' kb/agentic-systems` -- only the memory-systems table; no system analysis treats skill-library growth cost.

**Candidate evaluations:**
- Kept (theory): promote-only-when-value-exceeds-cost, choosing-what-to-learn, evaluate-memory-by-effects, learning-is-not-only-about-generality, constraining-and-extraction, failure-explanation-changes-later-branch-decisions, instruction-specificity-should-match-loading-frequency, llm-recompute-cost, cheap-adoption-and-weak-retirement.
- Kept (sources): chunking-in-soar ingest, EBG 2026-09-08 ingest.
- Kept (agent-memory-systems): trace-learning-techniques-in-related-systems.
- Rejected: see Rejected Candidates.

**Link following:**
- From the chunking-in-soar ingest: its Connections Found links [learning inside a fixed decomposition](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), [continual learning requires governing behaviour-changing writes](../../../../theory/continual-learning-requires-governing-behaviour-changing-writes.md) and the EBG ingest. The EBG link confirmed the 2026-09-08 ingest as the richer operationality-focused anchor.
- From the EBG 2026-09-08 ingest: links to [learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) as support for "making an entailed consequence usable" -- the same note Minton bounds from the cost side.
- From promote-only: links the [codification](../../../../theory/definitions/codification.md) gradient; not pursued because PRODIGY's rules are symbolic throughout, with no natural-language-to-symbolic crossing.
- From cheap-adoption: links [maintenance capacity must match harmful-artifact inflow](../../../../theory/maintenance-capacity-must-match-harmful-artifact-inflow.md); rejected as a separate candidate because PRODIGY's rules are not harmful in that sense, only net-costly.
- From the failure-explanation note: its neighbours (lightweight search control, search-controller testing) are about allocating exploration, not the cost of consulting retained control knowledge; not kept.

### Candidate origins

- kb/theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md — titles
- kb/theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md — titles
- kb/theory/agent-memory-requirements/evaluate-memory-by-effects.md — titles
- kb/theory/learning-is-not-only-about-generality.md — curated-head, titles, link-following
- kb/theory/constraining-and-extraction-both-trade-generality-for-reliability.md — curated-head, titles
- kb/theory/failure-explanation-changes-later-branch-decisions.md — body-search
- kb/theory/instruction-specificity-should-match-loading-frequency.md — titles
- kb/theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md — titles
- kb/theory/cheap-adoption-and-weak-retirement-accumulate-cost.md — titles
- kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md — body-search
- kb/sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md — body-search, link-following
- kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md — body-search

## Connections Found

All edges are proposed for the future `kb/sources/minton-utility-of-ebl-aaai88.ingest.md`.

- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) -- **is-evidence-for**: PRODIGY operationalizes the promotion rule as `AvrSavings x ApplicFreq - AvrMatchCost` and measures it; the cost it prices is per-use applicability testing, a cost the note's maintenance-centred ledger does not name.
- [Choosing what to learn requires both validity and learning-value gates](../../../../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) -- **is-evidence-for**: PRODIGY's rules are correct by construction (validity is guaranteed), yet only 19 of 328 blocksworld examples yield rules that pass utility validation; a separate value gate is the dominant filter.
- [Evaluate Memory By Effects, Not By Existence](../../../../theory/agent-memory-requirements/evaluate-memory-by-effects.md) -- **is-evidence-for**: rules estimated useful at learning time (69) mostly failed measured validation (19 survived), and skipping empirical validation cost about 65% in blocksworld; estimated value is not observed effect.
- [Learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) -- **is-evidence-for**: EBL's stated purpose is to re-express an already-defined concept more efficiently, and Minton shows that this speed/cost learning can be negative; the STRIPS result separates coverage (node counts similar) from cost (per-node time higher for learned rules).
- [Constraining and extraction can trade generality for reliability, speed, or cost](../../../../theory/constraining-and-extraction-both-trade-generality-for-reliability.md) -- **compares-with** on the axis of generality versus per-use cost of a use-shaped artifact: compression reduced match cost, and in the scheduling domain learned rules were cheaper to evaluate but less general than hand-coded rules.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) -- **compares-with** on the axis of what makes retained failure explanation operative: PRODIGY's FAILS target concept is the classical case of explanations compiled into rejection rules, and Minton adds that changing later branch decisions is necessary but not sufficient for improvement, because the check itself costs.
- [Instruction specificity should match loading frequency](../../../../theory/instruction-specificity-should-match-loading-frequency.md) -- **compares-with** on the axis of applicability frequency versus per-consultation cost: an always-loaded instruction pays attention cost every session as a PRODIGY control rule pays match cost every decision cycle, and both earn their place only when applicability frequency times savings exceeds that cost.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) -- **compares-with** on the store-versus-recompute ledger: a learned control rule is a stored derivation whose retrieval/match term can exceed the search it saves; Minton's argument that indexing cannot remove this term bounds how far cheap retrieval rescues materialization.
- [Cheap adoption and weak retirement accumulate cost](../../../../theory/cheap-adoption-and-weak-retirement-accumulate-cost.md) -- **compares-with** on the axis of whether retirement is operative: PRODIGY gives every admitted rule a measured retirement path, and removing that path degraded performance; the comparison is bounded because PRODIGY's cost is match time, not dependants or migration.
- [Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) -- **compares-with** on the axis of whether learned control knowledge is cost-evaluated: Soar installs every chunk, and Minton cites Tambe and Newell's "Some Chunks are Expensive" as Soar evidence of the utility problem; PRODIGY is the cost-sensitive contrast.
- [Explanation-based generalization: a unifying view (2026-09-08)](../../../../sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md) -- **compares-with** on the operationality criterion: Minton adopts Mitchell et al.'s EBL specification but argues that a per-description operationality test ignores cumulative match cost and the benefit side, which the EBG ingest leaves untreated.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with** on artifact scoring: ACE and cass-memory score retained bullets by helpful/harmful counters, whereas PRODIGY's utility includes an explicit cost-of-consulting term and applicability frequency; the comparison exposes a missing axis in those systems.

## Bidirectional Candidates

- [Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) <-> source -- **compares-with**: the Soar ingest's limitations section would gain the utility-problem boundary: transfer evidence there does not show net speedup once chunk match cost is counted.
- [Explanation-based generalization: a unifying view (2026-09-08)](../../../../sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md) <-> source -- **compares-with**: the EBG ingest notes that its worked examples establish no comparative search-cost evidence; Minton's paper is the measured follow-up on exactly that gap.

## Reverse-edge Candidates

Under `kb/theory/COLLECTION.md`, theory notes may link a tracked ingest with `evidenced-by`, and the phrase must say whether the evidence corroborates or only qualifies the claim. These edges become possible only after the ingest exists.

- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) → source -- **evidenced-by**: qualifies; PRODIGY's ablation tested "admit every estimated-useful rule" and found it 65% worse, and adds per-use applicability cost to the promotion ledger. Recorded independently of the note's construction.
- [Choosing what to learn requires both validity and learning-value gates](../../../../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) → source -- **evidenced-by**: corroborates the two-gate split with a case where validity is guaranteed and the value gate still removes most candidates; independent of how the note was built (its case is Self-Training-LLM).
- [Learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) → source -- **evidenced-by**: qualifies; the speed/cost axis has a sign, and learning aimed at speed can make the system slower.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) -- PRODIGY's rules are already structured, scoped and validated; the note's ingress-work mechanism is not what Minton tests.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) -- PRODIGY has only one lifecycle operation (discard on negative utility); the promote-only and cheap-adoption edges carry this more precisely.
- [Improvements can accumulate without compounding](../../../../theory/improvements-can-accumulate-without-compounding.md) -- the paper reports no later-episode counterfactual on reinvested savings; keyword overlap on accumulation only.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- prices search under revisable theories; PRODIGY's control rules are not tentative project theories, and the match-cost budget is not one of the note's axes in a way the paper informs.
- [Factory-learning mechanisms should be compared on the same causal job](../../../../theory/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) -- the PRODIGY vs macro-operator "solution quality versus search time" confound is a comparison-method lesson, but the note concerns factory-level retention, not task-solver learning.
- [Continual learning requires governing behaviour-changing writes](../../../../theory/continual-learning-requires-governing-behaviour-changing-writes.md) -- PRODIGY governs writes by measured utility, but the note's authorization and coordination concerns are absent; weaker than the promote-only and two-gate edges.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../theory/weight-resident-methodologies-compress-behavior-in-context.md) -- context-cost topic only; no shared mechanism.
- [Skill discovery re-fires in every sub-agent context](../../../../theory/skill-discovery-re-fires-in-every-sub-agent-context.md) -- names a consultation cost of skills, but the instruction-specificity edge already carries the applicability-cost analogy at the right level.
- [Novel Memory Forgetting Techniques](../../../../sources/novel-memory-forgetting-techniques-autonomous-ai-agents.ingest.md) -- relevance-scored budgeted forgetting; no cost-of-applying term, so the trace-learning comparison is the better agent-memory edge.
- [Explanation-based generalization: a unifying view (original ingest)](../../../../sources/explanation-based-generalization-unifying-view.ingest.md) -- duplicate observation of the same paper; link the 2026-09-08 ingest, which foregrounds operationalization.

## Index Membership

- [learning-theory tag](../../../../tags/learning-theory-README.md) -- the future ingest may carry `tags: [learning-theory]`: it substantively treats when retained learned knowledge increases or decreases capacity. Source tags do not affect the complete head's member listing.
- [continual-learning tag](../../../../tags/continual-learning-README.md) -- plausible but check: PRODIGY retains learned symbolic rules outside weights and governs them by measured utility, which meets "retained changes ... how those changes are governed"; the tagger should confirm that a 1988 non-LLM learner fits the head's intended scope.

## Synthesis Opportunities

Promote-only-when-value-exceeds-cost, instruction-specificity-should-match-loading-frequency, llm-recompute-cost and the trace-learning comparison together imply a claim the KB does not state: retained behaviour-shaping knowledge carries a per-consultation cost proportional to how often its applicability is checked, independent of maintenance cost, so a retention policy needs applicability frequency and consultation cost as well as benefit. Minton's utility formula is the oldest explicit statement; the KB's current ledgers price maintenance, review and context but not the recurring cost of deciding whether each retained item applies.

## Maintenance Observations

- The KB has no artifact naming the utility problem (net-negative learned knowledge through consultation cost), although at least four theory notes and one agent-memory comparison rely on adjacent cost ledgers. This is a repeated unnamed mechanism; see Synthesis Opportunities.
- Two tracked ingests of Mitchell, Keller and Kedar-Cabelli's EBG paper exist with different snapshot checksums. The collection contract allows this, but a reader choosing a link target has no stated preference between them.

## Flags

- No tracked ingest exists for this snapshot; all outbound candidates wait on `cp-skill-ingest` creating `kb/sources/minton-utility-of-ebl-aaai88.ingest.md`.
- Snapshot is OCR text with errors; any retained quotes must be checked character by character against the snapshot.
- Scope caution for every theory edge: the evidence is three symbolic planning domains with hand-written architecture axioms; Minton himself warns there is no "average domain". Edges should claim mechanism and bound, not prevalence for LLM agents.
