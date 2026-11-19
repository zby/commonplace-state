---
description: "Discovery report for possible KB connections from the Self-Harness paper snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/self-harness-harnesses-that-improve-themselves.md"
source_has_frontmatter: true
date: "2026-08-02"
depth: standard
---

# Connection Report: Self-Harness: Harnesses That Improve Themselves

**Source:** [Self-Harness: Harnesses That Improve Themselves](../../../sources/self-harness-harnesses-that-improve-themselves.md)

## Discovery Trace

**Description listing scan:**

- Ran scoped `rg '^description:'` listings over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`, filtered for `self-improv|proposal|diagnostic|trace|harness|regression|readable|evaluation|fixed decomposition|outer-loop`. The strongest theoretical candidates were the proposal-selection, diagnostic-richness, readable-artifact, fixed-decomposition, and computational-allocation notes. Reference hits described Commonplace rather than the external system and were rejected as outbound targets. The strongest system/source comparisons were Agentic Harness Engineering, Meta-Harness, and Co-Harness.

**Topic indexes:**

- Read `kb/notes/tags-README.md`, `self-improving-systems-README.md`, `deploy-time-learning-README.md`, `evaluation-README.md`, `observability-README.md`, and `tool-loop-README.md`. The self-improving-systems index supplied the proposal-selection and actor-allocation frame; deploy-time learning supplied diagnostic richness and readable artifacts. The evaluation, observability, and tool-loop heads produced adjacent but weaker candidates.
- Read `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The memory-system head routed to trace-learning coverage; the agentic-systems head contained no existing Self-Harness casebook entry.

**Full title listings:**

- Generated fresh complete `rg -N --no-heading -m1 '^# '` title surfaces for each authorized local destination and filtered them with `self-improv|proposal|diagnostic|trace|regression|harness|fixed decomposition|retention|artifact loop|evaluation`. This confirmed the selected candidates and exposed the closest reviewed systems without relying on a stored generated index.

**Body search:**

- `rg -n -i 'failure pattern|failure signature|diagnostic richness|verifier-grounded|trace.*evidence|evidence.*trace' ...` -- kept diagnostic richness and Agentic Harness Engineering because both distinguish verifier outcomes from causal failure mechanisms; rejected generic trace-retention hits that do not produce harness changes.
- `rg -n -i 'proposal.*evaluat.*retention|search.*evaluation.*retention|regression gate|non-regress|candidate.*accept|reject.*candidate' ...` -- kept the proposal-selection note because Self-Harness explicitly generates parallel candidates, rejects most by a two-split gate, and merges accepted edits into the operative harness.
- `rg -n -i 'harness (edit|improv|evol)|self-harness|model-specific harness|bounded edit' ...` -- kept the readable-artifact and computational-allocation notes; rejected always-loaded-context and generic harness-anatomy hits because they do not explain the improvement loop.
- `rg -n -i 'Self-Harness|Meta-Harness|Co-Harness|Agentic Harness Engineering' kb/sources --glob '*.ingest.md'` -- kept Meta-Harness and Co-Harness as the two clean source-level comparisons.

**Link following:**

- Followed diagnostic richness to the Meta-Harness and Agentic Harness Engineering reviews. Self-Harness occupies the same trace-to-harness family but replaces raw-trace proposer access with fixed structured failure signatures and uses the target model itself as proposer.
- Followed the readable-artifact note to Meta-Harness and Co-Harness. Self-Harness supplies another fixed-weight natural-language-plus-symbolic loop, while Co-Harness is the nearest contrast because it adds weight updates.
- Followed the proposal-selection note through the self-improving-systems index to computational allocation. The paper assigns search, evaluation, and retention to computational actors for a bounded benchmark pathway, but leaves the objective, evidence decomposition, editable surfaces, and evaluator fixed by the designers.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: Self-Harness is a direct worked instance in which parallel bounded edits supply search, a reject-capable held-in/held-out gate supplies evaluation, and merging accepted edits into the next runnable harness supplies operative retention.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: the loop separates pass/fail selection signals from structured failure signatures containing verifier cause, causal status, agent mechanism, passing behaviors, and prior-edit history, although it does not ablate this representation against raw traces or scores alone.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) -- **is-evidence-for**: fixed weights improve through small, auditable edits to natural-language instructions and symbolic harness controls, with regression tests and rollback-friendly lineage bounding the validation radius.
- [Computationally directed self-improvement is a fixed-boundary reallocation ending in contraction](../../../../notes/computationally-directed-self-improvement-is-a-reallocation.md) -- **is-evidence-for**: for the paper's bounded Terminal-Bench pathway, the target model generates changes and computational gates select and retain them without a stronger proposer or per-edit human decision, while human-authored objectives and machinery remain fixed outside that pathway.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting the gains requires separating improvement inside the declared harness-edit and evidence space from evidence for the fixed DeepAgent architecture, failure-signature representation, pass-rate objective, task split, evaluator, and model.
- [Agentic Harness Engineering](../../../../agent-memory-systems/reviews/agentic-harness-engineering.md) -- **compares-with**: both mine verifier-grounded traces into targeted harness edits around fixed models, but Self-Harness uses exact structured failure signatures and the target model as proposer, whereas AHE stages debugger reports before a separate evolve agent and exposes a broader component space.
- [Ingest: Meta-Harness](../../../../sources/meta-harness-end-to-end-optimization-of-model-harnesses.ingest.md) -- **compares-with**: both optimize fixed-weight harnesses on Terminal-Bench, but Meta-Harness uses a stronger external coding agent with raw-trace access and broad code search, while Self-Harness tests whether the evaluated model can propose narrower changes from prestructured evidence.
- [Ingest: Co-Harness](../../../../sources/co-harness-co-evolving-harness-and-model-weights.ingest.md) -- **compares-with**: both use trace-grounded attribution, local harness diffs, and held-out non-regression gates; Co-Harness then fine-tunes model weights, while Self-Harness deliberately holds weights fixed and isolates the readable harness loop.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **evidenced-by**: the paper gives a compact, empirical harness-level instance of all three functions and of actual candidate rejection.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source -- **evidenced-by**: the paper adds a fixed-weight, three-model Terminal-Bench result with explicit local diffs and non-regression promotion.
- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) → source -- **evidenced-by**: the fixed failure-signature bundle is an additional staged-diagnostic design, but should be cited as corroborating architecture rather than causal ablation evidence.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Always-loaded context mechanisms in agent harnesses](../../../../notes/always-loaded-context-mechanisms-in-agent-harnesses.md) -- rejected because Self-Harness changes some always-loaded instructions but its novel contribution is the learning loop, not a new context-loading mechanism.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- rejected because the paper assumes a prebuilt verifier and failure-attribution scheme rather than testing the comprehension-before-automation claim.
- [The Meta-Harness ablation does not identify episode-backed theory formation](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- rejected as a direct connection because Self-Harness supplies structured summaries without a raw-trace control, so it neither resolves nor materially sharpens that ablation's identification claim.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- rejected because it is a local shipped-system classification, not theory or a peer external-system comparison.
- [The What & When of Self-Evolving Agents](../../../../sources/the-what-and-when-of-self-evolving-agents.ingest.md) -- rejected as redundant once the more discriminating Meta-Harness, Co-Harness, and AHE comparisons are retained.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the source is a useful future casebook placement for a computationally directed, reflective proposal-selection pathway whose editable scope is narrower than its human-designed outer method.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- the source extends the harness-code branch with same-model proposal generation and fixed structured evidence rather than raw-trace or debugger-mediated proposal context.

## Synthesis Opportunities

- Self-Harness, Meta-Harness, and Agentic Harness Engineering imply a three-way design comparison over proposer identity, evidence representation, and edit-space breadth. The current KB has the individual axes but no compact synthesis showing their interaction: a weaker/same-model proposer may need more frontloaded causal structure, while that structure also fixes more of the hypothesis space outside learning.

## Maintenance Observations

None.

## Flags

- The paper's “held-out” split is hidden from the proposer but repeatedly used by the automatic promotion gate. It is therefore selection data, not an untouched final test set; reported held-out gains should not be treated as independent generalization evidence.
