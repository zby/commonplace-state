---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
  against kb/instructions/review-gates/semantic/underspecified-assertions.md
note: kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
note-sha256: 0366cb851ef44475ed808292e3919e8d5559c86b5d72261a6cdd8d5c82ee0aab
criterion: kb/instructions/review-gates/semantic/underspecified-assertions.md
criterion-sha256: 8c6f8c1d87e6a7fd99a51fa6c2aa1f3068c6f9d3deeadbca86366dfb0b811410
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews
launch: d148fd8b499e463b9bbd05cdf1df7659
completed-at: '2026-11-17T07:24:13Z'
findings:
- scope: passage
  quotes:
  - If that scope includes the ability to revise the system's improvement machinery
  reason: 'This assertion states what a non-regression scope must include, and it
    allows two materially different readings. Reading A: the scope must include the
    first-order capability to produce and install another revision of the system,
    the capability the example agent loses. Reading B: the scope must include the
    second-order capability to revise the improvement machinery itself, such as editing
    the revision workflow or the evaluator. The unresolved choice is the scope of
    the checked capability. The choice changes what a declared comparison must test:
    whether another revision can still be carried through to use, or whether the revision
    workflow itself stays revisable. It also changes whether the example''s successor
    fails. The surrounding text ("the revision capability", "the only applicable revision
    path") leans toward Reading A, but the explicit object "improvement machinery"
    supports Reading B.'
  level: warn
contract: verdict
target-sha256: 28e4977c71d1722304dbfa6ed9b70589b670e9a1a08cccbd5896d3ac4d3c8b54
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/207af125e506b99513821c62/inputs/target/kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/artifact/reviews/207af125e506b99513821c62/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/an-improvement-can-close-the-path-to-further-improvement/28e4977c71d1/reviews/calls/launches/d148fd8b499e463b9bbd05cdf1df7659/outputs/review-underspecified-assertions.md
raw-output-sha256: b207411541bfdcbc9143ff8d1baa1a9cf5045162360559235b256b70064a8b09
---

# Review

Most load-bearing assertions are exact.

- **The worked example.** It names the workflow, the change and the lost route.
- **The replacement condition.** It requires a replacement to "carry another revision through to use".
- **The Scope entries.** They state the system boundary and alternative paths.

The note's operative recommendation is the sentence that says what non-regression must check. That sentence leaves the object of the checked capability unresolved between producing another revision and revising the improvement machinery. The two readings call for different checks in a declared comparison, so the difference is material.
