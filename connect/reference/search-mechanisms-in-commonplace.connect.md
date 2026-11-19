---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/reference/search-mechanisms-in-commonplace.md"
source_has_frontmatter: true
date: "2026-07-15"
depth: standard
---

# Connection Report: Search mechanisms in Commonplace

**Source:** [Search mechanisms in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md)

Source is a `note`-type doc in the descriptive `reference` collection. Its claim: search (noticing + candidate-generation) in Commonplace's proposal-selection loop is channeled through the system's own self-representing mechanisms — `cp-skill-write`, `cp-skill-connect`, `kb/log.md`, mechanical/symbolic checks, agent initiative — not only a maintainer's unaided judgment. It already inline-links `commonplace-as-a-reflective-system` (label `evidence`) and footer-links `a-proposal-selection-loop-requires-search-evaluation-and-retention` (label `grounds`).

Authorised outbound from `reference` (per `kb/reference/COLLECTION.md`): `part-of`/`contains`, `implements`/`implemented-by`, `supersedes`/`superseded-by` (all reference→reference); `rationale`→notes (primary theory edge); `defined-in`→notes/definitions; `derived-from`/`evidence`→sources/agent-memory/agentic-systems (uncommon); `procedure`→instructions; `see-also`→any (sparingly). Excluded: `kb/work/`.

## Discovery Trace

**Curated heads:**
- `kb/reference/README.md` — read; the "Search and navigate" how-to describes read-path retrieval, a different sense of "search" than the source's noticing/candidate-generation sense (flagged below).
- `kb/notes/self-improving-systems-README.md` — `complete: true`, so **by-tag `rg` for `self-improving-systems` skipped** per that mark. Surfaced the reflective-system cluster (retrieval-failure, human-inclusive-boundaries, four-gradings, reflective-coverage) and confirmed the source generalizes the `commonplace-as-a-reflective-system` trace.
- `kb/notes/foundations-README.md` — selective; scanned, then rg'd the tag.
- `kb/notes/computational-model-README.md` — selective; scanned, then rg'd the tag.

**Description listing scan:**
- `rg '^description:' kb/reference/*.md | rg -i 'search|reflect|notic|candidate|proposal|self-improv|log|maintenance|initiative'` — flagged `commonplace-as-a-reflective-system.md` (already linked), `navigation.md` (retrieval sense — see Rejected), `link-vocabulary.md` / `design-rationale-management.md` (no noticing-loop overlap).
- `rg -l '^tags:.*\bfoundations\b' kb/notes/ | xargs rg '^description:'` and same for `computational-model` — flagged `retrieval-failure-is-reflection-failure.md`, `human-inclusive-boundaries-make-reflection-cheap.md`, `reflective-coverage-is-graded-across-representational-forms.md`, `a-proposal-selection-loop...` (already linked).

**Body search:**
- `rg -l -i 'noticing|candidate generation|candidate-generation' kb/notes/ kb/reference/ kb/instructions/` — returned only the source plus `a-methodology-governs-its-own-extension...`, `human-inclusive-boundaries...`, `context-contamination...`, `why-directories...`, ADR 040. Kept `human-inclusive-boundaries` (uses "noticing what is worth changing" = search); others were incidental keyword hits.
- `rg -l -i 'self-representation|self-representing' ...` — returned the reflective-system cluster; kept `reflective-system.md` (definition), `retrieval-failure...`.
- `rg -l 'search-mechanisms-in-commonplace' kb/ | rg -v reports/` — only `kb/reference/commonplace-as-a-reflective-system.md` links inbound (the reverse edge from the trace this note generalizes already exists).

**Link following:**
- From `human-inclusive-boundaries` followed to `a-proposal-selection-loop` (shared grounding, already linked by source) and confirmed its explicit line "Humans keep search (noticing what is worth changing)" — the exact claim the source complicates.
- From `retrieval-failure-is-reflection-failure` confirmed it reads the **same** `covered_by`/`learning-theory` symbolic-check trace the source's "Noticing is not purely human" section uses.

**Destinations skipped:** sources / agent-memory-systems / agentic-systems — source has no external-system derivation trigger (the arscontexta lineage lives in `traversal-improvements...`, not here); instructions — the skills the source names (`cp-skill-write`, `cp-skill-connect`, `cp-skill-ingest`) are already cited inline as evidence of mechanisms, and the `procedure` label ("for how to do this") does not match that evidential use.

## Connections Found

- [traversal-improvements-should-be-deferred-via-logging](../../../../notes/traversal-improvements-should-be-deferred-via-logging-to-avoid-mid.md) — **rationale**: the source lists `kb/log.md` as one of its noticing channels and says promoting a log entry "still needs an explicit maintenance or triage step"; this note is the design rationale for exactly that — separate noticing from fixing, capture one line, let a later pass process it. Following it explains *why* the log channel is shaped the way the source describes. (Minor tension worth carrying: the source calls the log "rarely used in practice," where this note states the design intent.)
- [retrieval-failure-is-reflection-failure](../../../notes/retrieval-failure-is-reflection-failure.md) — **rationale**: the source treats search as a first-class function worth surveying; this note grounds why — retrieval/search is "the wire the self-representation acts along," so a search mechanism is load-bearing, not convenience. Both notes read the identical `covered_by` symbolic-check-vs-prose-`rg` trace, from complementary angles (the source: a symbolic check *noticing*; this note: the broken *wire* a stronger check revealed).
- [reflective-system](../../../../notes/definitions/reflective-system.md) — **defined-in**: the source leans throughout on "self-representation" / "self-representing mechanisms"; this definition supplies the "aspect-bounded, causally connected self-representation" term. Lower-priority — `commonplace-as-a-reflective-system` (already linked) also carries the concept — but a `defined-in` serves a cold reader who meets the term here first.

## Bidirectional Candidates

- [commonplace-as-a-reflective-system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) <-> source — already satisfied: the source links out to it and it links back inbound. No new edge needed. (See Maintenance re: the label on the existing pair.)

## Reverse-edge Candidates

- [human-inclusive-boundaries-make-reflection-cheap](../../../notes/human-inclusive-boundaries-make-reflection-cheap.md) → source — this note asserts "Humans keep search (noticing what is worth changing) and the judgment-heavy part of evaluation." The source's whole argument is that search's noticing/candidate-generation is *substantially channeled through system mechanisms*, complicating that clean human/machine split. The note author (under `kb/notes/COLLECTION.md`) could add a `see-also`→reference caveat to this source at that line. This is the more natural direction than a forward edge (see Off-authorisation), because the theory note is the one making the strong claim the source qualifies.
- [retrieval-failure-is-reflection-failure](../../../notes/retrieval-failure-is-reflection-failure.md) → source — since both read the same symbolic-check trace, this note could carry a `see-also`→reference to the source as the wider survey of Commonplace's search mechanisms.

## Off-authorisation Candidates

- [human-inclusive-boundaries-make-reflection-cheap](../../../notes/human-inclusive-boundaries-make-reflection-cheap.md) — passes the articulation test as a *forward* edge (source complicates this note's "humans keep search" claim), but the relationship is corrective/refining, and `reference→notes` authorises only `rationale` ("rests on this claim"), which misstates the direction. `see-also` is technically permissible for any destination but undersells a substantive corrective link, and the skill warns against downgrading to `see-also` to force a fit. Recommendation: prefer the reverse edge above; alternatively `kb/reference/COLLECTION.md` could consider a `qualifies`/`complicates` reference→notes label for descriptions that refine a theory claim. Do not author a forward `rationale` edge here.

## Raw Text Candidates

None.

## Rejected Candidates

- [navigation.md](../../../../reference/navigation.md) — a keyword-strong hit on "search," but it uses "search" in the *retrieval / read-path* sense (finding notes with `rg`, indexes, descriptions), whereas the source means search-as-noticing/candidate-generation in an improvement loop. Linking them risks conflating two distinct senses; `retrieval-failure` (kept above) already bridges the senses more precisely.
- [reflective-coverage-is-graded-across-representational-forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) — a tag-neighbor whose "coverage across prose vs symbolic forms" loosely echoes the source's symbolic-check-vs-prose contrast, but the source makes no coverage-grading claim; the overlap is topical, not load-bearing.
- [a-proposal-selection-loop-requires-search-evaluation-and-retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — genuine grounding, but **already linked** by the source; not a new candidate (label noted in Maintenance).
- [false-positive-generation-is-filtered-before-retention](../../../../notes/false-positive-generation-is-filtered-before-retention.md) and [improving-an-agentic-system-crosses-the-prose-symbolic-boundary](../../../notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — sibling notes on *other* functions of the loop (the retention filter; reliability crossing the prose/symbolic boundary). Adjacent but not needed to understand the source's search-specific claim.

## Index Membership

- [self-improving-systems-README](../../../../tags/self-improving-systems-README.md) — the source is a reference-side instance of the search/noticing theme this head curates (its "Example placements" already list `commonplace-as-a-reflective-system`). A future maintainer could add the source under the loop-decomposition bullet as the survey of search mechanisms. Connect does not edit the index.

## Synthesis Opportunities

None new. The source is itself the synthesis generalizing the `commonplace-as-a-reflective-system` trace; `retrieval-failure` and `traversal-improvements` are its theory footings rather than a further higher-order claim.

## Maintenance Observations

- **Existing-link label drift (collection-contract).** The source's two current links use labels outside the `reference` authorised set: `a-proposal-selection-loop...` carries `grounds` (a `notes`-collection label; the reference equivalent is `rationale`), and `commonplace-as-a-reflective-system` carries `evidence` on a reference→reference edge (reference→reference authorises only `part-of`/`implements`/`supersedes`; `evidence` is authorised only toward sources/agent-memory/agentic-systems). The reference→reference "this doc generalizes that doc's analysis" relationship has no precise authorised label — only `see-also` (any). Candidate signal that either these labels want normalizing or the reference label set has a gap for generalization/refinement edges.
- **"search" term collision.** `reference` uses "search" in two unrelated senses — read-path retrieval (`README.md`, `navigation.md`) and noticing/candidate-generation in the improvement loop (this source). No disambiguation exists at the collection level; a future reader could conflate them.

## Flags

- **Register/placement note (not blocking):** the source is a `note`-type doc filed under descriptive `reference`, but its footer labels (`grounds`, `evidence`) and its generalizing, theory-shaped argument read like a `kb/notes/` theory note. Not a connect finding to act on here — surfaced only because it explains the label drift above.
