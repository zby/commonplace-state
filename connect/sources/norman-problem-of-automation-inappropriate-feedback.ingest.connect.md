---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/norman-problem-of-automation-inappropriate-feedback.ingest.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: Ingest: The "Problem" of Automation: Inappropriate Feedback and Interaction, Not "Overautomation"

**Source:** [Norman 1989 ingest](../../../../sources/norman-problem-of-automation-inappropriate-feedback.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` outbound section. Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags, sources, external. Excluded: `kb/work/`, `kb/instructions/`. Labels for ingest reports: `derived-from` (external), `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (use sparingly). The workshop named in `occasion` is in `kb/work/` and is excluded as a link target.

**Existing inline links verified (all paths exist):** unattended-work-needs-the-functions-that-interaction-supplied, final-task-success-does-not-establish-intended-path-health, ironies-of-automation.ingest, model-types-levels-human-interaction-automation.ingest, the-augmentation-automation-boundary-is-discrimination-not-accuracy, warranted-transfer-leaves-people-the-hardest-to-warrant-decisions, llm-generation-relaxes-goals-where-human-writing-stalls, NTRS external URL. The ingest's connections are inline only; it has no labelled footer.

**Topic indexes:**
- `kb/tags/observability-README.md` (source carries `tags: [observability]`). Runtime-visibility group flagged final-task-success (already linked) and silent-disambiguation-is-the-semantic-analogue-of-tool-fallback (new candidate). Inspectable-artifact note read by description; rejected (representational form, not runtime feedback).

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory --glob '*.md' | grep -i -E 'silent|hidden|fallback|signal|escalat|report|delegat|automat|interaction|feedback|visible|observab|unattended|salien|compensat|repair'` -- flagged silent-disambiguation, the-boundary-of-automation-is-the-boundary-of-verification, intent-framed-delegation, enforcement-without-structured-recovery (via description), an-omitted-loop-function-and-a-frozen-one, candidacy-evidence-licenses-escalation, stateful-tools-recover-control-by-becoming-hidden-schedulers.

**Body search:**
- `rg -l -i 'bainbridge|parasuraman|ironies of automation|autopilot|human-factors|out of the loop|out-of-the-loop|automation complacency|situation awareness' kb` -- human-factors cluster: increasing-computational-autonomy-relocates-human-effort, the-boundary-of-automation-is-the-boundary-of-verification, methodological-and-computational-closure-track-different-changes (Parasuraman precedent), reviewers-share-the-fields-prior, borretti-no-man-is-an-island.ingest, ironies-of-automation.ingest, model-types ingest. No artifact other than the source mentions Norman.
- `rg -l -i 'silent|compensat|fallback|hidden repair|feedback' kb/theory` -- broad; confirmed final-task-success and silent-disambiguation as the observability core; others keyword-only.
- `rg -l -i 'salien|alarm|threshold alert|nonintrusive|status report' kb/theory kb/sources` -- flagged locating-hidden-failures-paper.ingest (first-error localization); rest keyword-only.
- `rg -n -i 'hidden|silent|compensat' kb/sources --glob '*.ingest.md' -l` -- no source on silent compensation in physical control besides Bainbridge.
- agentic-systems / agent-memory-systems / reference: no plausible trigger match (no system-specific feedback mechanism discussed); skipped beyond the body searches above.

**Link following:**
- final-task-success -> silent-disambiguation (its runtime-visibility sibling in the tag head); its synchronous/asynchronous reporting section is where Norman's saturation dynamic lands.
- ironies-of-automation.ingest -> borretti-no-man-is-an-island.ingest (deskilling pair); not relevant to feedback.
- the-boundary-of-automation -> Bainbridge monitoring irony; Norman supplies the counter-reading (automation's limit is its own reporting, not only human verification).

## Connections Found

Already present inline and confirmed; no change needed: unattended-work, final-task-success, ironies-of-automation.ingest, model-types ingest, augmentation-automation boundary, warranted-transfer, llm-generation-relaxes-goals, external NTRS (`derived-from`).

New candidates:

- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) -- **compares-with**: shared axis is silent local repair that keeps the visible outcome normal while hiding that something failed; the autopilot compensating for engine loss is the physical-control instance, the agent resolving spec ambiguity the semantic one. Norman adds the saturation limit, which the semantic case may lack.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **compares-with**: both read the human-factors tradition on where automation stops; the note takes Bainbridge's line (humans cannot verify a superior system in real time), while Norman places the boundary in the automation's own inability to monitor and report its abnormal states ("monitoring of its own monitoring"). Useful as a named tension, not as corroboration.
- [Locating hidden failures (Traverse/Scout)](../../../../sources/locating-hidden-failures-paper.ingest.md) -- **compares-with** (weaker): shared axis is separating final outcome from where and when the first error occurred; Norman's cases are late detection of an early fault, Traverse measures first-error localization in agent trajectories. Include only if the ingest wants an agent-era counterpart.

## Bidirectional Candidates

- [Ironies of Automation (Bainbridge)](../../../../sources/ironies-of-automation.ingest.md) <-> source -- **compares-with**: Bainbridge's ingest should link back to Norman as the explicit counter-conclusion (more capable reporting automation rather than less automation) on the shared out-of-the-loop analysis.
- [A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) <-> source -- **compares-with**: Norman's "intermediate level maximizes difficulties" bears on the level/stage framework; the return link helps a reader of the levels model find the feedback condition.

## Reverse-edge Candidates

- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) -> source -- **evidenced-by** (theory contract): qualifies and extends the note with an independent, non-LLM case; the context phrase should say it bounds rather than corroborates (incident narratives, not a refutation test) and name the saturation dynamic relevant to the note's open question on synchronous versus asynchronous signals.
- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) -> source -- **evidenced-by**: bounds the note's scope with a delegate-supplied (not operator-supplied) function: continual state and anomaly reporting.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -> source -- **evidenced-by** (qualifies): Norman is a period counter-position to the Bainbridge reading the synthesis already uses.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Increasing computational autonomy relocates human effort](../../../../theory/increasing-computational-autonomy-relocates-human-effort.md) -- cites Bainbridge on role transformation; Norman's thesis is about feedback, not effort relocation. Topical only.
- [Enforcement without structured recovery is incomplete](../../../../theory/enforcement-without-structured-recovery-is-incomplete.md) -- recovery/escalation layering; Norman is about detection and reporting, not recovery strategy.
- [Methodological and computational closure track different changes](../../../../theory/methodological-and-computational-closure-track-different-changes.md) -- uses Parasuraman per-function reporting precedent; unrelated to feedback design.
- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../theory/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) -- representational inspectability of artifacts, not runtime state feedback.
- [Intent-framed delegation is a control regime](../../../../theory/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) -- delegation handoff content, not delegate reporting back; the thought-experiment link is too loose.
- [Borretti, No man is an island](../../../../sources/borretti-no-man-is-an-island.ingest.md) -- deskilling via community; no feedback axis.

## Index Membership

- [Observability tag head](../../../../tags/observability-README.md) -- the source already carries `tags: [observability]`; sources are outside tag-participating collections, so no head entry is expected. No action.

## Synthesis Opportunities

Final-task-success, silent-disambiguation and Norman's autopilot cases together suggest a claim not yet stated: hidden compensation with a capacity limit converts a recoverable early deviation into a late, time-compressed failure, so the need for a synchronous signal depends on whether the hidden repair saturates. The ingest already flags this as Extractable Value 4 and notes it needs an agent-runtime instance before it earns a note.

## Maintenance Observations

- The human-factors automation sources (Bainbridge, Parasuraman et al., Norman) have no reciprocal links among themselves apart from what this ingest authors; Bainbridge and the levels-model ingest do not mention Norman.

## Flags

- Tension to keep visible, not resolve: Bainbridge-derived theory (the-boundary-of-automation, increasing-computational-autonomy) treats the human verifier as the limit; Norman treats the automation's reporting capacity as the limit.
- Primary consumer named in `occasion` is the workshop `kb/work/operationalization-executability-automation`, which is excluded as a link target under the sources contract; the Recommended Next Action correctly routes value there by prose, not link.
