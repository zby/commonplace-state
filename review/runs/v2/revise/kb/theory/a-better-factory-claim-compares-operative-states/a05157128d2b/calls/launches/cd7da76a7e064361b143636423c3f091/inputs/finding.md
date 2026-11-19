---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 5de9bf9355e2491a931e50feca31b7f2
completed-at: '2026-11-18T00:18:19Z'
findings:
- scope: passage
  quotes:
  - A [software factory](./definitions/software-factory.md) undergoes experience-responsive
    retention
  reason: The note's central object, a software factory, is linked to its definition
    but never glossed inline. The sentence implies it has 'reusable machinery', but
    a reader cannot tell what kind of system counts as a software factory (an agentic
    production system? a human-plus-tool development process?) without following the
    link. Add a short appositive gloss on first mention.
  level: warn
- scope: passage
  quotes:
  - not a verdict on the factory's quality over its open production family
  reason: '''Open production family'' is KB-specific phrasing used without definition;
    the reader cannot infer what a production family is or what makes it open. The
    same concept returns in Scope (''over an open family'') and Open Questions (''the
    declared family is open-ended''). Gloss it on first use, e.g. as the unbounded
    range of production tasks the factory may face.'
  level: warn
- scope: passage
  quotes:
  - that later production and factory development depend on
  reason: '''Factory development'' is first used here without a gloss; its link and
    the implied meaning (revising the factory''s own machinery) arrive only later
    in the note. The plain reading is largely inferable, so this is minor, but a brief
    gloss at first mention would help.'
  level: info
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/0451a4c56092869f04c4f3ea/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/0451a4c56092869f04c4f3ea/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/5de9bf9355e2491a931e50feca31b7f2/outputs/review-undefined-terms.md
raw-output-sha256: 0127c8a628a211b6501ae7c24a6c14b9471ee1d0ee64a18cf872b757cfc3ddd7
---

# Review

Most technical terms are introduced with adequate inline context. "Experience-responsive retention" is defined in the same sentence. "Operative" is glossed as installed and depended on, not merely stored. "Antecedent" is explained as fixed before the development it judges. The two parts of the assessment relation and the prior scope used for non-regression are spelled out in their own sections.

The gaps are at the entry point. The compared object, the software factory, has only a link. The phrase "open production family", which bounds what the claim does not cover, is never explained, but the note's scope disclaimers depend on it.
