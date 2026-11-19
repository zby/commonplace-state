---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/norman-problem-of-automation-inappropriate-feedback.md"
source_has_frontmatter: true
date: "2026-10-31"
depth: standard
---

# Connection Report: The "Problem" of Automation: Inappropriate Feedback and Interaction, Not "Overautomation"

**Source:** [The "Problem" of Automation (Norman 1989)](../../../../sources/.snapshots/norman-problem-of-automation-inappropriate-feedback.md)

The source is an immutable snapshot. Every outbound candidate below is meant for its authored surface, the matching ingest `kb/sources/norman-problem-of-automation-inappropriate-feedback.ingest.md`. That ingest did not exist when this report was written. Reverse-edge candidates assume it will exist; do not link the snapshot.

Source claims used for judging candidates:

1. Automation is not the problem; inappropriate design is. Current automation sits at an *intermediate* level of intelligence. It can take over normal control but not abnormal situations, and it cannot provide the continual feedback that human co-workers provide. It should be made either less intelligent or more intelligent.
2. Silent compensation hides faults. In the China Airlines 747 and fuel-leak cases, the autopilot compensated quietly until it reached its limit. The crew then learned of the fault when the least recovery time remained.
3. The two thought experiments show that the culprit is missing feedback, not automation. The captain delegates either to the autopilot or to a first officer. The human delegate's informal talk keeps everyone informed, while the autopilot gives no such running report. The "incapacitated pilot" case shows the same failure with no automation at all.
4. Feedback needs to be continual, informative and unobtrusive, and it should report trends, not just cross single thresholds. Designers leave it out because "the automation itself doesn't need it."
5. Analysis should cover the whole system. Local fixes, such as a new alarm, retraining or a procedure, can signal poor overall design.
6. The "new irony": problems blamed on overautomation come from automation that is not powerful enough. This deliberately reverses the conclusion Bainbridge draws from the same evidence.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, Outbound links section. The snapshot is never the link author; the ingest is. Authorised destinations are theory, reference, sources, agent-memory-systems, agentic-systems, tags (scan), and external. Excluded: `kb/work/` and `kb/instructions/`. Labels by destination:
- theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`; `defined-in` for theory/definitions
- sources: `compares-with`, `see-also`
- agentic-systems and agent-memory-systems: `compares-with`, `see-also` (agent-memory-systems also allows `is-evidence-for`)
- reference: `see-also` only
- external: `derived-from`, `see-also`

**Type spec read:** `kb/types/connect-report.md`.

**Curated heads:**
- `kb/tags/observability-README.md`. Its Runtime visibility group names [final-task-success](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) and [silent-disambiguation](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md). Both are direct analogues of silent autopilot compensation, so I followed both.
- `kb/tags/warranted-autonomy-README.md` is `complete: true`, so I skipped the by-tag rg and recorded the skip. From the head I flagged [unattended-work](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md), [warranted-transfer](../../../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md), [augmentation-automation boundary](../../../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md), [boundary-of-verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) and [increasing-computational-autonomy](../../../../theory/increasing-computational-autonomy-relocates-human-effort.md).

**Titles listing (theory):**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | grep -i -E 'feedback|silent|hidden|visib|observ|oversight|monitor|automat|human|operator|interact|fallback|recover|degrad|whole|system-level|local fix'`
- This flagged [enforcement-without-structured-recovery](../../../../theory/enforcement-without-structured-recovery-is-incomplete.md), [human-analogies-suggest-functions](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md), [llm-generation-relaxes-goals](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) and [stateful-tools-hidden-schedulers](../../../../theory/stateful-tools-recover-control-by-becoming-hidden-schedulers.md), plus the warranted-autonomy notes above.
- I read the descriptions and bodies of the flagged notes.

**Body search:**
- `rg -il 'bainbridge|ironies of automation|norman|hutchins|out of the loop|in the loop|human-in-the-loop|silent(ly)? compensat|situation awareness|automation complacen|mental model' kb --glob '*.md'` (excluding work and instructions). The relevant hits were the ironies ingest, increasing-computational-autonomy, boundary-of-verification, the warranted-autonomy head and final-task-success. Hits in the agent-memory reviews and retained-archive analysis reports were incidental uses of "in the loop", so I rejected them.
- `ls kb/sources/ | grep -i 'norman|bainbridge|automation|parasuraman|endsley|woods|hutchins|sheridan'` found `ironies-of-automation.ingest.md` and `model-types-levels-human-interaction-automation.ingest.md`. It found no Norman ingest, so the target's ingest is not yet written.
- `rg -n -i 'bainbridge|ironies|irony' kb/theory kb/reference kb/agentic-systems kb/tags`. Only increasing-computational-autonomy and boundary-of-verification cite Bainbridge, and both cite the external PDF.
- `rg -n -i 'alert fatigue|nonintrusive|non-intrusive|interrupt(ion)? cost|escalat(e|ion) (to|the) (human|operator|user)|out[- ]of[- ]the[- ]loop|situation(al)? awareness|mental model|system image|human-on-the-loop' kb/theory kb/reference kb/agentic-systems kb/sources`. Nothing addresses feedback design for supervising operators. The "mental model" hits are unrelated uses.
- `rg -l -i 'human factors|human-factors|aviation|cockpit|autopilot|pilot' kb/sources --glob '*.ingest.md'`. I evaluated `towards-a-science-of-ai-agent-reliability.ingest.md`, which surveys aviation reliability engineering. Its axis is reliability metrics, not operator feedback, so I rejected it. The other hits match "pilot" as a system name.
- `rg -l -i 'silent(ly)? (retr|fall|recover|compensat|swallow)|swallow(s|ed)? (the )?error' kb/agentic-systems kb/sources kb/reference`. The hits were two ADRs and one memory ingest, none about masking failure through compensation. Rejected.
- `rg -n -i 'telemetry|path deviation|degraded' kb/reference -l`. The hits are review-system ADRs and proposals with no operator-feedback angle. There is no see-also candidate in reference.

**Link following:**
- From final-task-success to silent-disambiguation (its extension) and llm-generation-relaxes-goals. Together they form a "silent local repair hides failure" cluster. Norman's autopilot is the physical-control instance of that cluster, and it adds a mechanism the cluster lacks: compensation consumes margin.
- From the ironies ingest's Connections Found: it explicitly defers a `compares-with` to the Parasuraman–Sheridan–Wickens ingest and names the human-factors cluster. Norman is the third member and argues against Bainbridge's conclusion.
- From unattended-work to augmentation-automation boundary and increasing-computational-autonomy. Unattended-work's five-function inventory (purpose, context, correction, evaluation, stopping) has no explicit status-reporting or anomaly-reporting function, which is Norman's central one.

**Destinations skipped:**
- agentic-systems and agent-memory-systems: no review or comparison treats operator feedback from automated control. A 1989 human-factors essay has no shared axis with a specific system review, so I made no candidates.
- theory/definitions: no defined term matches the source's vocabulary (feedback, system image, intermediate automation). No `defined-in` candidate.
- External: the only already-known target is the source URL itself, kept as `derived-from`. I did no open-web prospecting. Hutchins (in press, *Cognition in the Wild*) and Bainbridge are cited by the source, but only Bainbridge is held in the KB, and I treated it under sources.

## Connections Found

- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) -- **is-evidence-for**: Norman's autopilot cases are a non-LLM instance of the note's condition. A compensating controller produces the same observable outcome, a level aircraft, whether or not a fault is present, and no independent execution signal reached the crew. The 727 simulator replication even shows that a technically available cue (the cocked control wheel) was not salient enough to serve as that signal. The cases also qualify the note: under drifting faults, silent compensation accumulates until it saturates. This bears on the note's open question of which failures need synchronous rather than asynchronous signals.
- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) -- **is-evidence-for**: the two thought experiments compare an autopilot with a first officer under the same delegation. The human delegate's informal talk supplies continual status and anomaly reporting that disappears when the delegate is automated. This is a function concealed by successful interactive work, as the note predicts. It also bounds the note: continual state reporting by the delegate is not among the note's five operator functions, which are supplied by the operator, not by the delegate.
- [Warranted transfer out of the human cut leaves people the hardest-to-warrant decisions](../../../../theory/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md) -- **is-evidence-for**: Norman reports that automation "seems to function best when the workload is light and the task routine," leaving the abnormal, highest-workload cases to people. This is period aviation evidence for the residue-composition prediction. It is illustrative, not the before-and-after evidence the note says it lacks.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../theory/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- **compares-with** on the axis of what a system must know about its own abnormal states before humans can step back. Norman's remedy is "less intelligent or more": automation that handles normal cases but cannot flag its abnormal ones sits in the dangerous middle. That matches the note's case of good accuracy with poor discrimination. His proposed signal, "compensating more than usual," is a crude self-assessment route (route a).
- [LLM generation can hide a relaxed goal where human writing exposes a stall](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) -- **compares-with** on the axis of whether failure announces itself at the fault. The silently compensating autopilot gives no "beacon at the fault", just as the fluent LLM output does not, while the human crew's talk does. The two sources differ in mechanism (control saturation versus plausibility argmax), which is why the comparison is useful.
- [Ironies of Automation (Bainbridge 1983)](../../../../sources/ironies-of-automation.ingest.md) -- **compares-with** on the axis of what follows from the same out-of-the-loop and failure-when-needed evidence. Norman accepts Bainbridge's analysis and cites it for the "irony" that automation fails when it is most needed. He then draws the opposite conclusion: automation is not too powerful but not powerful enough, and the fix is feedback design, not keeping humans in manual control.
- [A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- **compares-with** on the axis of the level of automation. Parasuraman, Sheridan and Wickens make level a per-stage design variable judged by its human-performance consequences. Norman argues that an intermediate level of intelligence maximizes difficulty unless it comes with continual feedback. Read together, they show that "intermediate level" is safe only if the system's information-acquisition and analysis stages are presented to the operator.
- [The "Problem" of Automation (NASA NTRS PDF)](https://ntrs.nasa.gov/api/citations/19900004678/downloads/19900004678.pdf) -- **derived-from**: the ingest analysis is worked out from this external original, ICS Report 8904 (1989), later published in Phil. Trans. R. Soc. B, 1990.

## Bidirectional Candidates

- [Ironies of Automation (Bainbridge 1983)](../../../../sources/ironies-of-automation.ingest.md) <-> Norman ingest -- **compares-with**: the ironies ingest already names its human-factors siblings and defers comparisons to future ingests. A return `compares-with` lets a reader of Bainbridge find the explicit reversal of its conclusion. Under the sources contract, this is a new `compares-with` in the ironies ingest's analytical sections, not a change to its quote pool.

## Reverse-edge Candidates

These depend on `kb/sources/norman-problem-of-automation-inappropriate-feedback.ingest.md` existing. Labels come from `kb/theory/COLLECTION.md`.

- [Final task success does not establish intended-path health](../../../../theory/final-task-success-does-not-establish-intended-path-health.md) → Norman ingest -- **evidenced-by**: this is the strongest reverse edge. Under the theory contract's "origin is not corroboration" rule, the context phrase must say that Norman's 1989 cases are independent of how the note was built, and that they qualify the note by showing a drifting fault exhausting a silent compensator. The note was built from tool-loop fallback cases, not these. Whether the cases count as a test the claim could have failed is debatable, so phrase it as qualifying or bounding.
- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) → Norman ingest -- **evidenced-by**: this qualifies the five-function inventory with a function contributed by the delegate (continual status reporting). The inventory's Scope section already says it is not exhaustive, so the edge fits there.
- [Silent disambiguation is the semantic analogue of tool fallback](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) → Norman ingest -- **evidenced-by** (weaker; optional): the "analogue" chain could extend downward from the semantic and tool layers to physical control. Add this only if final-task-success takes the edge first; otherwise it duplicates that edge.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- this note uses Bainbridge's monitoring irony as convergent evidence about verification cost. Norman's argument is about feedback and interaction design, not verification cost. A link would mostly duplicate the Bainbridge edge.
- [Increasing computational autonomy relocates human effort to the frontier](../../../../theory/increasing-computational-autonomy-relocates-human-effort.md) -- its claim is that human attention moves to an elastic frontier. Norman does not address where freed effort goes, and he cites Bainbridge only for the failure-when-needed irony.
- [Enforcement without structured recovery is incomplete](../../../../theory/enforcement-without-structured-recovery-is-incomplete.md) -- Norman's "design should assume the existence of error" matches it only by keyword. The note concerns typed recovery after a hook fires, not feedback to a supervising human.
- [Human analogies can motivate functions without determining component boundaries](../../../../theory/human-analogies-suggest-functions-not-component-boundaries.md) -- Norman does use a human analogy (crew talk) to motivate a function (continual feedback), which superficially fits. But he draws no component-boundary inference, and the note's claim is about that inference. A link would be a keyword match.
- [Stateful tools recover control by becoming hidden schedulers](../../../../theory/stateful-tools-recover-control-by-becoming-hidden-schedulers.md) -- "hidden" here means the location of the scheduler, not hidden fault state. Rejected.
- [Towards a science of AI agent reliability](../../../../sources/towards-a-science-of-ai-agent-reliability.ingest.md) -- it shares the aviation provenance, but its axis is reliability metrics (consistency, robustness, predictability). There is no shared feedback or operator-interaction axis, so `compares-with` would be vague.
- Agent-memory reviews and retained-archive analysis reports that matched "in the loop" -- incidental phrase use.

## Index Membership

These are source tags the future ingest may carry; sources do not participate in tag membership.
- [observability](../../../../tags/observability-README.md) -- this qualifies substantively: the paper explains why the available evidence (a slowly turning control wheel, single-threshold alarms) failed to expose a hidden fault, and what continual feedback would need to report.
- [warranted-autonomy](../../../../tags/warranted-autonomy-README.md) -- this plausibly qualifies under "the human–computation allocation": the paper argues that the level of automation must be judged by its interaction with human operators. Read the head's inclusion condition before assigning; the paper is about control, not decision warrant, so this fit is weaker than observability.

## Synthesis Opportunities

Norman's cases, [final-task-success](../../../../theory/final-task-success-does-not-establish-intended-path-health.md), [silent-disambiguation](../../../../theory/silent-disambiguation-is-the-semantic-analogue-of-tool-fallback.md) and [llm-generation-relaxes-goals](../../../../theory/llm-generation-relaxes-goals-where-human-writing-stalls.md) together suggest a claim not yet stated: **silent local compensation converts a recoverable drift into a late, compressed failure when the compensator has a limit.** The existing notes treat hidden recovery as a non-identifiability problem whose cost is unrepaired infrastructure, which asynchronous maintenance can address. Norman adds a dynamic. When the underlying fault grows and the compensator saturates, the hidden signal arrives exactly when the least time remains. That would decide when synchronous signals are required: when the masked fault can grow, not just when the guarantee changed. The candidate note belongs in theory, would carry the observability tag and would be abstracted from these sources. It needs an agent-runtime instance, such as context-pressure workarounds or retry budgets, before it would earn more than log status.

## Maintenance Observations

- [increasing-computational-autonomy](../../../../theory/increasing-computational-autonomy-relocates-human-effort.md) and [boundary-of-verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) cite Bainbridge by external PDF URL, although the tracked [ironies ingest](../../../../sources/ironies-of-automation.ingest.md) exists. The ironies ingest itself flags this. Durable follow-up: repoint them to the ingest when those notes are next revised.
- The KB now holds three human-factors automation sources (Bainbridge, Parasuraman–Sheridan–Wickens, Norman). None is cited from a theory note through its ingest, and no note covers the feedback-design or delegate-reporting side of this literature.

## Flags

- Tension to keep visible, not resolve: Norman's "new irony" (automation is not powerful enough) contradicts Bainbridge's framing as cited in the KB (automation removes needed human skill). An ingest should state both, not pick one.
- Dependency: every outbound candidate needs the Norman ingest as its author. At the time of this report the ingest had not been written; another agent may be producing it in parallel.
- Not a split candidate. The paper makes one integrated argument (feedback, not automation), even though it touches four topic areas.
