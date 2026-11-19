## Fix Report: memory-management-policy-is-learnable-but-oracle-dependent

Scope: all 17 persisted Luna WARN/FAIL verdicts for completed review jobs 6677–6717 (10 WARN, 7 FAIL). Fixed: 17. Deferred: 0.

| # | Job | Outcome | Check | Strategy | Summary | Status |
|---|---:|---|---|---|---|---|
| 1 | 6678 | WARN | Notation opacity | `new-pattern` (remove-separable-cluster) | Removed the undefined `f(...)` placeholder with the inspectability-spectrum cluster | fixed |
| 2 | 6679 | FAIL | Undefined terms | `new-pattern` (define-or-remove-specialist-terms) | Defined oracle and reinforcement learning inline; removed the remaining unexplained specialist shorthand | fixed |
| 3 | 6680 | WARN | Unidentified references | `new-pattern` (identify-or-remove-named-references) | Removed opaque person and benchmark references; identified the two retained systems by role | fixed |
| 4 | 6682 | FAIL | Connection inflation | `new-pattern` (deduplicate-navigation) | Replaced twelve mostly duplicated footer entries with two distinct, controlled navigation edges | fixed |
| 5 | 6692 | WARN | Confidence miscalibration | `hedge-strength-mismatch` | Recast signal availability as necessary, not sufficient, and stated what would isolate it as the dominant bottleneck | fixed |
| 6 | 6694 | FAIL | Proportion mismatch | `new-pattern` (narrow-to-claim) | Removed the reach, storage-form, curriculum, tool-use, and system-spectrum theses | fixed |
| 7 | 6695 | WARN | Pseudo-formalism | `new-pattern` (remove-separable-cluster) | Removed the content-free relevance function rather than preserving symbolic decoration | fixed |
| 8 | 6699 | WARN | Completeness boundary cases | `boundary-case-acknowledged` | Made inspectability, runtime responsiveness, and feedback-trained updating independent dimensions, with both requested counterexamples | fixed |
| 9 | 6701 | WARN | Grounding alignment | `qualifier-dropped`; `unsourced-addition`; `scope-narrowed` | Restored AgeMem's composite, partly judge-based reward; removed the unsupported reach claim; distinguished fixed parameters from responsive decisions | fixed |
| 10 | 6705 | WARN | Clause packing | `new-pattern` (remove-separable-cluster) | Removed the packed storage-split sentence with its unrelated representational-form thesis | fixed |
| 11 | 6707 | WARN | Framing mismatch | `new-pattern` (scope-title-to-mechanism) | Scoped the title and opening to policies trained from outcome feedback, explicitly excluding fixed policies | fixed |
| 12 | 6708 | FAIL | Misleading link text | `new-pattern` (remove-misleading-link) | Removed the mislabeled paper link and the unsupported random-pruning inference with the separable forgetting comparison | fixed |
| 13 | 6710 | WARN | Stock phrases | `new-pattern` (remove-metadiscourse) | Removed both elevation sentences with the storage-form cluster | fixed |
| 14 | 6711 | FAIL | Bullet capitalization | `new-pattern` (normalize-bullet-capitalization) | Rebuilt the footer with capitalized link labels | fixed |
| 15 | 6712 | FAIL | Compound bullet | `new-pattern` (remove-separable-cluster) | Removed the AgeMem-lessons list whose curriculum and Commonplace proposals formed separate claims | fixed |
| 16 | 6713 | WARN | General before specific | `new-pattern` (general-before-case) | Put the general mechanism and proof before the AgeMem and AgentFly evidence cases | fixed |
| 17 | 6714 | FAIL | Notes collection contract | `unframed-domain-examples`; `single-source-vocabulary`; `new-pattern` (generalize-single-system-proof); `new-pattern` (remove-separable-cluster) | Rebuilt the note as a general lemma, added an independent code-grounded case, narrowed the body to one premise, and normalized footer labels | fixed |

### Warning-to-fix mapping

- **#1 / job 6678 (notation opacity):** The undefined “relevance = f(recency, frequency, semantic alignment)” expression was removed with the separable system spectrum. The surviving discussion describes a hand-written relevance rule in plain language.
- **#2 / job 6679 (undefined terms):** `RL`, `LTM`, `STM`, step-wise GRPO, non-diffable, boiling cauldron, vision-feature problem, constrained optimization, Jaccard conflict detection, and distributed-parametric were removed. The retained terms are defined in prose: an oracle is an evaluative signal, and reinforcement learning is training from rewards.
- **#3 / job 6680 (unidentified references):** Simon, ALFWorld, HotpotQA, Fofadiya, and Tiwari no longer appear. AgeMem is introduced through its paper snapshot; AgentFly is identified as a code-inspected case-memory agent.
- **#4 / job 6682 (connection inflation):** The duplicated footer links for behavior change, artifact axes, exact specs, KB automation, reach, and inspectability were removed. The two surviving footer edges add navigation not already supplied inline.
- **#5 / job 6692 (confidence miscalibration):** “AgeMem succeeds because it has a clear oracle,” “cannot be fully specified,” the table that “establishes” a spectrum, and the claim that AgeMem “confirms” the KB bottleneck were replaced by a general necessity argument. The note now says an evaluative signal is necessary but cannot by itself rule out operation-set, data, model, or learning-procedure limitations; it also names the controlled comparison needed to establish signal quality as dominant.
- **#6 / job 6694 (proportion mismatch):** The facts-without-reach, representational-form storage, Commonplace medium, curriculum, tool-underuse, and four-system spectrum analyses were removed. The note now spends its body on the title's feedback-and-evaluation mechanism, two evidence cases, its boundaries, and one concise KB application.
- **#7 / job 6695 (pseudo-formalism):** The unspecified `f` function was removed rather than treated as a formula.
- **#8 / job 6699 (boundary cases):** The note now explicitly covers a readable decision tree updated from outcomes and an opaque fixed heuristic. It distinguishes policy learning from runtime responsiveness, so these cases no longer contradict a one-dimensional spectrum.
- **#9 / job 6701 (grounding alignment):** AgeMem is described as using task-performance, context-management, memory-management, semantic-relevance, and penalty components, with language-model judgment in part—not an unambiguous binary oracle. The unsupported “never produces knowledge with reach” claim was removed. The Fofadiya–Tiwari adaptability classification was removed, while the general boundary now distinguishes responsive fixed rules from learned parameter updates.
- **#10 / job 6705 (clause packing):** The 49-word AgeMem storage-split sentence was removed with the separable storage-form thesis.
- **#11 / job 6707 (framing mismatch):** The title is now “A feedback-trained memory-management policy requires an evaluative signal.” The opening immediately distinguishes outcome-trained updates from explicit and merely state-responsive policies.
- **#12 / job 6708 (misleading link text):** The “ingest limitations” text that linked to the paper itself, and the unsupported inference it introduced, were removed with the forgetting comparison.
- **#13 / job 6710 (stock phrases):** Both “The interesting question is therefore...” and “This is the deeper version...” were deleted.
- **#14 / job 6711 (bullet capitalization):** The old footer was replaced; both retained link labels begin with capitals.
- **#15 / job 6712 (compound bullets):** The entire separable lessons list was removed, including the two bullets that combined AgeMem observations with distinct Commonplace proposals.
- **#16 / job 6713 (general before specific):** The note now proceeds from claim and mechanism to evidence cases, boundaries, and the narrower KB application.
- **#17 / job 6714 (collection contract):** The opening and proof are general and survive removal of AgeMem. AgentFly adds an independent code-grounded learned read-back policy, while AgeMem remains a paper-grounded example rather than the premise. Separable claim clusters were removed. Footer labels are now the controlled `extends` and `exemplifies`, and there is no footer edge from a direct external URL.

### Deferred items

- None.

### Known intentional non-changes

- The existing filename and `distillation`-era migration conventions were not treated as defects or changed.

### New patterns

- **remove-separable-cluster:** When a flagged sentence belongs to an unrelated thesis that makes the note non-composable, remove that cluster rather than locally polishing it.
- **define-or-remove-specialist-terms:** Define load-bearing terminology inline and remove specialist shorthand that survives only in discarded side analyses.
- **identify-or-remove-named-references:** Give retained named systems a brief role gloss; remove names that occur only in discarded examples.
- **deduplicate-navigation:** Keep footer edges only when they add a traversal path not already explained by an inline link.
- **narrow-to-claim:** Restore proportionality by retaining only the mechanism, evidence, boundaries, and application needed for the titled premise.
- **scope-title-to-mechanism:** Scope a broad title to the exact mechanism the proof establishes.
- **remove-misleading-link:** Delete a link and its unsupported inference when no target exists that fulfills the link text's promise.
- **remove-metadiscourse:** Delete elevation sentences that merely announce a contrast already made concretely.
- **normalize-bullet-capitalization:** Rebuild or edit footer link labels so prose bullets begin with capitals.
- **general-before-case:** State and prove the transferable mechanism before presenting system examples.
- **generalize-single-system-proof:** Derive the claim independently, then use multiple systems as corroborating cases rather than treating one description as the premise.

### Validation

`commonplace-validate kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` completed with `Overall: PASS (clean)` for the note and its affected `learning-theory-README.md` tag index; both reported no WARN or FAIL findings.

## Sol follow-up

Scope: all 4 persisted Sol non-pass verdicts for `kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` from completed review jobs 6718–6758 (2 WARN, 2 FAIL). Result-level disposition: **4 fixed, 0 deferred**. The Luna mapping above is preserved unchanged.

| # | Job / pair | Outcome | Check | Strategy | Summary | Status |
|---|---|---|---|---|---|---|
| S1 | 6721 / 13628 | WARN | Unidentified references | `new-pattern` (identify-named-system-inline) | Identified AgeMem at first mention as a feedback-trained agent-memory system | fixed |
| S2 | 6726 / 13662 | FAIL | Claim strength | `new-pattern` (strengthen-title-to-result) | Replaced the definitional signal-requirement title with the contestable result that discrimination enables improvement and signal quality bounds feedback-trained adaptation | fixed |
| S3 | 6744 / 13784 | WARN | Load-bearing qualifiers | `new-pattern` (drop-non-load-bearing-restriction) | Generalized the theorem from memory management to feedback-trained policy adaptation while retaining memory management as the worked application and evidence | fixed |
| S4 | 6750 / 13825 | FAIL | Parsing ambiguity | `new-pattern` (disambiguate-possessive) | Replaced ambiguous `their downstream value` with `the downstream value of the choices being updated` | fixed |

### Sol result-to-fix mapping

- **S1 / job 6721 (unidentified references):** The first mention now reads “AgeMem, a feedback-trained agent-memory system,” before describing its operations and training; the paper-snapshot link remains the evidence route.
- **S2 / job 6726 (claim strength):** The title now states both substantive results: a signal must discriminate downstream value to improve a policy, and its quality bounds feedback-trained adaptation. The opening explains the zero-information, noisy-ranking, and misaligned-ranking cases rather than reducing the theorem to the existence of feedback.
- **S3 / job 6744 (load-bearing qualifiers):** The title, description, opening claim, and structural argument now concern policies generally. Memory management is explicitly the worked application; AgeMem and AgentFly remain corroborating cases. The load-bearing `feedback-trained` boundary remains explicit, as do the fixed-policy and runtime-responsive counterexamples.
- **S4 / job 6750 (parsing ambiguity):** The description now attributes downstream value specifically to “the choices being updated,” not to memory operations as context-free action types.

### Sol deferred items

- None.

### Sol new patterns

- **identify-named-system-inline:** Name the system's category at first mention; a source link alone is not an identification.
- **strengthen-title-to-result:** Replace a title that states a definitional prerequisite with the contestable consequence actually established by the argument.
- **drop-non-load-bearing-restriction:** Remove a domain restriction from the theorem when no proof step depends on it, then retain that domain as an application.
- **disambiguate-possessive:** Replace a possessive with the intended referent when two nearby plural nouns support materially different readings.

### Sol validation

`commonplace-validate kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` reported `Overall: PASS (clean)` for both the exact note and the affected `learning-theory-README.md` tag index, with no WARN or FAIL findings.

## Sol residual follow-up

Scope: the 2 residual Sol FAIL verdicts for `kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` from review jobs 6767–6768. Result-level disposition: **2 fixed, 0 deferred**. All earlier report content and mappings above are preserved.

| # | Job / pair | Outcome | Check | Strategy | Summary | Status |
|---|---|---|---|---|---|---|
| R1 | 6767 / 13930 | FAIL | Claim strength | `new-pattern` (surface-memory-policy-boundary) | Replaced the general signal-discrimination truism with the body-supported claim that feedback-trained memory management remains oracle-dependent even when its operations are hand-designed | fixed |
| R2 | 6768 / 13937 | FAIL | Description discrimination | `new-pattern` (description-add-scope-boundary) | Replaced the title-paraphrasing description with the fixed/runtime-responsive boundary plus the distinct effects of noisy and misaligned rankings | fixed |

### Sol residual result-to-fix mapping

- **R1 / job 6767, pair 13930 (claim strength):** The result found that no knowledgeable reader could dispute that non-discriminating feedback cannot direct policy updates, and that the causal title therefore read as a truism. The title is now “Feedback-trained memory management is oracle-dependent even when its operations are hand-designed,” surfacing the note's contestable application boundary while matching the AgeMem case and the general mechanism established in the body.
- **R2 / job 6768, pair 13937 (description discrimination):** The result found that the description merely paraphrased the prior title without adding mechanism, scope, implication, or application context. The description now distinguishes fixed and merely runtime-responsive memory rules from outcome-driven policy updates and records how noisy versus misaligned rankings affect learning.

### Sol residual deferred items

- None.

### Sol residual new patterns

- **surface-memory-policy-boundary:** When a general title is true by definition, title the non-obvious application boundary the body establishes.
- **description-add-scope-boundary:** Replace a title paraphrase with the boundary that distinguishes the note during retrieval, adding a compact implication only when it remains cohesive.

### Sol residual validation

`commonplace-validate kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` reported `Overall: PASS (clean)` for both the exact note and the affected `learning-theory-README.md` tag index, with no WARN or FAIL findings. `git diff --check -- kb/notes/memory-management-policy-is-learnable-but-oracle-dependent.md` also completed cleanly.
