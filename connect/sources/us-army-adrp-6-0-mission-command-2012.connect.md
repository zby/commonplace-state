---
description: "Discovery report for possible KB connections from ADRP 6-0: Mission Command"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/us-army-adrp-6-0-mission-command-2012.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: ADRP 6-0: Mission Command

**Source:** [ADRP 6-0: Mission Command](../../../../sources/.snapshots/us-army-adrp-6-0-mission-command-2012.md)

## Discovery Trace

**Collection rules:** Read `kb/sources/COLLECTION.md`. The target is an immutable local snapshot, so every outbound recommendation below is for the matching ingest's future authored surface; no durable artifact should link to `.snapshots/`. Authorised local destinations are notes, reference, agent-memory systems, agentic systems, and other sources. Work and instructions are excluded. External prospecting was skipped because the original Army PDF is already recorded in the snapshot.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. These routed discovery toward specification, orchestration, delegation, and coordination; no reference or agent-memory target survived candidate evaluation.
- The source carries no `tags`, so no tag README or by-tag scan applied.

**Full title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` over notes, reference, agent-memory systems, agentic systems, and sources, scanning 376, 157, 174, 12, and 327 headings respectively.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md'` over all five destinations, scanning 374, 156, 172, 10, and 327 descriptions respectively. The strongest description matches concerned executor discretion, methodology selection, governing intent, coordination guarantees, mission tactics, intelligent delegation, and verified shared context.

**Body search:**

- `rg -n -i "commander.?s intent|mission command|mission orders|disciplined initiative" kb/notes/ --glob '*.md'` -- found the two notes that explicitly name intent-based command or *Auftragstaktik* and the executor-boundary neighborhood.
- `rg -n -i "shared intent|specific intent|governing intent|intent.{0,40}(execution|executor|subordinat|delegat)" kb/notes/ --glob '*.md'` -- kept the specific-intent conjecture and rejected generic uses of intent without a delegation mechanism.
- `rg -n -i "delegat(e|ed|es|ing|ion)|decentrali[sz]|freedom of action|unity of effort|mutual trust" kb/notes/ --glob '*.md'` -- kept the transfer-warrant and coordination-guarantee notes; generic delegation mentions failed the articulation test.
- Ran the same mission-command, intent, delegation, trust, and accountability searches over `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. No Commonplace reference or memory-system review passed; Autogenesis and four source comparisons did.
- `rg -n -i "results? to be attained|outcomes?.{0,30}not.{0,20}how|executor.{0,40}determin" kb/notes/ --glob '*.md'` -- confirmed the direct match between mission orders that specify results rather than methods and the executor-boundary claim.

**Link following:**

- Followed [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) to its competent-executor and semantic-underspecification premises. ADRP 6-0 supplies the same competence-and-uncertainty boundary but does not establish LLM semantics.
- Followed [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) to the weight-resident-methodology note. The doctrine grounds what the named *Auftragstaktik* cluster contains, not whether a compact cue activates it reliably in a model.
- Followed [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) to the rationale-transfer neighborhood. The Army's short commander-intent form is a useful operational comparison but does not test the note's per-token conjecture.
- Followed [Borrowed patterns transfer only over shared mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) to Commonplace's source-adoption policy, and [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) to Intelligent AI Delegation and Tracecraft. This exposed the central transfer limit: trained human subordinates, professional trust, lawful authority, feedback, and retained accountability are not automatically reproduced by agent prompts or shared storage.
- Followed the local source neighborhood through Marine Corps MCDP 1, Intention Is All You Need, Intelligent AI Delegation, and DeLM. They provide distinct comparison axes: sibling doctrine, structured shared purpose, accountable authority transfer, and verification-gated shared state.

## Connections Found

- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **is-evidence-for**: ADRP 6-0 is an independent mature-domain instance of fixing purpose, desired end state, constraints, resources, and essential coordination while leaving situation-dependent means to a competent executor under uncertainty. It is doctrinal evidence for the boundary, not outcome evidence that the doctrine succeeds.
- [A capable agent needs methodology selection, not just relevant knowledge](../../../../notes/capable-agents-need-methodology-selection.md) -- **is-evidence-for**: the official doctrine specifies the coherent cluster invoked by the note's *Auftragstaktik* example—central intent, delegated means, disciplined local initiative, adaptation, and constraints—while supplying no evidence that an LLM reconstructs that cluster from the short cue.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- **compares-with**: the Army prescribes a concise purpose, key tasks, and end state as the basis for subordinate action when plans or communications fail; this is operational convergence on intent as a high-leverage inference seed, but it does not compare per-token yield or show that intent recovers contingent facts.
- [Borrowed patterns transfer only over shared mechanism](../../../../notes/borrowed-patterns-transfer-only-over-shared-mechanism.md) -- **rests-on**: any attempt to turn this military-human doctrine into agent-orchestration guidance depends on identifying which mechanisms actually carry over and testing the rest on the target; competence, trust, shared experience, lawful authority, and accountability are material source-side assumptions.
- [Agent orchestration needs coordination guarantees, not just coordination channels](../../../../notes/agent-orchestration-needs-coordination-guarantees-not-just.md) -- **compares-with**: mission command governs dispersed execution with clear intent, mutual trust, shared understanding, feedback, and retained commander responsibility, providing a socio-organizational comparison for the explicit guarantees an engineered multi-agent channel would need.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- **compares-with**: current Autogenesis delegates model-selected concurrent work while leaving decomposition and review prompt-guided; ADRP 6-0 shows that decentralised execution is not absence of control but a regime built on explicit intent, trained judgment, feedback, and accountability.
- [MCDP 1, Warfighting (1997)](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) -- **compares-with**: the Marine doctrine is a close independent formulation of task-and-purpose delegation under friction; comparing it with ADRP 6-0 separates shared mission-tactics mechanisms from service-specific doctrine and prevents either text from carrying the analogy alone.
- [Intention Is All You Need](../../../../sources/intention-is-all-you-need-2022428696595108152.ingest.md) -- **compares-with**: the essay makes structured shared intention a human-agent coordination surface, while ADRP 6-0 specifies what such intent contains and embeds it in competence, trust, authority, resources, feedback, and evaluation rather than treating intention as a sufficient control layer.
- [Intelligent AI Delegation](../../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md) -- **compares-with**: both accounts couple delegated authority to responsibility, accountability, trust, and bounded autonomy; ADRP 6-0 retains commander responsibility after delegation, whereas the AI framework adds verifiability, oversight, permission, and liability-firebreak mechanisms for recursive delegation chains.
- [Decentralized Multi-Agent Systems with Shared Context](../../../../sources/decentralized-multi-agent-systems-with-shared-context.ingest.md) -- **compares-with**: DeLM engineers parts of shared understanding through verified, reference-grounded, atomically published state, offering a concrete comparison with the Army's socially maintained trust and common operational picture while leaving intent and accountability outside its measured mechanism.

## Bidirectional Candidates

- [MCDP 1, Warfighting (1997)](../../../../sources/marine-corps-mcdp-1-warfighting-1997.ingest.md) <-> source -- **compares-with**: readers of either doctrine benefit from the sibling account because their shared uncertainty-to-intent-to-local-initiative mechanism makes their separate transfer assumptions easier to identify.
- [Intelligent AI Delegation](../../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md) <-> source -- **compares-with**: the return path would contrast retained human command responsibility with an AI delegation framework's proposed verification and liability controls.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Weight-resident methodologies provide context-efficient behavioral compression](../../../../notes/weight-resident-methodologies-compress-behavior-in-context.md) -- ADRP 6-0 defines the content behind the *Auftragstaktik* example but says nothing about model-weight storage, short-cue activation, reconstruction fidelity, or context efficiency; the methodology-selection note is the narrower useful landing.
- [Agentic systems interpret underspecified natural-language instructions](../../../../notes/agentic-systems-interpret-underspecified-instructions.md) -- mission orders intentionally leave methods open, but a human command doctrine does not establish the note's separate LLM semantic-underspecification and execution-indeterminism mechanisms.
- [Source adoption policy](../../../../reference/source-adoption-policy.md) -- it governs Commonplace's local adoption process rather than the Army doctrine; the transfer-mechanism note carries the reader need without an incidental source-to-reference `see-also` edge.
- [Claude Code dynamic workflows](../../../../agentic-systems/reviews/claude-code-dynamic-workflows.md) -- the system exposes model-authored scheduling and sub-agent prompts, but its analysis does not describe an intent-and-accountability regime; Autogenesis provides the more direct delegated-execution comparison.
- [Tracecraft](../../../../agent-memory-systems/reviews/tracecraft.md) -- its claims, mailboxes, barriers, and shared state instantiate coordination channels, but the review does not analyze commander intent, bounded initiative, or authority transfer.

## Index Membership

None. The sources README does not enumerate individual ingests, and the target is a local snapshot rather than a library artifact.

## Synthesis Opportunities

- **Intent-framed delegation is bounded autonomy, not mere under-specification.** ADRP 6-0, the executor-boundary note, the coordination-guarantee note, and Intelligent AI Delegation jointly imply that useful discretion requires a purpose and end state plus competence, resources, shared context, feedback, authority bounds, and answerability. Removing those preconditions changes mission command into ungoverned delegation.
- **A methodology cue has two independent warrants.** Doctrine can ground the coherent content associated with *Auftragstaktik*; separate target-side evidence must establish that a particular model reconstructs that content faithfully and applies it successfully from a compact cue.

## Maintenance Observations

- No matching `kb/sources/us-army-adrp-6-0-mission-command-2012.ingest.md` existed during discovery. Until that authored surface exists, reverse edges should not be proposed because the sources contract forbids durable links to the hidden snapshot.

## Flags

- **Partial-capture limit:** the snapshot declares `capture_scope: partial-source`; source-dependent details should be checked against the original Army PDF or a future name-paired ingest before durable use.
- **Cross-domain transfer limit:** the publication states military doctrine for trained people inside a hierarchy. It does not test LLM agents, prompts, multi-agent architectures, or the effectiveness of transferring its command philosophy to them.
- **Split candidate for downstream theory extraction:** the source makes independent contributions across at least three clusters—intent and mission orders, trust/initiative/risk, and information/control/accountability. The immutable snapshot should not be split, but future theory work should not force all clusters into one note.
