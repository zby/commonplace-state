---
description: "Full-text FALSIFYBENCH connections: scoped negative testing, process measurement, and the limits of known-target discovery evidence"
type: kb/reports/types/connect-report.md
source: kb/sources/.snapshots/falsifybench-rule-discovery-games-full-text.md
source_has_frontmatter: true
date: "2026-09-19"
depth: standard
---

# Connection Report: FALSIFYBENCH full text

**Source:** [FALSIFYBENCH snapshot](../../../../sources/.snapshots/falsifybench-rule-discovery-games-full-text.md)

## Discovery Trace

- Read the full 1,525-line capture, including the normative set-relation analysis, game construction, prompts, statefulness, regression, and example traces. Read the source collection's outbound contract and this report's type.
- Curated heads: `kb/notes/learning-theory-README.md`, `evaluation-README.md`, and `discovery-README.md`; `kb/sources/README.md`; `kb/agentic-systems/README.md`; leading routing sections of the agent-memory and reference READMEs. Discovery declares `complete: true`, so no by-tag discovery sweep was needed.
- Generated fresh complete title listings with `rg -N --no-heading -m1 '^# ' kb/<collection>/ --glob '*.md'` for notes (438), reference (162), sources (423), agent-memory-systems (175), and agentic-systems (21). Filtered that complete surface with `discover|hypothes|falsif|scientific|confirmation|test.*theor|evidence.*independ|experiment|oracle|verification.*target`.
- Prospected descriptions with `rg -n '^description:.*(hypothes|falsif|discover|oracle)'` across those five collections. Body query: `FALSIFY|Falsify|negative testing|confirmation bias`. Existing FALSIFYBENCH links led to the sample-efficiency note and hypothesis-generation source; their relevant arguments were checked, not accepted from titles.
- Notes: followed discovery's links to the lifecycle and known-target critique, then the latter's oracle-gap link; inspected experimental-contrast and typed-target arguments. Kept the lifecycle as a scoped comparison and the known-target boundary as evidence. Rejected typed-target classification as a weak fit: this source does not test KB artifact typing.
- Sources: read the incumbent abstract analysis and the hypothesis-generation/updating ingest; followed its comparison to Model Discovery Agent. Kept the active-versus-passive evidence distinction and authored-world comparison.
- Reference: title/description hits concerned skill discovery and ADRs, not hypothesis testing; no source-specific edge survived. Agent-memory and agentic systems: stateful conversation does not establish cross-session memory or characterize any reviewed runtime, so no broad system links were forced.
- External prospecting was skipped. Workshops and instructions are excluded by the source contract. Reverse candidates were assessed under `kb/notes/COLLECTION.md`'s `evidenced-by` rules.

## Connections Found

- [Known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **is-evidence-for**: hidden authored semantic targets permit process-level assessment without establishing open-ended discovery closure.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **compares-with**: the game's explicit hypotheses, tests, and revision instantiate part of inquiry, while an oracle-accepted guess is not KB integration or general acceptance authority.
- [Sample-efficiency conjecture](../../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) — **compares-with**: full text establishes the overly-narrow-hypothesis setting behind the note's existing abstract-level caution, but contains no retained-theory reuse across a controlled shift.
- [Experimental contrast](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — **rests-on**: strategy-success association and model comparisons do not identify the causal benefit of prescribing negative testing.
- [Hypothesis generation and updating](../../../../sources/hypothesis-generation-and-updating-in-large-language-models.ingest.md) — **compares-with**: active self-selected tests and feedback contrast with supplied positive-only examples and alternative hypothesis readouts.
- [Model Discovery Agent](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) — **compares-with**: both inspect experiment selection within supplied problem spaces, but MDA assigns belief update and acquisition to explicit statistical machinery while this game leaves choices to the LLM.

## Bidirectional Candidates

- [Sample-efficiency conjecture](../../../../notes/learning-by-theory-refinement-may-improve-sample-efficiency.md) could cite the new full-text ingest with **evidenced-by** to replace uncertainty about the benchmark construction with the paper's explicit restriction. Retain the distinction from cross-shift reuse; do not present the association as a retention result.

## Reverse-edge Candidates

- [Known-target discovery benchmarks](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) could cite the full-text ingest with **evidenced-by** as a case where process scoring adds evidence beyond final target recovery while leaving discovery closure untested.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Verification needs a typed target](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md): semantic categories and JSON actions do not test the note's artifact-classification mechanism.
- Broad agent-memory/runtime links: within-game conversation history is insufficiently discriminating and the paper does not evaluate persistent memory systems.

## Index Membership

None. The source belongs behind relevant evidence claims rather than requiring another index entry.

## Synthesis Opportunities

A bounded comparison of active probe selection, passive hypothesis elicitation, and explicit statistical experiment design could separate candidate-generation quality from test-policy quality. Existing FALSIFYBENCH, hypothesis-generation, and MDA observations supply different parts, not a controlled cross-system comparison.

## Maintenance Observations

The earlier abstract observation remains immutable. Future source uses needing construction or oracle details should select this full-text observation; do not overwrite the old snapshot or its checksum.

## Flags

- Negative testing is not universally superior: when the hypothesis contains the target, positive tests can refute it. Preserve this normative distinction.
- The same model serves as player and stateless oracle through separate calls; sampled human checks and an offline LLM annotator bound measurement claims.
- No cross-episode retention, weight learning, or criticism-machinery adaptation is evaluated.
