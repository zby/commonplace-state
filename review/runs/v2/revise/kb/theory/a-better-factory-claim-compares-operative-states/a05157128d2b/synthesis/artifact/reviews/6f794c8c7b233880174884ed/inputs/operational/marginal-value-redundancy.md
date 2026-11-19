---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 665981a8d0a94724aba21e71778aba84
completed-at: '2026-11-18T00:20:53Z'
findings:
- scope: passage
  quotes:
  - 'Antecedence blocks post-hoc dimension selection. It does not make the declared
    dimensions the right ones: a comparison can be properly declared in advance and
    still measure something that does not matter.'
  reason: 'This Scope bullet repeats the assessment-relation section almost line for
    line: ''Prior declaration prevents that form of post-hoc selection. It does not
    show that the requirements track factory quality.'' The bullet''s only addition
    is the phrase ''still measure something that does not matter'', which restates
    the same limit. Cut the bullet, or keep only that phrase and fold it into the
    earlier sentence.'
  level: warn
- scope: passage
  quotes:
  - The framework indexes and disciplines the comparison; it does not supply an oracle
    for it. What makes a successor genuinely better over an open family remains unresolved
    here.
  reason: 'The opening paragraph already sets this boundary: ''the claim is relation-relative
    and auditable, not a verdict on the factory''s quality over its open production
    family.'' The Scope section then states the same limit twice more, in this bullet
    and in the antecedence bullet. Counting the end of the relation section, the note
    says four times that declared requirements need not track real quality. Keep one
    plain statement of the limit, either in the introduction or in Scope, and cut
    this bullet or merge it with the antecedence bullet.'
  level: warn
- scope: passage
  quotes:
  - 'Non-regression needs a declared scope: the capabilities the successor must preserve,
    with thresholds specifying how much degradation is permitted. This framework uses
    the predecessor''s prior capabilities as that scope. Naming it makes explicit
    which losses would cause the comparison to fail.'
  reason: 'Two paragraphs earlier, the note already gives non-regression as thresholds
    ''on the predecessor''s prior scope''. This paragraph says that again and adds
    a sentence (''Naming it makes explicit which losses…'') that only follows from
    having a declared scope. It adds one useful gloss: the thresholds set how much
    degradation is permitted. Fold that gloss into the two-component sentence and
    drop the paragraph.'
  level: warn
- scope: passage
  quotes:
  - A comparison judges the adopted states. Whether an evaluator also controlled adoption
    is a separate causal question; a description cannot change whether its judgment
    was required for installation.
  reason: The note separates adoption from the comparison twice before this bullet.
    The relata section says 'A staging comparison can supply evidence for adopting
    a candidate; the improvement claim concerns the state actually installed and used.'
    The improvement section says 'Internal controls on what the factory retains govern
    adoption, but do not by themselves establish that the adopted state passes the
    declared comparison.' This third statement adds only an opaque clause about a
    description. Cut it, or fold any distinct point into one of the earlier sentences.
  level: warn
- scope: passage
  quotes:
  - Preserving factory development follows only when that capability is included in
    the checked scope.
  reason: This repeats the condition already stated in the factory-development paragraph
    ('If the checked prior scope includes an operative path for factory development,
    non-regression requires the successor to preserve that capability'). The first
    sentence of the bullet, which generalizes the framework to other systems, does
    new work. This trailing sentence does not and can be cut.
  level: warn
contract: verdict
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/aa8e05d4179cdd32189903ea/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/aa8e05d4179cdd32189903ea/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/665981a8d0a94724aba21e71778aba84/outputs/review.md
raw-output-sha256: 51e04ccf60a369bef57a8f6b55080d26047c66c60217cba7857af087acf45246
---

# Review

## Summary

The note's core moves each earn their space. The definitions of predecessor, candidate and operative successor do work. So do the two-component relation, the point that holding model weights fixed does not put the comparison out of reach, and the requirement to preserve a factory-development path. The three hypothetical cases are the clearest way the note separates retention, improvement and learning. Their closing line, "The declared comparison judges improvement; the experience-to-change link distinguishes learning", turns the cases into a decision rule. It is a permitted restatement.

The redundancy is concentrated in hedges about what the framework does not establish. The note says at least four times that a properly declared comparison need not track real quality: once in the introduction, once at the end of the relation section and twice in Scope. It also separates adoption from the comparison in three places. The Scope section mostly restates boundaries the body has already drawn. It adds two things the body does not say: retrospective criteria can ground a different, legitimate improvement claim, and a relation can be declared that allows obsolete capability to be retired. Those two bullets should stay. The flagged bullets and the non-regression paragraph should be cut or folded as described in the findings.

The roadmap sentence after the opening paragraph ("The comparison names the predecessor and adopted successor…") is borderline. It previews the section structure briefly and is not flagged.
