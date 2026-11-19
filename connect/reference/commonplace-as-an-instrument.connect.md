---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/reference/commonplace-as-an-instrument.md"
source_has_frontmatter: true
date: "2026-07-27"
depth: standard
---

# Connection Report: Commonplace as an instrument

**Source:** [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md)

Source collection: `kb/reference/` (descriptive profile). Authorised destinations per [kb/reference/COLLECTION.md](../../../../reference/COLLECTION.md): `kb/reference/`, `kb/notes/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, `kb/instructions/`. Excluded: `kb/work/`. Not on the scan list, therefore unauthorised: `kb/articles/`.

## Discovery Trace

**Curated heads:**
- `kb/reference/README.md` — read in full. The self-reflective cluster (instrument, reflective-system, declared-frame, design-rationale-management, where-change-candidates, the two tag-readme traces) is *absent* from every section of this index. Candidates surfaced: `architecture.md`, `control-plane-goals.md`, `navigation.md` — all rejected below on topic.
- `kb/notes/foundations-README.md` (source carries `tags: [foundations]`) — read in full. No `complete: true` mark in its frontmatter, so the by-tag `rg` sweep was **not** skipped. Its "Rationale and design method" section already carries `../reference/design-rationale-management.md`; the instrument note is a sibling with no entry.
- `kb/notes/self-improving-systems-README.md` — read in full, even though the source is not tagged `self-improving-systems`, because the source's objective/evidence language is that cluster's vocabulary. Yielded `increasing-computational-autonomy-relocates-human-effort.md`, `self-improvement-is-relative-to-a-declared-objective.md`, `real-self-improving-systems-occupy-combinations-no-rung-captures.md`, `methodological-and-computational-closure-track-different-changes.md`.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` — 120 titles. Flagged `commonplace-declared-frame.md`, `where-change-candidates-come-from-in-commonplace.md`, `full-improvement-pass-closure.md`, `agent-memory-coverage.md`, `architecture.md`.
- `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` — 35 titles. No procedural counterpart to a positional/evidential statement; destination skipped after the listing (no `procedure` candidate exists).
- `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` — `exo.md` was the only near-miss (sharpest allocation comparator per the casebook). The source neither derives from nor is corroborated by Exo, so no `derived-from` / `abstracted-from` / `evidence` candidate survives; destinations skipped.

**Description listing scan:**
- `rg '^description:' kb/notes/ --glob '*.md'` — full listing (~65KB, ~430 entries) scanned. Flagged the transfer/provenance/objective cluster.
- Per-candidate `rg -m1 '^description:'` over 25 shortlisted paths in `kb/notes/` and `kb/reference/` to judge fit before opening bodies.

**Body search:**
- `rg -l -i 'transfer|reuse' kb/notes/` — 40 hits; kept `an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md`, `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` (already linked), `a-decomposition-earns-explanatory-reach-by-derivation-or-inheritance.md` (already linked).
- `rg -l -i 'provenance' kb/notes/` — 45 hits; kept `definitions/lineage.md`, `history-has-one-chance-to-become-checkable.md`, `artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` for evaluation.
- `rg -l -i 'human judg|per unit of human|not automation|leverage' kb/notes/ kb/reference/` — 26 hits; `increasing-computational-autonomy-relocates-human-effort.md` is the direct match for the source's objective sentence.
- `rg -l -i 'by intervention|intervening|counterfactual' kb/notes/` — 13 hits; `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` and `definitions/reach-assessment.md` are the two that state an intervention test.
- `rg -l -i 'self-assess|assessed by the same|independent assessor|graded its own|marking its own homework|conflict of interest' kb/notes/ kb/reference/` — 3 hits, all about oracle/automation boundaries, none about assessment independence. **No note states the "assessed by nobody outside it" claim** the source makes; recorded under Flags.
- `rg -l -i 'worked case|dogfood|self-application|eating' kb/notes/ kb/reference/` — broad hit set; the source is the only artifact using "worked case" for the KB-as-instrument framing.
- `rg -l -i 'rationale' kb/sources/ --glob '*.md'` — 20 hits; `the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md` is the only one whose own claims bear on the instrument/product distinction.
- `rg -n 'commonplace-as-an-instrument' kb/ --glob '*.md'` — **zero inbound links repo-wide.** The artifact is currently an orphan on the inbound side.

**Link following:**
- Followed the source's existing footer to `design-rationale-management.md` → its footer carries `design-proposals-differ-from-claims-in-kind-not-confidence`, `first-principles-reasoning-selects-for-explanatory-reach-over`, `progressive-constraining-commits-only-after-patterns-stabilize`. None duplicates a candidate below.
- Followed `commonplace-as-a-reflective-system.md` → its footer carries `commonplace-declared-frame.md` as `part-of` ("the canonical boundary declaration this classification is assessed under"). This is the label precedent used for candidate 1.
- Followed `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` (already linked from the source) → it already links `an-outcome-check-licenses-replay-a-rule-needs-the-process-verified.md` inline and `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` as `grounds`. Used to test one-hop redundancy: outcome-check rejected, selective-revision kept (reasons below).
- Followed `real-self-improving-systems-occupy-combinations-no-rung-captures.md` → its Commonplace row already links `commonplace-as-a-reflective-system.md` as `evidence`; its "evidential limit" cell has no artifact behind it, which is what the source supplies.

## Connections Found

- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) — **part-of**: the frame note declares boundary and partition and says explicitly that it "fixes who and what, not when"; it never declares the objective. This source states the objective ("more useful and better-warranted knowledge work per unit of human judgment spent") that every attribution in the cluster is indexed to. Same label the sibling classification already uses for the same target.
- [Increasing computational autonomy relocates human effort to the frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) — **rationale**: the source's objective sentence — "per unit of human judgment spent. Not automation" — is exactly the measure this note argues for over falling human hours. A reader asking why the objective is stated as a ratio rather than a saving needs this note. The note already cites Commonplace as an instance, so the theory-ward edge is currently missing in the direction the descriptive profile authorises.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) — **rationale**: grounds why the source's second paragraph is a load-bearing declaration rather than throat-clearing. The note separates the two conditions an objective carries (indexed by the analyst, antecedent in the pathway), which is what makes "everything here is indexed to one objective" a checkable commitment.
- [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) — **rationale**: supplies the general claim behind "rationale retained at design time, which is what gives a transfer claim an antecedent to test" and behind "later recovery depends on what an author explicitly carried forward". The note states that production history converts to later-checkable form only at production time; the source asserts the consequence for Commonplace's own mechanisms without naming the mechanism.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — **rationale**: carries both halves of the source's third honest statement — the worse-than-absent asymmetry for unfaithful rationale, and the intervention-not-inspection test the source's "faithfulness test by intervention" bullet demands. Reachable in two hops today (via `use-tests…`), but that note cites it only for the asymmetry, not for the intervention test the source's change-the-status list rests on.
- [Ingest: The Anatomy of a Design Theory (Gregor & Jones 2007)](../../../../sources/the-anatomy-of-a-design-theory-gregor-jones-2007.ingest.md) — **evidence**: independent corroboration for the source's central framing. Gregor & Jones make the expository instantiation an *additional*, non-core component — a physical implementation that represents and tests a design theory without being it — and record that "an artifact by itself remains craft knowledge if the principles are not abstracted and articulated". That is the instrument-not-product claim and the retained-rationale requirement stated from outside Commonplace. Their "justificatory knowledge" component (essential, permitted to be incomplete) is the external counterpart of the source's rationale-retention argument. Note the reference profile marks source-ward edges as uncommon; this one earns it because the source's whole position is a claim about what an instantiation licenses.

## Bidirectional Candidates

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) ↔ source — **evidence** (notes→reference): the source is the worked instance of this claim inside the repository that states it — one composition trace that licensed replay, two provenance instances, and a named list of what is still missing. The note currently reaches Commonplace only through `design-rationale-management.md`.
- [A decomposition earns explanatory-reach by derivation or inheritance](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) ↔ source — **evidence** (notes→reference): the source holds one worked instance of each of the note's two routes (representational-form as derived, reflective-system as inherited) side by side in one corpus, with the auditability claim stated for both.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) ↔ source — **contains**: the source names that doc's two open TODOs as its missing evidence; a `contains` return edge lets a reader arriving at the survey find the position that depends on those TODOs closing.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) ↔ source — **see-also**: the two are siblings over the same repository and the same trace, differing in what they assess. The source links out; nothing links back, so a reader landing on the classification cannot find the instrument reading.
- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) ↔ source — **see-also**: the frame doc's "Using the frame" section invites applications to cite it; the source is the artifact that supplies the objective parameter the frame deliberately leaves out.

## Reverse-edge Candidates

- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) → source — **evidence** (notes→reference, its own authorised set): the casebook's Commonplace row has an "evidential limit" column reading "tests and validators; human judgment" with no artifact behind that cell. The source is the artifact that states Commonplace's evidential limits explicitly, including what has *not* been demonstrated. The row currently links only `commonplace-as-a-reflective-system.md`.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) → source — **see-also** (reference→reference): that survey closes on "more of it goes unnamed here than named" and repeatedly qualifies what the single ADR-026 trace does and does not establish. The source is where that limit is stated as a position. The edge is more natural authored from the survey side than from the source.
- [Foundations](../../../../tags/foundations-README.md) → source: see Index Membership — the tag-README is a curated head, and adding the entry is the index maintainer's act, not the source's.

## Off-authorisation Candidates

- [Reflective self-improvement (article)](../../../../articles/theory-building-inside-the-system.md) — passes the articulation test: the article's outward argument runs "bootstrapping with the author inside — verification the missing half, improvement indexed to a declared objective, reach as the bar, use as the bitter-lesson test", which is the same argument the source states inward with the repository's own evidence attached. But `kb/reference/COLLECTION.md`'s outbound section does not list `kb/articles/` among the collections to scan, so no authorised label exists for `reference → articles`. Suggestion: **reject as off-scope for now** rather than extend — ADR 057 gives articles an editorial profile whose usual direction is article→KB, and the article can carry the edge under its own contract. Revisit only if a second reference→article candidate appears.

## Raw Text Candidates

None.

## Rejected Candidates

- [An outcome check licenses replay; a rule needs the process verified](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) — vocabulary match is exact ("licenses replay… does not license the rule"), but `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` — already linked from the source's footer for that very sentence — cites this note *inline in its opening paragraph* for the decomposition case. A direct second edge from the same sentence adds a hop the reader already has and is the less precise of the two.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) — the source's "vary a stated force and observe whether the decomposition's fit degrades" is the four-part negative test this definition invokes, but the source never uses the term, so `defined-in`'s reader-need ("reader may not know the term") is not triggered, and `selective-revision…` states the intervention test in the form the source actually needs.
- [Definitions: lineage](../../../../notes/definitions/lineage.md) — lineage is about invalidating and regenerating source-dependent artifacts; the source is about whether rationale supports a *transfer judgment*. Adjacent vocabulary, different operation.
- [Artifacts produced from sources need lineage recorded at the source](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) — same reason; the source's `derived-from` edges to ingests are cited as evidence of the inherited route, not as a staleness mechanism.
- [Structure inference needs capture at the decision surface](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) — close on "the why is cheap to record there and hard to recover later", but scoped to bottom-up inference from execution traces; `history-has-one-chance-to-become-checkable.md` states the same constraint at the right level of generality for a design-rationale claim.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) — already carried by both siblings (`commonplace-declared-frame.md`, `commonplace-as-a-reflective-system.md`); the source makes no allocation or closure claim of its own.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md), [A methodology governs its own extension only as far as it settles the meta-decisions it raises](../../../../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md) — governance claims about the pathway, not about what the application is for.
- [Commonplace architecture](../../../../reference/architecture.md), [Control-plane goals](../../../../reference/control-plane-goals.md), [Navigation](../../../../reference/navigation.md), [Agent memory coverage](../../../../reference/agent-memory-coverage.md), [Full improvement pass closure](../../../../reference/full-improvement-pass-closure.md) — surfaced by the reference title listing; all describe shipped machinery, while the source describes what the machinery is an instrument *for*. `full-improvement-pass-closure.md` shares the epistemic-honesty posture ("stops without claiming convergence") but shares no claim.
- [Exo](../../../../agentic-systems/reviews/exo.md) — the casebook names Exo as Commonplace's sharpest allocation comparator, but the source neither derives a design choice from Exo nor is corroborated by it, so none of `derived-from` / `abstracted-from` / `evidence` applies.
- [Definitions: actionable methodology](../../../../notes/definitions/actionable-methodology.md) — shares the Gregor & Jones ingest as an upstream, but its subject is the operator/operations/target/setting mapping, which the source does not use.

## Index Membership

- [Foundations tag-README](../../../../tags/foundations-README.md) — the source carries `tags: [foundations]` and is not listed. It belongs in the existing "Rationale and design method" section beside `../reference/design-rationale-management.md`, contributing the *position* (what the KB application is for, and what evidence would demonstrate it) that the survey's state-to-surface map serves. The README declares no `complete: true` mark, so this is a curation gap rather than a violated contract.
- [Reference README](../../../../reference/README.md) — the whole self-reflective cluster (this source, `commonplace-as-a-reflective-system.md`, `commonplace-declared-frame.md`, `design-rationale-management.md`, `where-change-candidates-come-from-in-commonplace.md`, and the two tag-readme traces) is absent from every section of the reference index. A future writer adding this source alone would still leave it undiscoverable; the real entry is a new section for the cluster. See Maintenance Observations.

## Synthesis Opportunities

- `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md` + `history-has-one-chance-to-become-checkable.md` + `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` together imply a claim none of them states: retained rationale has a *three-part* admissibility condition — it must be recorded at design time (else unrecoverable), it must be faithful (else worse than absent), and its faithfulness is testable only by intervention (else the check is what confabulation survives). The source's three honest statements are the closest thing in the repository to that composite, but it states them about Commonplace rather than as a claim. Do not author during connect.

## Maintenance Observations

- **Inbound orphan.** `rg -n 'commonplace-as-an-instrument' kb/ --glob '*.md'` returns zero matches repo-wide. The artifact is reachable only by directory listing or full-text search.
- **Cluster-level index gap, not a single missing entry.** Seven reference artifacts about Commonplace's own reflectivity, frame, rationale, and evidential position are absent from `kb/reference/README.md`. The only curated surfaces that route into the cluster today are `kb/notes/foundations-README.md` (one entry, `design-rationale-management.md`) and workshop READMEs under `kb/work/`, which the reference profile forbids linking into and which are consumed rather than durable. This is a durable navigation gap worth a maintenance step, not a connection candidate.
- **Collection-contract observation.** `kb/reference/COLLECTION.md`'s outbound section lists the collections to scan and omits `kb/articles/`, while `kb/notes/COLLECTION.md` likewise omits it. ADR 057 established the articles collection after both lists were written. Whether that omission is deliberate (articles are outward-facing terminals) or an unupdated list is worth one explicit sentence in the contract either way; today a connect run has to infer it.

## Flags

- **Unbacked claim.** The source's second honest statement — "assessed by nobody outside it" — has no theory note behind it anywhere in the KB. A search for assessment-independence language (`self-assess`, `assessed by the same`, `independent assessor`, `graded its own`, `conflict of interest`) returned only oracle/automation-boundary notes. Either the claim stands as a bare observation, or there is a missing note about why self-assessment inside the system that states a claim is a weaker warrant. Not a connection candidate; a gap.
- **Not a split candidate.** The source connects to six targets but across one topic area (what the KB application is for and what evidence would demonstrate it), and its assertions are dependent rather than independent: the composition limit motivates the rationale route, which motivates the missing-evidence list. Recorded here because the target count alone would otherwise suggest a split.
- **No tension found** between any two candidates.
