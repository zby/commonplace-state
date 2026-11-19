---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/model-absorption-threatens-only-the-generalizable-half.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: Model absorption threatens only the generalizable half of a retention layer

**Source:** [Model absorption threatens only the generalizable half of a retention layer](../../../notes/model-absorption-threatens-only-the-generalizable-half.md)

## Discovery Trace

### Authorisation and source reading

- Read `kb/notes/COLLECTION.md`. It authorises prospecting in `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; excludes `kb/work/`; and authorises `external` only for already-known targets. No new external target was supplied or present in loaded context, so open-web prospecting was skipped.
- The source has frontmatter. Its central cut is indexicality: generalizable facts can eventually be supplied by model capability, while deployment-local commitments, current state, evidence, provenance, and authority cannot be reconstructed unaided. Its three mechanisms are missing information, currency, and addressability/authority; its downstream claims concern amortization and mixed-artifact retirement costs.

### Notes

**Curated heads and listings:**

- Read `kb/notes/README.md`, `learning-theory-README.md`, `agent-memory-README.md`, `deploy-time-learning-README.md`, and `foundations-README.md`. None declares `complete: true`; `learning-theory-README.md` declares `covered_by` rather than complete membership, so no by-tag scan was skipped.
- Generated the full title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and the full description surface with `rg '^description:' kb/notes/ --glob '*.md'`.
- Ran tag description scans for all four source tags with `rg -l "^tags:.*\\bTAG\\b" kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''`, substituting `learning-theory`, `agent-memory`, `deploy-time-learning`, and `foundations` for `TAG`.

**Body searches:**

- `rg -n -i 'absorb|absorption|internaliz|model (already )?(knows|know)|weights' kb/notes/ --glob '*.md'`
- `rg -n -i 'local state|deployment-local|current local|commitment|provenance|authority' kb/notes/ --glob '*.md'`
- `rg -n -i 'continual pretraining|continual learning|training corpus|model release|capability floor' kb/notes/ --glob '*.md'`
- `rg -n -i 'amortiz|decay curve|go(es|ing) redundant|obsolete|obsolescence' kb/notes/ --glob '*.md'`
- `rg -n 'model-absorption-threatens-only-the-generalizable-half|Model absorption threatens only the generalizable half' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` found no inbound links.

**Candidate evaluation and link following:**

- Kept [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md): it values retained facts and theories by generality/explanatory-reach, while the source shows that absorbability cross-cuts that axis. The difference changes retention decisions rather than merely sharing vocabulary.
- Kept [Ephemerality is safe where embedded operational knowledge has low explanatory-reach](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md): it predicts persistence from cross-context reach, while the source predicts external-copy durability from indexicality. The notes expose a real tension for high-reach general rules that a model later supplies unaided.
- Rejected [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) as an additional outbound edge: its three-form frame is already reachable through the source's links to the readable-artifact and continual-learning notes, and the new edge would add adjacency rather than a distinct reader need.
- Rejected [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) as redundant with the source's existing, more directly load-bearing link to `only-explicit-retention-is-durable-writable-and-addressable.md`.
- Rejected [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md): “current state” is a lexical overlap, but that note classifies memory surfaces rather than explaining resistance to model absorption.
- Rejected [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md): its cold-session assumption is narrower and relaxable via persistent memory, while the source's local-information claim is about unavailable facts under arbitrary capability.
- Followed the promising neighborhood through the source's existing links and the candidate footers into `bitter-lesson-selects-against-unearned-reach-not-against-structure.md`, `theory-mediated-self-improvement-needs-interpretation-and-retention.md`, `readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md`, `system-definition-artifacts-are-crystallized-reasoning-under-context.md`, and `only-explicit-retention-is-durable-writable-and-addressable.md`. This exposed four useful return paths and confirmed that the explanatory-reach tension is not already resolved in either candidate.

### Reference

**Curated head and searches:**

- Read `kb/reference/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` and `rg '^description:' kb/reference/ --glob '*.md'`.
- Ran the same four focused body-search expressions listed above against `kb/reference/`.
- Rejected [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md): it records that this repository places provider weights outside its declared boundary, but that local boundary choice neither corroborates nor explains the source's general indexicality mechanism.
- No reference artifact passed the articulation test.

### Agent-memory systems

**Curated head and searches:**

- Read `kb/agent-memory-systems/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'` and `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Ran the same four focused body-search expressions listed above against `kb/agent-memory-systems/`.
- Kept [Agent-R](../../../../agent-memory-systems/reviews/agent-r.md): its code-grounded trace-to-checkpoint pipeline gains context compression while losing per-lesson provenance, targeted recall, and invalidation at the operative parametric endpoint. This is concrete evidence for the source's authority/addressability half, not evidence that all local facts resist training.
- Followed Agent-R's comparison and read-back sections through its links to lineage, behavioral authority, and explicit-retention theory; those links confirmed that the source adds the missing content-class cut rather than duplicating the review's representational-form comparison.

### Agentic systems

**Curated head and searches:**

- Read `kb/agentic-systems/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Ran `rg -n -i 'state|history|provenance|weights|checkpoint|commitment|local' kb/agentic-systems/ --glob '*.md'` after the four cross-collection body queries exposed no title-level match.
- Kept [Exo](../../../../agentic-systems/reviews/exo.md): its inspected architecture deliberately leaves harness policy rewritable while protecting canonical state, secrets, lifecycle, and failed-attempt history. That is a worked system boundary closely matching the source's generalizable-policy/local-state split.
- Followed Exo's bitter-lesson and theory-mediated-self-improvement links. They confirmed that Exo's protected substrate is an independent implementation case and that the source supplies the unmade indexicality explanation.

### Sources

**Curated head and searches:**

- Read `kb/sources/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'` and `rg '^description:' kb/sources/ --glob '*.md'`.
- Ran the same four focused body-search expressions listed above against `kb/sources/`.
- Kept the authored companion [Ingest: We Should Take Text Optimization More Seriously](../../../../sources/we-should-take-text-optimization-more-seriously.ingest.md), which explicitly routes stable, repeatedly useful information toward weights and volatile, local, auditable, or not-yet-trusted information toward text. Its own limitations classify it as editorial corroboration, not independent empirical proof.
- Rejected the paired raw snapshot as a regular target because `kb/sources/` provides the `.ingest.md` authored surface. The source's two already-authored source links were not repeated as candidates.
- Following the ingest's cluster links led to the already-read substrate-coevolution and readable-artifact notes and reinforced the return-link candidates below.

### Instructions

**Curated head and searches:**

- Read `kb/instructions/README.md`; generated `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'` and `rg '^description:' kb/instructions/ --glob '*.md'`.
- Ran the same four focused body-search expressions listed above against `kb/instructions/`.
- No procedure adds ordering, defaults, or stopping conditions that operationalize the source's content-class distinction. Keyword hits in retirement, review, and improvement procedures concern artifact lifecycle or command behavior, so no `operationalized-from` or rare `see-also` edge passed the articulation test.

## Connections Found

- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) — **contrasts**: that note grades retained knowledge by explanatory-reach and capacity gain, while this source shows that external-copy durability is orthogonal — a low-reach local fact may be irreplaceable and a high-reach general theory may be absorbed.
- [Ephemerality is safe where embedded operational knowledge has low explanatory-reach](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) — **contrasts**: both predict when preservation pays, but one uses cross-context explanatory-reach and the other uses deployment indexicality; following both exposes the unresolved case of a high-reach general rule that models learn to supply unaided.
- [Ingest: We Should Take Text Optimization More Seriously](../../../../sources/we-should-take-text-optimization-more-seriously.ingest.md) — **evidenced-by**: the essay independently proposes nearly the same routing cut — stable, repeated information may move into weights, while volatile, local, auditable, or not-yet-trusted information remains in text — while its ingest correctly bounds this as conceptual corroboration.
- [Agent-R](../../../../agent-memory-systems/reviews/agent-r.md) — **evidenced-by**: this code-grounded trace-to-checkpoint system demonstrates the source's authority tradeoff: parametric compression removes runtime context cost but makes per-lesson provenance, selective recall, and invalidation unavailable at consumption.
- [Exo](../../../../agentic-systems/reviews/exo.md) — **evidenced-by**: this code-grounded self-modifying harness makes policy rewritable while protecting canonical state, secrets, lifecycle, and failed-attempt history, a concrete system boundary matching the source's generalizable-policy versus deployment-local-state cut.

## Bidirectional Candidates

- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) → source — **grounds**: its explicit concession that scale might absorb the retention half creates a reader need for this source's narrower rebuttal about deployment-indexed content.
- [The readable-artifact loop is the tractable unit for continual learning](../../../../notes/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md) → source — **grounds**: it asserts that deployment-specific natural-language knowledge survives whatever the opaque loop absorbs; this source is the missing argument for that assertion.
- [System-definition artifacts are crystallized reasoning under context scarcity](../../../../notes/system-definition-artifacts-are-crystallized-reasoning-under-context.md) → source — **extends**: its unbounded-context thought experiment preserves authority-bearing constraints while conceding the model may know their underlying facts; this source develops the capability-side case that local facts themselves are unavailable.
- [The bitter lesson selects against unearned reach, not against structure](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) → source — **contrasts**: the symmetric return path would warn readers that earning a general claim's reach protects the structure's truth but not the external copy from becoming redundant once scale converges on it.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Treat continual learning as substrate coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) — broader form-level adjacency already reachable through the source's existing continual-learning links; no additional reader need.
- [Reflection buys addressability](../../../../notes/reflection-buys-addressability.md) — valid premise but redundant with the source's more direct existing explicit-retention ground.
- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — shares “current state” vocabulary but answers a different memory-surface classification question.
- [Agent statelessness makes routing architectural, not learned](../../../../notes/agent-statelessness-makes-routing-architectural-not-learned.md) — rests on a narrower cold-session assumption and does not establish the source's arbitrary-capability information gap.
- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) — repository-specific placement of provider weights outside the boundary, not evidence for the general absorbability cut.

## Index Membership

- [deploy-time-learning](../../../../tags/deploy-time-learning-README.md) — add under “Learning fundamentals”: the source explains why deploy-time retention remains structurally necessary for local state even as model capability absorbs general exposition.
- [Agent memory](../../../../tags/agent-memory-README.md) — add under “Boundaries And Failure Modes”: the source gives memory designers a content-level test for which retained material faces capability-driven redundancy and which remains deployment-local ground truth.

## Synthesis Opportunities

- [Model absorption threatens only the generalizable half](../../../notes/model-absorption-threatens-only-the-generalizable-half.md), [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md), and [Ephemerality is safe where embedded operational knowledge has low explanatory-reach](../../../../notes/ephemerality-is-safe-where-embedded-operational-knowledge-has-low.md) together imply that retention economics needs two independent tests: explanatory-reach measures how many future contexts benefit from a resolution, while indexicality measures whether the current system can reconstruct that resolution unaided. A high-reach general theory and a low-reach local fact occupy opposite cells; neither axis subsumes the other.

## Maintenance Observations

None

## Flags

- **Unresolved tension:** the ephemerality note says structural explanatory-reach survives AI-assisted re-derivation “somewhere,” while the source says model agreement can make an external copy cease to be causally load-bearing. The synthesis above may reconcile survival of the knowledge with redundancy of a particular copy, but the two notes do not currently state that distinction together.
- **Split candidate:** the source meets the report contract's review trigger by supporting at least five genuine new connections across learning theory, source evidence, external memory systems, and agentic-system architecture while making separable claims about information availability, currency, authority, amortization, and mixed-artifact lifecycle. A future writer should test whether the two-class theorem and its document-maintenance consequences remain more composable as one note or as a lemma plus application; this is not an automatic split recommendation.
