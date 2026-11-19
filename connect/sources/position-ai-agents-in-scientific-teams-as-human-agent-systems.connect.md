---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/position-ai-agents-in-scientific-teams-as-human-agent-systems.md"
source_has_frontmatter: true
date: "2026-08-20"
depth: standard
---

# Connection Report: Position: AI Agents in Scientific Teams Should Be Studied as Human-Agent Systems

**Source:** [Position: AI Agents in Scientific Teams Should Be Studied as Human-Agent Systems](../../../sources/position-ai-agents-in-scientific-teams-as-human-agent-systems.md)

## Discovery Trace

**Description listing scan:**

- Generated fresh complete title surfaces with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: 355 files under `kb/notes/`, 135 under `kb/reference/`, 173 under `kb/agent-memory-systems/`, 12 under `kb/agentic-systems/`, and 519 under `kb/sources/`.
- Ran `rg -n -i '^description:.*(human|scient|collabor|delegat|autonom|divers|team|pair)'` over every authorised local destination. The notes scan foregrounded whole-system learning, human-inclusive actor allocation, warranted autonomy, and adversarial human-agent review. The sources scan foregrounded function-allocation, delegation, automation-ironies, scientific-review, and autonomous-research cases. Reference, agent-memory, and agentic-system descriptions exposed no direct target beyond system-specific analogues.
- The strongest path-and-description candidates were [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md), [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), [Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md), and [A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md).

**Topic indexes:**

- Read [Tags](../../../../tags/README.md) and the curated heads for [Reference](../../../../reference/README.md), [Agent Memory Systems](../../../../agent-memory-systems/README.md), [Agentic Systems](../../../../agentic-systems/README.md), and [Sources](../../../../sources/README.md). The notes hub routed toward foundations, evaluation, and learning theory; the other heads confirmed that this is a methodology source rather than a review of a current Commonplace component or a memory subsystem.
- Reference was rejected as an outbound destination because the likely hit, [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md), describes one shipped human-inclusive system rather than supplying a general claim the scientific-teams source needs. Agent-memory and agentic-system destinations were also skipped after focused searches found only implementation-level topical overlap.

**Body search:**

- `rg -n -i 'human-agent systems?|human-agent pairs?|standalone capabil|scientific teamwork|reduced diversity|de[- ]?skilling' kb/notes/ kb/sources/ --glob '*.md'` -- kept the automation-ironies and human-allocation sources; it found no duplicate local note that already states the paper's human-agent evaluation-boundary claim.
- `rg -n -i 'unit of learning|human-inclusive|function allocation|reviewer identity|human judgment' kb/notes/ --glob '*.md'` -- kept whole-system learning and human-inclusive allocation; rejected reviewer-subrole and autonomy-frontier notes whose narrower mechanisms are not established by the captured page.
- `rg -n -i 'human[- ]agent|human.?AI|human.{0,40}agent|agent.{0,40}human|unit of analysis|human judgment|human effort|complementar|synerg' kb/notes/ --glob '*.md'` -- evaluated warranted autonomy, effort relocation, and the adversarial writing loop, but retained only claims the abstract materially bears on.
- `rg -n -i 'human[- ]agent|human.?AI|human.{0,50}agent|agent.{0,50}human|scientific (team|collabor)|topic diversity|inquiry diversity|de[- ]?skill|complementar|synerg' kb/sources/ --glob '*.md'` -- kept the CRUX, automation-allocation, delegation, and automation-ironies comparisons.
- `rg -n -i 'scientific|human-agent|human.?AI|research team|collabor' kb/agent-memory-systems/ kb/agentic-systems/ kb/reference/ --glob '*.md'` -- evaluated AutoSci, Semiont, CORAL, and Commonplace's reflective-system description; rejected them as subsystem or current-system descriptions without a direct claim about scientific human-agent team outcomes.

**Link following:**

- Followed whole-system learning to the fixed-decomposition note. This exposed the paper's proposed human-agent pair as an extension of the current model-plus-harness boundary while preventing the reported case studies from validating that pair decomposition generally.
- Followed human-inclusive allocation through its external function-allocation precedent and its boundary-contraction application. The source supports treating human and agent contributions as a joint causal profile, but the captured page does not provide a per-function allocation matrix or a no-human ablation.
- Followed the CRUX ingest through its expert-oracle and fixed-decomposition analysis. CRUX supplies a useful contrast between autonomous research execution and expert rejection; this source proposes studying collaborative configurations instead.
- Followed the automation-ironies and delegation ingests. Their de-skilling, accountability, and function-allocation mechanisms are relevant background, but the new source's distinctive contribution is the scientific-team evaluation boundary rather than another general delegation taxonomy.

## Connections Found

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) -- **is-evidence-for**: the source independently rejects model-only evaluation and extends the causal unit in scientific work to the human-agent pair, where collaboration structure and human judgment affect the observed outcome.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- **is-evidence-for**: the paper's human-agent-system lens treats scientist and agent contributions as a joint allocation rather than reading standalone agent capability as the team's capability.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: the reported case studies can show complementarity inside selected scientist-model-task arrangements, but cannot establish that the chosen pair boundary, interaction protocol, representations, or allocation of operations is generally optimal.
- [Ingest: Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) -- **compares-with**: CRUX measures autonomous research systems against original-author judgment and finds an engineering/judgment gap; this source argues that collaborative human-agent configurations should themselves become the unit studied.
- [Ingest: A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- **compares-with**: the older framework operationalizes human-machine systems as per-function allocation profiles, while this source transfers the system-level stance to scientific teams and calls for synergy measures.
- [Ingest: Ironies of Automation](../../../../sources/ironies-of-automation.ingest.md) -- **compares-with**: Bainbridge supplies a general mechanism for role transformation and de-skilling under automation; the new source identifies analogous near-term risks in scientific collaboration.
- [Ingest: Intelligent AI Delegation](../../../../sources/intelligent-ai-delegation-tomasev-franklin-osindero.ingest.md) -- **compares-with**: the delegation framework supplies authority, accountability, verification, and task-allocation axes for human-AI chains; this source supplies the scientific-team problem frame in which those axes need outcome evidence.

## Bidirectional Candidates

- [Ingest: Can AI agents conduct open-ended AI research?](../../../../sources/can-ai-agents-conduct-open-ended-ai-research.ingest.md) <-> source -- **compares-with**: the return path would juxtapose autonomous shadow evaluation with the later proposal to evaluate interactive human-agent research teams.
- [Ingest: A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) <-> source -- **compares-with**: the pair connects a general function-allocation vocabulary to a scientific-collaboration application.

## Reverse-edge Candidates

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md) → source -- **evidenced-by**: the source is an independent domain-specific argument that causally consequential humans belong inside the evaluation boundary rather than outside as deployment context.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) → source -- **evidenced-by**: the paper provides a scientific-team case for treating human, computational, and joint contributions as an allocation profile rather than a scalar autonomy score.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Review automation should target verifiable subroles before reviewer identity](../../../../notes/verifiable-subroles-before-reviewer-identity.md) -- rejected because the source argues for human-agent scientific teams broadly, while the captured page does not decompose reviewer work or establish subrole-specific verification.
- [Increasing computational autonomy relocates human effort to the frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- rejected because complementarity and continued human involvement do not measure whether total effort relocated or whether output per human judgment increased.
- [An adversarial human-agent loop can reconstruct the writing-is-thinking filter](../../../../notes/adversarial-loop-can-reconstruct-the-writing-is-thinking-filter.md) -- rejected because the source's collaborative case descriptions do not establish an adversarial review loop or retain the human specifically as final judge.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) -- rejected because its scientific wiki memory is an implementation-level subsystem; the source does not evaluate its interaction design or memory mechanisms.
- [Commonplace as a reflective self-improving system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) -- rejected because a `see-also` link between two human-inclusive systems would be broad topical adjacency without a specific shipped-system reader need.

## Index Membership

None

## Synthesis Opportunities

- [The deployed system, not the model alone, is the unit of learning](../../../../notes/the-deployed-system-not-the-model-is-the-unit-of-learning.md), [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md), and this source together imply a broader evaluation rule: when human decisions causally shape the output, the human participants and interaction protocol belong inside the evaluated system boundary. The current learning note enumerates model, harness, and runtime components but does not yet state this human-inclusive extension explicitly.

## Maintenance Observations

None

## Flags

- The snapshot captures the Hugging Face abstract page and community summaries, not the full paper. Candidate edges that depend on case-study design, equations, or empirical details must remain provisional until the PDF is captured or code-grounded.
- The source is experiment-bearing, but its fixed-decomposition audit is necessarily coarse from the page capture: model access, scientist histories, task selection, interaction protocol, allowed operations, and evaluation measures are not exposed in enough detail to attribute the reported complementarity or validate the human-agent pair decomposition generally.
