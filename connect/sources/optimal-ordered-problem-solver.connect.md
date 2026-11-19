---
description: "Pre-ingest discovery for OOPS: retained programs reshape later search, with bias-relative guarantees and resettable-environment limits"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/optimal-ordered-problem-solver.md"
source_has_frontmatter: true
date: "2026-09-20"
depth: standard
---

# Connection Report: Optimal Ordered Problem Solver

**Source:** [Optimal Ordered Problem Solver](../../../../sources/.snapshots/optimal-ordered-problem-solver.md)

The prospective authored surface is `kb/sources/optimal-ordered-problem-solver.ingest.md`. All edges below are candidates for that ingest or later note revisions. Never add durable links to the snapshot.

## Discovery Trace

- Read the sources collection's outbound contract and the connect-report type before discovery. Permitted destinations are notes, reference, agent-memory-systems, agentic-systems, sources, and known external sources; instructions and work are excluded.
- Read the target paper, concentrating candidate judgments on Sections 2.1, 3–4, 5.2–5.4, and 6.3–6.6. It distinguishes search allocation, successful-code freezing, and later probability modification; it reports both transfer and a task whose general solution did not benefit from earlier solutions.
- Read curated collection heads: `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`; also read `kb/notes/learning-theory-README.md`. The source has no tags, so no matching-tag completeness shortcut applied.
- Generated title surfaces with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The large combined output was truncated; focused searches below provided the bounded standard-depth follow-up rather than a claim of exhaustive recall.
- Generated description candidates with `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md' | rg -i 'search|incremental|retention|reuse|Gödel|learning strateg'`.
- Across the five destinations, ran `rg -n -i 'oops|bias.optimal|metasearch|levin|schmidhuber' ... --glob '*.md'`; this was noisy because “oops” occurs within “loops”. Refined to `rg -l -i '\bOOPS\b|bias.optimal|metasearch|\bLevin\b|Schmidhuber' ... --glob '*.md'`. This isolated the Gödel-machine ingest, the earlier learning-strategies ingest, and the incremental-self-improvement review.
- **Notes:** read the proposal-selection, accumulation, compounding, search-controller, and backtracking notes. Followed the proposal-selection note's link to accumulation, then accumulation's link to compounding. Kept the concrete retained-program dependence and state-restoration cases. Rejected the failure-explanation route because OOPS restores search state without constructing explanations of failed trials.
- **Sources:** read the Gödel-machine ingest and scoped `rg -n -i 'reset|backtrack|search|frozen'` over the learning-strategies ingest. Kept comparisons on acceptance objective and reset assumptions, rather than a broad historical-author link.
- **Agent memory systems:** read `lightweight/incremental-self-improvement.md` fully. Kept the comparison between retained instruction probabilities and frozen reusable programs, and between whole-life reward-rate evaluation and resettable task verification.
- **Agentic systems:** followed the curated head to `reviews/exo.md` and read it fully. Kept a narrow comparison of reset coverage: OOPS restores candidate-induced state, while Exo rewinds a sandbox but preserves its attempt log and cannot thereby reverse external effects.
- **Reference:** the README and title/description scans produced operational search, freshness, and review documentation. Rejected those as merely sharing the words search or retention; OOPS does not establish a fact about shipped Commonplace behavior.
- **External:** no external prospecting. The paper URL is already in the source metadata and may supply the ingest's `derived-from` citation.
- Reverse-edge rules were checked in `kb/notes/COLLECTION.md`: `evidenced-by` is authorized toward sources. Candidate paths were verified before writing.

## Connections Found

- [Accumulation counts dependence through the retained result](../../../../notes/accumulation-counts-dependence-through-the-retained-result.md) — **is-evidence-for**: OOPS's frozen earlier program supplies the instruction identities that a later prefix uses to alter suffix probabilities; retained content, not only the evidence it caused, changes later search.
- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) — **is-evidence-for**: Sections 6.5–6.6 trace a later search speedup to a previous solution's instruction content, while reporting that finding the general language solver did not benefit from its predecessors. The paper supplies a local productivity contribution, not evidence of sustained compounding.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: program search, task verification with rejection, and freezing successful code for later use are distinct operative functions in this implemented construction.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) — **is-evidence-for**: Try records and restores candidate-induced state changes, including probability changes; Section 5.2 explicitly limits the foundation when environments cannot be reset.
- [Gödel Machines](../../../../sources/goedel-machines-schmidhuber.ingest.md) — **compares-with**: OOPS budgets search relative to a program bias and verifies task solutions; a Gödel machine licenses self-rewrites by a proof of higher axiomatized utility. Section 5.4 positions OOPS as a possible proof-search component, not the same optimality claim.
- [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) — **compares-with**: the earlier design retains reward-gated distribution changes in a nonresettable life; OOPS freezes successful programs and permits temporary distribution changes during resettable search.
- [On Learning How to Learn Learning Strategies](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) — **compares-with**: compares the search-change acceptance signal and cost accounting, distinguishing payoff-per-time learning from bias-relative allocation and verification of ordered tasks.
- [Exo](../../../../agentic-systems/reviews/exo.md) — **compares-with**: both make recovery part of an improvement pathway, but OOPS requires resettable task state whereas Exo's sandbox rewind intentionally preserves the attempt record and does not establish reversibility of the whole environment.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Improvements can accumulate without compounding](../../../../notes/improvements-can-accumulate-without-compounding.md) → future tracked ingest — **evidenced-by**: a bounded historical experiment connects an earlier retained solution to a later search-cost reduction through identified instructions and their probabilities. Retain the experimental setup and absence of a sustained sequence claim.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) → future tracked ingest — **evidenced-by**: Try supplies a precise state-restoration construction and the paper explicitly names the nonresettable-environment limit. Author only after the ingest exists and its grounding path is selected.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) — backtracking and search-state updates do not amount to an explanation of failure; citing OOPS here would blur the claimed mechanism.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — plausible but redundant for this ingest: the proposal-selection and backtracking links carry the more concrete mechanisms without a broad spray of search-control links.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Bias-optimality is relative to the initial/current program bias, with checking cost included; it is not a guarantee of useful real-world transfer or fast search under a poor prior.
- The reported roughly thousandfold search acceleration is explained by the specific probability change and curriculum; do not present it as a matched multi-run benchmark or a generic KB improvement factor.
- Frozen executable programs and temporarily rewritten suffix probabilities are different retained and transient surfaces. Do not describe OOPS as simply persisting every learned distribution update.
- The paper connects across retention, search control, and historical system comparison and supports multiple assertions. It is a split candidate for any later theory extraction; retain one source ingest and scope each later note separately.
