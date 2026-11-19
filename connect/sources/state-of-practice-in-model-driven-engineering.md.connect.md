---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/state-of-practice-in-model-driven-engineering.md"
source_has_frontmatter: true
date: "2026-09-02"
depth: standard
---

# Connection Report: The State of Practice in Model-Driven Engineering

**Source:** [The State of Practice in Model-Driven Engineering](../../../../sources/.snapshots/state-of-practice-in-model-driven-engineering.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/notes/tags-README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`; the notes hub routed the source toward foundations, constraining, and failure modes, while the other collection heads exposed no stronger target.
- Ran `rg '^description:'` over `kb/notes`, `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, and `kb/sources`, filtered by `software factor|model-driven|factory|domain|family|codif|reuse|scale|decomposition|expert|organization`. Kept the family-scope, breadth-pressure, and historical-factory artifacts below; rejected generic codification and agent-memory matches as too remote.

**Topic indexes:**
- The snapshot has no tags. The top-level tags hub was read; no completeness-marked child index exactly covers historical software-factory evidence, so discovery continued through complete title and description surfaces.

**Full title scan:**
- Ran `rg -N --no-heading -m1 '^# '` over every authorized destination collection and filtered on `codif|constraint|domain|model|factory|automation|reuse|scale|adopt|maintain|expert|organization|artifact|decomposition`. This surfaced the software-factory ontology, universality, breadth, construction/acquisition, and modern agentic-substrate notes; only the first three receive direct empirical support from this study.

**Body search:**
- Ran `rg -n -i "software factor|model-driven|domain-specific|family-scop|universality|scale-up|ground-up|codification cost|expert bottleneck|organizational|automation"` across all authorized local destinations. This found the historical Greenfield ingests and the Santos retrospective as the closest source comparisons.
- Read the complete snapshot and inspected `a-software-factory-is-family-scoped-lifecycle-production-machinery.md`, `universal-software-factory-needs-a-declared-universality-axis.md`, `broad-software-demands-create-pressure-for-agentic-factory-development.md`, `factory-construction-does-not-establish-knowledge-acquisition.md`, and `agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md`.

**Link following:**
- Followed the family-scope note to the 2003 and 2007 Greenfield ingests, then compared their proposed ontology and economic program with this later empirical study.
- Followed the breadth-pressure note to the universality and agentic-substrate notes. The empirical narrow-domain/scale-up findings bear directly on breadth pressure and universality, but not on the stronger claim that an agentic system must acquire its own production knowledge.
- Compared the source with the Santos ingest. Santos supplies a participant account of one Microsoft strategy and successor tool; this paper supplies broader, independent industry evidence but does not identify Microsoft's institutional decision.

## Connections Found

- [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) -- **is-evidence-for**: the study finds that successful MDE practice largely used customized DSLs for narrow, well-understood domains and generated bounded parts rather than whole systems, empirically locating the practical success region of the family-scoped ontology.
- [Universal software factory needs a declared universality axis](../../../../notes/universal-software-factory-needs-a-declared-universality-axis.md) -- **is-evidence-for**: the contrast between narrow successful DSLs, diverse partial uses, and scale-up failure shows why unqualified whole-system or organizational universality claims erase the operative scope boundary.
- [Broad software demands create pressure for agentic factory development](../../../../notes/broad-software-demands-create-pressure-for-agentic-factory-development.md) -- **is-evidence-for**: the study reports that MDE fit is strongest in specific domains, struggles in generic software organizations, and often fails during organization-wide scale-up; this supports the pressure claim without establishing its proposed agentic response.
- [Mass Customizing Solutions with Software Development Factories](../../../../sources/greenfield-mass-customizing-software-factories-2007.ingest.md) -- **compares-with**: Greenfield states the broad program and family machinery; the later study finds narrower, grassroots, mixed-method practice and identifies scale-up as a common failure point.
- [I ONCE WORKED in Buenos Aires](../../../../sources/jezz-santos-i-once-worked-in-buenos-aires.ingest.md) -- **compares-with**: the participant retrospective gives project-level testimony about Microsoft, NuPattern, and Aspen, while this independent study supplies broader adoption evidence and prevents that testimony from carrying the industry-scale conclusion alone.

## Bidirectional Candidates

- [A software factory is family-scoped lifecycle production machinery](../../../../notes/a-software-factory-is-family-scoped-lifecycle-production-machinery.md) <-> source -- **is-evidence-for**: the ontology note would gain an empirical outcome source that distinguishes bounded family success from whole-system ambition.
- [Broad software demands create pressure for agentic factory development](../../../../notes/broad-software-demands-create-pressure-for-agentic-factory-development.md) <-> source -- **is-evidence-for**: its stated evidence test asks for recurring human additions and breadth costs; this study supplies partial industry evidence on domain fit and scale-up, while not testing agentic acquisition.

## Reverse-edge Candidates

- [Universal software factory needs a declared universality axis](../../../../notes/universal-software-factory-needs-a-declared-universality-axis.md) → source -- **evidenced-by**: a future edit could use the study's partial-use and scale-up findings to show that constructional scope and organizational reach are empirically distinct.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Factory construction is not evidence of production-knowledge acquisition](../../../../notes/factory-construction-does-not-establish-knowledge-acquisition.md) -- rejected because the study examines adoption and organization, not whether factory-defining knowledge was supplied or acquired computationally.
- [An agentic substrate becomes a software factory through family-specific production machinery](../../../../notes/agentic-substrate-needs-family-specific-machinery-to-be-a-factory.md) -- rejected because the paper predates agentic substrates and cannot evidence that mapping.
- [Preferential codification concentrates less predictable work at the agent boundary](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) -- rejected because the source reports domain and organizational patterns, not the note's fixed-workload selection condition.
- [Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md) -- rejected as a direct edge because it concerns 2025 lights-off coding agents and delayed maintainability oracles, a different factory lineage and causal question.

## Index Membership

None

## Synthesis Opportunities

- The Greenfield program sources, this industry study, and the Santos retrospective together support a unit-of-analysis synthesis: family-scoped techniques saw real bounded success; whole-system and organization-wide adoption was uncommon and scale-up was a recurring failure point; Microsoft's strategy and NuPattern's fate remain separate institutional/project outcomes.

## Maintenance Observations

None

## Flags

- The workshop's categorical statement that the vision failed conflates institutional retreat, project/tool discontinuation, and industry adoption. The sources support separate claims with different authority and scope.
