---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews
launch: 734813e048274e73a7a5a1daf4a38636
completed-at: '2026-11-18T00:24:10Z'
findings:
- scope: passage
  quotes:
  - An independently supplied retrospective criterion can ground a legitimate improvement
    claim, just not this audit-proof one.
  reason: 'DOUBTFUL — premise (universal, carried by the title): every better-factory
    claim is made under an assessment relation declared before the development it
    judges — the note''s own Scope concedes a counterexample: a held-out benchmark
    or independent criterion first specified after development, but not fitted to
    the result, grounds a legitimate improvement claim with no antecedent relation.
    The body partly absorbs this by stipulating that ''better'' means better under
    the declared relation, but the title still reads as a claim about better-factory
    claims in general. The rescue rescopes the commitment itself (to auditable, antecedently
    declared better-factory claims), not one premise, so the failure reaches the central
    commitment as titled — GLOBAL — instance'
- scope: passage
  quotes:
  - Prior declaration prevents that form of post-hoc selection.
  reason: 'DOUBTFUL — premise (universal): declaring dimensions and thresholds while
    only the predecessor exists blocks selecting requirements the successor happens
    to satisfy — two routes to selection survive prior declaration: (a) declaring
    several antecedent comparisons and citing the one the successor passed, which
    is selection after seeing results among pre-declared relations, the case preregistration
    handles by naming one primary outcome; (b) declaring the improvement dimension
    while a planned candidate is already conceived, so the dimension is chosen for
    what the candidate is designed to improve. Neither defeats the narrow form the
    sentence names, but the note does not fence them; a Scope qualification (one primary
    comparison per claim, or all declared comparisons reported) repairs it — LOCAL
    — instance'
- scope: passage
  quotes:
  - This framework uses the predecessor's prior capabilities as that scope.
  reason: 'DOUBTFUL — premise (universal): the predecessor''s prior capabilities form
    a non-regression scope that can be named and checked at declaration time — the
    body says ''prior capabilities'' while the description says ''declared prior capabilities''.
    If the scope is all prior capabilities, a factory whose working behaviours include
    undocumented or latent ones (a retrieval habit nobody listed, a prompt side effect
    production silently relies on) can regress on them unchecked, and the comparison
    is not checkable. If the scope is only the declared ones, the non-regression guarantee
    is narrower than the prose suggests. The Open Questions concede checkability for
    open-ended families; stating which reading the framework takes, in Scope, repairs
    it — LOCAL — instance'
- scope: passage
  quotes:
  - The compared states span the whole production environment.
  reason: 'DOUBTFUL — premise (universal): treating the compared state as the whole
    production environment yields a comparison of the factory — when the environment
    includes parts the factory does not control, such as a hosted model the vendor
    silently upgrades or external data and API drift between the two measurements,
    the successor can pass the declared comparison with no change to the factory''s
    own reusable machinery. The note counts an externally selected tool upgrade as
    ''improvement without learning'', but an upgrade nobody in the factory installed
    strains ''the factory improved''. Bounding the compared state to machinery the
    factory installs, or requiring comparable conditions, repairs it — LOCAL — instance'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — unstated premise (universal): the predecessor can still be measured,
    after the successor is installed, under conditions comparable to the successor''s
    measurement — once a successor is operative, the predecessor may no longer be
    re-runnable: external tools, models, data or the production mix have moved, so
    its baseline is a historical measurement under different conditions and a measured
    difference confounds factory change with environment change. The first Open Question
    names baseline and comparable conditions but does not state that the comparison
    depends on them; making that dependency explicit as a condition in Scope keeps
    the commitment — LOCAL — instance'
- scope: passage
  quotes:
  - a retained change can degrade the factory as easily as improve it
  reason: 'DOUBTFUL — premise (as worded, a symmetry claim): retained changes degrade
    as readily as they improve — the argument needs only that retention can degrade,
    and the symmetry is contradicted where retention passes through gates or tests
    (the ''internal controls on what the factory retains'' the note itself mentions),
    which make degrading retentions rarer than improving ones in the ordinary gated
    pipeline. Weakening to ''can degrade the factory'' removes the dent without touching
    the commitment — LOCAL — prevalence'
- scope: passage
  quotes:
  - A candidate that is generated and discarded never enters the comparison, so a
    better-factory claim cannot be read off a construction event.
  reason: 'HOLDS — premise (universal): the relata are the predecessor and the installed
    operative successor, and a discarded candidate is not a relatum — hunted cases:
    a staging A/B on a candidate (conceded as adoption evidence, not the improvement
    claim); a successor rolled back after failing (still operative while it held,
    per the linked operative-change definition); continuous revision (handled by a
    named measurement boundary). None defeats it.'
- scope: passage
  quotes:
  - on the predecessor's prior scope, and must
  reason: 'HOLDS — premise (stated as this framework''s chosen shape, not the only
    one): the relation consists of non-regression thresholds plus a declared improvement
    on at least one named dimension — hunted: a large gain bought with small regressions
    (absorbed by thresholds that permit declared degradation); retiring unsafe capability
    (conceded and fenced in Scope). At its stated modality no counterexample survives.'
- scope: passage
  quotes:
  - non-regression requires the successor to preserve that capability
  reason: 'HOLDS — premise (conditional): if the checked scope includes an operative
    factory-development path, non-regression requires preserving it — the condition
    makes this nearly analytic, and the Scope line on retirement-permitting relations
    fences the case where it would not follow.'
- scope: passage
  quotes:
  - This is learning when the experience-derived change causally contributes to the
    improvement.
  reason: 'HOLDS — premise (universal): improvement, retention and learning are distinct
    claims, and learning additionally requires the experience-derived change to contribute
    causally — the three hypothetical cases separate them cleanly; interaction effects
    and stochastic runs make the with/without contrast harder to run but do not falsify
    the distinction, and the linked experiment note bounds what the contrast identifies.'
- scope: passage
  quotes:
  - the claim is relation-relative and auditable, not a verdict on the factory's quality
    over its open production family
  reason: 'HOLDS — premise (stipulation): ''better'' is read as better under the declared
    relation — hunted for an equivocation where the note later uses ''better'' in
    an unindexed sense; the Scope repeatedly disclaims an oracle and tracking of true
    quality, so the stipulation is held consistently in the body (the tension sits
    with the title, recorded separately).'
contract: report
target-sha256: a05157128d2b484721e22e5ce6a2c52816922a6bbe185d20025ad265eafdc830
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/613593885031d3ce99873aae/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/artifact/reviews/613593885031d3ce99873aae/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/a05157128d2b/reviews/calls/launches/734813e048274e73a7a5a1daf4a38636/outputs/review.md
raw-output-sha256: 8da586be493ed9aff8d53642db5f09c7287db4b97e1b8d0f965b75ee00b48c60
---

# Premise decomposition: better-factory claims compare operative states

**Register:** claim
**Central commitment (one sentence):** A claim that a software factory got better compares the predecessor state with the installed operative successor under an assessment relation, consisting of non-regression on the predecessor's prior scope plus a declared improvement on a named dimension, fixed before the development it judges, and this claim is distinct from retention and from learning.

## Premises and counterexamples

The commitment has three load-bearing parts, and each consumes its own premises.

The first part says what is compared: the relata are operative states, not candidates or construction events. Its premises concern which states count, and whether both states can be measured comparably. The relata premise holds. The comparability premises are where the commitment is thinnest. The note treats the whole production environment as the compared state but never states that the predecessor stays measurable under conditions comparable to the successor's. Uncontrolled environment drift can therefore pass for factory improvement.

The second part says how the states are compared: an antecedent, two-component, scope-indexed relation. Its premises are that prior declaration blocks post-hoc selection, that the predecessor's prior scope can be named, and that the two-component shape is adequate as this framework's choice. The shape premise holds because Scope fences it. The antecedence premise holds against the narrow failure it names but leaves multiple-comparison selection and design-anticipating declaration unfenced. The scope premise turns on an unresolved ambiguity between "prior capabilities" and "declared prior capabilities".

The third part separates improvement from retention and learning. Its premises are that retention carries no quality guarantee and that learning needs causal contribution. Both hold in substance; only an overstated symmetry in the retention premise is dented.

The decomposition also checks whether the commitment is universal over better-factory claims or limited to the framework's auditable kind. The note's Scope concedes that a retrospective but independent criterion can ground a legitimate improvement claim. The body's stipulation limits "better" to the declared relation, but the title still reads universally. That gap is the one failure that reaches the commitment itself rather than one premise.

## For the human

Look first at the title-versus-Scope tension: either rescope the title to auditable, antecedently declared better-factory claims, or drop the concession that retrospective independent criteria ground legitimate improvement claims.
