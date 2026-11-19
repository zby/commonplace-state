---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/evidence/clausal-binding-scopes-a-captured-predicate-word-like-a-coinage.md"
source_has_frontmatter: true
date: "2026-07-17"
depth: standard
---

# Connection Report: Clausal binding scopes a captured predicate-word like a coinage

**Source:** [Clausal binding scopes a captured predicate-word like a coinage](../../../notes/evidence/clausal-binding-scopes-a-captured-predicate-word-like-a-coinage.md)

The source is a worked-corpus evidence note. It already authors two `grounds` edges: to [vocabulary collisions are prevented at write time, not resolved at read time](../../../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) and to [actionable methodology](../../../../notes/definitions/actionable-methodology.md). This report surfaces candidates *beyond* those two.

## Discovery Trace

**Source collection / authorisation:** source path `kb/notes/evidence/...` → collection `notes`. `kb/notes/COLLECTION.md` present (no nested `COLLECTION.md` under `kb/notes/evidence/`). Outbound section read: theoretical profile; destinations `notes`, `notes/definitions`, `reference`, `agent-memory`, `agentic-systems`, `sources`, `instructions`; `kb/work/` excluded; edges to `instructions` rare (usual direction inverse via `rationale`); edges to `reference`/`sources` carry the snapshot a claim was abstracted from or corroborated by. Labels for `notes`: `extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`, `defined-in`, `see-also`.

**Topic indexes:**
- Read [computational-model-README](../../../../tags/computational-model-README.md) (source tag `computational-model`). No `complete` mark, so the by-tag `rg` was still run. The README is a *selective* head; its vocabulary/naming material lives only through the linked notes, not in the head itself. No naming/coinage cluster in the curated head — the relevant sibling notes are reached by body search below.

**Description listing scan:**
- `rg -l '^tags:.*computational-model' kb/notes/` → ~70 notes (large tag). Filtered to naming/vocabulary/scoping semantics; most are scheduling/orchestration and out of scope for this note.

**Body search:**
- `rg -l -i 'coinage|compound token|greppable|multi-word|coined' kb/notes/` → only 3 hits: the source, [vocabulary-collisions](../../../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) (already linked), and [discovery-lifecycle](../../../../notes/definitions/discovery-lifecycle.md). The coinage/greppability vocabulary is highly concentrated — strong signal that discovery-lifecycle is the one unlinked sibling.
- `rg -l -i 'predicat|clausal|namespace|tokenizer' kb/notes/` → source, vocabulary-collisions, llm-context-is-composed-without-scoping, actionable-methodology, plus many false hits (`predicate` in the SQL/query sense in files-not-database etc.). No new naming candidate.
- `rg -l -i 'write.time|lexical search|exact string|uniqueness invariant' kb/notes/` → source + vocabulary-collisions dominate; no additional naming note.
- Read [discovery-lifecycle](../../../../notes/definitions/discovery-lifecycle.md) body: its Exclusions section explicitly invokes the same rule — "a multi-word coinage is greppable and collision-free where a captured common word is not" — citing vocabulary-collisions. Confirmed as a live coinage-device instance of the same principle the source's clausal-binding case sits beside.
- `rg -l -i 'coined|coinage|one-term-one-sense|naming|vocabulary polic|multi-word' kb/instructions/ kb/reference/` → only incidental "naming" hits (ADRs about file/tag naming, convert/ingest skills). No dedicated naming-review gate or vocabulary-policy reference doc that this corpus check would corroborate as `evidence`. No reference/instructions connection.

**Link following:**
- From vocabulary-collisions one hop: `codification`, `methodology-enforcement-is-constraining`, `minimum-viable-vocabulary`, `prose-has-no-dereference`, `llm-context-is-composed-without-scoping`. Evaluated each against the source's specific claim (clausal binding as a scoping device between local-declaration and coinage on the binding-strength table). None adds something the source reader gains directly that is not already reachable through the authored `grounds` edge to vocabulary-collisions — see Rejected Candidates.

**Backlinks:** `rg -l 'clausal-binding-scopes' kb/` → none. The source is new; nothing links to it yet.

## Connections Found

- [discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **contrasts**: both notes are worked instances of the same write-time-prevention rule realised by *different* scoping devices — discovery-lifecycle uses a coined compound (empty prior, greppable by exact string), the source uses clausal binding of a captured common word (busy prior, greppable only as predicate-of-subject). The source's own binding-strength discussion already ranks clausal binding "near a coined compound," so the neighbouring-shape distinction is exactly what a reader gains by following the link. (Target is a `definition`; the edge is a genuine mechanism contrast, not a term-lookup, so `contrasts` fits better than `defined-in`. Confidence: medium — worth authoring, but a future writer may judge it too close to the shared `vocabulary-collisions` hub both already route through.)

## Bidirectional Candidates

- [vocabulary collisions are prevented at write time, not resolved at read time](../../../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md) → source — **extends**: the source states outright that clausal binding "is the mechanism the existing note does not fully spell out," adding a row between "locally declared" and "coined compound" on that note's binding-strength table. A reader of the general note who wants the argument developed further (and the corpus verification of its high-innocent-prior premise) gains directly from the forward edge. Strong candidate — this is the primary edge worth authoring, and it is authored from the *target* side under `kb/notes/` rules. (The source's existing `grounds` edge covers the reverse direction.)
- [actionable methodology](../../../../notes/definitions/actionable-methodology.md) → source — **see-also**: a reader of the definition could reach the corpus check confirming its `actionable` sense does not collide across 36 ordinary uses. Weak: the definition's job is to fix the term, not to defend its greppability, so this return edge is optional; surface it only if the definition author wants the corpus evidence discoverable.

## Reverse-edge Candidates

None. No reference ADR, naming-review gate, or instruction currently owns a vocabulary/coinage policy that would cite this corpus check as `evidence`/`rationale`. (If the naming-review gate raised in vocabulary-collisions' Open Questions is ever built, this note becomes its natural evidence target — recorded in Maintenance Observations.)

## Off-authorisation Candidates

None.

## Raw Text Candidates

None. Source has frontmatter; no frontmatter-less targets surfaced.

## Rejected Candidates

- [codification](../../../../notes/definitions/codification.md) — the source converts a write-time check "from semantic audit to lexical search," but clausal binding stays in prose and never crosses into a symbolic artifact, which is what codification names. vocabulary-collisions already carries the `codification` `mechanism` edge; reaching it via the authored `grounds` edge is enough. A direct edge would overstate the source's claim.
- [prose has no reliable dereference, so a declared fact must be reinforced where it applies](../../../../notes/local-materialization-should-outperform-distant-declarations.md) — the sibling "no resolution vs no boundaries" distinction is about vocabulary-collisions, not this narrower evidence note. Too indirect for the source.
- [silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) — describes the read-time silent-merge failure the source's write-time prevention avoids, but the conceptual bridge runs through vocabulary-collisions, not directly. Linking it from the source would confuse traversal.
- [minimum viable vocabulary is the naming set that most reduces](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — vocabulary *cost/minimality*; the source is about a scoping *device*, not naming-set size. No load-bearing overlap.

## Index Membership

None. [computational-model-README](../../../../tags/computational-model-README.md) is an explicitly selective head; this narrow worked-corpus evidence sub-note does not warrant a curated-head slot, and the complete by-tag listing is build-time generated (ADR 025), not an authored index.

## Synthesis Opportunities

None. The source, discovery-lifecycle, and vocabulary-collisions already form a cluster with vocabulary-collisions as the hub; no higher-order claim beyond that note is implied that isn't already captured.

## Maintenance Observations

- vocabulary-collisions' Open Questions ask whether the one-term-one-sense invariant should get a write-time naming-review gate. If such a gate or a vocabulary-policy reference doc is ever authored, this note is a ready-made `evidence`/`rationale` target for it — currently there is no destination to author that reverse edge into.

## Flags

- Not a split candidate: the source makes one assertion (clausal binding scopes a predicate-word like a coinage) and its genuine connections stay within a single topic area (KB vocabulary/scoping). No split needed.
- The single Connections-Found edge (to a `definition` via `contrasts`) is medium-confidence; a future writer may reasonably keep only the `vocabulary-collisions` → source `extends` bidirectional edge and skip the sibling contrast.
