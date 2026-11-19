---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: The title's limit (a pass certifies agreement only with the evidence the
    check used, and the capture-to-original link stays unchecked) is stated plainly
    only in the third section, so the four-question list and the normalization and
    occurrence material read as a coequal survey rather than as support for one claim;
    a revision could state the limit in the opening paragraph and frame the later
    sections as the things a pass is relative to (its normalization rule, its occurrence
    constraint, its evidence), after the author settles whether the note is the title's
    single claim or the description's general survey.
- scope: passage
  quotes:
  - A model may need several reads to check a source that exceeds its context budget.
  - Checking against verified source extracts avoids judging a paraphrase of a paraphrase.
  reason: Two passages drift from what a wording pass establishes into how to check
    context support and paraphrase, and the multi-read paragraph sits under the evidence
    section although it concerns the context question; a revision could keep only
    their bounding points (an exact excerpt can omit context needed to judge use;
    each exact check verifies only its own pair), attach them where the note already
    assigns context to a reader, and remove or rehome the checker procedure and the
    extract recommendation.
- scope: document
  quotes: []
  reason: The section 'Which evidence a pass is relative to', which carries the title's
    claim, states the no-fallback rule twice and says twice when change is detected,
    so its sequence of limits (binding, refusal to substitute, stop at the capture,
    drift) is harder to follow than its content; a revision could fold these into
    one pass through that sequence, stating each limit once.
outcome: report
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
contract: report
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/synthesis/artifact/reviews/59874c178c7a2f24ec5b99d5/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/synthesis/artifact/reviews/59874c178c7a2f24ec5b99d5/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/synthesis
launch: 543fde6b8c3148eabee2a0b4430b1cd8
completed-at: '2026-11-18T16:06:19Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/synthesis/calls/launches/543fde6b8c3148eabee2a0b4430b1cd8/outputs/review.md
raw-output-sha256: d947b775f2e74caa3cbfc01bc1f6cd16dc0e6bdbe480aa5fc3387f0aa81a113b
format: 2
---

# Simplification synthesis: A citation cannot assert more fidelity than its capture preserved

## Opportunities

### 1. Lead with the limit and organize the sections around it

- Location: opening paragraph ("A quote check makes it falsifiable by testing one relation") through the first sentences of "Which evidence a pass is relative to" ("A pass means \"agrees with the evidence this check used\"", "The binding stops at the capture").
- Reader problem: a reader who stops after the opening learns what the check tests but not the limit the title promises. The four questions and the material on normalization and occurrence come before that limit. With equal weight, they read as a general survey of quote checking, which matches the description's framing rather than the title's.
- Direction: state in the opening that a pass certifies agreement only with the compared evidence and that nothing checks the capture against the original. Then let each section show one way a pass says less than it seems to. One possible resolution, not settled: a pass is relative to its normalization rule, its occurrence constraint and its evidence. The note implies that three-way framing but never states it. The core-claim check proposed it as a possible revision target.
- Combines: core-claim-obscured (both findings).
- Preserve or decide: the title and the description choose different contributions. The title makes one claim about where fidelity stops; the description promises a survey of what each check establishes and what stays unverified. The body supports either reading. The author must choose. Retitling toward the survey keeps the current order. Keeping the title's claim requires the reordering above. If the three-way framing is adopted, keep the four-question taxonomy's distinct job: naming what stays unverified (context, truth, upstream attribution). It is not a fourth dimension of relativity.

### 2. Reduce the context and paraphrase branches to their bounding points

- Location: under "Which evidence a pass is relative to", the multi-read paragraph ("A model may need several reads…") and the closing sentences of the provenance paragraph ("Semantic hops compound instead…" through "…a paraphrase of a paraphrase.").
- Reader problem: both passages move from what a wording pass establishes to how a support-judging or paraphrase checker should work. The multi-read paragraph also sits in the evidence section, although the note gave the context question to a reader in its first section. The reader meets procedure inside an argument about limits.
- Direction: keep the sentences that bound the main claim. An exact excerpt can omit the context needed to judge use, so a wording pass does not establish support. Each exact check in a chain verifies only its own pair. Place the context point near the four-questions discussion. Cut the procedural rule (retrieve context and keep the full source outside the model's context) and the extract recommendation, or move them elsewhere. The contrast with semantic hops may stay as one clause if it sharpens why exact hops do not compound.
- Combines: branch-bloat (both findings) and detail-overhang (the multi-read paragraph).
- Preserve or decide: whether the note should give any guidance for a checker's procedure. If it should, the author must find a home for the retrieval rule and the extract recommendation; the checks found none. If they are cut, check that no reader of this note relies on the extract recommendation. Moving the context point must not merge it with the wording check: the note's claim that context needs a reader of both texts must stay intact.

### 3. Present the evidence section's limits once, in order

- Location: section "Which evidence a pass is relative to", from the source-identity paragraph through the "Retained, accessible and used material differ" paragraph.
- Reader problem: the section that carries the title's claim repeats itself twice. One repeat covers the no-fallback rule: "not an invitation to find another copy" and the later "silent fallback… (ADR 073)". The other covers when change is detected: the pin sentence and the sentence on checking current bytes. The section's sequence of separate limits is therefore harder to follow than its content warrants.
- Direction: go through the limits once, in order. First, binding to a recorded capture. Next, refusal to substitute another copy, stated once with its reason that ambient cache state would otherwise decide the result. Missing bytes report as unverified. The binding stops at the capture. Finally, a later check detects drift but misses changed surrounding context. The marginal-value check offered a folded pin sentence that illustrates one possible resolution.
- Combines: marginal-value-redundancy (the two warn findings).
- Preserve or decide: keep each distinct limit, as the detail-overhang check found that each sentence in the identity paragraph sets its own boundary. Specifically keep the blind spot for surviving quoted words in a changed context. Keep the rule that missing bytes are unverified, never passed. Keep the distinction between retained, accessible and used material. Keep the ADR 073 grounding attached to the no-fallback reason.
