---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Both are declared while only the predecessor exists.
  reason: UNSUPPORTED — The anti-selection argument needs the declarer not to know
    the result. The note fixes antecedence only relative to installed states (the
    predecessor is merely 'current when the comparison is declared'). Candidates can
    be constructed and staged before the declaration, and the note says a staging
    comparison can supply evidence for adoption, so dimensions and thresholds can
    be chosen with a candidate's staging results in hand. 'Prior declaration prevents
    that form of post-hoc selection' therefore does not follow. Declaring before installation
    is not declaring before the result is known.
- scope: passage
  quotes:
  - This framework uses the predecessor's prior capabilities as that scope. Naming
    it makes explicit which losses would cause the comparison to fail.
  reason: THIN — Naming the scope 'the predecessor's prior capabilities' makes failing
    losses explicit only if those capabilities can be enumerated with thresholds.
    The note's own Open Question doubts that for an open-ended family. The note also
    gives no reason for choosing this scope over a narrower declared one, beyond its
    being the framework's choice.
- scope: passage
  quotes:
  - Whether it got *better* is therefore its own claim with different relata and its
    own declarations.
  reason: THIN — The 'therefore' licenses only that improvement is a separate claim
    from retention, because retention carries no quality requirement. It does not
    establish that the separate claim has *different relata* (states rather than the
    change). That premise is introduced here and argued only later by stipulating
    the predecessor and successor terms.
- scope: passage
  quotes:
  - Comparing otherwise equivalent runs with and without the retained instruction
    tests its contribution
  reason: HOLDS — The linked contrast principle supports the claim that a with/without
    comparison identifies the instruction's contribution to that contrast. The burden
    of 'otherwise equivalent' is visible rather than hidden. The contrast does not
    test that experience produced the instruction, but the note assigns that link
    separately, so the joint claims no more than it supports.
- scope: passage
  quotes:
  - holding model weights fixed does not put the comparison out of reach
  reason: HOLDS — Given the linked premise that the deployed system is the unit of
    learning, a change to any operative non-weight component changes the compared
    state. A comparison with fixed weights therefore remains well-formed. The conclusion
    is modest and follows directly.
outcome: report
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/composition-friction-gate.md
contract: report
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/composition-friction-gate.md
note-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
criterion-sha256: 3707753f84e8f72696b0d30a580c6c0df6e56e914201550d788f69e4f906601b
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/1551bbe5e1b94fb7c30477e7/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/1551bbe5e1b94fb7c30477e7/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: c0ca38b23c5a490e96eff7989c83d041
completed-at: '2026-11-18T00:22:14Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/c0ca38b23c5a490e96eff7989c83d041/outputs/review.md
raw-output-sha256: cb161592bbf8e2c580cd407291e15c13580ea0c215fb40a14579d2ba8032714d
format: 2
---

# Friction check: better-factory claim compares operative states

**Central claim (one sentence):** A claim that a factory got better compares the predecessor state with the installed, depended-on successor state under an assessment relation, non-regression on the predecessor's prior scope plus a declared improvement on a named dimension, fixed before the development it judges.

## Filter
**Filter:** SURVIVES

The properties held at once are: operative-state relata, antecedent declaration, relation-relativity (not a quality verdict), non-regression over prior capabilities, and a declared improvement target. These can coexist. The Scope section keeps the claim consistent by making antecedence an auditability condition rather than a constitutive one, and by making the preserved-development-path consequence conditional on the checked scope. The pressure point is non-regression over an open-ended prior scope. The note leaves it as an open question, not as a contradiction.

## Thinnest joints

The antecedence joint ranks thinnest. The note's distinctive addition to the linked independent-specifiability requirement is prior declaration, and that addition is justified by one mechanism, blocking post-hoc selection. The note's own vocabulary lets candidates and staging evidence exist before the declaration, so the stated timing condition does not secure the information barrier the mechanism needs. The prior-capabilities scope ranks next. Its claimed benefit, explicit failure conditions, depends on enumerability, which the note itself questions. The "different relata" step is a smaller gap: the conclusion is plausible, but the stated reason does not carry it. The two `because` joints that cite linked notes hold, because each asks for only what its premise gives.

## For the human

First specify what "declared while only the predecessor exists" excludes: must declaration precede the construction or staging evaluation of candidates, or only installation?
