# Assessment: A citation cannot assert more fidelity than its capture preserved

**Proposed purpose (the operator named none):** Agents and maintainers who cite sources in a Commonplace KB, and the notes that cite this one as the capture bound, should learn early and precisely what a passing quote check certifies. It certifies that the span occurs, under a stated rule, in the evidence the check compared. They should also learn what stays unverified: attribution upstream of that evidence, contextual support and truth.

**Outcome: stop.** The highest-value change settles which claim the note makes and what its title says. That change replaces the opening and the section framing, and it changes the title claim that five dependents rely on. Passes run on that text would be redone, so none is planned.

## What reads well

The four-question decomposition and the occurrence-versus-location paragraph are precise and separable, and each names the mechanism that settles its question.

## Sentence a hostile reviewer would attack first

The H1: "A citation cannot assert more fidelity than its capture preserved." Its opening paragraph says the opposite in the descriptive sense: "Unchecked, that assertion rests on the author's word". A citation can assert anything; a *check* is what is bounded.

## Ranked changes (highest value against the purpose first)

1. **Settle the note's contribution and title, then lead with the limit.** Cost: a rewrite of the title, opening and section framing, plus coordinated edits in dependents. Pass: none; this needs the rewrite route. This is the stop below.
2. **Decide general rule versus Commonplace instance** for "no mechanism here", the "unresolved" outcome and "the extractor". Decide too whether signed or content-addressed sources fall outside the attribution limit (findings 6, 7; critique; premise decomposition). Cost: three or four sentences and the description. Pass: `fix-strategy-taxonomy` after the decision, or inside the rewrite.
3. **Resolve the two underspecified assertions** in "Which evidence a pass is relative to": "current bytes" of what, and "unreadable" versus "missing" (finding 8). Cost: one sentence each. These are claim questions first. After the decision, `fix-strategy-taxonomy` applies them.
4. **Fold the duplicated no-fallback rule and the duplicated change-detection sentences** (finding 5; synthesis 3). Cost: one pass over one section. Pass: `readability-and-flow`, which runs after items 2–3, because those passages hold open claim questions.
5. **Reduce the multi-read paragraph and the extract recommendation to their bounding points** (synthesis 2). This is a choice. Cost: two paragraphs. Pass: `readability-and-flow`, or the rewrite.
6. **Gloss "pin" and identify ADR 046 as this KB's architecture decision record** (findings 1, 2). Cost: two clauses. Pass: `fix-strategy-taxonomy`.
7. **Align the title with the body's scope** (finding 3). This is subsumed by item 1. Pass: `opening-and-title` cannot do it alone, because the title is a claim dependents rely on.

## Stop: kind and grounds

**Defect** (reports: `kb/reports/state/review/results/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md/kb/instructions/critique-note.md`, `kb/reports/state/review/results/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md/kb/instructions/composition-friction-gate.md`; finding `kb/reports/state/review/results/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md/frontmatter/title-body-alignment.md`). The note's wording supports two readings, and they lead to different conclusions:

- *Verification reading:* a check can establish fidelity only relative to the evidence it compared. The body argues this ("A pass means 'agrees with the evidence this check used'"). Read this way, the title is false as worded, because the opening says a citation's assertion "rests on the author's word" and can exceed any capture. The compared evidence may also be an extract or nothing, so it is not always a capture.
- *Normative reading:* a citing text may not legitimately claim more fidelity, strength or scope than its capture preserved. The dependents use this reading. The ROME ingest applies the title to claim strength and scope. The claims-and-grounding tag head glosses it as "stronger notation cannot restore lost fidelity". The atomic-step note uses it as a capture-time bound on which passages can be quoted. The body never develops this reading.

Correcting the defect means either retitling toward verification, which changes the claim the dependents cite, or developing the normative bound in the body, which gives the note a different thesis and structure. Either way the opening and framing are replaced. The synthesis reaches the same point as a choice: keep the title's single claim and reorder, or retitle toward the description's survey (`kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/synthesis`).

**Dependents affected** (role report: `kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/role`):
- `kb/reference/adr/046-verbatim-quotes-are-validated-against-their-cited-source.md`
- `kb/theory/a-note-is-an-atomic-step-relative-to-the-check-that-reads-it.md` (argues from the title as a premise)
- `kb/sources/rome-locating-and-editing-factual-associations-in-gpt.ingest.md`
- `kb/sources/peters-chin-yee-llm-generalization-bias.ingest.md`
- `kb/tags/claims-and-grounding-README.md`

**Route:** `commonplace-review run rewrite kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md --commission FILE`, with the commission prepared with `cp-skill-write-multistage`. The commission should fix which reading the note asserts. It should also say whether the dependents' normative use moves to this note's body or to another note.

## Candidate overclaims: support or divergence

- "A pass means 'agrees with the evidence this check used'." **Divergence.** Keep it; it is the core claim. It may be completed with the normalization rule (premise decomposition).
- "A string check answers only the wording question." **Divergence.**
- "Markers that never claimed exact wording, such as a paraphrase marker, give the check nothing to match." **Divergence;** ADR 046 relies on it.
- "Missing bytes therefore report as unverified, never as passed." **Divergence;** the atomic-step note relies on it.
- "The binding stops at the capture: no mechanism here checks that the capture faithfully represents the original or that the named author wrote it." **Support.** It may be narrowed to unsigned captures or attributed to the cited mechanisms.
- "For an exact-wording claim, an inexpensive occurrence check can justify treating mismatch as failure rather than warning." **Support.** It may be reconditioned on a calibrated normalization rule.
- "Judging support is costlier and noisier, so it cannot simply block the way a wording check does." **Support.**
- "Each exact check in a chain, such as capture to extract and extract to note, verifies only its own pair." **Support.** It may say when exact hops compose.
- "Checking against verified source extracts avoids judging a paraphrase of a paraphrase." **Support.**

## Stale qualifications

- The description promises "attribution upstream" stays unverified in general. The body hedges this to "no mechanism here". The description has drifted past the body's hedge.
- The last Scope bullet uses one implementation's vocabulary ("unresolved", "the extractor") under a general description.

## Claim questions for the operator

- **Title and contribution.** This is the stop above. Candidates: retitle toward verification (e.g. "A quote check verifies fidelity only to the evidence it compared"), or keep the title and develop the normative bound. A proposed change of title and file name is included here.
- **General rule versus instance** (findings 6, 7). Does "no mechanism here" mean this account or Commonplace's validator? Do signed or content-addressed sources fall outside the limit (critique; premise decomposition)? No defect in the body is shown, because "here" hedges it. The description overreaches.
- **"Current bytes" of what** (finding 8). Context favours the capture file's bytes compared with the pin. But "catches a changed or removed passage" reads like source drift. This is a defect a sentence would correct once the operator states the mechanism.
- **"Unreadable" versus "missing"** (finding 8). An absent capture is a failure under one sentence and unverified under the other. Case: a capture held on another machine. This is a defect one sentence would correct.
- **What a pass is relative to.** The opening includes the rule; the evidence section names only the evidence (premise decomposition). A retained pass can flip when the rule tightens. One clause would correct it.
- **Ground for failure semantics.** Cost versus calibration against false mismatches (friction). The note's own normalization paragraph supplies the missing condition. One sentence would correct it.
- **Exact-chain composition** (premise decomposition). Occurrence is transitive for contiguous extracts under one rule. I cannot tell whether this is a defect or an extension, so I treat it as a choice: no defect is shown.
- **Multi-read and extract-recommendation branches** (synthesis 2). This is a choice with no defect shown: cut or rehome the procedural material.

## Findings and proposals not acted on

All findings are deferred by the stop, because each passage they name is in text the rewrite will replace or in a passage with an open claim question.

- `accessibility/undefined-terms` (pin, reliance risk, extractor, locator): cheap glosses. Apply them in the rewrite or later with `fix-strategy-taxonomy`.
- `accessibility/unidentified-references` (ADR 046 unidentified; ADR 073/094 unlinked; casebook corpus): same as above.
- `frontmatter/title-body-alignment`: subsumed by the stop.
- `compression-bundle/core-claim-obscured`: subsumed by the stop. Leading with the limit depends on which claim is kept.
- `compression-bundle/marginal-value-redundancy`: both folds touch passages with open claim questions (finding 8).
- `prose/source-residue` and `semantic/conceptual-role-conflation`: these need the author's general-versus-instance decision, so they are claim questions.
- `semantic/underspecified-assertions`: these are claim questions (above).
- Extension, not recommended: cite the Peters & Chin-Yee ingest as evidence on paraphrase scope bias (role report, untaken). The purpose does not ask for that coverage.
- Extension, not recommended: name signatures, content addressing and independent captures as mechanisms past the capture (critique). This should be decided with the general-versus-instance claim question.
- Extension, not recommended: qualify the extract recommendation with selection loss (critique), "binary given a fixed rule" (critique, secondary), and whether the casebook edits were substantive (friction). These are small qualifications for the rewrite to weigh.
