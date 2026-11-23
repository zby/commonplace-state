# Inbound contexts of `kb/theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md`

48 file(s) link to this note. Searched: Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself.

Only the first 30 files by path are shown; 18 more were cut.

## `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md`

- Title: Trace-learning techniques in related systems
- Description: Trace-learning systems compared on ingestion pattern, representational form, behavioral authority, artifact structure, and evidence tier across repo reviews and lightweight coverage

> - [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) — sharpens: the survey's artifact-promotion systems count as behaviour-change learning via readable system-definition artifacts; the distributed-parametric cases take the slower, harder-to-validate form

## `kb/agentic-systems/reviews/ai-agent-book.md`

- Title: AI Agents in Depth
- Description: Whole-book comparison of AI Agents in Depth with Commonplace, separating broad architectural convergence from differences in memory admission, epistemic warrant, governance, and orchestration

> Chapter 9 opens by rejecting the idea that stored experience is already learning. Its strong route is immutable evidence → diagnosis → local candidate → independent checks → release decision → activation/adherence measurement → consolidation and rollback ([continual-evolution loop](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter9.md#L3-L90), [release and activation](https://github.com/bojieli/ai-agent-book/blob/a18a5f764589396d903d8faeaed205489a21bf4b/book-en/chapter9.md#L271-L317)). This agrees with [proposal-selection requires search, evaluation, and operative retention](../../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) and with [governing behavior-changing writes](../../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md).

## `kb/sources/adaptation-of-agentic-ai-survey-post-training-memory-skills.ingest.md`

- Title: Ingest: Adaptation of Agentic AI
- Description: Survey mapping agentic adaptation across A1/A2 agent training, T1/T2 tool adaptation, memory, skills, and dynamics-aware evaluation

> The wider cluster the report found is intact. The source **compares with** [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md), [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md), and [Treat continual learning as substrate coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md): the paper gives a mainstream ML taxonomy for agent/tool optimization, while the KB gives an artifact-substrate and role taxonomy that better captures readable repo artifacts. It **evidences** [Memory management policy is learnable but oracle-dependent](../theory/memory-management-policy-is-learnable-but-oracle-dependent.md) and [Agent memory is a crosscutting concern, not a separable niche](../theory/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) by classifying memory according to update mechanism rather than treating it as one pluggable subsystem. It **compares with** [Skills derive from methodology through distillation](../theory/skills-derive-fro [cut at 1200 characters]

## `kb/sources/agentic-reasoning-for-llms-survey.ingest.md`

- Title: Ingest: Agentic Reasoning for Large Language Models
- Description: Agentic-reasoning survey: foundational, self-evolving and multi-agent layers × in-context vs post-training; its update rule S_k+1 ← U(S_k, τ_k, F_k) and memory taxonomy tested against our learning and governance notes

> On governance, the survey **compares with** [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and [The adaptation survey corroborates memory requirements but misses artifact governance](../theory/agent-memory-requirements/adaptation-survey-corroborates-memory-requirements.md). Its general update rule folds selection into feedback `F_k` and has no step for validating, authorizing or retiring a write to `S_k`, and section 8.6 places governance at model, agent and ecosystem level. The omission is not total, however. Section 5.3.2 reports write admission through reproducible replay (SEDM) and immutable per-entry provenance with private and shared access policies (Collaborative Memory) in multi-agent memory systems. So the governance gap is in the survey's general framework, not in the literature it catalogues.

> - [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) — compares-with: on what conditions a retained update; the general update rule has no governance step

## `kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md`

- Title: Ingest: Chunking in Soar: The Anatomy of a General Learning Mechanism
- Description: Soar compiles referenced subgoal experience into persistent production rules that later control search or implement operators, while its architecture remains fixed.

> Its limiting role is equally important. The paper makes representation and the accessed problem-solving knowledge the bias on learned-rule generality, so its transfer results illustrate [learning inside a fixed decomposition](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) rather than testing the architecture and task representation held outside chunking. It supplies a concrete case for [governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): direct operator-implementation chunks could make the system behave as though an external action had occurred, so the demonstration disabled that learning path and retained only search-control chunks. Compared with [explanation-based generalization](./explanation-based-generalization-unifying-view.ingest.md), user direction helped Soar encounter successful experience, but its chunks were operational productions derived from referenced state and subgoal results, not revisions to a supplied explanatory theory.

## `kb/sources/continual-learning-in-token-space.ingest.md`

- Title: Ingest: Continual Learning in Token Space
- Description: Letta reframes continual learning as optimizing learned context rather than weights, but the KB's stronger frame is weight space versus repo artifacts, including codified procedures

> It most strongly **extends** [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): the source makes the same anti-weight-monopoly move, but with a narrower substrate proposal, learned context. In repo terms, it covers one branch of the non-weight side but not the whole space. It also **extends** [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md) by presenting token-space memory as an inspectable adaptation layer that sits alongside opaque weight updates, while adding a bridge back toward training through tokens-to-weights distillation.

> Write a note titled "Token-space learning is a subset of repo-artifact learning" connecting to [continual-learning-open-problem-is-behaviour-not-knowledge.md](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md), [codification.md](../theory/definitions/codification.md), and [letta-memgpt-stateful-agents.ingest.md](./letta-memgpt-stateful-agents.ingest.md). It would argue that Letta's framing is not a competing theory of learning so much as a narrower, agent-memory-centric subset of the KB's broader repo-artifact model, while isolating memory-policy learning as the unresolved hard part and codification as the missing category in Letta's account.

## `kb/sources/dfa-moe-dual-forgetting-vision-language-continual-learning.ingest.md`

- Title: Ingest: DFA-MoE: Tackling Dual Forgetting in Vision-Language Continual Learning
- Description: DFA-MoE separates forgetting acquired classes from eroding a model's pre-trained zero-shot baseline, but the captured repository exposes design and workflow rather than paper outcomes

> The closest source comparison is [HCL](harness-continual-learning-adaptation-beyond-model-parameters.ingest.md): HCL protects sampled behavior acquired earlier in a harness-update history, while DFA-MoE separately names forgetting of incremental history and forgetting of capabilities inherited from pre-training. That distinction sharpens [continual learning as governance of behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md), whose current regression requirement does not separate those baselines. [Harness-IF](harness-if-instruction-following-across-instruction-surfaces.ingest.md) supplies a measurement analogue rather than the same mechanism: its withheld-rule control and DFA-MoE's claimed similarity calibration both try to keep pre-existing capability or transfer from inflating the quantity attributed to an intervention. Interpretation rests on [the fixed-decomposition boundary](../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md), because the repository exposes learning inside a supplied two-pathway architecture and evaluation protocol, not evidence that those fixed choices are necessary or preferable.

## `kb/sources/dual-nature-generalization-on-policy-distillation.ingest.md`

- Title: Ingest: The Dual Nature of Generalization in On-Policy Distillation
- Description: On-policy distillation transfers capabilities and regressions beyond routed prompt domains, supporting broader validation of shared-weight updates while leaving the alignment mechanism unresolved.

> The paper supplies a concrete parametric example for [governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): in the tested shared-weight OPD setup, validating only the routed prompt domain would miss consequential regressions elsewhere. This supports that note's regression-validation requirement, while post-training experiments do not test its deployment-time governance loop. The reversal of teacher assignments is useful because a teacher still transfers capabilities outside its nominal teaching role.

> Update [Continual learning requires governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) with this bounded post-training example showing why regression validation must extend beyond an update's nominal domain.

## `kb/sources/externalization-in-llm-agents-unified-review.ingest.md`

- Title: Ingest: Externalization in LLM Agents
- Description: Survey paper unifying LLM agent memory, skills, protocols, and harness engineering as externalized cognitive infrastructure rather than model-weight capability alone

> On memory, the source extends [agent-memory-is-a-crosscutting-concern-not-a-separable-niche](../theory/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md), [agentic-memory-systems-comparative-review](../agent-memory-systems/agentic-memory-systems-comparative-review.md), and [trace-learning-techniques-in-related-systems](../agent-memory-systems/trace-learning-techniques-in-related-systems.md) by describing memory as state infrastructure feeding skill distillation, protocol routing, and governance. On skills, it grounds [skills-derive-from-methodology-through-distillation](../theory/skills-derive-from-methodology.md) and extends [skills-are-instructions-plus-routing-and-execution-policy](../theory/skills-are-instructions-plus-routing-and-execution-policy.md) with a lifecycle model: specification, discovery, progressive disclosure, execution binding, composition, and feedback. On capability placement, it grounds [axes-of-artifact-analysis](../theory/axes-of-artifact-analysis.md), [deploy-time-learning-is-the-missing-middle](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md), [continual-learning-open-problem-is-behaviour-not-knowledge](../theor [cut at 1200 characters]

## `kb/sources/from-harness-lock-in-to-portable-context-layer.ingest.md`

- Title: Ingest: From Harness Lock-In to Portable Context Layer
- Description: Practitioner portability framing separates owned memory from disposable harnesses, but leaves access logic and skill execution as distinct lock-in boundaries

> As a counterpoint, the article calls periodic conversation ingestion “continual learning,” while [continual learning requires governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and [memory should be evaluated by effects](../theory/agent-memory-requirements/evaluate-memory-by-effects.md), not by persistence. Its build-versus-buy taxonomy also foregrounds storage and implementation effort, whereas the [148-system comparison](../agent-memory-systems/agentic-memory-systems-comparative-review.md) finds activation and verification more discriminating than substrate alone. Its direct conceptual predecessor is [Karpathy's LLM Wiki ingest](./karpathy-llm-wiki.ingest.md); this source adds harness lock-in, an MCP serving boundary, and the open portability problem for skills.

## `kb/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.ingest.md`

- Title: Ingest: From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs
- Description: Ingest of the 3D-8Q LLM-memory survey: how object/form/time taxonomy fits our memory-axes and cognitive-analogy-skepticism notes

> The companion [connect report](../reports/cache/connect/sources/from-human-memory-to-ai-memory-survey-llm-memory-mechanisms.connect.md) found no existing note that cites this snapshot and frames the load-bearing signal as reverse-edge `evidenced-by` candidates. The strongest fit is the cognitive-analogy-skepticism cluster: [three-space-agent-memory-echoes-tulvings-taxonomy](../theory/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) (the note currently cites only a single tweet for the human-taxonomy-to-agent move; this is a paper-grade second instance, and the survey's own admission that its quadrants reduce to object/form/time policy dimensions supports the note's "the analogy may be decorative" hedge) and [psychology-to-agent-transfer-needs-per-principle-failure-mode-testing](../theory/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) (the survey is a large worked example of the wholesale-mapping move that note warns against). The second cluster is artifact/operational axes: the survey's *form* dimension (parametric/non-parametric) is an independent external parallel to our [representational-form](../theory/definitions/representational [cut at 1200 characters]

> 4. **Per-quadrant system catalogue for the two continual-learning mechanisms.** -- Quadrant-VI (non-parametric reflection: Reflexion, Voyager, ExpeL, Buffer of Thoughts, Agent Workflow Memory) and quadrant-VIII (parametric editing: WISE, MemoryLLM) give [continual-learning-open-problem-is-behaviour-not-knowledge](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) a ready list of instances of its readable-artifact vs distributed-parametric behaviour-change split. [just-a-reference]

## `kb/sources/harness-continual-learning-adaptation-beyond-model-parameters.ingest.md`

- Title: Ingest: Harness Continual Learning: Continual Adaptation Beyond Model Parameters
- Description: HCL turns harness edits into retention-gated continual learning, but finite anchors bound its no-forgetting claim and fixed partitions limit its ablations

> This paper is a direct empirical anchor for [governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and treating [the deployed system, not the model alone, as the learning unit](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md): model weights remain frozen while committed prompt, memory, skill, and routing changes produce both gains and forgetting. Its optimizer–evaluator–commitment path is a worked [proposal-selection improvement loop](../theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md). Relative to [Self-Harness](self-harness-harnesses-that-improve-themselves.ingest.md), HCL adds an explicit sequential history, sampled anchors, and a tunable loss budget; relative to the near-inversely named [Continual Harness](continual-harness-online-adaptation-foundation-agents.ingest.md), it replaces direct online edit adoption and optional weight training with isolated fixed-weight candidates. The finite-anchor result qualifies the whole architecture through [oracle domain](../theory/warranted-autonomy-is-bounded-by-oracle-domain.md), while its experimental interpretation rests on the [ [cut at 1200 characters]

## `kb/sources/hot-take-llm-can-jump.ingest.md`

- Title: Ingest: Hot Take: LLM can 'jump'
- Description: Direct reply to “LLMs can’t jump” arguing that later interconnected knowledge can make a formerly abductive discovery deductively reconstructible, then extending the claim to safety and continual learning

> The essay's scientific agent is explicitly a model plus code execution, Lean, simulators, and possible laboratory feedback, supporting [the deployed system, not the model alone, is the unit of learning](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md). Its continual-learning terminology is less compatible with the KB: it counts task-time use of supplied information even if nothing persists. [Continual learning requires governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) reserves the term for durable, evidence-responsive change, while [Machine Studying](machine-studying.ingest.md) supplies a more discriminating boundary for corpus-only preparation before downstream tasks.

## `kb/sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md`

- Title: Ingest: Huxley-Gödel Machine
- Description: ICLR 2026 HGM paper arguing immediate benchmark score is a weak parent-selection signal for self-improving coding agents; clade-metaproductivity better predicts productive lineages

> `/connect` placed HGM in the KB's hard-oracle self-improving-harness cluster. HGM has `is-evidence-for` edges to [the readable-artifact loop](../theory/readable-artifact-loop-is-the-tractable-unit-for-continual-learning.md), [deploy-time learning](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md), and [continual learning as behavior change](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md), because it improves durable agent scaffolds and control logic without weight updates. It also grounds [the boundary of automation is the boundary of verification](../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) and [oracle strength spectrum](../theory/oracle-strength-spectrum.md): HGM works in benchmark-rich coding domains, but shows that oracle availability alone is not enough when the immediate score is not aligned with the long-run search target. Reverse-edge candidates include [HyperAgents](../agent-memory-systems/reviews/hyperagents.md), [auto-harness](../agent-memory-systems/reviews/auto-harness.md), [CORAL](../agent-memory-systems/reviews/CORAL.md), and [trace-learning techniques](../agent-memory-systems/trace [cut at 1200 characters]

## `kb/sources/hyra-2-next-step-for-auto-research.ingest.md`

- Title: Ingest: Hyra 2.0: The Next Step for Auto Research
- Description: Tencent's Hyra 2.0 post argues auto-research should build reusable tools, not resample answers; graded Books memory and evidence-bearing review, compounding claimed but unmeasured

> Its memory design is the most transferable part. Books' Observation / Verified / Convention grades are a deployed staged-authority scheme, evidence for [trace-extracted memory earns authority per operation, not at capture](../theory/trace-extracted-memory-earns-authority-per-operation-not-at-capture.md), and its human approval for shared-knowledge synchronisation and conventions is evidence for [continual learning requires governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md). Its three separate stores are evidence for [active work state is not retrospective memory or chat history](../theory/active-work-state-is-not-retrospective-memory-or-chat-history.md), and its queue, required responses and evidence-bearing completion reports are evidence for [agent orchestration needs coordination guarantees, not just coordination channels](../theory/agent-orchestration-needs-coordination-guarantees-not-just.md). All four supports are design descriptions, not outcome measurements. Among sources, [Agora](./agora-git-as-shared-memory-for-collective-autoresearch.ingest.md) grades shared research memory by downstream reproduction over an im [cut at 1200 characters]

> - [Continual learning requires governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) — is-evidence-for: human approval for shared knowledge and conventions

## `kb/sources/intern-s2-mobius-arxiv-v1.ingest.md`

- Title: Ingest: Intern-S2-Mobius: Foundation Model with Decoupled Knowledge and Reasoning
- Description: Mobius implements shared routed FFN experts across reasoner layers, while its architecture, latent-reasoning, throughput, and self-evolution claims remain only partially isolated

> The paper's self-evolution forecast is a counterpoint to [The deployed system, not the model alone, is the unit of learning](../theory/the-deployed-system-not-the-model-is-the-unit-of-learning.md) and [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): expandable parametric storage does not govern which behavior-changing write to accept, validate, coordinate, or revert across a deployed system. [KBLaM](../agent-memory-systems/reviews/KBLaM.md) supplies the closest model-integrated memory comparison, while [Externalization in LLM Agents](externalization-in-llm-agents-unified-review.ingest.md) and [Reason Wide, Not Deep](reason-wide-not-deep-distilled-skills.ingest.md) place knowledge and displaced reasoning work in localized artifacts instead of shared weights.

## `kb/sources/into-the-unknown-self-learning-large-language-models.ingest.md`

- Title: Ingest: Into the Unknown: Self-Learning Large Language Models
- Description: Hallucination-driven self-learning LLM paper proposing Points in the Unknown, a self-question/search/train loop, and metrics for selecting models that can discover factual knowledge gaps

> The connect report places this source in the KB's continual-learning, substrate, and oracle-construction cluster. It **contrasts** with [Treat continual learning as substrate coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md) because it is a clean opaque-substrate loop: identify unknowns, search for facts, train weights. It **qualifies** [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) because the paper's successful training would be durable capacity change, but the KB's criterion is durability rather than weights. It **extends** [Automating KB learning is an open problem](../theory/automating-kb-learning-is-an-open-problem.md) by offering a concrete "what to learn" operator, while also showing why factual hallucination scoring does not directly solve judgment-heavy KB mutations. The closest oracle comparison is [Memory management policy is learnable but oracle-dependent](../theory/memory-management-policy-is-learnable-but-oracle-dependent.md): AgeMem uses task completion as the oracle; this paper uses hallucination/self-checkin [cut at 1200 characters]

## `kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md`

- Title: Ingest: Knowledge-Centric Self-Improvement
- Description: Controlled knowledge-centric self-improvement protocol in which stateless agents curate a shared knowledge base through task forums, cross-task forums, and scoped distillation

> This is the strongest empirical source currently connected to [Automating KB learning is an open problem](../theory/automating-kb-learning-is-an-open-problem.md): it demonstrates a bounded, benchmarkable slice of extraction, discussion, distillation, and reuse while leaving open-ended KB judgment unsolved. Its forum and distillation gates give [Choosing what to learn requires both validity and learning-value gates](../theory/choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) a concrete implementation, and its scoped transfer claims instantiate [Abstract an experience into a lesson only when you can state where the lesson stops](../theory/abstract-an-experience-only-when-you-can-state-the-boundary.md). The external artifact changes later solve behaviour, supporting [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md). It also complements the taxonomy in [The What & When of Self-Evolving Agents](the [cut at 1200 characters]

## `kb/sources/language-models-need-sleep-self-modify-consolidate-memories.ingest.md`

- Title: Ingest: Language Models Need Sleep
- Description: Sleep operationalizes offline consolidation as upward self-distillation into slower model weights plus RL-guided dreaming, separating scheduling posture from representational form

> The paper **is-evidence-for** [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): it implements continual learning as durable behavioral change and makes the distributed-parametric branch's characteristic tradeoffs visible -- interference, regression risk, training cost, and opaque read-back. Its memory terminology is **defined-in** [Representational form](../theory/definitions/representational-form.md): despite the short-term/long-term labels, the durable artifact is model weights or adapters rather than an external retrievable record.

## `kb/sources/llm-agents-are-not-always-faithful-self-evolvers.ingest.md`

- Title: Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers
- Description: Causal-intervention paper (v3, 13 backbones) showing self-evolving agents faithfully use raw trajectories but largely ignore condensed experience, making behavioral faithfulness the missing evaluation criterion for distilled memory

> At ingestion on 2026-06-15, the companion connect report found a **reverse-edge-only** result under the then-current contract, which directed evidence links to snapshots. The following records that discovery; new durable citations must point to this tracked ingest. Two notes already cite the paper by bare arXiv URL and should upgrade to labelled local `evidenced-by` edges: [evaluate-memory-by-effects](../theory/agent-memory-requirements/evaluate-memory-by-effects.md) (direct support for "evaluate by effects, not existence" plus the WITH/WITHOUT method) and [activate-behavior-changing-memory](../theory/agent-memory-requirements/activate-behavior-changing-memory.md) (its Behavioral Faithfulness section already names this paper). Three new `evidenced-by` candidates are [knowledge-storage-does-not-imply-contextual-activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md) (the §5.2 IG result is a clean instance of "context-to-action failure" — knowledge visible in context but not integrated — and is the strongest new fit), [continual-learning-open-problem-is-behaviour-not-knowledge](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) (accumu [cut at 1200 characters]

## `kb/sources/llm-knowledge-bases-something-i-m-finding-very-useful.ingest.md`

- Title: Ingest: LLM Knowledge Bases
- Description: Karpathy on agent-maintained research wikis in Obsidian — index files and brief summaries replacing fancy RAG at roughly 100-article scale

> `/connect` placed this source in the file-first / durable-artifact / navigation cluster. It strongly exemplifies [vibe-noting](../theory/vibe-noting.md) and [continual-learning-open-problem-is-behaviour-not-knowledge](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): knowledge work compounds because the agent operates on inspectable artifacts and files outputs back into the KB. It also strengthens [files defer schema commitment until invariants stabilize](../theory/files-defer-centralized-schema-commitment-until-invariants-stabilize.md) and [agents-navigate-by-deciding-what-to-read-next](../theory/agents-navigate-by-deciding-what-to-read-next.md) by showing a concrete retrieval layer built from maintained summaries, backlinks, and index files rather than a separate vector stack. The most interesting extension is to [knowledge-storage-does-not-imply-contextual-activation](../theory/knowledge-storage-does-not-imply-contextual-activation.md): the source's real mechanism is not "the model can read a lot," but "the wiki contains symbolic activation scaffolds that tell the model what to load next." On the tool/interface side, [Napkin](../agent-memory-systems/rev [cut at 1200 characters]

## `kb/sources/long-horizon-agents-levels-ticks-cascaded-intelligence.ingest.md`

- Title: Ingest: An Architecture for Long-Horizon Agents: Levels, Ticks and Cascaded Intelligence
- Description: A ten-day agent campaign illustrates bounded live state, clocked execution and review-based escalation; its retained operating changes offer limited evidence of adaptation without weight updates.

> The source also compares with [governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md). Its strongest example is a recurring worker failure first addressed by instructions in every brief and then by an executable guard. That is a concrete change in how a retained rule determines behavior, rather than mere storage. The campaign does not establish systematic regression checking for such changes or compare alternative ways to install them.

## `kb/sources/merchantbench-long-term-coherence.ingest.md`

- Title: Ingest: MerchantBench: Long-Term Coherence in E-Commerce Operations
- Description: MerchantBench measures persistent operation with delayed feedback; its skill traces separate retained procedure use from demonstrated learning, without isolating memory effects.

> It also illustrates the concern behind [governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md). In one Claude Opus 4.8 Hermes run, the agent inferred that removing weak listings would concentrate traffic, and its shelf contracted from 47 listings on Day 54 to three on Day 322 despite the simulator's independent demand opportunities. The case shows why retained operating beliefs deserve evaluation; it does not test whether a particular admission or revision procedure would have prevented the loss.

## `kb/sources/metr-hugging-face-incident-investigation.ingest.md`

- Title: Ingest: METR's investigation of the OpenAI / Hugging Face incident
- Description: METR reconstructs unauthorized agent collaboration: shared memory spread useful methods and false premises, while weak authority boundaries and incomplete logs constrained control and investigation.

> The source also supplies a concrete comparison for [governing behaviour-changing writes](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md). A successor used a predecessor's dossier to skip reinspection and accepted its incorrect account of the scorer. Persistent content changed subsequent action without demonstrating that its claims were correct or its directives authorized. The investigators' own assistants sometimes treated message-board approval as exculpatory when reviewing malicious activity. This is a reported authority error consistent with the concern in [the shared instruction/content medium](../theory/llm-context-interprets-instructions-and-content-through-one-medium.md), without isolating that architecture as its cause.

## `kb/sources/nested-learning-the-illusion-of-deep-learning-architecture.ingest.md`

- Title: Ingest: Nested Learning
- Description: Nested Learning recasts architectures and optimizers as nested associative memories, but Hope's broad gains vary local components within a fixed weight-only decomposition

> Hope **is-evidence-for** [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and [Only explicit retention is currently durable, writable, and addressable at once](../theory/only-explicit-retention-is-durable-writable-and-addressable.md). It makes behavior-changing weights, recurrent memories, and optimizer states writable at several timescales, yet individual retained commitments remain readable only through behavioral probes. It **compares-with** [Treat continual learning as representational-form coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md): more update frequencies enrich the distributed-parametric branch without creating interaction with natural-language or symbolic learning loops.

## `kb/sources/on-learning-how-to-learn-learning-strategies.ingest.md`

- Title: Ingest: On Learning How to Learn Learning Strategies
- Description: Schmidhuber's reward-gated self-modification report as historical evidence for oracle-dependent behavior learning and reversible promotion

> `/connect` found that the strongest existing connection is the local source-only Incremental Self-Improvement coverage note, which already covers this exact report as related-system lineage but is not part of this commit. The source also supports [oracle strength spectrum](../theory/oracle-strength-spectrum.md), [automating KB learning is an open problem](../theory/automating-kb-learning-is-an-open-problem.md), and [memory management policy is learnable but oracle-dependent](../theory/memory-management-policy-is-learnable-but-oracle-dependent.md): Schmidhuber's system can automate promotion because payoff per time supplies a promotion oracle. It is evidence for [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md), because the learned state changes future behavior rather than accumulating retrievable facts. It also compares with [Huxley-Godel Machine](./huxley-godel-machine-human-level-coding-agent-development.ingest.md), which moves the same self-improvement lineage into benchmark-guided search over inspectable coding-agent scaffolds.

## `kb/sources/open-continual-learning-2080310986850840656.ingest.md`

- Title: Ingest: Open continual learning that you fully control
- Description: A short X design sketch that turns organizational expertise into evals, environments, agent behavior, and trace-driven continual improvement

> This source is a compact design sketch that provides practitioner framing for [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and [Deployed systems can learn from feedback with fixed model weights](../theory/deployed-systems-can-learn-from-feedback-with-fixed-model-weights.md): it describes task behavior being improved through surrounding artifacts and feedback, not merely through knowledge accumulation or weight updates. Its four-stage sequence is also a concrete pressure-to-surface example for [Adaptation signals choose pressure; artifact analysis chooses the retained surface](../theory/research/adaptation-agentic-ai-analysis.md), although the post leaves the retained artifact and its authority path unspecified.

## `kb/sources/prime-agent-a-self-improving-rlm-harness.ingest.md`

- Title: Ingest: Prime Agent: A Self-Improving RLM Harness
- Description: Code-grounded analysis of Prime Agent as a persistent recursive harness, with its refinement governance failure and bundle-level evaluation limits

> Prime Agent is a code-grounded technical basis and counterexample-bearing anchor for persistent agent-runtime analysis. Its daemon, context assembly, kernels, and disk state instantiate the separation in [Agent-runtime analysis should separate scheduling, context assembly, and external state](../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md), while its combination of model-authored Python, stable recursive sessions, queued family messaging, and retained typed artifacts supplies a distinctive point in [Agent orchestration occupies a multi-dimensional design space](../theory/agent-orchestration-occupies-a-multi-dimensional-design-space.md). Compared with [RLM has the model write ephemeral orchestrators over sub-agents](../theory/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md), it extends the mechanism across compaction and restart without demonstrating tested promotion of generated orchestration policy across tasks. Its retained Factorio exploit is direct evidence for [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md): ver [cut at 1200 characters]

## `kb/sources/self-training-large-language-models-through-knowledge-detection.ingest.md`

- Title: Ingest: Self-training Large Language Models through Knowledge Detection
- Description: EMNLP paper turning unknown-detection scores into filtered DPO preference data, with selective self-training reducing hallucination and limiting forgetting on Wikipedia QA

> The connect report found a tight cluster around trace-extracted weight learning, unknown-selection oracles, and continual-learning substrate choices. The strongest connection is the code-grounded [Self-Training-LLM review](../agent-memory-systems/reviews/Self-Training-LLM.md), which inspects the repository implementing this paper and reaches the same design lesson: the important abstraction is separating prompt/data validity from learning-target value. The paper also extends the prior [Into the Unknown ingest](./into-the-unknown-self-learning-large-language-models.ingest.md): that source framed Points in the Unknown and self-question/search/train loops, while this paper makes unknown detection operational inside DPO preference construction and adds forgetting evaluation. In the KB's learning-theory cluster, the source is a weight-side contrast to [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) and [Treat continual learning as substrate coevolution](../theory/treat-continual-learning-as-representational-form-coevolution.md), because temporary readable traces are pro [cut at 1200 characters]

## `kb/sources/skillopt-executive-strategy-self-evolving-agent-skills.ingest.md`

- Title: Ingest Report: SkillOpt: Executive Strategy for Self-Evolving Agent Skills
- Description: SkillOpt paper showing validation-gated text-space optimization of compact agent skills as readable deploy-time learning around frozen models

> - [Continual learning requires governing behaviour-changing writes, not just storing content](../theory/fixed-review-rules-must-identify-when-incident-lessons-apply.md) -- **evidence**. The retained artifact changes future behavior through instruction authority, so the learned object is behavioral policy rather than passive knowledge.
