---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/surgical-safety-checklist-haynes-2009.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population

**Source:** [A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population](../../../../sources/.snapshots/surgical-safety-checklist-haynes-2009.md)

The source is an immutable snapshot (Haynes et al. 2009, NEJM; user-supplied PDF converted to Markdown). No tracked ingest `kb/sources/surgical-safety-checklist-haynes-2009.ingest.md` exists yet. Every outbound candidate below is for that future ingest, which is the authored connection surface under `kb/sources/COLLECTION.md`. Every reverse edge must target the ingest, never the snapshot.

**Source content used for judging candidates.** This is a before-after study in eight hospitals (3733 patients before, 3955 after). The intervention was a 19-item WHO checklist read aloud at three fixed junctures: before induction of anesthesia, before skin incision and before the patient leaves the operating room. Deaths fell from 1.5% to 0.8% and complications from 11.0% to 7.0%. Adherence to all six measured safety indicators rose from 34.2% to 56.7%, but "the omission of individual steps was still frequent". The practices themselves were mostly known beforehand. Pulse oximetry and prophylactic antibiotics were available at every site, "although their use was inconsistent". The authors call the mechanism "less clear and most likely multifactorial". It bundles team briefings, systems changes (antibiotic administration moved into the operating room at three sites), behavior change and a possible Hawthorne effect. They describe the checklist as "intentionally designed to create a collective awareness among surgical teams about whether safety processes are being completed". The design is not randomized; the authors argue against confounding by secular trends.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, section "Outbound links". Allowed destinations: theory, reference, agent-memory-systems, agentic-systems, tags and other sources. Excluded: `kb/work/` and `kb/instructions/`. External is authorized for `derived-from` and `see-also`; external prospecting was skipped, since the only known external target is the source's own `source:` URL (`derived-from`, to be authored by the ingest). Labels that apply by destination: theory takes `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also` and `defined-in` (theory/definitions only). Sources takes `compares-with` and `see-also`. Reference takes `see-also` only. agent-memory-systems takes `is-evidence-for`, `compares-with` and `see-also`. agentic-systems takes `compares-with` and `see-also`.

**Context read, not linked:** `kb/work/operationalization-executability-automation/exploration.md` lines 189-195 and 288, and the workshop README line 35. The workshop listed Haynes as the case "Human operationalization without task automation", blocked by a 403 from the publisher. This explains why the source was captured. The workshop is an excluded destination.

**Description and title listings:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` (433 titles), filtered with `rg -i 'procedur|method|human|operator|execut|verif|activation|reliab|evidence|evaluat|gate|step|ritual|habit|routine|unattended|delegat'`. Flagged candidates: knowledge-storage-does-not-imply-contextual-activation, promotion-selects-for-unreliable-activation…, methodology-enforcement-is-constraining, methodological-and-computational-closure…, capable-agents-need-methodology-selection, unattended-work-needs-the-functions…, human-writing-structures-transfer-to-llms…, agent-memory-requirements/evaluate-memory-by-effects, theory-and-methodology-form-a-two-layer-execution-system and traditional-software-can-bracket-executor-conformance….
- `rg -N -m1 '^description:'` over 9 flagged theory files and 9 source ingests (Norman, Parasuraman-Sheridan-Wickens, CMMN, operationalism, Church-Turing, Plotkin, AI-agent reliability, position-bias, ATAM).

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (`complete: true`; the by-tag rg was skipped). Its "Control and transfer" section supplied methodology-enforcement-is-constraining and methodological-and-computational-closure…
- `kb/tags/failure-modes-README.md` (`complete: true`; by-tag rg skipped), `kb/tags/evaluation-README.md` and `kb/tags/llm-reliability-README.md`. Only the headers and inclusion conditions were read, for source-tag fit.

**Body search:**
- `rg -l -i 'checklist' kb/theory kb/agentic-systems kb/agent-memory-systems kb/reference kb/sources` returned about 60 files. Theory hits were evaluated with `rg -n -i 'checklist' kb/theory`. Kept: knowledge-storage (line 44, "checklists are the cues that decide what becomes active"), elicitation-requires-maintained-question-generation-systems (the domain-checklists strategy and checklist lifecycle) and methodological-and-computational-closure (line 78, the "exact checklist" row). The scaling-absorbs-scaffolding hit was evaluated and rejected. Hits in agent-memory-systems and agentic-systems (memex, echowiki, arscontexta, okf-harness, decapod, ai-agent-book) are incidental mentions of software checklists; all were rejected.
- `rg -l -i -w 'gawande|surgical|surgery|aviation|pilot checklist|hawthorne'` across theory, agentic-systems, agent-memory-systems, reference, sources and tags. It found no prior Haynes or Gawande ingest. The aviation hits were Norman, Parasuraman et al. and the AI-agent reliability ingests.
- `rg -n -i 'surg|hawthorne|gawande|WHO checklist|safety checklist' kb/sources/*.ingest.md` found only a false positive ("surgical axis" in position-bias).
- Theory queries: `'before-after|before/after|pre-post|secular trend'` returned nothing. `'observer effect|being observed|Hawthorne|reactivity'` returned nothing. `'juncture|checkpoint|gate at|trigger point'` gave 15 files, none about pre-action human procedures. `'process adherence|adherence|compliance rate'` gave 3 files, none relevant. `'human factors|high-reliability|safety-critical|aviation|clinical|medicine|medical'` gave 3 files, none relevant. `'mechanism (is|remains) (unclear|unknown)|multifactorial|bundle'` surfaced an-experiment-identifies-only-the-contrast-it-actually-runs (kept).
- `rg -n -i 'checklist|surg|aviation|hawthorne'` over 5 source ingests confirmed that Norman's domain is aviation and human factors. None of those ingests discusses checklists.

**Link following:**
- knowledge-storage → elicitation-requires-maintained-question-generation-systems and process-structure-and-output-structure. Elicitation was kept; process structure was rejected because the paper does not separate process structure from output structure.
- promotion-selects-for-unreliable-activation → activate-behavior-changing-memory and evaluate-memory-by-effects. Both were rejected as subsumed (see Rejected).
- method-guided-action head → methodology-enforcement-is-constraining (kept) → borrowed-patterns-transfer-only-over-shared-mechanism. That target becomes a transfer-caution flag, not a link.
- actionable-methodology definition, read in full. Kept conditionally for `defined-in`.
- Norman ingest, read in full. Its Summary says automation "cannot provide the continual feedback that human co-workers give each other". Kept for `compares-with`.
- Path existence was verified for every kept and rejected target with `ls`.

## Connections Found

These are candidate outbound edges for the future ingest `kb/sources/surgical-safety-checklist-haynes-2009.ingest.md`.

- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) -- **is-evidence-for**: Haynes is a non-LLM case of the note's activation criterion against the absence criterion. The checklist items were mostly known, and the key resources were present at every site, but their use was inconsistent. The intervention therefore closed an application gap rather than supplying absent content. Its delivery is rooted in workflow events: before induction, before incision and before leaving the room. It does not depend on a clinician first recalling the concern. The study measures the package's effect on process adherence and outcomes, which is the note's test step 4. Scope: human teams, before-after design, bundle effect.
- [Methodology enforcement is constraining](../../../../theory/methodology-enforcement-is-constraining.md) -- **is-evidence-for**: the checklist hardens activation (a required pause at fixed junctures, read aloud by the team) while the response stays human-interpreted (oral confirmation; "omission of individual steps was still frequent"). It is a field instance of the note's claim that activation and response harden independently. Adherence to all six indicators rose only from 34.2% to 56.7%, which shows that fixed activation does not settle compliant response.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: this is a human analogue of the context-to-action failure with an intervention that reaches outcomes. Practitioners knew the practices and the means were present, yet use was inconsistent. A cue at a fixed point in the workflow raised both adherence and outcomes. The study also keeps the note's evaluation rungs apart: process adherence (uptake) and complications and deaths (benefit) are measured separately. It complements the note's existing human antecedents (Tulving–Pearlstone, Gick–Holyoak), which stop at recall or a single problem. The ingest must state the limits: human, non-randomized, a bundle effect and a possible Hawthorne effect.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **is-evidence-for**: the authors report at bundle grain. The conclusion says the checklist was "associated with" reductions, and the mechanism is called "most likely multifactorial". It covers briefings, relocation of antibiotic administration, behavior change and a possible Hawthorne effect. This makes it a clean external worked case of reporting a bundle effect without assigning it to a component. The ingest should also note that popular retellings often name the checklist itself as the cause, which is the attribution error the note describes.
- [Elicitation requires maintained question-generation systems](../../../../theory/elicitation-requires-maintained-question-generation-systems.md) -- **is-evidence-for** (weaker): the WHO checklist is a domain checklist under the note's strategy 3. It was seeded from the WHO Guidelines for Safe Surgery, matching lifecycle step 1, and was translated and "adjusted to fit into the flow of care at each institution". It shows that expert knowledge externalized once can raise application among skilled users. Limits: the note's motivating gap is a user's lack of expertise, whereas surgical teams had the expertise and lacked activation. The paper does not test ossification or the maintenance loop.
- [Actionable methodology](../../../../theory/definitions/actionable-methodology.md) -- **defined-in**: use this only if the ingest uses "actionable" in the technical sense, which is likely given the workshop's framing "human operationalization without task automation". The paper's systems changes shifted the available operations, not only the method. Three sites moved antibiotic administration into the operating room, and the formal pause created a team-wide occasion for confirmation. Readers need the operator, operations, target and setting relation to read that point correctly.
- [Ingest: Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with** on the axis "continual feedback among co-operators". Norman argues that automation fails because it cannot give the feedback that "human co-workers give each other". Haynes shows that even all-human teams do not supply that feedback reliably by default. The checklist installs it as a scheduled, spoken confirmation among peers to create "collective awareness". The comparison qualifies Norman's assumption that human co-workers supply the function. Haynes has evidence from a before-after study; Norman has incident narratives.

## Bidirectional Candidates

- [Ingest: Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) <-> Haynes ingest -- **compares-with**: the return direction helps readers of Norman too. Norman's Limitations section notes that his incidents cannot separate missing feedback from crew-resource-management culture. Haynes is a later, outcome-measured intervention that institutionalizes team feedback in another high-risk domain. This applies only after the Haynes ingest exists.

## Reverse-edge Candidates

All of these require the Haynes ingest to exist first. Each uses the `evidenced-by` label from `kb/theory/COLLECTION.md` (theory → sources). Under the theory contract, each citation must sit in a body sentence. A note above five unquoted tracked sources must pair a verbatim quote from the Haynes ingest's Quotes section.

- [Promotion selects for unreliable activation…](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) → Haynes ingest -- **evidenced-by**: the note has no external evidence for its rooted-delivery claim. Its examples of a root firing event ("a human invoking a procedure") are hypothetical. Haynes is a measured case in which a delivery path rooted in workflow junctures closed part of an application gap. It also qualifies the claim: closure was partial. The note currently cites 0 tracked sources.
- [Methodology enforcement is constraining](../../../../theory/methodology-enforcement-is-constraining.md) → Haynes ingest -- **evidenced-by**: the note's activation-and-response table has no evidenced row for "fixed activation, interpreted human response". Haynes shows that this configuration raises adherence substantially but incompletely. It currently cites 0 tracked sources.
- [Knowledge storage does not imply contextual activation](../../../../theory/knowledge-storage-does-not-imply-contextual-activation.md) → Haynes ingest -- **evidenced-by**: candidate for the "Two human studies supply historical antecedents" paragraph or the "Why It Matters" evaluation rungs. The note already cites 7 distinct tracked ingests, so it must quote Haynes rather than cite it unquoted.
- [An experiment identifies only the contrast it actually runs](../../../../theory/an-experiment-identifies-only-the-contrast-it-actually-runs.md) → Haynes ingest -- **evidenced-by**: a published example of an author correctly reporting bundle grain (it currently cites 4 tracked ingests).

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- its "exact checklist" row looks like a match, but the note classifies decisions in an improvement pathway (patch acceptance, revision). Haynes is about executing operations at runtime. A link would invite a misreading of the note's scope.
- [Activate behavior-changing memory before the mistake](../../../../theory/agent-memory-requirements/activate-behavior-changing-memory.md) -- it fits topically (checklists fire before the action), but the promotion note already names it as the menu of firing mechanisms and makes the sharper rooted-delivery claim. The note's checklist item also concerns moving a lesson toward symbolic enforcement, and the WHO checklist stays human-interpreted. Redundant traversal.
- [Evaluate memory by effects, not by existence](../../../../theory/agent-memory-requirements/evaluate-memory-by-effects.md) -- the point that effects are measured separately from existence is already carried by the knowledge-storage evaluation rungs. The note concerns agent memory, not procedures.
- [Scaling absorbs scaffolding at fixed task difficulty…](../../../../theory/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md) -- it mentions checklists as scaffolding absorbed by later model generations. Human expertise is not a model generation, and Haynes says nothing about absorption over capability growth. This is a keyword match only.
- [Process structure and output structure are independent levers](../../../../theory/process-structure-and-output-structure-are-independent-levers.md) -- the checklist is process structure, but the study does not vary process and output structure separately. It offers no evidence for or against independence.
- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) -- the note is about removing an operator. Haynes keeps every human operator and adds a coordination procedure, so the shared axis is too thin.
- [Ingest: Parasuraman, Sheridan and Wickens, types and levels of automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- the checklist allocates no function to automation. A comparison on function allocation would only say "level 1 everywhere".
- [Ingest: CMMN 1.1](../../../../sources/cmmn-1-1-specification.ingest.md) -- one could contrast CMMN's human run-time planning and discretionary activation with fixed checklist junctures. CMMN is a design standard without outcome evidence, and the contrast is the workshop's synthesis to make, not a source-to-source link.
- [Ingest: Towards a science of AI agent reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) -- its survey of safety-critical engineering does not discuss checklists.
- Agent-memory-systems and agentic-systems checklist hits (memex, echowiki, arscontexta, okf-harness, decapod, ai-agent-book) -- these are incidental mentions of software or prompt checklists with no shared mechanism.

## Index Membership

- [method-guided-action](../../../../tags/method-guided-action-README.md) -- a candidate inline `tags:` value for the future ingest. Its analysed contribution would be activation and enforcement of a known method at fixed junctures, which meets the tag's "activation, enforcement" condition. Under `kb/sources/COLLECTION.md`, source tags do not affect member listings.
- [evaluation](../../../../tags/evaluation-README.md) -- possible second source tag, but only if the ingest substantively analyses the before-after design, the bundle attribution and the Hawthorne confound, not just the reported results.

## Synthesis Opportunities

Promotion-selects-for-unreliable-activation and methodology-enforcement-is-constraining, together with Haynes, imply a narrower claim. Rooting activation in fixed workflow events closes only part of an application gap when the response stays interpreted, and the remaining gap shows up as omitted items. Haynes measures both halves: 34.2% → 56.7% of patients received all six indicators. That is a large improvement that still leaves most of the gap. Neither note states this split for interpreted responses. This needs more than one human study before it earns a note; record it in the log or the workshop first.

## Maintenance Observations

- `kb/work/operationalization-executability-automation/exploration.md` (source table, line 191; "Ingest status", line 195; disposition item 8, line 288) and the workshop `README.md` (line 35) still record Haynes as blocked and needing a user-supplied copy. A user-supplied PDF-to-Markdown snapshot dated 2026-10-31 now exists. The workshop entries will be stale once the ingest is written.

## Flags

- **The ingest does not exist yet.** All outbound and reverse edges depend on running `cp-skill-ingest kb/sources/.snapshots/surgical-safety-checklist-haynes-2009.md` first.
- **Transfer caution.** [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../theory/borrowed-patterns-transfer-only-over-shared-mechanism.md) applies to every theory edge above. The paper's own mechanism is unresolved ("multifactorial", with a Hawthorne effect "difficult to disentangle"), so links to LLM-activation notes can only be framed as a human analogue or precedent. They cannot carry transferred warrant to LLM executors. The ingest's Connections section should say so explicitly. The Norman ingest models this framing ("independent, non-LLM evidence").
- **Tension to keep visible.** Haynes partly undercuts Norman's premise that human co-workers naturally supply continual feedback, while supporting Norman's conclusion that the feedback function must be designed in. Do not resolve this in the ingest; record it as a comparison.
- Not a split candidate: the source makes one main assertion with bounded mechanism discussion.
