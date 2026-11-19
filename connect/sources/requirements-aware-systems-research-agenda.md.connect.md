---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/requirements-aware-systems-research-agenda.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Requirements-Aware Systems: A Research Agenda for RE for Self-Adaptive Systems

**Source:** [Requirements-Aware Systems: A Research Agenda for RE for Self-Adaptive Systems](../../../../sources/.snapshots/requirements-aware-systems-research-agenda.md)

## Discovery Trace

No semantic scores were available; all prospecting used repository-local curated heads and `rg`.

### Notes

**Description listing scan:**

- Read [the notes landing](../../../../notes/README.md). The source has no `tags:` field, so no matching tag-README was available and no tag-completeness skip applied.
- Ran the complete title scan `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (403 headings) and the complete description scan `rg '^description:' kb/notes/ --glob '*.md'` (401 entries).
- The scans retained the runtime-self-modeling, reflective-system, reflective-coverage, addressability, theory-mediated-loop, and fixed-decomposition candidates below. They rejected general requirements, runtime, and uncertainty matches that did not concern a causally connected self-model.

**Body search:**

- `rg -n -i "requirements[- ]aware|requirements reflection|run[- ]?time requirements|runtime requirements|requirements model|goal model|domain assumptions" kb/notes/ --glob '*.md'` -- found the direct structural-lineage discussion in the theory-mediated-system-learning note.
- `rg -n -i "causally connected|self-representation|introspect|reflection|reflective system" kb/notes/ --glob '*.md'` -- surfaced the definition, coverage, and addressability cluster; retained only candidates whose claims distinguish causal connection from mere stored description.
- `rg -n -i "uncertainty|multi-objective|trade[- ]?offs?|self-explanation|why not explanation" kb/notes/ --glob '*.md'` -- produced many generic matches; none added a stronger standalone candidate than the source's connection to the integrated theory-mediated and reflection notes.
- `rg -n -i "requirements|goal model|self-adapt|runtime self-model|run-time self-model|reflecti|causally connected self" kb/notes/ --glob '*.md'` -- confirmed the same cluster and exposed the fixed-decomposition boundary.

**Link following:**

- Followed the theory-mediated-system-learning note to [Reflective system](../../../../notes/definitions/reflective-system.md), [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), and its existing requirements-reflection and computational-reflection source links.
- Followed the reflective-system definition to [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) and [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md). The paper gives each of these a concrete requirements-specific comparison, but does not establish that the proposed architecture works.
- Evaluated [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md), [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md), and [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md); rejected them for the reasons recorded below.

### Reference

**Description listing scan:**

- Read [the reference landing](../../../../reference/README.md).
- Ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` (159 headings) and `rg '^description:' kb/reference/ --glob '*.md'` (158 entries).

**Body search:**

- `rg -n -i "requirements reflection|requirements-aware|run[- ]?time requirements|runtime requirements|requirements model" kb/reference/ --glob '*.md'` -- no match.
- `rg -n -i "reflective system|causally connected|self-representation|self-adapt" kb/reference/ --glob '*.md'` -- found Commonplace-specific case and provenance records, not a shipped-system analogue to this external research agenda.
- `rg -n -i "goal model|domain assumptions|multi-objective|self-explanation" kb/reference/ --glob '*.md'` -- no match.

**Link following:**

- Evaluated [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) through the reference landing and search result. It records Commonplace's current provenance and transfer boundary, so a source-side link would not help a reader understand this paper.

### Sources

**Description listing scan:**

- Read [the sources landing](../../../../sources/README.md).
- Ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` (341 headings) and `rg '^description:' kb/sources/ --glob '*.md'` (341 entries).
- The complete scans surfaced the existing requirements-reflection ingest, Maes's computational-reflection ingest, later self-adaptive-systems syntheses, and a modern runtime-contract paper.

**Body search:**

- `rg -n -i "requirements reflection|requirements-aware|requirements as runtime|runtime requirements|run-time requirements" kb/sources/ --glob '*.md'` -- retained the existing ICSE 2010 requirements-reflection ingest as the nearest comparison.
- `rg -n -i "goal model|domain assumptions|requirements model|requirements.*architecture|architecture.*requirements" kb/sources/ --glob '*.md'` -- confirmed that the existing ingest already owns nearly the same goal-model and requirements-to-architecture mechanism.
- `rg -n -i "self-adaptive systems|self-adaptation.*uncertainty|uncertainty.*self-adaptation" kb/sources/ --glob '*.md'` -- retained the later systematic review as a diachronic comparison; the broader Weyns tour was rejected as context already subsumed by the more discriminating candidates.

**Link following:**

- Read [Requirements Reflection: Requirements as Runtime Entities](../../../../sources/requirements-reflection-runtime-entities.ingest.md) fully. Its source paper is explicitly identified by the target as the initial account that this paper expands, and its links led to the same theory-mediated, coverage, addressability, and Maes cluster.
- Read [Computational Reflection](../../../../sources/maes-computational-reflection-1988.ingest.md) and [Defining Self-adaptive Systems](../../../../sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md) fully to check the general precursor and later gap assessment.
- Evaluated [Software Engineering of Self-Adaptive Systems](../../../../sources/weyns-software-engineering-self-adaptive-systems-tour.ingest.md) and [Agent Behavioral Contracts](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md); rejected both as weaker than the retained same-lineage and later-gap comparisons.

### Agent memory systems

**Description listing scan:**

- Read [the agent-memory-systems landing](../../../../agent-memory-systems/README.md).
- Ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` (175 headings) and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'` (173 entries).

**Body search:**

- `rg -n -i "requirements reflection|requirements-aware|run[- ]?time requirements|runtime requirements|requirements model|goal model" kb/agent-memory-systems/ --glob '*.md'` -- no match.
- `rg -n -i "causally connected|self-representation|reflective system|self-adapt" kb/agent-memory-systems/ --glob '*.md'` -- no match.
- `rg -n -i "uncertainty|multi-objective|self-explanation" kb/agent-memory-systems/ --glob '*.md'` -- found uncertainty handling in unrelated memory extraction and training systems only.

**Link following:**

- No candidate passed the destination trigger. [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) was the clearest search hit, but its uncertainty scores select synthetic training data; it has no runtime requirements self-model or requirements-to-architecture causal connection.

### Agentic systems

**Description listing scan:**

- Read [the agentic-systems landing](../../../../agentic-systems/README.md).
- Ran `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` (14 headings) and `rg '^description:' kb/agentic-systems/ --glob '*.md'` (12 entries).

**Body search:**

- `rg -n -i "requirements reflection|requirements-aware|run[- ]?time requirements|runtime requirements|requirements model|goal model" kb/agentic-systems/ --glob '*.md'` -- no direct match.
- `rg -n -i "causally connected|self-representation|reflective system|self-adapt|self-modif" kb/agentic-systems/ --glob '*.md'` -- retained Exo as the strongest realized reflective-system contrast.
- `rg -n -i "uncertainty|multi-objective|self-explanation|why not" kb/agentic-systems/ --glob '*.md'` -- no stronger candidate.

**Link following:**

- Read [Exo](../../../../agentic-systems/reviews/exo.md) fully. Its editable executor and rebuild/restart wire provide a concrete modern contrast to the paper's declarative requirements stratum and proposed semantic synchronization.
- Read [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) fully. Its product strategy and requirements are ordinarily target-domain knowledge rather than self-representation, so the comparison depends on a different boundary and was rejected in favor of Exo.

### External

- The target's DOI and capture URL were already present in loaded context. They are source identity and provenance, not separate connection candidates. No external prospecting or web search was performed.

## Connections Found

- [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) -- **is-evidence-for**: the paper supplies the requirements-specific structural lineage—runtime goals, assumptions, alternatives, and their proposed causal path into architecture—while its research-agenda status also supports the note's boundary that this is not empirical theory refinement or a demonstrated learning loop.
- [Reflective system](../../../../notes/definitions/reflective-system.md) -- **defined-in**: the local definition gives a reader the causal-connection, aspect-relative, and introspection/intercession distinctions needed to interpret the paper's use of “requirements reflection.”
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) -- **compares-with**: the paper's separate requirements and architecture strata, plus its unsolved semantic-synchronization obligation, are a requirements-specific instance of coverage and mapping needing to be stated separately.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) -- **compares-with**: the paper proposes human and system queries over goals, assumptions, agents, and alternatives and connects that addressability to selective adaptation and explanation, while providing no outcome evidence for the expected benefits.
- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- **compares-with**: requirements awareness supplies reflective membership, semantic interpretation, and addressable runtime objects, but the paper does not supply independent outcome read-back, empirical theory revision, or later continuation on the same path.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: the proposed runtime adaptation remains inside a designer-supplied goal language, meta-model, monitoring boundary, transformation operators, and decision procedure; the note names the limit when a needed correction falls outside that update space.
- [Requirements Reflection: Requirements as Runtime Entities](../../../../sources/requirements-reflection-runtime-entities.ingest.md) -- **compares-with**: the target explicitly presents itself as an expansion of this same-authors ICSE 2010 proposal, adding a five-part research agenda while substantially repeating the runtime-object and two-stratum architecture.
- [Computational Reflection](../../../../sources/maes-computational-reflection-1988.ingest.md) -- **compares-with**: Maes supplies the general causal-self-representation architecture that the paper specializes to requirements, including the consistency problem created by a declarative self-representation separate from implementation.
- [Defining Self-adaptive Systems: A Systematic Literature Review](../../../../sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md) -- **compares-with**: the 2010 agenda makes uncertainty and goal semantics central; the later review finds those same dimensions missing or weak in formal self-adaptive-system definitions, giving a useful diachronic check on which agenda items remained unresolved.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: both put self-representation on a causal path to runtime change, but the paper proposes a declarative requirements model synchronized with architecture whereas Exo edits its executor source and activates changes through rebuild/restart without a runtime requirements model.

## Bidirectional Candidates

None. A return edge must target the future matching ingest, not this immutable snapshot, and that ingest does not yet exist.

## Reverse-edge Candidates

None. Notes and system analyses may eventually benefit from links to the matching ingest, but durable links to `.snapshots/` are prohibited and the required authored companion path does not yet exist.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- rejected: the paper distinguishes change from uncertainty and addresses volatile environments; it does not bear on the note's narrower claim that agile “requirement change” often masks a prior interpretation error.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- rejected: requirements/architecture synchronization is a control surface, but the paper does not analyze governance operations across scheduler, context engine, and execution substrate; reflective coverage is the more exact target.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- rejected: the paper proposes monitoring and trading requirements but does not make or test the note's artifact–requirement–objective proxy distinction.
- [Software Engineering of Self-Adaptive Systems](../../../../sources/weyns-software-engineering-self-adaptive-systems-tour.ingest.md) -- rejected: its later six-wave history provides broad context, but the same-lineage predecessor and the later systematic gap review provide more discriminating comparisons.
- [Agent Behavioral Contracts](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- rejected: it enforces already specified agent constraints probabilistically; it does not maintain and revise a goal/assumption model causally synchronized with system architecture.
- [Self-Training-LLM](../../../../agent-memory-systems/reviews/Self-Training-LLM.md) -- rejected: “uncertainty” is a keyword-only match concerning training-data selection, not contextual uncertainty in a runtime requirements model.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- rejected: its product requirements ordinarily describe the target product rather than the modifying harness; Exo offers the cleaner same-boundary reflective-system comparison.
- [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) -- rejected: it records Commonplace-specific provenance and transfer evidence, not a reusable or shipped-system counterpart to the paper's requirements-aware architecture.

## Index Membership

None. The sources collection has no curated subject index for this paper, and source artifacts do not become members of the notes tag heads.

## Synthesis Opportunities

None. The higher-order relationship among requirements-level self-modeling, cross-stratum synchronization, addressability, fixed decomposition, and absent empirical read-back is already captured by the existing requirements-reflection ingest and the theory-mediated-system-learning note.

## Maintenance Observations

- The target says it expands the initial requirements-reflection proposal already represented by [Requirements Reflection: Requirements as Runtime Entities](../../../../sources/requirements-reflection-runtime-entities.ingest.md). Their core mechanism, limitations, and strongest note targets overlap substantially. A future matching ingest should state the delta explicitly—this paper's five-part research agenda and fuller uncertainty, decision-making, and self-explanation treatment—so the two source records do not compete silently for the same analytical ownership.

## Flags

- The matching authored surface `kb/sources/requirements-aware-systems-research-agenda.ingest.md` is absent. All outbound candidates above are therefore provisional recommendations for that future ingest; none licenses editing or linking to the immutable snapshot.
- The paper makes five independent research-agenda assertions. A future ingest should preserve those claim boundaries and should not convert the conceptual agenda into evidence that requirements reflection improves adaptation, trust, safety, explanation, or learning.
