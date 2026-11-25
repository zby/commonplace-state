---
description: "Pre-ingest discovery for Yu’s abstract on domination structures, nondominated sets, and Pareto optimality."
type: types/connect-report.md
source: kb/sources/.snapshots/yu-cone-convexity-and-nondominated-solutions.md
source_has_frontmatter: true
date: "2026-11-24"
depth: standard
---

# Connection Report: Cone convexity, cone extreme points, and nondominated solutions in decision problems with multiobjectives

**Source:** Yu’s publisher abstract at `kb/sources/.snapshots/yu-cone-convexity-and-nondominated-solutions.md` (local capture; no tracked ingest).

## Discovery Trace

Yu treats nondominance under a specified domination structure as a requirement for a good feasible solution, not a complete choice rule. The abstract identifies Pareto optimality as a special case and announces geometric results and mathematical-programming methods for finding nondominated solutions. For Commonplace, the question is whether a declared comparison can rule out some changes while keeping conflicting gains and losses visible. The capture contains frontmatter but only the abstract, not the definitions, proofs, or worked example.

The sources contract authorizes prospecting in `theory`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`. It gives no formal outbound label for tag heads; those were inspected for navigation and possible membership only. The known DOI was evaluated from the capture; no external prospecting was done. The snapshot has no topic tags. `kb/work/` and `kb/instructions/` were excluded. No matching tracked ingest exists yet; outbound candidates are for that future ingest, not the snapshot.

**Topic indexes and title scan.** Read each destination’s `README.md`. Ran `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/<destination>/ --glob '*.md' --glob '!*.brief.md'` once for each destination. Scanned the generated titles with `pareto|dominance|domination|nondominated|robust|trade.off|objective|multi.criteria|commensur|scalar|on.balance|priority|prioritiz|incomparab|admissib|benchmark|decision|evaluat`. This surfaced the on-balance judgment note in theory and the Interval SMART/SWING and hierarchical Choquet ingests in sources. The reference and system landings surfaced no direct candidate. The tags landing led to the robust-comparison head, which points to the necessary-preference note and examples of what to do when a comparison stays open.

**Description listing scan.** Ran `rg '^description:' kb/<destination>/ --glob '*.md'` in each destination, using `--glob '*.ingest.md'` for sources. Filtered on `pareto|nondomin|dominan|trade.off|commensur|scalariz|robust (ordinal|compar|optimi)|compatible (measures|scor|weight)|multiple (objectives|criteria)|multi.(criteria|objective|attribute)|partial order|on.balance|preference model|interval weights`. This surfaced the necessary-preference note and Greco’s ordinal-regression ingest, and confirmed Interval SMART/SWING. Theory hits on context isolation and enforcement strength concern different trade-offs or different objects being ordered. The requirements-aware-systems agenda was too broad: runtime requirements trade-offs do not supply a comparable dominance rule. No kept candidate came from a brief; `rg -in 'pareto|dominan|trade.off|weight' ... --glob '*.brief.md'` found only the unrelated model-weights brief.

**Body search and candidate evaluation.** In each destination ran `rg -in 'BF00932614|P\. L\. Yu|cone convex|pareto|non.?dominated'`, `rg -il 'necessary preference|robust ordinal regression|non.?commensur|multi.?criteri|multi.?objective|scalariz|compatible measures|dominance test'`, and `rg -in 'dominan(ce|tion) (cone|structure)|outranking|trade.?off.*(weight|veto)|meta.harness|sol.pi.efficient'` over Markdown. These are lexical searches with no scores.

- **Theory:** The on-balance note explicitly names dominance cones in its routing example; the necessary-preference note compares whole compatible scoring rules and is not a claim about Yu’s cone geometry. Kept the former as a reverse citation lead and the latter as a comparison. The maintainability-oracle brainstorm already notes that a Pareto profile needs a later decision rule; no separate edge without a specific policy or test to develop.
- **Reference:** No direct hit. An additional query for `((quality|accuracy|capability|reliability).{0,45}(versus|trade.?off|cost|latency)|(cost|latency).{0,45}(versus|trade.?off|quality|accuracy|capability)|frontier over|multi.objective)` found the note-refinement proposal, which specifies a Borda tournament and raises set-valued judging, not a comparison by nondominance. The landing’s source-adoption policy governs whether to adopt any result, not the mathematical comparison itself.
- **Agent memory systems:** The Meta-Harness review gives a concrete accuracy–context-length frontier in text classification. Kept as a bounded example of the Pareto special case, not evidence of Yu’s methods or their benefits. The collection is frozen, so no return edit is proposed.
- **Agentic systems:** The same additional quality/cost query surfaced PageIndex. Its reported accuracy and cost do not define a frontier, and its expansion formula is not a policy for retaining nondominated alternatives. No kept candidate.
- **Tags:** The robust-comparison head tests agreement across a family of compatible measures, not merely the presence of several objectives. Consider it only if the ingest develops that comparison explicitly.
- **Sources:** Kept Greco and Interval SMART/SWING for their different ways of specifying what makes one option dominate when trade-offs are not fully specified. Kept SoL-Pi for a harness case that separates capability eligibility from frontier retention. The Choquet ingest addresses interactions and rank frequencies, which the capture cannot illuminate. GEPA’s instance-wise parent selection addresses which prompts to explore, not the set of nondominated feasible changes under an agreed trade-off rule.

**Link following.** Followed the on-balance note to its recorded routing decision (ADR 076) and to the note on defining improvement. They establish the KB use case and the need to name the alternative, not a source link for the decision itself. Followed necessary preference to Greco’s ingest and to the local-comparison note; the latter bounds evaluation to reachable changes and need not inherit a method for searching a full objective space. The robust-comparison head’s split-comparison example shows how to identify a missing constraint; Yu’s abstract starts once a domination structure can be specified. Followed Meta-Harness to the trace-extraction note, which concerns which observations can be learned from, not frontier selection. Followed SoL-Pi to the context-efficiency note; that note distinguishes per-window feasibility from aggregate expense, so the reported cost reduction does not by itself settle a quality–cost comparison.

### Candidate origins

- https://doi.org/10.1007/BF00932614 — known
- kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md — descriptions, body-search, curated-head, link-following
- kb/sources/greco-ordinal-regression-revisited.ingest.md — descriptions, link-following
- kb/sources/mustajoki-interval-smart-swing.ingest.md — titles, descriptions, body-search
- kb/agent-memory-systems/reviews/meta-harness.md — body-search
- kb/sources/sol-pi-efficient-agent-harness.ingest.md — body-search
- kb/theory/on-balance-judgment-with-an-llm.md — titles, body-search, link-following

## Connections Found

- [Yu’s original paper](https://doi.org/10.1007/BF00932614) — **derived-from**: the future ingest would analyze the publisher abstract for this DOI; the link does not imply the paper body was read.
- [Necessary preference can guide improvement without a global measure](../../../../../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) — **compares-with**: distinguish removing dominated alternatives under a specified objective-space relation from preferring a particular change because no compatible evaluation favors the incumbent and at least one favors the change. Do not assume the two orders coincide without an explicit mapping.
- [Ordinal Regression Revisited](../../../../../sources/greco-ordinal-regression-revisited.ingest.md) — **compares-with**: Yu takes a domination structure over objective outcomes; UTAGMS starts from criterion-wise weak dominance without reference judgments and can order more pairs as consistent examples narrow the compatible scoring rules.
- [Decision Support by Interval SMART/SWING](../../../../../sources/mustajoki-interval-smart-swing.ingest.md) — **compares-with**: instead of taking a domination structure as input, elicit bounded trade-off ratios, then test whether the same pairwise advantage remains strictly positive across the allowed weights. That is a specific model and test, not a claim that Yu uses it.
- [Meta-Harness](../../../../../agent-memory-systems/reviews/meta-harness.md) — **compares-with**: the text-classification frontier makes the Pareto special case concrete for an agent maintainer by keeping accuracy and context length separate when comparing tested harnesses. It neither chooses a single best trade-off nor demonstrates Yu’s more general construction.
- [SoL-Pi](../../../../../sources/sol-pi-efficient-agent-harness.ingest.md) — **compares-with**: capability tolerances screen candidates before nondominated candidates are retained. This separates the question of which outcomes are eligible from which eligible changes survive the comparison; lower cost alone is not evidence of an unqualified improvement.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [On-balance judgment with an LLM](../../../../../theory/on-balance-judgment-with-an-llm.md) → source — **see-also**: the note’s dominance-cones example asks which gains may offset which losses. The future tracked ingest can give that lead a mathematical source for distinguishing a chosen domination structure from ordinary Pareto dominance. Cite the ingest once it exists, not the local snapshot. The abstract does not validate the example’s cone or show that an LLM can apply it reliably.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Brainstorming: maintainability oracles for agentic development](../../../../../theory/brainstorming-maintainability-oracles-for-agentic-development.md) — already notes that a quality frontier leaves the final choice open; it offers no specified dominance relation for a direct comparison.
- [Automated note refinement as a search over a fixed source bundle](../../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) — judging sets by coverage and redundancy is a potential application, but the proposal does not specify or test a frontier rule.
- [PageIndex](../../../../../agentic-systems/reviews-archive/pageindex-2026-09-29-02.md) — separate cost and accuracy figures are not a dominance policy.
- [Hierarchical Choquet models](../../../../../sources/angilella-ordinal-regression-smaa-choquet.ingest.md) — adding interactions and estimating rank frequencies under a sampling distribution answer questions absent from Yu’s captured abstract.
- [GEPA](../../../../../sources/gepa-reflective-prompt-evolution.ingest.md) — instance-wise parent sampling is a search-control mechanism; the shared Pareto vocabulary does not make it an implementation of Yu’s set-finding methods.

## Index Membership

- [robust-comparison](../../../../../tags/robust-comparison-README.md) — consider membership for the tracked ingest only if it explains, with a comparison, how accepting different offsets between effects changes what can be decided without choosing one scoring rule. Neither the snapshot nor an abstract summary alone meets that inclusion condition.

## Synthesis Opportunities

The on-balance and necessary-preference notes suggest a shared worked comparison: hold the routing alternatives and their measured effects fixed, then compare the verdict under a stated domination structure and under compatible whole-work evaluations. In particular, distinguish excluding a remedy for violating a hard ingestion commitment, leaving it feasible but incomparable because ingestion regresses, and preferring it because every admissible valuation allows the offset and at least one strictly favors the remedy. The point is to show which commitments change the verdict, not to rank the formalisms in general.

## Maintenance Observations

- The note-refinement proposal’s Open questions section says to promote a transferable claim to a theory note “in `kb/notes/`”; the current repository routes transferable theory to `kb/theory/`.

## Flags

- The capture is sufficient to attribute the general aim and the Pareto special case to Yu. Do not attribute a specific cone, theorem condition, optimization algorithm, or result about KB changes to this abstract. Consult the full text before using any such claim.
