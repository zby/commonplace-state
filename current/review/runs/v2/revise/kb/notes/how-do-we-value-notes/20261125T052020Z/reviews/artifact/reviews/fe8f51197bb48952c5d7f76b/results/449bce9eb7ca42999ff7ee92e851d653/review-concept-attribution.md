---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - combine structural maturity (type), review verdicts, recency, and link-strength-weighted
    inbound links
  reason: 'The sentence equates the ''structural and curation proxies'' lens with
    a combination that it attributes to both linked notes. Notes need quality scores
    to scale curation does propose type, inbound links weighted by link strength,
    review vetting and type-dependent recency. Quality signals for KB evaluation does
    not: it is an explicitly exploratory catalogue of graph-topology signals (orphan
    rate, centrality, reciprocity), content-quality proxies (description uniqueness,
    title-as-claim ratio, frontmatter completeness), metamorphic relations and LLM-hybrid
    ensemble evaluation, and it does not use review verdicts, recency or link-strength
    weighting. Its concept is a basket of weak signals for a learning-loop oracle,
    which is substantively different from the four-signal ranking named here. Attribute
    the four signals to the quality-scores note alone and describe the second note''s
    contribution separately.'
  level: warn
- scope: passage
  quotes:
  - grounds that test in expected downstream work and compares adding a note against
    a cheaper alternative
  reason: Defining improvement for open-ended work derives requirements from the expected
    task stream and its KB case compares adding a note with linking an existing decision
    record, so the substance is supported. It does not mention reader update, so 'grounds
    that test' presents a connection the target does not itself draw; this is the
    note's synthesis rather than a mismatch.
  level: info
outcome: warn
description: Retained verdict review of kb/notes/how-do-we-value-notes.md against
  kb/instructions/review-gates/sentence/concept-attribution.md
contract: verdict
note: kb/notes/how-do-we-value-notes.md
criterion: kb/instructions/review-gates/sentence/concept-attribution.md
note-sha256: d522bd49f4a992cdb1074f439716ff7caa3986d1eb6e783dac1960ddd5ec179e
criterion-sha256: 75949108abe516c6d5d80ba7a1c9546fbb81cc202dd215042cf5a323075358e6
target-sha256: b5cf96fb9ebd96b737254b02a2d6dd3751ffbc2288c0baca8446b70c0a189e92
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/449bce9eb7ca42999ff7ee92e851d653/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/artifact/reviews/fe8f51197bb48952c5d7f76b/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews
launch: 449bce9eb7ca42999ff7ee92e851d653
completed-at: '2026-11-25T05:23:44Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-value-notes/20261125T052020Z/reviews/calls/launches/449bce9eb7ca42999ff7ee92e851d653/outputs/review-concept-attribution.md
raw-output-sha256: 93e08e246fa436fc43d98bfe49b743307af4fc77805054e77834b78c0a1a1473
format: 2
---

# Review

## Summary

I checked each passage that identifies one of the note's valuation lenses with a linked note's concept: explanatory-reach, answerability, validity versus learning value, test record versus fit, warranted reader update, defining improvement, counterfactual system use, the quality-score notes, the reader-need labels in link vocabulary, and the underselection conjecture. All targets resolved.

Most identities hold. The explanatory-reach gloss matches its target's "claims that keep working outside the case that produced them". The answerability gloss matches the three-part definition. The validity/learning-value, test-record/fit, system-use and underselection characterisations match their targets' opening claims, including the underselection note's "production biased toward locally expedient changes" as the directional mechanism behind accumulating clutter. Mapping sub-question answering to reader-need labels matches link vocabulary's statement that labels name reader needs.

The one substantive mismatch is the curation-proxy lens. It attributes a specific four-signal composite to Quality signals for KB evaluation, but that note offers a different, exploratory catalogue of signals.
