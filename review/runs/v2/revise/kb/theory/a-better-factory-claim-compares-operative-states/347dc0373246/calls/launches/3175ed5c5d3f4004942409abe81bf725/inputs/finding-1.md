---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 2fa1537f71da4c8bab7c27fd40ab5b5f
completed-at: '2026-11-16T21:57:32Z'
findings:
- scope: passage
  quotes:
  - A [software factory](./definitions/software-factory.md) undergoes experience-responsive
    retention
  reason: The note's central object, 'software factory', is linked on first mention
    but never glossed. The reader must follow the link to learn what a software factory
    is; 'reusable machinery' in the same sentence hints at it only indirectly. Add
    a short inline gloss beside the link.
  level: warn
- scope: passage
  quotes:
  - its evaluator sits at a declared location that is not settled by the learner boundary
  reason: '''Learner boundary'' first appears in the opening paragraph as if known;
    its definition (''declares whose causal contributions count as the factory''s
    own learning'') arrives only in the later ''Evaluator location'' section. Move
    or repeat that gloss at first mention.'
  level: warn
- scope: passage
  quotes:
  - not a verdict on the factory's quality over its open production family
  reason: '''Open production family'' (later ''declared family'') is used without
    explanation. A reader cannot infer that it means the open-ended range of production
    tasks the factory may face; gloss it at first use.'
  level: warn
- scope: passage
  quotes:
  - includes an operative path for [factory development](./definitions/factory-development.md)
  reason: '''Factory development'' is linked but not glossed. The section''s argument
    depends on understanding it as the work of revising the factory itself rather
    than producing software with it; a brief inline paraphrase would let the reader
    follow without the link.'
  level: warn
- scope: passage
  quotes:
  - for the factory-development redesign class, not merely that the successor is editable
  reason: '''Redesign class'' is a technical term from the linked note and is not
    explained here; the sentence only makes sense if the reader already knows what
    a redesign class is and why the path''s applicability is indexed to one.'
  level: warn
- scope: passage
  quotes:
  - the human-inclusive boundary re-enters at the headline result
  reason: '''Human-inclusive boundary'' is not defined; context lets a careful reader
    infer a learner boundary that counts people as part of the learner, but stating
    that briefly would remove the inference step.'
  level: info
- scope: passage
  quotes:
  - the occurrence condition is silent about quality
  reason: '''Occurrence condition'' is a label not introduced elsewhere in the note;
    the reader can recover it from the opening''s account of retention, but naming
    it as the condition for retention to occur would make the reference explicit.'
  level: info
contract: verdict
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/dfd39859f225e71a941a467a/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/dfd39859f225e71a941a467a/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/2fa1537f71da4c8bab7c27fd40ab5b5f/outputs/review-undefined-terms.md
raw-output-sha256: dee3d9af2d28e076e6fa9eb4d917ec9332932f6c1e40dcc8fee8926e8252f938
---

# Review

## Summary

The note defines its own comparison vocabulary well: predecessor, candidate and operative successor get a dedicated glossed list; experience-responsive retention is defined in the sentence that introduces it; non-regression, the target dimension and prior scope ("what that state could already do") are explained where they appear; and compounding is paraphrased in the following sentence.

The gaps are terms imported from linked notes. The note's subject, "software factory", and the concepts "factory development", "redesign class" and "open production family" are relied on without an inline gloss, and "learner boundary" is used in the opening well before its definition. Each forces the reader to follow a link or carry an unresolved term through the argument. Short inline glosses at first mention would resolve all of them without restructuring the note.
