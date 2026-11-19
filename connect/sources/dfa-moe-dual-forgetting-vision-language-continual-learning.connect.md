---
description: "Discovery report for possible KB connections from the DFA-MoE repository snapshot"
type: kb/cache/types/connect-report.md
source: "kb/sources/dfa-moe-dual-forgetting-vision-language-continual-learning.md"
source_has_frontmatter: true
date: "2026-08-21"
depth: standard
---

# Connection Report: DFA-MoE: Tackling Dual Forgetting in Vision-Language Continual Learning

**Source:** [DFA-MoE repository snapshot](../../../sources/dfa-moe-dual-forgetting-vision-language-continual-learning.md)

## Discovery Trace

**Description listing scan:**
- Read the curated heads `kb/notes/README.md`, `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no tags, so no tag-specific README or by-tag search applied.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` separately over `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources` to generate each complete title surface.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over `notes`, `reference`, `agent-memory-systems`, and `sources`; the continual-learning and harness-retention cluster was the only strong fit. Reference documentation, agent-memory system reviews, and whole-harness analyses did not contain a candidate whose reader need was served directly by this model-editing repository.

**Body search:**
- `rg -n -i 'dual forget|foundational retention|foundational capabil|pre[- ]trained knowledge|zero[- ]shot capabil|positive transfer|similarity.calibrated retention|DFA-CIL|DFA-MoE' ...` -- found no earlier DFA analysis; the only pre-existing exact mention is the paper citation in the HCL snapshot.
- `rg -n -i 'forgetting|retention|regression|historical anchor|stability.plasticity|plasticity|baseline capabil|default behavio|original capabil|learned capabil' kb/notes --glob '*.md'` -- kept the governed-write note for its explicit catastrophic-forgetting requirement and the fixed-decomposition note for its experiment-interpretation boundary.
- `rg -n -i 'continual learning|continual adaptation|forgetting|retention|regression|historical anchor|stability.plasticity|plasticity|baseline capabil|default behavio|original capabil|learned capabil' kb/sources kb/agent-memory-systems kb/agentic-systems --glob '*.md'` -- kept HCL as the closest retention-gated harness comparison and rejected the broader optimizer and memory sources as redundant or substrate-mismatched.
- `rg -n -i 'router|routing|mixture.of.experts|task.specific expert|alignment pathway|plasticity pathway|functional pathway' ...` -- found broad routing overlap but no useful connection based on routing alone.

**Link following:**
- Followed the HCL ingest into `continual-learning-requires-governing-behaviour-changing-writes.md`, `warranted-autonomy-is-bounded-by-oracle-domain.md`, and `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`. HCL supplied the closest contrast: finite historical anchors protect acquired harness behavior, while DFA-MoE declares a separate baseline for the model's inherited zero-shot behavior.
- Followed `harness-if-instruction-following-across-instruction-surfaces.ingest.md` into `an-experiment-identifies-only-the-contrast-it-actually-runs.md`. Kept Harness-IF only as a measurement comparison: both designs introduce a baseline intended to prevent pre-existing capability or positive transfer from inflating the quantity attributed to an adaptation mechanism.
- Followed the governed-write note into `the-deployed-system-not-the-model-is-the-unit-of-learning.md` and `treat-continual-learning-as-representational-form-coevolution.md`. Rejected both as direct evidence targets because DFA-MoE updates only a distributed-parametric subsystem; any harness-level generalization remains a transfer hypothesis.

## Connections Found

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **is-evidence-for**: DFA-MoE supplies a concrete parametric design in which regression governance distinguishes forgetting newly acquired classes from eroding capabilities inherited from pre-training.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the repository's reported method can update task-specific and alignment pathways plus hierarchical routers, while the two-pathway split, CLIP backbone, task boundaries, similarity construction, and metric design remain fixed outside that update space.
- [HCL: continual adaptation beyond model parameters](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- **compares-with**: HCL gates loss on sampled prior-task anchors, whereas DFA-MoE separately names incremental-knowledge and pre-trained-knowledge forgetting; together they expose acquired history and inherited foundation as distinct retention targets.
- [Harness-IF](../../../../sources/harness-if-instruction-following-across-instruction-surfaces.ingest.md) -- **compares-with**: Harness-IF's withheld-rule baseline and DFA-MoE's claimed similarity-calibrated baseline address different tasks but share the measurement need to avoid crediting an intervention for behavior supplied by prior capability or transfer.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Continual learning requires governing behaviour-changing writes, not just storing content](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) → source -- **evidenced-by**: if the dual-baseline distinction is promoted, this repository is a bounded implementation case for separating inherited from incrementally acquired capability preservation; the absent paper and unrun code must remain explicit.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- rejected as a direct evidence target because this repository keeps the harness and broader deployed system outside its stated learning and evaluation boundary.
- [Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- rejected as redundant beside HCL: it evaluates prior-task transfer and re-optimization but adds no inherited-foundation baseline.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- rejected because the README describes an evaluation metric, not an autonomous acceptance gate whose authority is bounded by that metric.

## Index Membership

None

## Synthesis Opportunities

- HCL's historical anchors and DFA-MoE's pre-training baseline jointly suggest a transferable hypothesis: continual adaptation may require separate retention checks for capabilities acquired during the update history and capabilities inherited before that history began. The repository alone does not establish that this split transfers from VLM adapters to readable harness artifacts.

## Maintenance Observations

None

## Flags

- The captured source is the official repository README, not the unavailable paper. It documents the declared method, configuration, supported datasets, and evaluation workflow, but provides no quantitative outcome table and was not code-inspected or executed during this ingest.

