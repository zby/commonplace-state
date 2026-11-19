---
description: "Discovery report for possible KB connections from the Beyond Not Novel Enough source snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.md"
source_has_frontmatter: true
date: "2026-06-22"
depth: standard
---

# Connection Report: Beyond "Not Novel Enough"

**Source:** [Beyond "Not Novel Enough"](../../../sources/beyond-not-novel-enough-llm-assisted-scholarly-critique.md)

## Discovery Trace

**Duplicate/source scan:**
- `rg -n "https://arxiv.org/html/2508\.10795v4|arxiv\.org/html/2508\.10795|2508\.10795" kb/sources --glob "*.md"` -- no existing snapshot or ingest report found before capture.

**Collection contracts read:**
- `kb/sources/COLLECTION.md` -- snapshots remain immutable; the authored outbound surface is the ingest report. Authorized source-report labels include `evidence`/`derived-from`/`rationale` to notes, `compares-with` to sources and external-system collections, `defined-in` to definitions, and sparse `see-also`.
- `kb/notes/COLLECTION.md`, `kb/reference/COLLECTION.md`, `kb/agent-memory-systems/COLLECTION.md`, `kb/agentic-systems/COLLECTION.md` -- used to evaluate reverse-edge and cross-collection candidates.

**Description and body search:**
- `rg -n -i "novelty|peer review|reviewer|scholarly|scientific|literature|related work|prior work|LLM-as-Judge|judge|oracle|evaluation" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob "*.md"` -- surfaced the evaluation/oracle cluster: `oracle-strength-spectrum`, `evaluation-automation-is-phase-gated-by-comprehension`, `the-boundary-of-automation-is-the-boundary-of-verification`, `automated-synthesis-is-missing-good-oracles`, and several LLM-as-judge source ingests.
- `rg -n -i "human.*review|human.*alignment|automated.*evaluation|evaluation.*automation|soft oracle|verification|factuality|structured.*extraction|process structure|output structure|context rot|context length|retrieval|rerank" ...` -- added process-structure and semantic-review candidates; kept process-structure because the paper's pipeline and component analysis directly separate reasoning work from assessment output.
- `rg -n "^description:|^title:|^tags:" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- confirmed no direct agent-memory or agentic-system fit; candidate descriptions were mostly evaluation, type-system, or review-system notes.
- `rg -n -i "novelty assessment|not novel enough|ICLR 2025|OpenReviewer|DeepReviewer|Scideator|LLM-assisted feedback|literature-aware" kb/sources kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob "*.md"` -- no prior local coverage of this paper; source-level siblings were scientific-literature and LLM-judge ingests.

**Candidates opened and evaluated:**
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- kept. The paper's human-review analysis, prompt design, style-normalized human baseline, and human validation instantiate the comprehension -> specification -> generalization sequence in a soft-oracle domain.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- kept. Novelty assessment moves from vague reviewer judgment toward a manufactured soft oracle: related-work retrieval, structured comparison, LLM-as-judge scoring, and human validation.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- kept. The paper explicitly frames LLM support as augmenting peer review where human expertise remains necessary because novelty verification is knowledge-intensive and subjective.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- kept. The paper separates process stages (extract, retrieve, synthesize, compare) from the final novelty-assessment report, and its component analysis shows different gains by component.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- kept. The paper evaluates novelty reasoning alignment separately from bottom-line conclusion agreement, a sibling distinction to route validity vs answer agreement.
- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- kept as secondary. The paper is not the same experiment pattern, but its component analysis says human-informed prompt design supplies the largest gains, so it is evidence for converting human review insight into an executable prompt frame.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- rejected as a direct edge. The paper evaluates novelty and related-work comparison; it does not generate scientific syntheses. It belongs in synthesis only when compared with GIANTS and other scientific-discovery sources.
- [Structured output is easier for humans to review](../../../../notes/structured-output-is-easier-for-humans-to-review.md) -- rejected as too general. The human evaluation protocol uses structured dimensions, but the paper's stronger contribution is process/evaluator construction, not readability of structured output.
- [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) -- rejected as a direct edge. The analogy is real, but the source is about scholarly novelty review rather than KB semantic-review implementation.
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) -- rejected as direct evidence. The paper uses pairwise human evaluation to validate an automated evaluator, but it does not compare pairwise judging against scalar judging.

**Source-level candidates opened and evaluated:**
- [GIANTS ingest](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) -- kept as `compares-with`: both manufacture scientific-work soft oracles, but GIANTS uses backcast target reconstruction while this paper uses literature-grounded novelty deltas against human reviewer labels.
- [An Enigma of Artificial Reason ingest](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- kept as `compares-with`: VAIR separates answer correctness from reasoning validity; this source separates novelty conclusion agreement from reasoning alignment.
- [Agentic Code Reasoning ingest](../../../../sources/agentic-code-reasoning.ingest.md) -- kept as `compares-with`: both use explicit process structure as a soft verification surface, one against code hard oracles and one against scholarly-review soft oracles.
- [Koylan pairwise-judging ingest](../../../../sources/even-if-you-set-aside-whether-citations-are-the-right-proxy.ingest.md) -- kept as `compares-with`: Koylan argues for pairwise judging as an evaluator primitive; this paper supplies a concrete peer-review protocol using pairwise human comparisons, while not testing the scalar-vs-pairwise hypothesis.

## Connections Found

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- **evidence**: the source analyzes human novelty reviews before automation, turns observed reviewer patterns into prompt/process design, and validates the resulting evaluator with human pairwise judgments.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **evidence**: the source hardens a vague, subjective novelty judgment into a structured soft oracle using related-work retrieval, novelty-delta comparison, LLM-as-judge scoring, and human validation.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **evidence**: the source shows progress on peer-review support by improving the verification surface for novelty, while explicitly stopping short of replacing human expertise.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- **evidence**: the source's three-stage process and component analysis show that forced reasoning work, structured extraction, landscape analysis, and final report generation contribute differently.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- **evidence**: the source measures reasoning alignment and conclusion agreement as separate outcomes, showing that bottom-line novelty verdicts and supporting reasoning are distinct evaluation targets.
- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- **evidence**: the source's strongest component gain comes from prompts informed by human novelty-review analysis, a paper-scale instance of turning human critique patterns into deployable agent framing.
- [GIANTS ingest](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) -- **compares-with**: both sources manufacture soft oracles for scientific-literature work; GIANTS backcasts known downstream insights, while this paper evaluates novelty through related-work retrieval and reviewer-aligned comparison.
- [An Enigma of Artificial Reason ingest](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- **compares-with**: both separate conclusion-like agreement from reasoning-path validity, but VAIR does so in math reasoning and this source does so in scholarly novelty assessment.
- [Agentic Code Reasoning ingest](../../../../sources/agentic-code-reasoning.ingest.md) -- **compares-with**: both use explicit process structure to improve LLM evaluation; code reasoning approximates hard test oracles, while this source operates in a softer peer-review domain.
- [Koylan pairwise-judging ingest](../../../../sources/even-if-you-set-aside-whether-citations-are-the-right-proxy.ingest.md) -- **compares-with**: Koylan proposes pairwise judging as a general soft-oracle primitive; this source uses pairwise human validation in a concrete scholarly-review evaluation protocol.

## Bidirectional Candidates

- [GIANTS ingest](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md) <-> source -- **compares-with**: future source-review work should read these together as two scientific-literature oracle-manufacturing strategies, one target-reconstruction and one reviewer-alignment.
- [An Enigma of Artificial Reason ingest](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) <-> source -- **compares-with**: both reports should cross-reference the verdict-vs-reasoning split, with VAIR as adversarial evidence and this source as constructive evaluator design.

## Reverse-edge Candidates

- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -> source -- **evidence**: add this as a soft-oracle scholarly-review case where human analysis and judge calibration precede automation.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -> source -- **evidence**: add this as a worked soft-oracle hardening example for subjective novelty assessment.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -> source -- **evidence**: cite the paper as a peer-review domain case where better verification infrastructure enables augmentation but not autonomous replacement.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -> source -- **evidence**: use the paper's component analysis to show process stages and report structure are separable design dimensions.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -> source -- **evidence**: cite reasoning alignment vs conclusion agreement as a non-math case for separating route quality from verdict agreement.
- [Prompt ablation converts human insight into deployable agent framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -> source -- **evidence**: use the human-informed prompt design and component-analysis gain as adjacent evidence, while preserving the distinction from controlled prompt ablation.

## Off-authorisation Candidates

- [Grounding alignment gate](../../../../instructions/review-gates/semantic/grounding-alignment.md) -- The paper's novelty-delta analysis directly resembles checking whether a claim follows from cited sources and whether author framing overstates evidence. `kb/sources/` reports do not author links into `kb/instructions/`, so this should be considered only if a future instruction update cites the source under that instruction collection's own rules.

## Raw Text Candidates

None.

## Rejected Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- rejected as a direct edge because the source assesses novelty rather than synthesizing new knowledge; the relationship becomes useful only through a broader scientific-literature oracle synthesis with GIANTS.
- [Structured output is easier for humans to review](../../../../notes/structured-output-is-easier-for-humans-to-review.md) -- rejected because the source's human-evaluation dimensions are not specifically evidence for the human-readability claim.
- [Semantic review catches content errors that structural validation cannot](../../../../notes/semantic-review-catches-content-errors-that-structural-validation.md) -- rejected as too indirect; the paper's peer-review task is analogous to semantic review but does not evaluate Commonplace-style content review.
- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) -- rejected as direct evidence because the paper does not compare pairwise and scalar judging, measure position bias, or test pairwise optimization loops.
- [Systematic prompt variation serves verification and diagnosis](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- rejected because the source analyzes components and evaluator dimensions, not prompt-variation invariance or decorrelation.
- [Reference: REVIEW-SYSTEM](../../../reference/REVIEW-SYSTEM.md) -- rejected because the source does not describe shipped Commonplace behavior; at most it informs future review-gate design.

## Index Membership

None. The source is a snapshot plus ingest report, not a note to list in note tag indexes. Future note updates should land in the evaluation/oracle cluster.

## Synthesis Opportunities

- **Scientific-work oracle manufacturing has at least two shapes:** backcast target reconstruction, as in [GIANTS](../../../../sources/giants-generative-insight-anticipation-scientific-literature.ingest.md), and literature-grounded delta comparison, as in this source. A future note could compare when each soft-oracle construction is useful and what each excludes.
- **Verdict agreement and reasoning alignment deserve a general evaluator-design note.** [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) covers the route/destination failure mode; this source supplies a constructive peer-review evaluation protocol that separates reasoning alignment from conclusion agreement.

## Maintenance Observations

- The snapshot preserves prose, headings, references, limitations, and figure/table captions, but not table cell structure. Use the original arXiv HTML/PDF for precise table values beyond the headline results captured in the prose.

## Flags

- No split required. The source touches peer review, retrieval, LLM-as-judge, and process structure, but all actionable KB connections route through evaluation/oracle design.
