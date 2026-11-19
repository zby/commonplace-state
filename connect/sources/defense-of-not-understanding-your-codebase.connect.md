---
description: "Discovery candidates for Goedecke's defense of partial codebase understanding, focused on program-theory recovery, scale, and retention"
type: types/connect-report.md
source: "kb/sources/.snapshots/defense-of-not-understanding-your-codebase.md"
source_has_frontmatter: true
date: "2026-10-15"
depth: standard
---

# Connection Report: In defense of not understanding your codebase

**Source:** [In defense of not understanding your codebase](../../../../sources/.snapshots/defense-of-not-understanding-your-codebase.md)

Discovery only. The snapshot is immutable. All outbound suggestions below belong on a future matching ingest, not on the snapshot. No matching `defense-of-not-understanding-your-codebase.ingest.md` was found. Discovery used the source title and complete body; its frontmatter contains no tags. Judgments were produced by this single-agent `cp-skill-connect` invocation; no workers or external search were used.

The essay argues that large, high-turnover systems require partial, fallible understanding; successors can reconstruct useful understanding by tracing one flow and gradually modifying the system. It disputes wholesale rewrite as the default response to lost understanding and treats theory maintenance as a value traded against other obligations. Its LLM paragraph explicitly leaves the trade-off unsettled. These are practitioner arguments and recollections, not controlled comparisons.

## Discovery Trace

### Scope and indexes

- Read [sources contract](../../../../sources/COLLECTION.md), [report contract](../../../COLLECTION.md), and the connect-report type before authoring. Sources permits prospecting notes, reference, legacy agent-memory systems, agentic systems, tags, and sources; it excludes work and instructions. Snapshots cannot author links, and durable citations must use an ingest or external URL.
- Read `README.md` in each of the six destination collections. The notes and tags heads routed discovery toward program theory; reference identified design-rationale management. The two system heads identified historical versus current coverage, not source-specific evidence.
- Generated the complete title surface once for each destination using `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`. Scanned notes, reference, agent-memory-systems, agentic-systems, tags, and sources. Titles exposed the partial-theory, Naur-transfer, opacity, and software-disposal candidates below.
- Read [theory-builder head](../../../../tags/theory-builder-README.md), including its program-theory group. It has `complete: true`; no by-tag `rg` was run. The source itself has no tags, so there were no source-tag listings to generate.

### Description and body searches, by destination

For each of the six destinations, ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'theory|understand|rationale|reconstruct|local reasoning|opacity'`, then `rg -n -i 'Naur|partial understanding|abandoned codebase|theory of the program|theory of the codebase' kb/<destination>/ --glob '*.md' -l`.

A second bounded body pass used `rg -n -i 'reconstruct|turnover|partial|local reasoning|scale' kb/<destination>/ --glob '*.md' | rg -i 'understand|theory|rationale|codebase|opacity' | head -n 18`. This was a sampled supplementary pass, not an exhaustive body enumeration. No semantic scores were available.

- **notes:** Descriptions and Naur hits identified coherent search under delayed feedback, the historically bounded compiler case, project-theory assimilation, and rationale recovery. Full reads retained the first two plus opacity, rationale, and operational-knowledge preservation. Project-theory assimilation was evaluated but not retained: the source supplies no comparison of responsibility reuse versus additive patching. The title and description of theory-and-methodology also matched, but the source does not explain methodology fallback architecture.
- **reference:** The description search selected design-rationale management; full reading supported one sparse companion link about what can remain available after turnover. The Naur search returned ADR 077 rather than a direct theory-recovery argument; no additional architecture or ADR connection was retained.
- **agent-memory-systems:** Titles and descriptions produced no close source comparison; the first body query had no matches. The second returned Gnosis's policy of omitting reconstructible material. That policy alone does not show successful reconstruction after turnover, so it was not promoted to a candidate or followed into a broad system comparison.
- **agentic-systems:** Titles and descriptions surfaced retained-rationale mechanisms in Enoch, Meta^n, and PrimeScientist, but the Naur/partial-understanding query had no matches. The supplementary search mostly returned recovery plumbing and bounded memory findings. Persistence or restart support is not evidence for rebuilding a theory of an abandoned codebase; no system edge was retained.
- **tags:** Descriptions and Naur hits routed to the theory-builder head; the supplementary pass also exposed the artifact-analysis head's opacity link. These were navigation routes, not authored-source link targets. Sources lists tags as a scan destination but supplies no source→tags label; no ordinary `see-also` was invented.
- **sources:** Descriptions and Naur hits selected the primary Naur ingest and Answer.AI's simplicity ingest. Full reads retained both on named comparison axes. The source-title surface also exposed ephemeral-software discussions, but their strongest useful result was already captured in the existing operational-knowledge note, avoiding a redundant source spray.
- **external:** No web prospecting. The source's own URL is already supplied and qualifies as the originating external source. Other outbound article/comment links were not browsed or treated as independently inspected evidence.

### Link following and authored surface

- Followed the theory-builder head's links to the coherent-search and project-theory notes. Followed their rationale-retention neighborhood and read the rationale note in full. Its distinction between faithful recovery and plausible substitute explanation limits how the source's revival claim should be used.
- Followed the compiler-case note to the Naur ingest and read the ingest fully. Its existing limitations already distinguish original-theory reconstruction from acquiring different but adequate understanding; the new source would add an attributed practitioner counterpoint, not originate that distinction.
- Followed Naur's source comparison to the Answer.AI simplicity ingest and read it fully. Its billing example identifies concrete product-policy trade-offs, a useful comparison with Goedecke's general claim that simplicity and theory maintenance compete with other values.
- Read the opacity and operational-knowledge notes selected by titles. The former makes the scale argument directly useful to KB design; the latter translates the rewrite objection into a retention question rather than an absolute ban on regeneration.
- Read the notes contract before evaluating reverse directions. It permits `evidenced-by` to sources when the context says how a source qualifies or bounds a claim; it forbids durable links to snapshots.
- Checked `test -f kb/sources/defense-of-not-understanding-your-codebase.ingest.md` and searched `rg -n 'defense-of-not-understanding|in-defense-of-not-understanding' kb/sources --glob '*.ingest.md'`: neither located a tracked ingest.

## Connections Found

Candidates for the future ingest's authored surface:

- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) — **compares-with**: Goedecke's account of tracing one flow, making careful changes, and expanding a fallible understanding supplies a practitioner comparison for theory-guided modification. The note makes the stronger requirement explicit: the understanding must causally shape search and recovery across later demands. The essay does not establish that longitudinal test.
- [Naur's compiler case tests one historically bounded documentation-and-consumption system](../../../../notes/naurs-compiler-case-tests-one-documentation-and-consumption-system.md) — **compares-with**: both limit an impossibility inference from Naur, but on different axes. The note varies representation and consumption; Goedecke emphasizes system scale and reported revival after turnover. Following the link prevents treating the article as a test of modern retrieval or rationale machinery.
- [Opacity is a scale threshold, not a class property](../../../../notes/opacity-is-a-scale-threshold.md) — **compares-with**: the source's large-codebase argument compares with the note's account of practical inspectability degrading with aggregate size. For KB builders, this motivates selective retrieval and local inspection rather than assuming readable artifacts imply globally held understanding. The article does not establish a numerical threshold or compare representational forms.
- [Design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) — **compares-with**: rebuilding an adequate working model is not necessarily recovering the original decision premises. The note tells a KB designer which absent historical facts and scope conditions still need retention even if source inspection enables useful local work.
- [Discarding software requires preserving the operational knowledge later work needs](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) — **compares-with**: Goedecke's rewrite objection names accumulated quirks and edge cases as obstacles; the note asks what commitments must survive and through which carriers. This turns a blanket rewrite dispute into a concrete code-versus-tests-versus-records preservation comparison.
- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) — **compares-with**: compare successor-team recovery, required completeness of understanding, and revival versus rewrite. This gives the ingest reader the primary position being criticized, including the distinction between recreating the original mental theory and constructing a new adequate one.
- [Why LLMs can't make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) — **compares-with**: compare whether simplicity and theory maintenance can be traded against product requirements. Answer.AI's reported billing choice preserves simplicity partly by narrowing service behavior; Goedecke argues that obligations can justify accepting greater complexity. Neither source provides a matched LLM capability comparison.
- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) — **see-also**: adjacent implementation context for the recovery question: Commonplace distributes rationale across several surfaces but does not guarantee end-to-end continuity. Useful to a reader deciding what a successor agent can actually retrieve, not evidence that Commonplace solves turnover.
- [Original essay](https://www.seangoedecke.com/in-defense-of-not-understanding-your-codebase/) — **derived-from**: a future ingest's analysis would be worked out from this originating external source. This is an ingest→external suggestion, not a new snapshot annotation.

## Bidirectional Candidates

None. The source-to-source comparison above is sufficient; no automatic reciprocal edge is recommended.

## Reverse-edge Candidates

These are conditional on creating a tracked matching ingest. None should point to the local snapshot. The notes contract authorizes `evidenced-by` to sources for qualifying or bounding observations; the phrases below do not claim corroboration.

- [Holding a program theory means sustaining coherent search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) → future source ingest — **evidenced-by**: Goedecke's attributed revival experience would illustrate partial understanding guiding incremental work, while explicitly leaving causal mediation and longitudinal recovery untested. Useful as a practitioner boundary case, not a successful test of the note's conjecture.
- [Discarding software requires preserving the operational knowledge later work needs](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) → future source ingest — **evidenced-by**: the reported difficulty of rewriting accumulated quirks would qualify regeneration assumptions for large production systems. Retain the anecdotal status and do not infer that no alternative durable carrier can preserve those commitments.

## Off-authorisation Candidates

None. Tags were used for routing, not forced into the outbound label set.

## Raw Text Candidates

None.

## Rejected Candidates

- [Project-theory possession requires comparing new demands with existing organization](../../../../notes/project-theory-relates-new-demands-to-existing-organization.md) — the essay's local-work defense does not test assimilation versus additive patching; a link would blur successful local change with coherent responsibility reuse.
- [theory-builder head](../../../../tags/theory-builder-README.md) — useful discovery route, not an authorized source→tags edge or a membership recommendation for an immutable local snapshot.

## Index Membership

None. Do not index the ignored snapshot. Reassess routing only after an authored ingest determines its contribution; the source is not primarily about the registered theory-builder mechanism.

## Synthesis Opportunities

None. The existing coherent-search, recoverability, and operational-knowledge notes already express the useful distinctions. The source supplies a contrasting practitioner argument, not a demonstrated new mechanism.

## Maintenance Observations

- No matching tracked ingest was found. This leaves no authored surface for the suggested outbound links or durable reverse citations; creating it is a separate authorized task.
- The sources contract asks discovery to scan tags but declares no source→tags relationship label. This did not block useful discovery here. If source-to-tag edges are intended, the collection author must explicitly authorize their reader need; otherwise retain tags as routing-only surfaces.

## Flags

- Preserve the difference between reconstructing the original programmers' theory and acquiring enough new understanding to modify a system. The article disputes the practical rewrite recommendation, but reported revival does not settle exact historical recovery.
- Do not generalize the brief, explicitly unsettled LLM paragraph into evidence that LLMs improve theory acquisition or eliminate the need for maintained context.
- No split recommendation: this is an immutable external essay. The retained connections cluster around program understanding and retention, rather than three independent KB topic areas.
