---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Antecedence guards this claim's auditability; it is not constitutive of improvement.
  - the indexed and antecedent conditions this applies to a pairwise state comparison
  reason: 'The term ''antecedent/antecedence'' is shared with the linked note ''Self-improvement
    is relative to a declared objective''. There, antecedence is a constitutive pathway
    condition (independent specifiability plus causal shaping) whose failure makes
    the claim false or empty. This note''s own explication of the term is temporal
    prior declaration of comparison requirements. The footer says the note ''applies''
    the source''s antecedent condition. The Scope bullet says antecedence is ''not
    constitutive of improvement''. Reading 1: the term names the inherited concept,
    so the Scope bullet denies the source''s claim. Reading 2: the term names this
    note''s new temporal condition, so the note contributes a distinct condition under
    a reused name. The body paragraph distinguishing ''prior declaration'' from ''independent
    specifiability'' partly settles this, but the title, heading, Scope bullet and
    footer all use the bare term. The choice changes what the note inherits versus
    contributes and whether it contradicts its grounding note. The author must decide
    whether ''antecedent'' here names the inherited condition, the added temporal
    one, or both, and label it consistently.'
  level: warn
outcome: warn
description: Retained verdict review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/review-gates/semantic/conceptual-role-conflation.md
contract: verdict
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
note-sha256: e92964105187394f3212d2c6bdf568f07030246459b46429c89c70335e41378b
criterion-sha256: f8badd8635e1273dc87abd558f5631019a4238c75f5af84cf38e64933a44b803
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/b3458e028fb44842eba6196f/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/b3458e028fb44842eba6196f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 3201016eb0fe485d8456e269c8f1d639
completed-at: '2026-11-18T00:21:21Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/3201016eb0fe485d8456e269c8f1d639/outputs/review-conceptual-role-conflation.md
raw-output-sha256: 66dd344d0d0bc2ee0c581219a07ed7031fb8fd36af676be941756382ac9d3e49
format: 2
---

# Review

Most passages separate their roles cleanly.

- "Operative" is explicitly imported from the operative-change definition in its behavioral-authority sense.
- "Software factory" and "factory development" are imported definitions applied to the object being compared.
- "This framework" consistently names the note's own explication.

The note also marks its own choices as its own: "This framework uses the predecessor's prior capabilities as that scope" and "the shape this framework declares, not the only declarable one".

The one material blur concerns "antecedent". The linked self-improvement note gives the term a technical meaning: independent specifiability, plus a requirement that evidence causally shaped the change. That note calls the condition constitutive, because failing it makes the attribution false. This note's paragraph on prior declaration does say it *adds* prior declaration to independent specifiability. That sentence separates the inherited condition from the contributed one. Elsewhere the note uses the bare term for the contributed temporal condition: in the title, the section heading and the Scope bullet. The Relevant Notes entry says the note *applies* the source's antecedent condition.

A reader following the link can therefore take "Antecedence … is not constitutive of improvement" in two ways. It may be a denial of the source note's antecedent condition. Or it may be a remark about a different, temporal condition that happens to share the name. That changes attribution and what the note contributes, so this is a WARN.
