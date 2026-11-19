---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
note-sha256: 0366cb851ef44475ed808292e3919e8d5559c86b5d72261a6cdd8d5c82ee0aab
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews
launch: 7be1f3184c6a44c59369e23bf8f526df
completed-at: '2026-11-17T07:24:07Z'
findings:
- scope: passage
  quotes:
  - 'The speed gain can be real. The lost revision capability can also be real. There
    is no contradiction: the comparison checked task performance, while the change
    removed a different capability.'
  reason: This paragraph repeats the opening paragraph's point that the two outcomes
    are compatible because checking the current gain does not check the revision mechanism.
    The example has already made the case concrete, so the recap adds no new contrast.
    Cut it, or reduce it to one clause attached to the example's last sentence.
  level: warn
- scope: passage
  quotes:
  - 'Preserving the path is therefore a consequence of non-regression only under an
    additional condition: the revision capability must be included in what is checked.'
  reason: 'This sentence restates the preceding paragraph: non-regression protects
    only what is in its checked scope, and it protects the revision path when that
    scope includes it. The following sentence is the useful part, because it says
    that production-only non-regression leaves the path out. Fold that sentence into
    the previous paragraph and drop the restatement.'
  level: warn
- scope: passage
  quotes:
  - Closing one path does not establish loss of the capability if another applicable
    path remains.
  reason: 'The body already makes this point twice: a successor fails only if it ''destroys
    the only applicable revision path'', and ''The required function need not stay
    in its original component.'' The scope bullet adds no new boundary case and can
    be cut.'
  level: warn
- scope: passage
  quotes:
  - A maintainer may restore a path that the agent itself no longer has.
  reason: This partly repeats the earlier maintainer-editable-files paragraph. Its
    framing in terms of the declared system boundary may still help prevent misapplication.
    I am unsure whether that is enough to justify keeping it as a separate bullet.
  level: info
contract: verdict
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/4dcd5a14a0e353b1bb79f192/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/4dcd5a14a0e353b1bb79f192/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/calls/launches/7be1f3184c6a44c59369e23bf8f526df/outputs/review.md
raw-output-sha256: 3cae06e96d83c709904f07f38ef00a7842a28c69d2aa1e20232873ff6a55bc1e
---

# Review

## Summary

The note is short and its main parts do real work. The hypothetical agent makes the failure concrete. The non-regression section states the condition under which the failure is prevented. The section on remaining able to improve separates preservation from actual later improvement. The first Scope bullet, about fixed deployments that deliberately give up self-revision, adds a boundary the body does not otherwise state.

The redundancy is local. Three chunks restate a point that an adjacent or earlier passage has already made. The first is the "no contradiction" paragraph after the example. The second is the "therefore ... only under an additional condition" sentence, which repeats the scope rule it follows. The third is the Scope bullet about another applicable path, which the body already covers. Cutting or folding these would shorten the note without removing anything the reader needs.

The sentence "That note supplies the detailed test; this note explains why a successful improvement comparison can miss its failure" was considered and is not flagged. It tells the reader where the detailed test lives, which the earlier link alone does not.
