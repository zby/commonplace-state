---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/why-large-language-models-fail-at-tabular-prediction.md"
source_has_frontmatter: true
date: "2026-08-04"
depth: standard
---

# Connection Report: Why Large Language Models Fail at Tabular Prediction

**Source:** [Why Large Language Models Fail at Tabular Prediction](../../../sources/why-large-language-models-fail-at-tabular-prediction.md)

## Discovery Trace

**Curated heads:**

- Read the source collection contract and the notes, reference, agent-memory-systems, agentic-systems, and sources collection heads and contracts. The notes evaluation and context-engineering heads supplied the strongest routing signal. Reference describes shipped Commonplace, agent-memory-systems covers retained memory, and agentic-systems covers whole harnesses; none contained a direct casebook target for this deliberately harness-free model probe.
- The source carries no `tags`, so no tag-specific complete-mark shortcut or by-tag `rg` pass applied. The notes tags hub was still read for topical routing.

**Complete title and description scans:**

- `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` was run over all five authorised local destinations: notes, reference, agent-memory-systems, agentic-systems, and sources.
- `rg '^description:' kb/<destination>/ --glob '*.md'` was run over the same five destinations. The scans promoted the soft-context-bound, controlled-variation, fixed-decomposition, explanation-faithfulness, effective-context-window, and compositional-depth candidates below.

**Body search:**

- `rg -n -i "tabular|column|dimension|dimensionality|pure inference|in-context classification|benchmark contamination|memorisation|memorization|self-explanation|verbal explanation|stated rule|reasoning trace|harness measures|measures the harness" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- promoted the soft-bound, fixed-decomposition, systematic-variation, and rationale-faithfulness neighborhoods; reference, agent-memory, and agentic-system hits failed the articulation test.
- `rg -n -i "tabular|dimensionality|memorisation|memorization|explanation.*prediction|prediction.*explanation|pure inference|distance-based|nearest.neigh|Gaussian process|random projection" kb/sources --glob '*.md'` -- promoted DiscoverPhysics, Turpin et al., Paulsen MECW, and ConvexBench. SudokuBench and generic harness papers were evaluated but rejected as weaker or differently scoped comparisons.
- `rg -n -i "description:.*(in-context|benchmark|memor|contamin|dimension|tabular|scaffold|harness|pure inference|explanation|faithful|reasoning|intervention|ablation|decomposition|soft degradation|context window)"` over the five authorised destinations was used as a description-level synonym pass. It confirmed that no agent-memory-system or shipped-reference artifact bears directly on pure-inference tabular prediction.

**Link following:**

- Followed [Agent context is constrained by soft degradation, not hard token limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) to its Paulsen, GSM-DC, and ConvexBench evidence. The new source adds a distinct load variable: increasing coordinate count destroys integration while a designated-column retrieval task stays near ceiling at 60 columns.
- Followed [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) into its diagnosis/ablation boundary. H2-H4 are task-semantics-preserving prompt/data interventions used diagnostically, while H5 changes the represented coordinate surface and therefore needs a tighter claim.
- Followed [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) through its local-use and scope-warrant neighbors. Those neighbors sharpen the limitation, but the effective-update-space note is the least duplicative destination.
- Followed [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) to Turpin et al. and the reasoning-production/evaluation note. Turpin is the stronger causal-faithfulness comparison; the new paper contributes a behavioral-alignment test in which stated rules often fail to reproduce the model's predictions.

## Connections Found

- [Agent context is constrained by soft degradation, not hard token limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) -- **is-evidence-for**: with prompt size well inside the hard window, tabular classification collapses as coordinate count grows, while designated-column retrieval remains near ceiling through 60 columns. This separates the ability to read a context from the ability to integrate many relations within it and adds empirical structure to the note's complexity dimension.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- **is-evidence-for**: the paper uses task-preserving interventions on separation, target-column availability, numeric precision, and query batching to diagnose proposed failure mechanisms rather than to improve a prompt or establish explanation reach. The edge should preserve the narrower reading that each intervention bears only on the factor it varies.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the source fixes a single-pass, no-tool, no-scaffold interface, a label-vector response, the transformer hypothesis class, and mostly CSV representations while varying five selected factors. Interpreting the results as evidence about pure inference rather than about all LLM systems depends on separating improvement and failure inside that effective space from warrant for the fixed decomposition.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **is-evidence-for**: on 14 of 20 two-dimensional tasks the model's verbal rule fails to match the data, including cases where its predictions are substantially better than its explanation. This is an additional behavioral instance of legible explanation diverging from the behavior it purports to explain, though it does not directly test retained theory rationales.
- [Ingest: DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- **compares-with**: both benchmarks separate predictive behavior from verbal explanation and actively control recall, but DiscoverPhysics uses counterfactual interactive worlds and a harnessed agent whereas this paper uses a memorization probe plus pure single-pass classification. The comparison distinguishes anti-recall construction and system boundary while preserving the shared accuracy/explanation split.
- [Ingest: Language Models Don't Always Say What They Think](../../../../sources/language-models-dont-always-say-what-they-think.ingest.md) -- **compares-with**: Turpin et al. causally perturb an input feature and test whether chain-of-thought names the factor that moved the answer; this paper instead compares stated rules with rendered decision behavior. Together they distinguish causal faithfulness from the weaker but still useful test of behavioral alignment.
- [Ingest: Maximum Effective Context Window](../../../../sources/paulsen-maximum-effective-context-window-mecw.ingest.md) -- **compares-with**: Paulsen finds severe context degradation on exact structured-data operations but confounds growing token volume with task difficulty; this paper holds toy-scale context feasible, rejects a simple read-the-table failure with the 60-column needle task, and isolates coordinate count as the remaining tested correlate. The pair helps separate token volume, structured-data weakness, and relational integration load.
- [Ingest: ConvexBench](../../../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) -- **compares-with**: both expose one-pass LLM collapse far below hard context limits, but ConvexBench recovers performance through symbolic decomposition and focused calls while this paper intentionally excludes tools and scaffolding. The comparison makes the measurement boundary explicit: one characterizes the bare model; the other evaluates a model-harness compound.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Agent context is constrained by soft degradation, not hard token limits](../../../../notes/soft-degradation-often-binds-before-the-hard-cap-when-evidence-fits.md) → source -- **evidenced-by**: the random-projection and synthetic upscaling sweeps add coordinate-count integration as a measured soft-bound regime, while the needle task shows that column retrieval can remain intact after classification has failed.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) → source -- **evidenced-by**: the paper is a worked multi-intervention diagnostic in which four plausible explanations are rejected under task-preserving changes and the surviving factor is tested in both benchmark and synthetic regimes.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) → source -- **evidenced-by**: the explanation experiment supplies a new behavioral-alignment case where natural-language rules fail to reproduce the model's own prediction surface; the note should retain its caveat that this is not yet a test of rationales attached to retained theories.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [In-context learning presupposes context engineering](../../../../notes/in-context-learning-presupposes-context-engineering.md) -- the source deliberately removes routing, retrieval, tools, and persistent system adaptation. It establishes a boundary for bare in-context classification, not the note's claim that effective deployment depends on machinery selecting and loading the right knowledge.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- both warn against trusting fluent reasoning, but the note's mechanism is evaluator substitution of answer reconstruction for process inspection. The paper tests a model's self-description of its classifier-like behavior, so the rationale-faithfulness note and Turpin comparison provide more precise reader needs.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- a plausible contrast on harness boundaries, but it describes one orchestration API rather than an intervention on tabular reasoning. ConvexBench already supplies the useful bare-model-versus-harness comparison without importing an unrelated product surface.
- [Ingest: Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- shares an architectural-limit framing, but its undisclosed-model company benchmark and constraint-satisfaction task are methodologically weaker and do not clarify this paper's dimensionality mechanism.
- Agent-memory-system reviews -- rejected as a destination class. The source neither retains cross-session state nor evaluates a memory/context-engineering subsystem; its training examples exist only inside one inference prompt.
- Reference documents -- rejected as a destination class. The source bears on transferable evaluation and context theory, not on the shipped Commonplace implementation.

## Index Membership

None. The sources collection has no curated topical index for this paper; its matching ingest report is the durable authored routing surface.

## Synthesis Opportunities

The paper, the soft-bound note, Paulsen MECW, and ConvexBench jointly imply a sharper load model: **input readability, token volume, dependency depth, and integration dimensionality are separable constraints**. The tabular model reads a designated column at 60 dimensions yet fails to combine roughly 16 or more coordinates; Paulsen varies volume on exact structured operations; ConvexBench varies compositional depth and recovers through scoped decomposition. A future synthesis could name integration dimensionality as relation count or coordinate-binding load, but this source does not identify the internal mechanism and should not be made to prove that vocabulary alone.

The source, Turpin et al., and DiscoverPhysics also imply three distinct explanation checks: causal faithfulness to an intervened factor, behavioral alignment between a stated rule and observed predictions, and predictive correctness against ground truth. Treating all three as “explanation quality” would erase what each assay establishes.

## Maintenance Observations

- The snapshot's limitations prose says the final reported experiments cost roughly `$836` in input tokens, while Table 2 totals `$941`. The durable ingest should avoid repeating either aggregate without resolving whether the prose excluded a row or retained an earlier total.

## Flags

- The paper's strongest result is regime-bound: the main experiments use Claude Opus 4.6 in a single-turn, default-sampling, no-tool, no-system-prompt setup; Qwen is tested only on the two-dimensional behavioral comparison. Do not promote “LLMs fail with dimensionality” without this boundary.
- H2 rejects the claim that linearized CSV makes columns unreadable by showing target-column copying at 60 dimensions. It does not compare CSV with alternative structured serializations, so it does not establish that representation choice is irrelevant to classification.
- The main random-projection sweep changes both coordinate count and the particular projection, so lower-dimensional representations need not preserve identical usable signal. The upscaled synthetic two-dimensional suite is the stronger information-preserving control, but it fixes a correlated linear representation and still does not reveal the mechanism.
- The source makes independent claims about dimensionality, benchmark memorization, low-dimensional behavioral similarity, and explanation mismatch across context, evaluation, and faithfulness areas. If durable claims are promoted, use separate composable notes rather than one multi-claim paper note; the immutable snapshot itself should not be split.
