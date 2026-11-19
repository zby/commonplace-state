---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md"
source_has_frontmatter: true
date: "2026-07-16"
depth: standard
---

# Connection Report: Reflection may improve sample efficiency under structured shifts

**Source:** [Reflection may improve sample efficiency under structured shifts](../../../notes/reflection-may-improve-sample-efficiency-under-structured-shifts.md)

Source collection: `notes` (theoretical profile). Authorised outbound destinations and labels taken from `kb/notes/COLLECTION.md` "Outbound links": notes (`extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `defined-in`); notes/definitions (`defined-in`); reference/agent-memory/agentic-systems/sources (`evidence`, `derived-from`); + `see-also` (sparingly) to reference/agent-memory/agentic-systems/sources/instructions. Excluded: `kb/work/`. Note already carries 7 outbound edges — this report surfaces only *new* candidates.

## Discovery Trace

**Description listing scan:**
- Scoped `rg '^tags:.*\bself-improving-systems\b'` + `'^description:'` over `kb/notes/` — enumerated the whole tag cohort. Already-linked (skipped): reflection-buys-addressability, reflection-makes-retained-lessons-second-order, retrieval-failure-is-reflection-failure, warranted-autonomy-is-bounded-by-oracle-reach, a-proposal-selection-loop, definitions/self-improving-system, definitions/reflective-system. New flags: reflective-coverage-is-graded-across-representational-forms, three-independent-gradings, improving-an-agentic-system-crosses-the-prose-symbolic-boundary.
- Scoped `rg` over `foundations` tag cohort — same core cohort; no additional strong candidates beyond the self-improving-systems set.
- Broad `rg -i 'sample.efficien|transfer|distribution shift|structured shift|inductive|reach\b|generaliz|parametric|codif|representational form|amortiz|ledger|validation|falsif|conjectur|reuse|bitter lesson|explicit.*hypothes'` over `kb/notes/` — flagged codification-and-relaxing-navigate-the-bitter-lesson-boundary, learning-is-not-only-about-generality, generality-bought-to-avoid-counterexamples, and the reach/oracle cluster for evaluation below.

**Topic indexes:**
- `self-improving-systems-README.md` (`complete: true`) — source already sits at step 3 of the "why reflection might pay" chain; index membership already satisfied. Skipped by-tag rg for this tag per the `complete` mark.
- `learning-theory-README.md` + `deploy-time-learning-README.md` — source is NOT tagged learning-theory but its vocabulary (reach, generality, sample efficiency, transfer, applicability boundary) lives here. Flagged first-principles-reasoning-selects-for-explanatory-reach-over, learning-is-not-only-about-generality, abstract-an-experience-only-when-you-can-state-the-boundary, codification-and-relaxing-navigate-the-bitter-lesson-boundary.

**Body search:**
- `rg -i "sample efficien|sample-efficien"` across all authorised collections — the only *notes* hits are the source and reflection-makes-retained-lessons-second-order (already linked). Rich hits under `kb/sources/`: no-free-lunch-theorem, induction-bias-sequence-models-ebrahimi-2026, on-learning-how-to-learn, emergent-analogical-reasoning, transformers-learn-in-context-by-gradient-descent.
- `rg -i "bitter lesson"` — codification-and-relaxing-navigate-the-bitter-lesson-boundary is the KB's dedicated home for the "which side of the boundary are we on" question the source raises in its bitter-lesson paragraph; not reachable from any note the source currently links. New candidate.
- `rg -i "meta-learn|few-shot|transfer learning|inductive bias|out-of-distribution|domain generaliz"` — broad; concentrated in `kb/sources/` and `kb/agent-memory-systems/reviews/`. No new *notes* candidates.
- `rg -i "applicability condition|inductive commitment"` — only the source, abstract-an-experience-only-when-you-can-state-the-boundary, and reflection-makes-retained-lessons-second-order. Confirms the applicability-boundary tie to abstract-an-experience.
- `rg -i "deutsch|beginning of infinity"` — first-principles-reasoning-selects-for-explanatory-reach-over and learning-is-not-only-about-generality are the KB's homes for Deutsch's reach; the source cites Deutsch inline but links neither.
- Verified none of the source's eight inline arXiv citations (Schölkopf, Bengio, Ellis/DreamCoder, Gulrajani/Lopez-Paz, Rosenfeld, Yosinski, Finn, Hoffmann) are captured as `kb/sources/` snapshots — no source-side `evidence`/`derived-from` edge exists to author for them.

**Link following:**
- From first-principles-reasoning-selects-for-explanatory-reach-over → learning-is-not-only-about-generality → abstract-an-experience: a tight reach/boundary cluster the source argues within but does not join. abstract-an-experience already links `agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md` (the "reach vs local patch is open" node), which the source's conjecture directly addresses — surfaced below as a reverse-edge.
- From reflection-buys-addressability: its "Reuse and transfer" expected-advantage bullet is exactly what the source develops; source opens by citing it as grounds, but the return edge is absent — surfaced as a Bidirectional candidate.
- From induction-bias source ingest: "transformers need orders-of-magnitude more data than RNNs ... absence of step-by-step induction bias; sharing factor kappa quantifying cross-length mechanism reuse" — near-exact empirical shape of the source's directional prediction (mechanism reuse across a structured shift → fewer target observations).
- From codification-and-relaxing-navigate-the-bitter-lesson-boundary → fixed-artifacts-split-into-exact-specs-and-proxy-theories → constraining-and-distillation-both-trade-generality-for-reliability: a `learning-theory` cluster on the bitter-lesson boundary that the source engages rhetorically but never links.

## Connections Found

- [abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — **grounds**: the source treats a commitment's "stated applicability conditions" as a given property whose failure is a "failure of reach"; this note supplies the prerequisite — a commitment can carry statable applicability conditions only when its boundary/condition clause is nameable, and says what to do when it is not. A reader wanting to verify the "applicability conditions say so" premise lands here.
- [first-principles reasoning selects for explanatory reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — **grounds**: the source's central concept "reach" (a commitment operating wider than the evidence that produced it, cited to Deutsch) is defined and disciplined here as the adaptive-vs-explanatory distinction. The source's "reach is not warrant … generality is a property of what it says; warrant, of how it was checked" is the reach criterion this note operationalizes. A reader verifying the reach premise the conjecture rests on wants this.
- [codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — **contrasts**: the source's bitter-lesson paragraph stakes a claim that its "structured shifts" are distinguished from the bitter-lesson pattern because reach — naming a commitment's applicability conditions — is a *falsifiable, per-commitment* claim, not a blanket bet that captured structure stays durable. This note gives the neighbouring position: you *cannot* reliably tell which side of the bitter-lesson boundary you are on until scale tests it, so systems must stay hybrid (codify and relax). A reader wanting the distinction between "reach is a per-commitment handle on the boundary" and "the boundary is not knowable in advance" gains from holding both. Not reachable from any note the source currently links.
- [On the "Induction Bias" in Sequence Models (Ebrahimi 2026)](../../../sources/induction-bias-sequence-models-ebrahimi-2026.md) — **evidence**: a 190k-run empirical study showing transformers need orders-of-magnitude more data than RNNs for state tracking due to a missing step-by-step induction bias, with a "sharing factor kappa" quantifying cross-length mechanism reuse. This is a near-exact instance of the source's directional prediction — the right inductive bias / reused mechanism cuts target-observation requirements, and its benefit scales with reuse across the (length) shift. Strongest available KB corroboration for the "the contest lives at the level of inductive bias" and sample-efficiency clauses.
- [No Free Lunch — no universal learning algorithm](../../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.md) — **evidence**: corroborates the source's claim that "the generic bet that structure exists at all is held equally by every learner, so it is common ground neither pathway can exploit." NFL is exactly why the contest cannot be won at the generic level and must live at the specific inductive-bias level. Weaker/more foundational than the induction-bias snapshot; author only if the note wants the NFL grounding made explicit.

## Bidirectional Candidates

- [reflection buys addressability](../../../../notes/reflection-buys-addressability.md) → source — **extends**: reflection-buys-addressability lists "Reuse and transfer" as an untested expected advantage; the source is the note that sharpens exactly that affordance into a falsifiable target-data hypothesis. The source already cites it as grounds; the return edge (`extends`, this note develops the reuse-and-transfer advantage) is missing from reflection-buys-addressability's Relevant Notes and would close the loop symmetrically with reflection-makes-retained-lessons-second-order, which already carries it.

## Reverse-edge Candidates

- [trace-derived learning techniques in related systems](../../../agent-memory-systems/trace-derived-learning-techniques-in-related-systems.md) → source — the source's conjecture is the theoretical answer to the "does a mined pattern have reach or is it a recurring local patch" question this agent-memory-systems note flags as open (abstract-an-experience already cites it for that). Under `kb/agent-memory-systems/COLLECTION.md` rules a link *to* the source's sample-efficiency/reach claim may be warranted; author it from that side, not here.

## Off-authorisation Candidates

None. Every kept candidate has an authorised label for its source→destination pair.

## Raw Text Candidates

None. All candidate targets carry frontmatter.

## Rejected Candidates

- [learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) — genuinely adjacent (both refuse to collapse "generality" into a single value: the source cuts generality vs *warrant*, this note cuts generality vs the reliability/speed/cost *compound*), and both use Deutsch's reach. But the cuts are orthogonal and neither is load-bearing for the other; the reader gain over the stronger first-principles-reach link is thin. If authored, `contrasts` is the only fit. Left as a weak candidate rather than a recommended edge.
- [reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) — the source's parametric-retention discussion ("resident in the operative substrate … does not guarantee activation") is a different claim from graded coverage; the tie is topical, and the shared upstream (reflective-system, already linked) carries the needed context. Reachable in one hop from reflection-buys-addressability.
- [definitions/representational form](../../../../notes/definitions/representational-form.md) — the source's explicit-vs-parametric contrast IS the prose/symbolic vs distributed-parametric axis, so a `defined-in` is defensible; but the source never uses the term "representational form," and the vocabulary is already 1–2 hops away via reflection-buys-addressability → reflective-coverage. Adding it risks noise on an already dense note. Author only if the explicit/parametric contrast is later made a named axis in the source.
- [three independent gradings place a self-improving system](../../../notes/three-independent-gradings-place-a-self-improving-system.md) / [improving an agentic system crosses the prose-symbolic boundary](../../../notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — same-tag neighbours already threaded by the self-improving-systems README; no direct claim-level dependency with the source.
- [generality bought to avoid counterexamples is paid for in unreadability](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — adjacent to the source's "scope is not warrant" clause, but its mechanism (universality bought by widening vocabulary, paid in precision/readability) is a different claim about note-writing than the source's statistical scope-vs-warrant distinction; linking would blur two distinct uses of "generality."
- `kb/sources/on-learning-how-to-learn-learning-strategies.md`, `kb/sources/emergent-analogical-reasoning-transformers.md`, `kb/sources/transformers-learn-in-context-by-gradient-descent.md` — surfaced by the sample-efficiency/transfer body search but each corroborates a narrower or tangential sub-point (Schmidhuber meta-self-modification; analogy as vector transform; ICL-as-gradient-descent) not the source's specific inductive-commitment-reach claim. The source already cites its load-bearing external papers inline (Schölkopf, Bengio, Ellis, Gulrajani/Lopez-Paz, Rosenfeld, Yosinski, Finn, Hoffmann) as raw URLs, none of which are captured KB snapshots.

## Index Membership

- [self-improving-systems-README.md](../../../../tags/self-improving-systems-README.md) — already a member (step 3 of the "why reflection might pay" chain; `complete: true`). No action.

## Synthesis Opportunities

None. The reach/boundary/warrant cluster (source + abstract-an-experience + first-principles-reach) is already an articulated argument chain rather than an uncaptured higher-order claim.

## Maintenance Observations

- **Tag gap worth considering.** The source is tagged `foundations, self-improving-systems` but its argument is dense with `learning-theory` vocabulary (reach, generality, sample efficiency, transfer, applicability boundary) and its strongest new note candidates (first-principles-reach, abstract-an-experience, codification-and-relaxing) all live under `learning-theory`/`deploy-time-learning`. Not a connection candidate, but a maintainer may want to weigh whether a `learning-theory` tag (or a Related-Tags note) is warranted. `self-improving-systems-README` carries `complete: true`, so any tag change there must keep the mark honest.
- The source cites eight external arXiv papers as bare inline URLs (Schölkopf 2021, Bengio 2019, Ellis/DreamCoder 2020, Gulrajani/Lopez-Paz 2020, Rosenfeld et al. 2020, Yosinski 2014, Finn et al. 2017, Hoffmann et al. 2022); none are captured under `kb/sources/`. If any become load-bearing enough to warrant a snapshot, they would convert several inline citations into `evidence`/`derived-from` edges.

## Flags

- **Not a split candidate.** The note makes one governing conjecture (reflection→sample-efficiency under structured shifts) with supporting sub-claims that all serve it; it does not fragment across independent topic areas.
- **Density caution.** The note already carries 7 outbound edges and passed through a connection-inflation review gate. Three candidates (representational-form, reflective-coverage, three-gradings) were held back as one-hop-reachable rather than recommended, to keep any future edit conservative. The five Connections Found each address a specific clause the note argues but does not currently link.
- No unresolved tensions or contradictions found among candidates.
