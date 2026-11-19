---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/concept-bottleneck-models.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: Concept Bottleneck Models

**Source:** [Concept Bottleneck Models](../../sources/concept-bottleneck-models.md)

The source is a **snapshot** under `kb/sources/`, which `kb/sources/COLLECTION.md` declares immutable. No `.ingest.md` companion exists yet (`kb/sources/concept-bottleneck-models.ingest.md` is absent), so every entry under `Connections Found` is a recommendation for that future ingest report, and `Reverse-edge Candidates` carries the primary authoring signal the collection contract names for snapshots.

## Discovery Trace

**Collection contract read first:**
- `kb/sources/COLLECTION.md` — outbound section "Outbound links". Authorised destinations for a source's authored surface: `notes` (`evidence`, `abstracted-from`, `rationale`), `notes/definitions` (`defined-in`), `sources` / `agent-memory` / `agentic-systems` (`compares-with`), any (`see-also`, sparingly). Excluded: `kb/work/` and `kb/instructions/`. Explicit direction hint: "Running connect on a snapshot still works … the report's authoring signal is reverse-edge — which library notes (typically in `kb/notes/`) should add `evidence` or `abstracted-from` links pointing at this snapshot." Reverse-edge prospecting was therefore run as a first-class pass.
- `kb/notes/COLLECTION.md` outbound table read to state reverse-edge labels under the *destination's own* rules (`evidence`, `derived-from`, `abstracted-from`, `see-also` are the labels notes may aim at `kb/sources/`).

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — complete claim-title surface for `kb/notes/` (~450 titles). Filtered against the source's foregrounded terms: `oversight`, `faithful`, `rationale`, `interpret`, `legible`, `transparen`, `human `, `intervene`, `intervention`, `bottleneck`, `concept`, `intermediate`, `inspect`, `audit`. Title-level hits: `inspectable-artifact-not-supervision-defeats-the-blackbox-problem`, `reflection-may-lower-oversight-cost-when-its-rationale-is-faithful`. Zero title hits for `bottleneck` in the interpretability sense, `intervention`, `legible`, `transparen` — the source's own vocabulary is not the KB's, so body search carried most of the recall.
- `rg -N --no-heading -m1 '^# ' kb/notes/definitions/ --glob '*.md'` — 21 definitions listed; `representational-form`, `reflective-system`, `reach-assessment`, `retained-artifact` flagged as vocabulary the ingest would need.
- `rg -N --no-heading -m1 '^# ' kb/sources/ -g '*.md'` filtered on `interpret|faith|explan|causal|concept|reason|transparen|attribut|probe` — surfaced the three `compares-with` candidates below.

**Topic indexes:**
- `kb/notes/observability-README.md` — read in full. Its "Inspectable Artifact" section is a one-entry section pointing at `inspectable-artifact-not-supervision-defeats-the-blackbox-problem`; its "Related Tags" routed to `learning-theory` and `computational-model`. No `complete:` mark, so the by-tag `rg` was not skipped.
- `kb/notes/learning-theory-README.md` — carries `covered_by: [deploy-time-learning, constraining, discovery, artifact-analysis, agent-memory, llm-interpretation-errors]` and no `complete:` mark; typed routing trusted, by-tag sweep still run through the body searches below.
- `kb/notes/tags-README.md` family listed (`ls kb/notes/*README*.md`) — 22 tag READMEs; `observability`, `learning-theory`, `self-improving-systems`, `foundations` judged the only plausible landing tags for an ML-architecture interpretability paper. No `complete:` marks found on the four checked.
- `kb/sources/README.md` — read; the collection has no curated per-source index a snapshot would be added to.

**Body search** (actual queries, over `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`):
- `rg -il "concept bottleneck"` — **zero hits** anywhere. The paper's own name is not yet in the KB.
- `rg -il "Koh"` — one hit: `kb/notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md:46`. Inspected: the note already cites this exact paper by bare arXiv URL (`[Koh et al. 2020](https://arxiv.org/abs/2007.04612)`) as its counterexample to purely-parametric opacity. Highest-value finding of the run.
- `rg -in "ROME|Meng|model editing|semantically addressable|semantically targeted|intervene|intervention"` — surfaced `reflection-makes-retained-lessons-second-order.md` (parametric pathways and model editing), `definitions/reach-assessment.md` (intervention semantics), `world-models-assess-explanatory-reach-through-action-conditioned.md`, and the same `reach-assessed-commitments` line.
- `rg -il "blackbox"` — 10 hits; kept `inspectable-artifact-…`, `opacity-is-a-scale-threshold`, `observability-README`. Rejected `spec-mining-as-codification`, `axes-of-artifact-analysis`, `runtime-structure-determines-governance-control-surfaces`, `the-four-field-record-…`, `underspecification-and-indeterminism-…`, `agent-runtimes-decompose-…`, `adversarial-loop-…` as keyword-only.
- `rg -il "interpretab"` — 8 hits; kept `reflection-buys-addressability`, `reflection-may-lower-oversight-cost-when-its-rationale-is-faithful`, `only-explicit-retention-is-durable-writable-and-addressable`, `opacity-is-a-scale-threshold`. Rejected `theory-and-methodology-form-a-two-layer-execution-system`, `collections-never-own-frontmatter-semantics`, and the two agent-memory reviews (`ace.md`, `AI-Context-OS.md` — "interpretable" there means a hand-written heuristic score, an unrelated sense).
- `rg -il "retrain"` and `rg -il "test-time"` — surfaced `constraining-during-deployment-is-continuous-learning`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning`, `continual-learning-open-problem-is-behaviour-not-knowledge`, `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md`, `KBLaM.md`. Evaluated and rejected — see `Rejected Candidates`; CBM's "no retraining" is per-inference correction, not durable deploy-time retention, so the shared word does not carry a shared claim.
- `rg -in "interpretab" kb/agent-memory-systems/ kb/agentic-systems/` — 2 hits, both the unrelated sense above. No external-system candidate found in either collection.

**Link following:**
- From `inspectable-artifact-…` one hop: `definitions/representational-form.md`, `definitions/codification.md`, `verifiability-gradient.md`, `opacity-is-a-scale-threshold.md` (its `tempers` edge back). `opacity-is-a-scale-threshold` proved the sharper landing — it already argues opacity is a scale threshold set by structural affordances, which is what a concept layer supplies.
- From `reflection-buys-addressability` one hop: `only-explicit-retention-is-durable-writable-and-addressable.md`, `reflective-coverage-is-graded-across-representational-forms.md`, `retrieval-failure-is-reflection-failure.md`. This is the densest cluster for the source: `only-explicit-retention` names its own falsifier as tacit-form addressability, and `reflection-buys-addressability` carries an open question about exactly this.
- From `reflection-may-lower-oversight-cost-…` footer: `../sources/towards-faithfully-interpretable-nlp-systems.ingest.md` and `../sources/language-models-dont-always-say-what-they-think.ingest.md` — both already-ingested interpretability sources, giving the `compares-with` neighbourhood.
- From `kb/sources/towards-causal-representation-learning.ingest.md`: its summary names "the hard problem of discovering causal variables from low-level observations" — the problem CBM sidesteps by supervising the variables directly.

## Connections Found

Recommendations for the future `kb/sources/concept-bottleneck-models.ingest.md`, which will carry this snapshot's authored surface.

- [Reach-assessed commitments may cut target observations under structured shifts](../../notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md) — **evidence**: the note already leans on this paper (external URL, line 46) for its claim that "neural computation is compatible with semantically targeted intervention once an interface or architecture supplies one"; the ingest should be the local anchor that citation resolves to.
- [Only explicit retention is currently durable, writable, and addressable at once](../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — **evidence**: the note names its own falsifier as "addressability of a tacit form — interpretability-grade editing under which a weight-encoded commitment can be individually retrieved, criticized, and revised"; a concept bottleneck is an architecture-supplied partial instance (individual concepts retrievable and correctable), so the ingest should record how far it goes and where it stops short of the falsifier.
- [Reflection may lower oversight cost when its rationale is faithful](../../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md) — **evidence**: the note's condition is faithfulness rather than legibility, and its cited evidence is all failure-side (Turpin, Jacovi and Goldberg); CBM supplies the constructive side — an architecture where the exposed rationale is load-bearing by construction, and where intervening on a concept demonstrably moves the downstream prediction.
- [Reflection buys addressability](../../notes/reflection-buys-addressability.md) — **evidence**: the note's Open Questions ask "whether external interpretability tooling inside a declared boundary can make parametric retention addressable"; CBM answers a neighbouring version of that question from the architecture side rather than the tooling side, and bears on the "indirect handles" claim.
- [Reflective coverage is graded across representational forms](../../notes/reflective-coverage-is-graded-across-representational-forms.md) — **evidence**: the note's per-form verification obligation is "probe parametric ones behaviorally"; concept-level intervention is a probe with an addressable target, so the source is data on whether a parametric component can be graded above selection-only.
- [Opacity is a scale threshold, not a class property](../../notes/opacity-is-a-scale-threshold.md) — **evidence**: the note's closing question is "how much scale a form's structural affordances buy you before inspection breaks down"; a supervised concept layer is a deliberate structural affordance added to a distributed-parametric model, and its concept-count is exactly a threshold measurement.
- [Representational form](../../notes/definitions/representational-form.md) — **defined-in**: the ingest will need the prose / symbolic / distributed-parametric vocabulary to state precisely what CBM changes — the concept layer is a named-and-readable interface over an artifact whose form stays distributed-parametric.
- [Towards Causal Representation Learning](../../sources/towards-causal-representation-learning.md) — **compares-with**: CRL frames discovering high-level causal variables from low-level observations as the hard open problem; CBM takes the same variables as *given* via concept supervision, so the two are the unsupervised and supervised ends of one problem already in the KB.
- [Towards Faithfully Interpretable NLP Systems](../../sources/towards-faithfully-interpretable-nlp-systems.md) — **compares-with**: Jacovi and Goldberg define and grade faithfulness for post-hoc explanations; CBM is the architecture-level alternative that makes the explanation causally load-bearing instead of evaluating one after the fact.
- [Language Models Don't Always Say What They Think](../../sources/language-models-dont-always-say-what-they-think.md) — **compares-with**: Turpin et al. use controlled interventions to show a fluent explanation can omit the feature that moved the answer; CBM uses the same intervention move constructively, as a correction channel rather than as a diagnostic of unfaithfulness.

## Bidirectional Candidates

None. The snapshot is immutable and cannot author return links; the return direction for every entry above is covered under `Reverse-edge Candidates`.

## Reverse-edge Candidates

The primary authoring signal for a snapshot, per `kb/sources/COLLECTION.md`. Labels below are the ones the *destination* note may use toward `kb/sources/` under `kb/notes/COLLECTION.md`.

- [Reach-assessed commitments may cut target observations under structured shifts](../../notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md) → source — **evidence**: line 46 already cites `https://arxiv.org/abs/2007.04612` as a bare external URL. The paper is now snapshotted locally, so the note can cite the local capture (or its ingest once written) instead of relying on arXiv resolving. Note is currently untracked in git, so this is cheap to fold into its first commit.
- [Only explicit retention is currently durable, writable, and addressable at once](../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) → source — **evidence**: the "Open Questions" entry asking whether behavioral probing and activation steering "constitute a graded middle — partial addressability worth naming" has a concrete instance in this paper; the falsifier clause in "The claim is current, and its falsifier is named" is the natural anchor point.
- [Reflection may lower oversight cost when its rationale is faithful](../../notes/reflection-may-lower-oversight-cost-when-its-rationale-is-faithful.md) → source — **evidence**: the note's footer already carries two interpretability sources on the failure side; this one balances the citation set with an architecture where faithfulness is designed in and testable by intervention.
- [Reflection buys addressability](../../notes/reflection-buys-addressability.md) → source — **evidence**: for the Open Questions line on interpretability tooling making parametric retention addressable to the improving system itself.
- [Opacity is a scale threshold, not a class property](../../notes/opacity-is-a-scale-threshold.md) → source — **abstracted-from**: if the note is ever extended to say *how* structural affordances are added rather than only that they set the threshold, CBM is the worked case it would generalize past.

## Off-authorisation Candidates

- [Inspectable artifact, not supervision, defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — passes the articulation test: the note's load-bearing line is "You can write a test for a function. You can't write a test for a weight," and CBM is precisely a construction where you *can* write a test for an intermediate of a weight-based model, so the note's categorical framing needs qualifying. But the relation is *qualification*, not corroboration — `evidence` ("this source corroborates the claim") misstates it, and `see-also` would understate a real tension. `kb/sources/COLLECTION.md` authorises no tempering or contrasting label for `sources → notes`. Suggestion: extend the source label set with a `tempers` or `contrasts` entry for the `notes` destination (`kb/notes/COLLECTION.md` already has `contrasts`/`contradicts` for note→note, and `opacity-is-a-scale-threshold.md` already uses an unregistered `tempers` label toward this same note), or reject as a claim the ingest should state in prose without a labelled edge.
- [Commonplace as a reflective self-improving system](../../reference/commonplace-as-a-reflective-system.md) — passes the articulation test: it records the selection-only profile line over the parametric form that CBM shows is not the only available grade. But `sources → reference` is authorised only for `see-also`, which is too weak for what is really evidence bearing on a recorded profile decision. Suggestion: leave the edge unauthored and let the note-side edges above carry it, rather than extending the source label set for a single case.

## Raw Text Candidates

None. Every candidate carries frontmatter.

## Rejected Candidates

- [Constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md) — matched on `retrain`, but the note's claim is about durable symbolic artifacts accumulating adaptive capacity; a CBM concept intervention is per-inference and leaves nothing retained, so the shared "without retraining" phrasing is a false cognate.
- [Readable artifact loop is the tractable unit for continual learning](../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) — same `retrain` match, same reason. CBM adds no readable artifact that survives the inference.
- [Continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) — keyword-only; the paper makes no continual-learning claim.
- [The verifiability gradient](../../notes/verifiability-gradient.md) — reached by one hop from `inspectable-artifact-…`, but the gradient ranks symbolic artifacts by verification tightness; a concept layer is not a symbolic artifact on that gradient, and forcing it there would blur the form distinction the KB keeps deliberate.
- [Reflection makes retained lessons second-order](../../notes/reflection-makes-retained-lessons-second-order.md) — matched on `model editing`; its Scope already handles targeted parametric intervention generically, and adding this source would duplicate what `reach-assessed-commitments` already carries better.
- [World models assess explanatory-reach through action-conditioned prediction](../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) and [Reach-assessment](../../notes/definitions/reach-assessment.md) — matched on `intervention`, but there "intervention" is the causal-inference term for testing a commitment's reach; CBM's intervention is a human test-time correction of a predicted concept. Same word, different operation.
- `kb/agent-memory-systems/reviews/ace.md`, `kb/agent-memory-systems/reviews/AI-Context-OS.md` — matched on `interpretable`, meaning "hand-written heuristic rather than embedding" in both. Unrelated sense.
- `kb/agent-memory-systems/reviews/dynamic-cheatsheet.md`, `kb/agent-memory-systems/reviews/KBLaM.md` — matched on `test-time`, meaning test-time memory accumulation and knowledge injection. No concept-layer or human-intervention parallel; not a `compares-with` peer.

## Index Membership

- [Observability](../../notes/observability-README.md) — its "Inspectable Artifact" section currently holds a single entry. Nothing to add for the snapshot itself (tag READMEs index notes, not sources), but if the ingest's material is ever promoted into a note about architecture-supplied inspectability, that section is where it belongs.
- `kb/sources/README.md` — describes the collection's shape rather than enumerating sources, so no per-source entry is needed.

## Synthesis Opportunities

`only-explicit-retention-is-durable-writable-and-addressable.md` (addressability fails for every tacit form; falsifier named as interpretability-grade editing), `reflection-buys-addressability.md` (opaque retention admits only indirect handles), and `opacity-is-a-scale-threshold.md` (structural affordances set the opacity threshold) together imply a claim none of them states: **addressability of a parametric artifact can be bought at design time by architecture rather than recovered at inspection time by tooling** — a concept bottleneck installs the addressable interface before training, and its cost is paid in concept supervision rather than in interpretability effort. This source is the worked case that would ground it. Not created here.

## Maintenance Observations

- **Collection-contract gap.** `kb/sources/COLLECTION.md` authorises no label for a source that *qualifies* or *tempers* a note's claim — only `evidence` (corroborates), `abstracted-from`, `rationale`, `compares-with`, `defined-in`, and `see-also`. The `inspectable-artifact-…` candidate above is a clean instance and is unlikely to be the last, since interpretability sources routinely complicate rather than confirm claims about opacity.
- **Unregistered label already in use.** `kb/notes/opacity-is-a-scale-threshold.md:18` uses the label `tempers` toward `inspectable-artifact-…`, which is not in `kb/notes/COLLECTION.md`'s authorised table. Whether to register `tempers` or rewrite that edge is a decision the gap above would force anyway.
- **Bare external citation with a local capture available.** `kb/notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md:46` cites `arxiv.org/abs/2007.04612` externally while the snapshot now exists locally. The same line also cites Meng et al. (ROME, `arxiv.org/abs/2202.05262`), which has **no** local snapshot — a candidate capture if that note's parametric-intervention argument is developed further.
- **Missing ingest companion.** `kb/sources/concept-bottleneck-models.ingest.md` does not exist, so this snapshot currently has no authored outbound surface at all. Every entry under `Connections Found` is blocked on that file being written.

## Flags

- **Snapshot has no authored surface.** Nothing in `Connections Found` can be authored until the ingest report exists. If the ingest is being written concurrently, this report is its input rather than a follow-up.
- **Tension, unresolved.** `inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md` argues representational form determines inspectability ("You can't write a test for a weight"), while this source demonstrates an architecture that makes a weight-based model's intermediates individually testable and correctable. `opacity-is-a-scale-threshold.md` already tempers the first note in a related way. Flagged, not resolved.
- **Not a split candidate.** The source connects to six notes, but they cluster in one topic area (addressability and inspectability of parametric artifacts) and it makes one assertion, so the five-notes-across-three-areas threshold is not met.
- **Scope check.** An ML-architecture paper is outside the KB's stated scope on its own; it earns entry only through the addressability and oversight-cost notes it bears on. The ingest should keep the analysis pointed at that landing rather than summarising the ML contribution for its own sake.
