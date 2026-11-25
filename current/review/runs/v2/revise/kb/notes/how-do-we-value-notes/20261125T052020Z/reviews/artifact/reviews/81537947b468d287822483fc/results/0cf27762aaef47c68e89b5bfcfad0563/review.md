---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Without a clearer way to distinguish high-value notes from merely valid ones,
    autonomous authoring can accumulate well-formed clutter faster than review and
    curation can keep up.
  reason: UNSUPPORTED — The urgency rests on the linked maintenance-capacity note,
    but that note is about harmful retained artifacts and treats gross generation
    volume as only a proxy for risk-weighted inflow. The stakes paragraph moves from
    rising note volume to harm without showing that merely valid, low-value notes
    count as harmful inflow. It needs the mechanism by which well-formed clutter imposes
    risk, such as crowding retrieval, diluting navigation or adding maintenance load.
    Without that mechanism, the cited capacity condition does not bear on clutter.
- scope: passage
  quotes:
  - Commonplace currently spreads note valuation across five partial lenses rather
    than one rule
  reason: THIN — "Currently" implies that these lenses operate in Commonplace's selection
    practice. The note does not separate operative lenses from proposed ones. Answerability
    is stated as an admission invariant. The structural and curation proxies come
    from theory notes that say signals "could" be combined or "can" rank candidates,
    with no shipped scoring mechanism cited. Reader update and counterfactual use
    are framed as tests a note can be put to, not as checks that run. The sentence
    therefore supports a map of available valuation ideas better than a description
    of present practice. That distinction also matters for the Unsettled claim that
    nothing checks learning value.
- scope: passage
  quotes:
  - Structural validation, source grounding, and critique gates check validity more
    strongly than anything checks learning value or reader update.
  reason: 'THIN — This comparative premise drives the asymmetric-pressure argument,
    but the note asserts it without evidence such as gate inventories or rejection
    rates. It also sits uneasily with the Current answer, which lists learning-value
    gates and the reader-update test as lenses. The inference from the premise is
    otherwise careful: it is hedged as a conjecture and supplies the directional mechanism
    ("if production favors fluent local additions") that the linked conjecture says
    absolute degradation requires. The premise itself is the weak link.'
- scope: passage
  quotes:
  - Inbound links and counterfactual system use only become observable after a note
    has been retained and used. Autonomous production needs a way to filter, quarantine,
    or trial new candidates before those downstream signals exist.
  reason: 'THIN — The first sentence holds. The step to an unsolved cold-start gap
    does not address the admission-time lenses the note already lists: answerability,
    the learning-value gate, and reader update with comparative work gain against
    a cheaper alternative. Each could apply before downstream signals exist. The gap
    may be real if those lenses are unoperationalized or weakly discriminating, but
    the note does not say so. As written, it does not explain why lenses 1–3 fail
    to supply cold-start selection.'
- scope: passage
  quotes:
  - Those goals decide what a collection admits in principle, but they do not exhaust
    how to rank, keep, or reject candidate notes.
  reason: HOLDS — The examples support the contrast. Explanatory-reach, fidelity and
    economy are admission criteria stated per collection, and none supplies a comparative
    ranking among admissible candidates or a retention rule. The sentence gives no
    argument, but its scope is modest and the gap it names is the one the rest of
    the query develops.
outcome: report
description: Retained report review of kb/notes/how-do-we-value-notes.md against kb/instructions/composition-friction-gate.md
contract: report
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
criterion-sha256: 6e789a3c72156944d9b8f1322f23bbba3dec8f966da5a398c36cbea0c37230fc
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/0cf27762aaef47c68e89b5bfcfad0563/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/81537947b468d287822483fc/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 0cf27762aaef47c68e89b5bfcfad0563
completed-at: '2026-11-25T05:24:26Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/0cf27762aaef47c68e89b5bfcfad0563/outputs/review.md
raw-output-sha256: 218558729a861e50012cd25bc81865df3af5f6b65687ee91436cb777b3daef9a
format: 2
---

# Friction check: How do we value notes?

**Central claim (one sentence):** Commonplace values candidate notes through several partial lenses rather than a tested selection mechanism, and that gap becomes urgent as autonomous production raises volume faster than curation can separate high-value notes from merely valid ones.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent position: valuation is plural and partial now, and an explicit, validated mechanism is the open target. The properties it wants together are coverage of several value dimensions, scalability under autonomous volume and resistance to Goodharting. The note does not claim to have them all; it lists their combination as unsettled. A standing query that names the tension instead of resolving it does not dissolve.

## Thinnest joints

The stakes joint ranks first because the query's urgency depends on it. The note cites a capacity condition about harmful artifacts but applies it to low-value valid notes. The linked note also warns that volume is only a proxy. The "currently spreads" joint ranks next because it blurs operative practice and proposed practice. That blur affects two Unsettled items. The asymmetric-pressure premise and the cold-start gap each depend on whether the admission-time lenses are actually run. If they are run, those items weaken. If they are not, the Current answer overstates. The opening contrast between collection goals and ranking holds. It is included as the strongest of the surfaced joints, not as a defect.

## For the human

Start with the "currently spreads" sentence. Mark which of the five lenses actually operate in Commonplace's selection today. That answer decides whether the asymmetric-pressure and cold-start items are well-founded, and it supplies the missing link from volume to harmful clutter.
