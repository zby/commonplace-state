---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/semantic/grounding-alignment.md
note: kb/notes/how-do-we-value-notes.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: a38acad87c914bb7ae48d968378006fb
completed-at: '2026-11-25T05:23:10Z'
findings:
- scope: passage
  quotes:
  - Every retained artifact adds maintenance, navigation, and exposure cost
  - autonomous authoring can accumulate well-formed clutter faster than review and
    curation can keep up
  reason: The linked note 'Maintenance capacity must match harmful-artifact inflow'
    concerns the risk-weighted inflow of harmful, repair-requiring artifacts. It says
    gross generation volume is only a proxy, and that artifact volume matters 'through
    defect incidence, expected harm, exposure time, detection latency, and remediation
    effort, not by itself'. Here it is cited next to a per-artifact cost claim and
    a volume-driven urgency argument, and then applied to 'well-formed clutter'. The
    note does not say why valid but low-value notes count as harmful inflow in the
    target's sense. Without that, the citation supports a broader, volume-based reading
    than the target makes. The transfer is plausible, since clutter may raise navigation
    and exposure cost, but it is not stated clearly enough to verify.
  level: warn
- scope: passage
  quotes:
  - combine structural maturity (type), review verdicts, recency, and link-strength-weighted
    inbound links
  reason: 'Two notes are cited together as grounding a current lens that ''combine[s]''
    four named signals. ''Notes need quality scores to scale curation'' does name
    type, review vetting, recency and link-strength-weighted inbound links. However,
    it presents them as a proposed score that is needed, not one Commonplace uses.
    ''Quality signals for KB evaluation'' calls itself an ''Exploratory question set,
    not an established scoring model'' and catalogues different signals: graph topology,
    content proxies and LLM hybrids. The citations therefore support ''proposed signals'',
    not a current combining practice, and the second note does not support this particular
    set of four.'
  level: warn
- scope: passage
  quotes:
  - whether withholding or replacing a note actually changes search, diagnosis, decisions,
    or recovery
  reason: 'The target claims this about claims in a working theory: ''A claim whose
    withholding, replacement, or perturbation changes search or recovery''. The note
    applies it to whole notes without stating that transfer. This is a modest, plausible
    extension that does not bear weight here.'
  level: info
- scope: passage
  quotes:
  - grounds that test in expected downstream work
  reason: '''Defining improvement for open-ended work'' derives tests from the expected
    task stream and compares adding a KB note with linking an existing record. It
    does not refer to the reader-update test. Saying that it ''grounds that test''
    is a light synthesis by this note, not the target''s own claim. The synthesis
    is plausible and does not bear weight.'
  level: info
contract: verdict
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/569b9861b726753085ac90a3/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/a38acad87c914bb7ae48d968378006fb/outputs/review-grounding-alignment.md
raw-output-sha256: 76ffbb068c61f458caac3e768791de5fc53ffe69387eaebea1ebc040a6510920
---

# Review

## Summary

All linked targets are library artifacts, so I checked representation against each target's title and opening.

These links are represented accurately: answerability (all three named elements, and its role as the admission invariant for knowledge collections); the validity versus learning-value gates (faithful but redundant or too narrow notes); test record versus fit; warranted reader update (nontrivial update relative to the reader's prior and existing KB, beyond a generic treatment); the explanatory-reach gloss; and the underselection conjecture. The note marks the last as a conjecture and conditions accumulation on production favouring fluent local additions. That matches the target's requirement for an additional directional mechanism.

Two uses extend beyond their targets:

1. The maintenance-capacity note is about harmful inflow, not gross volume. The note uses it to support a per-artifact cost claim and applies it to well-formed clutter without explaining the transfer.
2. The structural-proxy lens presents a proposed composite score as a current lens. It also attributes the four named signals to a note that catalogues different signals and says it is exploratory.

Both are WARN, not FAIL. Support is plausible, but the scope and transfer are not stated clearly enough to verify.
