---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/a-new-era-of-theory-driven-ai-research-2084779496549548323.md"
source_has_frontmatter: true
date: "2026-08-18"
depth: standard
---

# Connection Report: A new Era Of Theory-Driven AI Research

**Source:** [A new Era Of Theory-Driven AI Research](../../../sources/a-new-era-of-theory-driven-ai-research-2084779496549548323.md)

## Discovery Trace

**Description listing scan:**
- Read the curated heads for `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`. For notes, also read `tags-README.md` and the discovery, learning-theory, evaluation, and foundations heads. The source tag `x-article` has no corresponding tag README, so no complete-tag shortcut applied.
- Generated the full title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for every authorised local destination. The notes surface identified explanatory-reach, discovery lifecycle, theory-mediated learning, fixed-decomposition, and verification-oracle candidates. The reference surface described the shipped Commonplace system rather than this source's claim. The agent-memory and agentic-system surfaces had no candidate whose design this essay documents. The sources surface identified the existing research-taste and scientific-model-discovery captures.
- Ran `rg '^description:' kb/<destination>/ --glob '*.md' | rg -i 'theor|predict|discover|experiment|research|explan|hypothes|verification|oracle|benchmark'` for each authorised destination. Kept the four note candidates below and the research-taste comparison; rejected system and current-state documentation matches as scope-only overlap.

**Topic indexes:**
- [Discovery](../../../../tags/discovery-README.md) supplied the lifecycle, explanatory-reach, and theory-mediated-learning cluster.
- [Evaluation](../../../../tags/evaluation-README.md) and [Learning theory](../../../../tags/learning-theory-README.md) supplied the verification-boundary and fixed-decomposition checks.
- The agent-memory and agentic-system indexes contained systems that run experiments, but none that this essay describes or evaluates as a system.

**Body search:**
- `rg -n -i 'predictive theory|theory.{0,40}experiment|experiment.{0,40}theory|post-hoc|hyper-parameter|autoresearch|auto-research|research taste|scientific discovery|theory-mediated|explanatory-reach' kb/<destination>/ --glob '*.md'` -- confirmed the explanatory-reach, theory-mediated-learning, verification-boundary, and research-taste candidates; source matches for MDA and harness engineering were useful comparison context but redundant as durable edges.
- `rg -n -i 'problem selection|brainstorming|researcher|applied math|theorem' kb/notes/ --glob '*.md'` -- confirmed that the source splits automatable theory work from researcher-owned problem selection, which qualifies rather than overturns the verification-boundary claim.

**Link following:**
- Followed [first-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) into its negative test and its existing research-taste evidence. The post supplies an unusually direct practitioner formulation of the same discriminator: a post-hoc account that can explain unsuccessful alternatives lacks predictive force.
- Followed [theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) into its MDA and DiscoverPhysics evidence. Those sources test parts of the pathway; this post adds a cost-transition conjecture, not stronger empirical evidence.
- Followed [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) into the earlier [research-taste ingest](../../../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md). The two essays disagree at headline level but converge after task decomposition: theory derivation and mathematical checking may automate while problem choice and research value remain weak-oracle work.
- Read [learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) because the author reports an intervention. The available signal is the author's judgment of “major progress” on several selected theory problems; the coding agent can compose mathematical and coding operations within an unspecified tool setup; its hypothesis space and the problem-selection, representation, evaluation, and comparison choices remain fixed or undisclosed.

## Connections Found

- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) -- **rests-on**: the post's predictive-versus-post-hoc theory distinction depends on the same negative test: a useful explanation must rule out alternatives and make discriminating predictions, not merely rationalize observed success.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- **compares-with**: the note conjectures fewer target observations when an addressable theory captures preserved structure; the post proposes a neighboring payoff in which cheaper theory construction reduces expensive experimental search, but supplies no controlled shift or experiment-count comparison.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) -- **compares-with**: the post's preferred rapid alternation among brainstorming, quantifiable goals, theory, and experiment is a practitioner-shaped version of the conjecture-consequence-test core, while leaving acceptance and integration implicit.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **compares-with**: the post is a timely counterpressure against treating “research” as one unverifiable unit; it reports mathematics and theory-development work moving toward automation while leaving problem selection and impact judgment with the researcher.
- [When code is free, research is all that matters](../../../../sources/when-code-is-free-research-is-all-that-matters-2031072399731675.ingest.md) -- **compares-with**: Tam treats research taste as the scarce, weak-oracle residue, whereas Defazio claims theory development itself has become much cheaper; both retain problem choice and goal formation as the researcher's work.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) → source -- **evidenced-by**: the captured essay is a practitioner statement that post-hoc theories able to explain rival failures lack the predictive constraint the note calls explanatory-reach.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidenced-by**: the post qualifies the note by showing why task decomposition matters inside research, while its retained human role remains concentrated in weak-oracle problem and goal selection.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- the post's confidence that impactful work will remain apparent creates a tension, but paper visibility and synthesis-value evaluation are different objectives; an edge would overstate the shared mechanism.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- both warn against plausible reasoning without validity, but the note concerns evaluating a supplied reasoning path and the post concerns producing predictive theories.
- [Evaluation automation is phase-gated by comprehension](../../../../notes/evaluation-automation-is-phase-gated-by-comprehension.md) -- the post also favors observation-informed iteration, but it does not describe evaluator construction or calibration.
- [Model Discovery Agent ingest](../../../../sources/model-discovery-agent-bayesian-experiment-design.ingest.md) -- MDA is a stronger empirical instance of theory-guided experiment choice, but adding it would turn this ingest into a map of existing sources rather than clarify the essay's role relative to casebook notes.
- `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` candidates -- rejected because the essay neither describes the shipped Commonplace system nor documents a memory system or concrete agent harness.

## Index Membership

None.

## Synthesis Opportunities

The Defazio and Tam essays together sharpen a decomposition already available in the verification-boundary note: “research” separates into problem selection, theory generation, formal or empirical checking, experiment execution, and value judgment, each with a different oracle. No new synthesis note is needed unless cases accumulate that contradict the existing note's task-decomposition caveat.

## Maintenance Observations

- The installed X snapshot command omitted the snapshot type's required `genre` field. Ingestion should classify it before validating the newly created snapshot.

## Flags

- The source is experiment-bearing only through an uncontrolled personal intervention: selected theory problems were given to one unspecified coding-agent setup and progress was assessed by the author. Improvement is therefore evidence only for usefulness within that setup, not for the fixed problem sample, tools, hypothesis space, evaluation criterion, or theory-first decomposition.
