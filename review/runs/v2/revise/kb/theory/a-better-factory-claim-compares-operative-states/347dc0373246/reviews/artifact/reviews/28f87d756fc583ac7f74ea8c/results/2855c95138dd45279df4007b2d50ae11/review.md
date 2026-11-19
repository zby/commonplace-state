---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Non-regression runs over the predecessor's prior scope
  reason: 'DOUBTFUL — Premise (unmoded, so read as universal): the predecessor''s
    prior scope can be specified well enough that a declared non-regression threshold
    over it is checkable, so the relation is determinate once declared. — The note''s
    own framing says a factory works over an open production family, so for factories
    the ordinary case is a prior scope that cannot be enumerated. A threshold over
    an unenumerable scope can be declared in advance and still cannot be checked;
    checking it needs a declared proxy, such as a finite task sample, which makes
    it non-regression on the proxy, not on the prior scope. The note leaves this as
    an Open Question when it is a condition on the ''four declarations make the claim
    determinate'' thesis. A repair can declare the proxy and move the condition into
    Scope, so the failure is local. — LOCAL — prevalence'
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated premise (universal): the predecessor stays evaluable
    under the declared relation when the comparison is run, so both relata can be
    measured on the same instances. — Under measurement over snapshots, the predecessor
    is superseded in place and no artifact need preserve it. Compared states ''span
    the whole production environment'', including hosted models, external tools and
    services that change outside the factory''s control. Such dependencies are common,
    so re-running the predecessor often means rebuilding a state that can no longer
    be rebuilt. The comparison then pairs a measured successor with a recalled or
    partly rebuilt predecessor, and environment drift is confounded with factory change.
    A repair can require a preserved or replayable predecessor state as a condition.
    — LOCAL — prevalence'
- scope: passage
  quotes:
  - A real episode can be described either way, and the description determines where
    the evaluator sits.
  reason: 'DEFEATED — Premise (universal): the choice between the two successor routes
    is a declaration about how an episode is read, and that description determines
    the evaluator''s location. — This contradicts the body, which says judgment that
    controls installation places the evaluator on the causal update path because it
    ''determines what the factory retains''. Counterexample: a human reviewer rejects
    two candidates and admits the third. Describing the episode as measurement over
    snapshots of the installed state leaves the causal fact unchanged: that person''s
    judgment gated retention. The description chooses which comparison is reported.
    Whether the evaluator gated the successor is a causal fact that the declaration
    must record, not create. Removing or qualifying this Scope bullet leaves the body''s
    account intact. — LOCAL — instance'
- scope: passage
  quotes:
  - non-regression over that set requires the successor to keep such a path
  reason: 'DOUBTFUL — Premise (universal): scope-indexed non-regression, as declared,
    already covers the factory-development path whenever the predecessor had one,
    so preservation ''falls out'' without separate declaration. — The relation section
    says non-regression is checked by thresholds that are declared in advance. The
    preservation section reads ''prior scope'' as the whole capability set. A comparison
    with antecedent thresholds only on production dimensions, such as task pass rate
    and latency, never measures whether a factory-development path remains applicable.
    A successor that closes that path can then pass. Preservation follows only if
    the declaration must list factory development as a checked element of scope, which
    is an added condition, not a consequence. — LOCAL — instance'
- scope: passage
  quotes:
  - Fixing the dimensions and thresholds in advance is what makes the comparison capable
    of failing.
  reason: 'DOUBTFUL — Premise (universal): declaring dimensions and thresholds in
    advance is enough to block post-hoc fitting of the comparison. — Dimensions and
    thresholds do not fix the measurement instances or procedure. An evaluator who
    declares ''pass rate on coding tasks ≥ X'' but picks the task set, harness or
    sampling after seeing the successor keeps the post-hoc freedom that antecedence
    was meant to remove. The comparison can fail, but only in name. A repair would
    extend the antecedent declaration to the measurement procedure and instance set.
    — LOCAL — instance'
- scope: passage
  quotes:
  - it is already operative when measured, and the measurement judges a realized trajectory
    rather than performing adoption
  reason: 'DOUBTFUL — Premise (universal): in an interleaved process, a successor
    state can be fixed at a measurement boundary and measured as one state. — In the
    note''s own interleaved process, each failed task causes a retained note, test
    or rule under the running factory. Running the measurement battery under that
    factory therefore keeps changing the state being measured. Later measurement tasks
    run against a different state than earlier ones, so the ''successor'' is a moving
    interval, not one relatum. A repair can freeze retention during measurement or
    declare the successor as the state at the start of measurement. — LOCAL — instance'
- scope: passage
  quotes:
  - Measuring whether a realized change helped does not by itself place a person on
    the causal update path
  reason: 'DOUBTFUL — Premise (universal): measurement that follows an update is off
    the causal path that produced the measured successor. — This holds for the single
    measured transition, but an antecedent relation is known before development. A
    factory or operator that knows the declared dimensions and thresholds will steer
    development toward them, so the anticipated evaluation shapes the trajectory without
    gating installation. Results from interim measurements over a development period
    also feed later changes inside the same measured period. Neither case makes the
    evaluator an admission gate, but both weaken the clean measurement-versus-admission
    split the evaluator-location argument relies on. A repair can qualify the split
    to the measured transition. — LOCAL — instance'
- scope: passage
  quotes:
  - 'Retention has no quality requirement: a retained change can degrade the factory
    as easily as improve it.'
  reason: 'HOLDS — Premise: retention is defined without a quality condition, so improvement
    needs a separate claim. — The linked learning note defines experience-responsive
    retention by its causal and dependency conditions alone. A regression that later
    work depends on, such as a bad rule installed after a misread failure, meets it.
    No counterexample was found; ''as easily'' is loose but not load-bearing.'
- scope: passage
  quotes:
  - A candidate that is generated and discarded never enters the comparison
  reason: 'HOLDS — Premise: only installed, depended-on states are relata; a discarded
    candidate is not one. — This follows from the operative-change condition the note
    adopts. The hunt looked for a case where a discarded candidate must be a relatum,
    such as an A/B arm later rolled back. That arm was operative while it ran, so
    it is a successor in its own right and not a counterexample.'
- scope: passage
  quotes:
  - Without antecedence the claim is close to unfalsifiable
  reason: 'HOLDS — Premise (hedged ''close to''): when the relation is chosen after
    the fact, almost any differing successor can be shown better on some named dimension.
    — This matches the redescription argument in the linked declared-objective note.
    The edge case of a successor that differs only in ways no dimension registers
    is covered by the hedge.'
- scope: passage
  quotes:
  - holding model weights fixed does not put the comparison out of reach
  reason: 'HOLDS — Premise: a better-factory comparison can register improvement made
    only through non-weight machinery such as prompts, tools, tests and workflows.
    — A factory whose only change is a new test gate that cuts shipped defects is
    a direct instance. The hunt found no case where a fixed model blocks the comparison.'
- scope: passage
  quotes:
  - A successor can even pass with no experience link at any boundary
  reason: 'HOLDS — Premise: passing the comparison does not entail learning at the
    declared boundary. — A factory rebuilt from a supplied specification by an outside
    builder can pass with no retained experience from the predecessor. The concrete
    case confirms the premise, and no counterexample to the non-entailment was found.'
outcome: report
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/premise-decomposition-gate.md
contract: report
note: kb/theory/a-better-factory-claim-compares-operative-states.md
criterion: kb/instructions/premise-decomposition-gate.md
note-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
criterion-sha256: daf263bd7f5fff877fecff20771f903459ac2f0b585044e1f68c4d871c59623b
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/28f87d756fc583ac7f74ea8c/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/28f87d756fc583ac7f74ea8c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 2855c95138dd45279df4007b2d50ae11
completed-at: '2026-11-16T22:03:15Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/2855c95138dd45279df4007b2d50ae11/outputs/review.md
raw-output-sha256: 427c9d33692479f630ab073cfa2396d58bf9c2646c67166e2af41b0e770e9399
format: 2
---

# Premise decomposition: better-factory claim compares operative states

**Register:** claim
**Central commitment (one sentence):** A claim that a factory got better is determinate and auditable only when four things are declared: operative predecessor and successor states as relata, an antecedent scope-indexed relation, the route by which the successor arose, and an evaluator location separate from the learner boundary.

## Premises and counterexamples

The commitment rests on one premise per declaration and on the conditions that keep each one checkable. The first group makes the relata well defined. Improvement must be a separate claim from retention, candidates must be excluded, a successor must be fixable as one state, and the predecessor must stay measurable. The last premise is unstated and is the one the note most needs to add. The second group makes the relation determinate: antecedence must block post-hoc fitting, and the prior scope must be specifiable enough to check. The preserved-path consequence is derived from this group, so it depends on how 'scope' is declared. The third group separates evaluator location from the learner boundary. It needs the measurement/admission split to be causally clean, and it needs the route to be a fact the declaration records rather than one it chooses.

Each failure found can be repaired by adding a condition or narrowing a reading, and none forces the commitment itself to be withdrawn, so all are local. The pattern is the same across them. The note names the right declarations, but several are underspecified for checking: the scope, the measurement instances and the predecessor's availability. One Scope bullet also contradicts the body's causal account of evaluator location.

## For the human

Start with prior-scope specifiability. Over an open production family, the note's 'determinate' thesis depends on a declared scope proxy that it currently leaves as an Open Question.
