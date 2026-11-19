---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/build-systems-a-la-carte-theory-and-practice.md"
source_has_frontmatter: true
date: "2026-10-07"
depth: standard
---

# Connection Report: Build systems à la carte: Theory and practice

**Source:** [Build systems à la carte: Theory and practice](../../../../sources/.snapshots/build-systems-a-la-carte-theory-and-practice.md)

The source is an immutable snapshot (JFP 30 e11, 2020; the extended version of the ICFP 2018 paper). It authors no links. Every "Connections Found" item is a candidate for the authored surface, which is the future `kb/sources/build-systems-a-la-carte-theory-and-practice.ingest.md` (not yet present). Durable links must target that ingest, never the snapshot.

The KB already holds an ingest of the 2018 conference version: [build-systems-a-la-carte.ingest.md](../../../../sources/build-systems-a-la-carte.ingest.md). Three KB artifacts already cite it. This report therefore concentrates on what the extended version adds. The paper itself (§1) lists the new material: §3.8, §5.2.2 (verifying step traces), §7 (Experience: Cloud Shake, Hadrian), and §8.1, 8.3, 8.6–8.9 (partial stores, impure computations, key-dependent types, multiple outputs, self-tracking, file watching vs polling).

## Discovery Trace

**Collection contract:** read `kb/sources/COLLECTION.md` "Outbound links". Authorised destinations: notes, reference, agent-memory-systems, agentic-systems, tags, other sources, external. Excluded: `kb/work/`, `kb/instructions/`. The snapshot is never the link author; candidates go to the ingest. Labels by destination: notes → is-evidence-for, abstracted-from, rests-on, compares-with, defined-in (definitions), see-also; reference → see-also only; sources / agentic-systems / agent-memory-systems → compares-with, see-also (plus is-evidence-for for agent-memory-systems); external → derived-from, see-also.

**Source reading:** frontmatter, abstract, contribution list (lines 47–105), §3.6 correctness, §5.1 dirty bit, §5.2 opening, §7 / §7.3 (Cloud Shake versions), §8.3 impure computations, §8.4 cloud implementation and Frankenbuild, §8.5 iterative computations, §8.8 self-tracking, §8.9 file watching vs polling, §9.3 memoisation, §10 conclusions.

**Existing ingest and its neighbourhood:** read `kb/sources/build-systems-a-la-carte.ingest.md` in full. Its candidate set was re-checked: `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent`, `link-graph-plus-timestamps-enables-make-like-staleness-detection`, `llm-recompute-cost-inverts-the-store-vs-recompute-default`, ADR 032, `factored-dependency-pairs-for-review-freshness`. Its candidate `distilled-artifacts-need-source-tracking` no longer exists (see Maintenance Observations).

**Who cites the conference version:** `rg -l 'build-systems-a-la-carte' kb --glob '*.md' --glob '!kb/reports/**'` → `kb/notes/first-principles-analysis-maps-design-space-before-selection.md`, `kb/notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md`, `kb/sources/in-toto-farm-to-table-guarantees.ingest.md`, plus `kb/work/` files (excluded destination; not candidates).

**Tag heads:** listed `kb/tags/`. Read the relevant lines of `review-system-README.md` (section "What review checks and when verdicts go stale"; "Proposals: freshness and invalidation") and `curation-README.md` ("Ranking and staleness signals"). Both route to candidates already found below. Grepped `kb-maintenance-README.md` and `computational-model-README.md` for stale/fresh/derived; no new candidates.

**Body search** (every query used `rg -l -i "<q>" kb --glob '*.md' --glob '!kb/work/**' --glob '!kb/reports/**' --glob '!kb/sources/.snapshots/**'`):
- `verifying trace` → criteria-edits note, old ingest. Kept: criteria-edits.
- `early cutoff` → old ingest only.
- `self-tracking` → criteria-edits note, old ingest.
- `build system` → `agent-memory-systems/reviews/o-o.md` (rejected; it says "no build system"), sutskevers-list chapters (rejected; general engineering appendix), criteria-edits, first-principles-analysis. Kept: the last two.
- `dirty bit` → old ingest only.
- `memoi[sz]` → `reference/proposals/code-scheduled-workflows.md`, `agentic-systems/reviews/eigenius.md`, `agent-memory-systems/reviews/cocoindex.md`, `notes/orchestration-strategies-and-run-state-have-opposite-persistence.md`. Kept: eigenius and cocoindex. Rejected: the other two (see below).
- `Frankenbuild` → none.
- `à la carte|a-la-carte|a la carte` → criteria-edits, first-principles-analysis, old ingest, in-toto ingest.
- `non-determinis` → `notes/execution-indeterminism-is-a-property-of-the-sampling-process.md`, `agentic-systems-interpret-underspecified-instructions.md`, workshop note, several ingests. Evaluated the execution-indeterminism note; rejected it as a direct edge (see below).
- `Makefile|like Make|make-like|Make-like` → link-graph-plus-timestamps, a-derived-copy, artifacts-produced-from-sources-need-lineage, stale-self-description, criteria-edits, maintenance-capacity, runtime-structure, the two freshness proposals, ADR 038, tag heads. Kept: link-graph, a-derived-copy, artifacts-produced lineage, factored-dependency-pairs. Rejected: the rest.
- `Excel|spreadsheet` → many ingests and reviews with incidental mentions; none treats spreadsheet recalculation as a mechanism.
- `incremental (computation|rebuild|build)` → none.
- `content-address` → several memory-system reviews (okf-harness, kgai, llmwiki-marimo), git-provenance note, runtime-structure note. None engages cache-key or trace design specifically; rejected as keyword overlap.
- `volatile` → incidental "volatile context/state" usages; no build-system sense.

**Description listing / reference scan:** `rg -N -m1 '^description:'` over ADR 032, 052, 065 and `reference/freshness-architecture.md`. Read the relevant lines of `freshness-architecture.md` (target identity, role-labelled inputs, exact hashes, applicability baseline).

**Link following:** criteria-edits (lines 10–35): its "formal frame" paragraph already reads Shake as verifying traces and Excel as self-tracking from the conference ingest. first-principles-analysis (line 20) uses the 3×4 grid and says Cloud Shake "remained a blueprint for later implementation". llm-recompute-cost (lines 8–30) requires "deterministic comparison semantics" for a checked materialization. eigenius review (line 59): the memo key omits the component-definition version. cocoindex review: incremental materialization with memoization and live file watching. in-toto ingest (line 41) proposes a three-source cluster with PROV and this paper.

**External:** no external target supplied; external prospecting skipped. The `derived-from` edge to the source URL is the ingest's own provenance, not a discovered candidate.

## Connections Found

All targets below are candidates for the future ingest of this snapshot.

- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) -- **is-evidence-for**: §8.8 says build systems whose tasks are written in a full programming language cannot compare tasks for equality. They must therefore pessimistically assume that any build-script change may change any task. §7.3 shows the practical remedy in Cloud Shake: cache lookups carry the version of the build script and of the key's rule, "to avoid using stale build products from previous versions of the build script". This is the build-system form of the note's process-side claim: a production-process edit must reach the artifact through a versioned task identity. The note currently cites only the conference version, which has a single sentence on self-tracking.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) -- **is-evidence-for**: §8.3 replaces "recomputing equals the stored value" with "the stored value belongs to the set of possible recomputations" for non-deterministic tasks. The §8.4 Frankenbuild shows that caching a non-deterministic task's dependents by terminal-input hashes yields a result inconsistent with its own dependency. LLM derivation is a non-deterministic task in this sense. The two sections support the note's requirement for a deterministic checking path, and they mark where exact-equality checking stops applying. §9.3 (minimal build strictly generalizes memoisation) remains the baseline for the note's "ordinary software" default.
- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) -- **is-evidence-for**: §3.6 defines "up to date" as exact agreement with recomputation from the final store. That is the formal version of "checked". §8.3 and §8.4 add the boundary: a check by exact recomputation is unavailable when the derivation is non-deterministic, and it gives wrong answers when the cache is keyed only on terminal inputs. This sharpens the note's split between deterministic marks and judgment-based derivations.
- [Link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) -- **is-evidence-for**: §5.1 analyses Make's timestamp check as a dirty bit that the file system controls. It explains why this scheme cannot support early cutoff, and why backup software can break it by moving timestamps backwards. These are precise failure modes of the mechanism the note proposes. §8.9 adds the cost argument for file watching over timestamp polling at scale.
- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) -- **is-evidence-for**: §7 reports that the authors built Cloud Shake from the paper's road map, using one of the grid's previously empty cells, and use it for GHC's build system (Hadrian). This turns the note's example from "a workable cell that remained a blueprint" into "a predicted cell that was then built". That is stronger evidence for the method. The note's current wording is accurate for the 2018 version it cites (see Flags).
- [Source changes should surface downstream review targets, while reverse lineage can remain searchable](../../../../notes/artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md) -- **is-evidence-for**: verifying traces (§5.2) are artifact-side lineage records: each derived key stores the hashes of the dependencies it used. §8.9 compares scanning those records (polling) with watching for change events. The note's "artifact-side records need a forward index and a change-handling surface" is the same trade-off, and the paper supplies a mature engineering instance. Moderate strength: the paper does not discuss who is interrupted.
- [Build Systems à la Carte (conference-version ingest)](../../../../sources/build-systems-a-la-carte.ingest.md) -- **compares-with**: same authors and framework. Shared axis: scope of the evidence. The 2018 ICFP version supplies the scheduler × rebuilder classification. The 2020 JFP version adds experience reports (§7) and engineering corners (§8: non-determinism, self-tracking, partial stores, file watching). A reader needs to know which version supports which claim.
- [Eigenius review](../../../../agentic-systems/reviews/eigenius.md) -- **compares-with**: shared axis is memo-key completeness. The review finds that Eigenius's memo key `SHA-256(component_iri || canonical CBOR(input))` omits the component-definition version. §8.8 and the Cloud Shake `Ver` arguments (§7.3) are the build-system statement of why the task's own identity or version belongs in the key. The paper gives the review's finding a named failure class (missing self-tracking).
- [CocoIndex review](../../../../agent-memory-systems/reviews/cocoindex.md) -- **compares-with**: shared axis is the incremental-maintenance mechanism for derived stores. CocoIndex combines memoization, target-state reconciliation and live file watching. The paper's rebuilder ladder and §8.9 watching-vs-polling discussion classify these choices. Use this edge for a comparison, not as evidence for a claim.
- [Freshness architecture](../../../../reference/freshness-architecture.md) -- **see-also**: Commonplace's freshness store records role-labelled inputs with exact hashes per registered target and treats a baseline as an applicability boundary. That is a verifying-trace rebuilder. The paper names and situates the design. Reference destinations allow only see-also.

## Bidirectional Candidates

- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) <-> source -- **is-evidence-for** / note-side `evidenced-by`: the note's "formal frame" paragraph relies on the self-tracking idea. The extended version's §8.8 and §7.3 are the fuller account, so the note gains from citing the new ingest beside or instead of the conference one.
- [Build Systems à la Carte (conference-version ingest)](../../../../sources/build-systems-a-la-carte.ingest.md) <-> source -- **compares-with**: the older ingest should point forward to the extended-version ingest so readers can find §7–§8, which the 2018 analysis could not cover. Its "Limitations" section says the paper assumes deterministic recomputation. §8.3 partly answers that point, so the forward link corrects a reader's picture.

## Reverse-edge Candidates

Under `kb/notes/COLLECTION.md` rules, which a future writer must check, these notes could author `evidenced-by` edges to the new ingest once it exists:

- [Criteria edits invalidate verdicts; process edits invalidate artifacts](../../../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) → new ingest -- §8.8 pessimistic self-tracking and §7.3 rule versions.
- [LLM recompute cost shifts the store-vs-recompute balance](../../../../notes/llm-recompute-cost-inverts-the-store-vs-recompute-default.md) → new ingest -- §8.3 set-membership correctness and §8.4 Frankenbuild, for the "deterministic checking path" section.
- [A derived copy of recomputable truth must be checked or absent](../../../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) → new ingest -- §3.6 correctness definition as the formal meaning of "checked".
- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) → new ingest -- §7 reports that the predicted cell was implemented.
- [Link graph plus timestamps enables make-like staleness detection](../../../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) → new ingest -- §5.1 limits of Make's timestamp dirty bit.
- [in-toto ingest](../../../../sources/in-toto-farm-to-table-guarantees.ingest.md) → new ingest -- **compares-with**: its proposed three-source cluster ("freshness side, descriptive side, cryptographic-integrity side") names this paper. The extended version is the better freshness-side member because of §8.4 (eviction, shallow builds, Frankenbuild).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Execution indeterminism is a property of the sampling process](../../../../notes/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- §8.3 non-determinism is about what a cache may assume of a task, not about diagnosing output deviation. Linking would conflate the two. The non-determinism material belongs with the derived-copy and recompute notes instead.
- [Orchestration strategies and run-state have opposite persistence economics](../../../../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) -- "memoization" and "scheduler" keyword hits; the note is about agent control flow, not rebuild decisions. This repeats the conference ingest's rejection of the orchestration-scheduler cluster.
- [Code-scheduled workflows proposal](../../../../reference/proposals/code-scheduled-workflows.md) -- memoization hit is incidental to workflow scheduling.
- [Stale self-description conceals its own staleness](../../../../notes/stale-self-description-conceals-its-own-staleness.md) -- considered for §8.8 ("tasks depending on the makefile itself"), but the note concerns an artifact describing the system that checks it, not task-change tracking. Rhyme only.
- [o-o review](../../../../agent-memory-systems/reviews/o-o.md) -- "build system" appears only as "there is no build system".
- `kb/sources/sutskevers-list/` chapters -- general engineering design-pattern appendix; spreadsheet and build mentions are incidental.
- Content-address hits (okf-harness, kgai, llmwiki-marimo reviews; git-provenance and runtime-structure notes) -- keyword overlap without cache-key or trace design.
- ADRs 032 / 052 / 065 -- superseded as the reference anchor by `freshness-architecture.md`, which states the current boundary; ADR 032 stays a candidate of the conference ingest.

## Index Membership

- [review-system tag head](../../../../tags/review-system-README.md) -- the section "What review checks and when verdicts go stale" could list the new ingest if the sources collection participates in tags (check `kb/tags/COLLECTION.md`); otherwise leave it reachable through criteria-edits.
- [curation tag head](../../../../tags/curation-README.md) -- "Ranking and staleness signals" is the other possible home; same participation check applies.

## Synthesis Opportunities

The conference ingest already flags the "KB freshness machinery is a build system" synthesis. The extended version supplies the piece that synthesis was missing: an account of where exact-recompute checking breaks down. §8.3 (non-deterministic tasks use set-membership correctness), §8.4 (Frankenbuild), §8.8 (self-tracking for tasks that cannot be compared), the criteria-edits note, the llm-recompute note and the derived-copy note together imply a higher-order claim. When a derivation step is an LLM call, it is a non-deterministic task in the paper's sense. Exact-equality rebuilders then apply only to the deterministic envelope, such as marks, hashes and generated regions. Judgment-produced artifacts need versioned task identity plus a set-membership check, which in practice is review. This would answer the conference ingest's main limitation ("borrow its taxonomy, not its cost model") with the paper's own terms rather than by excluding the case. The workshop `kb/work/lineage-mechanisms/verification-locus-and-provenance-theory.md` reportedly develops this line; it was not read here because `kb/work/` is an excluded destination.

## Maintenance Observations

- The conference ingest's "Connections Found" names `distilled-artifacts-need-source-tracking`, which no longer exists at `kb/notes/distilled-artifacts-need-source-tracking.md`. It was probably renamed. `artifacts-produced-from-sources-need-lineage-recorded-at-the-source.md` is a likely successor (not verified).
- The conference ingest says all its connections are reverse edges labelled `evidenced-by`. The current sources contract offers `is-evidence-for` for ingest-authored edges. The wording is stale but harmless, since the edges are authored from the note side.
- Two ingests will cover one work in two versions. The sources contract has no label or convention for "extended version of" or "supersedes"; `compares-with` with a scope axis is the closest authorised fit. If this recurs, it is a possible collection-contract gap.

## Flags

- **Tension (version-dependent claim):** [first-principles-analysis](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) says Cloud Shake "remained a blueprint for later implementation". That is true of the 2018 paper it cites. The 2020 version (§7, §10) reports that Cloud Shake was implemented and is in daily use. A writer should decide whether to update the note's claim and citation. This report does not resolve it.
- **Ingest scope:** a new ingest of this snapshot should focus on the extended material (§5.2.2, §7, §8) and point to the conference ingest for the core framework, rather than re-deriving the summary.
