---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/surgical-safety-checklist-haynes-2009.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population

**Source:** [Ingest: A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population](../../../../sources/surgical-safety-checklist-haynes-2009.ingest.md)

The ingest already carries seven inline connections (methodology-enforcement-is-constraining, promotion-selects-for-unreliable-activation, knowledge-storage-does-not-imply-contextual-activation, an-experiment-identifies-only-the-contrast, actionable-methodology, the Norman ingest, elicitation-requires-maintained-question-generation-systems) plus borrowed-patterns-transfer as a scope guard. All eight paths were verified to exist. This report surfaces only additions and reverse edges. The existing links lack explicit labels in footer form; a future editor may want to add `- [title](path) — label: context` footers, but the inline connectives are allowed by the sources contract.

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels used for filtering: `is-evidence-for` (theory, agent-memory-systems), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `rests-on`/`abstracted-from` (theory), `see-also` (sparingly), `derived-from` (external only). External prospecting skipped (no web search); the source URL is already in frontmatter.

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (complete: true, so by-tag rg skipped) -- flagged [methodological-and-computational-closure-track-different-changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) ("distinguish what the method settles from who executes the decision"), [fix-what-the-executor-cant-determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md), [theory-and-methodology-form-a-two-layer-execution-system](../../../../theory/theory-and-methodology-form-a-two-layer-execution-system.md); confirmed existing links to methodology-enforcement and borrowed-patterns.

**Description / title listing scan:**
- `rg -N -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "activat|trigger|enforce|adherence|automat|autonom|human|feedback|bundle|executor|setting|operat"` -- flagged usefulness-autonomy-warrant-and-power, human-analogies-suggest-functions, enforcement-without-structured-recovery, the-augmentation-automation-boundary, naur-equates-machine-execution, human-writing-structures-transfer, human-llm-differences, increasing-computational-autonomy, activate-behavior-changing-memory.
- `rg -N -m1 '^description:'` on each flagged file to evaluate.

**Body search:**
- `rg -il "checklist" kb/theory kb/sources kb/reference kb/agentic-systems kb/agent-memory-systems kb/tags` -- ~60 hits; key: `methodological-and-computational-closure...md:78` (table row "A maintainer applies an exact checklist ... Methodologically closed: Yes / Computationally closed: No"), `knowledge-storage...md:44` (checklists as activation cues; already linked), `agent-memory-requirements/activate-behavior-changing-memory.md:20`, `process-structure-and-output-structure...md:16` (peer-review checklists as process structure). Agent-memory/agentic-system reviews mention checklists only as system features — rejected.
- `rg -l "operationaliz" kb/theory kb/sources kb/agentic-systems kb/tags` -- sources sharing the occasion.
- `rg -l "^occasion:.*operationalization-executability" kb/sources` -- sibling ingests: operationalism-sep, plotkin-origins-of-sos, cmmn-1-1-specification, norman (linked), church-turing-thesis-sep.
- `rg -l -i "hawthorne|gawande|aviation|pilot checklist|time.?out|surgical|surgery|clinical"` -- surfaced `model-types-levels-human-interaction-automation.ingest.md` (Parasuraman/Sheridan/Wickens); other hits were incidental.
- `rg -n "haynes|surgical" kb -l` -- no non-work artifact links Haynes yet (only `kb/work/operationalization-executability-automation/exploration.md`, excluded destination).
- `rg -n -i "external trigger|workflow event|fixed junctur|hook" kb/theory -l` -- enforcement-without-structured-recovery, periodic-kb-hygiene-should-be-externally-triggered; evaluated below.

**Link following:**
- methodological-and-computational-closure → usefulness-autonomy-warrant-and-power (separate dimensions), Parasuraman per-function precedent, computationally-directed-self-improvement-is-a-reallocation.
- cmmn-1-1-specification.ingest Connections Found → already compares-with methodological-and-computational-closure and Parasuraman on the same axis; confirms a sibling cluster the Haynes ingest should join.

## Connections Found

- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- **is-evidence-for**: the note's first table row ("a maintainer applies an exact checklist") is a constructed example of method settlement without computational closure; Haynes supplies a field case with outcome data in which the procedure was operationalized and no function was computationally closed. It also qualifies the row: the checklist settles activation and item content but leaves verdicts (e.g., anticipated critical events) to interpreted human confirmation, so methodological closure was partial. This is the occasion's central distinction and the strongest unlinked theory target.
- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](../../../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) -- **is-evidence-for**: a measured "usefulness/outcome without autonomy" case — complications and deaths fell with computational autonomy unchanged at zero — instantiating the note's "usefulness without autonomy" pair outside software. Bundle and before-after caveats travel with it.
- [Ingest: OMG CMMN 1.1 specification](../../../../sources/cmmn-1-1-specification.ingest.md) -- **compares-with**: on the axis "operationalization without function automation". CMMN separates engine execution, performer type and activation in a standard with no outcome data; Haynes has outcome data with no engine at all and fixed (not discretionary) activation. Together they bracket the workshop's distinction from both sides.
- [Ingest: Parasuraman, Sheridan, Wickens — model of types and levels of automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- **compares-with**: on per-function human/automation allocation. Haynes sits at the manual end of every PSW stage, yet changes outcomes by restructuring human information acquisition and team feedback — an intervention that PSW's level scale does not register.

## Bidirectional Candidates

- [Ingest: Norman, The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) <-> source -- **compares-with**: Haynes already links Norman; Norman does not link back. The return edge is useful because Haynes qualifies Norman's premise that human co-workers supply continual feedback by default.
- [Ingest: OMG CMMN 1.1 specification](../../../../sources/cmmn-1-1-specification.ingest.md) <-> source -- **compares-with**: CMMN's Limitations section notes it has "no outcome data"; Haynes is the outcome-bearing human counterpart a reader of CMMN would want.

## Reverse-edge Candidates

Under `kb/theory/COLLECTION.md`, theory notes may link sources with `evidenced-by` (corroborates, qualifies, or bounds). Per "Origin is not corroboration", these would be qualifying/bounding evidence unless the note's claim risked failure on this case.

- [Methodology enforcement is constraining](../../../../theory/methodology-enforcement-is-constraining.md) → source -- **evidenced-by**: qualifies the activation/response split with field data: fixed activation at workflow junctures raised all-six adherence 34.2% → 56.7% but left omissions frequent. Context phrase should say it bounds, not corroborates, and name the bundle confound.
- [Promotion selects for unreliable activation, and the regress ends only at an external trigger](../../../../theory/promotion-selects-for-unreliable-activation-and-the-regress-ends-only.md) → source -- **evidenced-by**: a human instance of an externally triggered delivery path; bounded to the components that were known-but-unapplied practice (antibiotics, oximetry).
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) → source -- **evidenced-by**: a real case for the "checklist, method-closed, computationally open" table row, replacing a constructed example with an observed one.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Process structure and output structure are independent levers](../../../../theory/process-structure-and-output-structure-are-independent-levers.md) -- mentions peer-review checklists as pure process structure; Haynes does not separate process from output effects, so the link would be keyword-level.
- [Activate behavior-changing memory before the mistake](../../../../theory/agent-memory-requirements/activate-behavior-changing-memory.md) -- lists checklists as an activation surface, but its contribution is covered more precisely by the already-linked promotion/activation and knowledge-storage notes.
- [Enforcement without structured recovery is incomplete](../../../../theory/enforcement-without-structured-recovery-is-incomplete.md) -- Haynes does not report what happened after missed items; no recovery evidence.
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- plausible (site adaptation leaves choices to local teams), but the paper does not document which choices were fixed vs. left open; CMMN already carries this comparison.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- relevant to the ingest's "peer confirmation as feedback function" analogy, but that value item is explicitly untested; reconsider if that item is developed.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), [Naur's human-only conclusion...](../../../../theory/naur-equates-machine-execution-with-formulated-criteria.md) -- concern crossing into automation; Haynes never approaches that boundary.
- [Ingest: Operationalism (SEP)](../../../../sources/operationalism-sep.ingest.md), [Ingest: Church–Turing thesis (SEP)](../../../../sources/church-turing-thesis-sep.ingest.md), [Ingest: Plotkin, origins of SOS](../../../../sources/plotkin-origins-of-sos.ingest.md) -- same workshop occasion, but they concern the meaning of "operational"/"effective method"; a link would be workshop-cluster association with no named shared axis. The workshop is the right place to juxtapose them.
- Agent-memory-systems and agentic-systems reviews hitting "checklist" (e.g., arscontexta, decapod, okf-harness) -- checklist appears as a system feature, no shared mechanism with team-activation evidence.

## Index Membership

- [method-guided-action tag head](../../../../tags/method-guided-action-README.md) -- already tagged; sources do not participate in generated membership, so no head entry is needed.

## Synthesis Opportunities

Haynes (outcome data, no engine, fixed activation), CMMN (engine-executed model, discretionary human activation, no outcome data) and Parasuraman (per-function allocation scale) together imply a candidate claim: operationalization, model execution, function allocation and decision autonomy are independently settable, and outcome gains can come from operationalization alone. This belongs to the operationalization workshop to develop, not to connect.

## Maintenance Observations

None

## Flags

- Tension (already recorded in the ingest): Haynes qualifies Norman's premise that human teams supply feedback by default. Not resolved here.
- Transfer caveat: all theory edges are human-executor evidence; context phrases must keep the bundle and before-after confounds and the borrowed-pattern transfer limit.
