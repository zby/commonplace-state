---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["For an exact-wording claim, an inexpensive occurrence check can justify treating mismatch as failure rather than warning."]
    reason: "UNSUPPORTED — the stated ground is cost (\"inexpensive\"), but whether a mismatch can block depends on the false-mismatch rate, not on cost. The next section concedes this: under-normalization fails correct quotes, and ADR 046 judges such false mismatches worse than no check. Cheapness only lets the check run often. Failure semantics also need a normalization rule calibrated so that a mismatch reliably means a wrong quote, and this joint does not name that condition."
  - scope: document
    quotes: []
    reason: "THIN — the title claims that a citation \"cannot assert\" more fidelity than its capture preserved. The body argues a different thing: a check's pass is relative to the evidence it compared (\"A pass means 'agrees with the evidence this check used'\"). A citation can still assert fidelity to the original. What is limited is what a check can verify. The body also says the compared evidence may be an intermediary's extract or nothing, not only a capture. So the move from the body's verification limit to the title's assertion limit is never made, and the title's \"capture\" is narrower than the body's evidence set."
  - scope: passage
    quotes: ["In one casebook corpus the real mismatches were mostly editorial omissions, bracketed substitutions and case changes (ADR 046), which a permissive enough rule would ignore."]
    reason: "THIN — this is offered as evidence for \"Too much would let substantive edits pass.\" But the cited mismatches are editorial omissions, bracketed substitutions and case changes, which are often not substantive. The sentence does not show that the edits a permissive rule would hide changed meaning. It shows only that they changed wording, so the support for the over-normalization risk is weaker than the paragraph implies."
  - scope: passage
    quotes: ["A capture kept on another machine is not evidence for a check on this one, and neither is text that happens to sit in a model's context."]
    reason: "THIN — the note asserts that text in a model's context is not evidence, but does not say why. The implied reason is that such text is not bound to a recorded capture by checksum and name pairing (the previous paragraph's identity binding), so the check cannot say what it compared against. The note leaves that link unstated, and the following \"therefore\" (missing bytes report as unverified) rests on it."
  - scope: passage
    quotes: ["Judging support is costlier and noisier, so it cannot simply block the way a wording check does"]
    reason: "THIN — noisiness plausibly makes blocking on a support judgment risky, because false blocks would be frequent. Cost alone does not prevent blocking. The \"cannot\" states a design choice as an impossibility, and no measure of how noisy the judgment is backs it; the note itself says its reliability is unmeasured."
outcome: report
---

# Friction check: A citation cannot assert more fidelity than its capture preserved

**Central claim (one sentence):** A quote check verifies only that a span occurs, under a stated normalization rule, in the specific evidence it compared, so a pass says nothing about attribution upstream of that evidence, contextual support or truth.

## Filter
**Filter:** SURVIVES

The claim commits to one consistent thing. A pass is relative to identified evidence, and the note keeps wording, attribution, context and truth separate without needing them to hold at once. The trade-off it handles, too little against too much normalization, is stated as a trade-off rather than wished away. The one strain is between the title and the body: the title speaks of what a citation can *assert* and limits it to a *capture*, while the body concerns what a check can *verify* against any evidence. That gap does not make the claim incompatible with itself, but it is the first joint listed below.

## Thinnest joints

The failure-semantics joint ranks thinnest because the note's own later paragraph says what it leaves out. Cost is given as the reason a mismatch can be a failure, while the normalization section shows that the reason is actually calibration against false mismatches. The title-to-body mismatch comes next. It is a document-level joint because no single sentence derives the title. The casebook evidence and the model-context exclusion are both locally plausible, but the reader has to supply the step each one relies on: that the hidden edits are substantive, and that unbound text cannot be identified. The support-blocking joint is the strongest of these five. It holds if "noisier" carries the argument, but it is phrased as an impossibility. The remaining joints hold under the skeptical default and are not listed: uniqueness removing ambiguity, forbidding concatenation, the limits of the identity binding, missing bytes reporting as unverified, excerpts losing context, and exact checks verifying only their own pair.

## For the human
Look first at the second paragraph under "Four questions, one answered mechanically": should cheapness or a calibrated normalization rule justify treating mismatch as failure? Then decide whether the title should say "verify" rather than "assert", and "evidence" rather than "capture".
