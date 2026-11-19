---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/work/causal-impact-selective-evaluation/hcl-reading.md"
source_has_frontmatter: false
date: "2026-08-21"
depth: standard
---

# Connection Report: Reading HCL as deployment-time learning

**Source:** [Reading HCL as deployment-time learning](../../../../work/explanatory-theories-deployment-time-learning/hcl-reading.md)

## Discovery Trace

**Setup and authority surface:**
- Read [`kb/cache/types/connect-report.md`](../../../../types/connect-report.md), the full source file, and [`kb/work/COLLECTION.md`](../../../../work/COLLECTION.md).
- Source is raw workshop text with no frontmatter, so discovery used title/body signal rather than typed metadata or tags.
- `kb/work/COLLECTION.md` authorizes prospecting `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/instructions/`, `kb/sources/`, and peer workshops under `kb/work/`.
- The same collection contract says library collections do not link into `kb/work/`, so durable-library reverse edges to this file were treated as unauthorized and not surfaced.

**Curated heads read:**
- [`kb/work/causal-impact-selective-evaluation/README.md`](../../../../work/explanatory-theories-deployment-time-learning/README.md) to establish the workshop question and sibling-file roles.
- [`kb/notes/tags-README.md`](../../../../tags/README.md), [`kb/reference/README.md`](../../../../reference/README.md), [`kb/agent-memory-systems/README.md`](../../../../agent-memory-systems/README.md), [`kb/agentic-systems/README.md`](../../../../agentic-systems/README.md), [`kb/instructions/README.md`](../../../../instructions/README.md), [`kb/sources/README.md`](../../../../sources/README.md), and [`kb/work/README.md`](../../../../work/README.md).

**Notes prospecting:**
- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`
  - Flagged by title scan: `retained-artifacts-enable-persistent-deployment-time-adaptation`, `continual-learning-requires-governing-behaviour-changing-writes`, `localized-retention-pays-where-change-is-sparse-in-a-matching-decomposition`, and `learning-inside-a-fixed-decomposition-inherits-its-mistakes`.
- Description surface:
  - `rg '^description:' kb/notes/ --glob '*.md'`
  - Confirmed the same cluster: deployment-time adaptation, governed writes, locality under matching decompositions, and fixed-decomposition limits.
- Body search:
  - `rg -n 'deployment-time learning|deployed system|proposal-selection|search, evaluation, and retention|oracle domain|experiment identifies only the contrast|selective evaluation|causal graph|held-out forgetting|locality' kb/notes/ --glob '*.md'`
  - This search confirmed that the source already links [`the-deployed-system-not-the-model-is-the-unit-of-learning.md`](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [`a-proposal-selection-loop-requires-search-evaluation-and-retention.md`](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [`warranted-autonomy-is-bounded-by-oracle-domain.md`](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), and [`an-experiment-identifies-only-the-contrast-it-actually-runs.md`](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).
  - Read the unlinked candidates that materially sharpen this file's claims: [`retained-artifacts-enable-persistent-deployment-time-adaptation.md`](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [`continual-learning-requires-governing-behaviour-changing-writes.md`](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md), [`localized-retention-pays-where-change-is-sparse-in-a-matching-decomposition.md`](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), and [`learning-inside-a-fixed-decomposition-inherits-its-mistakes.md`](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md).
- Link following:
  - Followed the source's existing links into proposal-selection, oracle-domain, and contrast-grain notes.
  - Kept `retained-artifacts-enable-persistent-deployment-time-adaptation` because the source classifies HCL as deployment-time learning but never links the note that names that lifecycle/update-mechanism frame.
  - Kept `continual-learning-requires-governing-behaviour-changing-writes` because the source's joint versioning of interface, memory, capability, and router is a direct readable-artifact case of governed behaviour-changing writes across mutable retained state.
  - Kept `localized-retention-pays-where-change-is-sparse-in-a-matching-decomposition` because the source says HCL's four-part partition does not yet justify local impact claims; this note supplies the exact matching/dependency/bounded-impact condition the workshop would need.
  - Kept `learning-inside-a-fixed-decomposition-inherits-its-mistakes` because the source's closing caution about HCL's four-part engineering partition is an instance of that fixed-decomposition limitation.

**Reference / agentic-systems / agent-memory-systems / instructions prospecting:**
- Read the collection heads, then ran:
  - `rg -n 'HCL|Harness Continual Learning|continual harness|selective evaluation|causal impact|deployment-time learning' kb/reference/ kb/agentic-systems/ kb/agent-memory-systems/ kb/instructions/ --glob '*.md'`
- No matches. Those destinations were checked and skipped after the scoped search returned nothing specific to HCL, selective evaluation, or this workshop's causal-impact framing.

**Sources prospecting:**
- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`
- Description surface:
  - `rg '^description:' kb/sources/ --glob '*.md'`
- Body search:
  - `rg -n 'continual harness|harness continual learning|HCL|SPADE|selective evaluation|causal' kb/sources/ --glob '*.md'`
- Read the already linked authored surface [`harness-continual-learning-adaptation-beyond-model-parameters.ingest.md`](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) as the source's paired evidence record.
- Read [`dowhy-expressing-and-validating-causal-assumptions.ingest.md`](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) because the source explicitly refuses to treat HCL's four-part partition as a validated causal graph; DoWhy is the local source that states the assumption/partial-validation boundary for causal claims.
- Read [`the-risks-of-invariant-risk-minimization.ingest.md`](../../../sources/the-risks-of-invariant-risk-minimization.ingest.md) as a possible formal caution on causal-locality claims, but rejected it for this file: it bears more directly on the broader selective-evaluation model than on this HCL reading's concrete claims.
- Read [`continual-harness-online-adaptation-foundation-agents.ingest.md`](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) as a possible contrast case, then rejected it for this file: the direct-update contrast belongs to the workshop-level comparison, not to this source's HCL-specific architectural classification.

**Work prospecting:**
- Title surface:
  - `rg -N --no-heading -m1 '^# ' kb/work/ --glob '*.md'`
- Description surface:
  - `rg '^description:' kb/work/ --glob '*.md'`
- Body search:
  - `rg -n 'deployment-time learning|selective evaluation|causal|HCL|harness continual learning|SPADE|oracle domain|proposal selection|retention|forgetting|locality' kb/work/ --glob '*.md'`
- Rejected already linked siblings [`selective-evaluation-model.md`](../../../../work/explanatory-theories-deployment-time-learning/selective-evaluation-model.md), [`experiment-design.md`](../../../../work/explanatory-theories-deployment-time-learning/experiment-design.md), and [`for-hcl-authors.md`](../../../../work/explanatory-theories-deployment-time-learning/for-hcl-authors.md).
- Kept [`../continual-harness-governance-experiment/README.md`](../../../../work/continual-harness-governance-experiment/README.md) as the one peer-workshop raw-text candidate: it studies the same harness-adaptation governance question under a direct-update architecture and explicitly applies the fixed-decomposition lens this HCL reading invokes.

## Connections Found

- [retained-artifacts-enable-persistent-deployment-time-adaptation.md](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **rests-on**: the source classifies HCL as deployment-time learning but only links the unit-of-learning and proposal-selection notes; this note supplies the missing deployment-time adaptation frame and the lifecycle-versus-update-mechanism separation that classification assumes.
- [continual-learning-requires-governing-behaviour-changing-writes.md](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) -- **extends**: HCL's jointly versioned interface, memory, capability map, and router are a concrete instance of the note's broader claim that continual learning must govern behaviour-changing writes across retained state, not merely store new content.
- [localized-retention-pays-where-change-is-sparse-in-a-matching-decomposition.md](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- **draws-on**: the source says HCL's four-part partition does not yet justify local-impact claims; this note names the stronger condition the workshop would need before selective evaluation could rely on locality.
- [learning-inside-a-fixed-decomposition-inherits-its-mistakes.md](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **grounds**: the source's warning that HCL's update-permission ablations do not validate the four-part carve as the right causal units is a direct instance of this fixed-decomposition limit.
- [dowhy-expressing-and-validating-causal-assumptions.ingest.md](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) -- **draws-on**: once the source says the workshop should not treat HCL's partition as a validated causal graph, DoWhy becomes the nearest local source for why any causal extension needs explicit assumptions and only partial validation.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [README.md](../../../../work/continual-harness-governance-experiment/README.md) -> source -- **contrasts**: the peer workshop already uses the fixed-decomposition lens and distinguishes direct update from proposal selection; a link back to this HCL reading would give that workshop a concrete gated-candidate contrast case.

## Off-authorisation Candidates

None

## Raw Text Candidates

- [README.md](../../../../work/continual-harness-governance-experiment/README.md) -- potential **contrasts**: this raw-text peer workshop studies the same harness-adaptation governance question under a direct-update architecture and makes explicit the proposal-selection/direct-update distinction that this HCL reading only implies.

## Rejected Candidates

- [the-deployed-system-not-the-model-is-the-unit-of-learning.md](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- rejected as a new candidate because the source already links it directly.
- [a-proposal-selection-loop-requires-search-evaluation-and-retention.md](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- rejected as a new candidate because the source already links it directly.
- [warranted-autonomy-is-bounded-by-oracle-domain.md](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- rejected as a new candidate because the source already links it directly.
- [an-experiment-identifies-only-the-contrast-it-actually-runs.md](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- rejected as a new candidate because the source already links it directly.
- [harness-continual-learning-adaptation-beyond-model-parameters.ingest.md](../../../../sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md) -- rejected as a new candidate because the source already links its paired authored source analysis.
- [selective-evaluation-model.md](../../../../work/explanatory-theories-deployment-time-learning/selective-evaluation-model.md) -- rejected as a new candidate because the source already links it directly.
- [experiment-design.md](../../../../work/explanatory-theories-deployment-time-learning/experiment-design.md) -- rejected as a new candidate because the source already links it directly.
- [for-hcl-authors.md](../../../../work/explanatory-theories-deployment-time-learning/for-hcl-authors.md) -- rejected as a new candidate because the source already links it directly.
- [the-risks-of-invariant-risk-minimization.ingest.md](../../../sources/the-risks-of-invariant-risk-minimization.ingest.md) -- rejected because its invariance-bound warning bears on the broader selective-evaluation model, not on this source's narrower HCL reading and sampled-retention interpretation.
- [continual-harness-online-adaptation-foundation-agents.ingest.md](../../../../sources/continual-harness-online-adaptation-foundation-agents.ingest.md) -- rejected because the direct-update contrast is better carried by the peer workshop and would pull this file away from its HCL-specific classification task.

## Index Membership

None

## Synthesis Opportunities

- [`hcl-reading.md`](../../../../work/explanatory-theories-deployment-time-learning/hcl-reading.md), [localized-retention-pays-where-change-is-sparse-in-a-matching-decomposition.md](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md), [learning-inside-a-fixed-decomposition-inherits-its-mistakes.md](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), and [dowhy-expressing-and-validating-causal-assumptions.ingest.md](../../../../sources/dowhy-expressing-and-validating-causal-assumptions.ingest.md) together suggest a higher-order note: selective evaluation needs both a locality claim with explicit dependency closure and a stated assumption surface for its causal graph, not merely a useful engineering partition.

## Maintenance Observations

None

## Flags

- Source has no frontmatter, so this report is provisional and discovery relied on title/body signal.
- `kb/work/` is a sink for durable library references under [`kb/work/COLLECTION.md`](../../../../work/COLLECTION.md); library-to-work reverse edges were intentionally excluded rather than treated as missed links.
