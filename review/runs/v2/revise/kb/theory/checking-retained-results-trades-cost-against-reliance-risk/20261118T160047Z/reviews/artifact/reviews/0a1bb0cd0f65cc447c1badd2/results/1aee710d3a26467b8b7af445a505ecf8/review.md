---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - How often to check a retained result therefore depends on the cost of checking
    relative to the risk of relying on stale or wrong content.
  reason: The framing makes check frequency the decision variable. The incremental-computation
    objection is that check timing relative to source changes governs reliance risk.
    A check that fires on every relevant change leaves no unchecked window, whatever
    its frequency. Checks on a clock or on reads reduce risk only by chance alignment
    with changes. The note should name the trigger (on write, on read, on validation)
    as a separate axis and say that frequency is a proxy for it only when changes
    cannot reach the checker.
- scope: passage
  quotes:
  - 'Enforcement is reactive: the validator flags a gap when the head is next validated,
    so a mark can be false in between.'
  reason: The note presents the window between validations as an accepted cost of
    the trade-off. The mark's own conditions argue against that. The rule is defined,
    its inputs are named and the check is cheap, so a check triggered by writes to
    tagged artifacts in the participating collections could close the window. In its
    strongest example, then, the between-check risk follows from where the validator
    is invoked, not from the cost/risk balance. The note should say whether the gap
    is a deliberate trade, and what it saves, or a contingent invocation choice.
- scope: passage
  quotes:
  - The design difficulty is tracking a sufficient dependency set, including newly
    added relevant material.
  reason: 'This sentence concedes the attack''s central point, but only for the connect
    report. The note does not carry it back to the general claim. A reader therefore
    keeps the frequency framing even though the note''s own analysis puts the difficulty
    in dependency tracking. Promote it to the thesis: the cost/risk trade-off applies
    when the dependency set cannot be tracked soundly. Where it can be tracked, change-triggered
    checking turns the trade-off into a question of check cost per change.'
- scope: document
  quotes: []
  reason: 'Secondary: the qualitative claim ''depends on cost relative to risk'' fits
    almost any decision about checking. The note''s specific contribution is the distinction
    between results that authorize stopping (the mark) and results offered only as
    candidates (the connect report). The title and opening do not state it, so the
    most informative distinction appears only in the worked examples.'
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
criterion: kb/instructions/critique-note.md
note-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: 0d0cf44cba15ace932e01cefaf52f09ede4b4729916d13af8b19014f735708eb
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/0a1bb0cd0f65cc447c1badd2/inputs/target/kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/artifact/reviews/0a1bb0cd0f65cc447c1badd2/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews
launch: 1aee710d3a26467b8b7af445a505ecf8
completed-at: '2026-11-18T16:04:05Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/checking-retained-results-trades-cost-against-reliance-risk/20261118T160047Z/reviews/calls/launches/1aee710d3a26467b8b7af445a505ecf8/outputs/review.md
raw-output-sha256: 4f4d06cec00139c19a04a4d5df9ecfa6d72c5ee061b64add4027091430a82666
format: 2
---

# Critique: Checking retained results trades cost against reliance risk

**Note:** kb/theory/checking-retained-results-trades-cost-against-reliance-risk.md
**Central commitment:** How often to check a retained derived result should be set by the cost of checking relative to the risk of relying on stale or wrong content. Accepting risk between checks can be right when the choice is explicit.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The strongest opponent is the incremental-computation and build-system position, as held in Make and Bazel-style dependency tracking, in query systems such as Salsa and Adapton, and in cache-invalidation practice generally. On that view, "how often should I check?" is the wrong question. Reliance risk does not depend on how many checks run per unit time or per read. It depends on whether a check runs after each relevant source change and before the next reliance. A system that tracks the copy's dependencies and re-checks when one changes has no unchecked window, and its check cost scales with changes, not uses. A system that checks on a schedule or on some reads still has a window after every unobserved change. Raising its frequency narrows that window only statistically. Frequency is therefore a fallback proxy, needed only when changes cannot be propagated to the checker. Treating it as the main variable misdescribes the decision.

The note's own flagship example shows this most clearly. The completeness mark has every property that makes change-triggered checking available. The rule is defined (one-hop reach), the inputs are named (tagged artifacts in the participating collections), and the check is described as inexpensive. Yet the note presents "a mark can be false in between" validations as part of the accepted trade. An incremental-computation advocate would answer that a check this cheap, with a dependency set this well defined, should run whenever a dependency is written. On that view, the between-check falsity is an invocation gap, not a priced risk. If that is right, the note's main example does not show its thesis. It shows a case where the cost/risk trade-off was unnecessary.

For the connect report, the opponent concedes a real trade-off, but for a different reason than the note states. Its dependency set is unbounded, because any new KB material may change the result, so change-triggered invalidation cannot be made sound. Only in that case does a policy on check frequency or reuse become the right instrument.

## How the note engages it

**Partially engaged.** The note supplies the attack's components but does not let them reshape its thesis.

- "No known change does not establish freshness" states that absence of a known change counts as evidence only "if every relevant change reaches the checker." That is the change-propagation condition, but the note uses it only as a warning against assuming freshness. It does not identify it as the condition under which the frequency trade-off disappears.
- In the connect report section, the note says "The design difficulty is tracking a sufficient dependency set, including newly added relevant material." That names the attack's central variable, but only for the connect report.
- "What a mechanical check requires" lists the conditions that make a check possible, namely a rule, a locatable copy and source, an available source and a trustworthy checker. It does not list a trigger or change-propagation condition, so it cannot distinguish change-triggered from periodic checking.
- The mark section treats reactive enforcement as a given ("Enforcement is reactive") and does not ask whether the window is chosen or merely inherited from where validation runs.

The attack does not fully land, for two reasons. The claim remains true where dependency sets cannot be tracked soundly, as in the connect report, and even change-triggered checking has a per-change cost that a qualitative trade-off can absorb. It partially lands because the title and the frequency framing make the trade-off the general rule. In the note's strongest example, a defined dependency set makes change-triggered checking available, and the trade-off is then optional rather than necessary.

## Constructive findings

- Add the trigger as an axis separate from frequency. A check can be change-triggered (on writes to dependencies), use-triggered (before reliance) or periodic (at validation time). State that only a change-triggered or use-triggered check closes the reliance window, and that frequency is the fallback when changes cannot reach the checker.
- Restate the thesis conditionally. The cost/risk trade-off over check frequency applies when the dependency set cannot be tracked soundly, as with the connect report. When it can, as with the mark, the choice is whether per-change check cost is worth paying, which is usually an easy decision for a cheap, defined check.
- In the mark section, say whether the window between validations is a deliberate trade, and if so what it saves, or a contingent consequence of where the validator runs. As written, the reader cannot tell.
- Generalize the connect report's sentence about tracking a sufficient dependency set into the general framing. It currently explains why the two examples differ, but only locally.
- Consider adding a fifth condition to "What a mechanical check requires" or the surrounding prose: something that brings each relevant change to the checker. Without it, the four conditions make a check possible but do not determine when it runs.

## Secondary objections (optional)

- The headline claim that check frequency "depends on the cost of checking relative to the risk" is close to true of any checking decision, and the Scope section confirms it is uncalibrated. The note's specific contribution is the contrast between a result that authorizes stopping (a false mark tells exhaustive consumers to stop) and a result offered only as candidates (the connect report's contract withholds that permission). The title and opening paragraphs do not state that contrast, so the most informative distinction appears only in the worked examples.
- The first paragraph says verification can be cheaper than derivation, which allows checking on every use. That undercuts the trade-off in exactly the cases the mark represents, and the note does not return to it when discussing the mark.
