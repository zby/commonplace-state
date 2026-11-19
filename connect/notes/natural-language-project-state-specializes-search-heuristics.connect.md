---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/natural-language-project-state-specializes-search-heuristics.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Natural-language project state may specialize weight-resident search heuristics

**Source:** [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md)

## Discovery Trace

**Collection contract and scope:**

- Read the source contract at `kb/notes/COLLECTION.md` and the report contract at `kb/reports/types/connect-report.md`. The authorised local destinations are `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`; `kb/work/` is explicitly excluded.
- The source already authors links to the code-complement, lightweight-search-control, weight-resident-methodology, and methodology-selection notes. `rg -n 'natural-language-project-state-specializes-search-heuristics|Natural-language project state may specialize' kb/ --glob '*.md'` also found an authored inbound link from the code-complement note and workshop mentions. Those existing edges were not proposed again, and the workshop hits were excluded.

**Description listing scan:**

- Fresh complete title scans were run with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/types/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`, `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`, and `rg -N --no-heading -m1 '^# ' kb/instructions/ --glob '*.md'`.
- Complete description scans were run with `rg '^description:' kb/notes/ --glob '*.md'`, `rg '^description:' kb/types/ --glob '*.md'`, `rg '^description:' kb/reference/ --glob '*.md'`, `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`, `rg '^description:' kb/agentic-systems/ --glob '*.md'`, `rg '^description:' kb/sources/ --glob '*.md'`, and `rg '^description:' kb/instructions/ --glob '*.md'`.
- The note listings exposed four distinct candidate groups: project-state components, context-to-action mechanisms, controlled-intervention methodology, and observed or implemented cases. The other collections produced Reflexion, Compound Engineering, the faithful-self-evolvers ingest, the Commonplace change-candidate description, and the connect procedure as candidates requiring body-level qualification. The type listing produced no type whose claim would improve traversal from this source.

**Topic indexes:**

- Read the main `README.md` in every authorised destination collection and the source's three matching tag heads: [Foundations](../../../../tags/foundations-README.md), [Context engineering](../../../../tags/context-engineering-README.md), and [Self-improving systems](../../../../tags/self-improving-systems-README.md). None declares `complete: true`, so no tag sweep was skipped.
- Ran `rg -l '^tags:.*foundations' kb/notes/ kb/types/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'`, `rg -l '^tags:.*context-engineering' kb/notes/ kb/types/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'`, and `rg -l '^tags:.*self-improving-systems' kb/notes/ kb/types/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'`.
- The context-engineering head lacks an entry connecting selected prompt state to weight-resident search competence. The self-improving-systems head already names theory-mediated learning as an open payoff hypothesis but lacks this proposed local mechanism. The selective foundations head already routes this area through self-improving systems, so a third membership there would add less than the two narrower placements.

**Body search:**

- Notes: `rg -l -i 'working theory|prior branches|failure explanation|current intent|commitments and constraints' kb/notes/ --glob '*.md'`, `rg -l -i 'branch choice|candidate generation|search heuristics|backtrack|selecting probes' kb/notes/ --glob '*.md'`, `rg -l -i 'withholding|replacing|perturbing|ablation|holding .* fixed' kb/notes/ --glob '*.md'`, and `rg -l -i 'contextual activation|weight-resident|model weights|prompt context|consumption path' kb/notes/ --glob '*.md'`. These retained the component, activation, hybrid-computation, intervention, and bounded-evidence notes listed below; broad context and prompt-variation hits were rejected when they did not isolate project-state effects.
- Types: `rg -l -i 'prompt|context|search|retained' kb/types/ --glob '*.md'` returned only generic structural contracts. None makes a target-side claim about semantic state specializing search.
- Reference: `rg -l -i 'change candidates|agent initiative|collection contract|project state' kb/reference/ --glob '*.md'` made the Commonplace change-candidate description the strongest case, but its inventory does not test whether supplied state changes choices.
- Agent-memory systems: `rg -l -i 'reflection|failed trajectories|task-local|same-instance|project state|working theory' kb/agent-memory-systems/ --glob '*.md'` retained Reflexion because it injects failure-derived verbal plans into same-instance retries and includes aggregate memory switches. Claude Workstream Kit was rejected because its active-state injection has no faithfulness test.
- Agentic systems: `rg -l -i 'project knowledge|CONCEPTS|plans|solutions|retained|later work' kb/agentic-systems/ --glob '*.md'` made Compound Engineering the closest case. It was rejected as evidence because the review inspected rather than operated the plugin and reports no comparison establishing behavioral dependence on retained project text.
- Sources: `rg -l -i 'Empty|Shuffle|Irrelevant|causal intervention|behavioral faithfulness|natural-language project state' kb/sources/ --glob '*.md'` retained the faithful-self-evolvers ingest for its controlled content perturbations and negative result for condensed experience. Nearby sources on generic semantic-content effects, context programming, fragile experience construction, workflows, and skills did not isolate theory-organized project state.
- Instructions: `rg -l -i 'candidate|articulation test|stopping|collection contract' kb/instructions/ --glob '*.md'` surfaced `cp-skill-connect`. Its procedure is a close operational analogy, but `operationalized-from` would assert authoring lineage that is not established, while `see-also` would be too weak to justify an exceptional instruction link.
- These `rg` surfaces are unranked; no retrieval scores were available.

**Link following:**

- Followed the program-theory neighborhood into theory mediation, decision-point citation, failure interpretation, and backtracking. This retained the program-theory and theory-mediation claims while rejecting citation alone as weaker than the source's intervention criterion.
- Followed the intent and failure-explanation neighborhoods into lightweight search control. Intent and failure explanation survived as distinct state components; lightweight search control was already linked by the source.
- Followed the activation and action-model neighborhoods into prompt consumption, retained-versus-weight activation, and retrieval misses. The shared-token-medium, hybrid-route, activation, and consumption-path claims survived; retrieval misses were rejected because the proposed test holds successful exposure fixed.
- Followed the Commonplace evidence note into its mediation and decision-point links, Reflexion into its activation and trace-learning links, Compound Engineering into its proposal-selection and compounding links, and the faithful-self-evolvers ingest into its experiment-contrast and activation links. This separated a bounded observational case and two behavior-bearing sources from implementation-only cases.
- External prospecting was skipped: no external target was supplied or already present as a candidate, and the skill forbids open-web prospecting.

## Connections Found

- [Program theory sustains search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) -- **extends**: develops the working-theory component into a program-specific controller for candidate generation, failure interpretation, backtracking, and revision while feedback is delayed.
- [Failure explanation changes later branch decisions](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **extends**: isolates one part of retained project state and gives it the same behavioral test: a failure explanation is operative only when it changes a later branch choice.
- [Intent controls choices by distinguishing live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) -- **extends**: isolates current intent and specifies how it changes admissibility, priority, further search, and stopping among live alternatives.
- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **grounds**: supplies the storage-to-read-back-to-activation distinction behind the source's requirement that retained language reach the prompt and measurably change behavior.
- [An action model matters only through its consumption path](../../../../notes/an-action-model-matters-only-through-its-consumption-path.md) -- **exemplifies**: the source is a natural-language action-model case in which retained state matters only by participating in branch and intervention selection.
- [LLM contexts interpret instructions and content through the same token medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) -- **mechanism**: explains how natural-language state can enter the model's computation without translation while leaving role, scope, and authority to the surrounding architecture.
- [Borrowing can operate through retained artifacts or weight activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) -- **exemplifies**: the source instantiates the hybrid route of a weight-resident baseline plus retained project-specific state and current constraints.
- [Theory-mediated self-improvement needs interpretation and retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- **extends**: places search specialization inside the broader causal path that also requires semantic interpretation, addressable retention, independent outcome read-back, and continuation.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **grounds**: explains why the proposed withholding, replacement, or perturbation test must hold the model, symbolic state, tools, and task fixed before attributing a search change to natural-language project state.
- [Prompt ablation converts human insight to deployable framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) -- **contrasts**: varies elicitation framing against a fixed human-verified finding, whereas this source proposes varying semantic project state and observing branch behavior.
- [Commonplace revision used theory-guided computational search](../../../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) -- **evidenced-by**: supplies a bounded observed episode in which retained intent, theory, branch history, and constraints guided model-mediated search, while explicitly lacking the matched control needed to establish the conjecture.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) -- **evidenced-by**: provides an implemented same-instance path from failed trajectories and test feedback through task-local verbal repair advice into later prompts, with aggregate memory switches but no per-reflection causal attribution.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -- **evidenced-by**: supplies the closest controlled perturbation pattern and an important boundary result: behavior depends strongly on raw trajectories but often weakly on condensed experience, so retained natural language is not operative merely because it is present or plausible.

## Bidirectional Candidates

- [Program theory sustains search under delayed feedback](../../../../notes/program-theory-sustains-search-under-delayed-feedback.md) <-> source -- **mechanism**: the source proposes how retained program theory can specialize general LLM search competence for the current program.
- [Failure explanation changes later branch decisions](../../../../notes/failure-explanation-changes-later-branch-decisions.md) <-> source -- **exemplifies**: a retained explanation changing the next branch is one concrete instance of natural-language project state specializing search.
- [Intent controls choices by distinguishing live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) <-> source -- **exemplifies**: intent changing which alternatives remain live is one concrete instance of the broader specialization conjecture.
- [Borrowing can operate through retained artifacts or weight activation](../../../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md) <-> source -- **extends**: the source develops the hybrid retained-artifact plus weight-activation route specifically for project search.
- [Theory-mediated self-improvement needs interpretation and retention](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) <-> source -- **mechanism**: the source supplies a candidate local mechanism by which interpreted and retained theory changes later search choices.
- [Prompt ablation converts human insight to deployable framing](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md) <-> source -- **contrasts**: the return path helps an experiment designer keep framing ablations distinct from interventions on semantic project state.
- [Commonplace revision used theory-guided computational search](../../../../notes/evidence/commonplace-revision-used-theory-guided-computational-search.md) <-> source -- **exemplifies**: the bounded Commonplace episode is an observational instance of the conjectured project-state specialization path, not a controlled demonstration.

## Reverse-edge Candidates

- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) -> source -- **is-evidence-for**: its code-grounded review and aggregate with/without-memory switches materially bear on whether failure-derived natural-language state changes later attempts, while preserving the per-reflection attribution limit.
- [Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../../../sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md) -> source -- **is-evidence-for**: its controlled Empty, Shuffle, Irrelevant, Corrupt, and Filler interventions bear directly on the source's behavioral-dependence criterion and qualify which retained forms actually influence behavior.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Active work state is not retrospective memory or chat history](../../../../notes/active-work-state-is-not-retrospective-memory-or-chat-history.md) -- defines a useful current-state carrier, but it does not claim that the state's natural-language contents change search; the component notes above provide the sharper causal links.
- [Citing retained theory at the decision point is a mediation trace](../../../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) -- citation can show consumption but not load-bearing influence, and the theory-mediation connection already carries the stronger intervention requirement.
- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) -- concerns failure before exposure, while the source's proposed causal test holds context assembly and exposure fixed so it can test context-to-action influence.
- [Systematic prompt variation serves verification and diagnosis](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) -- catalogs prompt-variation purposes more broadly; the prompt-ablation and experiment-contrast notes distinguish the relevant treatment more precisely.
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../../../../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) -- proposes intent as an economical inference seed but does not test branch behavior; the intent-controls note is the more direct component connection.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- describes contract- and context-shaped candidate generation in the installed system, but records neither a held-fixed intervention nor a behavioral comparison.
- [Claude Workstream Kit](../../../../agent-memory-systems/reviews/claude-workstream-kit.md) -- pushes natural-language active-work state at session start, but its review records no faithfulness test showing that this state changes later search.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- deliberately retrieves plans, solutions, and project concepts into later work, but the review did not operate the plugin and reports no comparison showing changed behavior from that text.
- [Language models show content effects on reasoning](../../../../sources/language-models-like-humans-show-content-effects-on-reasoning.ingest.md) -- demonstrates semantic-content effects in deductive reasoning, not project-state specialization of open-ended search.
- [Context as an Environment](../../../../sources/context-as-an-environment.ingest.md) -- supports exact context construction and ablation but centers a programmatic or symbolic context representation rather than the distinctive natural-language theory contribution.
- [On the Fragility of Self-Improving Agents](../../../../sources/on-the-fragility-of-self-improving-agents.ingest.md) -- changes experience construction and instruction bundles, so its result does not isolate supplied natural-language state while holding the other proposed factors fixed.
- [Agent Workflow Memory](../../../../sources/agent-workflow-memory.ingest.md) -- reports gains from reusable workflows distilled from successful trajectories, but those procedure-like workflows are not current, theory-organized project state.
- [Reason Wide, Not Deep](../../../../sources/reason-wide-not-deep-distilled-skills.ingest.md) -- tests reusable natural-language skills, not project-specific intent, theory, branch history, or constraints.
- [Connect skill](../../../../instructions/cp-skill-connect/SKILL.md) -- uses loaded artifact and collection state to guide candidate search, but no evidence establishes that its procedure was authored from this new note; `operationalized-from` would invent lineage and `see-also` would not justify an exceptional instruction link.

## Index Membership

- [Context engineering](../../../../tags/context-engineering-README.md) -- candidate Core Claim connecting context selection and activation to a testable account of how current project state specializes weight-resident competence.
- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- candidate entry under “What reflection adds,” beside the open theory-mediated payoff hypothesis, because it proposes the local search mechanism and the intervention needed to test it.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- No candidate establishes the full held-fixed claim that theory-organized natural-language project state changes open-ended branch selection. The Commonplace episode is observational, Reflexion's comparison is aggregate, and the controlled self-evolver study tests experience forms rather than this complete state bundle; the source should retain conjectural modality.
- The strongest controlled source creates a useful boundary tension: raw trajectories alter behavior far more reliably than condensed experience. Any future test must distinguish theory-level organization from mere compression and must measure causal uptake, not prompt presence.
- Although the candidate set spans components, mechanisms, evaluation, and cases, they all serve one causal conjecture plus its test. No split is recommended.
