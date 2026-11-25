---
description: "Pre-ingest discovery for the textbook's cone comparison and Pareto minimality excerpts, applied to the scope of KB routing judgments."
type: types/connect-report.md
source: kb/sources/.snapshots/boyd-vandenberghe-convex-optimization.md
source_has_frontmatter: true
date: "2026-11-24"
depth: standard
---

# Connection Report: Convex Optimization

**Source:** [Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf), Boyd and Vandenberghe, §§2.4.1 and 4.7.3 only, as captured in `kb/sources/.snapshots/boyd-vandenberghe-convex-optimization.md`. The local snapshot is identified by path rather than linked because validation warns on links to ignored snapshots.

**Occasion:** Which comparisons between routing changes can a cone settle and when must the choice remain open?

## Discovery Trace

**Topic indexes:** Read the `README.md` landings of `theory`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`. The snapshot has no tags. In the follow-up pass, the tags landing led to the evaluation and robust-comparison heads: the latter names the necessary-preference note, but requires a substantive comparison across a family of measures. A fixed cone alone does not meet that boundary. No outbound label in the sources contract targets tag heads.

**Title and description scans:** Ran `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'` for each of those six destinations, filtering the resulting titles with `cone|pareto|dominanc|trade.off|routing|scalariz|incomparab|multicriter|criterion|judgment|electre|optimization|partial order|balance` (case-insensitive). Scanned `rg '^description:' kb/<destination>/ --glob '*.md'` with `rg -i 'pareto|cone |outrank|incomparab|trade.off|dominanc|scalariz|robust comparison|on.balance|model routing|routing policy|selection criteria|evaluation gate'`. The on-balance note surfaced in titles and descriptions; necessary preference and ordinal regression surfaced in descriptions. Yu and ELECTRE surfaced in titles; Yu also surfaced in descriptions. Task-specific model routing surfaced on both surfaces but addresses a different decision.

**Body searches:** Ran the following case-insensitive expressions over `kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}` with `--glob '*.md'`, then inspected matching lines (`full.md` omitted from the line-level pass). `rg` supplied no scores.

- `Pareto|proper cone|cone.convex|cone.induced|nondominat|outrank|scalariz|ELECTRE|incomparab` found the cone lead in the on-balance note, the Yu/ELECTRE ingests, necessary preference, and a concrete accuracy–context-length frontier in the historical Meta-Harness review. The frontier illustrates screening, but does not help decide what trade-offs to admit in this routing case.
- `routing (changes?|polic(y|ies))|on.balance judgment|robust comparison|admissible (measures|criteria)|dominance` brought up ordinal regression and Interval SMART/SWING. Kept ordinal regression for how reference judgments change the comparisons a family settles; did not add a second link about eliciting additive trade-offs. In reference, the authority-grades proposal's dominance hit concerns a different question. In agentic systems, Swamp's routing-policy hit concerns how workflows are dispatched, not how rival routing policies are ordered.
- `quotation routing|ordinary ingestion|cost.quality|quality.cost|accuracy.{0,40}(cost|latency)|cost.{0,40}accuracy` confirmed the shared routing example in theory and the Yu and ELECTRE ingests. Generic parser and retrieval benchmarks do not carry the comparison rule for this occasion. `rg -n 'boyd-vandenberghe-convex-optimization|bv_cvxbook\.pdf'` over the same destinations found no existing visible use or paired ingest.

**Link following:** Followed the on-balance note to ADR 076 and necessary preference, and necessary preference to its requirements note and Greco ingest. The ADR documents the rival routing remedies and the reason for the chosen design, not measured routing results; the requirements note separates design checks from outcome tests. Yu and ELECTRE link back to the same routing and necessary-preference notes, confirming that the strongest matches address this occasion rather than merely sharing terms. No stronger reference, system-review, or tag destination emerged. Excluded `work` and `instructions` per the sources contract. The original PDF URL is already in the snapshot as provenance; no external prospecting.

### Candidate origins

- kb/theory/on-balance-judgment-with-an-llm.md — titles, descriptions, body-search, link-following
- kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md — descriptions, body-search, curated-head, link-following
- kb/sources/yu-cone-convexity-and-nondominated-solutions.ingest.md — titles, descriptions, body-search
- kb/sources/electre-methods.ingest.md — titles, body-search
- kb/sources/greco-ordinal-regression-revisited.ingest.md — descriptions, body-search, link-following

## Connections Found

Candidates for the eventual paired ingest, not for the snapshot itself.

- [On-balance judgment with an LLM](../../../../../theory/on-balance-judgment-with-an-llm.md) — **is-evidence-for**: §§2.4.1 and 4.7.3 give the mathematical basis and limit of the note's cone lead. With costs oriented so lower is better, A is no worse than B if the outcome difference `B − A` belongs to the declared cone. If neither direction belongs, the outcome vectors are incomparable under that rule. This supports the comparison, not the proposed choice of offsets or a forecast that routing improves.
- [Necessary preference can guide improvement without a global measure](../../../../../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) — **compares-with**: compare what leaves a pair open. One fixed cone can leave a known difference unordered. Necessary preference can remain open because admitted measures favor opposite directions or because outcome evidence is missing. Agreement between these rules needs a demonstrated correspondence, not shared Pareto vocabulary.
- [Yu: Cone convexity, cone extreme points, and nondominated solutions](../../../../../sources/yu-cone-convexity-and-nondominated-solutions.ingest.md) — **compares-with**: both distinguish screening from choosing. The textbook gives a test for minimal outcomes under a proper cone; Yu's abstract announces methods for finding nondominated solutions, without exposing the assumptions or proofs. Use the textbook to check what nondominance means, not to infer the scope of Yu's algorithms.
- [ELECTRE Methods](../../../../../sources/electre-methods.ingest.md) — **compares-with**: compare what blocks a direction. A proper cone tests a difference and gives a transitive partial order on outcome vectors. ELECTRE Iv needs enough criterion support and no veto; a veto blocks one direction without establishing the reverse, and the outranking relation need not be transitive. Neither is the same as excluding a remedy before comparison.
- [Ordinal Regression Revisited](../../../../../sources/greco-ordinal-regression-revisited.ingest.md) — **compares-with**: the textbook takes a cone as given; ordinal regression elicits reference comparisons that narrow a family of additive value functions. This gives a different way to justify further comparisons when the routing outcomes are known but their trade-offs are not fixed.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [On-balance judgment with an LLM](../../../../../theory/on-balance-judgment-with-an-llm.md) → future paired ingest `kb/sources/boyd-vandenberghe-convex-optimization.ingest.md` — **evidenced-by**: the theory contract allows a tracked source to qualify or bound an assertion. Cite the textbook where the cone comparison is introduced, after the ingest exists and the supporting passage can be checked under the source-grounding rules. The citation would bound the mathematical claim, not corroborate selector performance. No durable reverse link to the snapshot is allowed.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [ADR 076: Source-claim grounding is a promoted skill](../../../../../reference/adr/076-source-claim-grounding-is-a-promoted-skill.md) — useful via the on-balance note for reconstructing the alternatives, but a direct edge would not add a comparison rule or evidence of subsequent routing outcomes.
- [Meta-Harness](../../../../../agent-memory-systems/reviews/meta-harness.md) — its classification frontier shows one concrete Pareto screen, not how to compare routing changes when ordinary ingestion and quotation routing pull in opposite directions.
- [Swamp](../../../../../agentic-systems/reviews/swamp.md) — describes how a routing policy is expressed and applied, not how to compare two policies with mixed outcomes.
- [The Best Model Routing is Task Specific](../../../../../sources/the-best-model-routing-is-task-specific-2077537847951945742.ingest.md) — selects an execution path subject to a quality bar; it does not compare changes to Commonplace's skill-routing policy under unresolved trade-offs.

## Index Membership

None

## Synthesis Opportunities

The on-balance note and the Yu and ELECTRE ingests suggest comparing the same routing remedies and outcomes under three separate commitments: an eligibility requirement, a cone order, and a directional veto. A hard ingestion requirement can exclude a remedy; a cone can leave two eligible remedies incomparable; a veto can block one comparison without reversing it. The necessary-preference note adds a diagnostic: better measurement can resolve missing outcome evidence, but cannot settle a trade-off that the stated commitments still leave open. This is a candidate comparison to investigate, not a proposed routing rule.

## Maintenance Observations

None

## Flags

- Preserve the distinction between **minimal** and **minimum**: §4.7.3 retains feasible outcomes with no distinct outcome below them, not a winner that is at least as good as every alternative. Two distinct remedies can have the same outcome vector; that is not incomparability. A nonzero difference on the cone boundary can establish dominance even though it does not satisfy the textbook's interior-based strict inequality.
- The excerpt does not select criteria, define permissible offsets, or measure routing effects. For mixed outcomes, neither direction may pass under the declared cone; choosing among survivors then requires grounds outside that comparison. Some captured glyphs are damaged; check any future formula quotation against a readable rendering before relying on the transcription.
