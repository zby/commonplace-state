---
description: "Post-ingest connections for JAZ, including independently useful inbound citations for context interfaces and host-language scheduling."
type: types/connect-report.md
source: kb/sources/harness-as-a-language-jaz.ingest.md
source_has_frontmatter: true
date: "2026-09-26"
depth: standard
---

# Connection Report: JAZ ingest

**Source:** [JAZ ingest](../../../../sources/harness-as-a-language-jaz.ingest.md)

## Discovery Trace

- Read the accepted ingest in full. Applied the sources collection outbound contract and the connect-report type. Reused the same-session collection README reads for notes, reference, agent-memory-systems, agentic-systems, tags, and sources; this pass targets the accepted analysis rather than its immutable source snapshot.
- Regenerated the complete title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/tags/ kb/sources/ --glob '*.md'`, selecting candidates with `rg -i 'fixed decomposition|theory builder|addressable theory|harness as a language|context.operation|host language|^.*# (ACE|Letta|Fractal)$'`.
- Notes: read the newly foregrounded fixed-decomposition note and the theory-builder/addressable-theory definitions; retained the already read context-interface and practical-scheduler notes. Followed the ingest's explicit links and the interface note's link to fixed decomposition. The ingest's learning assessment makes a definition link useful, but a speculative theory-builder case does not justify an inbound citation from the definition.
- Ran `rg -n 'frozen|meta.agent|adaptation|history|decomposition'` over the context-interface and practical-scheduler notes, Fractal, ACE, and Letta. The search verified concrete retained-history, adaptation, and control-flow comparisons, rather than mere shared vocabulary.
- Agent-memory-systems: revisited ACE's per-task and batch update paths and Letta's tool-mediated recall. Retained comparison candidates with the paper's particular configurations distinguished from these older code reviews.
- Agentic-systems: revisited Fractal's exact session history passed into Python and its cross-turn persistence. Retained a narrow comparison with JAZ's exposed current history and in-process continuation.
- Sources: the previous title/description scan and RLM walkthrough read remain useful for tracing programmable-input ancestry, but the accepted ingest's three main connections are more specific. No additional source link is needed for the recommended action.
- Reference: the same-session README, title, and description scan for `context|orchestrat|harness|call` found Commonplace implementation and proposal records; none adds a concrete reader need beyond the selected theory.
- Tags: reconsidered computational-model and context-engineering heads for navigation. The previously read continual-learning head is marked complete, so no by-tag sweep was needed. Do not manufacture an ordinary sources-to-tags relation.
- Inbound pass: applied notes/COLLECTION.md independently. The interface and scheduler notes each gain a bounded external case. The broader fixed-decomposition note already has detailed examples, so another inbound link is not justified solely because the ingest cites it.
- External prospecting skipped; the original paper is already supplied and cited by the ingest.

## Connections Found

- [Context-operation interface](../../../../notes/context-operation-interface-bounds-context-policy.md) — **is-evidence-for**: preserve the existing connection as a bounded recall case, with joint prompt/history removal and configured search beside any causal interpretation.
- [Practical host-language scheduler](../../../../notes/the-practical-scheduler-is-the-host-language.md) — **is-evidence-for**: preserve the existing example of recursive returning calls and live variables, bounded to in-process execution.
- [Fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: preserve the analysis of fixed model, task, feedback, and meta-agent/solver boundaries; the paper does not demonstrate that these boundaries are mistaken.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — **defined-in**: supplies the four conditions applied in the learning assessment, including the distinction between membership and demonstrated learning.
- [Addressable theory](../../../../notes/definitions/addressable-theory.md) — **defined-in**: supplies the selective-revision property whose benefit the source does not isolate.
- [ACE](../../../../agent-memory-systems/reviews/ace.md) — **compares-with**: a possible additional link for readers checking what the restricted 42-task baseline omits from the broader framework's update options.
- [Letta](../../../../agent-memory-systems/reviews/letta.md) — **compares-with**: a possible additional link for readers distinguishing the tested recall configuration from the broader memory service.
- [Fractal](../../../../agentic-systems/reviews/fractal.md) — **compares-with**: a possible additional comparison separating cross-turn session-history input from current-REPL history and continuation.

## Bidirectional Candidates

- [Context-operation interface](../../../../notes/context-operation-interface-bounds-context-policy.md) → [JAZ ingest](../../../../sources/harness-as-a-language-jaz.ingest.md) — **evidenced-by**: readers gain a concrete example of retrieval operations changing which context can be assembled. Phrase it as a bounded case, not general corroboration; retain the joint ablation and Letta configuration qualifications. Use `(snapshot required)` until sufficient quotes are retained.
- [Practical host-language scheduler](../../../../notes/the-practical-scheduler-is-the-host-language.md) → [JAZ ingest](../../../../sources/harness-as-a-language-jaz.ingest.md) — **evidenced-by**: readers gain a paper-described implementation of a returning recursive primitive and in-memory state, without inferring cross-restart durability. Use `(snapshot required)` until sufficient quotes are retained.

## Reverse-edge Candidates

None beyond the two independently justified return links above.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Theory builder](../../../../notes/definitions/theory-builder.md) as an inbound citation source: the ingest explicitly leaves consistent content-directed criticism less directly evidenced; this does not make JAZ a strong defining example.
- [Fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) as an inbound citation source: its existing examples already teach the boundary, while JAZ establishes no new impossibility result.
- [Unified calling conventions](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md): the source may motivate examining the necessity of name dispatch, but the accepted ingest does not assess the required refactoring property. Keep this outside its immediate connection set.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md): possible paper example for recursive returning calls and host-language composition.
- [Context engineering](../../../../tags/context-engineering-README.md): possible empirical example for programmable history and selective exposure.

## Synthesis Opportunities

None. Existing interface, scheduler, and fixed-decomposition notes already supply the useful abstractions.

## Maintenance Observations

None newly established by this pass.

## Flags

- The ingest's Quotes section remains empty. Future source-dependent uses must retain quotes or declare `(snapshot required)`.
- All added-edge proposals remain unexecuted. This report does not change library artifacts or indexes.
