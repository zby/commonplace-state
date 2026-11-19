---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "When non-regression protects the revision path"
      - "Preserving the path is therefore a consequence of non-regression only under an additional condition"
    reason: "The note presents scope inclusion as the condition under which non-regression protects or preserves the revision path. In the parent framework, non-regression is part of a comparison that judges the adopted states, and the parent's Scope separates that judgment from whether an evaluator controlled adoption. A successor that closes the path and fails a correctly scoped comparison has still been installed, and a system whose only revision path is gone cannot use the failed verdict to revert. Protection therefore also requires the check to gate installation. State that second condition, or rephrase protection as 'the successor fails the requirement'."
  - scope: passage
    quotes:
      - "If that scope includes the ability to revise the system's improvement machinery, a successor that destroys the only applicable revision path fails the requirement even if its production performance improves."
    reason: "The note does not say how revision capability can be checked before the successor is installed. The linked repeatable-path note accepts two kinds of evidence: a later episode, which arrives only after installation, and a specified transition mechanism, which supports the claim prospectively. Only prospective evidence, such as the mechanism argument or a trial revision run in staging, can make the check prevent closure rather than detect it. One sentence naming this pre-installation form would make the protection claim operational and would explain why ordinary production non-regression checks cannot cover it."
  - scope: document
    quotes: []
    reason: "Non-regression scoping is the only safeguard the note names. A common design keeps the revision machinery outside the edit surface the successor can change, which protects the path without any comparison check. The note's literal claim is restricted to non-regression and survives this point. Still, a brief contrast would stop readers from treating checked-scope inclusion as the only remedy. It would also tie the note to the parent's caveat that fixed placements need a stated reason."
outcome: report
attack-outcome: partially lands
---

# Critique: An improvement can close the path to further improvement

**Note:** kb/theory/an-improvement-can-close-the-path-to-further-improvement.md
**Central commitment:** A successor can improve a declared production dimension while disabling the machinery that would produce another revision, and non-regression prevents this only when revision capability is included in the checked scope.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

The opponent is an engineer who designs self-modifying agent loops, for example an archive-and-evaluate loop. In such a loop, a modified agent enters the archive only after a check confirms it can still edit code. The opponent accepts the first half of the note: a production gain and a lost revision path are compatible. That point is close to the general rule that a check covers only what it measures, and the note states it correctly. The objection targets the second half. The note says non-regression "protects" the revision path, and that preservation is "a consequence of non-regression", once revision capability is in the checked scope. The opponent says scope inclusion is necessary but not sufficient. Two further conditions do the protective work.

1. **The check must control adoption.** In the better-factory framework this note supplements, non-regression is part of a comparison that judges the *installed* successor. The parent note says this directly: "A comparison judges the adopted states. Whether an evaluator also controlled adoption is a separate causal question." A correctly scoped comparison that runs after installation reports that the successor fails, but by then the path is already closed. This loss differs from a production regression. A regressed production capability can be repaired by a later revision. A closed revision path removes the internal route that would make the repair. For the agent at the declared boundary, a failed verdict that arrives after installation cannot be acted on. This is the note's own hypothetical: the faster configuration has been installed and has removed the workflow.

2. **Revision capability must be checkable before installation.** Production non-regression can be checked by running the task set on the candidate. Revision capability has no equivalent check that is just as simple. The linked repeatable-path note accepts two kinds of evidence for continuity: a later episode, which comes after installation, and a specified transition mechanism that survives the transition. Only the second kind, or a trial revision run in staging, is available when the adoption decision is made. "Include it in the checked scope" therefore points to a check whose feasible form the note leaves unstated.

On this view, the note puts the protective mechanism in scope declaration. The work is actually done by a gate that runs before installation, using evidence that is available before installation. Getting scope right without that gate yields an accurate post-mortem, not protection.

## How the note engages it

Partially engaged. The body sentence about a successor that destroys the only applicable revision path is accurate: it says the successor "fails the requirement", not that it is prevented. The note also hands the detailed operational test to the repeatable-path note ("That note supplies the detailed test"). The separation between judging states and controlling adoption appears only in the parent note's Scope. This note's description ("non-regression prevents this"), section heading ("When non-regression protects the revision path") and conclusion ("a consequence of non-regression") each turn the necessary scope condition into protection without stating the adoption condition. The timing of the check is not discussed. The third section ("Remaining able to improve is not improving again") answers a different objection, about over-reading preservation, not the objection that preservation is under-delivered.

## Constructive findings

- State that scope inclusion makes a path-closing successor *fail* non-regression, and that this *prevents* closure only when the check gates installation. Otherwise the check records the loss after installation. One sentence in "When non-regression protects the revision path" would do it. The description's "prevents" should then match.
- Name the pre-installation form of the check: a trial revision carried through representation, determination, admission and installation in staging, or an argument from a specified transition mechanism. This also explains why non-regression on ordinary production tasks cannot cover revision capability: the task set never exercises the revision path.
- Optionally, add to Scope that the path closes for good at the declared boundary when the successor removes the only revision path. This is the asymmetry with ordinary regressions that makes adoption-time checking matter more here.

## Secondary objections (optional)

- The note names no safeguard other than non-regression. Keeping the revision machinery outside the edit surface the successor can change protects the path without any check. The note's literal claim is limited to non-regression, so this does not refute it. A contrast would still stop readers from treating scope inclusion as the only remedy.
- The opening argument ("Checking the current gain does not check that the revision mechanism survives") is close to the general rule that a check covers only what it measures. The note's specific contribution is the claim that production task sets do not exercise the revision path. That claim is implied, not stated, and stating it would make the note's reach clearer.
