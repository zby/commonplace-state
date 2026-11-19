---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/program-synthesis-gulwani-polozov-singh-2017.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Program Synthesis (Gulwani, Polozov, and Singh, 2017)

**Source:** [Program Synthesis](../../../../sources/.snapshots/program-synthesis-gulwani-polozov-singh-2017.md)

## Discovery Trace

**Scope:**
- The source collection authorizes prospecting in `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and other tracked sources. At the operator's direction, final candidates were restricted to direct, consequential connections about user-intent ambiguity and interaction.
- The snapshot has no `tags:` field, so no tag README or by-tag search applied. External prospecting was skipped as required; the already-known canonical URL is captured in the snapshot frontmatter.

**Curated heads and complete listings:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Generated each authorized destination's complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, then its description surface with `rg '^description:' kb/<destination>/ --glob '*.md'`. The note surface exposed the ambiguity, intent, and oracle candidates retained below. The other four collections exposed no artifact whose claim directly concerns interactive discrimination among candidate interpretations.

**Body searches:**
- `rg -l -i 'program synthesis|program search|candidate search|hypothesis space|search space' kb/notes --glob '*.md'` -- found the proposal-selection and oracle cluster; only oracle-domain consequences survived the narrowed articulation test.
- `rg -l -i 'specification|underspecification|under-specification|ambiguity|user intent|disambiguat|counterexample' kb/notes --glob '*.md'` -- found the semantic-underspecification, silent-disambiguation, intent, and specification-lifecycle clusters.
- `rg -l -i 'oracle|verification|verifier|evaluation|ranking|cost function|proxy' kb/notes --glob '*.md'` -- found the oracle-strength and selection clusters; [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) was retained because the survey explicitly contrasts automatic queries with the user as validation oracle.
- `rg -l -i 'interactive|clarification|active learning|distinguishing input|clarifying question' kb/notes --glob '*.md'` -- retained the intent and silent-disambiguation notes because FlashProg asks about concrete disagreements between surviving programs.
- `rg -l -i 'distinguishing (input|alternative)|conversational clarification|user intent|ambiguity resolution|underspecif|disambiguat' kb/notes --glob '*.md'` -- final bounded pass; it also found the weak matches recorded under Rejected Candidates.
- The corresponding focused searches over `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` returned only generic specification or oracle vocabulary, not a direct target. Searches over `kb/sources/` found later program-search ingests, but their fixed evaluators do not address interactive user-intent clarification.

**Link following:**
- Followed [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) to its delegation and determinability neighborhood. The survey supplies a cleaner formal instance than the adjacent delegation notes: a distinguishing input is constructed exactly where live programs disagree.
- Followed [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) to [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md). FlashProg joins these claims by detecting an unresolved semantic branch and exposing it as a question rather than silently choosing a program.
- Followed the oracle cluster through `oracle-strength-spectrum.md` to [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md). The latter is the tighter target because the source directly explains why user validation cannot be queried automatically at synthesis scale and how weaker query interfaces change the automated domain.
- Followed the later DreamCoder, FunSearch, and AlphaDev ingests. They compare on search-space and evaluator design, but not on the report's selected interaction axis, so no source-to-source edge was retained.

## Connections Found

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- **is-evidence-for**: programming by example can leave millions of precisely executable programs consistent with one example, most contrary to the user's unstated intent. This is a deterministic symbolic case in which semantic underspecification exists independently of execution indeterminism.
- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) -- **is-evidence-for**: a distinguishing-input query is generated only where two programs still consistent with the accumulated examples produce different outputs; the user's answer then removes alternatives or changes the next search round.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **is-evidence-for**: FlashProg detects disagreements among candidate programs, points the user to the discrepant input, and asks which output is intended. The interaction makes an otherwise silent semantic repair observable before adoption.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: the survey says the user is often the best validation oracle but cannot be queried automatically and scalably. Oracle-guided synthesis substitutes cheaper I/O and distinguishing-input queries where possible, showing that the available query interface bounds which synthesis decisions can run unattended.

## Bidirectional Candidates

- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) <-> source -- **evidenced-by** from the note side: distinguishing-input synthesis is an exact worked instance of live alternatives being surfaced at their point of disagreement and resolved by decision-relevant intent.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../notes/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) <-> source -- **evidenced-by** from the note side: FlashProg demonstrates a concrete recovery path that records and presents semantic ambiguity rather than hiding a guessed interpretation behind task success.

## Reverse-edge Candidates

- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) → future matching ingest -- **evidenced-by**: cite the tracked ingest, once drafted, for the survey's deterministic programming-by-example case separating specification ambiguity from execution randomness.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) → future matching ingest -- **evidenced-by**: cite the tracked ingest, once drafted, for the explicit cost and automation differences among validation, I/O, distinguishing-input, and user oracles.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- rejected: the survey establishes live clarification while the note deliberately compares durable artifact strategies; the source does not establish how the elicited answer is maintained as a durable specification.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- rejected: the survey says users may discover the scope of their intent during interaction, but it does not compare that discovery with genuine world change.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- rejected: both involve questions, but that note's claim turns on preserving or rewriting an agent-to-agent execution context, not on discriminating candidate program meanings.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- rejected for this bounded pass: the survey's ranking chapter is relevant to selecting among example-consistent programs, but it does not test the note's statistical enrichment claim and the ranking mechanism is not interactive clarification.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- rejected as an outbound candidate: the note concerns open-ended KB synthesis and already carves out formal domains; this survey is more useful through the narrower oracle-domain edge retained above than as a broad cross-domain analogy.
- [Ingest: DreamCoder: growing interpretable knowledge with wake-sleep Bayesian program learning](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md), [Ingest: Mathematical discoveries from program search with large language models](../../../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md), and [Ingest: Faster sorting algorithms discovered using deep reinforcement learning](../../../../sources/faster-sorting-algorithms-discovered-using-deep-rl.ingest.md) -- rejected: they are strong comparisons for program-space design and automated evaluation, but none supplies a user-interaction mechanism for resolving ambiguous intent.

## Index Membership

None.

## Synthesis Opportunities

None. The higher-order mechanism already exists in the intent and silent-disambiguation notes: ask only where live alternatives disagree, and expose the answer as a semantic recovery rather than a hidden guess.

## Maintenance Observations

None.

## Flags

- The matching authored surface, `kb/sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md`, does not yet exist. Outbound and reverse-edge candidates should target that ingest after it is drafted; no durable artifact should link to the immutable snapshot.
- This was a deliberately bounded connection pass over a broad 119-page survey. Search-space restriction, ranking, optimization, and neural-synthesis connections were evaluated only far enough to exclude them from the requested user-intent ambiguity and interaction scope.
