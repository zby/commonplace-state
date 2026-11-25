---
description: "Candidate connections for the Convex Optimization ingest: cone comparisons, feasible-set screening, and alternatives to a forced routing verdict."
type: types/connect-report.md
source: "kb/sources/boyd-vandenberghe-convex-optimization.ingest.md"
source_has_frontmatter: true
date: "2026-11-24"
depth: standard
---

# Connection Report: Ingest: Convex Optimization

**Source:** [Ingest: Convex Optimization](../../../../../sources/boyd-vandenberghe-convex-optimization.ingest.md)

## Discovery Trace

- **Curated heads.** Read `kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources}/README.md`. The source has no tags. The tags landing led to `robust-comparison-README.md`, which exposed the necessary-preference note again and suggested the objection and reversibility notes. The head is specific to agreement across compatible measures; it is not a general index of partial orders.
- **Titles and descriptions.** In each of those six collections, ran `rg -N --no-filename -m1 '^# (.*)' -r '$1' "kb/$d/" --glob '*.md' --glob '!*.brief.md'`; screened the listings with `pareto|dominance|outrank|incomparab|necessary preference|robust.comparison|on.balance|objection|reversib|trade.off|prioriti|routing|convex|electre|nondominat|admissib|eligible|regression|multi.criteria|ranking|threshold|goal conflict` (case-insensitive). Scanned respectively 452, 262, 175, 156, 35 and 632 titles. Ran `rg '^description:' "kb/$d/" --glob "$g"` with `*.ingest.md` for sources and `*.md` elsewhere; screened with `rg -i 'pareto|dominance|outrank|incomparab|necessary preference|robust.comparison|on.balance|reversib|trade.off|routing|convex|electre|nondominat|admissib|multi.criteria|ranking|goal conflict'`. These passes recovered the two theory notes already linked in the ingest and exposed Yu, ELECTRE and Greco as source peers. Reference title and description hits called “routing” mostly concern where content belongs, not how to compare routing remedies.
- **Body searches.** Across all six collections, ran `rg -n -i 'cone-induced|proper cone|pareto (minimal|dominance|front|win)|outrank|nondominat|necessary preference|incomparab'` and `rg -il 'quotation routing|ordinary ingestion|separate.skill|noncompensatory|veto threshold|hard eligibility|boyd-vandenberghe-convex-optimization'` over Markdown. Theory results included local selection and the maintainability brainstorm; the latter already proposes a frontier but supplies no worked KB comparison, so it is less useful than the implemented Meta-Harness example. The legacy agent-memory search found Meta-Harness's accuracy/context-length frontier; Origin's “outranking” is priority of a status file over recall, not an outcome comparison. The reference and current agentic-system passes found no candidate from these queries. A follow-up `rg -n -i 'pareto|multi[- ]objective|frontier' kb/agentic-systems/ --glob '*.md'` mostly returned other senses of “frontier,” such as ranked proof work and context selection. `rg -n -i 'cone|Pareto|trade.?off' kb/theory/definitions/ --glob '*.md'` yielded no definition for the comparison terms. Source hits also included online convex programming and ConvexBench, neither of which studies this screening rule. Searches supplied no scores.
- **Link following.** From *On-balance judgment*, followed ADR 076 and *Defining Improvement for Open-Ended Work*: they establish the recorded reason for preferring one advertised route, not comparative routing outcomes or cone lineage. From *Necessary preference*, followed Greco and *Selection-based learning needs only a local comparison*: Greco is the primary source for agreement across fitted value functions; the selection note already routes readers to the relevant formalisms. Yu and ELECTRE both lead back to the routing note, independently identifying the same place for a worked comparison. A filename search (`rg -l 'boyd-vandenberghe-convex-optimization\.ingest\.md' kb --glob '*.md' --glob '!work/**'`) found no existing inbound artifact link.
- **External.** The Stanford-hosted textbook PDF is already cited in the ingest. Checked the matching local capture against the ingest hash and read §§2.4.1 and 4.7.3. No new external candidate and no web prospecting.

### Candidate origins

- kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md — known, curated-head, titles, descriptions, body-search, link-following
- kb/sources/yu-cone-convexity-and-nondominated-solutions.ingest.md — titles, descriptions, body-search
- kb/sources/electre-methods.ingest.md — titles, descriptions, body-search
- kb/sources/greco-ordinal-regression-revisited.ingest.md — descriptions, link-following
- kb/agent-memory-systems/reviews/meta-harness.md — body-search
- kb/theory/on-balance-judgment-with-an-llm.md — known, titles, descriptions, body-search, link-following

## Connections Found

- [Necessary preference can guide improvement without a global measure](../../../../../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) — **compares-with**: Existing inline connection; keep the distinction between testing a known cost difference against one declared cone and testing whether all compatible measures agree. Both can leave a pair open after outcomes are known, but equal scores under all compatible measures need not establish identical outcomes. No claim that the rules agree in general.
- [Yu: Cone convexity, cone extreme points, and nondominated solutions](../../../../../sources/yu-cone-convexity-and-nondominated-solutions.ingest.md) — **compares-with**: Compare what nondominance establishes about the surviving feasible set. Boyd and Vandenberghe supply a precise order and minimality test; Yu's abstract motivates the screen and reports methods for finding survivors, but does not establish their hypotheses or applicability to KB routing.
- [ELECTRE Methods](../../../../../sources/electre-methods.ingest.md) — **compares-with**: Compare why neither direction passes under a fixed rule. A proper cone orders distinct cost vectors only if one difference lies in the cone; ELECTRE can block a direction for insufficient support or a veto. Both directions can pass in ELECTRE without identical outcomes, and the raw relation need not be transitive.
- [Greco, Mousseau and Słowiński: Ordinal Regression Revisited](../../../../../sources/greco-ordinal-regression-revisited.ingest.md) — **compares-with**: Compare what can make an unresolved pair decidable after outcomes are known. In UTAGMS, a consistent judgment on reference alternatives can narrow the compatible functions. A cone comparison requires a change to the declared rule if the known difference remains outside the cone in both directions. UTAGMS weak dominance without reference judgments is a useful baseline, not a general equivalence.
- [Meta-Harness](../../../../../agent-memory-systems/reviews/meta-harness.md) — **compares-with**: The historical review gives an implemented example of retaining alternatives on two measured criteria (accuracy and context length). Use it to see what a frontier records in an agent workflow, not to infer that the system uses a generalized cone or that screening predicts better Commonplace routing.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [On-balance judgment with an LLM](../../../../../theory/on-balance-judgment-with-an-llm.md) → source — **evidenced-by**: At the existing dominance-cones lead, cite §§2.4.1 and 4.7.3 as the mathematical basis and boundary of the proposed comparison, not as corroboration of routing gains or proof that Commonplace should admit a particular offset. The ingest already points to this note; the candidate is the missing citation at the claim. For a future source-dependent use, retain the supporting passages first or mark the citation `(snapshot required)`; the current Quotes section is empty.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [ADR 076: Source-claim grounding is a promoted skill](../../../../../reference/adr/076-source-claim-grounding-is-a-promoted-skill.md) — Relevant historical case, already reachable via the routing note. It records why the pointer was rejected; it neither uses cone screening nor measures the comparative outcomes the screen would need.
- [Selection-based learning needs only a local comparison](../../../../../theory/selection-based-learning-needs-only-a-local-comparison.md) — Establishes why a scalar ranking is unnecessary, not which partial order to use. Its existing links to the routing and necessary-preference notes already give the reader a more direct route to the specific comparison.
- [An objection can show where to split a comparison](../../../../../theory/an-objection-can-show-where-to-split-a-comparison.md) and [Reversibility can favor a change by limiting future loss](../../../../../theory/reversibility-can-favor-a-change-by-limiting-future-loss.md) — Useful when the job is to identify missing effects or bound a trial's downside. Neither supplies the rule for comparing fixed measured vectors or choosing among survivors.

## Index Membership

None. The [robust-comparison head](../../../../../tags/robust-comparison-README.md) concerns agreement across compatible measures. This ingest uses that approach as a contrast; its contribution is screening with one declared cone.

## Synthesis Opportunities

Use the same hypothetical routing outcomes in *On-balance judgment* to distinguish three dispositions with different consequences for later selection: failing a hard requirement excludes a remedy from the feasible set; losing a cone comparison to a feasible rival removes it from the survivors under that rule; an ELECTRE veto blocks only one direction of one comparison and does not alone justify either exclusion. The Boyd, Yu and ELECTRE ingests support those distinctions. Holding outcomes fixed makes clear which changes in verdict come from changed commitments, rather than new measurements. A worked comparison in the existing note would suffice; no separate synthesis artifact is needed.

## Maintenance Observations

None

## Flags

- For the worked comparison, do not treat the textbook's interior-only strict inequality as the dominance screen. A distinct feasible cost vector that is no worse under the nonstrict order suffices, even if the difference lies on the cone boundary. Equal vectors tie on the declared criteria; a set of minimal vectors need not contain a minimum.
- No source here establishes the actual routing outcome vectors or whether ordinary-ingestion reliability should be an eligibility requirement, a loss that no gain can offset, or a loss that some gains can offset. Keep those choices and the missing observations separate.
