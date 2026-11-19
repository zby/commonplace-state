---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/articles/theory-building-inside-the-system.md"
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: Theory building inside the system

**Source:** [Theory building inside the system](../../../../articles/theory-building-inside-the-system.md)

## Discovery Trace

**Existing authored link surface:**
- `rg -n '\[[^]]+\]\(([^)]+)\)' kb/articles/theory-building-inside-the-system.md` — confirmed the article already links its Naur companion, the declared frame, Argyris/Craik source analyses, the main autonomy/formalization notes, and the two downstream companion articles on reflective theory and revision decisions. Candidate screening below excluded already-authored targets.

**Curated heads:**
- Read [kb/articles/README.md](../../../../articles/README.md) — placed the source inside the draft sequence with `what-bound-naurs-theory-to-programmers`, `theory-building-inside-the-system`, `when-systems-learn-theories-about-themselves`, and `continual-learning-outside-the-weights`; flagged the last as the one distinct companion article not yet linked from the source.
- Read [kb/notes/README.md](../../../../notes/README.md) — confirmed notes are the theory fallback surface for deeper mechanism, definition, and boundary links.
- Read [kb/reference/README.md](../../../../reference/README.md) — confirmed reference is for shipped-system detail and operative traces; the source already uses the declared frame and ADR 080 for its two strongest Commonplace-specific needs.
- Read [kb/sources/README.md](../../../../sources/README.md) — confirmed ingests are the authored surface for external-source analysis, not a place to add extra topical parallels without a concrete attribution need.
- Read [kb/agent-memory-systems/README.md](../../../../agent-memory-systems/README.md) and [kb/agentic-systems/README.md](../../../../agentic-systems/README.md) — confirmed these collections are for explicit system comparison or system-specific descriptive evidence.
- Read [kb/instructions/README.md](../../../../instructions/README.md) — confirmed instructions are reusable procedures, suitable only if the article leaves the reader with a concrete operational next step.
- `kb/tasks/README.md` is absent and `test -f kb/tasks/COLLECTION.md` returned `no`; task prospecting therefore had no curated head or local contract.

**Notes prospecting:**
- Title surface: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — surfaced `Skills derive from methodology`, `Warranted autonomy is bounded by oracle domain`, `Theory-mediated self-improvement needs both interpretation and retention from one substrate`, `The deployed system, not the model alone, is the unit of learning`, and `Attempted recovery identifies informational gaps, not provenance or authority`.
- Description listing: `rg '^description:' kb/notes/ --glob '*.md' | rg 'theory|learn|formal|verification|autonomy|judg|behavior|maintain|reflect|methodolog|codif|context|artifact|admit|derive|validator'` — kept `skills-derive-from-methodology` and `warranted-autonomy-is-bounded-by-oracle-domain` as direct missing supports; opened `theory-mediated-self-improvement-needs-interpretation-and-retention`, `the-deployed-system-not-the-model-is-the-unit-of-learning`, `documentation-generates-the-system-rather-than-describing-it`, and `commitment-not-derivation-creates-new-ground-truth` for articulation testing.
- Body search: `rg -n 'theory|theory-mediated|behavioral authority|coherent|formal model|verification|admit|maintainer|interpreter|reflective|self-improving|validator|methodology' kb/notes/ --glob '*.md'` — confirmed:
  - `skills-derive-from-methodology` explains why procedures and validators count as derived consequences of retained theory.
  - `warranted-autonomy-is-bounded-by-oracle-domain` sharpens the closure/warrant distinction behind the article's "allocation is not a disposition" warning.
  - `theory-mediated-self-improvement-needs-interpretation-and-retention` is a real continuation, but the source already points readers to the outward-facing article that carries that case.
  - `the-deployed-system-not-the-model-is-the-unit-of-learning` overlaps strongly with the article-to-article continuation in `continual-learning-outside-the-weights`.
  - `documentation-generates-the-system-rather-than-describing-it` is a poor fit: its actual claim is about recoverability, provenance, and authority, not about operative retained theory in this article's sense.
- Link following: opened [skills-derive-from-methodology](../../../../notes/skills-derive-from-methodology.md), [warranted-autonomy-is-bounded-by-oracle-domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), [theory-mediated-self-improvement-needs-interpretation-and-retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), [the-deployed-system-not-the-model-is-the-unit-of-learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md), and [commitment-not-derivation-creates-new-ground-truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md); kept the first two and rejected the rest as either weaker than an already-linked companion article or too implementation-internal for the article reader's onward need.

**Reference prospecting:**
- Title surface: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`
- Description listing: `rg '^description:' kb/reference/ --glob '*.md' | rg 'theory|improvement|review|validator|change|reflect|frame|article|automation|verification|methodology|gate|admit|revision'`
- Body search: `rg -n 'theory|revision|maintainer|validator|full pass|review gate|reflective|self-improving|verification|automation|article|frame' kb/reference/ --glob '*.md'`
- Followed [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) because the source notes that future profiles could hide reallocation in "noticing"; rejected it because the article currently keeps that function explicitly untraced and the extra Commonplace-specific machinery would interrupt rather than clarify the external-reader path. No stronger missing reference target surfaced beyond the already-authored frame and ADR links.

**Articles prospecting:**
- Title and description surface: `rg -N --no-heading -m1 '^# ' kb/articles/ --glob '*.md'` and `rg '^description:' kb/articles/ --glob '*.md'`
- Body search: `rg -n 'theory|revision|self-improving|reflective|maintainer|interpreter|formal|learning|automation|verification' kb/articles/ kb/sources/ kb/agentic-systems/ kb/agent-memory-systems/ kb/instructions/ kb/tasks/ --glob '*.md'`
- Kept [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md): it is the only missing reader-facing companion that develops the same fixed-interpreter/artifact-layer premise in a different direction.
- Rejected `what-bound-naurs-theory-to-programmers`, `when-systems-learn-theories-about-themselves`, and `moving-revision-decisions-into-the-automatic-system` because all three are already linked in the source.
- Rejected `the-bitter-lesson-does-not-require-everything-to-live-in-weights` because it would widen the argument toward production-method strategy earlier than the source currently wants.

**Sources prospecting:**
- Title surface: `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md' > /tmp/theory-building-sources-titles.txt && rg 'Naur|Craik|Argyris|theory|learning|reflective|revision|verification|automation' /tmp/theory-building-sources-titles.txt`
- Description listing: `rg '^description:' kb/sources/ --glob '*.md' | rg 'theory|learning|reflective|revision|verification|automation|model|maintainer|interpreter'`
- The strongest surfaced ingests (`programming-as-theory-building`, `argyris-organizational-learning-and-mis-1977`, `craik-hypothesis-on-the-nature-of-thought-1943`, `sutton-javed-why-ai-models-stop-learning`, `ironies-of-automation`, `model-types-levels-human-interaction-automation`) either are already linked or would widen the article into fresh external debates rather than support a specific missing sentence. Kept none.

**Agentic-systems and agent-memory-systems prospecting:**
- Agentic titles/descriptions: `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ --glob '*.md'`
- Agent-memory titles/descriptions: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md' | rg 'reflective|self-improving|theory|learning|memory|review|comparison|trace'` and `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg 'reflective|self-improving|theory|learning|memory|review|comparison|trace'`
- Opened the possibility of `Exo` as a `compares-with` target because it is a running reflective self-improvement harness, but rejected it: the source article does not yet compare systems on a named axis, and importing one external system case here would interrupt the article's current within-Commonplace allocation argument.
- No agent-memory-system target met the article collection's trigger; the source is not choosing among memory systems or comparing them on a named axis.

**Instructions and tasks prospecting:**
- Titles/descriptions: `rg -N --no-heading -m1 '^# ' kb/instructions/ kb/tasks/ --glob '*.md'` and `rg '^description:' kb/instructions/ kb/tasks/ --glob '*.md' | rg 'article|review|theory|learning|revision|publication|explanatory|task'`
- `publish-an-article.md` was the only plausible instruction hit, but rejected it because the article's audience is an external technical reader, not an author ready to run the publication procedure.
- No task artifact serves as a durable onward path for the current draft's closing; task hits are maintenance records rather than reader-facing next steps.

## Connections Found

- [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) -- **extends**: carries the same fixed-interpreter/artifact-layer premise into the larger question of whether learning can live outside weights, giving the reader the missing companion continuation from this article's argument about operative retained theory and function allocation.
- [Skills derive from methodology](../../../../notes/skills-derive-from-methodology.md) -- **extends**: gives the fuller theoretical argument behind the table's "derive consequences: procedures, validators" row by showing why skill production counts as theory-derived consequence rather than mere prompting or generic constraining.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **extends**: sharpens the article's caution that one computational episode does not establish closure by separating bare computational assignment from warranted autonomous evaluation.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) -- source-note lineage made it an obvious check, but its actual claim is about recoverability/provenance/authority between artifacts, not about operative retained theory or theory-building allocation.
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- strong topical overlap, but the source already gives readers a cleaner onward path through the companion article [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md); a direct note link would duplicate that route.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- real substrate overlap, but [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) is the better outward-facing continuation for this article's audience.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- useful operative detail on noticing channels, but the article currently marks that function as untraced/human at its chosen evidence grain; adding this internal machinery here would overfit implementation detail rather than help traversal.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- plausible `compares-with` target on reflective self-improvement, but the source does not yet compare systems on a named axis, so the link would import a comparison the article has not prepared.
- [Publish an article](../../../../instructions/publish-an-article.md) -- authorised `procedure` destination, but the source does not end by handing the reader a concrete authoring step; this would switch from reader-facing argument to repo-maintainer workflow.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

- `kb/articles/COLLECTION.md` authorises `kb/tasks/` as a destination for concrete next-step links, but `kb/tasks/` currently has neither a `README.md` curated head nor a `COLLECTION.md` contract. That leaves article-to-task prospecting without the normal collection guidance and is a durable routing-surface gap if task links are meant to stay authorised from articles.

## Flags

None
