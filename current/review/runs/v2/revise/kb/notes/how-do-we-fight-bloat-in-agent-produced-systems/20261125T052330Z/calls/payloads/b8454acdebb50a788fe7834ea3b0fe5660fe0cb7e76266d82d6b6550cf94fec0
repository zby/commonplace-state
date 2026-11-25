# Assessment: How do we fight bloat in agent-produced systems?

**Proposed purpose (operator named none):** A Commonplace maintainer or agent deciding how to control bloat should be able to tell what Commonplace does against bloat today, what is only held as theory, and which problems remain open, with each claim no stronger than its evidence.

**Recommendation: stop before any pass.** The highest-value change is a rewrite of the Current answer section and correction of several claims across the note. That is a claim change, not text work, so the passes cannot make it.

## Ranked changes

1. **Separate the mechanisms Commonplace runs from the theory it holds in Current answer.**
   - Cost: a rewrite of the section's lead and of at least three of its five bullets.
   - Pass: none. This is a claim rewrite.
   - Kind: defect.
   - The lead "Commonplace currently counters bloat with five partial mechanisms" supports two readings that the note's own wording allows (`semantic/conceptual-role-conflation`, finding-7):
     - (a) Commonplace runs five practices, gates or procedures.
     - (b) Commonplace's KB holds five accounts that would counter bloat if applied.
   - The two readings lead to different conclusions about the retirement condition ("relies on periodic manual sweeps and ad-hoc restraint"). Under (a) the query is closer to retiring than under (b).
   - Evidence that the bullets do not all report running mechanisms:
     - The value-gate bullet says "without a value gate, valid redundant artifacts still accumulate". It links an open standing query, and no operating gate is named (critique report-2; friction report-1, UNSUPPORTED; premise report-3, DOUBTFUL).
     - The retirement-path bullet presents an "operative retirement path". The Unsettled bullet "Missing triggers for retirement" then says the triggers are missing (friction report-1, THIN).
     - The scaffolding bullet cites a note whose main claim is that structure recurs at the frontier. That note gives no retirement procedure; according to the critique, it hands candidate detection to a relaxing-signals note that is not linked here (report-2).
   - The critique's fix splits the section into operative practices and guiding doctrine, or moves the value-gate bullet to Unsettled. Either way the section changes what it claims and how it is organised, so the fix goes beyond sharpening one or two sentences.
2. **Correct the claims that outrun their evidence in Stakes and Unsettled.**
   - Cost: one or two sentences each.
   - Pass: none. Each is a claim change.
   - These are listed under Claim questions below. Taken together with item 1, they leave few passages a pass could safely touch.
3. **Bring the "software defenses fall short" thesis forward and join it to the reachability bullet.**
   - Cost: reordering Stakes and adding one cross-reference.
   - Pass: readability-and-flow, after the rewrite.
   - Kind: choice (synthesis report-4, opportunity 2). No defect is shown.
4. **Rebalance the brevity-pressure bullet around its open question.**
   - Cost: shortening one bullet and placing the log conjecture deliberately.
   - Pass: readability-and-flow, after the rewrite.
   - This overlaps with claim questions C5 and C6, so the claim decisions come first (synthesis report-4, opportunity 1; `structural/compound-bullet`; `sentence/clause-packing`).
5. **Gloss the undefined terms and identify Commonplace on first mention.**
   - Cost: a short gloss beside each term.
   - Pass: fix-strategy-taxonomy (findings 1 and 2), after the rewrite.
   - Terms: routing surfaces, doctrine, unknown-name routing / cross-component synthesis, and frontier difficulty.
6. **Unpack the long clauses that use a claim-title link as their subject.**
   - Cost: reordering a few sentences.
   - Pass: fix-strategy-taxonomy (finding-11) or plain-wording, after the rewrite.
   - Most affected sentences are in Current answer, which item 1 replaces.

**Sentence a hostile reviewer would attack first:** "Commonplace currently counters bloat with five partial mechanisms across prose, structure, and the code–prose boundary." The critique's objector puts it as "You have no current mechanisms. You have five essays."

**What reads well:** The Unsettled section is candid and well bounded. The Stakes section's three cost channels give a usable map of why bloat costs more in agent-operated mixed systems.

## Overclaims: support or divergence

**Support (may be narrowed):**
- "Commonplace currently counters bloat with five partial mechanisms": narrow to what operates.
- "Local rewrites confirm that raw brevity is the wrong target": "confirm" is stronger than two small, bounded cases support.
- "so verbose or obsolete material anchors later generations": the anchoring effect is a hypothesis.
- "a model can keep all the content while squeezing the wording": content preservation is not measured.
- "Empirically, agents default to additive changes": no evidence is cited.
- "Bloat in these mixed systems compounds": the note does not argue that cost grows faster than linearly.
- "Natural language has no comparable reachability check": partial analogues exist, such as the link graph, orphan detection and the sweep's recovery assay. The gap the note means is the lack of a check for decision relevance.

**Divergence (must be kept; carried into `must-keep`):**
- Software anti-bloat defenses do not carry over to natural-language artifacts. Prose has no check that tells whether a passage still changes any decision or answer.
- Raw brevity is the wrong target. The target is expansion that adds no structure.
- Validity checks alone do not stop valid but redundant artifacts from accumulating.
- Brevity pressure can change how text is worded without reducing its content bloat. Keep this as an open frontier.

## Claim questions for the operator

- **C1. Operative mechanisms or held theory** (Current answer: the lead sentence and the value-gate, retirement-path and scaffolding bullets).
  - The case is item 1 above.
  - Reports: `kb/workflow-state/data/current/review/results/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md/kb/instructions/critique-note.md`, `.../kb/instructions/composition-friction-gate.md`, `.../kb/instructions/premise-decomposition-gate.md` and `.../semantic/conceptual-role-conflation.md`.
  - This is the reason for the stop.
- **C2. The rewrite evidence is misattributed** (Current answer, bullet 2: "found that naive shortening dropped technical relations while clearer rewrites sometimes added words").
  - The two-rewrites evidence varied sentence splitting, which lengthened the text by 3.7%. It did not test shortening.
  - Only the three-passes evidence supports "naive shortening dropped relations".
  - The sentence should say which link supports which half (`semantic/grounding-alignment`, `sentence/misleading-link-text`).
- **C3. "Empirically, agents default to additive changes"** (Unsettled) has no evidence.
  - Either cite a log entry or episode, or label it an unrecorded observation with its scope.
  - The premise report adds a boundary: coding agents do delete things, such as tests, under check pressure (`prose/orphan-references`, `semantic/epistemic-status-blur`, `kb/notes/COLLECTION`, report-3).
- **C4. Anchoring in recursive exposure** (Stakes, third channel).
  - "so ... anchors later generations" states a hypothesis as fact.
  - The linked maintenance-capacity note treats the anchoring reports as unverified (`semantic/epistemic-status-blur`, report-1).
- **C5. Content preservation under brevity pressure** (Unsettled, brevity bullet).
  - Two parts of this claim go beyond the cited quotes:
    - "keep all the content" is not measured.
    - The transfer from a training-time length penalty to brevity pressure applied by prompts or review is not bridged.
  - Narrow the claim or mark the transfer as a conjecture (`semantic/grounding-alignment`, `prose/unbridged-cross-domain`, report-3).
- **C6. Placement of the log conjecture** (Unsettled, brevity bullet).
  - Choose whether it stays in the bullet, becomes its own bullet, or goes back to `kb/log.md` only.
  - Link the log entry if it stays (report-4, `structural/compound-bullet`).
- **C7. "Cutting six candidate pages by 53 percent and retiring two"** (Current answer, bullet 1).
  - The phrase can be read as seven pages or as eight.
  - The premise report says seven in total: the six byte-counted pages include one that was retired.
  - The evidence's precondition, that source access had to be repaired before removal was safe, is also omitted (`semantic/underspecified-assertions`, report-3).
- **C8. The reachability framing** (Unsettled, first bullet).
  - Should "no reachability oracle" become "no decision-relevance (use) oracle"?
  - Kind: choice; no defect is shown (reports 2 and 3).
- **C9. Placement in the collection** (Stakes, last sentence).
  - The `kb/notes/` contract describes finished replies, and this note declares itself an open standing query.
  - Kind: choice for the operator; no defect is shown. Recent commits add standing-query notes to `kb/notes/` deliberately, so the contract may need to name them (`kb/notes/COLLECTION`).

## Findings not acted on, with reasons

Because the run stops, none of the stored findings is planned. Each should be re-evaluated against the rewritten text.

- `accessibility/undefined-terms`, `accessibility/unidentified-references`: valid; deferred to the rewrite or a follow-up fix-strategy-taxonomy run, since several glossed passages will be rewritten.
- `complexity/connection-inflation`: valid. Edit the footer after the body's links settle.
- `kb/notes/COLLECTION`: placement goes to C9 and the evidence warning to C3.
- `prose/orphan-references`, `semantic/epistemic-status-blur`: these are claim questions C3 and C4, and the "confirm" overclaim under Support.
- `prose/unbridged-cross-domain`, `semantic/grounding-alignment`: these are claim questions C2 and C5.
- `semantic/conceptual-role-conflation`: this is C1, the reason for the stop.
- `semantic/underspecified-assertions`: this is C7. The INFO item on "bounded" is acknowledged in the text as an open problem.
- `sentence/clause-packing`, `sentence/misleading-link-text`, `structural/compound-bullet`: most of the flagged sentences are in passages the rewrite replaces. Re-review them afterwards.
- Critique secondary objection: say sharply what is specific to mixed systems. This is an extension; the claim as scoped stands without it.
- Role report: the note has no dependents, so no change reaches a linking file and nothing constrains the rewrite.
