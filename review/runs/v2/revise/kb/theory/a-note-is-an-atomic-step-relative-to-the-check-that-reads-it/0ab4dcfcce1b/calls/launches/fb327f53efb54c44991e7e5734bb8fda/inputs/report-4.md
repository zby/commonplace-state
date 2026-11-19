---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
note-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/synthesis
launch: 70a75d01895840689033388b916c149f
completed-at: '2026-11-16T22:41:54Z'
findings:
- scope: passage
  quotes:
  - Sizing a step to its checker rather than to the material is old.
  reason: The precedent section takes about as much space as the mechanism section
    and carries five verbatim quotations, but the note itself calls it analogy rather
    than evidence, and the Descartes half sizes parts 'to the solution', which sits
    closer to material-relative than checker-relative sizing; compress the section
    in place to the Lamport reader-relative test plus the analogy disclaimer and the
    closing validator point, reducing Descartes to a clause or removing it.
- scope: passage
  quotes:
  - The bounds are independent as constraints but coupled through this remedy
  reason: The coupling that qualifies the opening's 'nothing to do with each other'
    is buried mid-paragraph between an archived-proposal history and an unrelated
    links-are-not-sources point, and the second Open Question re-asks the cost this
    paragraph already states; split the paragraph so the coupling stands alone, move
    the links-are-not-sources sentence to where the source unit is defined, shrink
    the archived-proposal provenance, and narrow or cut the duplicate open question.
- scope: passage
  quotes:
  - The value is not that the reviewer copes
  reason: Auditability, the payoff the note values most, appears only near the end
    and is slowed there by a restatement of the occurrence-versus-representativeness
    limit, while the placement section argues from silent failure alone; preview auditability
    where the placement is argued and replace the repeated caveat with a back-reference,
    after the author settles what auditability is a reason for.
contract: report
target-sha256: 0ab4dcfcce1bc59c3edcadb859725e8fd19e65eb09c61c56332a86e56f0ddc8e
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/synthesis/artifact/reviews/d74db18b6934c70dca369f3f/inputs/target/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/synthesis/artifact/reviews/d74db18b6934c70dca369f3f/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it/0ab4dcfcce1b/synthesis/calls/launches/70a75d01895840689033388b916c149f/outputs/review.md
raw-output-sha256: 1d4ef7da9707c26b1f5f596c1179ae51b2745cd3f4a379c55753199fae8b7b61
---

# Simplification synthesis: A note is an atomic step relative to the check that reads it

The note's central claim is clear and well placed: a note is bounded twice, and the checking bound is relative to a named check. For the grounding check, its unit is the unquoted source. None of the four checks found a buried thesis. The three opportunities below each combine several local findings into one structural change. Two remaining findings stay local and are not included: the thesis sentence that runs into two inline links, and the first Scope bullet that repeats the opening's scope sentence. Each can be fixed with a wording edit.

## Opportunities

### 1. Compress the precedent section to the precedent that does the work

- Location: "What kind of number a step size is", from "Sizing a step to its checker rather than to the material is old." to "...into a check that costs the reviewer nothing."
- Reader problem: Two paragraphs and five quotations support a point the note explicitly calls analogy, not evidence. The Descartes half also undercuts the point it is cited for. In the note's own gloss, "The parts are sized to the solution", and that is a different axis from sizing by checker. The reader spends attention there while the argument stands still.
- Direction: Keep one compact paragraph that states that checker-relative sizing has precedent. Use Lamport's "depends on the sophistication of the reader" as the main quotation, keep the analogy disclaimer, and end on the validator point ("What the knowledge-base case adds..."). One possible resolution: reduce Descartes to a single lineage clause, or move it to a separate lineage note.
- Combines: branch-bloat (Descartes as the weakest-fitting branch); detail-overhang WARN (precedents out of proportion to their job).
- Preserve or decide: Decide whether Descartes' "long chains of simple and easy reasonings" is part of the note's contribution. Keep it if the note means that reliable chains rest on simple links, because that connects to "Title as claim enables traversal as reasoning". Drop it if it is only historical colour. Preserve the analogy disclaimer, which blocks the inference that a particular N carries over. Lamport's "possible, not inevitable" currently supports the sentence "a bounded check does not catch every error, but an unbounded one cannot be redone". If that quotation is cut, the sentence must stand on the auditability argument alone, or move there.

### 2. Make the coupling of the two bounds a visible qualification of the opening

- Location: "Mechanism" section, the joint-support paragraph ("A consequence worth stating..." through "...owes representation, not re-grounding"), with the opening sentence "for two reasons that have nothing to do with each other" and the second Open Question.
- Reader problem: The opening says the bounds are unrelated. The only place the note qualifies that is one sentence in a paragraph that also recounts an archived proposal and makes an unrelated point about links. The second Open Question then asks about this paragraph's cost as though the body had not stated it. A reader can leave believing the bounds are fully independent, or that the joint-support cost is unexamined.
- Direction: Split the paragraph. Keep the joint-support remedy and its coupling together. Move "Links to other notes are also not sources in this sense..." to the start of the mechanism section, where the counted unit is defined. Reduce the archived-proposal history to a short attribution. Narrow the second Open Question to what remains open, for example how often joint support exceeds a co-loadable note, or cut it. One possible resolution: let the opening sentence say "independent as constraints" so the later coupling reads as a promised qualification, not a reversal.
- Combines: core-claim-obscured (coupling buried in a three-point paragraph); detail-overhang (archived-proposal provenance); marginal-value-redundancy (the second Open Question repeats the body).
- Preserve or decide: Decide how strong the independence claim is meant to be. "Nothing to do with each other" (different mechanisms) and "coupled through this remedy" (quoting spends co-loading budget) are compatible only if independence is about what sets each bound, not about whether satisfying one affects the other. The revision must state that distinction, not erase either side. Preserve the by-claim split requirement and the snapshot fallback.

### 3. Give auditability its role in the placement argument

- Location: "Placing the bound on the artifact rather than the review" and "What kind of number a step size is", around "The value is not that the reviewer copes, but that the review becomes auditable".
- Reader problem: The note gives two reasons for small artifact-side steps in two distant sections. Early on, review-side budgets fail silently. Late, small steps make verdicts redoable. The second reason, which the note treats as the main value, arrives after the evidence section has shown reviewers coping, and is then slowed by a restatement of "Occurrence is not representativeness". A reader may keep the title claim but lose why it matters.
- Direction: Preview auditability in one sentence in the placement section. In the N section, replace the "lifted out of a qualifying context" caveat with a short pointer to the earlier limit. One possible resolution for the preview: "a bound on the artifact also keeps each verdict small enough to redo — the reason, developed below, that N is a convention rather than a capacity."
- Combines: core-claim-obscured (auditability appears late); marginal-value-redundancy and detail-overhang (repeated representativeness caveat).
- Preserve or decide: The author must decide what auditability argues for. As written, it justifies the kind of number N is (a convention for re-checkability). It is not explicitly a reason to prefer artifact-side over review-side placement, because the placement section says the two "differ in their failure mode, not in the constraint they express". If auditability is meant as a second placement argument, the note has to say why a review-side budget does not deliver it. If not, the preview should tie it to N only. Preserve the distinction that the audit covers the support judgment and not representativeness, at least as a pointer.
