---
description: "Connection discovery for Goedecke's defense of partial codebase understanding: successor recovery, rationale fidelity, and rewrite costs."
type: types/connect-report.md
source: kb/sources/defense-of-not-understanding-your-codebase.ingest.md
source_has_frontmatter: true
date: "2026-10-15"
depth: standard
---

# Connection Report: In defense of not understanding your codebase

**Source:** [In defense of not understanding your codebase](../../../../sources/defense-of-not-understanding-your-codebase.ingest.md)

Discovery only. All proposed edges below are candidates for future authoring. The ingest already links the rationale-retention note and theory-builder definition; these are identified separately from newly discovered connections. Discovery used the connect skill and current repository state, without workers or external search.

## Discovery Trace

### Authorization and breadth

Read the source collection contract and the connect-report type before prospecting. Sources permits prospecting notes, reference, agent-memory-systems, agentic-systems, tags, and other sources. Notes admits substantive evidential and comparison edges; reference admits only sparse `see-also` edges. No discovery into work or instructions was performed. Tags is named as a prospecting surface but has no corresponding source-to-tags label; its heads were used for routing rather than proposed as outbound targets.

### Curated heads and title surfaces

Read `README.md` for all six destinations. Generated the complete title surface for each using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, with destination replaced in turn by `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `tags`, and `sources`. Recovered truncated title output from the tool's full-output file.

- **Notes:** titles identified rationale recovery, partial program theory, compiler transfer, and software disposal as the strongest neighborhoods. The notes landing routes through tag heads rather than listing claims.
- **Reference:** its curated head identified design-rationale management; the description scan confirmed that this is a current-state companion rather than evidence about revival.
- **Agent-memory-systems:** the frozen survey landing and title surface supplied no direct successor-recovery case. No evidence for a particular memory product follows from the essay's conjectural LLM paragraph.
- **Agentic-systems:** the landing distinguishes authored accounts from archived generated analyses. Neither the title scan nor matching descriptions identified a codebase-revival experiment; rejected generic recovery and retained-rationale matches rather than importing unrelated runtime continuity claims.
- **Sources:** the complete title surface identified Naur's primary essay and the Answer.AI complexity essay as the closest comparisons.
- **Tags:** read the tags landing, then the theory-builder and deploy-time-learning heads, following their program-theory and compiler-transfer entries. Both heads declare `complete: true`; skipped by-tag `rg` for these tags. The source itself has domains but no tags. Read the tags collection contract: sources is not a participating collection, so no membership proposal is made.

### Description and body searches

For each of the six destinations, ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'understand|rationale|naur|recover|ephemeral|program.theory|comprehension|decision.premis'`.

- **Notes:** kept the rationale-retention note as an existing-edge baseline; promoted partial program theory and operational-knowledge preservation for full reading. Compiler-transfer and project-theory notes merited evaluation but not additional outbound links. The specification-strategy match concerns knowledge emerging during work, but the source does not test durable spec maintenance.
- **Reference:** read design-rationale management fully; retained it only as a rejected optional companion because the theoretical retention note provides the more direct route.
- **Agent-memory-systems:** exocomp's recovery description concerns workbench recovery, not reacquisition of design understanding. Review-framework rationale is about constructing a survey. Neither passes articulation for this essay.
- **Agentic-systems:** matches such as Enoch, Meta^n, ContextPilot, and PrimeScientist concern runtime recovery, score inheritance, or optimizer rationale. Rejected at description resolution: the shared words do not identify the source's mechanism.
- **Sources:** read Naur and Answer.AI fully; both support named-axis comparisons. Deep technical comprehension concerns paper critique, not abandoned software recovery, so it was not promoted.
- **Tags:** the theory-builder description routed into the program-theory neighborhood, not an outbound edge.

Ran `rg -l -i 'Naur|partial understanding|successor|end.to.end flow' kb/notes --glob '*.md'`. This found the compiler-transfer, rationale-retention, partial-theory, and project-theory cluster. Ran `rg -n -i 'Naur|partial understanding|lost theory|original theory' kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/tags --glob '*.md'`. Naur's ingest already distinguishes original mental possession from sufficiently compatible successor understanding; the new source adds practitioner counterpressure rather than discovering that distinction for the first time. No direct match appeared in the two system-review collections.

A supplementary, bounded search used `rg -n -i 'trace.*flow|incremental.*understand|production quirks|rewrite|abandoned' kb/notes kb/sources --glob '*.md' | head -70`. Most sampled rewrite hits concerned unrelated self-modification or narrative rewriting; this was not treated as an exhaustive body search. Also ran `rg -n -i 'codebase|reconstruct|understand' kb/agent-memory-systems/README.md kb/agentic-systems/README.md`; the only hit concerned historical survey reproducibility, not the essay's recovery mechanism.

### Link following and reverse pass

Read the rationale-retention note, followed its link to the informational-recovery assay, and read that assay fully. Both distinguish faithful reconstruction from plausible substitution. Followed the partial-program-theory note's rationale link and the theory-builder head's project-theory entry. Read the compiler-transfer note and operational-knowledge preservation note fully. Read the theory-builder definition to assess the source's existing terminology link.

Read the notes collection contract before evaluating note-to-source edges. Its `evidenced-by` label permits sources that qualify or bound a claim; corroboration requires an attempted refutation. Kept two narrow reverse candidates below, explicitly not corroboration. Rejected a theory-builder-definition return link because this source documents no stated theory/criticism sequence. No source contract hint required a broader reverse pass into unrelated collections.

External is authorized but is not a search surface. The source URL is already recorded in the ingest; its existing provenance needs no duplicate `derived-from` proposal. No other external candidate was evaluated.

## Connections Found

- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) — **compares-with**: compare original-theory reconstruction and guided transfer with acquiring a different, adequate successor understanding. This takes a reader directly to the primary position Goedecke contests and its retained caveats; reported maintenance success does not by itself refute historical irrecoverability.
- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) — **compares-with**: compare Goedecke's trace-one-flow-and-expand heuristic with the note's stronger longitudinal criterion for partial understanding: theory must shape search, recovery, and later revision. The link supplies an evaluation target without treating the recollections as a demonstrated causal path.
- [Discarding software requires preserving the operational knowledge later work needs](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) — **is-evidence-for**: the essay's production-quirk objection bears on the cost and information-loss risks of replacing an implementation that carries otherwise unrecorded commitments. It is anecdotal problem evidence, not a controlled test of the note or proof that retaining code is always necessary.
- [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) — **compares-with**: compare the value of design understanding against competing product obligations. Answer.AI describes preserving one billing path partly by narrowing product behavior; Goedecke emphasizes that understandability competes with product, security, and legal demands. Together they prevent simplicity or comprehension from being treated as cost-free objectives. Neither source establishes a general LLM capability result.

## Bidirectional Candidates

None. No new return link is recommended merely to mirror an outbound comparison. The stronger note-to-source uses are separated below.

## Reverse-edge Candidates

- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) → source — **evidenced-by**: a bounded practitioner counterpoint clarifies that a successor can report useful maintenance without recovering historical warrant or rejected alternatives. The context should say the source qualifies a reading of the retention argument, not that it refutes or corroborates the current note. The source already links this note; the useful new direction is inbound.
- [Naur's compiler case tests one historically bounded documentation-and-consumption system](../../../../notes/naurs-compiler-case-tests-one-documentation-and-consumption-system.md) → source — **evidenced-by**: qualify the transfer discussion with a claimed successful successor-recovery route based on tracing flows and careful changes, rather than assuming every code-and-document pathway fails. The recollections provide a rival pathway worth testing, not an independently repeatable counterexample or evidence that structured retrieval succeeds.

## Off-authorisation Candidates

None. No useful source-to-tag edge was established that would justify extending authorization merely to carry it.

## Raw Text Candidates

None.

## Rejected Candidates

- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) — rejected as a *new outbound addition*: the ingest already gives this connection substantial treatment. Preserve it; consider only the separately justified reverse edge.
- [Theory builder](../../../../notes/definitions/theory-builder.md) — already linked and appropriately qualified. Successful incremental maintenance alone does not establish its four conditions, so no additional evidential edge or definition-side return link is warranted.
- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) — valid distinction, but the existing rationale-retention connection already applies it to this source and links the assay. Another direct edge would add little traversal value.
- [Project-theory possession requires comparing new demands with existing organization](../../../../notes/project-theory-relates-new-demands-to-existing-organization.md) — tracing a flow may orient inspection, but the essay does not show assimilation versus additive-patch decisions or their later structural consequences. Do not use it as support for that conjecture.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — shared execution-discovered understanding is insufficient: the source does not compare spec-first, bidirectional records, or spec mining.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — an authorized `see-also` is possible, but current Commonplace recording surfaces are less directly useful than the existing theoretical retention link. Omitted to avoid a companion-link spray.

## Index Membership

None. Sources does not participate in the tag membership contract. The sources landing describes file roles rather than curating individual ingests; no additional landing entry is justified.

## Synthesis Opportunities

None. The primary Naur ingest and rationale-retention note already distinguish adequate successor understanding from faithful historical recovery. A new synthesis would duplicate that distinction before new recovery evidence is available.

## Maintenance Observations

The deploy-time-learning head describes the compiler case as explaining why maintainers lacking theory cannot make demanded changes. The linked note carefully restricts its inference to one historically bounded package and consumption process. A later index-maintenance pass could narrow the head's context phrase to avoid implying a universal impossibility. No index was changed.

## Flags

- The source retains no verbatim quotes. Any future source-dependent note edit must choose the appropriate grounding route before relying on specific source wording; this discovery report does not supply quote evidence.
- Keep operational recovery distinct from historical recovery, and partial human understanding distinct from a demonstrated stated-theory learning mechanism. The LLM paragraph remains conjectural.
- No split candidate: the retained connections concern one central recovery-versus-replacement argument, not five notes across three independent topic areas.
