---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/harnesscompass-guiding-automatic-harness-evolution.md"
source_has_frontmatter: true
date: "2026-08-06"
depth: standard
---

# Connection Report: HarnessCompass

**Source:** [HarnessCompass: Guiding Automatic Harness Evolution toward Generalizable and Effective Agent Harnesses](../../../sources/harnesscompass-guiding-automatic-harness-evolution.md)

## Discovery Trace

**Collection rules and curated heads:**

- Read `kb/sources/COLLECTION.md`; its authored companion rule makes the future ingest report, not the immutable snapshot, the outbound link surface. It authorises prospecting in notes, reference, agent-memory-systems, agentic-systems, and sources.
- Read the curated heads at `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The self-improving-systems, deploy-time-learning, trace-learning, and external-harness clusters were plausible; shipped Commonplace reference documentation was not a direct fit.
- Generated the complete fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination> --glob '*.md'`: notes 335, reference 127, agent-memory-systems 172, agentic-systems 11, and sources 439 titles. Keyword screening retained the fixed-decomposition, diagnostic-richness, proposal-selection, trace-learning, AHE, Meta-Harness, Self-Harness, and continual-optimizer neighborhoods.

**Description listing scan:**

- Ran `rg -n -i '^description:.*(harness|evol|feedback|generaliz|decompos|outer-loop|self-improv|trajectory)'` separately over every authorised local destination. Kept the notes on diagnostic richness, experience abstraction boundaries, fixed decompositions, scope warrant, and proposal selection; kept the AHE review and three source ingests as direct technical or empirical comparators.
- Rejected reference hits about Commonplace's own harness-orchestrated reviews and validation architecture: they describe shipped implementation details, not a source-relative design analogue that would aid traversal.
- Rejected most agent-memory-system hits: memory is one of HarnessCompass's seven editable component types, but the paper evaluates whole-harness evolution rather than a memory subsystem with a distinct storage, retrieval, or curation design.

**Body search:**

- `rg -n -i 'generalization gate|task-agnostic|held-out|overfit|scope claim' kb/notes --glob '*.md'` surfaced the scope-warrant and fixed-decomposition cluster. The source's held-out and cross-model tests genuinely probe the reach of accepted edits, while leaving the seven-component/two-track decomposition fixed.
- `rg -n -i 'first-person feedback|blind report|hindsight|trajectory-derived|diagnostic richness|misattribution' kb/notes --glob '*.md'` surfaced diagnostic richness. HarnessCompass adds an agent-perspective signal, grounds it against traces, and reports the important non-monotone result that feedback improves the evolution sample while worsening held-out performance before R3 is added.
- `rg -n -i 'structural.*guidance|guidance.*structural|component-wise|cross-component|interference|effective update space' kb/notes --glob '*.md'` surfaced fixed-decomposition analysis. The structural/guidance partition is a fixed hypothesis-space boundary, not an ablated conclusion.
- `rg -n -i 'generalization gate|task-agnostic|held-out|regression gate|first-person feedback|component-wise|harness evolution' kb/sources --glob '*.ingest.md'` surfaced Self-Harness, Meta-Harness, the phased optimizer study, and several weaker harness sources. The three retained comparators differ on exactly one useful axis each: evidence perspective, generalization protocol, or search/adoption structure.
- `rg -n -i 'generalization gate|task-agnostic|held-out|regression gate|first-person feedback|component-wise|harness evolution' kb/agent-memory-systems kb/agentic-systems --glob '*.md'` retained the code-grounded AHE review as the direct technical basis and rejected broader system reviews whose overlap was only benchmark gating.

**Link following:**

- Followed diagnostic richness to the Meta-Harness ingest and the code-grounded AHE review. This established HarnessCompass's distinctive role: it does not merely expose more external trace detail; it asks the task agent for blind and hindsight first-person reports, then subjects those reports to trace grounding.
- Followed fixed decomposition to the scope-warrant note and the proposal-selection/frozen-function cluster. This separated evidence for transfer within the admitted search space from evidence for the component partition, generalization gate, merger, objective, or evaluator held outside it.
- Followed the phased optimizer ingest to Self-Harness and Meta-Harness. HarnessCompass supplies clean 50/450 task separation and cross-model transfer, but not the later re-optimization episode needed for compounding, so the phased study remains a comparator rather than evidence for a compounding claim.

## Connections Found

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: HarnessCompass tests a new diagnostic viewpoint—blind and hindsight first-person harness feedback grounded against the originating trajectory—and shows that richer proposal evidence can improve the search sample while harming held-out transfer when used without the final integration safeguard.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- **is-evidence-for**: the generalization gate operationalizes the note's boundary clause by admitting only transferable criteria with applicability conditions and rejecting task IDs, test names, private symbols, and task-specific dispatch.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the reported gains occur inside fixed evidence channels, seven editable component types, a structural/guidance partition, two variant tracks, an R3 merge procedure, SWE-bench tasks and verifiers, and a Pass@1 objective; neither the progressive ablation nor cross-model transfer compares rival decompositions.
- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) -- **is-evidence-for**: the disjoint 450-task evaluation and frozen transfer to Claude-Sonnet-4.6 are refutation-capable encounters for the reach of the evolved GPT-5.4 harness, although they do not earn the scope of the fixed search decomposition as a whole.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: HarnessCompass instantiates parallel structural/guidance candidate search, Pass@1-based reject-capable selection, R3 consolidation, and retention of an accepted successor harness.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: AHE is the code-grounded technical basis whose seven-component editable harness and trace-driven evolution loop HarnessCompass retains while adding a task-agnostic gate, grounded agent self-feedback, separate component tracks, and R3 consolidation.
- [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: Meta-Harness demonstrates the value of raw external traces over summaries; HarnessCompass instead adds a grounded first-person diagnostic channel and exposes the transfer risk of that extra signal.
- [Ingest: Self-Harness](../../../../sources/self-harness-harnesses-that-improve-themselves.ingest.md) -- **compares-with**: both learn fixed-weight coding-agent harnesses from verifier-grounded failures, but Self-Harness uses bounded local proposals and a repeatedly consulted regression split, whereas HarnessCompass uses a global task-agnostic content/placement gate, disjoint final evaluation, and two-track merging.
- [Ingest: Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: both target harness-optimizer generalization, but the phased study distinguishes transfer from later re-optimization while HarnessCompass contributes a much larger disjoint held-out set and cross-model transfer without testing a later improvement episode.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → source -- **evidenced-by**: add HarnessCompass as evidence that diagnostic richness includes evidence viewpoint and grounding, and that additional diagnostic signal can worsen held-out behavior even while improving the search set.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) → source -- **evidenced-by**: cite the generalization-gate prompt as an executable worked case of requiring a transferable decision criterion plus an applicability condition.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source -- **evidenced-by**: cite the progressive ablation as a case where the experiment varies gate, feedback, and merge machinery but leaves the evidence representation, action/component basis, and two-track partition outside the effective update space.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) -- rejected: both distinguish symbolic structure from guidance, but this note concerns an LLM-interpreted workflow DSL versus a hard scheduler; HarnessCompass's split is an optimization partition and placement policy.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) -- rejected: HarnessCompass revises harness artifacts but does not revise its own generalization gate, evaluator, component taxonomy, or merger, so it does not supply a new reflective-machinery case.
- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- rejected: prompts, skills, tool descriptions, and memory are named component types, but the paper's claims concern optimization governance rather than always-loaded context mechanics.
- [Ingest: Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- rejected: it shares the harness-evolution topic, but its producer-versus-consumer capability cross-pairing does not clarify HarnessCompass's feedback, gating, or track-isolation claims beyond the retained comparators.

## Index Membership

None

## Synthesis Opportunities

- Extend the diagnostic-richness account from a one-dimensional quantity to a qualified evidence design: **viewpoint** (external trace versus first-person report), **grounding** (unsupported claim versus trace-checked item), and **transfer discipline** (whether richer evidence is prevented from driving sample-specific edits). Meta-Harness supplies the raw-detail contrast; HarnessCompass supplies the viewpoint/grounding mechanism and the result that more feedback alone improves the search sample while reducing held-out performance.
- Distinguish **edit-level generalization** from **decomposition-level generalization**. HarnessCompass's held-out and cross-model tests give meaningful reach evidence for the final evolved harness, while the progressive ablation varies only machinery inside a fixed seven-component, two-track design and therefore cannot validate that partition or the R3 account of cross-component interference.

## Maintenance Observations

None

## Flags

- The paper's progressive ablation is cumulative rather than factorial. It attributes the final result across gate, feedback, and R3 configurations, but does not independently vary the structural/guidance partition, compare alternative partitions, or isolate R3 from other changes under a matched search budget.
