---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Intent-framed delegation is a control regime; prompt length does not establish it

**Source:** [Intent-framed delegation is a control regime; prompt length does not establish it](../../../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md)

## Discovery Trace

**Setup and source read:**
- Read [connect-report](../../../../types/connect-report.md), [kb/notes/COLLECTION.md](../../../../notes/COLLECTION.md), and the full source artifact.
- Source claim: consequential planner-executor handoffs preserve intent only when the surrounding system governs authority, information, composition, feedback, and recovery; prompt brevity alone does not establish that control relation.

**Curated heads:**
- Read [Notes](../../../../notes/README.md) and [Tags](../../../../tags/README.md). `tags-README.md` is marked `complete: true`, but the source note has no `tags:`, so no tag-README by-tag scans were authorized or needed.
- Read [Types](../../../../types/README.md), [Reference](../../../../reference/README.md), [Agentic Systems](../../../../agentic-systems/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Sources](../../../../sources/README.md), and [Instructions](../../../../instructions/README.md) to identify plausible destination surfaces before body reads.
- Read [Computational model](../../../../tags/computational-model-README.md), [Tool loop](../../../../tags/tool-loop-README.md), and [Context engineering](../../../../tags/context-engineering-README.md) while checking possible index membership.

**Title surface:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ kb/types/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'` gave the complete fresh title surface across authorized destinations. Promising note-side candidates were the orchestration, delegation, and methodology-selection cluster; no type title suggested a direct definition or contract link stronger than the note's ordinary prose.

**Description listing scan:**
- `rg '^description:' kb/notes/ --glob '*.md' | rg 'delegat|authority|orchestrat|intent|coordination|constraint|control|executor|boundary|handoff'` flagged [fix-what-the-executor-cant-determine-not-what-it-will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md), [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md), [runtime-structure-determines-governance-control-surfaces](../../../../notes/runtime-structure-determines-governance-control-surfaces.md), [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md), [orchestration-needs-privilege-quarantine-not-permission-scope](../../../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md), and nearby orchestration notes. Kept the design-space and runtime-governance notes; rejected prompt-refinement and privilege-quarantine as narrower side questions; treated `fix-what-the-executor...` as already linked.
- `rg '^description:' kb/reference/ --glob '*.md' | rg 'delegat|authority|orchestrat|control|sub-agent|workflow|instruction|agent'` flagged [content-routing](../../../../reference/content-routing.md), [control-plane-goals](../../../../reference/control-plane-goals.md), and [harness-sub-agent-model-selection-regression](../../../../reference/harness-sub-agent-model-selection-regression.md). Read them; kept none as outbound connections because `control-plane-goals` already links back to the source, `content-routing` is a routing analogue rather than a traversal need from this note, and the harness regression is too provenance-specific.
- `rg '^description:' kb/agentic-systems/ --glob '*.md'` plus `rg -n 'delegat|authority|orchestr|sub-agent|control|supervision|mission command|intent' kb/agentic-systems/ --glob '*.md'` flagged [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md), [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md), [Swamp](../../../../agentic-systems/reviews/swamp.md), [GBrain](../../../../agentic-systems/reviews/gbrain.md), and [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md). Read Agno and dynamic workflows in full; kept Agno as the strongest target-side example of delegated execution governed by approvals, resources, supervision, and retained upstream responsibility; rejected dynamic workflows as too centered on orchestration API shape and withheld surfaces rather than the full consequential-control packet.
- `rg '^description:' kb/instructions/ --glob '*.md' | rg 'delegat|authority|handoff|sub-agent|review|control|workflow'` plus `rg -n 'delegat|authority|handoff|sub-agent|worker|orchestr|escalat|verification' kb/instructions/ --glob '*.md'` flagged [Write an Instruction](../../../../instructions/write-instruction.md), [run-review-batches](../../../../instructions/run-review-batches.md), and [kb/instructions/COLLECTION.md](../../../../instructions/COLLECTION.md). Kept `write-instruction` as a reverse-edge and off-authorisation case because the procedural packet matches this note's control surfaces, but the natural instruction-side label is `rests-on`, which the source collection does not authorize outbound to instructions.
- Read [Types](../../../../types/README.md) and surveyed type titles; no type-level candidate passed the articulation test, so `kb/types/` was skipped after prospecting.

**Body search:**
- `rg -n 'delegat|intent-framed|authority|control regime|executor|handoff|coordination guarantees|point-of-action|means|upstream|boundary' kb/notes/ --glob '*.md'` confirmed the source-side cluster and surfaced [specific-intent-may-out-yield-local-rationales-facts-stay-separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) and [compiling-coordination-preserves-primitive-not-aggregate-authority](../../../../notes/compiling-coordination-preserves-primitive-not-aggregate-authority.md). Read both; rejected the intent note as a design-rationale analogue rather than a delegated-execution neighbor and the compilation note as a different authority problem.
- `rg -n 'intent-framed-delegation-is-a-control-regime-not-a-short-prompt|intent-framed delegation|control regime' kb/agentic-systems/ kb/reference/ kb/instructions/ kb/notes/ --glob '*.md'` surfaced existing inbound uses in [capable-agents-need-methodology-selection](../../../../notes/capable-agents-need-methodology-selection.md), [borrowing-can-operate-through-retained-artifacts-or-weight-activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md), [weight-resident-methodologies-compress-behavior-in-context](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md), and [control-plane-goals](../../../../reference/control-plane-goals.md). Kept the methodology-selection and weight-resident notes as outbound candidates from the source; rejected `control-plane-goals` because the reference-side rationale link already exists and is sufficient.
- `rg -n 'intent-framed delegation|control regime|short prompt|delegation|mission command|Auftragstaktik|fix what the executor' kb/sources/marine-corps-mcdp-1-warfighting-1997.ingest.md kb/sources/us-army-adrp-6-0-mission-command-2012.ingest.md kb/sources/david-stahel-auftragstaktik-mission-command.ingest.md` showed that all three source ingests already carry outbound links back to this note. No new source-side reverse edge was needed.
- External prospecting was skipped. The source collection authorizes reserved `external`, but no already-known external target outside the loaded local artifacts offered a better connection than the existing ingests and agentic-system analyses.

**Link following:**
- Opened [agent-orchestration-occupies-a-multi-dimensional-design-space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md), [runtime-structure-determines-governance-control-surfaces](../../../../notes/runtime-structure-determines-governance-control-surfaces.md), [conversation-vs-prompt-refinement-in-agent-to-agent-coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md), [subtasks-that-need-different-tools-force-loop-exposure-in-agent](../../../../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md), [orchestration-needs-privilege-quarantine-not-permission-scope](../../../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md), [the-practical-scheduler-is-the-host-language](../../../../notes/the-practical-scheduler-is-the-host-language.md), and [bounded-context-orchestration-model](../../../../notes/bounded-context-orchestration-model.md). Kept only the design-space and runtime-governance notes because they sharpen the source note's control-regime argument rather than merely sharing the orchestration topic.
- Opened [weight-resident-methodologies-compress-behavior-in-context](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md), [capable-agents-need-methodology-selection](../../../../notes/capable-agents-need-methodology-selection.md), and [borrowing-can-operate-through-retained-artifacts-or-weight-activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md). Kept the first two; rejected `borrowing-can-operate...` as redundant once the more specific cue-compression and methodology-selection notes are present.
- Opened [behavioral-authority](../../../../notes/definitions/behavioral-authority.md), [content-routing](../../../../reference/content-routing.md), [harness-sub-agent-model-selection-regression](../../../../reference/harness-sub-agent-model-selection-regression.md), [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md), [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md), [Write an Instruction](../../../../instructions/write-instruction.md), [kb/instructions/COLLECTION.md](../../../../instructions/COLLECTION.md), and the three cited ingests to verify reverse-edge and off-authorisation judgments.

## Connections Found

- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) -- **mechanism**: the source note's claim that a compact cue can be adequate only when it reliably activates the intended mechanism is exactly the cue-compression boundary this note explains.
- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) -- **extends**: the source note supplies one bounded case where a methodology cue matters, and sharpens why a bare `Auftragstaktik` label is not enough when consequential choices depend on which governing method becomes active.
- [Runtime structure determines the control surfaces available to governance](../../../../notes/runtime-structure-determines-governance-control-surfaces.md) -- **mechanism**: the source note's authority, context, ownership, feedback, and recovery surfaces become operative only when the runtime externalizes the corresponding governance handles.
- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) -- **extends**: the source note gives a sharper account of the delegation/governance part of that design space by specifying what an intent-preserving control regime must govern at a consequential handoff.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- **evidenced-by**: Agno is a concrete target-side system where delegated execution is bounded by approvals, resource assignment, supervision, and retained upstream responsibility rather than by prompt wording alone.

## Bidirectional Candidates

- [Agent orchestration occupies a multi-dimensional design space](../../../../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) <-> source -- **extends**: the design-space note names a governance family for delegation chains but does not yet point to this note's fuller control-regime account.

## Reverse-edge Candidates

- [Write an Instruction](../../../../instructions/write-instruction.md) -> source -- **rests-on**: its consequential delegated-work packet fixes result, constraints, owned outputs, inputs, coordination, verification, and stop or escalation conditions, which are the same control surfaces this note says must be governed.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -> source -- **rests-on**: the Agno analysis treats delegated execution as bounded by approvals, resources, supervision, and retained responsibility; this note is the theory artifact that explains why those controls matter beyond prompt text.

## Off-authorisation Candidates

- [Write an Instruction](../../../../instructions/write-instruction.md) -- the source note clearly connects to this procedure, but the natural reader-need is instruction-side `rests-on`, not a source-side note→instruction label. `operationalized-from` may be arguable, but this looks better authored from the instruction side unless `kb/notes/COLLECTION.md` wants this methodology-to-procedure edge made explicit.

## Raw Text Candidates

None

## Rejected Candidates

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- already linked directly and already links back; no new candidate edge is needed.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- already linked directly and already does the specific guarantee work the source note builds on.
- [Conversation vs prompt refinement in agent-to-agent coordination](../../../../notes/conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) -- shares the handoff surface, but its question is trace preservation versus clean re-dispatch, not whether the surrounding system governs consequential delegation well enough.
- [Agent orchestration needs a privilege quarantine, not just a permission scope](../../../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) -- a real sibling case, but it isolates one security control surface rather than the full five-surface delegation regime.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- useful analogy for why upstream intent matters, but its direct subject is design-rationale retention rather than delegated execution.
- [Borrowing can operate through retained artifacts or weight activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) -- relevant, but redundant once the more specific methodology-selection and weight-resident cue notes are included.
- [Control-plane goals](../../../../reference/control-plane-goals.md) -- already links to the source note from the reference side; adding a source->reference edge would add little traversal value.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- a useful nearby harness, but the retained analysis is more about orchestration API shape and withheld control surfaces than about a complete consequential delegation regime.
- [Ingest: MCDP 1, Warfighting (1997)](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md), [Ingest: ADRP 6-0: Mission Command](../../../../sources/us-army-adrp-6-0-mission-command-2012.ingest.md), and [Ingest: Auftragstaktik and Mission Command](../../../../sources/david-stahel-auftragstaktik-mission-command.ingest.md) -- all three are already cited by the source and already link back to it from their authored ingest surfaces.

## Index Membership

- [Computational model](../../../../tags/computational-model-README.md) -- the note belongs in the Scheduling & Orchestration cluster beside design-space, coordination-guarantee, and prompt-framing notes, even though it currently has no tags routing it there.

## Synthesis Opportunities

- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) + [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) + [Intent-framed delegation is a control regime; prompt length does not establish it](../../../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md) + [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) imply a higher-order claim: a compact methodology cue is adequate only when content warrant, activation fidelity, and surrounding control regime all hold; prompt brevity by itself establishes none of the three.

## Maintenance Observations

- The source note currently has no `tags:` even though discovery and index fit place it in the computational-model orchestration cluster. That leaves curated traversal dependent on lexical search and inbound links rather than tag routing.

## Flags

- None
