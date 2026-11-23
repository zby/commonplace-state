# Assessment: Codification and relaxing navigate the bitter lesson boundary

**Proposed purpose (operator named none):** For KB maintainers and agents
deciding whether to commit a rule to code or leave it to a model call: they
should come away with the codify-and-relax claim and the bet framing (each code
extraction bets that what it commits is spec, not accident; relax when scale
makes a general component viable), and should be able to follow it without
decoding repeated caveats or two unmapped names for one distinction.

**Decision:** no stop. The depth 1 reports show several defects, but each can
be corrected by narrowing or bridging one or two sentences. The premise
decomposition finds no `GLOBAL` failure. The thesis (codify for current
leverage, relax on signal or scale, each extraction is a bet) and the order of
the argument stand. These defects go to the operator as claim questions. They
cover most of the bet section, the opening premise and the description, so the
passes are scoped narrowly to the text expected to survive. Two passes are
recommended. Opening-and-title, a Scope section and the compression folds in
the bet section are deferred until the operator has answered the claim
questions, because they would rewrite text those answers will change.

## Ranked changes

1. **Map the regime labels to the opening distinction once.** Cost: one clause
   or a parenthetical in the trade-off paragraph. Pass: `fix-strategy-taxonomy`
   on `prose/source-residue` (finding-15), scoped to the sentence that
   introduces "the arithmetic/vision-feature boundary" and the lead-ins of the
   two regime bullets. Readers meet "exact specs / proxy theories" in the
   opening and then "arithmetic / vision-feature" with a definite article, and
   nothing says these name the same split. Keep both names; the role report
   shows harness ingests rely on the arithmetic/vision-feature split.
2. **State each codification-scope caveat once, and unpack the relaxing
   definition.** Cost: removing two sentences, moving one and splitting
   another. Pass: `readability-and-flow`, scoped to:
   - the opening's last sentence ("This is not a partition…");
   - the codification-definition paragraph;
   - the relaxing-definition sentence;
   - heuristic 1's last sentence ("Merely writing the convention…").

   The model-package-adoption caveat appears three times and the
   prose-convention caveat twice. These repeats sit before the regime
   trade-off (core-claim-obscured, detail-overhang, marginal-value-redundancy,
   compound-bullet). Gather them in the definition paragraph. Move the
   constrains-without-codifying contrast there and link constraining
   (undefined-terms). Split the four-part relaxing definition so the trade-off
   is its own sentence (clause-packing). Keep the hybrid-not-partition point
   and the relaxing paragraph's sentence on what relaxing does not reverse.
3. *(Deferred; not planned)* **Front-load the thesis and gloss the bitter
   lesson in the opening.** This is the synthesis's top item, and it is
   undefined-terms and unidentified-references for "the bitter lesson". It
   belongs to `opening-and-title`, which runs last because it restates a
   settled body. The body is not settled until the claim questions below are
   answered. The opening's premise sentence also carries a claim question.
   Run it after those decisions.
4. *(Deferred; not planned)* **Fold the regime-recap paragraph and the
   duplicate hedge in the bet section.** This is synthesis item 3. Both
   passages carry open claim questions (spec drift; the "same property"
   identity), so a fold now would be rewritten.

## Sentence a hostile reviewer attacks first

"This means codification bets in the arithmetic regime are not merely
safe-for-now; the step-by-step structure that codification encodes is the kind
of regularity that persists under scaling." This sentence turns a finding about
architectural inductive bias inside trained sequence models, on calculator-class
state tracking, into a claim about rules committed to scripts and validators
across the whole arithmetic regime. It states no bridge. The friction, premise,
critique, framing-mismatch, unbridged-cross-domain, epistemic-status-blur and
grounding-alignment reviews all reach this sentence on their own.

## What reads well

The regime bullets and the spec-mining move, from "will these pieces compose?"
to "is this specific pattern load-bearing?", give a reader a concrete,
discriminating test. The edge-detection, FlashAttention and tokenizer
trajectory shows briefly that the movement goes both ways.

## Overclaim candidates: support or divergence

- "practical systems will always be hybrids": **divergence**, keep. The premise
  decomposition found no defeater, and the memory-design note and the
  Wikipedia ingest rely on it.
- "Every code-extraction codification is a bet": the bet is that the extracted
  regularity is spec, not accident. **Divergence**, keep. It is the claim
  dependents most rely on (codify-versus-LLM heuristics, constraining tag,
  codification definition, No Free Lunch and DomainBed ingests).
- "what relaxing reverses is the extraction, not symbolic membership":
  **divergence**, keep; the synthesis says it does distinct work. See the claim
  question on dependents' sense of relaxing.
- "The bitter lesson describes a trajectory, not a law of nature":
  **divergence**, keep.
- The non-identifiability premise: **support**. It may be scoped to the blurry
  zone, but only by the operator (claim question 1).
- The Ebrahimi "persists under scaling" sentence, the epiplexity safety
  sentence, "no working seeing system", the description's "avoids" and the
  "reveal" sentence on relaxing signals: **support**, may be narrowed (claim
  questions).
- Heuristic 2's "survives longer than": **support**; it is stated as a working
  heuristic. Not acted on (see below).

## Claim questions for the operator

Each is a **defect** that one or two sentences would correct unless marked
otherwise. The passes are scoped away from these passages.

1. **Opening premise is unconditioned.** Passage: "Since you can't reliably
   tell which regime you're in until scale tests the distinction". The note
   says the regime cannot be told before scale tests it, yet heuristic 1
   classifies a numerical-contract test as arithmetic-regime in advance. The
   bet section also confines the blurry zone to "most practical codification".
   Both statements cannot hold as written. Fix: scope the premise to the
   blurry zone, or say "often cannot tell without end-to-end evidence, of
   which scale comparisons are one kind". Reports: `report-1`
   (composition-friction-gate), `report-2` (critique-note), `report-3`
   (premise-decomposition-gate). The role report shows
   `bitter-lesson-selects-against-unearned-reach-not-against-structure.md` and
   the Duguid ingest rely on non-identifiability. Scoping it to the blurry zone
   leaves their reliance intact; a stronger change would not.
2. **The Ebrahimi transfer is unbridged and too broad.** Passage: the
   induction-bias paragraph, ending "This means codification bets…". The case
   is a result about model-internal architectural bias, used as evidence about
   code extraction. It is also redundant: the note already defines the
   arithmetic regime as the case where "the spec IS the problem". Fix: restate
   it as evidence that a step-structured inductive bias kept its advantage over
   the tested scale range, bounded to calculator-class state tracking, and
   either state a bridge or call it an analogy. Drop the κ figures (they are
   undefined: notation-opacity, framework-decoration, orphan-references,
   detail-overhang). Reports: `report-1`, `report-2`, `report-3`. Findings:
   unbridged-cross-domain, epistemic-status-blur, framing-mismatch,
   grounding-alignment, kb/theory/COLLECTION ("Origin is not corroboration").
3. **The epiplexity paragraph contradicts itself and the premise.** Passage:
   "High-epiplexity regularities are genuinely structural — codifying them is
   safer…". Two statements cannot both hold. Epiplexity is "learnable
   structure within computational bounds", so it is observer-relative, yet the
   note says it marks patterns that are "not artefacts of the observer's
   computational budget". It also gives an advance criterion, which the
   founding premise denies. Fix: cut it, recast it as an open question, or move
   it to a workshop lead. Recasting keeps the thesis and matches the
   epiplexity ingest's "conceptual check, not yet an engineering rule".
   Reports: `report-1`, `report-3`, `report-4` (synthesis item 2). Findings:
   branch-bloat, conceptual-role-conflation, underspecified-assertions,
   framing-mismatch.
4. **The vision-history contrast is defeated.** Passage: "without a working
   'seeing' system to extract from … with no evidence of successful
   composition". The case: biological vision, through Hubel and Wiesel's
   orientation cells and Marr–Hildreth, was a working system that edge
   detection was partly mined from, and it still failed to compose. Fix:
   narrow it to "no working engineered system on the target task, observed at
   its composed behavior", or name what separates the two kinds of mining. Also
   mark the paragraph as an illustrative historical case (source-residue,
   second item). Reports: `report-2`, `report-3`, `report-1`.
5. **"Spec" drifts between two senses.** Passages: "The bet is that what you
   extracted is genuinely part of the spec" and "In the vision-feature regime,
   the bet is risky: the spec is a theory". In the first, the spec is the
   load-bearing target behavior. In the second, it is the committed
   requirement, which may itself be a proxy. Under one reading the bet's
   success condition is met yet the bet is called risky. Fix: name the two
   senses, or reword the bet's condition. Finding: internal-consistency.
6. **Description and footer overstate spec mining.** The description and the
   spec-mining footer entry say spec mining "avoids" the vision-feature failure
   mode. The body says it "improves the odds" and is "still a bet". Fix: change
   "avoids" to "reduces the risk of". Reports: `report-2`, `report-3`.
   Findings: connection-inflation, misleading-link-text.
7. **Relaxing signals are said to "reveal" accident versus spec.** The linked
   signals note says its signals "shift confidence" and do not detect "the
   theory/spec distinction itself". The footer says they detect "vision
   features", but the body says "accident". Fix: make the signals triggers for
   diagnosis, and make the footer match the body. Findings:
   grounding-alignment, concept-attribution (info), internal-consistency
   (info). The passage also carries item 8.
8. **Extension, which the operator may decline: a third way a bet can lose.**
   The critique argues that classical edge features were real regularities
   (learned networks rediscover them) that lost because fixed, separately tuned
   stages could not adapt with the rest, and that relaxing signals should
   detect this as well as accidents. The claim as scoped stands without it.
   Adding it would sharpen heuristic 3, and the purpose would gain from it,
   because the note's own anchor case is the one this misses. Report:
   `report-2`.
9. **The "same property" identity with the bitter-lesson note.** Passage:
   "That is the same property one case-level conjecture offers as the
   diagnosis…". This note's property is whether a regularity is true (spec or
   accident). The target's property is whether a claim's scope was tested
   (earned reach). Both link texts also describe the target as a hedged,
   case-level, proxy-scope conjecture, but the target claims its criterion
   universally under the title "The bitter lesson selects against unearned
   reach, not against structure". Fix: identify the assessed-scope property, or
   say an accident is one way to have unearned reach; then align the link
   texts. Findings: concept-attribution, misleading-link-text, mannered-prose
   ("survivor's"), clause-packing (first item), marginal-value-redundancy
   (duplicate hedge).
10. **Choice, no defect shown: the title.** Title-body-alignment suggests "Code
    extraction and relaxing…". It is not ranked first. A title change would
    also touch 41 inbound links and the KB's use of this note as the home of
    "relaxing" across all codification.
11. **Choice, no defect shown: dependents' sense of relaxing.** The role report
    shows `definitions/codification.md`, `definitions/constraining.md`,
    `definitions/representational-form.md` and
    `continual-learning-requires-governing-behaviour-changing-writes.md` use
    relaxing more broadly than "reverses the extraction, not symbolic
    membership", including relaxing back into prose.
    `orchestration-strategies-and-run-state-have-opposite-persistence.md`
    cites the note for a net-negative claim it does not make. Either the note's
    restriction or those dependents should change. The passes keep the note's
    sentence. Role report run directory:
    `kb/reports/state/review/runs/v2/revise/kb/theory/codification-and-relaxing-navigate-the-bitter-lesson-boundary/20261120T091143Z/role`.

### Stale qualifications against the body or targets

- The relaxing-signals footer says "vision features"; the body says "accident"
  (item 7).
- The bitter-lesson link texts call the target a "case-level conjecture" and
  "may explain"; the target makes a universal earned-reach claim (item 9).
- The footer link text "fixed artifacts split into exact specs and proxy
  theories" states an artifact-level partition. The target places exactness
  and proxyhood on links of a named path (misleading-link-text).
- The Sources annotations repeat the Ebrahimi "permanent" and the epiplexity
  "grounds" claims. Update them with items 2 and 3.

## Findings and proposals not acted on

- **notation-opacity, framework-decoration, orphan-references (κ),
  detail-overhang (κ item):** these fall in the Ebrahimi paragraph, under
  claim question 2.
- **undefined-terms, unidentified-references ("the bitter lesson"):** deferred
  to `opening-and-title` after the claim questions. "Symbolic membership" sits
  in a must-keep sentence under choice 11. "Author/survivor" is under item 9.
  "Constrains" is handled by the readability scope.
- **connection-inflation:** the footer's spec-mining and relaxing-signals
  entries are under items 6 and 7.
- **kb/theory/COLLECTION:**
  - The `foundation` label, the unlabeled footer entries and the
    `grounds`-labeled external Sources are link-label conformance. No listed
    pass owns that; apply it as a direct edit after items 2, 3, 6 and 7.
  - The corroboration framing is part of items 2 and 3.
- **kb/types/note (Scope section):** a structural addition, and the limits it
  would gather are under items 1–3. Revisit after the operator decides them.
- **title-body-alignment:** choice 10.
- **branch-bloat, core-claim-obscured (κ and relaxing-late items),
  marginal-value-redundancy (regime recap, duplicate hedge, Ebrahimi
  restatement):** these fall in claim-question passages or are deferred to
  opening-and-title. The opening-caveat and model-package items are in the
  readability scope.
- **marginal-value-redundancy (maintenance-cost clause in the arithmetic
  bullet, info):** it guards against reading "safe" as "free"; keep it.
- **mannered-prose:** "survivor's" is under item 9. "Maximum disadvantage" is
  info and under item 4.
- **source-residue, second item (vision researchers):** under item 4. Only the
  label-mapping item is planned.
- **grounding-alignment:** its warn items are under items 2, 3 and 7. The info
  items (path relativity, "case-level") are under item 9 and the stale-link
  list.
- **semantic/conceptual-role-conflation, epistemic-status-blur,
  underspecified-assertions, framing-mismatch, unbridged-cross-domain:** items
  2 and 3. Info items on heuristic 2's comparative, heuristic 3's comparison
  basis and the regime object are recorded but not planned: heuristics are
  marked as working heuristics, and heuristic 1 resolves the regime object.
- **clause-packing:** the relaxing-definition item is planned. The identity
  sentence is under item 9. The from/to parenthetical is info, so it is not
  planned.
- **compound-bullet:** the heuristic 1 item is planned with readability. The
  footer hedge item is info and sits in a stale-link entry.
- **Extensions not recommended** (the purpose does not ask for this coverage):
  - premise decomposition: relaxing cost / Hyrum's law as an unstated
    condition of heuristic 1;
  - premise decomposition: heuristic 3's diagnostic precondition;
  - premise decomposition: the what-versus-how counterexamples;
  - premise decomposition: narrowing the bidirectional trajectory to
    arithmetic-regime pieces;
  - the role report's untaken No Free Lunch paragraph;
  - the critique's secondary epiplexity-estimation objection.

  The diagnostic precondition for heuristic 3 sits next to item 8, and the
  operator may fold it in there.
