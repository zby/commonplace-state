---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/falsifybench-inductive-reasoning-rule-discovery-games.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games

**Source:** [FALSIFYBENCH: Evaluating Inductive Reasoning in LLMs with Rule Discovery Games](../../../sources/falsifybench-inductive-reasoning-rule-discovery-games.md)

The target is a **snapshot** under `kb/sources/`, so it is immutable. Per `kb/sources/COLLECTION.md`, no link may be authored into it and the load-bearing output of this run is the **Reverse-edge Candidates** section. The `Connections Found` entries are recommendations for the matching `falsifybench-inductive-reasoning-rule-discovery-games.ingest.md`, **which does not exist yet** — they have no authored surface to land on until one is created.

## Discovery Trace

**Collection contract read first:**
- `kb/sources/COLLECTION.md` — outbound section: snapshots are immutable, ingest reports carry the outbound surface. Authorised destinations: `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`. Explicitly excluded: `kb/work/`, `kb/instructions/`. Label set: `evidence` (notes), `abstracted-from` (notes), `rationale` (notes), `compares-with` (sources, agent-memory, agentic-systems), `defined-in` (notes/definitions), `see-also` (any, sparingly). Note that `kb/reference/` is reachable only through `see-also` — no substantive label targets it from this collection.

**Topic indexes:**
- `kb/notes/discovery-README.md` (`complete: true`, so the by-tag `rg` sweep over `discovery` was **skipped** per the mark) — yielded the four operation notes (`conjecture-is-seeing-...`, `definitions/discovery-lifecycle`, `automated-synthesis-is-missing-good-oracles`, `known-target-discovery-benchmarks-...`) plus the reach cluster. This index alone produced the three strongest candidates.
- `kb/notes/learning-theory-README.md`, `kb/notes/tags-README.md` — confirmed `discovery` is a child of `learning-theory` and that the curated head above is the right entry; no additional candidates.
- `kb/sources/README.md` — prose orientation only, no enumerated source listing, so no index entry to propose.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (43 KB, ~430 titles), then filtered with `rg -iN 'test|verif|oracle|explor|curio|experiment|benchmark|evaluat|falsif|hypothes|discover|conject|scientific'` — surfaced `systematic-prompt-variation-serves-verification-and-diagnosis-not.md` and `reasoning-production-is-not-reasoning-evaluation.md`, which the topic indexes had missed.

**Body search:**
- `rg -il 'falsif' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` — ~60 files; too broad, mostly incidental uses of "falsifiable". Narrowed below.
- `rg -il 'popper|refutation|conjectur' ...` — surfaced `mechanistic-constraints-make-popperian-kb-recommendations-actionable.md`, `title-as-claim-exposes-commitments-enabling-popperian-maintenance.md`, `definitions/discovery-lifecycle.md`.
- `rg -in 'wason|2-4-6|negative test|disconfirm|confirmation bias|falsification-seeking' ...` — the decisive query. Hits: `first-principles-reasoning-selects-for-explanatory-reach-over.md` ("## The negative test", four-part test), `definitions/reach-assessment.md` (three separate references to "the four-part negative test"), `human-writing-structures-transfer-to-llms-because-failure-modes.md` and `sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md` (Wason selection task), `sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.md` (answer confirmation bias, ~15 hits), `abstract-an-experience-only-when-you-can-state-the-boundary.md`, `reach-assessed-commitments-may-cut-target-observations-under-shifts.md`.
- `rg -il '\binductive\b|\binduction\b' ...` — mostly Peirce/PDSA material already reached through `discovery-lifecycle`; added no new keepers.
- `rg -N --no-heading '^description:' <candidate list>` over sibling snapshots — used to judge the `compares-with` set (DiscoverPhysics, agentic automata learning, environmental curiosity, GIANTS, VAIR/enigma, content effects) against non-keepers (SuperARC, EsoLangBench, self-revising discovery systems, into-the-unknown).

**Link following:**
- From `known-target-discovery-benchmarks-show-reachability-not-discovery.md` one hop: → `automated-synthesis-is-missing-good-oracles.md`, `oracle-strength-spectrum.md`, `the-boundary-of-automation-is-the-boundary-of-verification.md`, `conjecture-is-seeing-the-particular-as-an-instance-of-the-general.md`, and `sources/giants-...`. Revealed that GIANTS is the KB's existing worked instance of a known-target discovery benchmark and that FALSIFYBENCH is the second — the cluster to join.
- From `definitions/reach-assessment.md` one hop: → `first-principles-reasoning-selects-for-explanatory-reach-over.md`, `abstract-an-experience-only-when-you-can-state-the-boundary.md`, `reflection-makes-retained-lessons-second-order.md`, `warranted-autonomy-is-bounded-by-oracle-domain.md`. Confirmed the definition's stated open problem ("reach-assessment is observed only in LLM-mediated evaluation ... Commonplace has no theory for why") is exactly what this paper measures behaviourally.
- From `mechanistic-constraints-make-popperian-kb-recommendations-actionable.md` one hop: → `error-correction-works-above-chance-oracles-with-decorrelated-checks.md`, `agentic-systems-interpret-underspecified-instructions.md`. Confirmed the falsifier-block argument currently rests on an untested premise about model behaviour.

## Connections Found

*(Recommendations for a future `falsifybench-inductive-reasoning-rule-discovery-games.ingest.md`; the snapshot itself is never the link author.)*

- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **evidence**: FALSIFYBENCH is a reinvention-construction known-target benchmark — the rule is authored and hidden, so success means recovering a planted generalization — giving the note a second worked instance beside GIANTS, and one that grades the *search process* (test selection) rather than only target similarity.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) — **evidence**: the definition asks a system's evaluator to apply the four-part negative test to its own candidate commitments and records the prose route as an open problem; this paper measures the closest behavioural proxy across 12 models and reports that negative-testing capacity, not confirmation-seeking, is the primary driver of success.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — **evidence**: the note's third test ("can it be criticized?") is asserted as a quality lever; FALSIFYBENCH is empirical support that seeking disconfirmation is the behaviour that separates better from worse hypothesis-formers, not merely a rhetorical virtue.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **evidence**: the lifecycle's consequence-derivation phase requires stating "what would count against" a conjecture before the test phase; the paper's turn-level failure analysis is direct measurement of whether LLMs perform that step in a closed loop, supporting the phase boundary as a real capability gap rather than bookkeeping.
- [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — **evidence**: the note argues criticism must be structural because models will not do it ambiently, and proposes falsifier blocks on that basis. This paper supplies the missing empirical leg — models that do not actively seek falsification underperform — and its "reasoning models beat instruction-tuned models but none approach optimal" result bounds how much the ambient route can be relied on.
- [Conjecture is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — **evidence**: the Wason 2-4-6 game is the canonical case of positing a general rule while proposing particulars to test it; the turn-level analysis is data on how the posit-and-recognize loop actually breaks.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) — **evidence**: the note already uses the Wason selection task (via Lampinen) as its transfer-boundary marker; FALSIFYBENCH covers the *other* Wason paradigm (2-4-6 rule discovery), where confirmation-seeking is the classic human failure, letting the per-convention transfer question be asked on a second task in the same family.
- [DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking](../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.md) — **compares-with**: both are closed-loop experimentation benchmarks where the agent proposes probes, observes feedback, and revises a hypothesis; DiscoverPhysics uses simulated exotic worlds with latent structure, FALSIFYBENCH an abstract rule game, and both report best agents well short of optimal.
- [Can LLM Agents Infer World Models? Evidence from Agentic Automata Learning](../../../sources/can-llm-agents-infer-world-models-agentic-automata-learning.md) — **compares-with**: membership and equivalence queries against a hidden DFA are the automata-learning analogue of negative testing against a hidden rule; both measure hypothesis refinement through *active* querying rather than passive inference.
- [Agents Explore but Agents Ignore: LLMs Lack Environmental Curiosity](../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md) — **compares-with**: complementary deficit in active information use — that paper finds agents surface solutions and fail to exploit them, this one finds agents form hypotheses and fail to test them adversarially.
- [An Enigma of Artificial Reason: the production-evaluation gap in LRMs](../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.md) — **compares-with**: the same confirmation-bias family measured at a different locus — VAIR finds answer confirmation bias when models *evaluate* given reasoning, FALSIFYBENCH finds confirmation-seeking when models *generate* their own tests.
- [Language Models, Like Humans, Show Content Effects on Reasoning Tasks](../../../sources/language-models-like-humans-show-content-effects-on-reasoning-tasks.md) — **compares-with**: the KB's other Wason-family paper; selection task versus 2-4-6, and a natural pairing for anyone asking how far the human confirmation-bias literature transfers to LLMs.
- [GIANTS: Generative Insight Anticipation from Scientific Literature](../../../sources/giants-generative-insight-anticipation-scientific-literature.md) — **compares-with**: the KB's existing known-target discovery benchmark, on the backcast construction; FALSIFYBENCH is the authored-hidden-target construction, so the pair instantiates both target constructions the reachability note distinguishes.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — **see-also**: adjacent companion on what counts as a real test of a mechanism; this paper varies the *instance* to probe a hypothesis, which is the move the note distinguishes from varying the prompt, so a reader working the "which variations test what" question gains a concrete contrast case.

## Bidirectional Candidates

None — the target is an immutable snapshot, so every note-side return path is already listed under Reverse-edge Candidates and every source-side path under Connections Found.

## Reverse-edge Candidates

*(Notes that should author a link **to** this snapshot under `kb/notes/COLLECTION.md`, whose `evidence` label targets `sources`. This is the load-bearing section for a snapshot target.)*

- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) → source — **evidence**: the note's "Two target constructions" section currently carries only GIANTS. FALSIFYBENCH is a clean authored-target instance and also stresses the note's own framing: because it scores the test-selection process, it is a partial counter-case to "the benchmark already knows what counts as success."
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) → source — **evidence**: the definition's "Provenance and departures" section names the prose route as Commonplace's own gap; a citation here gives that open problem its first behavioural measurement rather than leaving it purely asserted.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) → source — **evidence**: the four-part negative test has no external empirical grounding today; this paper corroborates that criticizability-seeking behaviour is discriminating.
- [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) → source — **evidence**: the note's "What would defeat this claim?" block asks whether models could reliably detect contradiction without externalized structure; this paper is evidence on that exact question, and the note has no external sources at all.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) → source — **evidence**: the note's existing external grounding is Peirce and PDSA; this is the first LLM-side measurement of the consequence-derivation → test transition it defines.
- [Conjecture is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) → source — **evidence**: turn-level failure patterns in the 2-4-6 loop are observational data on the posit-and-recognize duality the note describes.
- [Human writing structures transfer to LLMs because failure modes overlap](../../../../notes/human-writing-structures-transfer-to-llms-because-failure-modes.md) → source — **evidence**: extends the note's Wason-based transfer-boundary discussion onto the rule-discovery variant. Weaker than the entries above because the snapshot does not report a human baseline (see Flags).

## Off-authorisation Candidates

- [review-explanatory-reach](../../../../tasks/recurring/review-explanatory-reach.md) — the recurring criterion that restates the four-part negative test is the operational surface this paper speaks to most directly, but `kb/tasks/` appears nowhere in `kb/sources/COLLECTION.md`'s destination list and no label reaches it. **Suggested resolution: reject as off-scope for a source-side link** and let the edge run inbound instead — the criterion or `kb/notes/first-principles-reasoning-selects-for-explanatory-reach-over.md` can cite the snapshot under its own rules. No contract change is warranted from one candidate.
- [ADR 005: quality check placement](../../../../reference/adr/005-quality-check-placement.md) — the explanatory-reach check's placement rationale would be informed by evidence that criticizability-seeking is measurable, but `kb/sources/COLLECTION.md` reaches `kb/reference/` only through `see-also`, and `see-also` does not carry "this evidence supports the design decision." **Suggested resolution: reject for now**; if source→reference evidence edges recur, that is the signal to extend the label table, not this single case.

## Raw Text Candidates

None — every candidate carries frontmatter.

## Rejected Candidates

- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) — the "benchmark manufactures a missing oracle" reading is real but is already carried, with attribution, by `known-target-discovery-benchmarks-show-reachability-not-discovery.md`. A second edge would duplicate rather than add.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — reachable only through the known-target note; a direct edge adds a hop without adding a claim.
- [Title as claim exposes commitments, enabling Popperian maintenance](../../../../notes/title-as-claim-exposes-commitments-enabling-popperian-maintenance.md) — shares Popperian vocabulary, but its subject is human/agent review of *stored* claim titles, not active experiment selection against a hidden rule. Keyword-level match only.
- [Error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — already cites Lampinen for correlated-error content effects; FALSIFYBENCH reports no TPR/FPR-shaped quantity, so it cannot load-bear here.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — the production/evaluation split is about grading supplied reasoning; FALSIFYBENCH's models generate their own probes, so the note's distinction does not apply cleanly. The VAIR snapshot already carries this note's evidence.
- [Into the Unknown: Self-Learning Large Language Models](../../../sources/into-the-unknown-self-learning-large-language-models.md) — self-questioning loop is superficially similar, but it targets knowledge-gap detection via hallucination signals, not hypothesis falsification against feedback.
- [Self-Revising Discovery Systems for Science](../../../sources/self-revising-discovery-systems-agentic-ai.md) — a category-theoretic framework for discovery systems, not an empirical benchmark; the `compares-with` reader-need ("covers a similar/parallel system") is not met.
- SuperARC and EsoLangBench snapshots — both are LLM reasoning benchmarks, but on compression/abstraction and OOD code respectively; no hypothesis-testing loop, so the pairing would be "both are benchmarks" and nothing more.

## Index Membership

None. `kb/sources/README.md` is prose orientation with no enumerated source listing, and `kb/notes/discovery-README.md` is a `tag-readme` carrying `complete: true` — it indexes tagged notes, not source snapshots, so adding a source entry there would break the mark's meaning.

## Synthesis Opportunities

- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) + [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) + this source together imply a claim the KB has not stated: **where an outcome oracle for discovery is unavailable, the search policy can be graded instead of the answer** — negative-testing rate is a process-level proxy that a planted target makes measurable, and it partially escapes the "the benchmark already knows the answer" critique because the scored quantity is the agent's test selection, not its final rule. FALSIFYBENCH plus DiscoverPhysics would be the two worked cases.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) + [Mechanistic constraints make Popperian KB recommendations actionable](../../../../notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) together with this source suggest a second-order claim: **the prose route to reach-assessment is not a single capability but a behaviour with measurable variance across models**, which would make "who can make this judgment" an empirical selection question rather than only an open theoretical problem. Do not author either note during connect.

## Maintenance Observations

- **No curated head for the discovery-benchmark source cluster.** `kb/sources/` now holds at least four benchmark snapshots probing discovery/experimentation capability — GIANTS, DiscoverPhysics, agentic automata learning, and this one — with no shared index. `kb/notes/discovery-README.md` cannot serve: it is a `tag-readme` with `complete: true` and indexes notes only. Anyone arriving at the cluster must rediscover it by `rg`.
- **`kb/sources/COLLECTION.md` has no substantive label toward `kb/reference/`.** Two candidates this run (ADR 005, and by extension the explanatory-reach criterion) wanted a "this evidence supports the design decision" edge and had only `see-also`. One run is not enough to justify a contract change; recording it so a second occurrence can be counted.
- **`kb/notes/mechanistic-constraints-make-popperian-kb-recommendations-actionable.md` carries no external sources** despite making an empirical claim about model behaviour ("criticism must be structural, not ambient"). Its `traits` list omits `has-external-sources`; the reverse edge proposed above would be its first.

## Flags

- **Thin capture.** The snapshot is abstract-level only — no methods, no model list, no numbers, no human baseline, no description of how "negative testing" is operationalized or measured. Every candidate above rests on three summarized findings. An ingest report should either fetch the full paper or explicitly scope its claims to abstract-level fidelity; in particular, do not write that the paper compares LLM confirmation bias to the human 2-4-6 literature, because the capture does not support it.
- **No ingest companion exists.** `kb/sources/falsifybench-inductive-reasoning-rule-discovery-games.ingest.md` is absent, so the `Connections Found` section has no authored surface. Either run `cp-skill-ingest` on the snapshot or treat the Reverse-edge section as the only actionable output.
- **Split candidate.** The source touches 7 notes across 3 topic areas (discovery/benchmarks, explanatory-reach and reach-assessment, human-LLM reasoning transfer) and carries two independent assertions — that negative testing drives rule-discovery success, and that reasoning models outperform instruction-tuned models without approaching optimal. An ingest report should keep those two claims separately attributable.
- **Tension not resolved here.** `known-target-discovery-benchmarks-show-reachability-not-discovery.md` argues that planting the target converts discovery into target reconstruction. FALSIFYBENCH plants a target yet scores the process rather than the reconstruction, which is a partial counter-case to that framing. Flagging without resolving; see Synthesis Opportunities.
- **Uncommitted neighbours.** `kb/notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md` is untracked and several notes in the reach cluster (`definitions/reach-assessment.md`, `first-principles-...`, `reflection-makes-retained-lessons-second-order.md`) have uncommitted modifications. Candidate reasoning above reflects the working tree, not `HEAD`.
