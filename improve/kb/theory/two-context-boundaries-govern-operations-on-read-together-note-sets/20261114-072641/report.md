---
type: reports/types/improvement-run-report.md
description: 'Fix-findings run on the two-context-boundaries note: four fixes applied from eight fresh warnings, five findings left open, re-review cited'
note: kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md
variant: kb/work/decision-lifecycle-evidence/first-variant-fix-findings.md
start-commit: 8786a9aebefe03406fd6e9e35a0f852c1613705e
start-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
started-at: '2026-11-14T07:26:41Z'
ending: partly-applied
final-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
ended-at: '2026-11-14T07:29:46Z'
---

# Fix-findings run on the two-context-boundaries note

The run started from eight fresh review warnings holding ten warning-level findings. Five findings were fixed by four edits and five were left open.

## Skipped

The higher-order check was not run. It does not exist as an atom yet; its wordings are still in calibration.

## Fixed

- An inline gloss for "per-window degradation" (undefined terms).
- An inline gloss for "index-scan candidate discovery" (undefined terms).
- The overloaded sentence on poorly described notes was split in two (parsing ambiguity and clause packing, one edit for both findings).
- The quality-scores paragraph now states the general limit first and names `/connect` as the Commonplace instance (source residue).

## Left open

Five items are pending in `answers.md`: the description's use of "connect", the proportion of the library/workshop section, the relation between "collection" and "area", the strength of the library/workshop claim against ADR 025, and a footer label. Each carries the agent's view.

## Not worked

The reviews also held INFO-level findings. They were read and not recorded as entries or worked.

## Re-review

The edited text was re-reviewed with the full gate sweep: 40 results, 33 pass, 7 warn. Pairs that warn on the edited text: accessibility/undefined-terms, kb/theory/COLLECTION, prose/confidence-miscalibration, prose/proportion-mismatch, semantic/grounding-alignment, sentence/clause-packing, sentence/stock-phrases. None was worked in this run.
