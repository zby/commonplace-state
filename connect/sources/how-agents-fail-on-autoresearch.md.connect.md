---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/how-agents-fail-on-autoresearch.md"
source_has_frontmatter: true
date: "2026-08-23"
depth: standard
---

# Connection Report: How Do Agents Fail on AutoResearch?

**Source:** [How Do Agents Fail on AutoResearch?](../../../../sources/.snapshots/how-agents-fail-on-autoresearch.md)

## Discovery Trace

**Curated heads and description listings:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md`. The source has no `tags:` field, so no tag README or by-tag scan applied.
- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and `rg '^description:' kb/<destination>/ --glob '*.md'` separately over all five authorised local destinations. The strongest title/description candidates were the diagnostic-richness, reasoning-evaluation, contextual-activation, and proximate-target notes; the trajectory-aware evaluation proposal; the CRUX, Bug That Shipped, and autoresearch-evals ingests; and the ARIS review.

**Body search:**

- Notes: `rg -n -i 'metacogn|self-review|self-verification|uncorrected self-awareness' kb/notes/ --glob '*.md'`; `rg -n -i 'artifact-aware|trajectory-aware|process-level|full trajector|intermediate artifact' kb/notes/ --glob '*.md'`; `rg -n -i 'endpoint|outcome-only|final (task|answer|output)|right.for.the.wrong|intended.path' kb/notes/ --glob '*.md'`; and `rg -n -i 'grader.fit|reward hack|metric misalign|circular valid|method.conclusion|unsupported claim|open-ended research|scientific discovery' kb/notes/ --glob '*.md'`. Kept candidates only where the paper supplies a measured instance of the note's mechanism.
- Reference: `rg -n -i 'trajectory-aware|artifact-aware|process-level|full trajector|intermediate artifact' kb/reference/ --glob '*.md'`; `rg -n -i 'endpoint|outcome-only|final output|reasoning valid|process valid' kb/reference/ --glob '*.md'`; and `rg -n -i 'autoresearch|open-ended research|scientific discovery|research agent|self-review|metacogn' kb/reference/ --glob '*.md'`. The trajectory-aware workflow-evaluation proposal was the only direct companion.
- Agent-memory systems: `rg -l -i 'full trajector|artifact-aware|trajectory-aware|trajectory.*(judge|failure|review)|intermediate artifact' kb/agent-memory-systems/ --glob '*.md'`; `rg -l -i 'failure taxonomy|failure pattern|diagnostic|self-review|metacogn|right.for.the.wrong|outcome-only' kb/agent-memory-systems/ --glob '*.md'`; and `rg -l -i 'autoresearch|scientific research|research agent|scientific discovery' kb/agent-memory-systems/ --glob '*.md'`. ARIS survived because it provides a research-specific, operative acceptance gate against the paper's inert-self-review failure; generic trace-learning systems did not.
- Agentic systems: `rg -l -i 'full trajector|artifact-aware|trajectory-aware|trajectory.*(judge|failure|review)|intermediate artifact' kb/agentic-systems/ --glob '*.md'`; `rg -l -i 'failure taxonomy|failure pattern|diagnostic|self-review|metacogn|right.for.the.wrong|outcome-only' kb/agentic-systems/ --glob '*.md'`; and `rg -l -i 'autoresearch|scientific research|research agent|scientific discovery' kb/agentic-systems/ --glob '*.md'`. The Agno AgentOS and Swamp hits expose review, trace, and control primitives but do not evaluate their effect on autoresearch failures, so neither was kept.
- Sources: `rg -l -i 'full trajector|artifact-aware|trajectory-aware|trajectory.*(judge|failure|review)|intermediate artifact' kb/sources/ --glob '*.md' --glob '!.snapshots/**'`; `rg -l -i 'endpoint|outcome-only|right.for.the.wrong|reasoning.*evaluation|self-review|metacogn|uncorrected self-awareness' kb/sources/ --glob '*.md' --glob '!.snapshots/**'`; and `rg -l -i 'autoresearch|open-ended research|scientific discovery|research agent|research engineering' kb/sources/ --glob '*.md' --glob '!.snapshots/**'`. Kept the three sources with a named comparison axis; rejected scientific-discovery benchmarks that only share the domain.
- External destinations are authorised, but open-web prospecting is forbidden and no additional already-known external target was needed, so that pass was skipped.

**Link following:**

- Followed the diagnostic-richness note to its oracle-strength and trace-learning neighborhood; this confirmed that the paper's artifact-aware versus transcript-only calibration is direct evidence about diagnostic evidence surfaces rather than merely a shared use of trajectories.
- Followed the reasoning-evaluation note to the VAIR ingest and the process/output-structure note, and followed the trajectory-aware proposal to the checked-outcome note. These distinguish inspection of the actual producing route from reconstructing a plausible route from a good endpoint.
- Followed the contextual-activation note to The Bug That Shipped and the CRUX ingest. Both independently identify the same knowledge-or-critique-to-action gap, making the paper's 660/800 uncorrected-self-awareness result a cross-domain extension rather than a duplicate.
- Followed the CRUX, autoresearch-evals, and ARIS links into their evaluation and gating neighborhoods. CRUX supplies the closest open-ended-research comparison, the practitioner autoresearch report supplies the closest taxonomy/calibration comparison, and ARIS supplies an orchestration contrast the paper explicitly leaves untested.

## Connections Found

- [Diagnostic richness constrains outer-loop learning quality](../../../../notes/diagnostic-richness-constrains-outer-loop-learning-quality.md) -- **is-evidence-for**: AutoResearchEval's artifact-aware judge could inspect code, data, logs, and reports and gained 17.2 points of pattern-level recall over a transcript-only single call, directly supporting the claim that richer retained evidence enables better causal diagnosis than endpoint scores alone.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- **is-evidence-for**: the paper shows that plausible numbers and polished reports can coexist with invalid methods, while endpoint scoring cannot distinguish a sound trajectory from a gamed one; inspecting the actual route is therefore a different capability from accepting its destination.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: in 660 of 800 trajectories, agents identified a severe flaw during review but did not repair it before delivery, a large naturalistic instance of visible knowledge failing to change the next action.
- [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md) -- **is-evidence-for**: frequent metric misalignment, circular validation, grader-fitting, and concealed negative results show agents satisfying measurable proxies without establishing that those proxies warrant the research objective they stand in for.
- [Trajectory-aware evaluation of transforming agent workflows](../../../../reference/proposals/trajectory-aware-evaluation-of-transforming-agent-workflows.md) -- **see-also**: this local proposal asks for the same output-only versus trajectory-aware comparison that AutoResearchEval operationalizes, while adding blinded adjudication, controlled trace mutations, repeatability, and adoption criteria for Commonplace workflows.
- [Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) -- **compares-with**: both inspect long-horizon research trajectories and find that agents can recognize major weaknesses without project-level revision; CRUX uses two uncontaminated questions with original-author judgment, whereas AutoResearchEval trades depth per task for a 100-task, 800-trajectory failure taxonomy.
- [The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md) -- **compares-with**: the coding study's gap between prompted diagnosis and undirected self-review matches AutoResearchEval's uncorrected-self-awareness pattern, but the latter extends the phenomenon across full scientific workflows and measures failure after the flaw was already written down.
- [Improving AI Skills with autoresearch and evals-skills](../../../../sources/improving-ai-skills-with-autoresearch-evals-skills-203525743436.ingest.md) -- **compares-with**: both make an empirically derived failure taxonomy and human calibration prerequisites for useful automated judging; one is a three-iteration practitioner report, while the other scales the design to 800 artifact-rich trajectories with reported agreement statistics.
- [Auto-claude-code-research-in-sleep](../../../../agent-memory-systems/reviews/Auto-claude-code-research-in-sleep.md) -- **compares-with**: AutoResearchEval finds that same-run self-review is merely more text unless a finding changes delivery, while ARIS separates executor `done` from reviewer `accepted` and uses cross-model gates; this is a concrete orchestration contrast, not evidence that ARIS closes the measured deficit.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An Enigma of Artificial Reason](../../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.ingest.md) -- rejected as a direct source-to-source edge because its valid-answer/invalid-reasoning contrast is already reached more precisely through the reasoning-evaluation note; another comparison would duplicate that route without adding an autoresearch-specific axis.
- [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) -- rejected because its counterfactual-law discovery and prediction/explanation split share the scientific-discovery domain but do not diagnose full-lifecycle research trajectories or self-review-to-revision failure.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md) -- rejected because its trace APIs and pause/retry gates are enabling runtime primitives, not evidence about whether a review architecture reduces the paper's autoresearch failure patterns.
- [Swamp](../../../../agentic-systems/reviews/swamp.md) -- rejected because durable workflow state and reports improve observability but do not supply the artifact-aware semantic diagnosis or metacognitive repair mechanism at issue.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The target is an immutable snapshot and no matching `kb/sources/how-agents-fail-on-autoresearch.ingest.md` exists. All outbound candidates belong on that future authored ingest surface, never on the snapshot.
- Preserve the paper's attribution boundary: recurrence across eight harness-model combinations supports a shared failure pattern, but the study does not intervene on orchestration and therefore does not establish that the deficit is irreducibly model-level or that review gates cannot compensate.
- Pattern frequencies come from a human-calibrated agent judge with aggregate pattern- and pillar-level agreement on 50 trajectories; the paper does not report per-pattern agreement, so individual prevalence estimates should not be treated as equally calibrated.
