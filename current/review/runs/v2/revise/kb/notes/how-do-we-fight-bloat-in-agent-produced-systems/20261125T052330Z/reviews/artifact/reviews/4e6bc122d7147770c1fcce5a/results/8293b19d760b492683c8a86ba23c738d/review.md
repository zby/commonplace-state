---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Commonplace currently counters bloat with five partial mechanisms across prose,
    structure, and the code–prose boundary
  reason: The Current answer describes five linked theory notes as mechanisms Commonplace
    currently runs. Most of them diagnose or state principles and name no operative
    step, owner or trigger. The note's own Stakes section says control 'relies on
    periodic manual sweeps and ad-hoc restraint'. The section should say which items
    are operative practices, such as the documentation sweep and the retire-artifact
    procedure, and which are authoring doctrine applied through restraint. Without
    that split, a reader may overestimate the current defenses.
- scope: passage
  quotes:
  - Gate inflow by value as well as validity.
  reason: This bullet presents a value gate as a current countermeasure. Its own sentence
    says that 'without a value gate, valid redundant artifacts still accumulate'.
    The linked choosing-what-to-learn note calls the value oracle part of an open
    problem. The text does not say whether Commonplace has an operative value gate.
    If it does, the note should name it, for example the AGENTS.md quality bar ('A
    design insight earns a note when…') or review gates. If it does not, the item
    belongs under Unsettled or should be labelled as a target.
- scope: passage
  quotes:
  - Retire fixed-difficulty scaffolding as models improve.
  reason: The linked scaling note mainly argues that external structure recurs at
    the deployment frontier. It concedes fixed-difficulty absorption but does not
    supply a retirement practice. It hands that job to the relaxing-signals note,
    which is not linked here. As cited, the bullet presents a distinction as a mechanism.
    It should link the relaxing-signals note as the actual candidate-detection step
    or call this a criterion for judging what to retire.
- scope: passage
  quotes:
  - Empirically, agents default to additive changes
  reason: '''Empirically'' asserts an observed regularity, but the note cites no observation,
    log entry or source. The rest of the bullet depends on this bias existing. The
    note should cite the evidence or present the bias as an observed but unrecorded
    pattern.'
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/critique-note.md
contract: report
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/critique-note.md
note-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8293b19d760b492683c8a86ba23c738d/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/4e6bc122d7147770c1fcce5a/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 8293b19d760b492683c8a86ba23c738d
completed-at: '2026-11-25T05:27:16Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/8293b19d760b492683c8a86ba23c738d/outputs/review.md
raw-output-sha256: 877efcbdd96436f94c5c560ffd3a3d89150c36303cb24f14c2af5f3616cad46e
format: 2
---

# Critique: How do we fight bloat in agent-produced systems?

**Note:** kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
**Central commitment:** Bloat in mixed natural-language and code systems produced by agents is an unsolved problem beyond software anti-bloat practice. Commonplace currently counters it with five partial mechanisms, while six named gaps remain open.
**Critique mode:** description
**Attack outcome:** partially lands

## Strongest case against it

The objector is a maintenance-minded software engineer in the tradition of Lehman's laws of software evolution. That tradition says complexity grows unless work is spent to reduce it. The objector would grant the Stakes and Unsettled sections but reject the Current answer as a description. The objection reads: "You have no current mechanisms. You have five essays." A mechanism in the sense software anti-bloat practice uses has a trigger, an actor and an effect, like dead-code elimination, a linter or a dependency budget. Check each item:

- *Do not write what the executor supplies* is an authoring principle. The one operative datum is the seven-case documentation sweep, which was a one-off manual sweep.
- *Target zero-structure expansion* is a diagnostic concept. The two cited rewrite studies show that naive shortening fails. They do not show a process that removes expansion.
- *Balance cheap adoption with retirement*: the linked note says retirement is weak. It also says the retire-artifact procedure "does not supply the earlier signal, decision owner, or rule". That is the diagnosis of a missing mechanism.
- *Retire fixed-difficulty scaffolding*: the linked note argues mostly for keeping structure at the frontier. It hands candidate detection to a relaxing-signals note that this note does not link.
- *Gate inflow by value*: the bullet itself says that without a value gate, redundant artifacts accumulate. The linked note calls the value oracle open.

The objector concludes that the honest current answer is the one in the Stakes section: manual sweeps and restraint, guided by these principles. Calling them "mechanisms that counter bloat" is a small instance of the problem the note studies. It adds a confident-looking layer without the operational substance behind it.

## How the note engages it

Partially engaged. The note hedges with "partial mechanisms". Its Stakes section says control "relies on periodic manual sweeps and ad-hoc restraint". The retirement-trigger item under Unsettled admits that the adoption/retirement item lacks a trigger. A careful reader can therefore reconstruct the real state. The attack still lands on two points. First, the "Gate inflow by value" bullet appears under Current answer while its text and its linked note describe the gate as missing. The note never names an operative value gate, such as the quality bar in AGENTS.md or a review gate, that would justify listing it. Second, the scaling bullet cites a note whose main claim is about recurrence, not retirement. The note does not cite the relaxing-signals note that supplies the actual retirement candidates. The attack does not land against the Stakes or Unsettled sections, which are candid and well bounded.

## Constructive findings

- Split the Current answer into **operative practices** and **guiding doctrine**. Operative practices name a trigger, an actor or a procedure: the documentation sweep, the retire-artifact procedure once a target is named, and any review gate that rejects redundant notes. Guiding doctrine covers determinability, reverse compression and entrenchment warrant. The split makes the opening sentence true and makes the Stakes condition testable.
- Either name the value gate Commonplace actually applies, for example the AGENTS.md quality bar plus the log-before-note rule, or move "Gate inflow by value" under Unsettled as a missing oracle.
- Link the relaxing-signals note as the actual mechanism behind the scaffolding-retirement bullet, or reword the bullet as a criterion for what retirement should target.
- Support "Empirically, agents default to additive changes" with a log entry, an episode or a source. Otherwise label it as an unrecorded observation.

## Secondary objections (optional)

- **Reachability is not the right absence.** Under "No reachability oracle for natural language", a KB does have reachability proxies: link graphs, inbound-link counts, and agent read or retrieval traces. The note's real point is that being reachable does not mean being used in a decision, and code has the same gap, as the note concedes. The item may be better framed as having no *use* oracle, with weaker usage proxies, rather than having no reachability check.
- **The distinction between mixed and pure systems is asserted rather than shown.** The Stakes section implies that mixed natural-language and code systems need different treatment. But most listed remedies, including retirement paths, value gates and scaffolding relaxation, apply equally to pure code. Only the cross-boundary item in Unsettled is specific to mixed systems. The note could say more sharply what does not carry over from software anti-bloat practice.
