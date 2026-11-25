---
description: "Candidate links for the ELECTRE survey: veto-based outranking as an alternative to additive trade-offs in judging KB changes."
type: types/connect-report.md
source: "kb/sources/.snapshots/electre-methods.md"
source_has_frontmatter: true
date: "2026-11-24"
depth: standard
---

# Connection Report: ELECTRE Methods

**Source:** ELECTRE Methods (local run input named in `source`). Author any eventual outbound links in `kb/sources/electre-methods.ingest.md`; that file has not been published. Any durable source-dependent KB claim should cite the tracked ingest once it exists, not the local reading copy.

The survey models “at least as good as” for each direction of a pair. A sufficient coalition of criteria must support the comparison, and no opposing criterion may object too strongly. Criterion weights represent voting power, not rates for exchanging one loss for another. Failure in both directions means incomparability, not indifference. The method for turning the relation into a shortlist, ranking, or assignment is a separate choice (§§2.2–2.5, 3). This gives Commonplace a way to ask when an ordinary-ingestion regression should block a proposed routing improvement even if other results favor the change. The chapter does not establish which criteria or thresholds Commonplace should choose, or whether a model can judge them reliably.

## Discovery Trace

Read the source collection's outbound rules before prospecting. Searched the six named local destinations, with the broadest pass in theory and sources, where there was a direct comparison-method match. Used reference and systems searches to check for an existing application, and tags to check navigation fit. No prospecting in `kb/work/` or `kb/instructions/`: both are excluded. The snapshot has no `tags:`. No external search: the publisher page was already named by the source metadata.

**Title and description listings:** For each `D` below, generated `rg -N --no-filename -m1 '^# (.*)' -r '$1' "kb/$D/" --glob '*.md' --glob '!*.brief.md'` and screened the full stream with `rg -i 'electre|outrank|pareto|on.balance|preference|trade.off|multi.criteria|multiobjective|robust|compar|priorit|domin|veto|compensat|review|judg'`. Ran `rg -i '^description:' "kb/$D/" --glob "$G"` and filtered the descriptions with `rg -i 'description:.*(electre|outrank|pareto|on.balance|preference|trade.off|multi.criteria|multiobjective|robust|compar|priorit|domin|veto|compensat)'`. `G` was `*.ingest.md` for sources and `*.md` elsewhere. Resolved shortlisted titles with `rg -l -F -x -e '# <exact H1>'` in their collection. The ignored snapshots did not enter the destination listings.

**Body searches:** Across each `D` (same `G`), ran these two queries without relevance scores:

- `rg -il 'ELECTRE|outrank(ing|s)?\b|non[- ]?compensat|concordance|discordance|veto threshold|incomparab' "kb/$D/" --glob "$G"`
- `rg -il 'necessary preference|robust ordinal|Pareto|additive (value|model)|pairwise (comparison|judg)|trade[- ]?off point|weighted sum' "kb/$D/" --glob "$G"`

Checked matching lines in the shortlisted artifacts and followed existing local links one hop. No theory brief matched the combined body expressions (`--glob '*.brief.md'`). Results by destination:

- **Theory:** Read `kb/theory/README.md` for the improvement frame. The robust-comparison head surfaced Necessary preference first; titles surfaced On-balance judgment, Local comparison, and An objection. Descriptions corroborated those leads, and body search found the maintainability-oracle brainstorm's veto stack. On-balance judgment explicitly asks the question the survey answers; followed its links to Necessary preference, Defining Improvement, and ADR 076. Followed Necessary preference to Local comparison and Greco; Local comparison to Reversibility; and the maintainability brainstorm to Quality signals and ATAM. Kept Necessary preference to distinguish universal agreement across measures from a veto within a decision model; kept Local comparison for the concrete non-scalar mechanism and the warning about cycles; kept the brainstorm for a testable alternative to a blanket veto stack. Defining Improvement and An objection explain how to find consequences or new criteria, not how to apply a specified veto. Reversibility changes the alternative under consideration rather than settling the same pair. Quality signals asks whether proxies discriminate; a rule for aggregating criteria cannot establish that they do.
- **Reference:** Read `kb/reference/README.md`. Titles and descriptions surfaced review policy and comparison documentation, not an implementation of outranking. Both shared body queries returned no hits. Extended with `rg -n -i 'decision aid|non[- ]?regression|hard constraint|admissib|quality.attribute' kb/reference/ --glob '*.md' -m 1`. Examined ADR 076 via the On-balance note: the ADR supplies alternatives and the historical reason for choosing one advertised route, not observations or thresholds for ordinary-ingestion regressions. No direct reference edge.
- **Agent-memory-systems:** Read `kb/agent-memory-systems/README.md`. Title and description hits were mostly surveys, review specifications, or preference memory. Body hits included “outrank” meaning read-back priority and the Meta-Harness Pareto frontier. Followed the landing page's comparison table to the same Meta-Harness review found by body search; the trace-learning survey also points to it. The accuracy/context-cost frontier is a genuine dominance screen, but the review provides no criteria or operator commitments for evaluating a veto; a link here would be a speculative retrofit to a frozen historical review.
- **Agentic-systems:** Read `kb/agentic-systems/README.md` and followed Methods & Data to its research-topics pointer. Listings exposed memory comparisons, not criteria for choosing between evaluated alternatives. Body search surfaced Jaz Evals' pairwise deduplication; `rg -n -i 'multi.criteria|rank aggregation|hard gate|pareto|multi.objective' kb/reference/ kb/agentic-systems/ --glob '*.md' -m 2` also surfaced hard gates in retained analyses. Deciding whether two entries are duplicates, or whether a structural check passed, does not aggregate support across a coalition of conflicting criteria. No candidate kept.
- **Tags:** Read `kb/tags/README.md` and the `robust-comparison`, `evaluation`, and `goal-prioritization` heads; followed the robust-comparison head into Necessary preference and An objection. Listings and body search reinforced these routes. Evaluation is a potential navigation home for a substantive KB comparison in the ingest. Robust comparison has the narrower across-compatible-measures inclusion condition; the survey's discussion of robustness alone is not a reason to assign it. Goal prioritization would need substantive treatment of precedence in KB work, not just the existence of thresholds. No outbound relationship label is authorized for tag heads; navigation membership is a separate question.
- **Sources:** Read `kb/sources/README.md`; title, description, and body passes exposed Greco, Angilella, Interval SMART/SWING, and Yu. Followed Greco to Necessary preference, Angilella to Greco, and Yu to On-balance judgment. Checked the source-review surface with `rg -l '^type: types/source-review.md' kb/sources/ --glob '*.md'` and `rg -n -i 'concordance|discordance|veto threshold|outrank|necessary preference|Pareto|preference elicitation' kb/sources/ashby-design-for-a-brain-ultrastability.md`: no match in that review. Kept Greco as the closest durable comparator. Angilella and SMART/SWING answer narrower questions about interactions, rank frequencies, or swing ratios; those are not the main distinction here. Yu is a useful comparator on what a screen leaves undecided, but `git ls-files` showed its ingest is not yet tracked. ATAM helps elicit scenario-specific consequences but does not judge pairs of remedies under a veto and concordance rule.
- **External:** Used only the canonical publisher URL already in the capture. It identifies the chapter the future ingest will analyze; the capture does not establish byte identity with the version of record.

### Candidate origins

- kb/theory/necessary-preference-can-guide-improvement-without-a-global-measure.md — curated-head, titles, descriptions, body-search, link-following
- kb/theory/selection-based-learning-needs-only-a-local-comparison.md — titles, descriptions, body-search, link-following
- kb/theory/brainstorming-maintainability-oracles-for-agentic-development.md — body-search
- kb/sources/greco-ordinal-regression-revisited.ingest.md — descriptions, body-search, link-following
- https://link.springer.com/chapter/10.1007/0-387-23081-5_4 — known
- kb/theory/on-balance-judgment-with-an-llm.md — titles, descriptions, body-search, link-following

## Connections Found

- [Necessary preference can guide improvement without a global measure](../../../../../theory/necessary-preference-can-guide-improvement-without-a-global-measure.md) — **compares-with**: Hold the routing effects fixed and distinguish two ways a verdict stays open. Necessary preference fails to select a winner when compatible measures favor opposite choices. At a fixed ELECTRE model, incomparability means neither directional claim meets the support and non-opposition conditions; it is not evidence that compatible measures disagree.
- [Selection-based learning needs only a local comparison](../../../../../theory/selection-based-learning-needs-only-a-local-comparison.md) — **is-evidence-for**: ELECTRE supplies a concrete pairwise comparison that need not assign each candidate a single score or order every pair. Cycles in the raw relation bound what that example establishes: a separate rule is needed if repeated adoption must be acyclic. The chapter does not test learning outcomes.
- [Brainstorming: maintainability oracles for agentic development](../../../../../theory/brainstorming-maintainability-oracles-for-agentic-development.md) — **compares-with**: Compare the proposed veto stack with a veto on a specific pairwise claim. In ELECTRE Iv (§3.1.2), a comparison-relevant loss can block asserting that the candidate is at least as good as its rival without making the candidate ineligible in every comparison. That distinction can guide a test of decision rules over KB revisions that have already passed hard validation.
- [Ordinal Regression Revisited](../../../../../sources/greco-ordinal-regression-revisited.ingest.md) — **compares-with**: Greco et al. infer a family of additive value functions from judgments on reference alternatives. ELECTRE TRI (§4.2.2) can infer parameters of a relation with vetoes from assignment examples. The elicitation inputs and model family determine what can be inferred; ELECTRE's importance coefficients are not additive substitution rates.
- [ELECTRE Methods, publisher chapter](https://link.springer.com/chapter/10.1007/0-387-23081-5_4) — **derived-from**: Canonical external identity of the survey that the future ingest analyzes.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [On-balance judgment with an LLM](../../../../../theory/on-balance-judgment-with-an-llm.md) → `kb/sources/electre-methods.ingest.md` (after publication) — **evidenced-by**: Ground the note's preliminary outranking example in §§2.2, 2.4 and 3.1.2: require enough support as well as no veto, check the reverse comparison, and do not mistake a blocked direction for a win in the other. This qualifies the method lead; it does not validate the LLM selector or supply a defensible Commonplace threshold. Cite at the worked use and retain the source wording needed to check it before using an ordinary ingest citation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [ADR 076](../../../../../reference/adr/076-source-claim-grounding-is-a-promoted-skill.md) — use through the routing example. It explains the adopted design, not what level of ordinary-ingestion regression should veto it or whether the regression occurred.
- [Meta-Harness](../../../../../agent-memory-systems/reviews/meta-harness.md) — the measured frontier screens for dominance; it does not supply a reason for converting a difference into a veto.
- [Robust ordinal regression and rank acceptability for hierarchical Choquet models](../../../../../sources/angilella-ordinal-regression-smaa-choquet.ingest.md) and [Interval SMART/SWING](../../../../../sources/mustajoki-interval-smart-swing.ingest.md) — interaction, rank frequency, and bounded additive trade-offs are distinct topics, but Greco is sufficient for the comparison between necessary preference over additive models and veto-based outranking.

## Index Membership

- [Evaluation](../../../../../tags/evaluation-README.md) — consider membership for the authored ingest if it substantively explains what the veto comparison can and cannot establish when evaluating a KB change. Do not tag the snapshot or add a curated head entry on the strength of this report.

## Synthesis Opportunities

Combine [On-balance judgment with an LLM](../../../../../theory/on-balance-judgment-with-an-llm.md) and [Local comparison](../../../../../theory/selection-based-learning-needs-only-a-local-comparison.md) in a worked routing comparison. Separate three decisions: whether a remedy is eligible under existing commitments, whether each directional comparison is warranted by the stated outcomes and rule, and what to do if neither direction is warranted. Then vary the permitted ingestion loss without changing the outcome evidence. A changed verdict reveals dependence on the rule; missing regression measurements call for a trial, not a different threshold. ELECTRE's construction/exploitation distinction is useful here even if Commonplace never adopts an ELECTRE algorithm.

## Maintenance Observations

None

## Flags

- Revisit comparison with `kb/sources/yu-cone-convexity-and-nondominated-solutions.ingest.md` once it is tracked. Yu's abstract establishes the screen-versus-final-choice distinction, not the cone assumptions needed for the routing example.
- Do not conflate robustness across parameter settings (§4.1), incomparability within a specified model (§2.2), and ignorance of relevant outcomes. The survey cannot establish that repeated KB changes will be improvements or that an LLM can elicit stable judgments.
