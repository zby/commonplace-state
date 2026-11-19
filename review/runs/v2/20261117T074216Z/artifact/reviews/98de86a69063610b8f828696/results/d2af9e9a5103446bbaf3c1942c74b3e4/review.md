---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Optional observation is different from monitoring on which the process relies.
  reason: The note's operative test for dependency is waiting ('must wait', 'human
    stop'), but this sentence extends dependency to non-blocking monitoring without
    stating what 'relies' means. The process runs without the monitor, so 'relies'
    can only mean 'would run unacceptably without it'. Stating that counterfactual
    test explicitly, and saying that it, not blocking, is the general criterion, would
    let the note contend with the objection that blocking is a latency property rather
    than a dependency property.
- scope: passage
  quotes:
  - Whether a check is adequate, and whether a change improves the system, remain
    separate questions.
  reason: If dependency on post-adoption monitoring is judged by whether the process
    would degrade without it, then classifying a human activity as an operating dependency
    already presupposes a judgment about outcome quality. The scope bullet declares
    those questions separate without showing how the classification avoids them. The
    note should either admit that the non-blocking case requires a quality counterfactual,
    or restrict its clean separation to the blocking case.
- scope: passage
  quotes:
  - Anticipated assessment can shape proposals without creating a human stop.
  reason: 'The non-blocking example leaves open the case where later assessment revises
    the adoption rules or the agent''s instructions. Then the next adoption depends
    on that human verdict, although no single adoption waits for it. The note should
    classify this outer-loop case: an operating dependency on a longer timescale,
    or mere influence. Otherwise the ''Non-blocking assessment'' example does not
    show that the assessment is outside the operating process.'
- scope: document
  quotes: []
  reason: 'The file name (''evaluation-that-controls-adoption-helps-determine-the-change'')
    states a causal-contribution claim. The body explicitly rejects that framing:
    it distinguishes operating dependency ''rather than deciding who deserves causal
    credit''. The title (''Evaluation required for adoption is part of the operating
    process'') matches the body. The file name should be brought in line with the
    title, or a reader retrieving by path will expect the opposite commitment.'
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/critique-note.md
note-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: 541a682500facea176646d7bdfe6093663673fe51d93f06bb184d3c3d493580e
target-capture: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/98de86a69063610b8f828696/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/20261117T074216Z/artifact/reviews/98de86a69063610b8f828696/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261117T074216Z
launch: d2af9e9a5103446bbaf3c1942c74b3e4
completed-at: '2026-11-17T07:43:59Z'
raw-output: kb/reports/state/review/runs/v2/20261117T074216Z/calls/launches/d2af9e9a5103446bbaf3c1942c74b3e4/outputs/review.md
raw-output-sha256: d5f30337386664bb7f74fb4634d98a4caece2dbe99e9407c070b5b2f79579c68
format: 2
---

# Critique: Evaluation required for adoption is part of the operating process

**Note:** kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
**Central commitment:** Human evaluation that a system must wait for before adopting a change is an operating dependency; assessment that only measures an already-adopted change need not be, and this distinction locates the human stops that automation must address.
**Critique mode:** claim (with a definitional core: "operating dependency" vs. "assessment of results")
**Attack outcome:** partially lands

## Strongest case against it

The objection comes from control theory and from the cybernetic view of sociotechnical systems, such as Ashby or Beer's viable-system model. In that view, blocking is a timing property, not a dependency property. A controller in an outer loop is as much a part of the control system as a gate in the inner loop. It acts with more latency and over more cycles. Suppose a maintainer reviews adopted instructions a week later and then either rolls back bad ones or tightens the acceptance rules the agent applies. The system's long-run behaviour is regulated by that human, even though no individual adoption waited for them. Remove the human and the system still "proceeds". But the same is true if you remove the pre-adoption gate and let the agent self-approve. Unless the classification asks whether the system would drift into bad states, "the process can proceed without a person" tells you nothing about either case.

So, the opponent argues, the only non-trivial test of "the process depends on this human activity" is counterfactual and quality-laden: would the system still operate acceptably if the activity were removed? That test treats pre- and post-adoption review alike, so the waiting-based distinction does no work. It also contradicts the note's own scope claim that dependency is separate from whether the check is adequate or the change is good. The operator who uses the note to find "human stops that automation must address" would then aim at the visible blocking gates and miss the outer-loop dependencies. Those are the ones that silently erode when "nobody waits for them".

## How the note engages it

Partially engaged. The note anticipates the monitoring half of the objection in "Name the process being automated". It says that automating adoption while relying on human monitoring and rollback "has not eliminated that dependency", and that "Optional observation is different from monitoring on which the process relies." That concedes the opponent's central point: blocking is not the general criterion. It answers the rollback case correctly.

It does not engage three further points:

- **What "relies" means.** The note never states the test that separates optional observation from relied-upon monitoring. The only test available is the quality counterfactual. Yet the Scope section says adequacy and improvement "remain separate questions". The note asserts the separation without showing that the classification can be made without judging adequacy.
- **Feedback into adoption rules.** The "Non-blocking assessment" case is presented as clearly outside the operating process. If that week-later verdict feeds revisions to the instruction or to the acceptance rules, the next adoption depends on it. The Scope bullet on "anticipated assessment" covers influence on proposals, not human revision of the rules themselves.
- **The title's force.** The opponent concedes the title's direction, that required pre-adoption evaluation is part of the operating process. The attack lands on the converse: "need not be" and the claim that the distinction identifies "the human stops that automation must address". "Stop" is the waiting-based reading, and the note's own monitoring paragraph shows it is incomplete.

The blocking case survives the attack: an adoption that must wait for a human is plainly an operating dependency. The attack lands against the claim that the blocking/non-blocking contrast is the distinction automation should track.

## Constructive findings

- State the general criterion explicitly as counterfactual reliance: the process would not run acceptably without the activity. Present waiting as its most visible case rather than its definition.
- Reconcile that criterion with the Scope claim that adequacy is a separate question. For example, say that classifying a non-blocking activity as a dependency requires a judgment about what happens without it, while classifying a blocking stop does not.
- Classify the outer-loop case: later assessment that revises the agent's instructions or acceptance rules. Then the "Non-blocking assessment" example either stays clean, with that assumption stated, or is marked as a dependency over a longer timescale.
- Align the file name with the title and body. The current name asserts a causal-credit claim that the body explicitly sets aside.

## Secondary objections (optional)

- The description says the distinction "identifies human stops that automation must address". But the note's own monitoring paragraph identifies dependencies that are not stops. "Stops" understates what the operator is told to look for.
- The two cases are hypothetical and constructed to be clean. One mixed case, where assessment both feeds rollback and is sometimes skipped, would test whether the reader can apply the distinction where it is hard. The note says such episodes exist ("An episode can contain both required approval and later assessment") but does not work one through.
