# Claim account: checking retained results as a cost–risk trade-off

No write brief was supplied, so the commission is the only statement of intent and no commission–brief contradiction can arise. Source labels follow the reconstruction: S1 `kb/types/tag-readme.md`, S2 `kb/types/connect-report.md`, S3 `kb/theory/frontloading-spares-execution-context.md`, S4 `kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`.

The note's order follows the shape the commission says the user approved. First comes the opening claim: the reuse benefit and the trade-off. Then come the two contrasting examples, the completeness mark and the connect report, which carry most of the explanation. After them come one added conclusion (no known change does not establish freshness), the compact numbered checking conditions, and `## Scope`. Body target: 600–800 words, with 850 as the ceiling.

## 1. Retaining a derived result saves recurring work, and reuse amortizes producing it

- **Treatment:** state as inference. This is the note's opening premise.
- **Basis:** Reconstruction A and Inference 1. Per S3, executing a procedure at use time costs work that "recurs on every invocation", and one earlier computation "saves many runtime calls from repeating the same work". The saving comes from the discovery and derivation that are no longer performed.
- **Scope and qualifiers:** S3 argues this for frontloading results into LLM calls. Applying it to persisted KB artifacts such as marks and reports is a transfer, so state it as reasoning. Do not cite it as S3's own claim about artifacts. Keep the claim qualitative. Do not invent sizes of the saving.
- **Depends on:** nothing else in this account. Sections 2 and 3 depend on it.
- **Destination:** the opening paragraph. Link S3 inline as the premise that the reuse saving rests on.

## 2. Checking by full recomputation on every use largely defeats the saving

- **Treatment:** state as inference. Add the cheaper-verification point in at most one sentence, with a "when" qualifier.
- **Basis:** Inference 2. If the check repeats the derivation the copy replaced, the recurring cost from S3 comes back. The mark's `rg` sweep (S1) is the concrete case. No source states this directly. Gaps: no source distinguishes verification from derivation.
- **Scope and qualifiers:** Say "largely", not "entirely": verification and context-loading costs may differ (commission). The cheaper-verification sentence must be conditional, in the form "when verification is cheaper than derivation, checking on every use can still save work". Do not claim that mechanical comparison against inputs is generally cheaper.
- **Depends on:** 1.
- **Destination:** the opening argument, right after 1. It can be illustrated briefly in the mark example ("re-running the sweep on every read").

## 3. How often to check depends on the cost of checking relative to the risk of relying on stale or wrong content

- **Treatment:** state as inference. This is the note's central claim, and it replaces the old categorical argument; do not present it as an exception to that argument.
- **Basis:** Inference 3. S3 sets the context saving against the wrongness of frozen values ("commits a guess that the executor could have read off the live state"). S4 §Scope and §Defenses treat accepting an imperfect index as an explicit utility trade-off, "rather than a hidden consequence of false completeness".
- **Scope and qualifiers:** This is a qualitative design trade-off, not a calibrated expected-loss policy. Give no numbers, intervals or risk estimates. Do not set up a universal valid/invalid or safe/unsafe split, and do not prohibit unchecked copies universally. Keep S4's point that an accepted risk should be an explicit choice rather than a hidden consequence; this can be folded in briefly.
- **Modality:** The claim reads as universal by default. It is a universal conditional claim about what the right checking frequency depends on, not a prevalence claim, so no statistical mode needs declaring. It would be refuted by a case where the right checking policy plainly does not respond to check cost or reliance risk.
- **Depends on:** 1, 2 and 4.
- **Destination:** the opening, stated once. The two examples then work it out.

## 4. A false trusted copy can suppress the work that would expose its error

- **Treatment:** state with a qualifier, as a conditional mechanism.
- **Basis:** Reconstruction C. Per S4, the failure is "in control flow, not merely in missing content". The view "ends discovery before the operation that could reveal additional current items". The mechanism applies to "any artifact a consumer treats as exhaustive". S1 applies it to the mark: "a false mark tells exhaustive consumers to stop looking while members are still out there."
- **Scope and qualifiers:** The mechanism requires that the consumer actually stops on the copy, and that the suppressed route would find more task-relevant items. S4 explicitly makes no prevalence claim. Do not call every error catastrophic. Do not imply that non-exhaustive hints are harmless.
- **Depends on:** nothing else in this account. Sections 3, 5 and 6 depend on it.
- **Destination:** one or two sentences in the opening, used as the risk side of the trade-off. It is then instantiated in the mark example and noted as possible in the connect-report example. Link S4 inline as the mechanism.

## 5. Example 1: the completeness mark, a stop-authorizing claim with a cheap, defined, reactive check

- **Treatment:** state, with qualifiers. This is the first main example.
- **Basis:** Reconstruction E and Inferences 4 and 5.
  - `complete: true` authorizes skipping the by-tag `rg` membership search. Its contract says "validator-enforced; readers may skip the by-tag `rg` sweep".
  - The derivation is defined: one-hop reach from the head to every artifact carrying the tag.
  - The inputs are identified and locatable: the participating collections and nothing else.
  - The sweep always recovers the membership, so a fallback recomputation exists.
  - Enforcement is reactive. The validator queues the gap when the head is next validated, so a mark can be false between validations.
  - The check covers reach given the tags. It does not cover whether an assignment fits the tag, which is a matter for semantic review.
- **Why enforcement is attractive here (inference):** The claim authorizes a stop, so mechanism 4 applies. The check is deterministic, and its rule and inputs are defined. Together these make enforcement attractive where it is inexpensive.
- **Scope and qualifiers:**
  - Assurance holds as of the last validation, not continuously. Do not invent an always-current guarantee.
  - Do not say the mark meets all four conditions of section 10. Its contract supplies conditions 1, 2 and 3 (when the inputs are supplied). Nothing establishes condition 4, the validator's trustworthiness.
  - Do not adopt S1's own wording "enforced-or-omitted", "never load-bearing" or "never correctness" as general law (see Conflicts).
  - Mention the fallback (drop the mark; readers return to `rg`) only if it is needed, without guaranteeing graceful degradation.
- **Depends on:** 2, 3 and 4.
- **Destination:** the first example section. Link S1 at the example as the actual contract. This is a scoped illustration of the theory, not corroboration of it.

## 6. Example 2: the connect report, a candidate-only result whose reuse can be reasonable

- **Treatment:** state the contract facts. State the reuse argument and the breadth of dependencies as inference.
- **Basis:** Reconstruction F and Inferences 6 and 7. S2 says the report gives "candidate edges for a future writer to act on" and that readers "should treat its contents as suggestions to evaluate". Candidates are assessed against the target's actual claim, evidence and contract. The report records its discovery pass, and its `depth` matches the pass actually run.
- **Inferences to carry:**
  - Rerunning discovery has a real cost.
  - Material added anywhere the pass searches may change what a renewed search finds.
  - Reusing an earlier report can be reasonable when rerunning costs more than the risk accepted for the task.
  - Because the report is candidate-only and is evaluated before action, its contract does not authorize stopping the way the mark's does.
- **Scope and qualifiers:**
  - Do not infer that suggestions carry no risk or that their failure is always loud. No source settles the failure mode.
  - If a consumer treats a report as the full set of connections, mechanism 4 can apply.
  - Do not say the report's dependencies cannot be enumerated. The difficulty is tracking a *sufficient* dependency set, including newly added relevant material.
  - Do not offer a "per unchanged version" rule as the solution.
  - The candidate-only status is a contract on readers, not evidence of how consumers actually behave.
- **Depends on:** 3, 4, 7 and 9.
- **Destination:** the second example section. Link S2 at the example.

## 7. Staleness arises because the source and the retained copy have separate update paths

- **Treatment:** state as a brief supporting premise, folded in where it is used rather than given its own section.
- **Basis:** Reconstruction D. Per S4, "the source set and its navigation surface have separate update paths". The question is whether every relevant change reaches the copy "through a reliable synchronization path". S3's validity window and lineage (Reconstruction B) say a copy is accurate only while its inputs are, and that lineage supports refresh.
- **Scope and qualifiers:** Do not claim lineage is always complete or obtainable. Give no refresh interval.
- **Depends on:** nothing else in this account. Sections 6 and 8 depend on it.
- **Destination:** a clause in the connect-report example and in the post-example conclusion (8). It needs no separate section.

## 8. No known change does not establish freshness

- **Treatment:** state as inference. This is the only added conclusion after the examples.
- **Basis:** Inference 8. The absence of a known change counts as evidence of freshness only if every relevant change reaches the checker (D, B). S1's reactive enforcement shows that even an enforced mark can be stale until the next validation.
- **Scope and qualifiers:** Keep it to this conclusion. Do not restate the two examples or their costs in a summary section (commission revision constraint).
- **Depends on:** 5, 6 and 7.
- **Destination:** immediately after the two examples, before the numbered conditions.

## 9. Mechanical checking is distinct from semantic review; judgment-produced results can still have checkable properties

- **Treatment:** state, with a qualifier.
- **Basis:** Inference 10. S1 separates validator checks from assignment fit, which is judged in review. S2 says "Every candidate link must resolve. `commonplace-validate` checks this", while assessing candidates is judgment.
- **Scope and qualifiers:**
  - Say plainly that assessing connect candidates calls for judgment. Do not present semantic review as a weak substitute for a mechanical check that is supposedly missing.
  - Distinguish checking a result's checkable properties (link resolution, required sections) from mechanically reconstructing its substantive judgment.
  - Do not make a blanket statement that judgment-produced results lack checkable properties.
  - The connect report is a contrast case for retained results in general, not a claim that discovery can be re-derived by a fixed rule.
- **Depends on:** 5 and 6.
- **Destination:** one or two sentences in the connect-report example, possibly echoed in the definition of condition 1.

## 10. The numbered checking conditions

- **Treatment:** state compactly as reasoning, keeping the numbering and recognizable concepts that dependents cite.
- **The conditions:**
  1. A derivation or comparison rule.
  2. A locatable copy and source.
  3. The source is available at check time.
  4. A sufficiently trustworthy checker.
- **Definition:** A mechanical check derives the result from, or compares it against, identified available inputs.
- **Basis:** Inference 9.
  - Condition 1: S1 defines one-hop reach. S4 says completeness claims should be machine-readable and checked against the canonical set.
  - Condition 2: S1 §Scope and the frontmatter field.
  - Condition 3: S1's validator reads the participating collections, and S3 requires lineage for refresh.
  - Condition 4: no source supports it. It is reasoning only.
- **Scope and qualifiers:**
  - These are conditions for a check being possible and worth relying on, not guarantees.
  - Do not assume checking is free, that every relevant dependency can be enumerated or monitored, or that assurance stays current without a check.
  - For condition 4, add one brief sentence: testing or centralizing a validator lowers the cost of assurance but does not prove the validator correct. This is reasoning with no source, so do not open a regress discussion.
  - Do not map every example onto every condition. Say only what each example's contract actually supplies. In particular, the mark lacks support for condition 4 (see 5).
- **Depends on:** 2, 5 and 9.
- **Destination:** a compact numbered list after conclusion 8.

## 11. Computation amortization versus amortization of validator development

- **Treatment:** leave out as a claim. Only avoid conflating the two.
- **Basis:** Gaps. No source discusses amortizing validator development across artifacts.
- **Scope and qualifiers:** "Amortization" in the note means spreading the cost of producing or checking a result over its uses (section 1). If the note mentions validator cost at all, in the condition-4 sentence, it must not merge the two senses.
- **Destination:** none, beyond care with wording.

## 12. Applicability limits

- **Treatment:** state in `## Scope` as actual limits, not a list of general disclaimers.
- **Content:**
  - The trade-off is qualitative, and no costs or risks are calibrated.
  - The suppression mechanism is conditional and makes no prevalence claim.
  - The examples are Commonplace contracts used as illustrations, scoped to their declared inputs. The mark's assurance holds over the participating collections only, as of the last validation, and covers reach given the tags rather than tag correctness.
  - The amortization argument is transferred from frontloading.
- **Open gaps that may be named:**
  - No source establishes when a checker is sufficiently trustworthy.
  - No source establishes whether the omissions of candidate-only results fail silently.

## Reserved for the operator

- **Title:** The title is kept temporarily, together with the existing H1 and path (`types/note.md`). Its universal wording is a transition constraint and does not license any matching body claim. The author proposes one replacement title in the report only.
- **Dependents:** Do not edit dependents. That covers S1's "safety half … enforced-or-omitted" wording, S4's §Defenses sentence citing "the broader rule", and others. The report explains which classes of dependent rationale need correction. It notes that the role report inspected only 30 of 38 linking files, so no complete dependency audit exists.
- **Publication:** needs the user's separate approval. Create no lasting brief, and do not edit indexes or contracts.

## Commitments the note must not make

- **No categorical rules:** no universal checked-or-absent rule, enforce-or-omit rule or forbidden middle, and no valid/invalid or safe/unsafe dichotomy. Do not keep any such slogan nominally while softening it elsewhere. The body must not support the title's universal wording.
- **No guaranteed outcomes for the mark:** no guaranteed graceful degradation, and no "dropping the mark never costs correctness". S1's guarantee rests on consumers actually running the fallback, which S4 flags.
- **No blanket handling of judgment results:** no automatic omission of judgment-based material, and no claim that judgment-produced results lack checkable properties.
- **No free or always-current checking:** no claim that mechanical checking is free or generally cheaper than derivation. No assurance that stays current because no change is known. No always-current guarantee for the reactively enforced mark.
- **No overclaiming about dependencies:** no claim that every dependency can be enumerated or monitored, nor that the connect report's dependencies categorically cannot be. No "per unchanged version" rule for broad dependencies.
- **No overclaiming about either example:** no claim that the mark meets all four conditions or that its validator is trustworthy. No claim that suggestions are risk-free or that their failures are always loud. No claim that S2 endorses reuse between runs.
- **No invented numbers:** no refresh interval, risk estimate, prevalence or empirical reliability claim.
- **Excluded material:**
  - The old examples (compiled memory views, hot-path contract values, duplicated `AGENTS.md.template`).
  - The cache maxim, repeated asymmetry summaries and unrelated open questions.
  - A taxonomy of risk factors or a catalogue of maintenance policies.
  - ADRs cited as authority.
  - External literature, including S3's external evidence.
  - Any history of this rewrite.
