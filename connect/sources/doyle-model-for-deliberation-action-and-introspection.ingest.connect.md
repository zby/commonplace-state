---
description: "Candidate comparisons for Doyle on choosing a belief revision and deciding when to stop deliberating."
type: types/connect-report.md
source: kb/sources/doyle-model-for-deliberation-action-and-introspection.ingest.md
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: A Model for Deliberation, Action, and Introspection

**Source:** [Doyle dissertation ingest](../../../../sources/doyle-model-for-deliberation-action-and-introspection.ingest.md)

## Discovery Trace

- Read the README heads for theory, reference, sources, agent-memory-systems, agentic-systems and tags. The ingest has domains but no tags, so there was no by-tag search. The tags head routes to reflection and improvement loops; sources do not participate in the heads' member listings. The original dissertation is already cited; no external prospecting.
- In each of those six collections, generated titles with `rg -N --no-filename -m1 '^# (.*)' -r '$1'` over Markdown excluding briefs. Filtered for `belief revision|truth maintenance|addressable theory|credit assignment|conflict resolution|reconsider|blame|dependency.directed|theory revision|change candidates` (case-insensitive). The theory and source hits included the already linked definition and earlier Doyle memo. The reference case study on change candidates concerns noticing and drafting, not choosing which premise to withdraw. Neither systems collection yielded a closer title match.
- Filtered each collection's `rg '^description:'` listing for `belief revision|truth maintenance|conflicting beliefs|competing repairs|fault localization` (case-insensitive); no additional hits. Searched bodies with `rg -il` for `belief revision`, `dependency-directed` and `competing revisions`. Read Hansson for his selector and the BDI survey for failure recovery. The OpenViking archive hit did not identify a comparable repair-selection policy. The BDI survey's plan retry rules address a narrower decision than Doyle's choice among revising the plan, the observation and a background assumption.
- Followed the BDI survey to Russell and Wefald: the useful comparison is not belief representation but the separate decision to spend time thinking. Followed Doyle's recommended next action to the addressable theory definition and checked its existing precedents and the theory collection's evidence rule. Its proof-trace examples already locate repair candidates; Doyle adds the distinction between a contemplated action and a completed one.

### Candidate origins

- kb/sources/in-defense-of-base-contraction.ingest.md — body-search
- kb/sources/russell-wefald-principles-of-metareasoning.ingest.md — link-following
- kb/theory/definitions/addressable-theory.md — known, titles, link-following

## Connections Found

- [Hansson on base contraction](../../../../sources/in-defense-of-base-contraction.ingest.md) — **compares-with**: When several withdrawals would remove a conflict, what chooses among them? Hansson can leave the choice to a stable background function. Doyle proposes making the choice an intention, so a policy can object to one reason for a withdrawal without defeating another. Neither account shows that its selector chooses better repairs.
- [Russell and Wefald on metareasoning](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md) — **compares-with**: Doyle §5.7 asks whether to hear another argument, commit or defer. Russell and Wefald give a stopping rule where action utilities and delay costs can be estimated: commit when no further computation has positive expected net value. This makes clear what a reader would need before replacing Doyle's policy judgment with a calculation.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Addressable theory](../../../../theory/definitions/addressable-theory.md) → [Doyle (snapshot required)](../../../../sources/doyle-model-for-deliberation-action-and-introspection.ingest.md) — **evidenced-by**: Use §6.2.1 to bound what locating a repair candidate establishes. Withdrawing a planned move can avoid a collision; withdrawing the plan after the move cannot explain the observation. The example illustrates why the choice needs context, not that Doyle's interpreter reliably found the faulty premise. The ingest currently retains no quotes.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Where change candidates come from in Commonplace](../../../../reference/case-studies/where-change-candidates-come-from-in-commonplace.md) inventories ways to notice problems and draft changes. It does not explain how to choose between incompatible repairs once both are on the table.
- [BDI agent architectures](../../../../sources/bdi-agent-architectures-a-survey.ingest.md) distinguishes retrying a plan from changing the plan library. That is useful for plan recovery but not a close comparison for choosing which belief to give up.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
