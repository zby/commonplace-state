## Fix Report: llm-generation-relaxes-goals-where-human-writing-stalls

Source review run: 2298 (15 warns), then 2300 (3 residual warn gates after the 2298 fixes — see "Run 2300" section at end)

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | prose/pseudo-formalism | new-pattern: notation-removal | Replaced `costs the reader O(1)` with plain prose "gives the reader one localized joint to inspect"; preserved the cheap-vs-expensive contrast | fixed |
| 2 | accessibility/notation-opacity | new-pattern: notation-removal | Same `O(1)` edit as #1 (both gates flagged the one Big-O instance) | fixed |
| 3 | accessibility/undefined-terms | new-pattern: term-gloss | Glossed `semi-decidable` inline ("success is conclusive, failure is not") and bolded it on first use | fixed |
| 4 | accessibility/undefined-terms | new-pattern: term-link | Added definition link `[codification](./definitions/codification.md)` on first meaningful use | fixed |
| 5 | accessibility/undefined-terms (INFO) | new-pattern: term-gloss | Glossed `external oracle` as "an automatic verifier" on first use | fixed |
| 6 | accessibility/unidentified-references | new-pattern: reference-identification | Introduced "Fernando Borretti" on first mention | fixed |
| 7 | accessibility/unidentified-references (INFO) | new-pattern: reference-identification | Introduced "Josef Weizenbaum" on first mention | fixed |
| 8 | semantic/grounding-alignment | grounding: qualifier added | Softened the typicality claim from "the model does not drop a random conjunct; it keeps... sheds..." to a conditional "where the novel constraint is also the least probable... it is the one most likely to be shed" / "tends to sacrifice"; marks the added empirical premise the linked confidence note requires | fixed |
| 9 | semantic/internal-consistency | new-pattern: scope-precision | Changed "When a full witness exists, that most-plausible artifact is the witness" to "When generation lands on a full witness..." to stay consistent with the semi-decidability framing (existence ≠ reachability) | fixed |
| 10 | sentence/clause-packing | new-pattern: sentence-split | Split six over-packed sentences at the caveat boundary: the argmax sentence, the camouflage/discontinuity sentence, the typicality sentence, the relaxation-hidden-fault sentence, the falsifiable-prediction sentence, and the hallucination-analogy sentence | fixed |
| 11 | structural/compound-bullet | new-pattern: bullet-split | Split the first "Open questions" bullet into two: technical recoverability of the stall, and whether a reconstructed stall has the same epistemic force | fixed |

### Warning-to-fix mapping

- **#1–2 (pseudo-formalism / notation-opacity):** "`A human-flagged fault costs the reader O(1)` uses Big-O for an informal reader-effort comparison." → replaced with plain prose; the O(n)-style contrast is carried by "forces a search over an unknown... constraint set."
- **#3–5 (undefined-terms):** glossed `semi-decidable` and `external oracle` inline; linked `codification` to its definition.
- **#6–7 (unidentified-references):** full first names for Borretti and Weizenbaum so the body does not require a link-follow to identify the cited authors.
- **#8 (grounding-alignment):** the flat "keeps the typical / sheds the novel" claim outran the linked confidence note (which only asserts typicality/soundness decoupling); reworded as the conditional, expected tendency it actually is.
- **#9 (internal-consistency):** the witness sentence compressed "exists" and "is reached," conflicting with the earlier "failure does not prove non-existence."
- **#10 (clause-packing):** split the longest sentences; left dense-but-single-claim sentences intact (the surrounding `complexity/*` and `could-be-a-paragraph` gates passed, so the note's overall density is intentional, not a defect).
- **#11 (compound-bullet):** separated the two distinct questions per the reviewer's split suggestion.

### Deferred items

- **semantic/completeness-boundary-cases (INFO, gate result PASS):** the reviewer suggested a local qualifier that the human-stall contrast concerns the writing-to-think default, not every human process. Deferred: this boundary is the entire subject of the linked note [the machine searches for the camouflage a human writer usually slips into](../../notes/machine-searches-for-camouflage-human-writer-slips-into.md), which the core note already cites; a local restatement would duplicate it. Not a warn finding.

### New patterns

Several accessibility/sentence fixes here are not yet in the taxonomy and recurred enough within this single note to be worth proposing:

- **notation-removal:** an informal comparison is dressed in computational notation (Big-O) that defines no input size and derives nothing. Fix: state the comparison in plain prose.
- **term-gloss / term-link:** a computability or KB-vocabulary term (`semi-decidable`, `external oracle`, `codification`) appears before a local gloss or definition link. Fix: add a 3–6 word inline gloss and, for KB vocabulary, a definition link on first meaningful use.
- **reference-identification:** a cited author is introduced by surname only, requiring a link-follow to identify. Fix: give the full name on first mention.
- **sentence-split / bullet-split:** a sentence or bullet packs several separable claims/caveats. Fix: split at the caveat or enumeration boundary without changing the claims.
- **scope-precision:** a later sentence silently strengthens an earlier hedged claim (existence vs reachability). Fix: restate it in the earlier claim's weaker terms.

If these recur across other notes (3+ instances), promote them into `kb/instructions/fix-warnings/fix-strategy-taxonomy.md`.

---

## Run 2300 (re-review after the 2298 fixes)

Run 2300 re-reviewed the same note and confirmed the 2298 fixes held (O(1) no longer flagged). Three residual warn gates remained:

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 12 | prose/pseudo-formalism | new-pattern: notation-removal | Replaced the decorative `C-speed ∧ Lisp-dynamism ∧ all the unstated rest` with plain prose ("C-speed and Lisp-dynamism and all the unstated rest"); the "conjunct" vocabulary survives in prose | fixed |
| 13 | accessibility/unidentified-references | new-pattern: reference-identification | Attributed the C/Lisp example to "Fernando Borretti's example" at its first (opening) use, identifying him in-body as the source; demoted the later para to "Borretti's" | fixed |
| 14 | sentence/clause-packing | new-pattern: sentence-split | Split three more sentences: the typicality sentence (main claim vs. "usually holds" justification), the counterfeit-witness sentence, and the code-oracle sentence (verifier check vs. training effect) | fixed |

### Deferred items (run 2300)

- **pseudo-formalism — "argmax over plausibility":** kept. The term is the note's central handle for plausibility-maximization and is already explicitly framed as a reader's idealization, not the decoder's operation (the immediately following parenthetical). Removing it would weaken the MAX-SAT/optimization through-line; the over-signal is already disclaimed.
- **clause-packing — argmax sentence and first open-question bullet:** kept. Both were already split once in the 2298 pass; the residual density is the caveat structure itself, and further splitting would fragment the disclaimer rather than clarify it. The surrounding `complexity/*` and `could-be-a-paragraph` gates pass, so the note's overall density is intentional.
