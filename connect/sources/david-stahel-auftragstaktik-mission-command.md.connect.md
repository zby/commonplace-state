---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: kb/sources/.snapshots/david-stahel-auftragstaktik-mission-command.md
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Auftragstaktik: The Prussian-German Origins and Application of Mission Command

**Source:** [Auftragstaktik: The Prussian-German Origins and Application of Mission Command](../../../../sources/.snapshots/david-stahel-auftragstaktik-mission-command.md)

The source is an immutable snapshot. Every outbound candidate below is therefore a recommendation for the matching `david-stahel-auftragstaktik-mission-command.ingest.md`, not an edit to the snapshot.

## Discovery Trace

**Source analysis:**

- Read the snapshot in full. Its central contribution is a historical reassessment: *Auftragstaktik* was contested in meaning, uneven across command levels and periods, dependent on communications, training, doctrine, culture, and personalities, and not identical to modern mission command. Its strongest transfer implication is that an imported methodology cannot be reduced to a short label or a general rule favoring decentralization.
- The source has no `tags:` field, so no matching tag-README pass or by-tag `rg` pass applied.

**Curated heads and title surfaces:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`.
- Generated the complete title surface for each authorized local destination with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`, substituting `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources` for `<destination>`.
- Notes: the title scan foregrounded the transfer, executor-discretion, methodology-selection, underspecification, and orchestration-guarantee clusters.
- Reference: no shipped-system document gained a concrete reader benefit from a direct connection.
- Agent-memory systems and agentic systems: no reviewed system matched the source's historical claim closely enough to pass the articulation test.
- Sources: the scan identified the U.S. Army mission-command and Marine Corps warfighting ingests as direct doctrinal comparators.

**Description listing scan:**

- Ran `rg '^description:' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'` over all authorized local destinations.
- Kept the mechanism-preserving transfer, retained-versus-weight-activated borrowing, executor-discretion, and methodology-selection notes because their descriptions named a precise transfer or execution question raised by the source.
- Rejected broad autonomy, context, and orchestration matches whose descriptions did not identify the same mechanism.

**Body search:**

- `rg -n -i 'borrow(ed|ing)|transfer|imported (idea|concept|method)|shared mechanism|source and target' kb/notes/ --glob '*.md'` -- kept the two borrowing/transfer notes; the source supplies a historical case in which cultural translation, shifting institutional setting, and conceptual ambiguity prevent a label from carrying a methodology intact.
- `rg -n -i 'decentral|delegat|autonom|freedom of action|commander.s intent|shared (doctrine|culture)|training and education|scope for action' kb/notes/ --glob '*.md'` -- kept the executor-discretion note; rejected generic autonomy hits that concern evaluation authority or unrelated orchestration dimensions.
- `rg -n -i 'doctrine|declared.*(practice|behavior)|practice.*declared|implementation|context[- ]sensitive|situat|contingent' kb/notes/ --glob '*.md'` -- retained the contextual limit on fixing execution means; other matches were topical rather than evidential.
- `rg -n -i 'mission command|Auftragstaktik|decentral|delegat|autonom|borrow|transfer|doctrine.*practice' kb/reference/ --glob '*.md'` -- no reference candidate passed the articulation test.
- `rg -n -i 'mission command|Auftragstaktik|decentral|delegat|autonom|shared doctrine|command intent' kb/agent-memory-systems/ --glob '*.md'` -- no agent-memory-system candidate passed.
- `rg -n -i 'mission command|Auftragstaktik|decentral|delegat|autonom|command intent|shared doctrine' kb/agentic-systems/ --glob '*.md'` -- no agentic-system candidate passed.
- `rg -n -i 'mission command|Auftragstaktik|commander.s intent|freedom of action|MCDP 1|Warfighting' kb/sources/ --glob '*.md'` -- kept the ADRP 6-0 and MCDP 1 ingests as direct comparisons on doctrine, historical lineage, and transfer conditions.
- External prospecting was skipped: `external` is authorized only for already-known targets, and no external target was supplied in the task or loaded context.

**Link following:**

- Followed the ADRP 6-0 and MCDP 1 ingest neighborhoods into the executor-discretion, mechanism-preserving transfer, methodology-selection, specification-timing, predictable-choice, specific-intent, and coordination-guarantee notes.
- Kept links where Stahel adds a distinct historical test or qualification. Rejected links where the military case was only an analogy to a technical agent-system mechanism.

## Connections Found

- [ADRP 6-0: Mission Command](../../../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md) -- **compares-with**: ADRP 6-0 states a coherent modern doctrine of bounded decentralized execution, while Stahel shows that historical *Auftragstaktik* was contested, unevenly practiced, and not interchangeable with modern mission command; reading both separates prescribed modern doctrine from claimed historical lineage.
- [MCDP 1, Warfighting (1997)](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) -- **compares-with**: MCDP 1 presents shared doctrine, training, trust, intent, and local initiative as a coherent normative system; Stahel supplies the historical counterweight that these elements varied by period, command level, technology, and command culture rather than forming a stable German golden-age model.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- **is-evidence-for**: the Anglo-American import of *Auftragstaktik*, its cultural filtering, and the mismatch between historical and modern command systems provide a concrete case in which a shared label and surface resemblance do not carry warrant beyond the mechanisms and institutional preconditions actually shared.
- [Borrowing can operate through retained artifacts or weight activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) -- **is-evidence-for**: Stahel documents interpretation anarchy around a familiar methodology name and therefore supplies a source-domain example of the note's warning that a compact pretrained cue may reconstruct a distorted, underspecified, or internally mixed methodology.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **is-evidence-for**: the historical command problem supplies a bounded external case for fixing purpose while leaving situation-dependent execution to a competent local actor, and it sharpens the note's limits by showing that improved communications, command level, training, and culture can change how much discretion is useful.
- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) -- **compares-with**: the note uses “Use Auftragstaktik” as a compact methodology cue, while Stahel shows that the term has no stable, universally valid operational content and should not be collapsed into modern mission command; the comparison exposes the fidelity test a methodology-selection cue must pass.

## Bidirectional Candidates

None. Durable artifacts must not link to an immutable local snapshot; any return link should target the matching ingest after its author evaluates these candidates.

## Reverse-edge Candidates

None. The source collection forbids durable links to `.snapshots/`; candidate inbound uses belong on the matching ingest rather than on this local materialization.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- Stahel identifies human institutional conditions such as doctrine, training, culture, and accountability, but does not establish the technical scoping, consistency, verification, or liability guarantees claimed for agent orchestration.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- local battlefield knowledge is an intuitive analogue for execution-time understanding, but the source does not study durable specifications or their revision lifecycle.
- [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) -- the source's standardization-versus-initiative debate is suggestive, but military drills and regulations do not by themselves evidence the note's symbolic-codification mechanism.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- commander's intent is a useful analogy, but Stahel does not compare reconstruction yield per token or the note's intent-versus-rationale conditions.
- [Actionable methodology](../../../../notes/definitions/actionable-methodology.md) -- the source illustrates setting-dependent applicability, but this stipulated operator-relative definition neither depends on nor gains enough traversal value from the historical case.

## Index Membership

None. The snapshot is a local source materialization, not an authored member of a notes or system-review index.

## Synthesis Opportunities

- **Intent-framed delegation is a control regime, not a short prompt.** Stahel's historical reassessment, the two modern doctrinal ingests, the executor-discretion note, and the mechanism-preserving transfer note jointly imply that useful discretion depends on competence, intent, authority bounds, information position, communication, feedback, training, and shared norms. The higher-order claim would reject both procedural micromanagement and unconstrained “delegate more” advice while requiring target-side evidence for agent-system transfer.

## Maintenance Observations

None.

## Flags

- The source creates a direct tension with the *Auftragstaktik* example in the methodology-selection note: a short cue can select a methodology only if the consuming model reconstructs a coherent cluster, while this source argues that the historical term itself is contested, context-dependent, and distinct from modern mission command.
- Apply accepted candidates to the matching ingest only. The snapshot is checksum-sensitive and must remain unchanged.
