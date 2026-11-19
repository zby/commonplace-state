---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/sean-goedecke-what-requirements-dont-you-have.ingest.md"
source_has_frontmatter: true
date: "2026-10-19"
depth: standard
---

# Connection Report: Ingest: What requirements don't you have?

**Source:** [Ingest: What requirements don't you have?](../../../../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md)

The ingest already authors six connections (four notes, two sources). All six target paths exist and their labels are authorised for sources -> notes/sources, so this report confirms them and adds candidates the ingest does not yet cite.

## Discovery Trace

**Authorisation read:** `kb/sources/COLLECTION.md` "Outbound links". Prospect destinations: notes, reference, agent-memory-systems, agentic-systems, tags, sources. Excluded: `kb/work/` and `kb/instructions/`. Labels: `is-evidence-for` and `abstracted-from` and `rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), `see-also` (notes, reference, sources, agent-memory-systems, agentic-systems, external), and `derived-from` (external). No label authorises sources -> tags.

**Existing links verified:** `ls` on all six targets in the ingest's Connections Found. All exist.

**Description listing scan:**
- `rg '^description:'` over the candidate files from the body searches below. Flagged: silent-disambiguation, design-rationale-must-preserve-unregenerable-decision-premises, agentic-systems-interpret-underspecified-instructions, out-of-spec-output, changing-requirements, writing-styles, specification-strategy (notes); why-software-factories-fail, defense-of-not-understanding-your-codebase, what-spec-driven-development-gets-wrong, professional-software-developers-dont-vibe (sources).

**Topic indexes:**
- `kb/tags/` listing. Read the heads of `llm-reliability`, `failure-modes` and `software-factory`. `failure-modes` and `software-factory` declare `complete: true`. Tags do not list sources (sources are not a participating collection in `kb/tags/COLLECTION.md`), and sources -> tags has no authorised label, so no tag candidates were kept.

**Body search:**
- `rg -il 'over-?engineer|overengineer|unrequested|scope creep|gold-?plat|defensive (code|check)|underspecif|under-specif' notes reference sources agentic-systems agent-memory-systems tags` -- about 60 hits, mostly underspecification theory. Kept silent-disambiguation. Rejected the rest below.
- `rg -il 'sycophan|reward hack|rlvr|grader|over-satisf|maintainab|slop|complexity' sources --glob '*.ingest.md'` -- 40 hits. Kept why-software-factories-fail (an RL-against-fast-checks mechanism for maintainability decay). The existing compares-with targets (Alvarez Vecino, Briggs) also appear here.
- `rg -il 'rlvr|reward.?hack|tolerance|non-requirement|maintainability' notes` -- 12 hits. All relevant hits are already cited (weakly-discriminated, brainstorming-maintainability-oracles).
- `rg -n -i 'goedecke' --glob '*.md'` -- found the second Goedecke ingest, defense-of-not-understanding-your-codebase.
- `rg -il 'overengineer|over-engineer|invent|scope' agentic-systems` -- only incidental hits (agno-agentos, swamp, exo, compound-engineering-plugin). None is about agents adding unrequested requirements.

**Link following:**
- silent-disambiguation footer -> agentic-systems-interpret-underspecified-instructions, changing-requirements, out-of-spec-output. Only the parent note adds something beyond the three-way-diagnosis link the ingest already has.
- why-software-factories-fail Connections -> boundary-of-automation, maintenance-capacity, inspectable-artifact. These relate to the source only through why-software-factories-fail, so none was kept as a direct edge.
- defense-of-not-understanding Connections -> design-rationale-must-preserve-unregenerable-decision-premises. Kept: Goedecke's "petrify" claim bears on it directly.
- `kb/notes/COLLECTION.md` outbound table checked for the reverse-edge label (`evidenced-by` notes -> sources; corroboration requires a test the claim could have failed).

## Connections Found

Confirmed (already in the ingest; keep as authored):
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- **is-evidence-for**: an adverse directional mechanism (grader-shaped coordination additions that tests do not penalise and that accumulate). Anecdotal; it qualifies the note rather than testing it.
- [Fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **is-evidence-for**: an acceptable-staleness tolerance is author-only business knowledge.
- [LLM output deviation requires three-way diagnosis](../../../../notes/llm-output-deviation-requires-three-way-diagnosis.md) -- **is-evidence-for**: the prompt tolerance acts before generation and review acts after it.
- [Brainstorming: maintainability oracles](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) -- **is-evidence-for**: "scope in diff but absent from task" is a cheap candidate oracle.
- [Ingest: Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) -- **compares-with**: on the source of LLM-added complexity (missing design context vs. training disposition).
- [Ingest: Simplification](../../../../sources/simplification-2090443748077416467.ingest.md) -- **compares-with**: on human authority over what is unnecessary (agent-led removal vs. agent-added scope).

New candidates:
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **is-evidence-for**: an invented mutex or re-check is the agent silently resolving an unacknowledged tolerance ambiguity in the strict direction. The tests still pass, so success hides that the spec did not settle the tolerance. Goedecke's review scan is the independent signal the note says is missing. This is the strongest new edge. It also gives the ingest's Limitations an explicit name for its "simpler account" (underspecification without a training bias).
- [Design rationale must preserve unregenerable decision premises](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) -- **is-evidence-for**: the "petrify" warning is a case of a missing premise. Once an unrequested guard ships, a successor cannot tell from the code whether the guard is load-bearing. The stated tolerance ("stale data is fine") is exactly the kind of premise that cannot be regenerated from the implementation. Practitioner forecast only, so it illustrates the note rather than corroborating it.
- [Ingest: Why Software Factories Fail](../../../../sources/why-software-factories-fail-2080697380379427275.ingest.md) -- **compares-with**: on how RL against fast outcome checks degrades code. Horthy blames a delayed maintainability oracle that tests cannot price. Goedecke names a concrete artifact of the same pressure (added coordination code that tests reward or ignore) and a review-time counter. Both are single-practitioner accounts.
- [Ingest: In defense of not understanding your codebase](../../../../sources/defense-of-not-understanding-your-codebase.ingest.md) -- **compares-with**: same author, on the cost of code whose rationale is unknown. Here he forecasts that invented requirements petrify a codebase. There he argues that partial understanding is enough to keep changing one. The pair locates the cost: unexplained guards raise the price of each careful change rather than forbidding change.

## Bidirectional Candidates

- [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) <-> source -- the note currently cites only the Augment spec-driven source as an example. A body sentence citing this ingest would give it a coding-agent case where the silent choice is visible in the diff. Under notes rules this is `evidenced-by` with a "qualifies/illustrates" phrase, not corroboration.

## Reverse-edge Candidates

- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) → source -- **evidenced-by**: the note asks for an adverse directional mechanism, and this ingest supplies a named, anecdotal one. The context phrase must say it bounds or illustrates, not corroborates, under the notes rule "Origin is not corroboration". The note's five-unquoted-source grounding bound (ADR 082) applies; the ingest has no quotes yet.
- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) → source -- **evidenced-by**: the "requirements present in the diff but absent from the task" signal could join the note's candidate-signal list as a hypothesis with Goedecke's uncalibrated "about half" rate.
- [Ingest: Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) → source -- **compares-with**: return edge for the comparison the Goedecke ingest already authors.

## Off-authorisation Candidates

- [llm-reliability tag head](../../../../tags/llm-reliability-README.md) -- the source fits the head's underspecification-to-repair arc, but sources are not tag participants and sources -> tags has no authorised label. Reject as off-scope; the notes it supports already carry the tag.

## Raw Text Candidates

None

## Rejected Candidates

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- foundational, but the three-way-diagnosis and silent-disambiguation edges already carry the underspecification point more specifically.
- [Out-of-spec output is a failure of the interpreter](../../../../notes/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- the specs in Goedecke's cases admit the added guards, so this is not interpreter failure. The link would mislead.
- [Changing requirements conflate genuine change with disambiguation](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- about late discovery of a wrong interpretation over time. Goedecke's issue is scope added during generation; the shared ground is only the word "requirements".
- [Writing styles are strategies for managing underspecification](../../../../notes/writing-styles-are-strategies-for-managing-underspecification.md) -- a stated tolerance could be a permissive style, but the note's taxonomy has no such entry. That is a synthesis signal (below), not a link.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) and [Ingest: What spec-driven development gets wrong](../../../../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) -- about durable spec artifacts and their maintenance, not per-task tolerances.
- [Ingest: Professional software developers don't vibe](../../../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) -- general developer control practices. No specific shared axis.
- agentic-systems and agent-memory-systems reviews -- no system review addresses agents adding unrequested scope; the incidental keyword hits were rejected.
- reference -- no reference artifact concerns task specification for coding agents.

## Index Membership

None. Sources are not indexed by tag heads, and `kb/sources/` has no curated topic index.

## Synthesis Opportunities

Writing-styles, fix-what-the-executor-can't-determine and this ingest, together with the Alvarez Vecino ingest, suggest an uncaptured claim. Explicitly widening the acceptable set ("I don't mind stale data") is a specification move distinct from adding constraints, and existing taxonomies of narrowing styles omit it. This matches the ingest's own Recommended Next Action (log first, promote once a mechanism or test exists). Do not create the note from this report.

## Maintenance Observations

None

## Flags

- Tension to keep visible: the ingest attributes over-satisfaction to RLVR training, while silent-disambiguation and the ingest's own Limitations support a training-neutral underspecification account. Linking both makes the competing explanations explicit; the ingest should not resolve it.
- The ingest has no retained quotes. Notes that add `evidenced-by` reverse edges will count it against the ADR 082 unquoted-source bound unless the quotes are grounded through `cp-skill-ground`.
