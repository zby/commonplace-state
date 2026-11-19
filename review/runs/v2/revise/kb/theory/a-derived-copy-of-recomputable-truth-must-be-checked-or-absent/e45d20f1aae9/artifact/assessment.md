# Assessment: A derived copy of recomputable truth must be checked or absent

**Proposed purpose (the operator named none):** Agents and maintainers deciding whether to keep a derived copy, such as a mark, an inlined list or a duplicated file, should be able to tell from this note when the copy must be validator-checked, when it must be deleted or replaced by a live read, and why.

**Outcome: stop.** The depth 1 reports propose changing the note's central claim, not its text. Dependents rely on that claim and on the precondition numbering. No passes are planned.

## Why the run stops

1. **Proposal to narrow the claim (critique).** `kb/reports/state/review/results/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md/kb/instructions/critique-note.md` concludes the attack "partially lands". It proposes two changes. First, scope the rule to copies whose falsity cannot be detected at the point of use: completeness and other negative claims. Second, admit a third valid state, a copy that is present, unchecked and consumed as a hint, or argue explicitly why that state collapses into one of the two. It also proposes reconsidering the compiled-cue instance, which is the standard example of a hint. Each of these changes what the note claims, so no pass can make it.
2. **Same proposal from premise decomposition.** `kb/reports/state/review/results/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md/kb/instructions/premise-decomposition-gate.md` finds that the actual commitment is narrower than the title. On its reading, the rule covers trusted copies of mutable sources whose check is cheap and runs before consumption. It marks two premises DEFEATED: "always one missed edit away" fails for immutable sources, and "saves nothing" fails for checks that are mechanical but expensive. Three more are DOUBTFUL: the third state, validator placement before consumption, and the validator's correlated failure.
3. **The validator regress (composition friction).** `kb/reports/state/review/results/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md/kb/instructions/composition-friction-gate.md` finds that precondition 4 answers a question about cost when the worry is about correctness. It proposes that the note either say why a wrong validator fails loudly or limit the prohibition to validators that are themselves checked. Either option changes a claim.
4. **Grounding fail.** The fourth instance is unsupported as written. `semantic/grounding-alignment` (outcome fail) reports that ADR 027 never mentions `AGENTS.md.template` and designs the opposite editable-install arrangement. The instance needs evidence that supports it, or it has to go. That is a claim question for the operator. A pass cannot settle it.

**Dependents the change would reach.** The role report is at `kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/role`.

- **The two-state rule and the forbidden middle:** ADRs 038, 041 and 068; the proposals `checked-inline-blocks-for-shared-instruction-text`, `channel-compiled-instruction-artifacts`, `decisions-bind-their-consumers-through-site-back-pointers` and `factored-dependency-pairs-for-review-freshness`; the archived proposal `source-genre-is-one-open-field-on-the-snapshot`; the theory notes `a-consumption-channel-delivers-force-…`, `evidence/seven-documentation-cases-…` and `files-defer-centralized-schema-…`; and the claims-and-grounding and context-engineering tag heads.
- **The definition of "checked":** the banner proposal, the archived `atomic-step-grounding` proposal, `a-note-is-an-atomic-step-…`, the swamp review, and the build-systems and harness-handbook ingests.
- **The asymmetry:** `commitment-not-derivation-creates-new-ground-truth` and `kb/reference/validation-contract.md`. The Dagster ingest cites it as the claim it qualifies.
- **The preconditions and their numbers:** ADR 046 uses all four. `validation-contract.md` cites precondition 3 by number and `commitment-not-derivation-…` cites precondition 1. `a-citation-cannot-assert-more-fidelity-…` reuses precondition 4's wording.

Narrowing the rule to trusted copies or to negative claims, or admitting a hint state, would change the premise these dependents argue from. Eight further linking files were cut from the role report's input and are unseen.

**Route.** The claims are wrong or unsupported as stated: the two-state universal, the fourth instance's grounding, and precondition 4's argument. The route is `commonplace-review run rewrite kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md --commission FILE`, with the commission prepared by `cp-skill-write-multistage`. The operator also decides what changes in the dependents listed above.

## Ranked changes (for the rewrite commission, not for passes)

1. **Scope the rule to what the asymmetry supports.** Move the note's own condition, "tells consumers to stop looking", into the rule statement. Then either name or rule out a hint state that is untrusted and checked when used. The compiled-cue instance follows from that choice. Cost: a claim change that reaches nearly every dependent.
2. **Fix or drop the fourth instance.** Either find the source that actually designs the two `AGENTS.md.template` copies or remove the ADR 027 attribution. Also say whether a byte-identity check exists. Cost: one bullet plus a footer link.
3. **Repair precondition 4.** The note needs an argument about correctness: validators tested against copies known to be false, or a correlated failure that shows up loudly. Label "reviewed on every change" as a requirement or as an assumption. Cost: one paragraph; ADR 046 and `a-citation-…` depend on it.
4. **Settle the conflict at the regime boundary.** Precondition 1 and the Consequences bullet send natural-language summaries to omission. The regime section says a hand-maintained dependent is unavoidable where verification is judgment. Cost: one sentence in each place.
5. **State the conditions on "absent" and "checked".** An absent copy is bounded only when the consumer is directed to the live source. A checked copy is safe only when the validator runs before anyone consumes the copy. Mechanical derivation does not imply cheap derivation. Cost: a few clauses.
6. **Decide the cache-maxim sentence.** Drop it or state its limit. The compression checks disagree on what to do. Cost: one sentence.
7. **Wording and compression findings at depths 3–6.** These cover the asymmetry recap, the repeated machine-followable-lineage point, the "use-shaped artifact", "interrupt-placement problem" and "sweep pattern" terms, the description, and the idiom "rides on". They are worth doing only on the text after the rewrite.

**Sentence a hostile reviewer would attack first:** "Such a copy has exactly two valid states." The note's own next sentence, which forbids only copies that are "maintained by hand and trusted by consumers", and its compiled-cue instance both leave room for a third state.

**What reads well:** the absent-versus-false asymmetry, together with the Level A check price that moves a copy from managed staleness to enforce-or-omit, is a clear mechanism that dependents reuse directly.

## Support versus divergence (proposed)

- **Divergence, keep:**
  - the definition of "checked": a validator re-derives the copy from the source and fails on mismatch;
  - the asymmetry mechanism: a false copy causes silent wrongness when it tells consumers to stop looking;
  - "In that regime the hand-maintained dependent artifact is not forbidden; it is unavoidable";
  - precondition 1's exclusion of natural-language summaries from checking;
  - the numbering of the preconditions, which dependents cite.
- **Support, may be narrowed:**
  - "An unenforced copy is always one missed edit away from the catastrophic state";
  - "since trusting an unchecked copy now saves nothing";
  - "The spread is what shows it generalizes";
  - "would dominate, recovering the context economy without the drift";
  - "a validator is centralized, versioned, reviewed on every change".
- **In dispute, for the operator:** "Such a copy has exactly two valid states" and the title. These are what the critique and premise reports attack.

## Stale qualifications (claim questions for the operator)

- **ADR 027 citation:** the fourth instance and its footer link cite ADR 027 for a design the ADR does not contain. The grounding result failed on this.
- **Instance state labels:** the instance section promises four application states, but bullets 2 and 4 never state theirs (framework-decoration).
- **Compiled-views bullet:** it is filed as an instance surface "in the system", but it points to a prior requirement in another note (conceptual-role-conflation).
- **"This is the sharpest case of":** it reverses the specialization direction that the indexes note declares (grounding info).
- **Dependent side:** `validation-contract.md` cites precondition 3 for a sense, ground truth located in a second artifact, that is closer to precondition 2. ADR 056 cites the note as ruling out a lifecycle field, but the note raises `status:` only as an open question.

## Findings not acted on

The plan stops, so no finding gets a pass. Findings 1 to 6 are claim questions. They become input to the rewrite commission. The rest are wording and compression issues; they wait for the rewritten text, because a pass over the current text would be replaced.

- `…/semantic/grounding-alignment.md` (fail): claim question. Unsupported fourth instance; fix in the rewrite.
- `…/semantic/completeness-boundary-cases.md`: claim question. The third state; this is the stopped proposal.
- `…/semantic/internal-consistency.md`: claim question. Conflict at the regime boundary.
- `…/semantic/conceptual-role-conflation.md`: claim question. Whether the compiled-views bullet is an instance or a prior account.
- `…/semantic/epistemic-status-blur.md`: claim question. The status of precondition 4's premise.
- `…/semantic/underspecified-assertions.md`: claim question. Whether "unbounded" means duration or magnitude decides how "forbidden" is supported.
- `…/complexity/framework-decoration.md`: the instance-state labels depend on what the rewrite keeps.
- `…/kb/instructions/compression-bundle/branch-bloat.md`, `…/detail-overhang.md`, `…/marginal-value-redundancy.md`: compression of text the rewrite will replace. The cache-maxim item is a meaning choice.
- `…/accessibility/undefined-terms.md`, `…/prose/mannered-prose.md`, `…/sentence/clause-packing.md`, `…/sentence/concept-attribution.md`, `…/sentence/framing-mismatch.md`, `…/sentence/misleading-link-text.md`, `…/sentence/stock-phrases.md`, `…/structural/compound-bullet.md`: wording of text the rewrite will replace.
- `…/frontmatter/description-discrimination.md`: the description should follow the rewritten claim and scope.
