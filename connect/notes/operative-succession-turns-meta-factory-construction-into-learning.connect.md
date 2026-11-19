---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/operative-succession-turns-meta-factory-construction-into-learning.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Operative succession and meta-factory learning

**Source:** [Evidence-responsive operative succession turns meta-factory construction into learning](../../../../notes/operative-succession-turns-meta-factory-construction-into-learning.md)

## Discovery Trace

**Collection rules and curated heads:**

- Read the complete source contract at `kb/notes/COLLECTION.md`. It authorises prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; it excludes `kb/work/`. It permits `external` only for already-known targets, so open-web prospecting was skipped.
- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the three matching curated heads: `foundations-README.md`, `computational-model-README.md`, and `self-improving-systems-README.md`. The tags hub is complete over tag pages, but none of the three matching tag heads declares complete membership, so all three by-tag description sweeps were run.
- Read the destination landings `kb/types/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. No authorised destination was omitted.

**Title and description listings:**

- Generated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` once for each of the seven local destinations.
- Ran `rg '^description:' kb/<destination> --glob '*.md'` for each destination.
- Ran the required note-tag listings with `rg -l '^tags:.*\b<TAG>\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` for `foundations`, `computational-model`, and `self-improving-systems`.

**Body searches:**

- `rg -l -i 'operative change|direct update|proposal-selection|fixed general machinery|deployed system' kb/notes --glob '*.md'` retained the operative-change definition, the direct-update/omitted-function distinction, the fixed-machinery Bitter Lesson argument, and the deployed-system learning boundary. The self-improving-system definition and the computational-closure notes were rejected as redundant one-hop targets because the source already links the closed-successor derivation and factory-closure definition.
- `rg -l -i 'software factor|complete version|successor factor|factory development|installed harness' kb/agentic-systems --glob '*.md'` returned only the collection landing, Compound Engineering, and Exo. The latter two survived full-text review as contrasting code-grounded boundary cases.
- `rg -l -i 'software factor|successor factor|factory development|complete version' kb/agent-memory-systems --glob '*.md'` returned no candidates. Broader `self-modif|harness|patch|promotion|operative|trace-learning` searching surfaced subsystem reviews, but none established the family-scoped production relation needed here.
- `rg -l -i 'software factor|tool factor|factory-factory|harness optimization|durable updates' kb/sources --glob '*.md'` recovered the three already-cited primary prior-art ingests plus AutoSaddler, Fluent, the partial Greenfield book preview, and secondary factory commentary. AutoSaddler and Fluent were evaluated but rejected below; the already-cited Greenfield, Cook/Kent, and MDSoFa records are not duplicate recommendations.
- `rg -l -i 'software factor|successor factor|factory development|operative succession' kb/reference --glob '*.md'`, and the same query over `kb/types` and `kb/instructions`, returned no candidates. Their complete title and description surfaces also exposed no direct trigger, so these destinations were closed without forced links.

**Link following:**

- Followed the source's existing ontology, successor, closure, reach, and repeatability links. This established that software-factory definitions, the closed-successor derivation, and domain reach are already connected and should not be proposed again.
- Followed the operative-change definition through behavioral authority and the architecture-neutral self-improving-system definition. The definition adds the missing declared-horizon and live-consumption semantics without duplicating the successor relation.
- Followed `Machinery persists by warrant...` through its computational-closure and domain-extensibility links. Its distinct contribution is the fixed-general-machinery versus family-specific-specialization burden, not closure or reach themselves.
- Followed `An omitted loop function...` through the proposal-selection and direct-update cases. It directly supports the source's claim that candidate generation, rejection, and promotion are one optional architecture rather than the definition of learning.
- Followed Compound Engineering's links to the omitted/frozen distinction and Exo, then read Exo's complete-version recursion, rebuild-and-restart, protected substrate, and oracle limits. The pair gives two nonduplicate tests of the source's boundary: product/project-knowledge compounding without installed-harness succession, and strong self-rewriting recursion without an automatically closed evidence-to-adoption path.

## Connections Found

- [Operative change](../../../../notes/definitions/operative-change.md) — **defined-in**: the source repeatedly relies on “operative” to distinguish a stored or generated factory from machinery that actually reaches later production; this definition supplies the declared horizon and live behavioral-authority path.
- [An omitted loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) — **grounds**: it establishes the architecture-neutral distinction the source uses when it permits a direct evidence-responsive update as well as reject-capable proposal selection.
- [Machinery persists by warrant, not position, in a reflective loop](../../../../notes/machinery-persists-by-warrant-not-position-in-a-reflective-loop.md) — **grounds**: it supplies the Bitter Lesson argument for why fixed general machinery may remain while task- or family-specific specialization over the claimed reach must be computationally produced.
- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) — **grounds**: it explains why learning is attributed to the behavior-producing deployed organization, letting the source specialize that wider unit to family-scoped factory machinery while excluding changes to one product alone.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — **evidenced-by**: this code-grounded case separates ordinary product and project-knowledge compounding from revision of the installed plugin harness, and shows that editability in a local-development topology still does not supply a standing evidence-to-successor path.
- [Exo](../../../../agentic-systems/reviews/exo.md) — **evidenced-by**: Exo's complete-version recursion and rewritable executor show that strong self-production or self-modification can exist while evidence, semantic acceptance, and automatic adoption remain incompletely connected—the exact non-entailment the source asserts.

## Bidirectional Candidates

- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) ↔ source — source-side **evidenced-by** and plugin-side **rests-on**: the case supplies a concrete boundary test, while the theory supplies the producer-relative product/factory and operative-succession distinctions needed to explain why project compounding is not installed-harness learning.
- [Exo](../../../../agentic-systems/reviews/exo.md) ↔ source — source-side **evidenced-by** and Exo-side **rests-on**: Exo supplies the strong-recursion countercase, while the theory separates its complete-version production relation from an evidence-responsive factory-learning relation.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A closed factory-learning transition produces a successor factory](../../../../notes/a-closed-factory-learning-transition-produces-a-successor-factory.md) — already linked from the source and therefore not a new connection.
- [Self-improving system](../../../../notes/definitions/self-improving-system.md) — its causal anatomy is relevant, but the already-linked closed-successor derivation cites it directly; another footer edge would duplicate that one-hop path.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) — the source already links the factory-specific closure definition, which in turn specializes this actor-allocation account; a direct link would add little traversal value.
- [AutoSaddler: Automatic Harness Optimization with Durable Updates](../../../../sources/autosaddler-automatic-harness-optimization-with-durable-updates.ingest.md) — a good harness-optimization case, but it does not establish a declared product family or Greenfield-style factory boundary; using it here risks turning the source's explicitly limited harness analogy into factory evidence.
- [How I built a self-improving software factory](../../../../sources/fluent-self-improving-software-factory-2081823472016335059.ingest.md) — the practitioner account uses the name directly, but its human shaping and self-reported implementation status make it weaker for this distinction than the code-grounded Compound Engineering case.
- [Software Factories book preview](../../../../sources/greenfield-short-software-factories-book-preview.ingest.md) — the partial preview supports bibliography and declared scope only; it cannot add substantive ontology beyond the already-cited primary Greenfield paper.
- [auto-harness](../../../../agent-memory-systems/reviews/auto-harness.md) — its retained trace and benchmark state is a memory-subsystem view of harness evolution, not evidence for a product-family factory or a complete operative succession path.

## Index Membership

None. The source's three existing tags make it discoverable through the relevant by-tag sweeps, while the curated heads remain intentionally selective; the more atomic closed-successor and closure notes are better head candidates.

## Synthesis Opportunities

None. The tempting higher-order synthesis—factory-valued production, harness self-modification, evidence-responsive operative succession, and domain reach as separate axes—is already the source's own contribution together with the linked domain-reach note. A new synthesis artifact would duplicate rather than combine unresolved claims.

## Maintenance Observations

- The existing footer entry for `A closed factory-learning transition produces a successor factory` uses the label `derives`, which is not in the notes collection's authorised label set. A future library edit should replace it with an authorised relation that matches the reader need, most likely `grounds`.

## Flags

- **Possible thinning rather than a new split:** the note has one coherent central distinction, but its generic-harness and reach sections overlap strongly with already-atomic linked notes. If it grows, keep the prior-art/evidence-to-operativity derivation here and shorten those two boundary sections rather than creating another synthesis note.
