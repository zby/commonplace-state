---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it

**Source:** [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md)

## Discovery Trace

**Authorisation and breadth:**
- Read [`kb/notes/COLLECTION.md`](../../../../notes/COLLECTION.md). It authorises prospecting `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; `kb/work/` is excluded. The source's `learning-theory`, `discovery`, and `foundations` tags and its decomposition/rationale claim made `notes`, `reference`, and `sources` the substantive passes. `agent-memory-systems`, `agentic-systems`, and `instructions` were checked for a concrete application or procedure, but no candidate passed articulation. `external` is authorised only for already-known targets; none was supplied or loaded, so external prospecting was skipped.

**Curated heads and title/description surfaces:**
- Read [`kb/notes/README.md`](../../../../notes/README.md), [`learning-theory-README.md`](../../../../tags/learning-theory-README.md), [`discovery-README.md`](../../../../tags/discovery-README.md), and [`foundations-README.md`](../../../../tags/foundations-README.md), plus each authorised destination's `README.md`. The `discovery` head has `complete: true`, so its by-tag listing was skipped; `learning-theory` declares `covered_by`, not completeness, and `foundations` has neither mark.
- Generated complete title and description surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` for all six local destinations: notes (322 titles, 319 descriptions), reference (124, 122), agent-memory-systems (171, 169), agentic-systems (8, 6), sources (403, 343), and instructions (36, 85). Tag-description scans returned 111 `learning-theory`, 14 `discovery`, and 50 `foundations` descriptions.

**Body search and evaluations:**
- `rg -n -i 'decomposition|scope claim|discriminating use|starting warrant|free choice|inheritance|derivation|rationale' kb/notes --glob '*.md'` identified the already-linked local-transfer note and the stronger unlinked candidates [First principles are inherited constraints, not design choices](../../../notes/first-principles-are-inherited-constraints-not-design-choices.md) and [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md). It also surfaced [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md), rejected because it supplies domain-specific scheduling forces rather than a warrant or test for their scope.
- `rg -n -i 'decomposition|scope claim|discriminating use|starting warrant|free choice|inheritance|derivation|rationale' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` and the focused `rg -n -i 'discriminating|refutation-capable|starting warrant|scope claim' ...` pass retained [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) and [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md). Agent-memory and agentic hits described operational scope or derived artifacts, not evidence about decomposition-scope warrant; instruction hits concerned retrieval-description discrimination, not an operationalization of this claim.
- `rg -n -i 'only derivation and inheritance warrant|discriminating use|starting warrant' ...` found existing inbound links from [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) and [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md). The latter was rejected as an additional edge: its existing outbound `extends` link already provides the more useful direction, while a return link would duplicate the local-versus-upstream validation distinction without adding a separate reader need.

**Link following:**
- Followed the source's links to [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), [Representational form](../../../../notes/definitions/representational-form.md), and [Reflective system](../../../../notes/definitions/reflective-system.md). The first already reaches the scheduling-heuristics and design-rationale material; the two definitions are the source's recorded derived and inherited instances. This left the distinction between structural inherited constraints and transferred evidential inheritance, the faithfulness precondition for targeted testing, and the shipped-system evidence boundary as independently useful candidates.
- Followed [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) to its two provenance instances and its explicit non-demonstration/faithfulness limits. Its existing inbound `rests-on` edge is useful, and the reference document also independently corroborates the source's Commonplace-specific scope caveat.

## Connections Found

- [First principles are inherited constraints, not design choices](../../../notes/first-principles-are-inherited-constraints-not-design-choices.md) -- **contrasts**: it calls a constraint inherited when it arrives inseparably with a framework boundary commitment; this source calls an ontology inherited when its discriminating source-domain evidence is transferred. The distinction prevents a reader from treating structural unavoidability as evidence that a decomposition cuts consequential boundaries.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **grounds**: the source's warning that an unfaithful rationale directs transfer tests at the wrong premise depends on this note's intervention-based account of why a plausible rationale is worse than none.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) -- **evidenced-by**: the shipped-system account records the inherited-constraint/local-requirement/free-choice distinction and documents that the repository does not enforce its continuity, corroborating the source's recorded-instance boundary without claiming an efficacy result.

## Bidirectional Candidates

- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) <-> source -- **evidenced-by**: its two auditable provenance records and explicit statement that Commonplace has not demonstrated transfer provide the concrete application and limitation of the source's two warrant grades. The reference already rests on the source; a return edge would independently serve a reader assessing the source's Commonplace-specific scope statement.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

- [Parnas (1972): On the criteria to be used in decomposing systems into modules](../../../sources/parnas-1972-criteria-decomposing-systems-modules.md) -- potential **evidenced-by**: its comparison of flowchart and information-hiding decompositions, including cross-implementation carryover and a later identified overconstraint, gives a concrete case for asking whether a borrowed criterion was tested discriminatingly. It is raw text without frontmatter, so it remains here rather than an outbound connection.

## Rejected Candidates

- [Decomposition heuristics for bounded-context scheduling](../../../../notes/decomposition-heuristics-for-bounded-context-scheduling.md) -- supplies possible forces for a scheduler split but not independent support that those forces warrant scope; the source's existing link through the local-transfer note is the more precise route.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- shares the boundary and refutation theme, but concerns abstraction of episodes into lessons rather than the provenance of a decomposition; a direct edge would be topical rather than a distinct traversal need.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- already links to this source with `extends`; the reverse candidate does not add an independent reader need.

## Index Membership

None -- the source is already curated in both the [discovery](../../../../tags/discovery-README.md) and [foundations](../../../../tags/foundations-README.md) heads.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
