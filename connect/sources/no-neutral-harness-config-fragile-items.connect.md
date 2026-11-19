---
description: "The fragility grid measures item-level sensitivity of model scores and rankings to evaluation configurations, with selection and treatment-grain limits."
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/no-neutral-harness-config-fragile-items.md
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: There Is No Neutral Harness

**Source:** [Paper snapshot](../../../../sources/.snapshots/no-neutral-harness-config-fragile-items.md)

## Discovery Trace

Read all 1,933 lines, including the full reproducibility appendix. Reused the batch contracts, curated heads and complete title surfaces across notes, reference, agent-memory-systems, agentic-systems and sources. Ran `rg -n -i '^description:.*(evaluat|compar|reliab|contrast)'` over memory requirements and the reliability, comparison and experiment note paths. Read reliability dimensions, pairwise-comparison test plan and experimental contrast fully. Followed the experimental-contrast link to systematic prompt variation and read it fully; selected this more precise diagnostic connection rather than reliability dimensions. `rg -l -i 'fragility.grid|config.fragil|no neutral harness' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources` returned no matches, so no additional edges selected there. No external prospecting, instructions or work destinations.

## Connections Found

- [Systematic prompt variation](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — **is-evidence-for**: item-level response and ranking changes under supplied formatting and ordering variations instantiate diagnostic brittleness testing. This is not independent evidence aggregation or variation of an explanation's premises; the scoring comparison additionally changes how answers are elicited and read.
- [Experimental contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **compares-with**: the generation-versus-likelihood comparison bundles presentation, output interface and extraction/scoring. Even the letter-versus-digit templates change answer instructions. Measuring effects per item does not isolate one component of those differences.
- [Pairwise-comparison test plan](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — **compares-with**: a useful evaluation design must test rank and winner stability under interface changes rather than assume that a precise ordering measures stronger discrimination. This paper tests multiple-choice answering, not pairwise judging; its grid is a design analogy for the plan's stability checks.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Systematic prompt variation](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) → eventual tracked ingest — **evidenced-by**: add a bounded example of resolving diagnostic variation to individual items and the rankings they support. Distinguish observed configuration sensitivity from equal capability and from the correctness of a robust-only selection rule.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Reliability dimensions as an additional edge: the systematic-variation note already supplies the specific reader need; avoid redundant general evaluation links.
- Stable-item ties prove equal underlying capability: the pairs retain only 72–336 items after outcome-dependent filtering, and absence of disagreement is not general capability equivalence.
- All benchmark compression methods worsen ranking quality: this analysis uses point-biserial discrimination from twelve models, not a direct evaluation of every compression algorithm or downstream use.

## Index Membership

None.

## Synthesis Opportunities

None.

## Maintenance Observations

None.

## Flags

The study evaluates twelve open-weight instruction models on 3,679 four-choice items across 26 configurations: 24 generation settings from four templates and six orderings, plus two order-invariant likelihood cloze stems. This is not a complete three-axis factorial grid. Greedy generation and fixed items/weights remove those sources of variation, but no stochastic-decoding comparison or agentic-task result follows. Exact regex parsing with eight output tokens scores unparseable generations wrong; the competence/compliance split is left for future work. Likelihood uses mean continuation log-probability with different presentation. The separate code analysis must establish implementation behavior; this paper pass does not.

Distinguish a min/max single-configuration score interval from the much wider robust-to-optimistic item-wise envelope, whose endpoints need not be jointly attainable under one configuration. Axis-robust values .598, .396 and .314 are absolute accuracies, not fractions of already credited answers. Fragile share is a decomposition of the reference gap, not a causal attribution of capability; robustness is selected using observed responses across the grid. Ninety-five-point-seven percent averages ten nonzero pair gaps equally; pooling yields 99.7 percent. Five pairs agree completely on their robust sets, four differ on one item, two have opposing differences that net to zero. Bootstrap zero containment is partly structural and does not establish equivalence.

Four models attain rank one, but two win only one configuration each by one or three items. The two main winners divide 24 generation configurations; margins and exact template text matter. TruthfulQA construction places the correct option first in the original order. Excluding it leaves the main sensitivity findings, changes champion count to three and minimum Kendall correlation to positive .03. The prose says all five non-identity permutations move its correct answer, but the displayed permutation table includes non-identity rows beginning with zero; treat the table/prose discrepancy as unresolved paper detail, not a corrected implementation claim.

Discrimination is a point-biserial correlation of item correctness against reference model accuracy over twelve models. Its association with fragility is .2767, with bootstrap interval .25–.30. At the top-100 threshold, only 36 slots are uniquely selected and 64 come from a 102-item tie. Across 200 seeded tie-breaks the champion mean is 5.67 versus 5.08 for random 100-item subsets and four for the full set; most change comes from sample reduction. One winner per configuration is chosen by a fixed tie-breaking order. These finite-grid findings do not prove an intrinsically neutral or universally valid robust-only evaluation subset.
