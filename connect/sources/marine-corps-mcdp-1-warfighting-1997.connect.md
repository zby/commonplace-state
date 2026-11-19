---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/marine-corps-mcdp-1-warfighting-1997.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Warfighting

**Source:** [Warfighting](../../../../sources/.snapshots/marine-corps-mcdp-1-warfighting-1997.md)

The source is an immutable local snapshot. Per `kb/sources/COLLECTION.md`, the matching ingest report will carry its authored connection surface.

## Discovery Trace

**Collection contract and destination heads:**

- Read `kb/sources/COLLECTION.md` and its `Outbound links` section. The authored ingest may prospect `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`; it must not link into `kb/work/` or `kb/instructions/`. The applicable labels here are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, and sparse `see-also`.
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source bears directly on transferable planner/executor theory in notes. Reference is Commonplace-specific, agent-memory covers retained-memory systems, and agentic-systems contains whole-system reviews; no candidate in those two descriptive collections passed the articulation test. Sources supplied one task-contingent empirical comparison.
- Read `kb/notes/COLLECTION.md` for the reverse-edge pass. Notes may point to the future ingest with `evidenced-by`, `derived-from`, `abstracted-from`, or sparse `see-also`.

**Full titles and description listings:**

- Generated fresh title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for notes (376 files), reference (157), agent-memory-systems (174), agentic-systems (12), and sources (326). Filtered the resulting surfaces on `execut`, `plan`, `mission`, `intent`, `initiative`, `delegat`, `decentral`, `runtime`, `predict`, `codif`, `methodolog`, `uncertain`, `freedom`, `constraint`, `choice`, and `means`.
- Ran `rg '^description:' kb/notes/ --glob '*.md'` (374 descriptions), then filtered with `rg -ni 'execut|plan|mission|intent|initiative|delegat|decentral|runtime|predict|codif|methodolog|uncertain|freedom|autonom|constraint|choice|means'`. This surfaced the requested planner/executor cluster plus `specification-strategy-should-follow-where-understanding-lives.md`, `specific-intent-may-out-yield-local-rationales-facts-stay-separate.md`, and `agentic-systems-interpret-underspecified-instructions.md`.

**Topic indexes and by-tag sweeps:**

- Read `kb/notes/foundations-README.md`, `computational-model-README.md`, `self-improving-systems-README.md`, and `context-engineering-README.md`. None declares `complete: true`, and no `methodology-README.md` exists, so no by-tag scan was skipped.
- Ran `rg -l '^tags:.*\\bTAG\\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\\s*' -r ''` for `foundations`, `computational-model`, `self-improving-systems`, `context-engineering`, and `methodology`. The sweeps reinforced the codification, execution-time planning, methodology-selection, and weight-activation candidates below.

**Body search:**

- `rg -n -i "mission tactics|commander.?s intent|auftragstaktik" kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'` — three direct note hits: methodology selection, weight-resident behavioral compression, and retained-versus-weight-mediated borrowing. All use *Auftragstaktik* as an example; the source can establish the conventional mission-tactics content but cannot establish that a model reconstructs it from a cue.
- `rg -n -i "decentraliz|delegat(e|ed|ing|ion)|subordinate initiative|freedom.*initiative|choice of means|means.*executor|execution[- ]time|point of (action|decision)" ...` — kept the planner/executor notes below. Rejected AgentOS and generic delegation-system hits because they expose delegation topology without the source's task/intent/local-information mechanism.
- `rg -n -i "stable intent|intent, constraints|goal, the constraints|what done means|assigned (task|result)|purpose.*task|task.*purpose" ...` — kept `fix-what-the-executor-cant-determine-not-what-it-will.md`, `specific-intent-may-out-yield-local-rationales-facts-stay-separate.md`, and `specification-strategy-should-follow-where-understanding-lives.md`.
- `rg -n -i "incomplete information|information.*arrive.*execution|fluidity|changing situation|unforeseen|over.?specif|brittle plan|planning.*uncertain|uncertain.*initiative" ...` — kept the codification and executor-timing candidates. The source itself joins uncertainty, incomplete information, fluidity, local decisions, and subordinate initiative explicitly; generic uncertainty hits in source limitations and vocabulary notes were rejected.

**Link following:**

- Followed the footer neighbourhood of `codifying-predictable-choices-leaves-agents-with-less-predictable-work.md` to the automation/verification and methodology-extension notes. The source directly discriminates repetitive techniques and procedures from tactics requiring judgment, but it does not discuss verification, so the codification note was kept and the automation-boundary note was rejected.
- Followed `fix-what-the-executor-cant-determine-not-what-it-will.md` to `frontloading-spares-execution-context.md`, `design-for-the-first-time-human-except-on-access-cost.md`, and the underspecification note. Frontloading and first-time-human access cost are downstream or differently scoped; controlled underspecification is a direct mechanism match.
- Followed `weight-resident-methodologies-provide-context-efficient-behavioral-compression.md` to methodology selection and followed `borrowing-can-operate-through-retained-artifacts-or-weight-activation.md` to the shared-mechanism transfer note. These links expose the main evidence boundary: doctrine can anchor what the borrowed pattern means, but not model activation fidelity or cross-domain success.

## Connections Found

Recommendations for `kb/sources/marine-corps-mcdp-1-warfighting-1997.ingest.md`, the snapshot's authored surface.

- [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) — **is-evidence-for**: the doctrine separates repetitive techniques and procedures, which can be drilled without variation, from tactics requiring judgment and creativity; it then assigns mission accomplishment under uncertainty to subordinate initiative. This is a source-side instance of moving settled recurring responses out of open-ended choice while leaving situation-dependent work at the executor boundary.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — **is-evidence-for**: mission tactics fixes the assigned task, purpose, authority boundary, and coordination-essential methods while leaving the manner of accomplishment to the subordinate at the point of decision, where local conditions are better known. The military hierarchy and combat assumptions bound the transfer.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) — **is-evidence-for**: MCDP 1 supplies an authoritative doctrinal account of the cluster this note says a compact *Auftragstaktik* cue may activate: purpose, delegated means, initiative, and adaptation. It does not test cue compression, model reconstruction, or activation fidelity.
- [Borrowing can operate through retained artifacts or weight activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) — **is-evidence-for**: the publication is a canonical retained artifact against which the doctrine's explicit-import route can be inspected and against which any claimed weight-mediated reconstruction can be compared. It provides no evidence that a particular model actually activates the right pattern.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) — **is-evidence-for**: the source makes the candidate source-side mechanism precise enough to test rather than importing military doctrine wholesale: execution faces locally changing conditions and incomplete information; the senior fixes purpose and coordination essentials; a competent subordinate selects means within intent and authority. It does not itself establish that agent orchestration shares enough of that mechanism.
- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) — **is-evidence-for**: the source specifies the coherent behavioral regime the note names—mission tactics as intent-framed, initiative-bearing delegated execution—while also showing that this regime rests on trust, competence, and shared understanding. It does not demonstrate that naming the methodology selects it reliably in an LLM.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) — **is-evidence-for**: commander's intent is explicitly presented as a brief statement of purpose that remains useful after a task becomes obsolete and guides many subordinate decisions. This is normative doctrine and conceptual argument, not an empirical measurement of rationale-per-token yield.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — **is-evidence-for**: MCDP 1 says planning farther ahead should impose less precision and that decisions at execution should use situational awareness, while mission tactics leaves live-state choices to the subordinate. It is a military-domain argument for matching advance specification to when information becomes available.
- [Agentic systems interpret underspecified instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) — **is-evidence-for**: mission tactics is deliberate, bounded underspecification of means rather than absence of control; task, purpose, guidance, authority, coordination, and shared doctrine constrain the admissible execution space. The source does not address LLM sampling or prove that natural-language agent instructions reproduce the same control properties.
- [Towards a Science of Scaling Agent Systems](../../../../sources/towards-a-science-of-scaling-agent-systems.ingest.md) — **compares-with**: MCDP 1 gives normative reasons for decentralized execution under fluid local conditions, while the agent-systems paper reports task-contingent empirical effects of centralized and decentralized multi-agent topologies. The topologies and tasks are not equivalent, so the comparison is useful mainly as a warning against turning the doctrine into a general decentralization rule.

## Bidirectional Candidates

None. The snapshot is immutable; useful return directions are recorded under `Reverse-edge Candidates` for later note-side action toward the tracked ingest.

## Reverse-edge Candidates

- [Codifying predictable choices leaves agents with less predictable work](../../../../notes/codifying-predictable-choices-leaves-agents-with-less-predictable-work.md) → future ingest — **evidenced-by**: the doctrine's techniques/tactics distinction and its uncertainty-to-initiative link are a bounded external case for the selection mechanism and planning consequence.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → future ingest — **evidenced-by**: MCDP 1 gives a mature-domain statement of the same information-timing division, including the essential-coordination exception and the competent-executor premise.
- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) → future ingest — **evidenced-by**: the note's *Auftragstaktik* example currently has no source link for the doctrinal content the cue is claimed to reconstruct; this ingest can ground that content while leaving activation efficacy unclaimed.
- [Borrowing can operate through retained artifacts or weight activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) → future ingest — **evidenced-by**: the ingest would give the retained-artifact side of the note's worked example a versioned, inspectable primary source.
- [A borrowed pattern transfers only as far as source and target share a mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) → future ingest — **evidenced-by**: the source is the object against which the mission-tactics mechanism and its military-only machinery can be separated before any agent-system adoption.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) → future ingest — **evidenced-by**: commander's intent is a compact, explicit source-side case of one purpose guiding many local decisions, but the note should preserve that this is doctrinal support rather than yield measurement.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None. Every evaluated candidate has frontmatter.

## Rejected Candidates

- [Design for the first-time human, except on access cost](../../../../notes/design-for-the-first-time-human-except-on-access-cost.md) — the source requires competent subordinates, but this note's claim is about consumer access paths and their processing cost, not delegated judgment.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) — both distinguish what can be settled before execution from what should remain live, but MCDP 1 does not discuss precomputation, context cost, or caller-resolved inputs. The executor-timing note carries the shared mechanism without stretching the analogy.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — the source distinguishes repetitive procedure from judgment but supplies no verification-cost account for why a choice can be automated.
- [AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) — matched on delegation and leader/subordinate topology, but its review does not establish intent-framed autonomy, a local-information advantage, or an equivalent execution contract.
- Generic reference and agent-memory hits on `delegation`, `planning`, and `intent` — rejected as vocabulary overlap. No Commonplace current-state document or retained-memory-system review gains a concrete reader path from this military doctrine.

## Index Membership

None. `kb/sources/README.md` describes the collection rather than enumerating ingests, and the relevant tag READMEs index notes rather than sources.

## Synthesis Opportunities

The source and the planner/executor notes suggest a compact transferable candidate mechanism: **fix the result, purpose, constraints, authority boundary, and coordination essentials that execution cannot safely reconstruct; delegate means whose premises arrive at the point of action; require the executor to remain aligned to intent and to report rather than await permission.** MCDP 1 also makes competence, trust, shared doctrine, and a fluid local-information advantage preconditions. Whether agent work actually shares those preconditions requires target-side evidence; the doctrine alone does not license adoption.

## Maintenance Observations

None.

## Flags

- The snapshot is the complete 20 June 1997 MCDP 1 publication and presents authoritative but non-prescriptive Marine Corps doctrine. Its claims are normative doctrine embedded in a broader maneuver-warfare theory, not experimental evidence about organizational or agent performance.
- Several current notes use *Auftragstaktik* as a compact methodology cue. MCDP 1 uses the Marine Corps term *mission tactics* and does not establish that the terms are interchangeable in every historical or doctrinal sense.
