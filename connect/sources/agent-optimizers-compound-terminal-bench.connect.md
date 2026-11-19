---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/agent-optimizers-compound-terminal-bench.md"
source_has_frontmatter: true
date: "2026-08-04"
depth: standard
---

# Connection Report: Do Agent Optimizers Compound?

**Source:** [Do Agent Optimizers Compound? A Continual-Learning Evaluation on Terminal-Bench 2.0](../../../sources/agent-optimizers-compound-terminal-bench.md)

## Discovery Trace

**Description listing scan:**

- Generated complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes` (333 files), `reference` (127), `agent-memory-systems` (172), `agentic-systems` (11), and `sources` (430). The closest note titles were *Improvements can accumulate without compounding*, *Compounding is tested in later improvement, not by the accepting metric*, *Continual learning's open problem is behaviour, not knowledge*, and *An omitted improvement-loop function and a frozen one need different repairs*.
- Ran `rg -n '^description:.*(compound|continual|recursive|self-improv|regress|optimizer|overfit|generaliz|benchmark|retention|proposal-selection)' ... -i` across all authorised local destinations. This added the Self-Harness, Meta-Harness, HyperAgents, Auto Harness, and Huxley-Gödel Machine candidates. Reference hits concerned Commonplace-specific implementation regressions and were rejected because this source makes no claim about the shipped Commonplace system. Agentic-system hits named recursive-improvement harnesses but supplied no shared experimental axis beyond broad topic overlap.

**Topic indexes:**

- Read `kb/notes/README.md` and `kb/notes/self-improving-systems-README.md`. The latter routes compounding through later dependence on retained results and later-improvement evidence, making the two compounding notes the primary theory cluster.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The memory-system index routed to code-grounded Meta-Harness, Auto Harness, and HyperAgents reviews; the agentic-system index yielded no candidate with a concrete reader need.

**Body search:**

- `rg -n -i "regression control|no-regression|static benchmark|one-shot benchmark|re-optimization|task expansion|compounding question|optimizer-driven|previously solved|later improvement" ...` found the compounding notes' displaced-measure requirement, the Self-Harness regression gate, the Auto Harness promoted regression suite, and the HyperAgents cross-domain transfer case.
- `rg -n -i "RELAI-VCL|verifiable continual|Meta Harness|agent optimizer|regression-aware" kb --glob '*.md'` found no prior RELAI-VCL coverage and confirmed that this snapshot is the first local capture of the method's reported continual-learning evaluation.
- `rg -n '^description:' ... | rg -i 'regression|compounding|harness|overfit|benchmark|proposal-selection'` confirmed the nearest descriptive artifacts: the Self-Harness and Meta-Harness ingests plus the Meta-Harness and Auto Harness reviews.

**Candidate evaluation:**

- Kept the proposal-selection note because all three methods expose candidate generation, reject-capable benchmark evaluation, and retained harness changes; RELAI-VCL's in-loop regression rule is a particularly explicit evaluation design.
- Kept the fixed-decomposition note because the experiments vary optimizers while fixing the base model, baseline harness, Terminal-Bench task partition, verifier interface, rollout budgets, and most method-specific update machinery. The gains distinguish methods inside that setup but cannot validate those surrounding choices.
- Kept the two compounding notes because the paper operationalises the term differently: it measures transfer plus successful re-optimization from the retained Phase-1 agent, whereas the KB requires evidence that the earlier retained benefit helped produce the later improvement. No fresh-start Phase-2 control isolates that contribution.
- Kept the frozen-function note because RELAI-VCL supplies another proposal-selection system whose no-regression acceptance rule is deliberately fixed outside the update space it governs.
- Kept Self-Harness and Meta-Harness as source comparisons because they share Terminal-Bench harness search and regression evaluation; kept HyperAgents because its cross-domain transfer protocol is the closest existing comparison for the stronger KB definition of compounding.
- Kept the code-grounded Meta-Harness and Auto Harness reviews as comparisons for, respectively, one evaluated optimizer's actual retained surfaces and an independent promoted-regression-suite design. Rejected the HyperAgents review as duplicative once its paper ingest carried the relevant evaluation claim.
- Rejected *Continual learning's open problem is behaviour, not knowledge*: the source is a readable-artifact behaviour-change case, but the existing Self-Harness and Meta-Harness sources already establish that class and this paper's novelty lies in repeated optimization and regression control.
- Rejected the Huxley-Gödel Machine ingest: both question immediate benchmark score, but HGM studies parent-selection productivity across a lineage rather than regression-aware re-optimization on an expanding task set.

**Link following:**

- Followed the self-improving-systems index into the two compounding notes, then followed their links to HyperAgents and the proposal-selection decomposition. HyperAgents revealed the missing counterfactual in the current paper: later use of retained machinery is visible, but whether the retained Phase-1 improvement made Phase 2 more productive than a fresh start is not isolated.
- Followed the fixed-decomposition note into the frozen-function comparison and the Self-Harness ingest. Self-Harness supplies the nearest fixed-boundary analogue and clarifies which claims a regression gate can support.
- Followed the Meta-Harness ingest into its code-grounded review. The review verifies the method's trace/code surfaces, while the present paper supplies a new two-phase outcome for one concrete Meta-Harness run.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: the compared harness optimizers instantiate rejectable search and operative retention, while RELAI-VCL makes prior-task non-regression part of candidate selection.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: the comparison varies update methods inside a fixed model, benchmark, task split, verifier, budget, and outer experimental protocol, so its gains do not validate those fixed choices.
- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) -- **is-evidence-for**: Meta Harness's transfer followed by stalled re-optimization and GEPA's weak transfer followed by recovery empirically separate retained task gains from reliable later improvement, while RELAI-VCL's result still lacks the counterfactual needed for the KB's causal compounding claim.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **is-evidence-for**: the phased protocol moves evaluation to a later optimization episode, but reuse of task pass rate and the absence of a fresh-start Phase-2 control bound what it establishes about the retained Phase-1 benefit's causal contribution.
- [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -- **is-evidence-for**: RELAI-VCL adds a proposal-selection case whose explicit no-regression evaluator is present and effective within the experiment but fixed outside the edits it governs.
- [Ingest: Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both use Terminal-Bench harness edits and regression-aware selection, but Self-Harness studies bounded same-model proposals while this paper compares three optimizer designs over two task-arrival phases.
- [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: the current source supplies a new two-phase transfer and re-optimization result for Meta-Harness, complementing the earlier source's static search and trace-richness ablation.
- [Ingest: HyperAgents](../../../../sources/hyperagents.ingest.md) -- **compares-with**: both claim compounding, but HyperAgents transfers retained improvement machinery across domains whereas this paper retains a Phase-1 agent and expands the task objective without isolating whether that earlier improvement helped produce the later one.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- **compares-with**: the review code-grounds the optimizer's trace, history, and executable-update surfaces that the present evaluation treats as one method.
- [Auto Harness](../../../../agent-memory-systems/reviews/auto-harness.md) -- **compares-with**: both put regression control inside harness-update selection; Auto Harness promotes repaired failures into a durable regression suite, while RELAI-VCL rejects candidates that lose previously solved tasks.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → source -- **evidenced-by**: the source is a useful boundary case because it names a later re-optimization episode “compounding” without isolating the retained first-round improvement's causal contribution against a fresh-start control.
- [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) → source -- **evidenced-by**: RELAI-VCL extends the note's casebook with a fixed, reject-capable regression gate whose measured benefit does not imply that the gate itself is revisable or generally warranted.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Continual learning's open problem is behaviour, not knowledge](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- correct class but no new reader need beyond already captured readable-harness learning cases.
- [Ingest: Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) -- both challenge one-shot scores, but HGM's lineage-productivity question is too different from phased regression-aware task expansion for a compact comparison edge.
- [HyperAgents review](../../../../agent-memory-systems/reviews/hyperagents.md) -- code-grounded topical match, but the paper ingest carries the relevant transfer and compounding evidence more directly.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- recursive self-improvement is only broad topical overlap; no shared evaluated method or claimed mechanism passes the articulation test.

## Index Membership

None

## Synthesis Opportunities

None. The apparent synthesis -- regression preservation is not yet compounding evidence -- is already owned by the existing compounding notes and should be handled as a bounded empirical case rather than a new note.

## Maintenance Observations

None

## Flags

- Terminology tension: the paper defines compounding as positive transfer plus continued improvement under a second optimization budget; the KB reserves compounding for a causal contribution from an earlier retained benefit to later improvement. Preserve both meanings explicitly rather than silently treating the reported headline as evidence for the stronger local claim.
