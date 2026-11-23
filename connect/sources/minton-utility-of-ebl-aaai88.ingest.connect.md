---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/minton-utility-of-ebl-aaai88.ingest.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: Ingest: Quantitative Results Concerning the Utility of Explanation-Based Learning

**Source:** [Ingest: Quantitative Results Concerning the Utility of Explanation-Based Learning](../../../../sources/minton-utility-of-ebl-aaai88.ingest.md)

## Discovery Trace

**Setup:** Read `kb/sources/COLLECTION.md` outbound section. Prospected destinations: theory, reference, agent-memory-systems, agentic-systems, sources, tags. Excluded: `kb/work/`, `kb/instructions/`. External prospecting skipped (no externally supplied targets). Authorised labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from`/`rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (sparingly).

**Known links (already in the source's Connections Found / Learning Claims):** all 14 targets checked for existence with `test -f` — all resolve: promote-only-when-value-exceeds-cost, choosing-what-to-learn-requires-both-validity-and-learning-value-gates, evaluate-memory-by-effects, learning-is-not-only-about-generality, constraining-and-extraction-both-trade-generality-for-reliability, instruction-specificity-should-match-loading-frequency, failure-explanation-changes-later-branch-decisions, learning-inside-a-fixed-decomposition-inherits-its-mistakes, theory-builder, codification, actionable-methodology, chunking-in-soar ingest, EBG 2026-09-08 ingest, trace-learning-techniques-in-related-systems. Not re-proposed below.

**Curated heads:**
- `kb/tags/learning-theory-README.md` (source tag) — `complete: true`, so by-tag rg skipped. Routing surfaced learning-is-not-only-about-generality and constraining-and-extraction (both already linked) and the agent-memory child area.

**Titles listing:**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md' | rg -i 'cost|retain|retention|promot|memory|forget|prun|loading|context|search|learn|chunk|rule|valid|effect|accumul|materializ|compil|speed|retriev|consult|instruction|always'` — flagged and resolved: Retire, Redact, Supersede, And Relax Memory; Raw accumulation does not create usable memory; Localized retention pays…; Retained theories compared with retained traces…; Knowledge storage does not imply contextual activation; Backtracking keeps lightweight search control provisional; Context efficiency is the central design concern; Checking retained results trades cost against reliance risk; Promotion selects for unreliable activation…; Always-loaded context mechanisms…; Cost-sensitive formalisms for tentative theory search; A retained instruction preserves what testing selected; Improvements can accumulate without compounding; Current-task fit alone…; Weight-resident methodologies…; Explicit retention provides direct targets…. Descriptions read for each via `rg -m1 '^description:'`.

**Body search:**
- `rg -il 'utility problem|PRODIGY|Minton|match cost|explanation-based' kb --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/**'` — only sources: introspective-multistrategy-learning, chunking-in-soar, both EBG ingests, and this source. No theory note names the utility problem (confirms the ingest's claim).
- `rg -n -i 'minton|prodigy|utility problem|explanation-based'` over introspective-multistrategy-learning, EBG (08-31), chunking-in-soar ingests — none cites Minton; Meta-AQUA mentions EBG only as a repair operator (rejected).
- `rg -n -i 'retrieval is cheap|keep everything|cost of consult|consultation cost|per-use cost|applicab\w* (check|test)|always-loaded|context load|forgetting|retire|prune|pruning|harmful counter|helpful.harmful|match(ing)? cost|slow(s|ed)? (the|down)' kb/theory kb/agent-memory-systems kb/agentic-systems kb/reference -l` — broad (60+ files); used only to cross-check the titles pass; reference hits were proposals/ADRs about Commonplace internals, none on retention utility.
- `rg -n -i 'utilit|decay|usage|frequen|cost|harm'` in retire-redact-supersede-relax — cass-memory harmful-feedback weighting and decay; no consultation-cost term. Kept.
- `rg -n -i 'learning|budget|utilit|speed|cost'` in cost-sensitive-formalisms — budgets for search/evaluation/revision, no match-cost of learned control. Rejected (see below).
- `rg -n -i 'slow|negative|cost|savings'` in improvements-can-accumulate-without-compounding — compounding defined via reduced later cost; rejected.
- `rg -n -i 'chunk|soar|EBL|explanation-based' kb/theory` — theory-and-methodology-form-a-two-layer-execution-system mentions Soar chunking/ACT-R compilation as illustration; rejected.
- `rg -n -i 'harmful|helpful|decay|retire|prune|utility'` in ace review and trace-learning survey — survey already covers ACE, ExpeL strength-decay and cass-memory score-based deprecation.
- `rg -n 'Minton|utility' kb/log.md` — led to a-retained-instruction-preserves-what-testing-selected, which links llm-recompute-cost-inverts-the-store-vs-recompute-default. Read that note fully. Kept.
- `rg -m1 '^description'` on opposed-recompute-factors-do-not-decide-documentation-segmentation and indexes-lower-recall — the former is the general cache ledger; rejected as narrower than the recompute note for this source.

**Link following:**
- llm-recompute-cost → checking-retained-results-trades-cost-against-reliance-risk, opposed-recompute-factors, frontloading. Checking-retained-results kept as a weaker comparison candidate.
- retire-redact-supersede-relax → context-efficiency-is-the-central-design-concern (stale memory has a real cost). Rejected as too general.
- trace-learning survey → cass_memory_system review. Rejected as a separate target because the survey link already carries the comparison.

### Candidate origins

- kb/theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md — body-search, link-following
- kb/theory/agent-memory-requirements/retire-redact-supersede-relax.md — titles, body-search
- kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md — titles, link-following
- kb/theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md — known
- kb/theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md — known
- kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md — known, body-search
- kb/sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md — known, body-search
- kb/sources/explanation-based-generalization-unifying-view.ingest.md — body-search

## Connections Found

- [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) -- **compares-with**: shared axis is the total-cost ledger for keeping a derived result versus recomputing it. PRODIGY's control rules are cached consequences of the domain theory; its utility formula adds a measured lookup term (match cost times frequency of checking) to that ledger, and its unfiltered runs show stored derivations losing to recomputation (search without rules). The note's ledger names "retrieval" and "context use" but has no symbolic-system measurement of the retrieval term turning the sign negative.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) -- **is-evidence-for**: PRODIGY's validation stage is an early, ablated instance of use-statistics-driven retirement — 69 rules estimated useful, 19 kept, and skipping retirement cost about 65% in the blocksworld. It bears on the note's claim that lifecycle metadata becomes memory management only when a process acts on it, and adds a retirement trigger (negative net time) the note's list lacks.
- [Checking retained results trades cost against reliance risk](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) -- **compares-with**: both price a recurring cost of a retained result against the work it saves; the note's recurring cost is checking for staleness, Minton's is testing applicability. Following the link shows an agent that "retained results save recurring work" has at least two distinct recurring debits. Weaker candidate; author only if the ingest's Connections section is extended toward the cache-economics cluster.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Promote Only When Future Value Exceeds Maintenance Cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md) → source -- **evidenced-by**: under the theory contract, the context phrase should say the source qualifies the note rather than corroborates it: it adds a per-check consultation cost the maintenance-centred ledger omits. The note's "always-loaded policy only when … high-frequency, and cheap" line is the natural attachment point.
- [Retire, Redact, Supersede, And Relax Memory](../../../../theory/agent-memory-requirements/retire-redact-supersede-relax.md) → source -- **evidenced-by**: bounds/qualifies the note with a measured retirement-by-net-effect case; pairs with the outbound candidate above.
- [Choosing what to learn requires both validity and learning-value gates](../../../../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) → source -- **evidenced-by**: a case where the validity gate is guaranteed (EBL rules correct by construction) and a separate value gate still removes most candidates. The phrase should state whether this tested the two-gate claim or only illustrates it; it was recorded independently of the note's construction.
- [Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) → source -- **compares-with** (sources→sources): axis is admission policy for learned productions; Soar installs every chunk, while PRODIGY admits and retires by utility, and Minton cites expensive Soar chunks as the utility problem. Soar's ingest currently has no forward pointer to this cost-side critique.
- [Explanation-based generalization: a unifying view (2026-09-08)](../../../../sources/explanation-based-generalization-unifying-view-2026-09-08.ingest.md) → source -- **compares-with**: axis is the operationality criterion; Minton argues that criterion ignores cumulative match cost and benefit. The 08-31 ingest ([EBG unifying view](../../../../sources/explanation-based-generalization-unifying-view.ingest.md)) is an equal candidate; see Maintenance Observations on which one is canonical.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Raw accumulation does not create usable memory](../../../../theory/raw-accumulation-does-not-create-usable-memory.md) -- the PRODIGY "keep everything" ablation looks like support, but the note's mechanism is missing ingress (handles, scope, provenance); PRODIGY's failure is match cost on well-formed rules. Linking would blur the two mechanisms.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- maps budgets for search, evaluation and revision of theories; the per-consultation cost of learned control rules is not one of its budgets, and the source is not a formalism.
- [Improvements can accumulate without compounding](../../../../theory/improvements-can-accumulate-without-compounding.md) -- PRODIGY measures per-problem speed-up, not whether earlier rules make later learning cheaper; no compounding test.
- [Context efficiency is the central design concern in agent systems](../../../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- the analogy (match cost vs context cost) is already carried more precisely by the instruction-specificity comparison in the ingest; too general to help traversal.
- [Theory and methodology form a two-layer execution system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md) -- mentions Soar chunking/ACT-R compilation as an illustration only; keyword match.
- [Introspective multistrategy learning](../../../../sources/introspective-multistrategy-learning.ingest.md) -- uses EBG as one repair operator; no cost/utility axis shared.
- [cass-memory review](../../../../agent-memory-systems/reviews/cass_memory_system.md) and [ACE review](../../../../agent-memory-systems/reviews/ace.md) -- score-based deprecation is comparable, but the already-linked trace-learning survey carries that comparison across systems; separate links would duplicate it.
- [Opposed recompute factors do not decide documentation segmentation](../../../../theory/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) -- general cache ledger, but specialised to documentation segmentation; the llm-recompute note is the better entry.
- Reference, agentic-systems destinations -- no artifact on retention utility, rule match cost or learned-control admission found; no candidates.

## Index Membership

- [learning-theory tag head](../../../../tags/learning-theory-README.md) -- the source already carries `tags: [learning-theory]`. Sources are outside the participating collections, so no head entry is required; noted only for discovery.

## Synthesis Opportunities

The source's own Recommended Next Action is corroborated by this pass: [Promote Only When Future Value Exceeds Maintenance Cost](../../../../theory/agent-memory-requirements/promote-only-when-value-exceeds-cost.md), [Instruction specificity should match loading frequency](../../../../theory/instruction-specificity-should-match-loading-frequency.md), [LLM recompute cost shifts the store-vs-recompute balance](../../../../theory/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) and [Checking retained results trades cost against reliance risk](../../../../theory/checking-retained-results-trades-cost-against-reliance-risk.md) each price one recurring debit of a retained item (maintenance, attention per session, retrieval, staleness checks). None names the per-applicability-check consultation cost as a separate term. A theory note "retained knowledge pays a consultation cost each time its applicability is checked" would unify them, with this source as its only measured anchor (symbolic systems; LLM transfer conjectural).

## Maintenance Observations

- Two ingests of the same EBG paper exist: `explanation-based-generalization-unifying-view.ingest.md` (captured 2026-08-31) and `explanation-based-generalization-unifying-view-2026-09-08.ingest.md`. This source links the later one; the Soar ingest links the earlier one. Inbound links to the same paper are split across two observations.
- The KB has no artifact that names the "utility problem" outside this ingest; the term may warrant a vocabulary-collision check (Minton's "utility" vs KB's general value sense), as the ingest's Terminology paragraph already notes.

## Flags

- None
