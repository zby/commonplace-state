---
description: "Discovery report for possible KB connections from Why Software Factories Fail: Turning the lights back on"
type: kb/cache/types/connect-report.md
source: "kb/sources/why-software-factories-fail-lights-back-on-2081058573556306030.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: Why Software Factories Fail: Turning the lights back on

**Source:** [Why Software Factories Fail: Turning the lights back on](../../../sources/why-software-factories-fail-lights-back-on-2081058573556306030.md)

## Discovery Trace

**Description listing scan:**
- Read the curated heads for context engineering, constraining, computational model, and evaluation, plus the top-level heads for reference, agent-memory systems, agentic systems, and sources. Generated the full title surface with `rg -N --no-heading -m1 '^# ' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'`.
- Scoped descriptions with `rg '^description:.*(frontload|specif|planning|review|slice|increment|constraint|oracle|verification|architecture|design|human|feedback|decompos)' ... -i`. The strongest candidates concerned specification timing, frontloading, interpretation-error propagation, oracle discrimination, and human/automation function allocation. Agent-memory and agentic-system matches did not pass the articulation test because they describe runtime architectures rather than staged human steering of generated code.

**Topic indexes:**
- `context-engineering-README.md` surfaced frontloading as precomputing known inputs for a later call.
- `constraining-README.md` surfaced specification strategy and the boundary between fixing knowable intent early and leaving execution-discovered facts live.
- `computational-model-README.md` surfaced specification-level separation and bounded-call decomposition.
- `evaluation-README.md` supplied the oracle-hardening frame but no settled note specifically about maintainability verification.

**Body search:**
- `rg -n -i 'vertical slice|tracer bullet|program design|call graph|file.tree|planning.*review|review.*planning|early feedback|resteer|rework|specification level|expensive.*change|decision.*review|human.*loop|function allocation|frontload' ...` found the specification-strategy cluster and empirical developer-control sources.
- `rg -n -i 'human.analysis.first|analysis.first|review.*earl|earl.*review|progressive.*review|incremental.*review|small.*diff|small.*change|function allocation' ...` found the function-allocation framework and adjacent early-review evidence.
- Read the temporary `/tmp/maintainability-oracles-working-note.md` only to test whether Part II answers its open questions; it is not a durable candidate and is not linked from this report.

**Link following:**
- Followed specification strategy to changing requirements and the executor-author boundary. Product, architecture, and program-design reviews frontload intent that humans can know, while vertical slices preserve a live feedback path for facts learned only during execution.
- Followed frontloading to its partial-evaluation account. The source is a cross-domain instance: settle expensive human decisions once before code generation rather than reconstruct them during a large diff review.
- Followed the automation boundary to discrimination and error correction. The source keeps the human as current maintainability oracle and merely names better verifiers as future work; it does not demonstrate an automated composite oracle.
- Followed the professional-developer study and the Parasuraman function-allocation ingest. Both independently support graded, task-dependent supervision rather than one scalar autonomy setting.
- Followed the first article and `The Bug That Shipped`. Part I supplies the verifier-gap diagnosis; the latter supplies evidence that coding models can possess failure knowledge that undirected review fails to select. Part II contributes the mitigation of explicit staged questions and short feedback intervals.

## Connections Found

- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- **evidence**: the four-phase method puts knowable product and design decisions in upfront artifacts, then uses vertical slices for understanding that emerges only through execution.
- [Frontloading spares execution context](../../../../notes/frontloading-spares-execution-context.md) -- **evidence**: product, architecture, and program-design reviews precompute human decisions so the coding call receives settled constraints and later review need not reconstruct them from a large implementation.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) -- **evidence**: early review and small vertical slices bound how far an agent's wrong interpretation propagates before a human can observe and correct it.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **evidence**: the source's tiered process fixes privileged intent and high-leverage design choices upfront while leaving small or execution-obvious tasks to one-shot agents; vertical slices provide the live evidence needed to revise rather than overcommit the plan.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) -- **evidence**: the author retains human review because current automated judges may generate good code often yet cannot reliably identify the maintainability failures that require intervention.
- [Professional Software Developers Don't Vibe, They Control](../../../../sources/professional-software-developers-dont-vibe-they-control.ingest.md) -- **compares-with**: the empirical study independently observes experienced developers using planning, small agent steps, tests, version control, and code review—the same control posture prescribed here.
- [A Model for Types and Levels of Human Interaction with Automation](../../../../sources/model-types-levels-human-interaction-automation.ingest.md) -- **compares-with**: the article's 80/20 task tiers and phase-specific human gates instantiate graded function allocation rather than a single human-in/out setting.
- [Why Software Factories Fail](../../../sources/why-software-factories-fail-2080697380379427275.md) -- **compares-with**: Part I diagnoses delayed maintainability verification as the failure of lights-off factories; Part II responds by restoring the human oracle upstream and at short implementation intervals.
- [The Bug That Shipped](../../../../sources/the-bug-that-shipped-2035319413474206122.ingest.md) -- **compares-with**: that experiment shows models can diagnose failures when explicitly probed but omit them in generic self-review, supporting Part II's use of structured design artifacts and staged questions rather than undirected reviewer calls.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) → source -- **evidence**: the staged workflow is a practitioner case of placing disambiguation in the earliest artifact that can truthfully carry it.
- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) → source -- **evidence**: vertical slices provide a coding-agent instance of limiting interpretation-error propagation.
- [The augmentation-automation boundary is discrimination not accuracy](../../../../notes/the-augmentation-automation-boundary-is-discrimination-not-accuracy.md) → source -- **evidence**: the retained human reviewer supplies per-instance discrimination that current model judges lack for maintainability.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Specification-level separation recovers scoping before it recovers error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) -- rejected because the article separates product, architecture, and program design conceptually but does not provide isolated execution frames or a DSL-level scoping mechanism.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) -- rejected because vertical slices iterate one feature and do not establish cross-run pattern stability before codification.
- [Process structure and output structure are independent levers](../../../../notes/process-structure-and-output-structure-are-independent-levers.md) -- rejected as adjacent but weak: the workflow constrains process, yet the article offers no comparison against output structure.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- rejected as a direct edge because Part II proposes a human oracle and short loops, not amplification from multiple weak automated checks.

## Index Membership

None

## Synthesis Opportunities

Part I, Part II, the specification-timing cluster, and the automation-boundary cluster imply a higher-order operating principle: when the decisive oracle is expensive, move its judgments to the earliest truthful decision surface and shorten the unchecked span between later judgments. This reduces correction cost without pretending the oracle has been automated.

Together with `The Bug That Shipped`, the series also supports a distinct conjecture: a model may possess relevant quality knowledge while an execution loop underselects it because the operative correctness oracle is stronger than the maintainability oracle. Part II does not itself establish that mechanism or show how to combine weak automated maintainability signals.

## Maintenance Observations

None

## Flags

- Split candidate: the source independently supports specification timing, feedback-interval design, and graded human/automation allocation.
- Open tension: the article calls maintainability failure a model-training problem but offers no evidence distinguishing absent model knowledge from known considerations that the training and execution objectives underweight.
