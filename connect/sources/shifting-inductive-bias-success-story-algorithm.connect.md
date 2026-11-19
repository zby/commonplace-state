---
description: "Pre-ingest discovery for the 1997 success-story algorithm paper, emphasizing rollback, long-horizon accounting, and transfer limits"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/shifting-inductive-bias-success-story-algorithm.md"
source_has_frontmatter: true
date: "2026-09-20"
depth: standard
---

# Connection Report: Shifting Inductive Bias with Success-Story Algorithm

**Source:** [1997 paper snapshot](../../../../sources/.snapshots/shifting-inductive-bias-success-story-algorithm.md)

This is pre-ingest discovery. Outbound recommendations belong in the future matching ingest, never in the immutable snapshot. Produced by the connect worker under `cp-skill-connect/SKILL.md`; bounded repository-only discovery.

## Discovery Trace

- Read the source snapshot, source collection contract, report contract, and notes outbound contract. Read curated heads `kb/notes/README.md`, `kb/notes/learning-theory-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`; the attempted `kb/sources/README.md` read found no file. The snapshot has no tags, so no by-tag sweep applies.
- Generated the title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. Broad output exceeded the display budget, so narrowed by descriptions and body terms instead of claiming exhaustive evaluation of every title.
- Description/title query: `rg -n -i '^(description:|# ).*(reward|self.improv|levin|schmidhuber|retention|evaluation)' kb/notes kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources --glob '*.md'`. This selected the proposal-selection note, objective-relative improvement note, historical incremental-self-improvement coverage, and the preceding 1995 report ingest.
- Body query: `rg -n -i 'success.story|levin|reward acceleration' kb/notes kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources --glob '*.md'`. Sources and agent-memory-systems yielded direct historical matches. Reference and agentic-systems yielded no candidate whose reader need was stronger than the historical coverage and theory links below; no generic architecture link is recommended.
- Notes: inspected the proposal-selection note in full, the objective-relative improvement note, and the entrenchment note. Kept the first two for explicit rollback and antecedent objective mechanisms; rejected entrenchment as too distant from the paper's cheap reversible policy changes.
- Sources: inspected the 1995 learning-strategies ingest in full. Kept it as the direct predecessor comparison; its links also reveal existing oracle-strength and behavior-write governance coverage, so no new broad synthesis is needed merely to restate oracle dependence.
- Agent-memory-systems: inspected the existing Incremental Self-Improvement coverage. It currently declares the 1995 report as its reviewed version; the 1997 paper can supply supplementary evidence only if the version distinction remains explicit.
- One-hop following: the predecessor ingest led to the Incremental Self-Improvement coverage and the coverage returned to that ingest. The proposal-selection note's source neighborhood distinguishes Ashby's viability-triggered transition from separately rejectable changes; SSA supplies the latter through explicit rollback.
- External: evaluated only the paper URL already in the snapshot. No external prospecting. Excluded `kb/work/` and `kb/instructions/` from candidate discovery as required by the sources contract.

## Connections Found

- [Original paper](https://link.springer.com/content/pdf/10.1023/A:1007383707642.pdf) — **derived-from**: the future ingest analyzes this exact 1997 paper and its two SSA implementations.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **is-evidence-for**: SSA separates generating policy modifications from rejecting them by restoring saved components, and surviving changes control later action generation. Evaluation follows actualization rather than preceding every use.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) — **is-evidence-for**: the objective is explicitly long-term reward per elapsed lifetime, including learning time. SSA's retrospective success-story inequality establishes a scoped historical property, not global optimality or increasing reward in every future interval.
- [Incremental Self-Improvement](../../../../agent-memory-systems/lightweight/incremental-self-improvement.md) — **is-evidence-for**: section 4 supplies a later account of policy-generated self-modification and reward-gated rollback, while section 3 adds the distinct adaptive-Levin-search implementation. Supplementing the review requires acknowledging its current 1995 version boundary.
- [On Learning How to Learn Learning Strategies](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) — **compares-with**: compare the predecessor's self-modification architecture with the 1997 paper's general SSA wrapper, explicit success-story criterion, and separate adaptive-Levin-search experiments; retain separate source identities rather than treating them as duplicate captures.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → future matching ingest — **evidenced-by** under the notes contract: the explicit rollback mechanism offers a concrete example of reject-capable evaluation after a candidate has already become operative. Create the ingest first; a durable edge must never target this snapshot.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md): the paper's overfitting example illustrates changed-task harm, but its easily reversible numeric policy changes do not instantiate costly structural entrenchment. A generic current-fit warning would obscure the target's narrower claim.

## Index Membership

None. The immutable snapshot should not be inserted into durable navigation; the authored ingest supplies the source landing.

## Synthesis Opportunities

None. Existing coverage already owns reward-gated reversible self-modification. The distinct addition is empirical and formal detail from the 1997 paper, not a demonstrated new general theory of KB learning.

## Maintenance Observations

None

## Flags

- Preserve the separation between enforcing a retrospective inequality on surviving policy changes and establishing their causal responsibility, future superiority, convergence speed, or global optimality. The source explicitly denies general guarantees of the latter kinds.
- The evaluation trigger can be policy-dependent in the general setup; the function-learning experiment fixes evaluation after five nonzero rewards. Do not present all reported experiments as learning their own evaluation schedule.
- Learning and policy tests consume the same lifetime budget as acting. Claimed transfer gains belong to the stated task sequences and priors; the paper does not test an open-domain KB reward oracle.
- PDF-to-text ordering damages equations and tables. Any precise equation or numeric table interpretation should be checked against the PDF by the ingest writer.
