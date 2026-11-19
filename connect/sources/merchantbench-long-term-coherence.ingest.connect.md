---
description: "Post-ingest discovery for MerchantBench's distinction between created skills, recorded use, and beneficial learning"
type: kb/reports/types/connect-report.md
source: "kb/sources/merchantbench-long-term-coherence.ingest.md"
source_has_frontmatter: true
date: "2026-09-25"
depth: standard
---

# Connection Report: MerchantBench ingest

**Source:** [MerchantBench ingest](../../../../sources/merchantbench-long-term-coherence.ingest.md)

## Discovery Trace

- Read the accepted ingest fully and reread the source's pre-ingest discovery report. The full 2,467-line snapshot had already been read during this batch's pre-ingest pass; this pass evaluates the accepted analysis as its own authored target.
- Reused this batch's fully read source/report and destination collection contracts, destination README heads, and complete fresh title listings for notes, reference, agent-memory-systems, agentic-systems and sources. The ingest carries domains, not tags; no tag-completeness shortcut applies.
- Fresh description query over all five destinations: `rg -n -i '^description:.*(merchant|delayed feedback|memory.*effect|policy revision|persistent.*operation)'`. Effects-based evaluation was the strongest direct match; embedding-memory forgetting is a different mechanism and was rejected.
- Fresh body query: `rg -l -i 'delayed feedback|skill.*(creation|use)|memory-specific|policy revision|WITH/WITHOUT'` over memory-requirement notes and the other four destinations. This confirmed PAST-Bench as a concrete intervention comparator and found many generic skill-use matches that did not improve on the direct effects note.
- Notes: reread effects-based evaluation and governing behavior-changing writes fully. Reused previously full reads of fixed decomposition, conjectural learning, active work state, experimental contrasts and program theory. The accepted ingest's central distinction supports the effects note; governance is a bounded risk illustration. The fixed-decomposition and learning-definition links remain appropriate to the ingest's explicitly analytical section.
- Sources: reused the fully read PAST-Bench analysis; its retention-access intervention gives a specific comparison that whole-framework MerchantBench runs cannot supply. Link following from PAST-Bench to effects evaluation and experimental contrasts keeps persistence, activation, uptake and outcome distinct.
- Reference: the description scan and body matches yield generic memory-coverage and governance documents, not a more useful merchant-evaluation companion. No reference edge retained.
- Agent-memory-systems: the earlier full Hermes review read and current skill-use scan identify a possible implementation comparator, but the accepted ingest explicitly excludes implementation inspection and does not depend on that comparison. No new edge recommended to it in this pass.
- Agentic-systems: current body matches concern general skill and workflow persistence. None offers a sharper comparison than the retained effects and experimental-design targets; no main-system edge recommended.
- Candidate paths checked. The notes contract was rechecked for `evidenced-by` authorization to sources. No external prospecting; only the supplied primary URL was retained. No library changes made.

## Connections Found

- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) — **is-evidence-for**: the ingest's existing connection separates skill creation, recorded use, and business outcomes while explicitly withholding memory-specific causal attribution. Retain this bounded empirical use.
- [Governing behaviour-changing writes](../../../../notes/continual-learning-requires-governing-behaviour-changing-writes.md) — **is-evidence-for**: the existing connection uses an erroneous operating belief and declining shelf size as a risk illustration, without claiming that memory caused the loss or that a specific governance intervention would prevent it.
- [Learning inside a fixed decomposition](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — **compares-with**: the existing learning analysis identifies the simulator objective, action interface and hidden dynamics as outside the agents' update space; success within it does not compare those fixed design choices.
- [Conjectural learning](../../../../notes/definitions/conjectural-learning.md) — **defined-in**: the existing definition link lets readers distinguish possible evidence-responsive revision from demonstrated improvement through criticism of retained theory content.
- [PAST-Bench](../../../../sources/past-bench-personal-agents-pdf.ingest.md) — **compares-with**: an optional new connection would contrast retained-state access across fresh sessions with MerchantBench's continuous operation and framework-bundle comparison. The contrast clarifies which experiment can identify persistence effects.
- [MerchantBench paper](https://arxiv.org/abs/2607.28956) — **derived-from**: existing primary-source citation for the analysis.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Evaluate Memory By Effects, Not By Existence](../../../../notes/agent-memory-requirements/evaluate-memory-by-effects.md) → [MerchantBench ingest](../../../../sources/merchantbench-long-term-coherence.ingest.md) — **evidenced-by**: add a bounded example separating creation counts, recorded use and outcomes, retaining the missing memory-specific intervention beside it. Because the Quotes section is empty, a source-dependent note use currently requires the exact `(snapshot required)` marker in its ingest link text, or a separately commissioned grounding pass before ordinary citation.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Program theory under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) — delayed effects alone do not establish a theory-holder mechanism or a program-modification intervention.
- [Active work state](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) — the original snapshot's horizon-confusion episode could support this comparison, but the accepted ingest does not analyze that episode. It is not a necessary extension of this artifact's central contribution.
- [Experimental contrasts](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) — the ingest already explains the bundle confound directly; another general methodology edge adds little beyond the concrete PAST-Bench comparison.

## Index Membership

None

## Synthesis Opportunities

None. Effects-based memory evaluation already owns the transferable distinction.

## Maintenance Observations

None

## Flags

- Recommended next action: update the effects-based evaluation note with this bounded case, keeping the absence of a memory-specific intervention next to the example. Discovery does not authorize or perform that note edit.
- Preserve the three-run configuration samples, three human participants, simulated 365-day horizon, framework-bundle confound and observational status of memory-error traces.
- Inbound candidate disposition: one reverse evidence candidate reported; no inbound or outbound library edge authored by this pass.
