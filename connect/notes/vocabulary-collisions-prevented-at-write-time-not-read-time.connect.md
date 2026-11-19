---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md"
source_has_frontmatter: true
date: "2026-07-17"
depth: standard
---

# Connection Report: Vocabulary collisions are prevented at write time, not resolved at read time

**Source:** [Vocabulary collisions are prevented at write time, not resolved at read time](../../notes/vocabulary-collisions-prevented-at-write-time-not-read-time.md)

Source already authors five outbound edges (llm-context-is-composed-without-scoping · grounds; prose-has-no-dereference · contrasts; minimum-viable-vocabulary · extends; codification · mechanism; methodology-enforcement-is-constraining · grounds). This report looks only for edges not already present.

Authorised labels for `notes -> notes` (from `kb/notes/COLLECTION.md`): extends, grounds, enables, exemplifies, mechanism, contradicts, contrasts, defined-in. `see-also` is not authorised for the notes destination. `kb/work/` excluded.

## Discovery Trace

**Curated heads:**
- Read `kb/notes/README.md` and `kb/notes/computational-model-README.md` (source's only tag). The computational-model README is an explicitly **selective head** — no `complete: true` mark — so the by-tag `rg` sweep was required and run (not skippable).
- Read `kb/notes/COLLECTION.md` outbound section for authorised destinations/labels.

**Description listing scan:**
- `rg -l '^tags:.*\bcomputational-model\b' kb/notes/ | xargs rg '^description:'` — ~60 notes; overwhelmingly scheduling/orchestration/reflection, off-topic for a vocabulary claim. Kept for follow-up: `symbolic-context-engineering-is-bounded-by-symbol-availability` (codified-feature slots), `llm-context-is-a-homoiconic-medium` (scoping hazards sibling).

**Body search:**
- `rg -il 'vocabular|naming|coinage|coined|namespace|polysemy|jargon'` over `kb/notes/` — flagged `minimum-viable-vocabulary` (already linked), `symbolic-context-engineering-is-bounded-by-symbol-availability`, `legal-drafting-solves-the-same-problem-as-context-engineering`.
- `rg -l '\bscop'` over `kb/notes/` — flagged `directory-scoped-types-are-cheaper-than-global-types`, `specification-level-separation-recovers-scoping...`, homoiconic/composed-without-scoping (linked).
- `rg -il 'body-composab|composab'` over `kb/notes/` — flagged `short-composable-notes-maximize-combinatorial-discovery` (the note asserts sense-uniqueness is "a precondition for body-composability").

**Link following:**
- From `minimum-viable-vocabulary` (already linked) confirmed no existing backlink to source — recorded as bidirectional candidate.
- Confirmed neither `llm-context-is-composed-without-scoping` nor `minimum-viable-vocabulary` currently link to source (`rg` for the slug returned nothing), so both qualify as return-link candidates.

## Connections Found

- [short-composable-notes-maximize-combinatorial-discovery](../../notes/short-composable-notes-maximize-combinatorial-discovery.md) -- **extends**: the source's own text says "Sense uniqueness is therefore a precondition for body-composability: composition is only sound over a collision-free vocabulary." short-composable-notes argues the library exists for co-loading/combinatorial discovery; the source supplies the vocabulary safety condition that co-loading silently assumes, developing that argument further. (Following the source->target link: a reader of the source who wants the co-loading payoff that sense-uniqueness protects.)
- [deterministic-validation-should-be-a-script](../../notes/deterministic-validation-should-be-a-script.md) -- **extends**: the source's third naming mechanism ("exact-string rarity ... drops write-time prevention from semantic audit to lexical search — `rg` over the exact string") makes vocabulary-uniqueness a deterministic, greppable check — a new instance of the hard-oracle-check-should-be-a-script thesis. Moderate: deterministic-validation is scoped to `/validate`; the tie is the shared "move an enforceable check off the LLM onto a script" mechanism, and the source's Open Question about a write-time collision check is where the author would act on it.

## Bidirectional Candidates

- [minimum-viable-vocabulary-is-the-naming-set-that-most-reduces](../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) <-> source -- **extends**: source already links here (extends, cost mechanism). The return edge is also useful — the source develops minimum-viable-vocabulary's payoff into an enforcement/collision-prevention consequence, so a reader arriving at minimum-viable-vocabulary benefits from being pointed onward to the write-time prevention argument.
- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) <-> source -- **extends**: source links here as `grounds` and frames itself as "the corpus-scale form of a session-scale mechanism." The return edge (session-scale -> corpus-scale) lets a reader of the composed-without-scoping note reach the durable-notes version of the name-collision pathology.

## Reverse-edge Candidates

- [symbolic-context-engineering-is-bounded-by-symbol-availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) → source -- **grounds**: that note selects context by matching codified features (type, path, tag, link label) and assumes those symbols are unambiguous. The source's "Scope in a KB is position in a schema" section explains *why* they are — position in a validator-defined slot disambiguates, not spelling. symbolic-context-engineering could ground its "already-observable symbol" premise on the source under its own COLLECTION.md rules. Modest confidence: the unambiguity is assumed rather than argued in that note, so the author may judge it non-load-bearing.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [llm-context-is-a-homoiconic-medium](../../notes/llm-context-is-a-homoiconic-medium.md) -- redundant grounds. The source's "no scope" premise is already grounded on `llm-context-is-composed-without-scoping`; homoiconicity (no program/data boundary) is a *different* mechanism and adds nothing to the vocabulary-collision claim that the existing grounds edge doesn't already carry. Linking both would double the same premise.
- [directory-scoped-types-are-cheaper-than-global-types](../../notes/directory-scoped-types-are-cheaper-than-global-types.md) -- uses "scope" in a different sense (load-scope: which type defs are visible per directory) than the source's binding-scope (where a term's technical sense applies). Authoring this edge would fuse two senses of "scope" in the reader's context — the exact write-time collision the source warns against. Rejected on the source's own principle.
- [legal-drafting-solves-the-same-problem-as-context-engineering](../../notes/legal-drafting-solves-the-same-problem-as-context-engineering.md) -- topical overlap only (both concern natural-language term management, and legal defined-terms are a prose binding device with the source's "citations strip the qualifier" failure mode). But neither note develops the other's specific claim and the source never invokes legal drafting; the shared surface is a keyword, not a load-bearing premise.

## Index Membership

- The source carries `tags: [computational-model]` and already appears in the by-tag membership. `computational-model-README.md` is a selective head, so no committed-index edit is implied (build appends the full listing). No new curated grouping is clearly warranted for a single vocabulary-focused note in an otherwise scheduling-heavy tag.

## Synthesis Opportunities

None. The vocabulary/naming cluster (this note + minimum-viable-vocabulary + codification) is already tightly cross-linked; no higher-order claim is left unnamed by the existing edges.

## Maintenance Observations

- The `computational-model` tag mixes two loosely related bodies — PL-concepts-applied-to-LLMs (scoping, homoiconicity, this note) and the scheduling/orchestration architecture. The tag-README already flags itself as selective; if the tag keeps growing, a `covered_by` split (e.g. a naming/scoping child vs a scheduling child) may become worth proposing. Not a connection candidate; noted for a future triage step.

## Flags

- No split needed: the source makes one coherent assertion (write-time prevention of sense collisions) and, excluding its five existing edges, this run surfaces only two new forward candidates across one topic area — below the 5-notes/3-areas split threshold.
