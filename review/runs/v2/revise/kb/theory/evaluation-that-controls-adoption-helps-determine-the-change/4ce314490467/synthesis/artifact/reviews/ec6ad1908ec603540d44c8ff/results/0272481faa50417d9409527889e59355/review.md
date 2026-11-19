---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Whether a specified task is useful or necessary is a separate question.
  - not by itself evidence that the system would fail or degrade without the task
  - This example establishes a gap against the specification, not that skipping review
    causes harm.
  - It is an actual wait to remove, not evidence that the evaluation is needed to
    meet a stated requirement.
  reason: 'The note disclaims necessity four times: in the opening, the definitions
    paragraph, the weekly-review example and the habitual-wait Scope bullet. After
    the opening, the repeats make the note read as defending against an objection
    instead of drawing its distinction, and the reader cannot tell whether each repeat
    adds a boundary. A revision could state the necessity disclaimer once, as a scope
    boundary in the opening or in Scope, and end the other passages at their positive
    point (for example, end the definitions sentence at ''an unfulfilled requirement'').'
- scope: passage
  quotes:
  - This distinguishes human work within the process from optional assessment of its
    results, rather than deciding who deserves causal credit for an improvement.
  reason: The positioning paragraph sits between the definitions and the cases, and
    it rules out a causal-credit reading that nothing earlier in the note invites.
    This delays the cases that apply the definitions. A revision could move the link
    to the before/after comparison note to the end of the note, or cut it to a one-line
    pointer there, and drop the causal-credit clause unless readers from the linked
    note are likely to bring that question.
outcome: report
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
target-sha256: 4ce314490467b56a65602d322f71dc9333598a43919d4e4549ca983cbf4f4a27
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/synthesis/artifact/reviews/ec6ad1908ec603540d44c8ff/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/synthesis/artifact/reviews/ec6ad1908ec603540d44c8ff/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/synthesis
launch: 0272481faa50417d9409527889e59355
completed-at: '2026-11-17T13:10:25Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/4ce314490467/synthesis/calls/launches/0272481faa50417d9409527889e59355/outputs/review.md
raw-output-sha256: 85ea635e924fda6cd942a241c11516c74d673138029d9493aa20f551c967a12f
format: 2
---

# Simplification synthesis: Removing approval waits can leave required human evaluation in place

The four checks found the note compact and its claim prominent. Branch-bloat found no competing branch, and detail-overhang reported only a one-sentence overhang in the subsequent-revision paragraph. That overhang is local compression, so this synthesis leaves it out. Two opportunities combine several findings into one structural change each.

## Opportunities

### 1. State the necessity disclaimer once

- Location: opening paragraph ("Whether a specified task is useful or necessary is a separate question."); second paragraph ("not by itself evidence that the system would fail or degrade without the task"); "Name the process being automated", first paragraph ("This example establishes a gap against the specification, not that skipping review causes harm."); Scope, second bullet ("not evidence that the evaluation is needed to meet a stated requirement").
- Combines: marginal-value-redundancy (warn: defensive redundancy); the habitual-wait echo the same review notes in its body.
- Preserve or decide: Keep one explicit statement that an undone specified task is a gap against the specification, not evidence of harm or necessity. This separation is part of the claim, so it cannot simply be deleted. The author must decide where it lives: in the opening, as a definitional consequence, or in Scope, as a boundary. Check that the weekly-review example still reads as a specification gap and not as a harm claim when its caveat is removed. The habitual-wait bullet also says such a wait is "an actual wait to remove". Keep that point even if its necessity clause goes.

### 2. Let the definitions lead straight into the cases

- Location: third paragraph of the introduction ("This distinguishes human work within the process … a judgment that the system improved does not by itself show whether human evaluation was required to operate it.").
- Combines: core-claim-obscured (info: positioning apparatus before the examples); marginal-value-redundancy (info: causal-credit clause does no visible work).
- Preserve or decide: Keep the link to [the comparison of operative states](./a-better-factory-claim-compares-operative-states.md) and the contrast it carries: a judgment that the system improved does not show whether human evaluation was required. The author must decide whether readers of that note are likely to treat evaluation as a claim to causal credit. If so, the clause should stay, perhaps at the end of the note. If not, it can go. Moving the paragraph changes only placement and should not weaken the complement relation to a bare see-also.
