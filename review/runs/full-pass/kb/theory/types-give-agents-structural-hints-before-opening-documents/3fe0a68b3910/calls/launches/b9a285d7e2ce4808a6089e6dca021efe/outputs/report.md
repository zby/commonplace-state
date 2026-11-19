---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/theory/types-give-agents-structural-hints-before-opening-documents.md"
source_has_frontmatter: true
date: "2026-11-12"
depth: standard
---

# Connection Report: Types give agents structural hints before opening documents

**Source:** [Types give agents structural hints before opening documents](../../../../../../../../../../../../../theory/types-give-agents-structural-hints-before-opening-documents.md)

Judged text: the invocation's `inputs/note.md` (it may differ from the checkout file). The source collection is `theory`. `kb/theory/COLLECTION.md` exists, and its `## Outbound links` section was read before prospecting.

## Discovery Trace

**Setup and outbound rules:**
- Source claim: a document's type says what operations it affords, and its description filters among instances of that type. Together they let a stateless agent with finite context route without loading bodies. The claim depends on verifiable types and on enforced descriptions. Existing outbound links: `document-types-should-be-verifiable` (foundation), `type-system-enforces-metadata-that-navigation-depends-on` (enables), `kb/types/note.md`, and `why-notes-have-types` (context).
- `kb/theory/COLLECTION.md` outbound rules: most links stay inside `kb/theory/`. Theory→theory labels are extends, grounds, enables, exemplifies, mechanism, contradicts, contrasts and defined-in (definitions only). `evidenced-by` is the only label that may target `types`. `see-also` may target reference, instructions and sources, but not theory. Links into `kb/work/` are excluded. Links to `kb/instructions/` are rare because the usual direction is inverse (`instruction → note` via `rests-on`), so I ran a reverse-edge pass against `kb/instructions/`. `external` is authorized, but no external target was supplied or loaded, so I skipped external prospecting.
- AGENTS.md goal frame: the note is in scope because it covers KB navigation and context engineering.

**Curated heads (tags: type-system, context-engineering, document-system):**
- `kb/tags/type-system-README.md`: none of the three heads declares `complete: true`, so I did not skip any by-tag search. The source is already listed under "Type Roles". Its siblings (`type-system-enforces-metadata…`, `document-types-should-be-verifiable`, `directory-scoped-types-are-cheaper-than-global-types`, `why-notes-have-types`) were evaluated. The first two and the last are already linked. `directory-scoped-types` is about the cost of loading type specs, not routing by type, so I rejected it.
- `kb/tags/context-engineering-README.md`: flagged `definitions/context-engineering.md` (it defines routing as "deciding what knowledge is relevant before loading it"), `addressability-grain-sets-a-matched-selective-read-floor.md`, `context-efficiency-is-the-central-design-concern-in-agent-systems.md` and `design-for-the-first-time-human-except-on-access-cost.md`.
- `kb/tags/document-system-README.md`: flagged `title-as-claim-enables-traversal-as-reasoning.md` (titles are another hint available before opening) and `addressability-grain…` again.

**Body search (kb/theory/):**
- `rg -i "retrieval filter|progressive disclosure|structural hint|before (opening|loading)|without (opening|loading)|routing decision" kb/theory --glob '*.md'` returned these hits:
  - `agents-navigate-by-deciding-what-to-read-next.md`: the follow/skip decision model that the source's "routing decision" presupposes. Kept.
  - `agent-statelessness-makes-routing-architectural-not-learned.md`: argues the source's opening premise (stateless agents, routing as permanent architecture). Kept.
  - `pointer-design-tradeoffs-in-progressive-disclosure.md`: classes descriptions as fixed write-time pointers with staleness and low-specificity costs. Kept.
  - `link-following-and-search-impose-different-metadata-requirements.md`: says titles and descriptions are often all the agent has during search, while inline links carry their own context. Kept.
  - `two-context-boundaries-govern-operations-on-read-together-note-sets.md`: argues that descriptions become load-bearing for orientation in the middle regime, beyond per-document routing. Kept.
  - `addressability-grain-sets-a-matched-selective-read-floor.md`: already links to the source with `mechanism`, and says a description lowers the read floor only when it suffices for the routing decision. Kept as a reciprocal outbound edge.
  - `information-value-is-observer-relative.md`: its bullet "Descriptions as retrieval filters" has no link. Kept, with a return-link candidate.
  - `document-types-should-be-verifiable.md`: already linked. It cites `agents-navigate-by-deciding-what-to-read-next` for the same hint claim, which supports keeping that candidate.
  - `knowledge-storage-does-not-imply-contextual-activation.md`: lists "retrieval filters" only as one routing tool among many. Rejected as a keyword match.
  - `quality-signals-for-kb-evaluation.md`: its "pruning accuracy" signal measures link metadata against the follow decision. Rejected as a connection because it proposes a measurement and reports no evidence. Recorded in Flags as a test opportunity.
  - `title-as-claim-exposes-commitments…`, `title-as-claim-makes-overlap…` and `short-composable-notes…`: about titles or maintenance, not type/description routing. Rejected.
  - `skills-are-instructions-plus-routing-and-execution-policy.md`, `diagnostic-richness-constrains-outer-loop-learning-quality.md` and `soft-bound-traditions…`: use "progressive disclosure" in other contexts. Rejected.
- `rg` for "pre-existing signal" / type as a selector input (reached by reading `addressability-grain`, which links to it): `rule-based-context-selection-needs-a-pre-existing-signal.md` names "type" among rule-ready signals. Kept.

**Reverse-edge search (kb/reference/, kb/instructions/):**
- `rg "description|type" kb/reference/navigation.md`: line 25 says "Descriptions are the important middle layer… fixed, agent-facing filters between lexical search and full reads… This is why validation requires descriptions." The file links to theory rationale (pointer-design, two-context-boundaries) but not to the source. The reference `rests-on` label authorizes the edge. Kept as a reverse edge.
- `rg "navigat|routing|before open|structural hint" kb/reference/collections-and-types.md`: one hit, about collection routing conventions and not about type-as-hint. Rejected.
- `rg "retrieval filter|discriminat.*description|description.*discriminat" kb/instructions`: hits in `fix-warnings/fix-descriptions.md` (line 14: "Descriptions are the most important frontmatter field — they're retrieval filters that help agents decide whether to load the full note"), `review-gates/frontmatter/description-discrimination.md`, `cp-skill-write/SKILL.md:182` and `cp-skill-snapshot-web/SKILL.md:287`. `rg "theory/"` over the first two found no theory links. `fix-descriptions.md` restates the source's rationale nearly verbatim, so it is kept as a `rests-on` reverse edge. The gate and the two skills state a writing rule rather than rest on this argument. They are mentioned only in Rejected.
- Repository-wide `rg -l types-give-agents-structural-hints kb`: inbound links already exist from `addressability-grain…`, `why-notes-have-types`, `type-system-enforces-metadata…`, `kb/tags/type-system-README.md`, `kb/reports/retained/*` and `kb/work/*`. The `kb/work/` hits are excluded.

**Link following:**
- `addressability-grain…` → `rule-based-context-selection-needs-a-pre-existing-signal`, `pointer-design-tradeoffs…`.
- `pointer-design-tradeoffs…` → `agents-navigate…`, `agent-statelessness…`, `a-knowledge-base-should-support-fluid-resolution-switching` (rejected: too broad; reachable through pointer-design).
- `agent-statelessness…` → `context-efficiency-is-the-central-design-concern…` (rejected: reached through statelessness, too general to help as a direct hop).
- `link-following-and-search…` → `title-as-claim-enables-traversal-as-reasoning` (rejected as a connection; see Flags).
- Existence check: `kb/**/types/{spec,index,structured-claim}.md` matched only `kb/theory/types/structured-claim.md` (see Maintenance Observations).

### Candidate origins

- kb/theory/agents-navigate-by-deciding-what-to-read-next.md — body-search, link-following
- kb/theory/agent-statelessness-makes-routing-architectural-not-learned.md — body-search, link-following
- kb/theory/pointer-design-tradeoffs-in-progressive-disclosure.md — body-search, link-following
- kb/theory/link-following-and-search-impose-different-metadata-requirements.md — body-search
- kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md — body-search
- kb/theory/addressability-grain-sets-a-matched-selective-read-floor.md — curated-head, body-search
- kb/theory/rule-based-context-selection-needs-a-pre-existing-signal.md — link-following
- kb/theory/definitions/context-engineering.md — curated-head
- kb/theory/information-value-is-observer-relative.md — body-search
- kb/reference/navigation.md — body-search
- kb/instructions/fix-warnings/fix-descriptions.md — body-search

## Connections Found

- [Agents navigate by deciding what to read next](../../../../../../../../../../../../../theory/agents-navigate-by-deciding-what-to-read-next.md) -- **grounds**: the source's "informed routing decision" is that note's follow/skip decision under bounded context. That note also supplies the source's missing condition: a cue such as a type or description helps only when its diagnosticity repays its own context cost.
- [Agent statelessness makes routing architectural, not learned](../../../../../../../../../../../../../theory/agent-statelessness-makes-routing-architectural-not-learned.md) -- **grounds**: the opening premise ("agents are stateless… start fresh every session") is asserted without support. This note argues it and explains why type/description routing aids stay permanent architecture instead of being outgrown.
- [Pointer design tradeoffs in progressive disclosure](../../../../../../../../../../../../../theory/pointer-design-tradeoffs-in-progressive-disclosure.md) -- **extends**: it places descriptions among fixed write-time pointers (high availability, low specificity, can go stale). This bounds the source's claim that type and description let an agent narrow down "without opening any" document.
- [Link-following and search impose different metadata requirements](../../../../../../../../../../../../../theory/link-following-and-search-impose-different-metadata-requirements.md) -- **extends**: it scopes where type and description hints carry the whole decision. In search, they are often all the agent has. In link-following, surrounding prose and context phrases add hints the source does not mention.
- [Two context boundaries govern operations on read-together note sets](../../../../../../../../../../../../../theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md) -- **extends**: descriptions do more than filter one document at a time. Above the full-text boundary they become the compressed representation an agent uses to orient and plan sub-passes.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../../../../../../../../../../theory/addressability-grain-sets-a-matched-selective-read-floor.md) -- **mechanism**: it explains why routing by description saves reads. The description is addressable at a much finer grain than the body. It also states when the saving fails: the description must suffice for the routing decision. This reciprocal edge helps independently, because the source has no stated failure condition.
- [Rule-based context selection needs a pre-existing signal](../../../../../../../../../../../../../theory/rule-based-context-selection-needs-a-pre-existing-signal.md) -- **extends**: it separates the two halves of the source's hint pair. `type` is a rule-ready signal a deterministic selector can match. Choosing among same-type instances by description requires inferring relevance from content.
- [Context engineering](../../../../../../../../../../../../../theory/definitions/context-engineering.md) -- **defined-in**: the source uses "routing" in the technical sense this definition fixes (deciding relevance before loading), without a link.
- [Information value is observer-relative](../../../../../../../../../../../../../theory/information-value-is-observer-relative.md) -- **exemplifies**: types and descriptions are views of a document reshaped for the agent's "should I read this?" decision. They are an instance of that note's general claim about observer-shaped compression.

## Bidirectional Candidates

- [Information value is observer-relative](../../../../../../../../../../../../../theory/information-value-is-observer-relative.md) <-> source -- **extends** (from the target's side): its unlinked bullet "Descriptions as retrieval filters" under "How to present" could link to the source, which develops the routing argument behind that convention. The return path gives readers the type half of the hint pair.
- [Rule-based context selection needs a pre-existing signal](../../../../../../../../../../../../../theory/rule-based-context-selection-needs-a-pre-existing-signal.md) <-> source -- **exemplifies** (from the target's side): it names "type" as a rule-ready signal without saying where types come from or what they promise. The source supplies the case where a type signal is authored to serve routing.

## Reverse-edge Candidates

- [Navigation](../../../../../../../../../../../../../reference/navigation.md) → source -- **rests-on**: line 25 justifies required descriptions and description-built listings because descriptions are "fixed, agent-facing filters between lexical search and full reads". That design rests on the source's routing claim. It currently cites only pointer-design and two-context-boundaries as rationale.
- [Fix descriptions](../../../../../../../../../../../../../instructions/fix-warnings/fix-descriptions.md) → source -- **rests-on**: the procedure's rationale ("they're retrieval filters that help agents decide whether to load the full note") restates the source's claim and links no theory.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Title as claim enables traversal as reasoning](../../../../../../../../../../../../../theory/title-as-claim-enables-traversal-as-reasoning.md) -- titles are a parallel hint the agent sees before opening. No authorised label states that the source omits a neighbouring hint layer. `contrasts` would overstate the difference, so this goes to Flags instead.
- [Directory-scoped types are cheaper than global types](../../../../../../../../../../../../../theory/directory-scoped-types-are-cheaper-than-global-types.md) -- about the context cost of loading type specs, not about routing by a document's type.
- [Context efficiency is the central design concern in agent systems](../../../../../../../../../../../../../theory/context-efficiency-is-the-central-design-concern-in-agent-systems.md) -- the source's "context is finite and expensive" premise, but too general. It is reached through `agent-statelessness…`, which links to it.
- [Knowledge storage does not imply contextual activation](../../../../../../../../../../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- mentions retrieval filters only in a list of routing tools. Keyword match.
- [Quality signals for KB evaluation](../../../../../../../../../../../../../theory/quality-signals-for-kb-evaluation.md) -- its pruning-accuracy signal proposes a measurement and reports no evidence, so it cannot carry `evidenced-by`. See Flags.
- [A knowledge base should support fluid resolution-switching](../../../../../../../../../../../../../theory/a-knowledge-base-should-support-fluid-resolution-switching.md) -- broader resolution claim, reachable through pointer-design. A direct hop adds little.
- [Collections and types](../../../../../../../../../../../../../reference/collections-and-types.md) -- describes the path-valued type model, not routing by type. It is already reached through `why-notes-have-types`.
- `kb/instructions/cp-skill-write/SKILL.md`, `kb/instructions/cp-skill-snapshot-web/SKILL.md` and `kb/instructions/review-gates/frontmatter/description-discrimination.md` -- each states the "retrieval filter, not a summary" writing rule without leaning on this argument for a design choice. A `rests-on` edge from each would be link spray.

## Index Membership

- [Type system tag head](../../../../../../../../../../../../../tags/type-system-README.md) -- already listed under "Type Roles". No change.
- [Context engineering tag head](../../../../../../../../../../../../../tags/context-engineering-README.md) -- the source carries this tag but is not listed in the selective head. It could sit under "Core Claims" beside `addressability-grain…` as the routing claim for typed metadata. Optional, because the head declares itself selective.

## Synthesis Opportunities

None

## Maintenance Observations

- The source's examples name types that no longer exist as type specs. `spec` and `index` come from the retired flat enum described in `document-types-should-be-verifiable.md` ("What went wrong with flat types"). Only `kb/theory/types/structured-claim.md` resolves. `why-notes-have-types.md` (Navigation section) repeats the same three examples. Current examples include `kb/reference/types/adr.md` and `kb/types/generated-index.md`.
- `document-types-should-be-verifiable.md` line 14 still routes subject matter to an "`areas` field". That field looks retired in favour of `tags`; this was not verified further.
- The source's link text "description is the most important field" points to `kb/types/note.md`. That file says "Discriminating retrieval filter, not a summary" and never says "most important". The phrase survives in `kb/instructions/fix-warnings/fix-descriptions.md`. The link text slightly misattributes it.
- `kb/reference/navigation.md` labels its theory links `rationale:`. That label does not appear in the reference COLLECTION.md rows I matched (`rests-on`, `defined-in`, `see-also`), but I did not read the full table. Check it there.
- Validation: the invocation forbids repository-changing commands and gave this session no shell tool, so `commonplace-validate` was not run on this report. Relative links were computed for the report's actual location: 13 levels below `kb/`.

## Flags

- The source claims that type and description together let an agent narrow to the few documents it needs. It does not mention claim titles, which `title-as-claim-enables-traversal-as-reasoning` and `link-following-and-search…` treat as the first hint layer. A future edit could say how titles relate to the type/description pair, or scope the claim to frontmatter hints.
- The claim ("narrow from hundreds of files to the few it needs without opening any of them") is universal and has no stated failure condition. `addressability-grain…` (the description must suffice and be smaller than the body) and `pointer-design…` (fixed pointers go stale) supply bounds. `quality-signals-for-kb-evaluation`'s pruning-accuracy signal describes a test that could corroborate or refute it.
- Not a split candidate: the source makes one assertion.
