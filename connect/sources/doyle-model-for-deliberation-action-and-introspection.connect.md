---
description: "Pre-ingest candidates for Doyle’s 1980 dissertation: who chooses a belief revision, what an objection defeats, and what the proposed interpreter actually demonstrated."
type: types/connect-report.md
source: kb/sources/.snapshots/doyle-model-for-deliberation-action-and-introspection.md
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: A Model for Deliberation, Action, and Introspection

**Source:** [Doyle’s dissertation](https://hdl.handle.net/1721.1/6883), using the local reading copy identified in `source`. The proposed author of the outbound links is the future ingest, not the snapshot.

## Discovery Trace

Standard local pass with `cp-skill-connect` and `gpt-6.2-astra`. Read the six destination READMEs. For each collection, generated titles with `rg -N --no-filename -m1 '^# (.*)' -r '$1'` over Markdown excluding briefs. Filtered for `reflect|deliberat|doyle|truth maintenance|self-model|justification|self-modification|self-refer|eurisko|gödel machine`. Filtered `rg '^description:'` listings for `reason maintenance|truth maintenance|reflective coverage|defeasible`. Body queries were `Doyle|truth maintenance` and `deliberation record|reflective coverage` (case-insensitive). No retrieval scores. No source tags to match; no by-tag search.

- **Sources:** Doyle’s memo was identifiable before the title scan; its §8 explicitly defers revision plans to the thesis. Compared its summary with dissertation §§3.10 and 6.2.1. The body search also found de Kleer’s alternative to choosing a single revision. The EURISKO title and ingest led to a reported change to a heuristic-selection rule, a useful contrast to Doyle’s skill-change sketch.
- **Theory:** The second-order lessons title led to the distinction between rejecting a commitment and narrowing its scope. Followed the reflection tag head to the precedents note: it distinguishes a representation used in control from evidence of criticism and lasting change. The latter is the better inbound route for readers evaluating historical precedents.
- **Reference:** The head’s design-rationale entry explains where Commonplace keeps reasons. That does not make those reasons executable tests of current support. No shipped contract was needed to interpret Doyle.
- **Agent memory systems:** The truth-maintenance body search found kgai. Its decision history makes a useful contrast: superseding a decision is not defeating one of several independent reasons for it.
- **Agentic systems:** The head exposed Eigenius’s justification certificates and Exo’s rewritable executor. Neither certificate checking nor permission to rewrite answers how the program selects a revision when several would restore consistency. No additional edge.
- **Tags:** Followed the reflection head for its definition and theory links. Its complete listing concerns participating collections, not source membership. No reason to add the snapshot to an index.
- **External:** Used only the dissertation handle supplied in the capture. No web prospecting. Excluded workshop and instruction destinations.

### Candidate origins

- https://hdl.handle.net/1721.1/6883 — known
- kb/sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md — known, titles, body-search
- kb/sources/an-assumption-based-tms.ingest.md — body-search
- kb/sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md — known, titles
- kb/theory/reflection-makes-retained-lessons-second-order.md — titles, link-following
- kb/agent-memory-systems/reviews/kgai.md — body-search
- kb/theory/theory-building-has-distinct-precedents.md — link-following

## Connections Found

- [Doyle’s dissertation at MIT](https://hdl.handle.net/1721.1/6883) — **derived-from**: identifies the work under analysis; the OCR archive is the reading-copy provider.
- [A Truth Maintenance System](../../../../sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md) — **compares-with**: the 1979 memo already makes individual argument steps challengeable. What the dissertation adds is a proposed decision procedure: when several revisions would work, policies give reasons to prefer one in these circumstances. Section 3.10 explicitly says the existing system still selected revisions randomly rather than by decision intentions.
- [An Assumption-based TMS](../../../../sources/an-assumption-based-tms.ingest.md) — **compares-with**: de Kleer labels a conclusion with the minimal consistent assumption sets that support it. Doyle instead asks which assumptions the agent will act on now. Retaining several contexts avoids some backtracking; it does not decide which context to adopt.
- [EURISKO learns new heuristics and domain concepts](../../../../sources/eurisko-learns-new-heuristics-and-domain-concepts.ingest.md) — **compares-with**: Doyle’s §6.2.5 distinguishes patching a failed procedure from retaining a critic to catch that kind of failure later. EURISKO’s H12′ episode reports the latter kind of change: after eliminating a bad heuristic, the system generated restrictions on future heuristic changes. The chapter sketches a design; the episode reports a run, not a general success rate.
- [Reflection makes retained lessons second-order](../../../../theory/reflection-makes-retained-lessons-second-order.md) — **compares-with**: in §5.8 the second policy defeats the *reason* for holding the door, not the action or the standing policy. An independent reason still supports the same action. This distinguishes an exception to one application from a lasting revision of the rule that produced it.
- [kgai](../../../../agent-memory-systems/reviews/kgai.md) — **compares-with**: both separate retained history from what governs now. In kgai a supersession event removes an earlier decision from head-only recall. In Doyle an objection disables one justification; defeat the objection and the old justification can support the conclusion again. A log that preserves old decisions need not implement that reinstatement rule.

## Bidirectional Candidates

- [Doyle’s 1979 memo](../../../../sources/doyle-1979-truth-maintenance-system-aim-521.ingest.md) — **compares-with**: once a tracked thesis ingest exists, readers following the memo’s deferred revision plans could inspect the later proposal and its implementation limit rather than infer that the promised interpreter was finished.

## Reverse-edge Candidates

- [Theory building has distinct epistemic, structural, and implementation precedents](../../../../theory/theory-building-has-distinct-precedents.md) → future ingest — **see-also**: Doyle combines a self-description consulted in action with explicit criticism of a particular inference. Sections 1.5 and 6 separate partially tested components from proposed skill changes. That makes it a useful precedent for the combination, not corroboration that a complete system learned. Target the tracked ingest only after it exists.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Eigenius](../../../../agentic-systems/reviews/eigenius.md) — checking whether a certificate is valid on a load path is a different decision from choosing which otherwise permissible belief revision to make.
- [Design rationale management](../../../../reference/design-rationale-management.md) — preserving why a design was chosen helps later readers, but Doyle’s reason records also determine whether the inference currently holds.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- Keep the implementation boundary beside the mechanism. In particular, the HACKER reconstruction is a plan for skill revision, not a SEAN learning trace. Section 7.3 also explains why current justifications alone do not determine the agent’s past beliefs: they lack temporal order and may admit several interpretations.
