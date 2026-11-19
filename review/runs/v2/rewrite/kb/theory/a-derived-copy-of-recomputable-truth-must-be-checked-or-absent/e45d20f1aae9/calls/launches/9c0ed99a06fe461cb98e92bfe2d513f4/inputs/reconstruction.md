# Reconstruction: checking retained results as a cost–risk trade-off

Basis for the commissioned rewrite of
`kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`.
No brief was supplied; the commission is the only statement of intent. The
commission and the source list agree on the four sources and their roles.
No contradiction was found within the commission.

Commitments the contribution needs (from the commission's "Intended
contribution" and "Must keep"):

- C1 Retaining a derived result can save work; reuse amortizes producing and checking it.
- C2 Full recomputation on every use largely defeats that saving.
- C3 A false trusted copy can suppress work that would expose its error (conditional mechanism).
- C4 Completeness-mark example: permits skipping a membership search; deterministic check; reactive enforcement; fallback.
- C5 Connect-report example: candidate links for evaluation; broad dependencies; reuse can be reasonable when rerunning costs more than the accepted risk.
- C6 Checking frequency depends on checking cost relative to the risk of relying on stale or incorrect information.
- C7 Mechanical checking (derive/compare against identified available inputs) is distinct from semantic review.
- C8 Four numbered checking conditions: (1) derivation/comparison rule, (2) locatable copy and source, (3) source available at check time, (4) sufficiently trustworthy checker.
- C9 Testing or centralizing a validator lowers assurance cost but does not prove correctness.

## Support

### C1 — Reuse saves work and amortizes its production

- `kb/theory/frontloading-spares-execution-context.md` (source-3), "The context saving": executing a procedure during a task can add tool calls, search results, reasoning traces and extra LLM calls beyond its result; "The cost recurs on every invocation."
- source-3, "The context saving", third paragraph: frontloading "is also economic when one build-time, install-time, or session-start computation saves many runtime calls from repeating the same work." This is the source's amortization statement: one computation, many uses.
- source-3, "The context saving", second paragraph: the saving is largest on "the discovery, derivation, and indirection the call no longer performs"; on raw volume it saves only when the inserted result is smaller than what it replaces. Qualifier: inlining content the call would load anyway moves tokens rather than removing them.
- source-3, "Discovery avoidance" paragraph: pre-resolving values means the agent "does not spend runtime context determining them."
- `kb/types/tag-readme.md` (source-1), Frontmatter, `complete: true`: the mark lets "readers ... skip the by-tag `rg` sweep." This is a concrete instance of retained results saving a search.
- source-1, Frontmatter, the paragraph after the bullet: the mark is "a **validated cache** of tag membership, which the scoped `rg` sweep ... always recovers."

Scope of source-3: it is about pre-computing inputs inserted into a later LLM call (frontloading). The commission asks to use its argument, not its external study claims (the Machine Studying footer entry).

### C2 — Recomputing on every use defeats the saving

- No source states this directly. source-3 supports the premise that the saving consists of discovery and derivation the consuming call "no longer performs" ("The context saving"). See Inference I1.

### C3 — A false trusted copy can suppress the work that would expose it

- `kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md` (source-4), opening paragraph: an incomplete index lowers recall relative to no index "when it appears exhaustive and suppresses retrieval that would have produced greater task-relevant coverage." The comparison holds consumer, task, relevant-item set and endpoint fixed.
- source-4, second paragraph: "The failure is therefore in control flow, not merely in missing content." The index "ends discovery before the operation that could reveal additional current items."
- source-4, third paragraph: "This is a conditional mechanism, not a prevalence claim." It does not establish that consumers usually stop or that fallback usually finds more.
- source-4, fourth paragraph: the mechanism applies to "any artifact a consumer treats as exhaustive, including specs, documentation, plans, and curated lists."
- source-4, Scope: the claim requires the suppressed retrieval to have "greater realized task-relevant coverage at the fixed endpoint"; a fresher corpus is not enough if the actual operation would retrieve nothing more.
- source-4, Scope: "An imperfect index may still have greater overall utility when it is the only discovery route or when speed and orientation outweigh omissions." The claim concerns recall on the suppressed route, "not global visibility or total utility."
- source-4, Defenses, last paragraph: "A consumer may choose an incomplete index for speed or orientation, but any resulting loss of recall should be an explicit trade-off rather than a hidden consequence of false completeness."
- source-1, Frontmatter: "a false mark tells exhaustive consumers to stop looking while members are still out there."

### C4 — Completeness mark

- source-1, Frontmatter: `complete: true` means every artifact carrying the tag, across participating collections, is linked from the head or carries a tag whose head is linked: "the head reaches every member in one hop. Validator-enforced; readers may skip the by-tag `rg` sweep."
- source-1, Scope: membership ranges only over the collections declared in `kb/tags/COLLECTION.md` `participating:`. This is the identified, enumerable input set for the check.
- source-1, Frontmatter, after the bullet: the mark is recomputable from the scoped `rg` sweep; "dropping the mark costs one recomputation, never correctness."
- source-1, "Maintaining the mark": "Enforcement is reactive ... writing a note does not require touching any head; the validator queues the gap when the marked head is next validated." Also: a clean validation of one collection does not clear a head; `kb/tags/` must be validated after tagging anywhere in the participating set.
- source-1, Exits: (1) drop to selective, where "readers fall back to `rg`"; (2) split with overlap; (3) retirement is never a size remedy.
- source-1, Authoring Instructions: do not hand-write a complete listing or claim coverage without declaring `complete: true`, because "an unenforced version of that claim decays silently into the stale-index failure."
- source-1, Authoring Instructions: the validator "does not establish that an artifact fits the tag's meaning". Assignment fit is semantic and is judged in authoring and review. The mark's check covers declared tags, not the correctness of tagging.
- source-4, Defenses, "Derive exhaustive views from canonical membership" and "Check retained completeness claims": when membership is mechanically queryable, derive or check against the canonical set. A failed check must invalidate the claim. "Repair, recomputation, fallback, and explicit reclassification as partial are all valid responses."

### C5 — Connect report

- `kb/types/connect-report.md` (source-2), Authoring Instructions: "Every connection section describes candidate edges for a future writer to act on, not edges already encoded anywhere." Readers "should treat its contents as suggestions to evaluate, not as state already in the KB."
- source-2, Authoring Instructions: a connect report "records evidence for future KB authoring; it is not itself a durable knowledge claim."
- source-2, Connection Standards: candidates pass an articulation test and a judgment of whether an agent "gains something concrete by following the link"; labels are chosen by reader-need; a target's capacity to carry a load-bearing label is judged "from its actual claim, evidence, caveats, and collection/type contract." This makes discovery judgment-based, not a fixed derivation rule.
- source-2, Discovery Trace: the report records actual queries, scores, indexes read and candidates kept or rejected. It retains the record of a discovery run, not a recomputable value.
- source-2, Edge Cases: "If traversal reveals unconnected notes, flag them but do not treat them as part of the current connect result." Also: report no-connections findings with the indexes and searches checked.
- source-2, Metadata: `depth: quick | standard | deep` matches the pass "actually run". Discovery effort varies.

Broad dependency (new material anywhere can change a renewed search) is not stated in source-2; see Inference I4.

### C6 — Checking frequency as cost relative to risk

- source-4, Scope and Defenses (cited under C3): utility of an imperfect view can outweigh omissions; loss of recall should be an explicit trade-off.
- source-3, "What to frontload", last paragraph: "context saving is not the only cost in play"; freezing a situation-dependent detail "can save context. But it can still be wrong because it commits a guess that the executor could have read off the live state. Saving context and forfeiting that runtime advantage are two pulls in the same decision."
- source-3, "What to frontload": a frontloaded artifact "needs a validity window: the span during which its pre-computed inputs remain accurate"; if inputs may change, include lineage, timestamp or regeneration information "to support refresh."

No source gives a general cost-versus-risk rule for checking frequency. See I3 and Gaps.

### C7 — Mechanical checking versus semantic review

- source-1, Authoring Instructions: "Assignment fit is judged during authoring and semantic review. The deterministic validator checks head existence, structure, links, weight, and declared completeness."
- source-4, Defenses, "Scope claims that depend on semantic judgment": "When membership is inferred from meaning rather than declared in queryable data, search and review can reveal omissions but cannot prove completeness."
- source-2, Connection Standards (judgment-based selection), cited under C5.
- source-3, "Frontloading vs codification": frontloading becomes codification when "a symbolic artifact with formal semantics or assigned consequences consumes the result", such as a validator input. This is adjacent, not a definition of mechanical check.

### C8 — The four checking conditions

- (1) Derivation/comparison rule: source-1 Frontmatter (the one-hop reachability definition) together with source-1 Scope (the participating set) gives an exact rule. source-4 Defenses: "When membership is mechanically queryable."
- (2) Locatable copy and source: source-1 gives the head's path (`kb/tags/<tag>-README.md`, Authoring Instructions), the mark's frontmatter field, and `tags:` lines on artifacts in declared collections (Scope). source-4 Defenses: the completeness claim "should be machine-readable."
- (3) Source available at check time: source-1, "Maintaining the mark", where validation reads the participating set and must be rerun on `kb/tags/` after tagging anywhere. source-4: "Derive it at use time, or require a refresh to finish before asserting completeness."
- (4) Trustworthy checker: source-1 says "Validator-enforced". No source discusses checker trustworthiness. See Gaps.

### C9 — Validator testing or centralization

- No source addresses this. See Gaps.

## Inference

- I1 (C2). If the retained result's value is the discovery and derivation a later call "no longer performs" (source-3, "The context saving"), then a check that reruns the full derivation on every use performs that work again, and that use keeps little of the computational saving. The commission states this directly. The sources supply only the premise. A cheaper verification, such as a comparison rather than a rederivation, would keep more of the saving. No source describes such a verification, so the note can only define the distinction. The cost of loading the copy into context is separate from the cost of computing it (source-3: inlining content that would be loaded anyway "moves those tokens earlier"). So verification cost and context-loading cost may differ, as the commission says.
- I2 (C3, C4). The completeness mark is a case of source-4's mechanism: it licenses a stop (source-1: "readers may skip the by-tag `rg` sweep"), so a false mark is exactly a trusted exhaustive view that suppresses a retrieval (`rg`) that would find more (source-1: "members are still out there"). This rests on source-1 Frontmatter and source-4's opening and second paragraphs. Under source-4 Scope, harm requires that the suppressed `rg` sweep would actually find more for the task.
- I3 (C6). Combining source-3's validity-window and two-pulls paragraphs with source-4's explicit-trade-off and utility Scope gives a qualitative trade-off. A retained result is worth relying on to the extent that its saving exceeds the expected cost of stale or wrong reliance. Checking is worth paying for when it costs less than the risk it removes. This is an inference; no source states it as a rule for checking frequency. The commission asks for a qualitative trade-off, not a calibrated policy.
- I4 (C5). The connect report's discovery surfaces are KB-wide: curated heads, titles, descriptions, body search and link-following (source-2, Discovery Trace, surface identifiers). It follows that material added anywhere these surfaces reach can change what a renewed search finds, so the report's dependencies cannot be enumerated as a fixed input set. That breaks condition (2) and limits condition (3) as source-1's case meets them. This rests on source-2 Discovery Trace and Connection Standards. The sources do not state it.
- I5 (C5, C3). The report is marked "suggestions to evaluate" (source-2). A consumer that treats it as candidates does not stop discovery on its authority the way a `complete` mark licenses a stop (source-1). So source-4's suppression mechanism bites less directly. But the commission forbids inferring that suggestions carry no risk or fail loudly. A consumer that relies on a stale report in place of renewed discovery can still miss connections, and nothing in the report signals that miss (source-2 has no freshness or invalidation field). The final point rests on the absence of such a field in source-2's Metadata. It is an inference from omission.
- I6 (C4). Reactive enforcement (source-1, "Maintaining the mark") means the mark can be false between a tagging change and the next validation of `kb/tags/`. The guarantee is "checked when validated", not "always current". Source-1's fallback ("dropping the mark costs one recomputation, never correctness") holds only for consumers that do fall back. A consumer that trusts a stale mark before validation runs has no such protection. This rests on source-1's "Maintaining the mark" and Frontmatter, combined with source-4's control-flow claim.
- I7 (C8, C1). Condition (4), together with the checker's own cost, is amortized across every artifact it checks, not across uses of one copy. That distinction is what the commission asks the note to keep apart from computation amortization. No source states this. It is offered only as the commission's framing.

## Conflicts

- source-1 (Frontmatter, after the bullet) states a universal design rule: any mark must be "**recomputable, therefore never load-bearing**" and "**enforced-or-omitted**". It names the target note as the "safety half". source-4 (Defenses, "Check retained completeness claims") calls the target note's old title "the broader rule". Both sources therefore present the categorical checked-or-absent rule that the commission explicitly replaces with a cost–risk trade-off and forbids preserving ("Do not preserve an enforce-or-omit slogan as universal"). source-4's own Scope and Defenses also concede utility trade-offs for imperfect views, so source-4 is internally compatible with the commission's direction. Its cross-reference sentence is not. No source settles this conflict. The commission authorizes the new direction. The dependent wording in source-1 and source-4 belongs in the report's dependent-correction list; it must not be edited here.
- source-1 says the mark's absence "costs one recomputation, never correctness". The commission says not to assume that assurance stays current because no change is known, and not to invent an always-current guarantee. These do not conflict directly, because source-1's claim concerns dropping the mark, not trusting it. But a writer should not stretch "never correctness" to cover reliance on a present but stale mark (see I6).

## Scope

- source-1 holds for one local contract: tag membership over the declared participating collections, checked by the Commonplace validator. It shows that the four conditions can be met. It does not show they are generally met, and it does not support a universal prohibition (commission role).
- source-2 is a type contract. It shows that the report is advisory and judgment-based. It says nothing about how often reports are reused, how stale they get, or what failure costs.
- source-3's argument concerns pre-computed inputs to a later LLM call and context budget. Its amortization statement is qualitative ("saves many runtime calls"). Its soft-degradation evidence establishes possibility, "not its prevalence". Its external study claim is excluded by the commission.
- source-4 is explicitly conditional and non-prevalence. Harm requires that the suppressed route would actually find more at a fixed endpoint, and the claim concerns recall on that route, not total utility.
- None of the sources gives an empirical reliability, a refresh interval or a risk estimate. The commission forbids inventing them.

## Gaps

- C2: no source states that full recomputation on every use defeats the saving. This is supported only by inference (I1) and by the commission's direction.
- C6: no source gives a general rule that checking frequency depends on checking cost relative to reliance risk. The rule is assembled from source-3 and source-4 (I3) and must be presented as a qualitative trade-off.
- C5: no source states that a connect report's validity depends on material anywhere in the KB, or that reusing a report between reviews is reasonable when rerunning costs more than the accepted risk. These rest on I4 and the commission's "Current direction" (the operator's acceptance in practice).
- C8 (4) and C9: no source discusses checker trustworthiness, validator testing, centralization, or the fact that a tested validator is not proven correct. The commission's framing is the only basis.
- C7: no source defines "mechanical check" as deriving or comparing against identified available inputs. The closest material is source-4 ("mechanically queryable", "checked against the canonical set") and source-1 ("deterministic validator"). The commission supplies the definition. The distinction between verification and recomputation is also unsupported by any source.
- Amortization of validator development across artifacts versus computation amortization across uses (I7): unsupported. The commission names the distinction only to keep the two apart.
- Undefined terms in the sources: "retained result" and "derived copy" (neither source defines a general term; source-1 uses "validated cache"); "recomputable truth"; "assurance"; "risk" in the reliance sense. "Validity window" is defined in source-3 ("the span during which its pre-computed inputs remain accurate"). "Lineage" is linked but not defined in the supplied text.
- Replacement title: no source proposes one. The report must propose it (commission, Reserved decisions).
- Dependent audit: only source-1 and source-4 among the supplied inputs cite the note. The sources do not support the commission's statement that the role report inspected 30 of 38 linking files; it comes only from the commission.
