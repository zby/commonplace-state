---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/articles/what-bound-naurs-theory-to-programmers.md"
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: What bound Naur's theory to programmers

**Source:** [What bound Naur's theory to programmers](../../../../articles/what-bound-naurs-theory-to-programmers.md)

## Discovery Trace

The source has no `tags:` field, so no matching tag-README existed to read and no by-tag `rg` scan was applicable. Search scores were not available from the repo-local tools.

The source now authors reader-facing links to its Naur and Popper ingests; its basis, recovery, design-rationale, and review-narrowing notes; ADR 080; and all three sequel articles. Those existing edges were treated as traversal starts, not rediscovered candidates. The Argyris ingest remains lineage in `source_notes` but is no longer a reader-facing body link.

### `kb/notes/`

**Curated heads and listings:**

- Read `kb/notes/README.md`; the article's existing basis-note and design-rationale links routed into the program-theory, recovery, intended-contribution, revision, and theory-mediated-learning neighborhoods.
- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` for the complete fresh title surface, viewing the sorted output in bounded chunks.
- Ran `rg '^description:' kb/notes/ --glob '*.md'` for the collection-wide path-plus-description surface.

**Body searches:**

- `rg -n -i 'Naur|program theory|theory-holder|holding the theory|interpreter-plus|formulated criteria|unregenerable|intended contribution|single-loop|self-sealing|successor group' kb/notes/ --glob '*.md'`
- `rg -n -i 'face recogn|similarity judgment|grasp of similarity|analogical|trained (model|recognizer)|rule[- ]based|criteria.{0,30}formulat|formulat.{0,30}criteria|parametric' kb/notes/ --glob '*.md'`
- `rg -n -i 'repair.{0,40}claim|claim.{0,40}repair|narrowing.{0,40}review|defeated claim|rationale.{0,40}transfer|transfer.{0,40}rationale|theory-mediated|live theory|single-loop|double-loop|self-sealing|intended contribution' kb/notes/ --glob '*.md'`

**Candidate evaluation and link following:**

- Confirmed [Narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) as an existing link: it generalizes the article's two true-but-displaced repairs into a gate-only optimization failure and supplies contribution-preserving guards.
- Kept [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md): it develops why the maintainer's one-sentence statement of what the note was for could restore judgments that the artifact package did not determine.
- Kept [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md): it states the rationale condition under which critique can become premise-level repair rather than a defensible patch.
- Confirmed [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) as an existing link: it bounds Naur's compiler case as failure of a declared recovery source set, not proof of global inexpressibility or human-only authority.
- Followed the basis note to the recovery note and [Theory-mediated self-improvement needs both interpretation and retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md). The latter was rejected as a direct link because the article deliberately sends that constructive and reflective development through its sequel articles.
- Followed the design-rationale note to the specific-intent and selective-revision notes. [A bare writing prompt does not determine its intended contribution](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) was rejected as a narrower initial-commission case once the specific-intent note supplied the closer repair-time connection.
- Followed the narrowing note to the widening failure, warranted-reader-update, and citer-test neighborhood. Only the narrowing note directly explains the article's observed retreat toward the nearest defensible claim.
- Evaluated [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), the two-layer execution note, and the new representational-form/prototype note. They belong to what can be built after Naur's question is reopened, a scope the source already routes through the companion article.
- Confirmed that the article's existing basis and design-rationale links already provide the primary theoretical path; the kept candidates add distinct boundaries or mechanisms rather than restating those targets.

### `kb/reference/`

**Curated heads and listings:**

- Read `kb/reference/README.md`, including the review-system and repository-as-worked-case groups.
- Ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`.
- Ran `rg '^description:' kb/reference/ --glob '*.md'`.

**Body search:**

- `rg -n -i 'full improvement|pending revise|claim change|reconstruct.{0,30}brief|contribution|repair|Naur|theory[- ]holder|decision premise|composition test|transfer evidence' kb/reference/ --glob '*.md'`

**Candidate evaluation and link following:**

- Confirmed [ADR 080](../../../../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) as the exact operative record of the article's current-response claim; it is already linked in the source and was not repeated.
- Followed ADR 080 to the full-pass procedure and compared [Full improvement pass closure](../../../../reference/full-improvement-pass-closure.md). The closure document describes current final-byte reassessment, not the two historical repair failures, so it adds less than the already-authored ADR edge.
- Evaluated [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md). Its composition and transfer limits are compatible with the case, but its distinct tag-readme trace does not corroborate this article's repair episode closely enough for a direct link.
- Evaluated the per-artifact-write-brief and defeated-claim-disposition proposals. They are possible future system responses, not shipped detail needed to understand the article's current claim.

### `kb/sources/`

**Curated heads and listings:**

- Read `kb/sources/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` for the complete title surface in two sorted chunks.
- Ran `rg '^description:' kb/sources/ --glob '*.md'`.

**Body search:**

- `rg -n -i 'face recogn|analogical reasoning|similarity judgment|explicit criteria|formulated criteria|decision tree|unformulable|program theory|theory building|successor group' kb/sources/ --glob '*.md'`

**Candidate evaluation and link following:**

- Kept [Why LLMs can’t make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) as a contemporary practitioner application of Naur. Its billing case supports the importance of omitted design context while its analysis explicitly bounds the stronger conclusion that theory is necessarily human-only.
- Confirmed the Naur and Popper ingests as existing authored links. They remain the primary evidence for the article's attributions and were not repeated as candidates. The Argyris ingest remains in `source_notes`, but the compressed body no longer makes an Argyris attribution.
- Evaluated [Emergent Analogical Reasoning in Transformers](../../../../sources/emergent-analogical-reasoning-transformers.ingest.md), but rejected it as grounding for the bridge claim: its controlled task explicitly operationalizes relational structure and its prompted-LLM evidence is suggestive, not evidence that real program-modification similarity lacks a formulable rubric.
- Evaluated the intention and recent maintainability ingests around the repair episode. The specific-intent note already supplies the KB-level synthesis; only the modern Naur application creates a distinct source-facing reader need.

### `kb/agent-memory-systems/`

**Curated heads and listings:**

- Read `kb/agent-memory-systems/README.md`, including its comparison axes and system roster.
- Ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`.
- Ran `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.

**Body searches:**

- `rg -n -i 'Naur|programming as theory|program theory|theory building|decision rationale|why-memory|retained rationale|natural-language theory|holds? (a )?theory|theory-holder' kb/agent-memory-systems/ --glob '*.md'`
- `rg -n -i '\btheor(y|ies|etical)\b|rationale|intent|why' kb/agent-memory-systems/reviews/thalo.md kb/agent-memory-systems/reviews/gnosis.md kb/agent-memory-systems/reviews/compound-engineering-plugin.md kb/agent-memory-systems/agentic-memory-systems-comparative-review.md`

**Candidate evaluation:**

- Rejected [Gnosis](../../../../agent-memory-systems/reviews/gnosis.md): it is a concrete mechanism for retaining decisions, rejected alternatives, constraints, and intent, but its review supplies no behavioral evidence that an interpreter-plus-memory composite passes Naur's acquisition or reliability tests.
- Rejected [Thalo](../../../../agent-memory-systems/reviews/thalo.md): its synthesis story is explicitly outside the inspected core, so it cannot evidence theory possession.
- The comparative review and trace-learning cases describe memory or patch retention, not program-specific theory holding. The article makes no named system comparison on their axes, so broad topical overlap did not fire the collection trigger.

### `kb/agentic-systems/`

**Curated heads and listings:**

- Read `kb/agentic-systems/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`.
- Ran `rg '^description:' kb/agentic-systems/ --glob '*.md'`.

**Body search:**

- `rg -n -i 'Naur|programming as theory|program theory|theory building|decision rationale|retained theory|natural-language theory|theory-mediated|rationale' kb/agentic-systems/ --glob '*.md'`

**Candidate evaluation and link following:**

- Evaluated [Exo](../../../../agentic-systems/reviews/exo.md), whose editable substrate satisfies structural interpretation-and-retention conditions while its acceptance oracles do not establish reach. Rejected it here because it does not pass Naur's three theory-possession tests and the reflective sequel already owns that system comparison.
- No other whole-system analysis made a program-theory claim or compared systems on the article's formulated-criteria axis.

### `kb/articles/`

**Curated head and listings:**

- Read `kb/articles/README.md`; it already lists the source first in the four-article sequence.
- Ran `rg -N --no-heading -m1 '^# ' kb/articles/ --glob '*.md'`.
- Ran `rg '^description:' kb/articles/ --glob '*.md'`.
- Ran `rg -n -F 'what-bound-naurs-theory-to-programmers.md' kb/articles/ --glob '*.md'` to inspect authored return paths.
- Read the relevant sections of the Bitter Lesson and continual-learning articles to distinguish generic artifact-learning overlap from a direct use of this article's premise.

**Candidate evaluation and link following:**

- Confirmed [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) as a new authored return link. It already cites this source for the interpreter-plus-text division and applies that division to the distinct claim that continued concept formation need not occur only in weights.
- The source also links [Theory building inside the system](../../../../articles/theory-building-inside-the-system.md) and [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md); both already link back and were not repeated.
- Rejected [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) as a reverse-edge candidate. Its production-method-versus-form argument does not depend on Naur, and the later continual-learning article already carries the direct application and inbound link.
- The human-inclusive and atomic-steps articles have no distinct reader-facing development of this article's Naur claim.

### `kb/instructions/`

**Curated head and listings:**

- Read `kb/instructions/README.md`.
- Ran `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`.
- Ran `rg '^description:' kb/instructions/ --glob '*.md'`.
- Ran `rg -n -i 'full improvement|pending revise|claim-level|intended contribution|decision premise|Naur|theory-holder|rationale' kb/instructions/ --glob '*.md'`.

**Candidate evaluation:**

- The current full-pass and disposition procedures explain how an operator acts after the adopted ADR, but the article offers no concrete operational next step. The source collection's `procedure` trigger therefore did not fire; external readers already have the ADR as the durable account of the response.

### `kb/tasks/`

**Listings and body search:**

- `kb/tasks/` has no curated `README.md` or `COLLECTION.md` to read.
- Ran `rg -N --no-heading -m1 '^# ' kb/tasks/ --glob '*.md'`.
- Ran `rg '^description:' kb/tasks/ --glob '*.md'`.
- Ran `rg -n -i 'Naur|theory|rationale|full improvement|claim|repair|article' kb/tasks/ --glob '*.md'`.

**Candidate evaluation:**

- No active, backlog, completed, or recurring task gives an external reader a concrete next action on the article's claim.

### Excluded and external destinations

- Per `kb/articles/COLLECTION.md`, `kb/work/` and `kb/reports/` were excluded as durable article destinations. Hits there were not evaluated as connections.
- The `external` destination is authorized, but no external target was supplied or already loaded as a candidate. Open-web prospecting was skipped as required.

## Connections Found

- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- **extends**: the article reports that one sentence from the maintainer restored the missing repair direction; this note develops why an unrecoverable governing intent can act as a high-yield reconstruction seed while leaving contingent decision facts separate.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **extends**: the article separates successful critique from failed repair; this note states the missing condition that premise-level repair needs a faithful rationale exposing why the theory held and where it was expected to stop.
- [Why LLMs can’t make your code simpler](../../../../sources/why-llms-cant-make-your-code-simpler.ingest.md) -- **see-also**: this contemporary practitioner application of Naur supplies a concrete maintainability case in which omitted future-change and product premises matter, while the ingest's limits expose the stronger human-only conclusion as untested rather than settled.

## Bidirectional Candidates

None. The previous continual-learning return-link candidate is now authored in the source, and that article already links back.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A bare writing prompt does not determine its intended contribution](../../../../notes/a-bare-writing-prompt-does-not-determine-its-intended-contribution.md) -- genuine shared underdetermination, but rejected as a direct link because it concerns an initial bare commission; the specific-intent note gives the closer repair-time mechanism and already connects to it.
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- rejected because it develops the reflective arrangement after the article's reopened question, a scope already delegated to the companion and further articles.
- [Full improvement pass closure](../../../../reference/full-improvement-pass-closure.md) -- rejected because it documents the current one-cycle closing rule, while the already-linked ADR 080 directly records the historical repair failure and the adopted hand-back response.
- [Emergent Analogical Reasoning in Transformers](../../../../sources/emergent-analogical-reasoning-transformers.ingest.md) -- rejected as evidence for unformulated criteria because its synthetic task supplies explicit relational structure and its prompted-LLM transfer is only suggestive.
- [Gnosis](../../../../agent-memory-systems/reviews/gnosis.md) -- rejected because retaining why-memory is a candidate input to Naur's second test, not evidence that the composite passes acquisition or dispositional reliability.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- rejected because an editable self-description and weak acceptance gate do not establish possession of a program-specific theory, and the reflective sequel already owns the comparison.
- [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) -- rejected as a reverse edge because its categorical production-method argument stands without Naur; the continual-learning article is the distinct article that actually imports this source's premise.
- [Run a full improvement pass on one note](../../../../instructions/run-full-improvement-pass-on-note.md) -- rejected because the source does not offer a concrete operator next step and already links the decision record that explains the machinery's response.

## Index Membership

None. The source is already listed in [Articles](../../../../articles/README.md) as the first article in the four-part draft sequence, and no other curated article index was found.

## Synthesis Opportunities

None.

## Maintenance Observations

- The article's bridge argument depends on the empirical assertions that trained face recognizers make a relevant similarity judgment without a formulable rubric and that a language model can make the corresponding program-demand judgment. The current `kb/sources/` corpus has no retained analysis that directly grounds both steps; the analogical-reasoning ingest was rejected because its task operationalizes the relation and does not test this transfer.
- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) has a filename preserving its superseded “documentation generates the system” claim while its current H1 and description state a different recovery claim. The mismatch degrades title-surface traversal and should be handled by a later explicit relocation or maintenance pass.
- `kb/articles/COLLECTION.md` authorizes outbound `procedure` links to `kb/tasks/`, but `kb/tasks/` has neither a curated `README.md` nor a `COLLECTION.md`. Outbound task candidates can be prospected by title/body, but reverse-edge authorization from tasks cannot be evaluated without inventing rules.

## Flags

None.
