---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the right folder and type contract
  reason: '"Type contract" is Commonplace-internal vocabulary: a binding spec for
    a kind of document. It appears unglossed in the opening worked example. An external
    reader cannot tell what a proposal is being directed to. Gloss it (e.g., "the
    spec that says how a design proposal must be written") or drop it from the example.'
  level: warn
- scope: passage
  quotes:
  - belonged in a temporary workshop instead
  reason: '"Workshop" is an active vocabulary term (the KB''s layer for in-flight
    work) and is used here with neither a gloss nor a link. "Temporary" hints at its
    meaning but does not say what a workshop is or how it differs from where design
    proposals go. Add a short gloss such as "a temporary workshop area for unfinished
    work", plus a link to the workshop definition.'
  level: warn
- scope: passage
  quotes:
  - represents the hard-oracle extreme
  reason: '"Hard-oracle" is not defined. The following sentences (every rewrite requires
    a formal proof) let the reader infer it, so this is minor. A brief paraphrase
    ("the extreme where a formal proof must approve every change") would remove the
    guesswork.'
  level: info
- scope: passage
  quotes:
  - review machinery, and judgment probes
  reason: '"Judgment probes" is used without explanation. A reader cannot tell whether
    these are tests of the language-model judge''s reliability or something else.
    A short gloss would help.'
  level: info
outcome: warn
description: Retained verdict review of kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
contract: verdict
note: kb/articles/deliberative-learning-judgment-in-place-of-a-value-function.md
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
note-sha256: 768613364cfc91b94f5eac5c7a2f1d7a4edb3d0409c4913629636496938c5545
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
target-sha256: 404d5a6b16a45f15ccc3e7402fe5b460b6f640af581d796113e1fb783073548e
target-capture: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/bc2026f7d9e144359832d91a80d5c184/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/artifact/reviews/623319a47b9955d1c0bd84bf/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews
launch: bc2026f7d9e144359832d91a80d5c184
completed-at: '2026-11-21T19:26:33Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/articles/deliberative-learning-judgment-in-place-of-a-value-function/20261121T192511Z/reviews/calls/launches/bc2026f7d9e144359832d91a80d5c184/outputs/review-undefined-terms.md
raw-output-sha256: c2b631be32023847b999f4bf1747b040f0e34974acaccbc411e9eac82e62de09
format: 2
---

# Review

The article handles its central terms well. "Deliberative learning" gets an inline gloss in the intro and a linked two-condition definition. "On-balance judgment" is paraphrased on first use and expanded later with a link. "Single-loop" and "double-loop" are glossed in context (single-loop needs Minton outside the system to revise the formula; double-loop revises the working criterion). "Targeted correction", "operative dependence", "accretion" and "pure triggers" each come with an inline explanation. "Theory builder" also gets a parenthetical gloss. Standard ML vocabulary (loss, value function, backpropagation, credit assignment, policy gradients) needs no gloss.

The gaps are in the opening worked example. That example is meant to be readable before the article's own terms are introduced, but it uses two Commonplace-internal terms, "type contract" and "workshop", as if the reader already knew them. "Workshop" is a declared active vocabulary term, so it needs both a gloss and a link. Two later phrases, "hard-oracle" and "judgment probes", are mildly opaque, but surrounding context recovers or bounds them.
