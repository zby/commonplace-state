---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/herbert-simon-architecture-of-complexity.ingest.md"
source_has_frontmatter: true
date: "2026-11-03"
depth: standard
---

# Connection Report: Ingest: The Architecture of Complexity (Simon, 1962)

**Source:** [Ingest: The Architecture of Complexity (Simon, 1962)](../../../../sources/herbert-simon-architecture-of-complexity.ingest.md)

The ingest already carries eight library footer links plus `derived-from`. This run verified them (all paths exist, all labels are authorised for their destinations) and looked for additions and reverse edges. Authorised destinations under `kb/sources/COLLECTION.md`: theory, reference, agent-memory-systems, agentic-systems, tags, sources, external. Excluded: `kb/work/`, `kb/instructions/`. No label in the table names `tags` as a destination.

## Discovery Trace

**Description and title listing scan:**
- `rg -N --no-heading -m1 '^# ' theory/ --glob '*.md' | rg -i "decompos|modul|local|atomic|granular|opac|inspect|compress|boundar|isolat|hierarch|complex|subtask|partition|bounded context|span|interface|aggregat"` flagged these candidates: dependency-locality, use-tests-a-decomposition-locally, addressability-grain, a-note-is-an-atomic-step, ad-hoc-explanation-cheap-and-local, epiplexity-by-example, feasibility-is-the-heaviest-fork, learning-inside-a-fixed-decomposition (already linked in prose), localized-retention (already linked), decomposition-heuristics (already linked), topology chain (already linked), opacity (already linked).
- `rg -N --no-heading -m1 '^# ' sources/ --glob '*.ingest.md' | rg -i "modul|decompos|hierarch|complex|alexander|conway|brooks|coupling|architecture|span of control|scaling agent"` flagged these candidates: towards-a-science-of-scaling-agent-systems, gibson-1998 locality, long-horizon-agents-levels-ticks, lane-1990, 08-simplicity-hidden-in-complexity, Parnas (already linked), Tu (already linked).
- `rg -m1 '^description:'` over the flagged files gave the description-level evaluation recorded below.

**Topic indexes:**
- `kb/tags/` listing was read. `tags/artifact-analysis-README.md` is `complete: true` and lists the opacity note, so no by-tag rg was run for it. `tags/computational-model-README.md` lists decomposition-heuristics under Scheduling & Orchestration, which confirms the existing link. The source has no `tags:` field.

**Body search:**
- `rg -n -i "herbert simon|H\. ?A\. Simon|near(ly)?[- ]decompos|bounded rationality|satisfic|watchmaker|sciences of the artificial"` over theory, reference, sources, agentic-systems, agent-memory-systems, tags, articles found Simon's *learning* definition (learning-is-not-only-about-generality, constraining-during-deployment, retained-artifacts, in-context-learning), bounded rationality (information-value-is-observer-relative, soft-bound-traditions), and a Newell–Simon mention in the Sutskever list. Near-decomposability and watchmaker have no hits outside this ingest, which confirms the ingest's claim that the concept is new to the KB.
- `rg -il "decomposab|simon"` was noisy: it mostly matched Simon Willison, Simon Peyton Jones and Simon Osindero. It did surface towards-a-science-of-scaling-agent-systems ("task decomposability") and language-model-harnesses (benchmarks chosen for decomposable structure, rejected below).
- `rg -n -i "coupling|coupled|interaction locality|local reasoning|hierarch(y|ical) "` over theory, tags and agentic-systems found evolving-understanding (interdependence), human-analogies (coupling trade-offs), open-ended-construction (coupling of object and theory, a different sense), fix-what-the-executor-cant-determine (cross-task coupling of choices), and the topology chain.
- `rg -n -i "decompos|hierarch|exponential"` over the MAKER ingest confirmed that its main result is exponential versus O(s ln s) cost under maximal decomposition.
- `rg -n -i "span|managerial|branching"` over decomposition-heuristics found no hits. This confirms the Tu-ingest gap that the source's span point targets.
- `rg -l -i "near-decompos|interaction (matrix|strength)|weakly coupled|loosely coupled|time.?scale"` over agentic-systems, agent-memory-systems and reference found only the MemoryOS review (on time-scale memory tiers). Nothing in it bears on Simon's mechanism, so those destinations were skipped.

**Link following:**
- Opacity note, "Scale" section: it says "coupling can defeat local reasoning" but states no condition. It has no Simon link. This confirms the reverse edge.
- Decomposition-heuristics: its objective list includes "Preservation of cross-item interactions needed by later synthesis" and its heuristic says "choose representations not subsets". Simon's aggregate variables are the structural case for both. This sharpens the existing footer phrase.
- Use-tests-a-decomposition-locally: it uses Parnas KWIC and argues that "inspecting the artifact cannot recover which [force-set] was operative". Simon's interaction-intensity criterion is a boundary force that *is* partly recoverable from the product, since its interaction structure can be measured. That is a real comparison axis.
- Addressability-grain: its matched read assumes the answer is "explicit in one unit". Near-decomposability is a structural condition under which that assumption approximately holds, with other units entering as aggregates.
- Information-value-is-observer-relative: it cites Simon (bounded rationality) from training data and carries a TODO to ingest real sources. This ingest's description-relative complexity point ("depends critically upon the way in which we describe it") is a sourced Simon statement adjacent to that claim.

## Connections Found

New candidates (beyond the eight existing footer links, which remain sound):

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../theory/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **compares-with**: the axis is whether a boundary's force can be recovered from the artifact. That note argues that use cannot tell which force a split answers. Simon's ε-block criterion locates boundaries by measurable interaction strength, so interaction-driven boundaries are partly recoverable from the product, while change-anticipation boundaries (Parnas, the note's example) are not. The Learning Claims point that "the partition itself is selected" also bears on the note's inherited-constraint / local-requirement / free-choice split.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../theory/addressability-grain-sets-a-matched-selective-read-floor.md) -- **compares-with**: the axis is when a one-unit read suffices. That note assumes the answer is explicit in one addressed unit. Near-decomposability is the structural condition under which this approximately holds, with neighbouring units entering only as aggregates. Its ε tolerance corresponds to that note's "required reliability". Apply this only if Extractable Value item 3 (the inspection-cost conjecture) is developed; otherwise it is optional.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) -- **is-evidence-for**: Simon's "how complex or simple a structure is depends critically upon the way in which we describe it" is sourced support for description-relative extractable structure. That note's Simon entry currently rests on training-data recall and carries a TODO to ingest sources.
- [MAKER ingest](../../../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) -- **compares-with**: the axis is decomposition against exponential sequential failure. Simon's watchmaker caps loss from *interruption* with stable subassemblies and no verification. MAKER caps loss from *wrong output* with per-step voting. The pair separates the topology contribution from the verification contribution, which is the bound the ingest's Extractable Value item 6 draws.
- [Towards a Science of Scaling Agent Systems ingest](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) -- **compares-with**: the axis is task decomposability as the determinant of coordination gains. Kim et al. measure decomposability's effect empirically without defining it structurally. Simon supplies a structural definition (strong within-block, weak cross-block interaction, with a tolerance).

Refinement of an existing link (no new edge):

- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) -- **is-evidence-for** (existing): the context phrase could also name aggregate variables as the mechanism behind that note's "choose representations not subsets" and its "preservation of cross-item interactions" objective, not only span and progress cues.

## Bidirectional Candidates

- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../theory/localized-retention-pays-where-change-is-sparse-in-a-matching.md) <-> source -- **compares-with**: the ingest says the KB names only change locality. The note's "impact closure" condition would gain a return link to the interaction-locality criterion and its short-run/long-run split.
- [Parnas 1972 ingest](../../../../sources/parnas-1972-criteria-decomposing-systems-modules.ingest.md) <-> source -- **compares-with**: source-to-source return edge on the boundary-criterion axis (anticipated change versus interaction intensity). Authorised for sources -> sources.
- [Tu hierarchical-MAS ingest](../../../../sources/xinmingtu-structured-test-time-scaling-hierarchical-mas-theory.ingest.md) <-> source -- **compares-with**: the Tu ingest's open quick-win (name managerial capacity as a branching constraint) can cite Simon's span as its precedent.

## Reverse-edge Candidates

- [Opacity depends on the inspection question and budget](../../../../theory/opacity-depends-on-the-inspection-question-and-budget.md) → source -- **evidenced-by** (theory footer vocabulary, as used by that note's existing source links): this is the primary reverse edge and matches the ingest's Recommended Next Action. Cite near-decomposability in the "Scale" section as the condition under which a local question stays affordable, with the transfer marked conjectural. Check the label against `kb/theory/COLLECTION.md` before authoring.
- [Decomposition heuristics for bounded-context scheduling](../../../../theory/decomposition-heuristics-for-bounded-context-scheduling.md) → source -- evidence for a span/branching constraint and aggregates-as-representations heuristic; label per `kb/theory/COLLECTION.md`.
- [Topology, isolation, and verification form a causal chain for reliable agent scaling](../../../../theory/topology-isolation-and-verification-form-a-causal-chain-for-reliable.md) → source -- the watchmaker is an early, verification-free precedent for the topology step and bounds how strict the chain is. Label per `kb/theory/COLLECTION.md`.
- [Information value is observer-relative](../../../../theory/information-value-is-observer-relative.md) → source -- would partially discharge that note's TODO by replacing a training-data citation of Simon with an ingested Simon text (description-relative complexity, not bounded rationality proper).

## Off-authorisation Candidates

- [artifact-analysis tag head](../../../../tags/artifact-analysis-README.md) -- the source bears on the opacity note this head lists, but no label in `kb/sources/COLLECTION.md` names `tags` as a destination, even though the outbound prose says to scan `kb/tags/`. Use the optional inline `tags:` field instead (see Index Membership) rather than a link; reject as a link.

## Raw Text Candidates

None

## Rejected Candidates

- [Dependency locality supports ordering heuristics, not a reading-cost rule](../../../../theory/dependency-locality-supports-ordering-heuristics-not-a-reading-cost.md) -- keyword match on "locality" and "reading cost". That note concerns syntactic head–dependent distance in human sentence processing, not interaction structure between subsystems. A link would conflate two senses of locality.
- [Gibson 1998 ingest](../../../../sources/gibson-1998-linguistic-complexity-locality.ingest.md) -- same reason as dependency-locality.
- [Learning is not only about generality](../../../../theory/learning-is-not-only-about-generality.md) -- this cites Simon's *learning* definition from a different work. Same author, no shared mechanism.
- [Under sub-agent decomposition, feasibility is the heaviest fork's net load](../../../../theory/feasibility-is-the-heaviest-forks-net-load.md) -- adjacent (decomposition as feasibility), but its mechanism is per-window load, not interaction structure. The aggregate point is better carried by decomposition-heuristics.
- [Evolving understanding needs holistic rewrite, not composition](../../../../theory/evolving-understanding-needs-holistic-rewrite-not-composition.md) -- the "interdependence adds coordination work" point is the non-decomposable case, but the note's claim concerns narrative rewrite. A link would be a stretch without new analysis.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- it discusses coupling trade-offs, but its claim concerns analogy-driven bundling. Simon's cross-domain analogies are a method parallel at most.
- [Epiplexity by example](../../../../theory/epiplexity-by-example-what-entropy-and-complexity-miss.md) -- observer-relative structure is adjacent to Simon's description-relativity, but information-value-is-observer-relative is the better-scoped target.
- [Long-horizon agents: levels, ticks and cascaded intelligence ingest](../../../../sources/long-horizon-agents-levels-ticks-cascaded-intelligence.ingest.md) -- levels organized by time scale resemble Simon's short-run/long-run split. However, that ingest says the campaign does not isolate the hierarchy's benefit, so a comparison would have no evidence on either side.
- language-model-harnesses-are-compositional-generalizers ingest, open-ended-construction, fix-what-the-executor-cant-determine, a-note-is-an-atomic-step, ad-hoc-explanation-cheap-and-local, lane-1990, 08-simplicity-hidden-in-complexity -- keyword-level only ("decomposable", "coupling", "complexity"). No shared mechanism was found on reading the descriptions.

## Index Membership

- Optional source tag `tags: [artifact-analysis]` -- the source's analysed contribution is a candidate mechanism for the scale source of opacity, which that head lists. The head's inclusion condition ("defines, extends, tests, or draws design consequences from the scheme or an individual field") fits only loosely, since this source proposes a mechanism without testing it. Under the sources contract, source tags are search aids and do not affect member listings. Read the head's boundary text before assigning it.

## Synthesis Opportunities

The ingest, Parnas, localized-retention and use-tests-a-decomposition-locally together imply a higher-order claim the KB does not yet state: **boundary criteria come in two kinds, change locality and interaction locality, and they differ in testability.** Interaction boundaries can be partly read off an artifact's dependency structure. Change boundaries need retained rationale. This is already flagged in Extractable Value item 4 as `[deep-dive]`.

## Maintenance Observations

- `kb/sources/COLLECTION.md` tells writers to scan `kb/tags/` for link targets, but its label table authorises no label for the `tags` destination. This is a small collection-contract gap: either add `tags` to `see-also` or drop `kb/tags/` from the scan list.
- `theory/information-value-is-observer-relative.md` carries an open TODO to replace training-data citations with ingested sources. This ingest partially serves its Simon entry.

## Flags

- Split candidate check: the ingest connects to more than five notes across three or more areas (opacity, locality/decomposition, agent-scaling topology, learning theory). It is an ingest report, not a note, so the split rule does not apply. The Learning Claims section (the theory-builder mapping) is the most separable part if a note is later written.
- Tension, not resolved: use-tests-a-decomposition-locally holds that boundary forces leave "no residue in the product". Simon's interaction criterion implies that some forces do leave a measurable residue. Both hold under different boundary criteria, which is the synthesis above.
