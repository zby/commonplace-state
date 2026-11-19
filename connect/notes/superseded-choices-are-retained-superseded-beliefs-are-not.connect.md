---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/superseded-choices-are-retained-superseded-beliefs-are-not.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: Superseded choices are retained; superseded beliefs are not

**Source:** [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md)

## Discovery Trace

**Notes destination**

- Curated heads read: [README](../../../../notes/README.md), [Tags](../../../../tags/README.md), [artifact-analysis](../../../../tags/artifact-analysis-README.md), [KB maintenance](../../../../tags/kb-maintenance-README.md), and [Foundations](../../../../tags/foundations-README.md). `artifact-analysis-README.md` is marked `complete: true`, so the by-tag `rg` sweep for `artifact-analysis` was skipped per contract. The source was already curated there; it was absent from the curated heads of `kb-maintenance` and `foundations`.
- Full titles listing: `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`. Reviewed hits around `supersed`, `history`, `belief`, `choice`, `retain`, `archive`, `rewrite`, and `artifact`. Kept [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md), [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md), [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md), and [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md). Rejected [Mixed epistemic status must be preserved below the document level](../../../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md) as warrant-classification rather than retention-standing, and [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) as about operations on addressable commitments rather than what displaced content must retain.
- Description listing scan: `rg '^description:' kb/notes/ --glob '*.md' | rg 'supersed|belief|history|retain|retention|choice|maintenance|rewrite|episode|epistemic|archive|standing|decision|witness'`. Confirmed the same cluster plus [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) as neighborhood context; rejected that one as too general once [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) supplied the sharper authoritative-witness constraint.
- Tag listings: `rg -l '^tags:.*\bkb-maintenance\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''` and `rg -l '^tags:.*\bfoundations\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`. `kb-maintenance` surfaced the maintenance-regime neighborhood and supported a curated-head membership candidate; `foundations` surfaced overlap with record/authority notes but no stronger missing connection than the notes already kept.
- Body search: `rg -n 'supersed|refut|belief|histor|witness|retention|choice event|expired prescription|mixed epistemic|episode retention|holistic rewrite|append|append-only|decision record|ADR|history' kb/notes/ --glob '*.md'`. This separated the retained-witness notes from nearby but looser hits such as [A compact, refreshable whole-picture narrative can replace infeasible fragment reconciliation](../../../../notes/evolving-understanding-needs-holistic-rewrite-not-composition.md), which the source already cites, and exposed [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md) as the bridge to the more specific decision-surface note.
- Link following: followed the source's existing links through [History has one chance to become checkable](../../../../notes/history-has-one-chance-to-become-checkable.md), [Commitment, not derivation, creates new ground truth](../../../../notes/commitment-not-derivation-creates-new-ground-truth.md), and [Artifact classification separates content kind, lineage, and authority](../../../../notes/artifact-classification-separates-content-kind-lineage-and-authority.md). That route reinforced the kept candidates above and showed no stronger missing note-to-note link beyond them.

**Reference destination**

- Curated head read: [Reference](../../../../reference/README.md).
- Full titles listing: `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`. Reviewed titles around `history`, `choice`, `archive`, `proposal`, `rationale`, `retention`, and `supersedes`.
- Description/body search: `rg '^description:' kb/reference/ --glob '*.md' | rg 'history|histor|choice|decision|archive|proposal|adr|rationale|retention|supersed|state|witness'` and `rg -n 'supersed|archive|histor|choice event|retention|proposal|ADR 056|alternatives|rationale|decision record|witness' kb/reference/ --glob '*.md'`. Kept [070-Notes bind choices; reference records Commonplace selections and state](../../../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md) as a reciprocal candidate because it already rests on the source and applies the same distinction at collection-boundary level. Kept [056-Adopted and retired proposals archive out of the frontier](../../../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) as a reverse-edge candidate because its archive/delete boundary is a concrete instance of the source's rule. Evaluated [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) as a real companion but moved it to off-authorisation: the connection is stronger than `see-also`, yet the notes→reference authorised set offers no descriptive-companion label.
- Link following: followed the source's inline reference to ADR 056, then searched for existing references back to the source. This surfaced ADR 070's existing `rests-on` edge, which makes the missing source→ADR 070 return path independently useful rather than redundant.

**Instructions destination**

- Curated head read: [Instructions](../../../../instructions/README.md).
- Full titles and search scans: `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`, `rg '^description:' kb/instructions/ --glob '*.md' | rg 'retire|supersed|archive|history|decision|proposal|artifact|review|maintenance'`, and `rg -n 'retire|supersed|archive|history|proposal|artifact|choice|belief|witness' kb/instructions/ --glob '*.md'`.
- Kept [Retire an artifact](../../../../instructions/retire-artifact.md) as a reverse-edge candidate: Step 1's archive-vs-delete test operationalizes the same distinction between preserving a displaced choice witness and refusing to keep displaced claims alive just because they once governed.
- Rejected [Resolve a full-pass disposition](../../../../instructions/resolve-full-pass-disposition.md) as packet-lifecycle handling rather than subject-matter standing, and [Migrate a directional link label](../../../../instructions/migrate-directional-link-label.md) as history-preservation for corpus migration rather than belief-vs-choice retention.

**Agent-memory-systems destination**

- Curated head read: [Agent Memory Systems](../../../../agent-memory-systems/README.md).
- Description/body search: `rg '^description:' kb/agent-memory-systems/ --glob '*.md' | rg 'retire|supersed|history|trace|episode|archive|lifecycle|retention|decision|proposal'` and `rg -n 'retire|supersed|history|trace|episode|archive|lifecycle|retention|decision|proposal' kb/agent-memory-systems/ --glob '*.md'`.
- Kept [kgai](../../../../agent-memory-systems/reviews/kgai.md): its append-only decision log, explicit `SUPERSEDES` chain, and head-only recall policy are a direct external witness for the source's claim that superseded choices keep historical standing while expired guidance leaves the active frontier.
- Rejected broad trace-lifecycle hits such as [REM](../../../../agent-memory-systems/reviews/REM.md) and [Graphiti](../../../../agent-memory-systems/reviews/graphiti.md): they manage episodes, facts, and invalidation, but not the sharper question of when a displaced artifact remains true only as a historical witness.

**Agentic-systems destination**

- Curated head read: [Agentic Systems](../../../../agentic-systems/README.md).
- Search scans: `rg '^description:' kb/agentic-systems/ --glob '*.md' | rg 'retire|supersed|history|trace|episode|archive|lifecycle|retention|decision|proposal'` and `rg -n 'retire|supersed|history|trace|episode|archive|lifecycle|retention|decision|proposal' kb/agentic-systems/ --glob '*.md'`.
- Rejected [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) and [Exo](../../../../agentic-systems/reviews/exo.md): both expose retirement/rollback or retained-attempt history, but neither is primarily about the truth-role asymmetry between superseded choices and refuted beliefs. No agentic-systems candidate passed the articulation test strongly enough to keep.

**Skipped destinations**

- `kb/types/`: no plausible target after the notes/reference pass; the relevant ADR-type witness already appears through [ADR](../../../../reference/types/adr.md), which the source already cites from `kb/reference/`.
- `kb/sources/`: no already-known source artifact in loaded context carried the note's argument more directly than the local Commonplace witnesses; the note is not source-derived in the lineage sense.
- `external`: not prospectable under the skill, and no already-supplied external target was in scope.

## Connections Found

- [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) -- **extends**: both distinguish current authority from retained historical evidence; this note widens the source's choice-event witness rule into a general episode/rule retention architecture.
- [Bottom-up structure inference needs capture at the decision surface, not the state](../../../../notes/structure-inference-needs-capture-at-the-decision-surface.md) -- **mechanism**: explains why the choice event's "why" must be captured at production time for the witness the source requires to remain reconstructible later.
- [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) -- **grounds**: sharpens what counts as the source's required "reliable witness" by ruling out mere content reproduction without stable identity, contestability, and governed supersession.
- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- **extends**: gives the belief-side complement to the source's standing boundary by separating case-level historical retention from renewed endorsement of the old explanation as current truth.
- [kgai](../../../../agent-memory-systems/reviews/kgai.md) -- **evidenced-by**: supplies an external worked case where superseded engineering decisions remain in append-only history while only current head decisions enter ordinary recall.

## Bidirectional Candidates

- [070-Notes bind choices; reference records Commonplace selections and state](../../../../reference/adr/070-notes-bind-choices-reference-records-selections-and-state.md) <-> source -- **evidenced-by**: the ADR already rests on the source from the reference side, and the source would gain a concrete record of its distinction being adopted as an explicit collection-boundary rule.

## Reverse-edge Candidates

- [056-Adopted and retired proposals archive out of the frontier](../../../../reference/adr/056-adopted-and-retired-proposals-archive-out-of-the-frontier.md) → source -- **rests-on**: its archive/delete boundary is a concrete case of preserving a superseded choice event while refusing to keep expired guidance live.
- [Retire an artifact](../../../../instructions/retire-artifact.md) → source -- **rests-on**: Step 1's archive-vs-delete rule operationalizes the same distinction between surviving decision witnesses and displaced claims that should not retain standing.

## Off-authorisation Candidates

- [Design rationale management in Commonplace](../../../../reference/design-rationale-management.md) -- the source connects because it explains which Commonplace surfaces retain displaced design rationale, but notes→reference only authorizes `evidenced-by`, `derived-from`, `abstracted-from`, and sparse `see-also`; none cleanly names "descriptive operational companion to the same retention boundary." Suggest extending the notes→reference authorised set or rejecting the edge as too adjacent.

## Raw Text Candidates

None

## Rejected Candidates

- [Mixed epistemic status must be preserved below the document level](../../../../notes/mixed-epistemic-status-must-be-preserved-below-the-document-level.md) -- region-level warrant preservation is relevant background, but it does not answer the source's stronger question of what displaced content must still survive as history.
- [Reflection makes retained lessons second-order: a lesson can reject or rescope a prior commitment](../../../../notes/reflection-makes-retained-lessons-second-order.md) -- explains how a later lesson can operate on a prior commitment, but not which rejected or superseded content keeps historical standing after that operation.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- shows runtime retention, stale-marking, and rollback, but the claim is about project-memory lifecycle rather than the truth-role asymmetry between superseded choices and refuted beliefs.

## Index Membership

- [KB maintenance](../../../../tags/kb-maintenance-README.md) -- the source is the clearest note in that head on why maintenance splits into append-only history for choices and holistic rewrite for beliefs.

## Synthesis Opportunities

- [Superseded choices need a historical witness; refuted beliefs lose subject-matter standing](../../../../notes/superseded-choices-are-retained-superseded-beliefs-are-not.md), [Retaining the episode keeps a distilled rule re-derivable](../../../../notes/retaining-episode-evidence-keeps-a-distilled-rule-open-to.md), and [Parametric reproduction alone cannot replace an authoritative record](../../../../notes/parametric-reproduction-cannot-replace-an-authoritative-record.md) together suggest a broader note: retention obligations follow whether later governance needs an addressable, contestable witness, not whether the displaced content can be approximately reproduced or summarized.

## Maintenance Observations

None

## Flags

- None
