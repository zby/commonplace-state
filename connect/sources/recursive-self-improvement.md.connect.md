---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/recursive-self-improvement.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: Recursive self-improvement

**Source:** [Recursive self-improvement](../../../../sources/.snapshots/recursive-self-improvement.md)

## Discovery Trace

No ranked scores were available from the repo-local tools.

**Curated heads:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md` before prospecting their collections. The source has no `tags`, so there was no matching tag-README lookup to run. The notes title and body scans led to [Self-improving systems](../../../../tags/self-improving-systems-README.md), which was then read as the relevant selective head.
- The notes head led to the local membership definition, improvement-objective rule, proposal-selection architecture, compounding distinction, oracle boundary, and casebook. These candidates survived because each corrects or sharpens a different part of the source's broad account.
- The agent-memory head and exact-example search led to [Voyager](../../../../agent-memory-systems/reviews/voyager.md), which is a code-grounded account of an experiment the source names. The agentic-systems head led to [Exo](../../../../agentic-systems/reviews/exo.md), a code-grounded running harness explicitly designed for recursive self-improvement.
- The reference head exposed Commonplace-specific worked cases rather than general RSI analysis. They were evaluated and rejected as destination-specific rather than useful continuations from this source.

**Full title surfaces:**
- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (429 headings), `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (162), `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (175), `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (20), and `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` (395).
- The complete title pass surfaced the self-improving-system theory cluster, Exo, Voyager, and the direct source comparisons retained below. It also surfaced the rejected Gödel-machine, Agno, Poetiq, and Commonplace-specific candidates recorded below.

**Description listings:**
- Ran `rg -n '^description:' kb/notes/ --glob '*.md' | rg -i 'recursive|self-improv|self-modif|reflective|compoun|objective|oracle|verification|evaluation|alignment|model collapse|continual learning|feedback|evolution'`. Kept the definition, objective, proposal-selection, compounding, oracle, and casebook candidates; rejected reflection-only and generic evaluation matches that did not sharpen this source.
- Ran the same first-stage listing and filter over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. In reference, matches were Commonplace-specific worked cases and were rejected. In agent memory, Voyager was the exact named experiment and Exo's memory review was redundant with the stronger whole-system review. In agentic systems, Exo was the clearest mechanism-level comparison. In sources, the harness, measurement, safety, and Darwin Gödel Machine ingests supplied non-redundant comparison axes.

**Body search:**
- Ran `rg -n -i 'recursive self-improvement|intelligence explosion|seed improver|seed ai|model collapse|alignment faking|AlphaEvolve|Self-Taught Optimizer|\bVoyager\b' kb/notes/ --glob '*.md'`. This confirmed that Voyager is already used as an executable-skill example, while no note directly develops the source's intelligence-explosion, AlphaEvolve, STOP, model-collapse, or alignment-faking claims.
- Ran the same query over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. Reference had no exact matches. Agent memory returned Voyager as the exact named system. Agentic systems returned Exo and a weaker Agno boundary discussion. Sources returned the selected direct RSI comparisons plus weaker or redundant neighbors.
- Ran `rg -n -i 'self-modif|rewrite(s|ing)? (its|their) own (code|program)|automated evaluation|evaluation function|validation protocol|recursive.*improv|compounding' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`. This confirmed the source's central tensions: code writability does not establish an improvement pathway, an acceptance metric does not establish compounding, and automated evaluation bounds the domain in which unattended adoption is warranted.

**Link following:**
- Followed [Self-improving systems](../../../../tags/self-improving-systems-README.md) to [Self-improving system](../../../../notes/definitions/self-improving-system.md), [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md), [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md), [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md), [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), and the thirteen-system casebook. This neighborhood supplied the accepted theory candidates and showed that the Gödel-machine note was a more specialized formal case.
- Followed Voyager's retained-skill mechanism through its existing note links and kept the review because the source explicitly cites Voyager as experimental research. Followed Exo from the agentic-systems head into its self-modification loop and oracle limits; its separate memory review was rejected as duplicative for this source.
- Followed direct RSI source ingests into their linked theory and neighboring sources. Kept four with distinct reader needs: near-term harness optimization, measurement of compounding, the safety/intelligence-explosion canon, and an empirical self-rewriting archive. Poetiq and the fragility paper were rejected as redundant or mechanism-mismatched.

## Connections Found

- [Original Wikipedia article](https://en.wikipedia.org/wiki/Recursive_self-improvement) -- **derived-from**: the future ingest analysis is worked out from this captured external article.
- [Self-improving system](../../../../notes/definitions/self-improving-system.md) -- **defined-in**: gives the KB's frame-indexed, causal definition of self-improvement, preventing the source's broad code-rewriting account from silently treating work-product improvement, storage, or self-modification alone as system improvement.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) -- **compares-with**: the source supplies “improve your capabilities” as a seed goal and later raises misalignment, while the note states the boundary, horizon, and objective conditions needed to judge whether a change is improvement at all.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **compares-with**: the source's seed architecture names programming, validation, testing, and retained changes; the note separates the search, reject-capable evaluation, and operative-retention functions that make this a governed improvement loop.
- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) -- **compares-with**: the source moves from repeated self-change to an intelligence explosion, while the note requires evidence that an earlier retained benefit makes a later improvement episode more productive before calling the pathway compounding.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: the source's AlphaEvolve summary identifies automated evaluation functions as the limiting condition on iterative algorithm optimization, a concrete instance of evaluation warrant bounding autonomous search and adoption.
- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -- **compares-with**: the source groups heterogeneous systems under one RSI progression, while the casebook separates update architecture, reflection, cumulativity, actor allocation, and evidential limits across actual systems.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- **compares-with**: the source names Voyager as experimental RSI; the code-grounded review shows the narrower mechanism—critic-gated promotion of successful Minecraft programs into a retrieved executable skill library—and its missing faithfulness and governance evidence.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: provides a running, code-grounded case of a harness deliberately built for self-rewriting, including the protected substrate, editable executor, rebuild-and-restart path, rollback, and the point where build-and-test oracles stop warranting adoption.
- [Harness engineering for self-improvement](../../../../sources/harness-engineering-for-self-improvement.ingest.md) -- **compares-with**: replaces the source's weight- and code-rewrite-centered hypothetical with a near-term map of prompts, context, workflows, harness code, optimizer code, and joint harness-weight improvement, together with evaluator and governance limits.
- [Toward measuring recursive self-improvement](../../../../sources/toward-measuring-recursive-self-improvement-2090411367819809047.ingest.md) -- **compares-with**: supplies an explicit measurement attempt and the key limitation that one autonomous adaptation episode does not establish recursive compounding.
- [Safe superintelligence](../../../../sources/09-safe-superintelligence.ingest.md) -- **compares-with**: addresses the source's intelligence-explosion, superintelligence, alignment, and control-risk frame while insisting that boundary, objective, horizon, criteria, and limits be stated before those ideas are used for engineering or policy.
- [Darwin Gödel Machine](../../../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md) -- **compares-with**: gives an empirical self-rewriting archive in which compilation and editability gate admission while benchmark score guides reproduction, exposing a more precise evaluation/retention architecture than the source's generic validation protocol.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) -- rejected because the source does not discuss proof-governed rewrite admission; linking it directly would make a specialized formal architecture look like an explanation of the source's generic validation story. The Darwin Gödel Machine ingest preserves the useful contrast more concretely.
- [Commonplace declared frame](../../../../reference/commonplace-declared-frame.md) -- rejected because it declares the boundary for one local system rather than explaining recursive self-improvement generally.
- [Exo memory-system review](../../../../agent-memory-systems/reviews/exo.md) -- rejected because the source mentions long-term memory only as a hypothetical extension, while the whole-system Exo analysis gives the more useful self-modification and evaluation comparison without duplicating the same system.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- rejected because its bounded target-agent hardening loop is not a named example in the source and adds less than Exo to the broad RSI comparison.
- [A Poetiq Perspective on Recursive Self-Improvement](../../../../sources/poetiq-perspective-on-recursive-self-improvement.ingest.md) -- rejected as a vendor-defined same-axis neighbor whose useful compounding and actor-allocation qualifications are already represented more strongly by the measurement and theory candidates retained above.
- [On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) -- rejected because task-order variance in textual-memory agents is a distinct mechanism from the source's brief model-collapse objection; the shared “self-improving” wording is insufficient.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None.

## Flags

- **Split candidate:** the source makes independent claims about the definition of RSI, seed architecture, reported experiments, safety and alignment risks, and model collapse. A future ingest should keep those analytical threads distinct rather than treating the article as one evidential claim.
- **Terminology tension:** the source calls Voyager, STOP, self-rewarding models, and AlphaEvolve attempts at RSI while the KB's local definition and compounding test distinguish work-product optimization, bounded retained self-change, and later-episode compounding. The future ingest should preserve this disagreement explicitly.
- **Authored-surface handoff:** all outbound candidates are recommendations for the eventual `kb/sources/recursive-self-improvement.ingest.md`; they must not be added to the snapshot. No bidirectional or reverse-edge candidate can target the immutable `.snapshots/` path, and the matching ingest does not yet exist.
