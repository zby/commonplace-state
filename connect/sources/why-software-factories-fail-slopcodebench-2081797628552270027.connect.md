---
description: "Discovery report for possible KB connections from Dex Horthy's SlopCodeBench software-factory benchmark report"
type: kb/cache/types/connect-report.md
source: kb/sources/why-software-factories-fail-slopcodebench-2081797628552270027.md
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Why Software Factories Fail: Benchmarking the new frontier

**Source:** [Why Software Factories Fail: Benchmarking the new frontier](../../../sources/why-software-factories-fail-slopcodebench-2081797628552270027.md)

## Discovery Trace

**Description listing scan:**
- Read the self-improving-systems curated head and generated the full note, agentic-system, and agent-memory title surfaces. The strongest candidates were [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md), [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), and [brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md).
- Read the existing Part I and Part II ingest reports because the source explicitly continues the same series. Both were retained as comparisons rather than duplicated as new claims.

**Topic indexes:**
- Read `kb/notes/self-improving-systems-README.md`. The source is not a case of self-improvement: it evaluates repeated codebase modification but reports no retained model-, prompt-, or harness-level adaptation. It therefore should not be added as a self-improving-system placement.
- Read the source collection contract and the connect-report type. Source-side candidate labels below use only the authorised `is-evidence-for` and `compares-with` relations; reverse candidates use the notes collection's `evidenced-by` label.

**Body search:**
- `rg -n -i --glob '*.md' 'SlopCodeBench|software factor|maintain.*codebase|lights[- ]off|strict pass|deterministic feedback|quality.*oracle|proposal-selection|self-improv' kb/notes kb/sources kb/agentic-systems kb/agent-memory-systems` — confirmed the oracle, maintainability, and software-factory cluster; rejected proposal-selection as a direct match because the benchmark evaluates submitted code rather than selecting and retaining self-changes.
- `rg -N --no-heading -m1 '^# ' ... | rg -i 'oracle|maintain|benchmark|evaluation|quality|autonom|software|factory|slop|verif|code|prompt|human'` — surfaced the same three notes plus [measuring autonomy well enough to see it improve is an open problem](../../../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md); that candidate was rejected because the report does not compare autonomy profiles.

**Link following:**
- Followed the links from the two earlier Horthy ingests to their shared verification-boundary, specification, and human-review context. Part I supplies the failure diagnosis; Part II supplies the human-steering response; this source adds a benchmarked longitudinal evaluation and a proposed oracle extension.
- Followed the maintainability-oracle note's sections on synthetic futures, static proxies, and later outcomes. The benchmark is a concrete instance of the proposed repeated-change surface, but its small subset does not validate the proxy-to-maintainability link.

## Connections Found

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — **is-evidence-for**: the report gives a practitioner benchmark instance in which correctness can be checked at each checkpoint while maintainability remains only indirectly observed; strict-pass decay supports the boundary claim without proving it.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — **is-evidence-for**: SlopCodeBench combines hard held-out behavior checks, delayed accumulation across checkpoints, and soft deterministic structural metrics, making the hard/soft/delayed distinction operational.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) — **is-evidence-for**: the run instantiates the note's synthetic-futures and longitudinal-outcome surfaces and exposes the unresolved question of whether static slop metrics predict future change cost.
- [Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md) — **compares-with**: Part I argues from a failed lights-off deployment and an oracle gap; Part III adds a small empirical benchmark that tests the proposed long-horizon failure mode.
- [Why Software Factories Fail: Turning the lights back on](../../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.ingest.md) — **compares-with**: Part II restores human judgment and shortens unchecked spans; Part III asks whether a better benchmark and future verifier could eventually make that steering unnecessary.

## Bidirectional Candidates

- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) <-> source — **evidenced-by**: the note should point back to this report as a concrete, bounded test of its synthetic-futures and proxy-calibration proposals.

## Reverse-edge Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source — **evidenced-by**: add the benchmark as a practitioner case for the claim that unattended generation remains bounded by the verifier's discrimination over delayed maintainability.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) → source — **evidenced-by**: add the source as a concrete mixed-oracle example rather than treating structural metrics or strict pass as a complete maintainability oracle.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — the source has evaluation and a repeated trajectory, but no candidate self-change is selectively retained as the system's operative improvement.
- [Measuring autonomy well enough to see it improve is an open problem](../../../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — the report measures model performance and cost on a fixed benchmark, not movement of a comparable human/computational function-allocation profile.
- [Deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) — no evidence here of prompts and code co-evolving through retained deploy-time lessons; the article is about evaluation and steering, not an adaptation loop.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) — do not add as a system placement; retain as source evidence for the cluster's evaluation and governance questions only.

## Synthesis Opportunities

The benchmark, Part II's human-oracle workflow, and the maintainability-oracle note jointly suggest a sharper synthesis: longitudinal benchmarks can manufacture delayed evidence and calibrate static proxies, but they do not automatically transfer authority from human review to the benchmark. This is an extension of the existing brainstorming note, not a separate self-improvement claim.

## Maintenance Observations

- The three-part Horthy series now has a coherent source lineage in `kb/sources/`, but the current source reports do not yet cross-link all three parts from a common series surface.

## Flags

- The experiment is practitioner evidence from a three-problem subset, not a definitive benchmark result; preserve its 24%/6% strict-pass figures as context-bound.
- The source's proposed “smart model writes, smaller model maintains” transfer test is an especially useful future experiment for separating code-generation capability from maintainability.
