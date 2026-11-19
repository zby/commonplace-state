---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.md"
source_has_frontmatter: true
date: "2026-08-04"
depth: standard
---

# Connection Report: The Optimal Choice of Hypothesis Is the Weakest, Not the Shortest

**Source:** [The Optimal Choice of Hypothesis Is the Weakest, Not the Shortest](../../../sources/optimal-choice-of-hypothesis-is-the-weakest-not-the-shortest.md)

## Discovery Trace

**Curated heads:**

- Read the sources, notes, reference, agent-memory-systems, and agentic-systems `README.md` files plus the notes tags hub. The strongest routing signal was the notes learning-theory area; its learning-theory, discovery, evaluation, and constraining heads were read. The fixed-decomposition and formal-reach clusters were stronger than the broad compression and evaluation clusters.
- A targeted follow-up read the explanatory-reach definition surface in `first-principles-reasoning-selects-for-explanatory-reach-over.md` and followed its distinction between transfer produced by a captured mechanism and mere breadth of application. This exposed a concept boundary absent from the original pass: Bennett's technical `weakness` predicts task coverage but is not itself explanatory-reach.
- The agent-memory-systems and agentic-systems heads exposed no casebook entry whose retained-memory or harness mechanism turns on extension-size weakness. Reference concerns the shipped Commonplace system and produced no plausible target for this external induction result.

**Complete title and description scans:**

- `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` was run over all five authorised local destinations: 330 notes headings, 127 reference headings, 172 agent-memory-systems headings, 11 agentic-systems headings, and 426 sources headings.
- `rg '^description:' kb/<destination>/ --glob '*.md'` was run over the same five destinations: 327 notes descriptions and the complete description surfaces of reference, agent-memory-systems, agentic-systems, and sources were evaluated. The title/description pass promoted the fixed-decomposition, formal reach-assessment, generality, No Free Lunch, and DreamCoder candidates below.

**Body search:**

- `rg -n -i 'weakness|weakest hypothesis|weak hypothesis|no more specific' kb/notes/ --glob '*.md'` -- no lexical use of Bennett's technical sense of weakness; ordinary-language hits were rejected.
- `rg -n -i 'description length|minimum description|MDL|Ockham|Occam' kb/notes/ --glob '*.md'` -- promoted the DreamCoder neighborhood through `theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md`; direct notes hits about frontmatter description length were rejected as homonyms.
- `rg -n -i 'uniform distribution|task distribution|distribution over tasks|no free lunch' kb/notes/ --glob '*.md'` -- no direct note hit, which made the existing No Free Lunch ingest the relevant source-level comparison.
- `rg -n -i 'hypothesis class|inductive bias|fixed vocabulary|representable|expressive' kb/notes/ --glob '*.md'` -- promoted `learning-inside-a-fixed-decomposition-inherits-its-mistakes.md` and the linked scope-warrant neighborhood.
- `rg -n -i 'compression.*generali[sz]|generali[sz].*compression|specificity.*generali[sz]|generali[sz].*specificity' kb/notes/ --glob '*.md'` -- found boundary-statability and compression-ablation notes, but none states that description length is a general proxy for transfer.
- `rg -n -i 'explanatory-reach.{0,80}(mechanism|why|structure|generali|scope)|(?:mechanism|why|structure|generali|scope).{0,80}explanatory-reach' kb/notes/ --glob '*.md'` -- promoted the explanatory-reach definition as a contrast: the definition requires a mechanism and premise-sensitive consequences, while Bennett's own empty-hypothesis limit maximizes extension without explanatory content.
- `rg -n -i 'weakest assumptions|no more specific|less specific|extension size|description length|minimum description|uniform task|task distribution' kb/notes/ --glob '*.md'` -- confirmed that the collection's ordinary phrase "weakest assumptions" is not Bennett's registered technical quantity; the former removes unused premises from an argument, while the latter counts the extension of a hypothesis inside a fixed language.
- The same five focused searches were run over `kb/sources/`. They promoted the No Free Lunch and DreamCoder ingests; SuperARC, ROME, compression-faithfulness, and generic induction-bias hits were evaluated and rejected as measuring different objects.
- `rg -n -i 'weakness|weakest hypothesis|description length|minimum description|MDL|Ockham|Occam|uniform distribution|task distribution|no free lunch|hypothesis class|inductive bias|fixed vocabulary|compression.*generali[sz]'` was run separately over reference, agent-memory-systems, and agentic-systems. Agent-memory hits concerned changing task distributions in retained policies rather than hypothesis selection; reference and agentic-systems produced no articulated candidate.

**Link following:**

- Followed the fixed-decomposition note to `use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md`, `only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md`, `bitter-lesson-selects-against-unearned-reach-not-against-structure.md`, and `exact-implementation-does-not-validate-a-requirement.md`. These sharpen the scope warning but duplicate the direct fixed-decomposition edge for this source.
- Followed the learning-theory head through `learning-is-not-only-about-generality.md` and the generality-for-reliability note. The former supplies a distinct objective-level contrast; the latter is a downstream trade-off rather than a claim this paper tests.
- Followed the DreamCoder ingest into `formal-systems-assess-explanatory-reach-through-causal-and-proof.md` and the theory-mediated-learning neighborhood. The formal-reach note passed because Bennett's theorem is exactly a utility comparison proved inside a supplied language and distribution; the broader theory-mediated claim was rejected because the binary-arithmetic experiment does not test explicit-theory retention under structured shifts.
- Followed the explanatory-reach definition into `generality-bought-to-avoid-counterexamples-is-paid-for-in.md` and `abstract-an-experience-only-when-you-can-state-the-boundary.md`. Both reinforce that coverage without exclusions or a statable boundary is not explanatory content, but neither is as direct a reader destination as the definition itself.

## Connections Found

- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **compares-with**: Bennett's `weakness` is extension size, so it rewards a valid hypothesis for admitting more possible decisions under a uniform task prior; explanatory-reach instead requires a criticizable account of why a pattern transfers and how conclusions change when a load-bearing premise changes. The paper's theorem can have explanatory-reach inside its formal model, while the hypotheses its proxy selects need not: Bennett's own empty-hypothesis limit maximizes modeled generalisation while explaining nothing.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **rests-on**: Bennett's learner selects only among models expressible in a fixed vocabulary `v`; the paper's theorem and arithmetic comparison establish relative performance inside that update space, not warrant for the vocabulary, child/parent task construction, or uniform task prior.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **is-evidence-for**: the paper proves an optimal proxy over a formally specified finite language and explicitly locates the result's boundary in that language and task distribution, giving the note a compact non-causal example of genuine within-model reach whose translation remains unchecked.
- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) -- **compares-with**: Bennett treats generalisation probability as the performance target and cites generalisation as intelligence, while the KB note separates generality from reliability, speed, cost, and capacity-to-learn; following the edge prevents importing the paper's one-axis objective as a complete learning objective.
- [Ingest: The No Free Lunch Theorem](../../../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) -- **compares-with**: both arguments turn on a uniform distribution, but No Free Lunch averages over all problem functions while Bennett defines a particular finite language, task space, and parent/child relation in which extension size changes how many tasks a model satisfies. The comparison is needed to determine whether the apparent disagreement is a different sample space rather than a contradiction.
- [Ingest: DreamCoder](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) -- **compares-with**: DreamCoder uses description-length reduction as a retention gate and reports held-out transfer in curated symbolic domains, whereas Bennett constructs a formalism and binary-arithmetic experiment where minimum description length loses to extension-size weakness. Together they make proxy performance visibly representation- and task-distribution-relative.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) → source -- **evidenced-by**: Bennett supplies a formal boundary case showing that broad generalisation can be obtained by semantic permissiveness alone. A short scope example would sharpen the definition's existing claim that explanatory-reach is not unlimited generality: the paper's theorem is a bounded explanation, but extension size is not a measure of explanatory depth.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) → source -- **evidenced-by**: Bennett fixes states, vocabulary, statement language, task relation, and available model selection before comparing proxies, then concedes that tasks outside the vocabulary's representable subset are excluded; this is a worked formal instance of the note's effective-update-space boundary.
- [Formal symbolic systems assess explanatory-reach only through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) → source -- **evidenced-by**: the proof establishes a quantified optimality claim under explicit axioms while leaving the task prior and representation outside the proof, matching the note's proof-route/formalization-boundary distinction.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Only derivation and inheritance warrant a decomposition's scope claim; discriminating use earns it](../../../notes/only-derivation-and-inheritance-warrant-a-scope-claim-use-earns-it.md) -- genuine scope relevance, but the direct fixed-decomposition target already carries this premise and gives a more precise reader need for an experiment-bearing source.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- the binary experiments are local evidence, but the paper's central fixed choices are more directly handled by the effective-update-space note; a second scope edge would duplicate that route.
- [Constraining and extraction can trade generality for reliability, speed, or cost](../../../../notes/constraining-and-extraction-both-trade-generality-for-reliability.md) -- shares a generality axis, but Bennett compares generalisation proxies and does not evaluate reliability, speed, or cost, so the articulation would import an untested trade-off.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- its DreamCoder discussion mentions description length, but Bennett does not compare explicit-theory retention with episodic or parametric pathways under controlled shifts.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- Bennett's extension semantics resemble that note's "content is what a claim rules out" account, but the paper does not study defensive vocabulary widening or its precision/readability mechanism; the explanatory-reach definition carries the useful distinction without importing those untested claims.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) -- Bennett states the prior and representational boundary of his theorem, but his hypothesis-selection proxy does not recover a lesson's applicability condition or rationale; shared concern with generalisation is not enough for a separate edge.
- [Ingest: SuperARC](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) -- measures algorithmic compression capability rather than whether compression is an optimal hypothesis-selection proxy; lexical overlap would confuse two uses of compression.
- [Ingest: On the "Induction Bias" in Sequence Models](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) -- shows architecture-specific data-efficiency differences, but does not compare weakness, description length, or task priors.

## Index Membership

None. The sources collection has no curated topical index for this source family; the authored ingest report will carry the durable routing surface.

## Synthesis Opportunities

The paper, the No Free Lunch ingest, DreamCoder, and the fixed-decomposition note jointly imply a higher-order claim not yet stated directly: **a hypothesis-selection proxy is optimal only relative to both a task distribution and a representational decomposition**. Bennett supplies a proof after fixing both; No Free Lunch shows uniform averaging can erase every advantage under a broader problem space; DreamCoder supplies a domain where description length is useful; and the fixed-decomposition note explains why none of those results validates choices held outside the comparison.

The paper and the explanatory-reach definition also imply a narrower clarification worth retaining: **statistical breadth and explanatory-reach are separate properties**. A semantically permissive hypothesis may cover many modeled tasks because it rules out little, while an explanation earns reach by naming structure that constrains counterfactual changes and exposes where it fails.

## Maintenance Observations

None.

## Flags

- The apparent tension with No Free Lunch should not be called a contradiction without reconciling the two task spaces and conditioning assumptions.
- Do not equate Bennett's technical `weakness` with the notes collection's instruction to state a claim under the "weakest assumptions" its argument uses. One measures a hypothesis's extension in a fixed language; the other removes premises that do no argumentative work.
