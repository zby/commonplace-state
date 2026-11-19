---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Antecedence here is the pairwise-comparison form of the condition that makes
  reason: 'About 45 words carrying four ideas: antecedence as a pairwise form, the
    condition that makes an objective a declared parameter rather than a post-hoc
    reading, the self-referential objective that fails antecedence, and the concession
    about intact causal history. The colon joins an identity claim to a separate test.
    Split at the colon: state the identity, then give the failing case as its own
    sentence.'
  level: warn
- scope: passage
  quotes:
  - the successor may improve through changes to any operative part of its machinery
  reason: 'About 45 words: a ''because'' clause citing the linked note, the main clause,
    a seven-item dash list, and a second coordinated clause about fixed weights. Three
    concepts stay open at once. Reorder by moving the fixed-weights consequence into
    its own sentence (''Holding model weights fixed therefore does not put the comparison
    out of reach.'').'
  level: warn
- scope: passage
  quotes:
  - Learning by the factory at the declared boundary needs retained experience from
    the predecessor's own production to causally enter the changes the improvement
    depends on
  reason: 'About 60 words in one sentence: the requirement for an experience link,
    a ''because'' clause citing the experiment note, the manipulation claim, a dash-inserted
    operationalization, and a contrast with observing a higher score. Two independent
    claims (what learning requires; how the link is established) are chained with
    '', and because''. Split there; no reordering keeps it readable.'
  level: warn
- scope: passage
  quotes:
  - The structure — operative states as relata, an antecedent scope-indexed relation,
    admission distinguished from measurement, evaluator location declared apart from
    the learner boundary — is stated for factories
  reason: 'A four-item dash list of about 20 words separates the subject ''The structure''
    from its verb ''is stated'', and a ''because'' clause follows the verb. Two long
    dependencies are open in sequence. Reorder: introduce the list after a short verb
    phrase (e.g. ''The structure has four parts: …. It is stated for factories because
    …'').'
  level: warn
- scope: passage
  quotes:
  - Internal controls a factory places on what it retains
  reason: A reduced relative clause and a dash list separate the subject from 'are
    design choices'. This is one long dependency and stays readable; moving the example
    list after the predicate would shorten it.
  level: info
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/sentence/clause-packing.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/sentence/clause-packing.md
note-sha256: 0f9b8fa858ef3eff5ad2c4bb73aaa08f70fba9472292114722a770233b53631d
criterion-sha256: 1546b936d349c05735443368da75ea0829b04f34cd3e6084351c128713f320a1
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/2a984fff4ac7c6911d470047/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/2a984fff4ac7c6911d470047/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: c50667b742724b11b82a141c9cc38486
completed-at: '2026-11-16T22:00:06Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/c50667b742724b11b82a141c9cc38486/outputs/review-clause-packing.md
raw-output-sha256: 5cfce2fa0a76bece1dfe4a2bf526d83732d64c46a71213f8c1a86d982c239c6d
format: 2
---

# Review

Most sentences in the note are short and carry one relation; the definitions of predecessor, candidate and operative successor are cleanly separated, and the route paragraphs keep each claim in its own sentence.

Four sentences overload the reader. Two are long chains joined by a colon or by ', and because', where a split at that joint keeps every relation. The other two hold a subject open across a long inserted list. In the scope bullet, reordering the list after the verb repairs it. In the deployed-system sentence, the trailing fixed-weights clause should stand alone. The internal-controls sentence has only one long dependency and is noted for information only.
