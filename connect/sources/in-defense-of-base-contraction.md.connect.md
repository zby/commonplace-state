---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/in-defense-of-base-contraction.md"
source_has_frontmatter: true
date: "2026-09-17"
depth: standard
---

# Connection Report: In Defense of Base Contraction

**Source:** [In Defense of Base Contraction](../../../../sources/.snapshots/in-defense-of-base-contraction.md)

## Discovery Trace

**Description listing scan:**
- Scoped `rg '^description:' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'` filtered for `belief|base|state|history|provenance|dependency|deriv|revision|change|memory|record|representation`. It surfaced the lineage definition, source-dependency maintenance notes, and decision-surface capture notes. Reference and external-system results described implementation state or systems rather than the paper's representational argument and were rejected.

**Topic indexes:**
- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`. The paper fits the artifact-analysis and agent-memory theory areas. No current-system reference or external-system index membership is warranted for a general 1992 belief-revision paper.

**Full title scan:**
- Ran `rg -N --no-heading -m1 '^# '` over every authorised local destination and filtered for `belief|base|state|history|provenance|dependency|deriv|revision|change|memory|record|representation`. Candidate titles about lineage, retained history, and decision-shaped capture survived; generic revision and memory-system matches did not.

**Body search:**
- `rg -n -i 'belief base|belief state|dependency information|derivation history|derivational history|closure under|logical consequence|repeated change|revision history|state-specific' ...` found no existing note on AGM/base contraction and identified `Lineage` as the closest registered concept.
- `rg -n -i 'same.*closure|same.*state|history.*state|different.*history|source dependenc|dependent.*source|basic.*derived|distill.*omit' kb/notes --glob '*.md'` surfaced the production-history, decision-surface, and derivation/commitment notes. The last was rejected because its ground-truth distinction is not the paper's belief-base distinction.

**Link following:**
- Followed links among `Lineage`, `History has one chance to become checkable`, `Bottom-up structure inference needs capture at the decision surface, not the state`, `Explicit retention provides direct targets for selective revision`, and `Commitment, not derivation, creates new ground truth`. The first three form the useful neighborhood: they explain why dependency-bearing representation changes what later updates can do. The explicit-retention note is adjacent but too broad; the commitment note uses a different authority distinction.

## Connections Found

- [Lineage](../../../../notes/definitions/lineage.md) — **is-evidence-for**: Hansson supplies a formal belief-revision case in which two bases with the same logical closure must remain distinguishable because their different dependency structure determines different later contractions.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) — **compares-with**: the paper's belief base preserves grounds that a closed belief set collapses, giving a formal analogue of the note's claim that endpoint state cannot recover unrecorded production history.
- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) — **compares-with**: Hansson's contrast between `{a}` and `{a, a or b}` shows how equivalent endpoint consequences can conceal the distinct grounds needed to choose a later update.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Lineage](../../../../notes/definitions/lineage.md) → future ingest — **is-evidence-for**: once the ingest exists, the definition could cite Hansson as a compact formal example of dependency information changing valid revision behavior even when represented consequences coincide.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Explicit retention provides direct targets for selective revision](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — both concern revision surfaces, but Hansson compares two explicit symbolic representations rather than explicit retention with other representational forms.
- [Commitment, not derivation, creates new ground truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md) — its derivation/commitment distinction assigns authority after artifact production; Hansson instead distinguishes independent grounds from logical consequences inside a belief representation.
- [Link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — shares dependency language, but its pairwise timestamp mechanism is not supported or challenged by belief-base contraction.

## Index Membership

None

## Synthesis Opportunities

- Hansson's base/set comparison, `Lineage`, and the decision-surface capture note jointly suggest a higher-order claim: representations that preserve dependency structure support selective repeated change that extensionally equivalent state summaries cannot reconstruct. This is a candidate contribution for the theory-builder refactor, not a claim established by the connection report.

## Maintenance Observations

None

## Flags

None
