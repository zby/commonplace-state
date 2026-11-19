---
description: "Discovery report for possible KB connections from Harness Updating Is Not Harness Benefit"
type: kb/cache/types/connect-report.md
source: "kb/sources/harness-updating-is-not-harness-benefit.md"
source_has_frontmatter: true
date: "2026-08-04"
depth: standard
---

# Connection Report: Harness Updating Is Not Harness Benefit

**Source:** [Harness Updating Is Not Harness Benefit](../../../sources/harness-updating-is-not-harness-benefit.md)

## Discovery Trace

**Collection contract:**
- Read `kb/sources/COLLECTION.md`. The snapshot is immutable, so its adjacent ingest report carries authored outbound links. The authorised local destinations are notes, reference, agent-memory systems, agentic systems, and sources; `kb/work/` and `kb/instructions/` are excluded.

**Curated heads:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The notes head routed the paper toward deploy-time learning; the agent-memory head foregrounded the distinction between read-back and behavioral effect; the other heads supplied no stronger system-specific target.
- The snapshot has no `tags`, so no tag-README or by-tag search applied.

**Full title listings:**
- Ran `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md'`, and the corresponding command over `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, and `kb/sources`. The strongest title-level candidates were the notes on compounding, contextual activation, fixed decompositions, and proposal-selection loops, plus the two recent harness source ingests.

**Description listing scan:**
- Ran `rg -n '^description:.*(compoun|accumul|harness|activation|invocation|adherence|benefit|consum|self-improv|deploy-time|retention)' kb/notes --glob '*.md' -i`. Kept the compounding, activation, and fixed-decomposition notes. The accumulation and generic retention hits were broader than the paper's specific intervention.

**Body search:**
- Ran `rg -n '(harness[- ]benefit|harness[- ]updat|activate.*(artifact|skill|knowledge)|invok.*skill|adher.*(skill|harness)|later improvement|compounding|produce.*update.*benefit|benefit.*update)' kb/notes --glob '*.md' -i`.
- Ran `rg -n '(harness[- ]benefit|harness[- ]updat|compounding|activate.*artifact|invok.*skill|adher.*skill|self-improv)' kb/reference --glob '*.md' -i`.
- Ran `rg -n '(harness[- ]benefit|harness[- ]updat|activation|invocation|adherence|self-evolv|compounding)'` over `kb/agent-memory-systems` and `kb/agentic-systems`.
- Ran `rg -n '(Harness Updating Is Not Harness Benefit|2605\.30621|harness[- ]benefit|harness[- ]updating)' kb/sources --glob '*.md' -i`. This located the Weng synthesis that cited the paper, the Agent Optimizers compounding boundary case, and the Faithful Self-Evolvers activation evidence.

**Link following:**
- Read the neighborhoods of [Compounding is tested in later improvement](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md), [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md), [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md), and [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
- Followed their source links to the [Agent Optimizers ingest](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md), [Faithful Self-Evolvers ingest](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md), and the [Weng harness-engineering ingest](../../../../sources/harness-engineering-for-self-improvement.ingest.md). Kept only connections that distinguish update production, artifact uptake, task benefit, and later improvement.

## Connections Found

- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **compares-with**: the paper's harness-benefit metric tests whether a retained update improves later task solving, whereas the note reserves compounding for a further causal step in which that benefit helps produce a later improvement.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: skill-load rate measures a storage-to-context transition, while harness-following rate and the case studies measure the distinct context-to-action transition.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: interpreting the model comparisons requires keeping the fixed solve-evolve loop, prompts, task streams, writable substrates, tool interfaces, execution policies, scoring rules, and anchor sets outside the claimed update space.
- [Ingest: Harness Engineering for Self-Improvement](../../../../sources/harness-engineering-for-self-improvement.ingest.md) -- **compares-with**: this paper is the primary empirical basis for the secondary essay's harness-updating versus harness-benefit distinction and narrows the essay's broader claim to three benchmark-specific update surfaces.
- [Ingest: Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **compares-with**: both studies separate stages hidden by end-to-end scores, but this paper separates updater from consumer within an in-situ stream while Agent Optimizers separates transfer from later re-optimization across phases.
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **compares-with**: both test whether retained experience changes later behavior; this paper varies task-solving backbones and decomposes loading from adherence, while Faithful Self-Evolvers intervenes on raw versus condensed experience.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) → source -- **evidenced-by**: the paper supplies a measured necessary bridge from retained update to operational benefit, while also bounding that bridge short of benefit feeding into a later improvement episode.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidenced-by**: the paper operationalizes both failure transitions with skill-load and harness-following measurements and illustrates each with a trajectory case.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected because the paper formalizes evidence-to-update-and-apply, but does not establish a reject-capable candidate-selection gate; treating every evolver update as proposal-selection would erase the note's subtype boundary.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- rejected as a broad inventory whose relevant trace-to-skill cases add no sharper reader need than the activation and fixed-decomposition notes.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected because shared harness editability is only topical; Exo's protected substrate and rewind architecture are not tested by this paper.

## Index Membership

None

## Synthesis Opportunities

- The paper, the activation note, and the compounding notes imply a five-stage causal chain: update production → operative retention → artifact loading → faithful use and task benefit → contribution of that benefit to later improvement. The paper measures the middle stages. It does not measure the final feedback step, which is the distinction a compounding definition must preserve.

## Maintenance Observations

None

## Flags

- The paper names `Δupdate` as an evolver capability, but calculates it through downstream gains obtained by anchor agents. Cross-pairing reduces agent-specific confounding without eliminating dependence on the fixed anchor set and those agents' harness-benefit capabilities.
- The weak-tier activation and adherence diagnosis is observational apart from two illustrative trajectories. No intervention repairs loading or adherence and then measures whether the weak-tier benefit gap closes.
