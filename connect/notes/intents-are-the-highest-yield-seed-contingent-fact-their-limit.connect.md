---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/intents-are-the-highest-yield-seed-contingent-fact-their-limit.md"
source_has_frontmatter: true
date: "2026-08-25"
depth: standard
---

# Connection Report: Specific intent and contingent facts

**Source:** [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md)

## Discovery Trace

**Setup and source contract:**
- Read `.agents/skills/cp-skill-connect/SKILL.md`, `kb/cache/types/connect-report.md`, `kb/notes/COLLECTION.md`, and the full source note before candidate discovery.
- Source collection is `notes`. The notes outbound section authorizes local prospecting in `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`; excludes `kb/work/`; and authorizes `external` only for already-known targets. No external target was supplied, so external prospecting was skipped.
- Source claim: a specific unrecoverable governing intent is a conjecturally high-yield seed for reconstructing local rationale, but it does not regenerate contingent facts such as selected alternatives, project-specific world forces, observations, applicability limits, or arbitrary conventions.

**Notes destination:**
- Curated heads read: `kb/notes/README.md`, `kb/notes/document-system-README.md`, and `kb/notes/context-engineering-README.md`. Neither matching tag README declares `complete: true`, so by-tag scans were run.
- Ran title surface: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`.
- Ran description listings: `rg '^description:' kb/notes/ --glob '*.md'`; `rg -l '^tags:.*\bdocument-system\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`; `rg -l '^tags:.*\bcontext-engineering\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`.
- Ran body searches: `rg -n "intent|intention|purpose" kb/notes/ --glob '*.md'`; `rg -n "rationale|design rationale|local rationale" kb/notes/ --glob '*.md'`; `rg -n "contingent fact|contingent facts|selected alternative|decision status|decision premise" kb/notes/ --glob '*.md'`; `rg -n "regenerate|recoverable|unrecoverable|not faithfully recoverable" kb/notes/ --glob '*.md'`.
- Link/backlink following: `rg -n "intents-are-the-highest-yield-seed-contingent-fact-their-limit|A specific intent may out-yield|Intents are the highest-yield" kb/notes kb/reference kb/types kb/agent-memory-systems kb/agentic-systems kb/sources kb/instructions --glob '*.md'` found existing inbound links from the parent retained-design-theory note, `content-routing.md`, ADR 077, and the Naur ingest. Loaded and evaluated `linked-note-durable-payload-is-what-consumption-path-cannot-supply.md`, `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md`, `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md`, `opposed-recompute-factors-do-not-decide-documentation-segmentation.md`, `retaining-the-episode-keeps-a-distilled-rule-re-derivable.md`, `mixed-epistemic-status-must-be-preserved-below-the-document-level.md`, and `addressability-grain-sets-a-matched-selective-read-floor.md`.

**Types destination:**
- Curated head read: `kb/types/README.md`.
- Ran title and description listings: `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`; `rg '^description:' kb/types/ --glob '*.md'`.
- Ran body search: `rg -n "intent|contingent|rationale|regenerate|recoverable|decision premise" kb/types/ --glob '*.md'`.
- Loaded `kb/types/instruction.md`. Kept it as a source-to-types `evidenced-by` candidate because the type contract is a concrete system-definition witness for the source note's instruction-specific implication: retain the goal, keep per-step rationale minimal, and put durable reasoning in notes.

**Reference destination:**
- Curated head read: `kb/reference/README.md`.
- Ran title and description listings: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`; `rg '^description:' kb/reference/ --glob '*.md'`.
- Ran body search: `rg -n "intent|contingent|rationale|regenerate|recoverable|decision premise" kb/reference/ --glob '*.md'`.
- Loaded `kb/reference/content-routing.md` and `kb/reference/adr/077-content-routing-by-regeneration-source-and-consumer.md`. Rejected both as new outbound candidates: the source already links to `content-routing.md`, and ADR 077 already records the reverse dependency on this note.

**Agent-memory-systems destination:**
- Curated head read: `kb/agent-memory-systems/README.md`.
- Ran title and description listings: `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`; `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`.
- Ran body search: `rg -n "intent|contingent|rationale|regenerate|recoverable|decision premise" kb/agent-memory-systems/ --glob '*.md'`.
- Evaluated hits including `trace-learning-techniques-in-related-systems.md`, `reviews/REM.md`, `reviews/hindsight.md`, `reviews/hyperagents.md`, `reviews/swamp.md`, and `lightweight/IsaacCLupus_mnemosyn_spec.md`. Rejected them as review-specific observations about intent fields, extracted rationale, or regenerated views rather than direct support for the source note's intent-yield and contingent-fact boundary.

**Agentic-systems destination:**
- Curated head read: `kb/agentic-systems/README.md`.
- Ran title and description listings: `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`; `rg '^description:' kb/agentic-systems/ --glob '*.md'`.
- Ran body search: `rg -n "intent|contingent|rationale|regenerate|recoverable|decision premise" kb/agentic-systems/ --glob '*.md'`.
- Evaluated hits in `swamp.md`, `exo.md`, `eigenius.md`, and `gbrain.md`. Rejected them: they show operational intent, regeneration, or justification pipelines in agentic systems, but no specific reader-useful edge to this retained-design-theory ranking.

**Sources destination:**
- Curated head read: `kb/sources/README.md`.
- Ran title and description listings: `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`; `rg '^description:' kb/sources/ --glob '*.md'`.
- Ran body search: `rg -n "intent|contingent|rationale|regenerate|recoverable|decision premise" kb/sources/ --glob '*.md'`.
- Loaded `programming-as-theory-building.ingest.md` and `intention-is-all-you-need-2022428696595108152.ingest.md`. The Naur ingest is already linked from the source and already links back. The Slotnick ingest was rejected as a direct candidate: it treats intention as a coordination surface and purpose input to theory, but does not bear on the source note's same-budget yield conjecture or contingent-fact boundary.

**Instructions destination:**
- Curated head read: `kb/instructions/README.md`.
- Ran title and description listings: `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`; `rg '^description:' kb/instructions/ --glob '*.md'`.
- Ran body search: `rg -n "intent|contingent|rationale|regenerate|recoverable|decision premise" kb/instructions/ --glob '*.md'`.
- Evaluated hits in `cp-skill-write/SKILL.md`, `cp-skill-write-multistage/SKILL.md`, `run-full-improvement-pass-on-note.md`, and compression/review instructions. Rejected them as operational variants or downstream applications of retained-intent handling; the sharp evidence surface for this source note's instruction implication is the global `instruction` type contract.

## Connections Found

- [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) -- **extends**: applies the same recoverability boundary at note-composition grain, where the durable payload is the recognition anchor, local fact, or rationale the consumption path cannot supply.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- **contrasts**: bounds the source note's intent-over-local-rationale conjecture by showing a case where retained rationale is the antecedent that makes a transfer claim testable.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **contrasts**: shows that some rationale is not a low-yield explanatory snippet but the surface that lets a retained theory be repaired at the premise that broke.
- [Instruction](../../../../types/instruction.md) -- **evidenced-by**: the type contract implements the instruction-specific implication of the source note by requiring a goal first, treating it as the only rationale the body keeps, and routing durable reasoning to notes.

## Bidirectional Candidates

- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) <-> source -- **contrasts**: a return link would help readers of the retained-rationale transfer note distinguish rationale-as-test-antecedent from intent-as-high-yield-reconstruction-seed.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Content routing](../../../../reference/content-routing.md) -- Rejected as a new outbound candidate because the source already carries this `see-also` edge.
- [077-Content routing by regeneration source and consumer](../../../../reference/adr/077-content-routing-by-regeneration-source-and-consumer.md) -- Rejected as a new source-to-reference edge because the ADR already records the reverse dependency on this note, and another source-side `see-also` would duplicate the applied table path.
- [Ingest: Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) -- Rejected as a new candidate because the source already cites it inline and the ingest already links back.
- [Ingest: Intention Is All You Need](../../../../sources/intention-is-all-you-need-2022428696595108152.ingest.md) -- Rejected because it supports intent as a coordination/purpose surface, not the source note's specific per-token yield conjecture or contingent-fact limit.
- [Opposed recompute factors do not decide documentation segmentation](../../../../notes/opposed-recompute-factors-do-not-decide-documentation-segmentation.md) -- Rejected as direct edge: it excludes unregenerable intent and decisions from cache pricing, but the source's parent retained-design-theory path already carries that cache boundary.
- [Addressability grain, not compression ratio, sets a matched selective-read floor](../../../../notes/addressability-grain-sets-a-matched-selective-read-floor.md) -- Rejected as too retrieval-economics-specific; its recovery-failure caveat is adjacent but does not add a distinct reader need for the intent-yield note.
- [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- Rejected because its episode/rule retention layers are about evidence-backed re-derivation, not governing intent versus contingent fact.
- [Mixed epistemic status must be preserved below the document level](../../../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md) -- Rejected because the source already marks its conjectural and boundary claims locally; document-level warrant preservation is too broad for a useful direct edge.
- `kb/agent-memory-systems/` hits such as `reviews/REM.md`, `reviews/hindsight.md`, and `reviews/hyperagents.md` -- Rejected because they report system-specific retained intent or rationale artifacts without testing or directly exemplifying the source note's ranking.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) -- Rejected because agent-authored operational intent compiled into workflows is a symbolic-execution case, not evidence for which retained design-theory residue has the highest reconstruction yield.
- `kb/instructions/cp-skill-write/SKILL.md`, `kb/instructions/cp-skill-write-multistage/SKILL.md`, and `kb/instructions/run-full-improvement-pass-on-note.md` -- Rejected as direct instruction candidates because they are operational variants of retained-intent handling, while `kb/types/instruction.md` is the cleaner corroborating contract for this note's goal/rationale implication.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) -- The source belongs in the curated context-engineering head because it states which design-understanding payloads should be retained rather than regenerated under bounded context.
- [Document system](../../../../tags/document-system-README.md) -- The source belongs in the document-system head because it supplies a document-content retention rule for design rationale: keep governing intent and contingent facts, not every recoverable per-part rationale.

## Synthesis Opportunities

The source plus [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md), [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md), and [A linked note's durable payload is what its consumption path cannot reliably supply](../../../../notes/linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) suggest a synthesis note on roles of retained rationale. The higher-order claim would separate intent as a reconstruction seed, rationale as a transfer antecedent, rationale as a repair surface, and local facts as consumption-path payloads, instead of treating "rationale" as one retention class.

## Maintenance Observations

Existing inbound links still use the older stronger title text "Intents are the highest-yield retained seed, and contingent fact is their limit" or a close variant, while the current H1 is "A specific intent may out-yield local rationales, but contingent facts stay separate." The stale link text appears in `kb/notes/a-retained-design-theory-is-what-the-interpreter-cannot-regenerate.md`, `kb/reference/adr/077-content-routing-by-regeneration-source-and-consumer.md`, and `kb/sources/programming-as-theory-building.ingest.md`; future link maintenance should decide whether to keep the old summary wording or update it to the softened current claim.

## Flags

None
