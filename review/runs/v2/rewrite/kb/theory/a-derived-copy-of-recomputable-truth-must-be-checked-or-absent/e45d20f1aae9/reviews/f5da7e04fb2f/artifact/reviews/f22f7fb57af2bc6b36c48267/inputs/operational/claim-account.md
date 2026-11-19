# Claim account: checking retained results as a cost–risk trade-off

No write brief was supplied, so the commission is the only statement of intent. The commission does not contradict itself, and the reconstruction found no contradiction in it. The note keeps `types/note.md`, its existing path, and its existing title and H1. Keeping the title is a transition constraint set by the commission. The body must not inherit the title's universal wording.

Ordering that the commission sets: (A) the opening mechanism, meaning the reuse benefit, amortization and the suppression risk; (B) the completeness-mark example; (C) the connect-report contrast; (D) the trade-off that governs checking frequency; (E) the compact numbered checking conditions; (F) `## Scope` for the limits. The body should be 600–800 words, with 850 as the ceiling. The two examples carry most of the explanation. Abstract lists stay short.

Mode: declare the central claim as a qualitative design trade-off with conditional mechanisms. It is not a universal prohibition and not a calibrated policy. The collection contract asks for the mode to be declared in the claim text. The opening should therefore present the claim as a trade-off ("how often to check depends on…"). It should not present it as a rule about whether a copy is permitted.

## C1 — Retaining a derived result saves work, and reuse amortizes producing and checking it

- **Treatment:** state it.
- **Basis:** source-3 (`frontloading-spares-execution-context.md`), "The context saving". The cost of discovery and derivation "recurs on every invocation". Frontloading is economic when "one build-time, install-time, or session-start computation saves many runtime calls from repeating the same work". The saving lies in the discovery and derivation "the call no longer performs". Source-1 is the concrete instance: the `complete: true` mark lets readers "skip the by-tag `rg` sweep".
- **Scope and qualifiers:** the saving is qualitative. Source-3 gives no magnitudes, so the note must invent none. Source-3 is about pre-computed inputs to a later call. The note generalizes its amortization argument to any retained derived result. Present that generalization as the note's own claim, with source-3 as its origin. Do not present source-3 as having said it. Do not use source-3's external study claims.
- **Amortizing a check** across uses of the copy is a different thing from amortizing the development of a validator across artifacts (see C9/I7). Do not merge the two.
- **Dependencies:** none. This is the premise everything else rests on.
- **Destination:** the opening paragraph, in one or two sentences. Link source-3 inline, for example with "as in" or "since".

## C2 — Full recomputation on every use largely defeats the saving

- **Treatment:** state it as inference.
- **Basis:** I1. The premise comes from source-3: the value is the work the later call "no longer performs". The conclusion is that a check which reruns the full derivation does that work again. The commission states this conclusion directly.
- **Scope and qualifiers:** say "largely", not "entirely". Loading the copy into context and computing it are separate costs (source-3: inlining content that would be loaded anyway "moves those tokens earlier"). Verification cost and context-loading cost may therefore differ. Verification that is cheaper than recomputation, such as a comparison, keeps more of the saving. No source describes such a verification. The commission allows this distinction **at most one sentence**, as a definition, with no examples or claims about how common it is.
- **Dependencies:** C1.
- **Destination:** the opening, right after C1. It motivates why checking frequency is a real decision.

## C3 — A false trusted copy can suppress the work that would expose its error

- **Treatment:** state it with a qualifier. It is a conditional mechanism, not a prevalence claim.
- **Basis:** source-4 (`indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`). The failure is "in control flow, not merely in missing content". The copy "ends discovery before the operation that could reveal additional current items". The mechanism applies to "any artifact a consumer treats as exhaustive". Source-1: "a false mark tells exhaustive consumers to stop looking while members are still out there."
- **Scope and qualifiers:** the harm needs three things:
  - the consumer treats the copy as licensing a stop;
  - the suppressed operation would actually find more for the task at a fixed endpoint;
  - the loss is in recall on the suppressed route, not in total utility. An imperfect view may still have greater overall utility (source-4 Scope).

  Do not call every error catastrophic, and do not call every hint harmless.
- **Dependencies:** C1, because the saving is what makes the copy trusted in place of the work.
- **Destination:** the opening, as the risk side of the trade-off. Then make it concrete in the completeness-mark example (I2). Link source-4 inline with "because" or "as".

## C4 — The completeness mark: a licensed stop, deterministically checkable, enforced reactively, with a fallback

- **Treatment:** state it. This is the first developed example.
- **Basis:** source-1 (`kb/types/tag-readme.md`):
  - Frontmatter: `complete: true` means the head reaches every member in one hop. It is "Validator-enforced; readers may skip the by-tag `rg` sweep."
  - Scope: membership ranges over the participating collections declared in `kb/tags/COLLECTION.md`, which is an enumerable input set.
  - "Maintaining the mark": "Enforcement is reactive". The validator queues the gap when the marked head is next validated, and `kb/tags/` must be revalidated after tagging anywhere.
  - Exits: drop to selective, and readers "fall back to `rg`".
- **Inference to include:** I2 says a false mark is exactly source-4's suppressing exhaustive view. I6 says reactive enforcement means the mark can be false between a tagging change and the next validation. The guarantee is "checked when validated", not "always current". Source-1's "dropping the mark costs one recomputation, never correctness" covers dropping the mark. It does not cover relying on a present but stale mark.
- **Scope and qualifiers:**
  - The case is one local contract. It shows that the checking conditions **can** be met, not that they generally are.
  - The check covers declared tags only. Whether an artifact fits a tag's meaning is semantic and is judged in authoring and review (source-1 Authoring Instructions). This links to C7.
  - The deterministic check makes enforcement **attractive where inexpensive**, not obligatory everywhere.
  - Do not invent an always-current guarantee.
- **Dependencies:** C1, C3 and C7, and it feeds C8.
- **Destination:** section B, as a short developed paragraph or two. Link source-1 at the example as the actual contract, not as authority for the general reasoning.

## C5 — The connect report: candidates for evaluation, with broad dependencies; reuse can be reasonable

- **Treatment:** state it, with parts marked as inference. This is the second developed example and the contrast case.
- **Basis:** source-2 (`kb/types/connect-report.md`):
  - Readers should treat its contents as "suggestions to evaluate, not as state already in the KB". It "is not itself a durable knowledge claim".
  - Selection is judgment-based: the articulation test, reader-need labels, and a judgment of the target's actual claim. It is not a fixed derivation rule.
  - The Discovery Trace records queries, indexes and searches across KB-wide surfaces.
- **Stated as inference:** I4 says that because discovery surfaces are KB-wide, new material anywhere can change what a renewed search finds. The dependencies cannot be listed as a fixed input set, which breaks condition (2) and limits condition (3). I5 says the report does not license a stop the way the mark does, so suppression bites less directly. But a consumer that relies on a stale report instead of renewed discovery can still miss connections, and nothing in the report signals the miss, because source-2 has no freshness or invalidation field. That last point is an inference from omission.
- **Reuse judgment:** "reusing it can be reasonable when rerunning discovery costs more than the risk accepted for the task." The basis is the commission and the operator's current direction, which accepts this in practice. No source states it. Phrase it as a consequence of the C6 trade-off, not as an empirical finding.
- **Scope and qualifiers:**
  - Do not infer that suggestions carry no risk or that their failure is always loud.
  - Do not claim discovery can be re-derived by a fixed rule. The report contrasts with the mark as a retained result, not as a mechanically recomputable copy.
  - Source-2 says nothing about how often reports are reused, how stale they get, or what failure costs. Invent none of these.
  - No "per unchanged version" rule.
- **Dependencies:** C3, C6 and C7, and it contrasts with C4.
- **Destination:** section C, right after the mark. Link source-2 at the example.

## C6 — Checking frequency depends on checking cost relative to the risk of relying on stale or incorrect information

- **Treatment:** state it as inference. It is the note's central qualitative claim.
- **Basis:** I3 combines source-3 and source-4:
  - source-3: a frontloaded artifact needs a "validity window", and lineage, a timestamp or regeneration information to support refresh. Saving context and forfeiting the live-state advantage are "two pulls in the same decision".
  - source-4: an imperfect view may have greater overall utility, and loss of recall "should be an explicit trade-off rather than a hidden consequence of false completeness".
- **Scope and qualifiers:**
  - It is qualitative and not numerically calibrated. No refresh interval, risk estimate or reliability figure.
  - Do not build a risk-factor taxonomy or a catalogue of maintenance policies.
  - Assurance does not stay current just because no change is known.
  - Do not assume every relevant dependency can be enumerated or monitored.
  - The two examples sit at different points of the same trade-off. The mark is cheap and exact to check and is relied on as a stop. The report is costly to re-derive, has broad dependencies, and is consumed advisorily.
- **Dependencies:** C1, C2, C3, C4 and C5.
- **Destination:** the thesis is stated in the opening. Section D gives a short synthesis after the two examples, and it must not restate them.

## C7 — Mechanical checking is distinct from semantic review

- **Treatment:** state it, with the definition supplied by the commission.
- **Definition:** a mechanical check derives the result from identified, available inputs, or compares the copy against them.
- **Basis:** source-1: the deterministic validator checks declared completeness, and "Assignment fit is judged during authoring and semantic review". Source-4: when membership is inferred from meaning, "search and review can reveal omissions but cannot prove completeness". Source-2's judgment-based selection is the other half of the contrast. No source gives this exact definition (Gaps), so attribute it to the note, not to a source.
- **Scope and qualifiers:** keep it to one or two sentences. The connect report is not a case where semantic review stands in for a mechanical check that is merely missing. Its result has no fixed rule to check against.
- **Dependencies:** none. It underpins C4, C5 and C8.
- **Destination:** where section B moves into section C, or at the head of section E. It should appear once.

## C8 — Four numbered checking conditions

- **Treatment:** state each condition, with qualifiers. Keep the numbering 1–4 and the recognizable concepts, because dependents cite them by number:
  1. A derivation or comparison rule exists.
  2. The copy and its source can be located.
  3. The source is available at check time.
  4. The checker is sufficiently trustworthy.
- **Framing:** present them as the conditions under which a **mechanical** check is possible. They describe when checking is available and how cheap it is. They do not give a valid/invalid verdict on keeping a copy, and they are not guarantees.
- **Basis:** source-1 meets (1) through (3) for the mark: the one-hop rule plus the participating set, the head path plus `tags:` lines, and validation that reads the participating set. Source-4 supports them with "mechanically queryable", "machine-readable" and "derive it at use time, or require a refresh". For (4), source-1 says only "Validator-enforced". No source discusses checker trustworthiness, so (4)'s basis is the commission.
- **Scope and qualifiers:**
  - Map the connect report onto the conditions in at most a clause: (1) fails, (2) fails, and (3) is limited (I4).
  - Do not state that failing the conditions forbids retaining the copy. It only means the copy cannot be checked mechanically, and reliance is then a risk judgment under C6.
- **Dependencies:** C4, C5 and C7.
- **Destination:** section E, as a compact numbered list.

## C9 — Testing or centralizing a validator lowers assurance cost but does not prove correctness

- **Treatment:** state it with a qualifier, in a sentence or two attached to condition (4).
- **Basis:** the commission only. No source addresses it (Gaps).
- **Scope and qualifiers:**
  - No long regress discussion.
  - Keep the amortization of validator development across artifacts (I7) separate from the amortization of computation across uses of one copy (C1). Either name the difference in one clause or simply avoid merging them.
  - No empirical reliability claim.
- **Dependencies:** C8(4).
- **Destination:** section E, right after the list.

## Scope section content

Destination: `## Scope`. Keep it short and avoid duplicating the body. It contains:

- The two examples are local contracts that illustrate the trade-off. They do not establish prevalence.
- The suppression mechanism is conditional. Harm requires that the suppressed route would actually find more.
- The trade-off is qualitative and has no calibrated thresholds.
- Dependency tracking is often incomplete. Not every dependency can be enumerated or monitored, and the note gives no general refresh rule for broad dependencies.
- Condition (4) has no established measure of checker trustworthiness.

Name real gaps plainly. Do not hedge defensively. Source-status disclaimers that add no qualification relevant to the reader belong in the report, not in the note.

## Decisions reserved for the operator

- **Replacement title:** propose one concise title in the report only. Do not retitle. An illustrative direction, to be decided by the operator: "How often to check a retained derived result depends on checking cost relative to reliance risk."
- **Publication** needs the user's separate approval.
- **Dependents:** do not edit them. In the report, list the classes of dependent rationale that need correction: the checked-or-absent or forbidden-middle rule, the enforce-or-omit regime flip, guaranteed graceful degradation, and automatic omission of judgment-based material. Note specifically source-1's "recomputable, therefore never load-bearing" / "enforced-or-omitted" passage that calls this note the "safety half", and source-4's "the broader rule" cross-reference. State in the report that the role report inspected only 30 of 38 linking files. This figure comes from the commission alone, and the report must not imply a complete dependency audit.
- Create no lasting brief, and edit no indexes or contracts.

## Commitments the note must not make

- No universal valid/invalid or safe/unsafe dichotomy for retained copies. No universal prohibition on unchecked copies. Source-1's "enforced-or-omitted" and "never load-bearing" wording conflicts with the commission and is not to be carried over. The note must not soften that slogan in one place while keeping it universal in another.
- No forbidden-middle claim, no claim of guaranteed graceful degradation, and no claim that judgment-based material is automatically omitted.
- No claim that mechanical checking is free, that every dependency can be enumerated or monitored, or that assurance stays current when no change is known.
- No stretching of source-1's "never correctness" to cover reliance on a present but stale mark (I6).
- No "per unchanged version" rule as a general solution for broad dependencies.
- No refresh interval, risk estimate, prevalence or empirical reliability claim. No claim about how often connect reports are reused or go stale.
- No claim that suggestions carry no risk or that their failure is always loud. No claim that discovery can be re-derived by a fixed rule.
- No claim that a tested or centralized validator is proven correct.
- No source-attributed claim for C2, C6, C7's definition, C8(4), C9 or I4. These rest on inference or on the commission. The note may assert them as its own reasoning but must not cite a source as saying them.
- None of the old examples: compiled memory views, hot-path contract values, duplicated `AGENTS.md.template` files. No cache maxim, repeated asymmetry summaries or unrelated open questions.
- No ADRs as authority, no external literature, no imports of the sources' external links, and no history of this rewrite.
