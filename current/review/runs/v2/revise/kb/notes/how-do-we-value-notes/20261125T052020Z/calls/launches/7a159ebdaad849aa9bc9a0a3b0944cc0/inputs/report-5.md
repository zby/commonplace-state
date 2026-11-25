---
type: types/review-result.md
format: 2
description: Retained report review of kb/notes/how-do-we-value-notes.md against kb/instructions/role-in-the-kb-gate.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
criterion: kb/instructions/role-in-the-kb-gate.md
criterion-sha256: 1181f261a8ee86614d6e432a316715fe90534ea271ad19b4783ed89c9cea04b3
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/role
launch: 1111119618e649a8b02162c9061dc8a7
completed-at: '2026-11-25T05:26:07Z'
findings:
- scope: passage
  quotes:
  - a note can be grounded and coherent yet redundant or too narrow to justify its
    maintenance cost
  reason: 'PARTLY SUPPLIED — kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
    — its lever ''Gate inflow by value as well as validity'' cites the note for the
    distinction that validity checks pass valid but redundant artifacts, so a value
    gate is also needed. The note supplies that distinction in its ''Validity separate
    from value'' lens. It does not supply a value gate at inflow: its ''Cold-start
    selection at admission'' bullet says value signals appear only after retention
    and use, and admission-time filtering remains unsettled. The dependent''s lever
    therefore rests on a gate the note marks as open.'
- scope: document
  quotes: []
  reason: 'SUPPLIED — kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
    — its footer cites the note only as a ''companion standing query on selecting
    which notes earn retention and maintenance cost''. The whole note is that standing
    query: its title, description and Stakes frame selection of notes against retention
    and maintenance cost.'
- scope: passage
  quotes:
  - Without a clearer way to distinguish high-value notes from merely valid ones,
    autonomous authoring can accumulate well-formed clutter faster than review and
    curation can keep up.
  reason: DUPLICATED — kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
    — the dependent's passage states 'structural and grounding checks block invalid
    artifacts, but without a value gate, valid redundant artifacts still accumulate',
    which restates this Stakes sentence and the note's 'Asymmetric selection pressure'
    bullet. Both also link the same theory note on validity and learning-value gates.
    The dependent's one-line form suits its use as a bloat-control lever; the note's
    version adds the mechanism (weakly discriminated qualities are underselected),
    which the dependent does not need at that point.
contract: report
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/role/calls/launches/1111119618e649a8b02162c9061dc8a7/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/role/artifact/reviews/a2482a6cc0aaf5587af7d749/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/role/calls/launches/1111119618e649a8b02162c9061dc8a7/outputs/review.md
raw-output-sha256: e3770c740210540f9492b44f55eb99eec7f7dccd809cc151b58957fa5b4e3731
---

# Role in the KB: How do we value notes?

## Role
One file links to the note: the companion standing query on bloat in agent-produced systems. That query uses it as the home of the validity-versus-value distinction behind its "gate inflow by value" lever, and as a see-also for selecting notes against retention and maintenance cost. No dependent argues from the five valuation lenses or the unsettled items individually.
Relied on: the distinction between validity and value; the claim that valid but low-value artifacts accumulate as clutter without a value check; the note's scope as a standing query on retention-worthy notes. Unused: answerability as admission, reader update and comparative work gain, counterfactual use in live work, structural and curation proxies, root questions versus sub-questions, combining dimensions without Goodharting. Cold-start selection at admission is not cited, but it bears on the dependent's inflow-gate lever.

## Dependents
- `kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md` — needs the validity/value distinction and the case for an inflow value gate (one passage). It also cites the note as a companion standing query in its footer.

## Duplication
The dependent's "Gate inflow by value as well as validity" passage restates the note's Stakes sentence on well-formed clutter and its asymmetric-selection bullet. Both cite the same theory note on validity and learning-value gates. The dependent's compact form fits its role as a lever; the note holds the mechanism.

## Untaken recommendations
None. The only linking file is a note, not a source ingest, and it recommends no change to this note.

## Reach
- The validity-versus-value distinction and the well-formed-clutter claim (Stakes, "Validity separate from value" and "Asymmetric selection pressure under autonomous production") reach `kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md`.
- The note's scope as a standing query on which notes earn retention and maintenance cost reaches the same file's footer citation. A change of title or scope would reach it.
- How the note treats admission-time selection ("Cold-start selection at admission") bears on the same dependent's inflow-gate lever, although the dependent does not cite that bullet.
- No dependent relies on the answerability, reader-update, counterfactual-use, structural-proxy, root-question or Goodharting content. A change to those reaches no one.
