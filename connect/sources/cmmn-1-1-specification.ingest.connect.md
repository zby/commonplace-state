---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/cmmn-1-1-specification.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: Case Management Model and Notation (CMMN) Version 1.1

**Source:** [Ingest: Case Management Model and Notation (CMMN) Version 1.1](../../../../sources/cmmn-1-1-specification.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations to prospect: theory, reference, agent-memory-systems, agentic-systems, tags, sources. Excluded: `kb/work/`, `kb/instructions/`. Authorised labels: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external). External prospecting skipped; the only external target, the OMG URL, is already present as `derived-from`.

**Existing connections verified (all paths exist):** methodological-and-computational-closure, model-types-levels-human-interaction-automation.ingest, fix-what-the-executor-cant-determine, scheduler-llm-separation, progressive-constraining, definitions/codification, statecharts-and-programs, workshop-layer, active-work-state. This run looks for candidates the ingest does not already carry.

**Topic indexes:**
- `kb/tags/method-guided-action-README.md` (`complete: true`; by-tag rg skipped). Flagged: methodology-enforcement-is-constraining (activation/response split), theory-and-methodology-form-a-two-layer-execution-system, intent-framed-delegation.
- `kb/tags/warranted-autonomy-README.md` (`complete: true`; by-tag rg skipped). Theory titles under `kb/theory/` were listed by filename for autonomy and automation: usefulness-autonomy-warrant-and-power-are-separate-dimensions, the-boundary-of-automation-is-the-boundary-of-verification, increasing-computational-autonomy-relocates-human-effort, capability-placement-should-follow-autonomy-readiness.

**Body search** (scope: `kb/theory kb/reference kb/agentic-systems kb/agent-memory-systems kb/sources kb/tags`):
- rg -i "CMMN|BPMN|guard-stage|case management|case worker" -- no hits outside the source. This confirms the ingest's claim that no artifact treats CMMN directly.
- rg -i "discretion(ary)?" -- codifying-predictable-choices (kept), specification-level-separation (kept), intent-framed-delegation (weighed, rejected), mission-command ingests (kept one), argyris and ontology-grounded-project-memory (incidental mentions, rejected), AAS retained-archive results (incidental mentions, rejected).
- rg -i "run-time planning|runtime planning|planning table" -- no hits.
- rg -i "workflow engine|orchestrat(ion|or) engine|state machine" -- mostly agentic-system reviews and ADRs about Commonplace's own workflow runner (agno-agentos, swamp, ADR 101/118). None of them separates run-time human planning from engine execution, so all were rejected. The statecharts and workshop-layer notes were already connected.
- rg -i "human-in-the-loop|approval gate|manual activation" -- augmentation-automation-boundary (weighed, rejected), agent-memory-requirements/make-authority-explicit (weighed, rejected), various system reviews (incidental).
- rg -i "preferential codification|codif(y|ication) (only )?after" -- codifying-predictable-choices (kept), constraining tag head, pmi-lexicon and haasnoot ingests (kept haasnoot).
- rg -i "automation level|levels of automation|function allocation" -- computationally-directed-self-improvement-is-a-reallocation (weighed), vocabulary-collision-ledger (not relevant).
- Sibling ingests from the same workshop batch were checked via the git status listing: norman-problem-of-automation-inappropriate-feedback.ingest (kept).

**Link following:**
- methodology-enforcement-is-constraining -> the-boundary-of-automation-is-the-boundary-of-verification, definitions/codification. This confirmed that the activation/response split maps onto CMMN's sentry/ManualActivationRule versus RequiredRule/completion criteria.
- haasnoot ingest body: signposts and triggers that start, alter or stop actions. These are structurally close to CMMN sentries (OnPart event plus IfPart condition).
- `kb/work/operationalization-executability-automation/exploration.md` already mentions CMMN (rg -l cmmn kb/work). The workshop is excluded as a destination.

## Connections Found

- [Methodology enforcement is constraining](../../../../theory/methodology-enforcement-is-constraining.md) -- **compares-with**: on the axis of activation versus response rules. CMMN separates activation (sentries; ManualActivationRule deciding whether enabled work starts automatically or waits for a human) from completion and response criteria (RequiredRule, autoComplete). This is a standardized instance of the note's claim that the two parts harden independently. A manually activated HumanTask has engine-fixed activation and human-interpreted response.
- [Codifying predictable choices leaves agents with less predictable work](../../../../theory/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) -- **compares-with**: on the residual left after codification. CMMN 4.2's analyst cycle folds emerging patterns into rules while the discretionary catalogue keeps the rest with case workers. This is the institutional shape of preferential codification at a human boundary. The spec gives no workload data, so the comparison does not test the composition shift. The ingest already names "preferential codification" in Extractable Value 3 without linking it.
- [Specification-level separation recovers scoping before it recovers error correction](../../../../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) -- **compares-with**: on how a notation exposes discretion boundaries. OpenProse marks discretionary judgment in the spec but leaves scheduling on the LLM. CMMN marks discretion (PlanningTables, discretionary items) and also hands scheduling and state tracking to a symbolic engine. That makes it a reference point for the far end of the regime the note describes.
- [Tool usefulness, computational autonomy, warrant, and system power are separate dimensions](../../../../theory/usefulness-autonomy-warrant-and-power-are-separate-dimensions.md) -- **compares-with**: on keeping capability dimensions separate. CMMN's independent dials (engine execution, performer type, manual activation, discretionary planning) show a deployed design where "the engine runs the model" carries no claim about computational autonomy over the work. Use this link only if Extractable Value 1 is developed. The two sets of dimensions differ, so the shared axis is "separate predicates", not a one-to-one mapping.
- [Dynamic Adaptive Policy Pathways](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md) -- **compares-with**: on condition-triggered transitions instead of fixed sequences. DAPP signposts and triggers start, alter or stop actions under monitored conditions. CMMN sentries (OnPart event plus CaseFile IfPart) do the same for plan items. Both declare the space of possible moves at design time and commit at run time.
- [Norman: The "Problem" of Automation](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md) -- **compares-with**: on what a human partner can see of automated state. CMMN makes plan-item lifecycle state explicit and engine-tracked, but leaves non-blocking HumanTasks untracked. That is a design-level answer, and a gap, relative to Norman's feedback requirement. This is a same-batch sibling, so check the link still reads well once both ingests are final.

## Bidirectional Candidates

- [Dynamic Adaptive Policy Pathways](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md) <-> source -- **compares-with**: the haasnoot ingest's outbound surface would gain a non-policy, software-standard instance of trigger-gated commitment.

## Reverse-edge Candidates

- [Progressive constraining commits only after patterns stabilize](../../../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) → source -- **evidenced-by** (theory contract): CMMN 4.2 qualifies or broadens the claim's scope to human case-work practice. The context phrase must say this is an institutionalized recommendation, not a test the claim could have failed ("Origin is not corroboration").
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) → source -- **evidenced-by** (theory contract), as a qualifying or bounding case: a standard where routing and completion are settled and engine-executed while content and selection stay with humans.
- [Scheduler-LLM separation exploits an error-correction asymmetry](../../../../theory/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) → source -- **evidenced-by** (bounding): a pre-LLM industrial design with the same engine/judgment split. It needs a context phrase that names the shared mechanism (symbolic bookkeeping versus interpreted selection) and does not claim corroboration of the asymmetry itself.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Intent-framed delegation is a control regime](../../../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) -- concerns how intent governs adaptive executor choice. CMMN supplies Role authorizations and applicability filters but no intent mechanism. The fix-what-the-executor-cant-determine link already covers the design-time/run-time axis.
- [US Army ADRP 6-0 mission command](../../../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md) -- a bounded-autonomy analogue, but the shared axis (delegated discretion under intent) is weaker than the haasnoot trigger match. It adds a third human-organisation comparison without a new distinction.
- [The augmentation-automation boundary is discrimination, not accuracy](../../../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- about per-instance discrimination for crossing to automation. CMMN has no account of when items may become automatic (the ingest's Limitations section says so explicitly).
- [Make authority explicit](../../../../theory/agent-memory-requirements/make-authority-explicit.md) -- Role-gated planning is an authority mechanism, but the note is scoped to memory read/write/promote rights, not work planning.
- [Computationally directed self-improvement is a reallocation](../../../../theory/computationally-directed-self-improvement-is-a-reallocation.md) -- concerns self-improving systems. CMMN's codification is done by human analysts, so the source does not bear on the endpoint test.
- Agentic-system reviews matching "workflow engine/state machine" (agno-agentos, swamp) -- keyword matches only. They do not separate human run-time planning from engine execution.

## Index Membership

- [method-guided-action tag head](../../../../tags/method-guided-action-README.md) -- the source already carries this tag. Sources do not appear in complete tag listings (sources/COLLECTION.md), so no index change is needed.
- [warranted-autonomy tag head](../../../../tags/warranted-autonomy-README.md) -- the source carries this tag. The ingest's own Limitations section says CMMN "gives no warrant account for which items stay discretionary". The tag's inclusion condition should be rechecked: substantive treatment, not mention.

## Synthesis Opportunities

Read together, methodology-enforcement-is-constraining (activation versus response), methodological-and-computational-closure (settlement versus executor) and the CMMN ingest suggest a candidate claim. The claim: "executes the model", "starts the work" and "decides the work" are three separately hardenable parts of a delegated task. CMMN is a deployed standard that fixes the first, makes the second a per-item switch and leaves the third human. This is the workshop's question, so it belongs to `kb/work/operationalization-executability-automation/` until its mechanism is settled.

## Maintenance Observations

- The source carries `tags: [warranted-autonomy]` while its Limitations section says it cannot ground warranted-autonomy claims. The tag assignment may fail the substantive-treatment condition.
- The ingest names "preferential codification" (Extractable Value 3) without linking the defining note, codifying-predictable-choices-leaves-agents-with-less-predictable-work.

## Flags

- Same-batch sibling links (norman) depend on concurrently written ingests. Verify both are committed before authoring.
