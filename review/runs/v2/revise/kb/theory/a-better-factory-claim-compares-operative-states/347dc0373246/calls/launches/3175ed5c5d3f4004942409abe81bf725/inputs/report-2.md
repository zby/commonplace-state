---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-better-factory-claim-compares-operative-states.md
  against kb/instructions/critique-note.md
note: kb/theory/a-better-factory-claim-compares-operative-states.md
note-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews
launch: 0889a6b4464e4168ab5b4ddb2ca0b130
completed-at: '2026-11-16T22:00:46Z'
findings:
- scope: passage
  quotes:
  - Passing the comparison establishes improvement between the two states; the open
    part is attribution — who or what learned.
  reason: 'The sentence overstates what a passed comparison shows. The successor is
    measured later than the predecessor. On production dimensions, that later measurement
    runs in a changed environment: the task mix drifts, external models and tools
    change, and later work already depends on the successor. A pass is therefore confounded
    by environmental change before attribution becomes an issue. The note uses the
    contrast-identification principle only for the experience link. It should also
    say what contrast the improvement comparison runs. One option is to baseline the
    predecessor at declaration on a fixed, replayable suite. Another is to run the
    predecessor and successor on matched work. Otherwise the claim should be limited
    to ''passed the declared relation under the conditions measured''.'
- scope: passage
  quotes:
  - It may be the state after a period of development or after a single retained change;
    either way it is already operative when measured
  reason: The measurement route says nothing about how the predecessor's side of the
    comparison is obtained. The compared states 'span the whole production environment',
    and in an interleaved process the predecessor is superseded continuously. Once
    superseded, it usually cannot be re-run. The comparison then relies on a baseline
    recorded at declaration time. If no such baseline exists, it relies on a time-series
    reading that the antecedence condition does not protect. The note should require
    the predecessor-side measurement to be fixed together with the relation, or name
    this as a limit.
- scope: passage
  quotes:
  - A real episode can be described either way, and the description determines where
    the evaluator sits.
  reason: This conflicts with the evaluator-location section. That section says judgment
    that controlled installation is on the causal update path, which is a fact about
    the episode. If the chosen description fixes evaluator location, an author can
    describe a human-gated admission as a measurement and keep the human off the causal
    path. That reopens the post-hoc freedom the note works to close. The note should
    say which facts about the episode constrain the description. Gating, if it occurred,
    should fix the admission reading.
contract: report
target-sha256: 347dc0373246bc0c26cae06050cec4c0334af5c876bcb2555736417cf94f41cc
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/402c2c3a10da8fd3b6c7f330/inputs/target/kb/theory/a-better-factory-claim-compares-operative-states.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/artifact/reviews/402c2c3a10da8fd3b6c7f330/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-better-factory-claim-compares-operative-states/347dc0373246/reviews/calls/launches/0889a6b4464e4168ab5b4ddb2ca0b130/outputs/review.md
raw-output-sha256: d62ec30534236891829c18c6460362a03577d22098837fbf1d3331a4573ffe1c
attack-outcome: partially lands
---

# Critique: A better-factory claim compares operative states under an antecedent assessment relation

**Note:** kb/theory/a-better-factory-claim-compares-operative-states.md
**Central commitment:** A better-factory claim is determinate only when it declares four things. The relata are the predecessor and the installed, depended-on successor, not a candidate. The relation is fixed before the development and combines non-regression on the prior scope with a named target. The successor's route is either measurement or admission. Evaluator location is declared separately from the learner boundary.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is a practitioner of online experimentation and causal evaluation, such as an A/B-testing or counterfactual-evaluation engineer. On this view, "the successor is better than the predecessor" is a counterfactual claim. The question is how the successor performs on the same work under the same conditions, compared with the predecessor. Only a matched contrast can answer it: run both on shared tasks, or run them concurrently on randomized traffic.

The note makes the later relatum the installed, depended-on state and treats a staging comparison only as "evidence for that decision". That choice moves the comparison away from a matched contrast in two ways:

1. **Time separation confounds the result.** The operative successor is measured later than the predecessor, and the note's measurement route is a "measurement boundary drawn on a continuous process". On a "named production dimension", the later measurement takes place in a different environment. The task distribution has drifted. External models and tools may have changed. Because later work depends on the successor, the successor has itself shaped the work it is measured on. Antecedence stops post-hoc choice of dimensions. It does not stop the environment from passing the comparison for the factory. A successor that is no better can pass because the work became easier, and a better one can fail because the work became harder.
2. **The predecessor usually cannot be recovered.** The compared states "span the whole production environment", including prompts, artifacts, tools, workflows, tests and evaluators. In an interleaved process, that whole state is not normally kept as a runnable snapshot. Once it is superseded, the predecessor's side of the comparison is either a baseline recorded at declaration or a recollection. The note requires neither.

The opponent concludes that the defensible relata are runnable configurations compared on matched work, which is what the note calls candidates. Installation is a further fact about deployment and adds nothing to the comparison except confounds. The note's own sentence "Passing the comparison establishes improvement between the two states" is therefore false as written whenever the comparison is not matched.

## How the note engages it

**Partially engaged.** Several parts of the note limit the attack:

- The relation is fixed "while only the predecessor exists". On a natural reading, this includes measuring the predecessor's baseline at declaration. On a fixed, replayable suite, that covers the non-regression component and the recovery problem.
- The note grants that a staging comparison is evidence for the claim. It insists only that the claim's later term is the installed state. That position is consistent: the relata can be operative states while the evidence comes from a matched contrast. Taken as a claim about what the relata are, the note's main commitment survives. Installation does determine which state the claim is about, and a discarded candidate should not count.
- The Scope section admits that the framework "does not supply an oracle" and that a properly declared comparison can still measure the wrong thing. The first open question raises whether the prior scope can be specified for open-ended families.
- The note applies [an experiment identifies only the contrast it actually runs](./an-experiment-identifies-only-the-contrast-it-actually-runs.md), but only to attribution, meaning whether the factory learned.

Three things go unengaged. The note never applies the contrast principle to the improvement comparison itself. It does not say how the predecessor-side measurement is obtained in the measurement route. Its "Neither claim entails the other" section says that passing establishes improvement between the states. The attack lands on that sentence and on the missing predecessor-measurement requirement. It does not land on the choice of operative states as relata.

## Constructive findings

- Limit "Passing the comparison establishes improvement between the two states", or add a condition to it. Passing establishes improvement under the declared relation only when the comparison is matched. That means a predecessor baseline fixed at declaration on a replayable suite, or matched runs of both states. For production-dimension targets measured over time, say that environmental drift and the successor's own effect on later work are confounds the declarations do not remove.
- Add the predecessor-side measurement to what antecedence fixes. Declare the relation and also record the predecessor's measured standing on it at declaration time. Otherwise the measurement route compares a present measurement with nothing. This also turns part of the first open question into a concrete requirement.
- Bring the Scope bullet on successor routes into line with the evaluator-location section. State that whether an evaluator gated installation is a fact about the episode. Choosing a description cannot move a gating evaluator off the causal path.

## Secondary objections (optional)

- The note says the compared state includes evaluators and tests, but it does not say whose tests decide the relation. Antecedence implies the relation stays fixed even if the successor revises its own test suite, but the note does not state this. A reader could take a successor that rewrote its acceptance tests to be measured by them.
- The line `TODO! remove or update to use software house instead of software factory` signals a pending terminology change. If "software house" replaces "software factory", the note's title, the claim's name and the scope bullet that relies on factory development may all need revising. The critique judges the current factory wording.
