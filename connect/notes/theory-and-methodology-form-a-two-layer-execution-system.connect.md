---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/theory-and-methodology-form-a-two-layer-execution-system.md"
source_has_frontmatter: true
date: "2026-07-17"
depth: standard
---

# Connection Report: Theory and methodology form a two-layer execution system

**Source:** [Theory and methodology form a two-layer execution system](../../../../notes/theory-and-methodology-form-a-two-layer-execution-system.md)

Source tags: `learning-theory`, `constraining`. Both are `kb/notes/` collection; the theoretical profile authorises the `notes` destination as the densest path, plus `evidence`/`derived-from`/`abstracted-from`/`see-also` into reference, agent-memory, agentic-systems, sources, and rare `see-also` into instructions (usual direction there is inverse `rationale`).

The source already carries 8 footer links (spec-mining, codification-and-relaxing-navigate-the-bitter-lesson, methodology-enforcement-is-constraining, constraining-and-extraction-both-trade-generality, first-principles-reasoning-selects-for-explanatory-reach, learning-is-not-only-about-generality, deploy-time-learning-is-the-missing-middle, a-derived-copy-of-recomputable-truth). Candidates below exclude those.

## Discovery Trace

**Topic indexes / curated heads:**
- `kb/notes/constraining-README.md` — read fully. Neither `constraining-README.md` nor `learning-theory-README.md` carries `complete: true`, so by-tag `rg` sweeps were run. Curated groupings flagged: "Deciding and reversing" (progressive-constraining, specification-strategy, codify-versus-llm-decision-heuristics, operational-signals-relaxing-candidate) and "Instances and techniques".
- `kb/notes/learning-theory-README.md` — read fully. `covered_by` confirms child-tag routing; "Start here" surfaced verifiability-gradient and discovery.

**Description listing scan:**
- `rg -l '^tags:.*\blearning-theory\b'` + `rg -l '^tags:.*\bconstraining\b'` over `kb/notes/`, descriptions piped. Large listings scanned for promotion/derived-copy/coverage-bet signal.

**Body search** (over notes, reference, agent-memory-systems, agentic-systems):
- `rg -i "proceduraliz"` — 0 hits. `rg -i "effective field theory"` — 0 hits. `rg -i "ACT-R|SOAR"` — 0 hits. The note's physics loans (matching/cutoff/correspondence) and cognitive-architecture terms are novel to the KB; no existing target owns them.
- `rg -i "recomputable"` — surfaced `llm-recompute-cost-inverts-the-store-vs-recompute-default`, `first-principles-are-inherited-constraints`, `prose-has-no-dereference` (plus already-linked a-derived-copy).
- `rg -i "amortiz"` — surfaced `discovery-is-seeing-the-particular-as-an-instance-of-the-general`, `reflection-may-improve-sample-efficiency`.
- `rg -i "cutoff"` — notes hits (`admitting-a-human-into-the-boundary`, `measuring-autonomy`) were the autonomy/boundary sense, not validity-cutoff; rejected.
- `rg -i "fallback"` — mostly reference/architecture and agent-memory reviews (implementation fallbacks), not the coverage-bet sense; rejected.

**Link following:**
- From `progressive-constraining` → `agentic-systems-interpret-underspecified-instructions` and `spec-mining` (already linked). From `codify-versus-llm-decision-heuristics` → `operational-signals-relaxing-candidate` (a "Deciding and reversing" cluster the source should join at its coverage-bet section).
- Reverse direction: `rg` confirmed two reference artifacts already link *to* this note via `rationale` — `kb/reference/link-vocabulary.md` (derived-from semantics) and `kb/reference/proposals/automated-note-refinement-as-search-over-source-bundle.md`.

## Connections Found

- [progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — **grounds**: the source's rule "promote on recurrence, not on first sighting" rests on the progressive-constraining discipline of committing only interpretations that consistently emerge; a reader wanting to verify the promote-on-recurrence premise goes here.
- [LLM recompute cost inverts the store-vs-recompute default](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — **grounds**: the source frames the derived methodology as a "recomputable copy" whose promotion "amortizes" under "cache economics"; this note supplies the premise that materializing a derived value pays off precisely for an LLM consumer, where in-context recompute is the expensive step. Complements the already-linked a-derived-copy note (maintenance side) with the economics side.
- [abstract an experience into a lesson only when you can state where it stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — **grounds**: the source's **cutoff** — "the validity boundary a good methodology declares for itself" — is the same requirement this note states for episodic abstraction (abstract only when you can state the boundary). A reader verifying that promotion must carry a stated cutoff finds the general boundary-discriminator here.
- [the verifiability gradient](../../../../notes/verifiability-gradient.md) — **grounds**: the source's "checkability graded by the theory's coherence" (crisp theory → near-mechanical comparison; tacit theory → loose) is the verifiability gradient applied to the generator layer; the gradient grounds why "derived" does not by itself make a prose methodology mechanically safe.
- [codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) — **extends**: the source's "coverage bet is not the correctness bet" adds a lens to the codify-vs-LLM decision; a reader wanting the fuller decision framework for whether to build the derived layer at all follows here.
- [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) — **contrasts**: the source detects a failed *coverage* bet by the **fallback rate** (artifact right but rarely applicable); this note detects a failed *correctness* bet by proxy-theory signals (artifact applicable but wrong). Neighbouring-shape distinction between the two failure detectors over a codified layer.
- [specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — **extends**: the source's promotion (compute-at-boundary, commit-on-recurrence) is the "store disambiguation after repeated observation" branch of this note's three-location taxonomy; it develops where the two-layer system's matching sits among specification strategies.

## Bidirectional Candidates

- [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) <-> source — **contrasts**: `contrasts` is symmetric and additive; the relaxing-signals note would also benefit from pointing at the fallback-rate signal as the coverage-failure sibling of its correctness-failure signals.

## Reverse-edge Candidates

- The inbound direction is already served: [kb/reference/link-vocabulary.md](../../../../reference/link-vocabulary.md) and [kb/reference/proposals/automated-note-refinement-as-search-over-source-bundle.md](../../../../reference/proposals/automated-note-refinement-as-search-over-source-bundle.md) already author `rationale`/`derived-from` links **to** this note. No new reverse edge is required for those.
- Possible new reverse edge (low confidence, for the author of that doc to decide): the review/freshness reference surface (`kb/reference/README-REVIEW-SYSTEM.md`, `kb/reference/freshness-architecture.md`) implements "stale-until-rechecked on revision" as baseline invalidation; a `rationale` link from that surface to this note would ground the invalidation semantics. Not authored here — connect does not edit those artifacts.

## Off-authorisation Candidates

None. Every kept candidate found an authorised label (`grounds`, `extends`, `contrasts`) for the `notes → notes` pair.

## Raw Text Candidates

None.

## Rejected Candidates

- [discovery is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — the recurrence-recognition tie (spotting a corner case as an instance of an already-handled pattern) is real but thin, and the reach/region axis is already covered by the linked learning-is-not-only-about-generality and first-principles-reasoning notes. Surfaced via `amortiz`; not load-bearing enough to add to an already dense footer.
- [constraining during deployment is continuous learning](../../../../notes/constraining-during-deployment-is-continuous-learning.md) — promotion-as-learning-during-use is genuine overlap, but it is already carried by the linked deploy-time-learning-is-the-missing-middle edge; adding this would duplicate the same reader-need.
- [first principles are inherited constraints, not design choices](../../../notes/first-principles-are-inherited-constraints-not-design-choices.md) — surfaced via `recomputable`, but its subject (constraint-packet inheritance) is off-axis from the theory-as-generator claim; the first-principles reach connection is already served by the linked first-principles-reasoning note.
- [prose has no reliable dereference, reinforce facts at point of use](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — surfaced via `recomputable`, but its concern (single-source-of-truth restatement in prose) is tangential to the generator/derived maintenance regime; no load-bearing label.
- [reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md) — surfaced via `amortiz`/reach; a specific statistical conjecture, too far from the two-layer execution claim to help traversal.
- `admitting-a-human-into-the-boundary...`, `measuring-autonomy...` — `cutoff` matches were the autonomy-boundary sense, unrelated to the note's validity-cutoff.

## Index Membership

None new. The source is already routed under `learning-theory` and `constraining` tag-READMEs (both would list it under "Deciding and reversing"/deploy-time-learning framing; connect does not edit indexes).

## Synthesis Opportunities

None. The note is itself the synthesis for its cluster (coverage-bet + recomputable-copy + promotion-on-recurrence); no higher-order claim is implied that it does not already state.

## Maintenance Observations

- The note's physics vocabulary (matching, cutoff, correspondence — effective field theory) and cognitive-architecture terms (proceduralization, ACT-R, SOAR) have zero other occurrences across `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`. If any of these become recurring load-bearing vocabulary, a definition under `kb/notes/definitions/` would prevent silent drift; for now they are correctly local loans, as the note itself flags.

## Flags

- The source already carries 8 outbound links and makes several independent assertions (two-layer execution, recomputable-copy maintenance, coverage-vs-correctness bet, region-as-falsifiable-hypothesis, the Batterman mixed-boundary caveat). It reads as a `synthesis`-style note but does **not** declare the `synthesis` trait; a future writer may consider whether that trait applies or whether a component claim (e.g. the coverage-bet argument) warrants extraction into its own citable note.
