# Reconstruction: checking retained results as a cost–risk trade-off

Basis for the commissioned rewrite of `kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`. No write brief was supplied; the commission is the only statement of intent. Sources: S1 `kb/types/tag-readme.md`, S2 `kb/types/connect-report.md`, S3 `kb/theory/frontloading-spares-execution-context.md`, S4 `kb/theory/indexes-lower-recall-when-they-suppress-retrieval-that-would-find-more.md`.

## Support

### A. Retaining a derived result saves work; reuse amortizes it

- S3 §"The context saving", para 1: executing a procedure during a task can add tool calls, search results, reasoning traces, interpretation work and sometimes extra LLM calls; "The cost recurs on every invocation."
- S3 §"The context saving", para 2: the relevant comparison is *realized* execution context, not instruction size; the saving is largest on "the discovery, derivation, and indirection the call no longer performs"; on raw volume it saves only when the inserted result is smaller than what it replaces. A pointer can be shorter than a result but cost more ("read file X").
- S3 §"The context saving", para 3 (last sentence): pre-computation "is also economic when one build-time, install-time, or session-start computation saves many runtime calls from repeating the same work." This is the repeated-work amortization the commission asks for. S3 states it for frontloading into LLM calls, not for retained artifacts generally.
- S3 §"The context saving", para 4: discovery avoidance — pre-resolving what is known replaces runtime determination.
- S3 §"What to frontload", para after list ("Possibility is not enough…"): frontload when the pre-step removes repeated discovery; context saving "is not the only cost in play"; freezing a situation-dependent value can save context but still be wrong because it "commits a guess that the executor could have read off the live state." Two pulls in one decision — direct support for a trade-off framing rather than a rule.

### B. Validity window and refresh

- S3 §"What to frontload", "A frontloaded artifact also needs a validity window: the span during which its pre-computed inputs remain accurate." If inputs may change before use, include lineage, timestamp, or regeneration-instruction information "to support refresh." Lineage "states what the artifact depends on and when it must be regenerated."
- S3 gives no refresh interval and no claim that lineage is always complete or obtainable.

### C. A false trusted copy can suppress the work that would expose it (conditional mechanism)

- S4 opening para: an incomplete index lowers recall relative to no index "when it appears exhaustive and suppresses retrieval that would have produced greater task-relevant coverage"; comparison holds consumer, task, relevant set and endpoint fixed.
- S4 para 2: "The failure is therefore in control flow, not merely in missing content." The index "ends discovery before the operation that could reveal additional current items."
- S4 para 3: "This is a conditional mechanism, not a prevalence claim." It does not establish that consumers usually stop or that fallback usually finds more.
- S4 para 4: the mechanism applies to "any artifact a consumer treats as exhaustive, including specs, documentation, plans, and curated lists."
- S4 §Scope para 1: requires the suppressed retrieval to have "greater realized task-relevant coverage"; a broader surface is insufficient if the actual operation would find nothing more.
- S4 §Scope para 2: an imperfect index "may still have greater overall utility" when it is the only route or when speed/orientation outweigh omissions; the claim concerns recall on the suppressed route, "not global visibility or total utility."
- S4 §Defenses, last para: a consumer may choose an incomplete index for speed, but loss of recall "should be an explicit trade-off rather than a hidden consequence of false completeness."

### D. Staleness arises from separate update paths

- S4 §"Staleness arises…": a derived view drifts when items are added, removed, renamed or reclassified without a matching view update; "the source set and its navigation surface have separate update paths." The question is whether every relevant source change reaches the view "through a reliable synchronization path."

### E. Example 1: the completeness mark

- S1 §Frontmatter: `complete: true` means every artifact carrying the tag across participating collections is reached from the head in one hop. "Validator-enforced; readers may skip the by-tag `rg` sweep." This is the authorized stopping shortcut (skipping a membership search).
- S1 §Scope: membership ranges over the collections declared in `kb/tags/COLLECTION.md` `participating:`, "and over nothing else" — the inputs are identified and locatable.
- S1 §Frontmatter, para 2: the mark is "a **validated cache** of tag membership, which the scoped `rg` sweep … always recovers" — the fallback recomputation exists and is defined.
- S1 §Frontmatter, para 2: "a false mark tells exhaustive consumers to stop looking while members are still out there" (citing S4) — the suppression mechanism instantiated.
- S1 §"Maintaining the mark": "Enforcement is reactive": writing a note does not require touching a head; "the validator queues the gap when the marked head is next validated." A clean validation of one collection does not clear a head; validate `kb/tags/` after tagging anywhere in the participating set. This supports reactive enforcement, not an always-current guarantee: between validations a mark can be false.
- S1 §Authoring Instructions, last bullets: "an unenforced version of that claim decays silently into the stale-index failure"; assignment fit is a semantic-review matter — the validator "does not establish that an artifact fits the tag's meaning." So the mechanical check covers membership-reach given tags, not tag correctness.
- S1 §"Exits": drop to selective is the default exit; "readers fall back to `rg`."

### F. Example 2: the connect report

- S2 §Authoring Instructions: every connection section describes "candidate edges for a future writer to act on"; readers "should treat its contents as suggestions to evaluate, not as state already in the KB." It "is not itself a durable knowledge claim."
- S2 §"Connection Standards": candidates must pass an articulation test; labels are judged from the target's "actual claim, evidence, caveats, and collection/type contract" — candidate assessment is judgment.
- S2 §"Discovery Trace": the report records which indexes were read, which searches were run, scores, candidates and reasons — the inputs of one discovery pass are recorded, which bears on what is checkable (trace structure, link resolution) versus what is judgment.
- S2 §"Quality Gates": "Every candidate link must resolve. `commonplace-validate` checks this, along with the required sections and frontmatter fields." So some properties of a judgment-produced result are mechanically checkable, distinct from re-deriving its substantive judgment.
- S2 §Metadata: `depth: quick | standard | deep` "to match the discovery pass that was actually run" — the result depends on the pass chosen.
- S2 §Edge Cases: "If traversal reveals unconnected notes, flag them but do not treat them as part of the current connect result."

## Inference

1. **Reuse benefit and amortization (rests on A).** A retained derived result spares the recurring discovery/derivation cost on each later use; one production amortizes over many uses (S3 para 3). Inferred for the note's general case: S3 argues it for frontloading into calls; extending it to retained KB artifacts (marks, reports) is an application, not stated by S3.
2. **Checking by full recomputation on every use largely defeats the saving (rests on A, E).** If the check is the same derivation the copy replaced (e.g. running the `rg` sweep every time the mark is read), the recurring cost S3 identifies returns. No source states this directly; it follows from A plus the existence of the sweep as the mark's recomputation (S1). The commission adds that verification cheaper than derivation can still save work when checked on every use; no source states that relation either.
3. **Checking frequency is a cost–risk trade-off (rests on A, B, C).** S3 frames frontloading as weighing context saving against wrongness from frozen values; S4 frames accepting an incomplete index as an explicit utility trade-off. Together: how often to check depends on check cost relative to the risk of relying on stale or wrong content. Qualitative only — no source gives calibration.
4. **Why the mark's check is attractive (rests on E).** The mark's contract defines the derivation (one-hop reach over tagged artifacts), names the inputs (participating collections, tags, head links) and has them locally available to the validator; and it authorizes a stop, so a false mark triggers mechanism C. A cheap deterministic check and a stop-authorizing claim together make enforcement attractive. S1 makes enforcement reactive, so assurance holds as of last validation, not continuously.
5. **The mark's check does not establish checker trustworthiness (rests on E; commission).** S1 asserts validator enforcement but nothing in S1 shows the validator is correct; the fourth condition is not supplied by any source for the mark.
6. **Why reuse of a connect report can be reasonable (rests on F, A, C).** The report is explicitly candidate-only and evaluated before action (S2), so its consumer does not stop on it as exhaustive in the way S1's mark authorizes. Rerunning discovery has cost (S2 trace requirements, depth levels). Reuse can be reasonable when rerunning costs more than the accepted risk. But S2 does not say its omissions are harmless: if a consumer treats a report as the full set of connections, mechanism C could apply (S4 para 4 extends the mechanism to any artifact treated as exhaustive). Its failure need not be loud.
7. **Broad dependencies of the connect report (rests on F, D).** A discovery pass ranges over indexes and searches across the KB (S2 trace), so material added anywhere it searches could change a renewed result. Combined with D (separate update paths), tracking a sufficient dependency set — including newly added relevant material — is hard. Sources do not show it is impossible to enumerate KB files; the difficulty is sufficiency, per commission.
8. **No known change does not establish freshness (rests on B, D, E).** S3's validity window and S4's separate-update-path account imply that absence of a known change is not evidence the inputs are unchanged unless every relevant change reaches the checker; S1's reactive enforcement shows a mark can be stale until next validation.
9. **Numbered conditions (rests on E, S3 B, S4 §Defenses "Check retained completeness claims").** (1) derivation/comparison rule — S1 defines one-hop reach; S4 says completeness claims should be "machine-readable and checked against the canonical set". (2) locatable copy and source — S1 §Scope, frontmatter field. (3) source available at check time — S1's validator reads the participating collections; S3's lineage/refresh requirement. (4) sufficiently trustworthy checker — no source supports this; only assumed by S1's "validator-enforced." Testing/centralizing a validator lowering assurance cost is not stated by any source.
10. **Mechanical check vs semantic review (rests on E, F).** S1 separates validator checks from assignment fit judged in review; S2 separates mechanically checked properties (link resolution, sections) from judgment about candidates. Assessing candidates calls for judgment; a judgment result can still have checkable properties.

## Conflicts

- **S1 states the categorical rule the commission retires.** S1 §Frontmatter para 2: "any future mark must keep both: **recomputable, therefore never load-bearing** — dropping the mark costs one recomputation, never correctness; and **enforced-or-omitted**." It also names the target note as "the safety half" of the mark's theory. The commission excludes a universal enforce-or-omit slogan and guaranteed graceful degradation. Resolution within scope: S1's statement is a local requirement on marks in this type, which the commission says S1 supports only as "the concrete example, not a universal prohibition." The note can use the mark as an enforced case without generalizing. S1 itself is a dependent whose rationale wording ("safety half", "enforced-or-omitted") would need correction; the reconstruct step does not edit it.
- **S1 "never correctness" vs S4 mechanism.** "Dropping the mark costs one recomputation, never correctness" holds only if consumers then actually run the fallback; S4 §Defenses last para notes the system "must still deliver the signal and make the consumer honor it." Not a direct contradiction, but S1's guarantee rests on a consumer-behavior assumption S4 flags.
- **S4 cites the target note's old categorical rule.** S4 §Defenses "Check retained completeness claims" ends: "the broader rule that [a derived copy of recomputable truth must be checked or absent]". S4's own body is conditional and allows explicit trade-offs (§Scope para 2), which agrees with the commission rather than the categorical rule. S4 is another dependent whose rationale sentence would need correction.
- **S4 "A failed check must invalidate the claim"** is stated as a defense for exhaustiveness claims; compatible with the commission if confined to stop-authorizing claims under check, not extended to all retained copies.

## Scope

- S3's amortization argument is about frontloading inputs into LLM calls and context budget; applying it to persisted KB artifacts is a transfer. S3's cited external evidence (Machine Studying footer) is excluded by commission.
- S4's mechanism is conditional: it requires that the consumer stops on the view and that the suppressed route would find more at the fixed endpoint; it makes no prevalence claim, and allows that an imperfect view can have greater overall utility.
- S1's guarantees hold over the declared participating collections only and are reactive (as of last validation of `kb/tags/`); they cover one-hop reach given tags, not correctness of tag assignment.
- S2 describes one report type in this KB; its candidate-only status is a contract on readers, not evidence about how consumers behave in practice.
- All support is qualitative; no source gives costs, risk magnitudes, refresh intervals, or reliability rates.

## Gaps

- **Condition 4 (trustworthy checker):** no source supports that the mark's validator, or any validator, is trustworthy; nor that testing or centralizing a validator lowers assurance cost without proving correctness. The note would state this as reasoning, not sourced fact.
- **Verification cheaper than recomputation:** no source distinguishes verification from derivation or says checking each use can still save work when verification is cheaper.
- **"Full recomputation on every use defeats the saving":** follows from S3 but is not stated by any source for retained copies.
- **Connect report's broad dependencies:** S2 does not state that new material anywhere may change a renewed search, nor anything about reuse between runs or staleness; this is inferred from the trace/search structure. S2 does not say reuse is reasonable under any cost condition.
- **Connect report failure mode:** no source states whether its omissions fail loudly or silently.
- **Distinction between computation amortization across uses and validator-development amortization across artifacts:** no source discusses the latter.
- **Undefined terms in the sources:** "mechanical check", "retained result"/"derived copy", "risk of reliance", "assurance" are not defined in any source. "Validity window" and "lineage" are defined in S3 (lineage via a linked definition not in this source set). "Validated cache" appears in S1 without definition beyond its two properties.
- **Dependents:** the sources show two dependents citing the old rule (S1 §Frontmatter "safety half … enforced-or-omitted"; S4 §Defenses). The commission says a role report inspected 30 of 38 linking files; that report is not in the source set, so no complete dependency audit is available here.
- **Replacement title:** no source supplies one; it is for the author's report.
