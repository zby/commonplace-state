---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: DiscoverPhysics: Benchmarking LLMs for Out-of-the-Box Scientific Thinking

**Source:** [DiscoverPhysics](../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.md)

The target is a `snapshot` under `kb/sources/`, which the collection contract declares immutable. Nothing below is authored anywhere; the `Connections Found` list is a recommendation for the **not-yet-written** `discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.ingest.md`, and `Reverse-edge Candidates` is the load-bearing section per `kb/sources/COLLECTION.md`.

Load-bearing content of the snapshot, used as the articulation basis:

1. 22 simulated worlds with physics that deliberately deviates from ours (screened/fractional-power gravity, multi-species couplings, hidden dark-matter-like particles, non-coordinate-free physics, time-varying interactions) — an anti-recall design.
2. Agents propose rounds of experiments and observe raw trajectory data — an interventional, action-conditioned protocol.
3. Agents submit **both** a natural-language explanation and a Python implementation of the inferred law — two representational forms of the same commitment.
4. Best agents pass ~half the worlds; failures concentrate on **latent** structure.
5. Strong predictive accuracy does **not** guarantee good conceptual explanations.

## Discovery Trace

**Collection contracts read:**
- `kb/sources/COLLECTION.md` — outbound section "Outbound links". Snapshots never author links; the authored surface is the `.ingest.md`. Authorised labels: `evidence` → notes, `abstracted-from` → notes, `rationale` → notes, `compares-with` → sources / agent-memory / agentic-systems, `defined-in` → notes/definitions, `see-also` → any (sparingly). Excluded destinations: `kb/work/`, `kb/instructions/`. The contract explicitly names reverse-edge as the primary authoring signal for a snapshot.
- `kb/notes/COLLECTION.md` — read to label the reverse-edge candidates correctly. Notes → sources authorises `evidence`, `derived-from`, `abstracted-from`, `see-also`.

**Topic indexes:**
- `kb/notes/discovery-README.md` — `complete: true`, so the by-tag `rg` sweep for `discovery` was **skipped** per skill rule. Flagged from its "The operation" and "Reach" groupings: `known-target-discovery-benchmarks-show-reachability-not-discovery`, `automated-synthesis-is-missing-good-oracles`, `definitions/discovery-lifecycle`, `conjecture-is-seeing-the-particular-as-an-instance-of-the-general`, `first-principles-reasoning-selects-for-explanatory-reach-over`.
- `kb/notes/evaluation-README.md` — no `complete` mark. Flagged `systematic-prompt-variation-serves-verification-and-diagnosis-not` (rejected below) and `brainstorming-how-to-test-whether-pairwise-comparison-can-harden` (rejected, judge-calibration topic).
- `kb/notes/learning-theory-README.md` — frontmatter carries `covered_by: [deploy-time-learning, constraining, discovery, artifact-analysis, agent-memory, llm-interpretation-errors]`, so routing through the `discovery` child was trusted rather than re-swept.
- `kb/agentic-systems/README.md` title sweep — 5 system artifacts (Swamp, Fractal, GBrain, Semantic Engine, Claude Code dynamic workflows); none is a discovery/experimentation harness. No candidate.
- `kb/agent-memory-systems/` title sweep — `reviews/AutoSci.md` and `reviews/voyager.md` are the only discovery-adjacent entries; both are memory-system reviews rather than benchmarks, evaluated and rejected below.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (full claim-title surface, ~300 titles) — used to spot reach/world-model/oracle titles the discovery README does not carry.
- `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'` and same over `kb/agent-memory-systems/`.

**Description listing scan:**
- `rg '^description:' kb/sources/ --glob '*.ingest.md'` filtered through `rg -i 'discover|scien|benchmark|physic|explor|curios|causal|reason'` — surfaced the compares-with cluster: GIANTS, EsoLang-Bench, Into the Unknown, Self-Revising Discovery Systems, Agents Explore but Agents Ignore, An Enigma of Artificial Reason, SuperARC, causal-inference-using-invariant-prediction, towards-causal-representation-learning.

**Body search:**
- `rg -l -i 'benchmark' kb/notes/ --glob '*.md'` — 31 hits; kept `known-target-discovery-benchmarks-*`, `oracle-strength-spectrum`, `the-boundary-of-automation-*`, `reach-assessed-commitments-*`, `first-principles-reasoning-*`. Discarded infrastructure hits (`files-not-database`, `links-README`, `decomposition-heuristics-*`).
- `rg -l -i 'hypothesis|experimental design|active learning' kb/notes/ --glob '*.md'` — surfaced `definitions/discovery-lifecycle`, `diagnostic-richness-constrains-outer-loop-learning-quality`, `mechanistic-constraints-make-popperian-kb-recommendations-actionable`.
- `rg -l -i 'world model' kb/notes/ --glob '*.md'` — 4 hits: `world-models-assess-explanatory-reach-through-action-conditioned`, `definitions/reach-assessment`, `an-action-model-matters-only-through-its-consumption-path`, `structure-inference-needs-capture-at-the-decision-surface`.
- `rg -l -i 'predictive accuracy|prediction.{0,20}explanation|explanatory-reach' kb/notes/ --glob '*.md'` — 30 hits; this query is what produced the strongest cluster (`definitions/reach-assessment`, `reach-assessed-commitments-*`, `formal-systems-assess-*`, `world-models-assess-*`).

**Link following:**
- From `known-target-discovery-benchmarks-show-reachability-not-discovery` one hop → `automated-synthesis-is-missing-good-oracles`, `oracle-strength-spectrum`, `the-boundary-of-automation-is-the-boundary-of-verification`, `conjecture-is-seeing-the-particular-*`, and the GIANTS snapshot. This is the exact neighbourhood DiscoverPhysics should join; GIANTS is already cited there as the backcast exemplar, so the simulator-authored construction is the visible gap.
- From `definitions/reach-assessment` one hop → `world-models-assess-*` (distributed-parametric route), `formal-systems-assess-*` (symbolic route), `first-principles-reasoning-*` (prose route), `reach-assessed-commitments-*`. Reading the routes together is what identified finding (3) — the paper collects a prose artifact and a symbolic artifact for the same commitment — as the sharpest connection in the report.
- From `reach-assessed-commitments-may-cut-target-observations-under-shifts` → its "What would test it" section prescribes controlled shifts of distinct kinds and warns "target accuracy alone will not separate the arms"; finding (5) is an independent report of exactly that separation.
- Path check: all candidate paths below verified present with `ls`.

## Connections Found

Recommended outbound edges for the future `discoverphysics-*.ingest.md`.

- [known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **evidence**: DiscoverPhysics corroborates the reachability reading and adds a **third target construction** beyond the note's backcast/reinvention pair — a simulator-authored world whose law is planted, so the oracle is executable rather than a similarity judgement, yet the target is still known in advance.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) — **evidence**: the benchmark collects a natural-language explanation and a Python implementation of the *same* inferred law, then reports that predictive accuracy and explanation quality come apart — a direct empirical instance of the note's claim that the assessment route must match the representational form carrying the commitment.
- [Reach-assessed commitments may cut target observations under structured shifts](../../../notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md) — **evidence**: the note's "What would test it" section asks for controlled shifts of distinct kinds and states that target accuracy alone will not separate the arms; 22 authored physics worlds are that shift family, and finding (5) is an independent measurement of the accuracy/mechanism gap the note predicts.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) — **evidence**: an agent that predicts trajectories well without a good conceptual account is adaptive fit passing a fit test and failing negative-test item 2 ("does it reach"); the deliberately non-standard physics is what stops pretrained recall from masquerading as explanation.
- [Conjecture is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) — **evidence**: failures concentrating on **latent** structure (hidden dark-matter-like particles) is the note's "hard problem is recognition, not linking" measured on a machine — the agent must posit an unobserved particular before any general law can organize the trajectories.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) — **evidence**: the benchmark supplies a cheap hard oracle for the *predictive* half (run the submitted Python against the simulator) and none for the *explanatory* half, so it isolates the oracle gap the note describes inside a single task rather than across systems.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) — **evidence**: a worked case where one task carries two oracles of different strength simultaneously — hard on trajectory prediction, soft on conceptual explanation — which the spectrum's fixed-artifact framing does not currently illustrate.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **evidence**: the agent protocol (observe raw trajectories → propose a law → design the next experiment → submit for simulator test) instantiates the observation/conjecture/consequence-derivation/test phases in an automated setting, and the ~50% pass rate is a measurement of where the loop breaks.
- [World models assess explanatory-reach through action-conditioned prediction](../../../../notes/world-models-assess-explanatory-reach-through-action-conditioned.md) — **evidence**: corroborates the note's *test surface* (action-conditioned prediction probed under specified shifts) while showing the retained artifact need not be a latent predictor — here it is executable code plus prose. Cite for the test surface; the representational-form half is a contrast, not support.

Source-to-source parallels:

- [EsoLang-Bench](../../../sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming.md) — **compares-with**: the closest methodological sibling in the KB. Both defeat pretraining recall by moving the task into a domain the training corpus cannot contain — esoteric programming languages there, counterfactual physics here — and both then report that scores drop sharply, which is the shared claim that standard benchmarks partly measure corpus fit. EsoLang-Bench also finds interpreter feedback beats textual critique, the direct analogue of DiscoverPhysics's finding that success requires refinement through well-designed experiments.
- [GIANTS: Generative Insight Anticipation from Scientific Literature](../../../sources/giants-generative-insight-anticipation-scientific-literature.md) — **compares-with**: the other scientific-discovery benchmark in the KB, and the contrast is the informative part — GIANTS manufactures a *soft* similarity oracle over historical insights, DiscoverPhysics gets a *hard* executable oracle by authoring the world. Reading them together separates the target construction from the oracle strength it buys.
- [Self-Revising Discovery Systems for Science](../../../sources/self-revising-discovery-systems-agentic-ai.md) — **compares-with**: supplies the architecture side (retrieval/search/discovery typology, MDL/AIC acceptance gates) for which DiscoverPhysics is an evaluation instrument; its MDL/AIC gates are a concrete proposal for the explanation-quality oracle DiscoverPhysics reports missing.
- [Agents Explore but Agents Ignore](../../../sources/agents-explore-but-agents-ignore-llms-lack-environmental-curiosity.md) — **compares-with**: parallel failure mode at a different point in the loop. There, agents observe an explicit solution in context and fail to act on it; here, agents gather trajectory data and fail to infer latent structure from it. Both isolate observation-to-action integration rather than raw capability.
- [Into the Unknown: self-learning large language models](../../../sources/into-the-unknown-self-learning-large-language-models.md) — **compares-with**: the closest self-directed-inquiry loop in the KB (self-question, search, train, with metrics for gap discovery); DiscoverPhysics evaluates the same capability with an external world instead of the model's own hallucination signal as the gap detector.

## Bidirectional Candidates

None. The snapshot is immutable and cannot author a return path; the ingest report would carry the outbound side and the notes the inbound side, so the pair is already covered by the two lists above.

## Reverse-edge Candidates

Per `kb/sources/COLLECTION.md`, this is the primary authoring signal for a snapshot. Each entry is an edge a **note author** would add under `kb/notes/COLLECTION.md` rules (notes → sources authorises `evidence`, `derived-from`, `abstracted-from`, `see-also`).

- [known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) → source — **evidence**: strongest reverse edge in the report. The note's "Two target constructions" section currently has one worked exemplar (GIANTS, backcast) and an unexemplified reinvention branch; DiscoverPhysics is an authored-target case with a leakage control the note does not yet discuss — the target world is *counterfactual*, so historical ordering is unnecessary and canonical-phrase leakage is structurally impossible.
- [Reach-assessed commitments may cut target observations under structured shifts](../../../notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md) → source — **evidence**: the note's testbed design is currently supported only by transfer-literature citations; this is a shipped benchmark that already implements the controlled-shift family and reports the accuracy-vs-mechanism separation the design depends on.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) → source — **evidence**: the definition's Exclusions state "reach-assessment is not empirical testing alone." DiscoverPhysics is the clean illustration: agents that pass the empirical trajectory check can still fail the explanation, so passing tests leaves the explanatory-reach question open.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) → source — **evidence**: the note's "Current attempts" list is drawn from memory systems; a benchmark that instruments the fidelity/novelty/validity split inside one task would strengthen the "Why the oracle is hard to build" section.
- [Conjecture is seeing the particular as an instance of the general](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) → source — **evidence**: latent-structure failure as a quantified recognition failure.
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over.md) → source — **evidence**: candidate replacement or companion for the note's own hedged SuperARC citation ("suggestive... but not load-bearing here"); the predict-well/explain-badly finding bears on the adaptive-vs-explanatory polarity much more directly.

## Off-authorisation Candidates

- [An Enigma of Artificial Reason: the production-evaluation gap in LRMs](../../../sources/an-enigma-of-artificial-reason-production-evaluation-gap-lrms.md) — passes the articulation test in the *other* direction: DiscoverPhysics reports produce-well/explain-badly, VAIR reports solve-well/evaluate-badly, and reading them together is what makes the shared shape visible. But `kb/sources/COLLECTION.md` authorises `compares-with` for "a similar/parallel system", and neither source is a system — they are both benchmark papers whose *findings* rhyme. Suggestion: either widen `compares-with`'s reader-need to cover parallel findings, not only parallel systems, or accept it under `compares-with` on a loose reading; do not downgrade to `see-also`, which loses the reason.
- [Reach-assessment](../../../../notes/definitions/reach-assessment.md) — noted for contract clarity rather than as a separate candidate: it lives under `kb/notes/definitions/`, and the source labels table routes `defined-in` to `notes/definitions` while routing `evidence` to `notes`. The connection's purpose here is corroboration, not term lookup, so the report uses `evidence` and reads `notes` as covering the `definitions/` subtree. If that reading is wrong, the candidate has no authorised label at all — see Maintenance Observations.

## Raw Text Candidates

None.

## Rejected Candidates

- [Formal symbolic systems assess explanatory-reach through causal and proof obligations](../../../../notes/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) — the submitted Python law is a symbolic artifact, so the title looks like a match, but the note's symbolic route runs through *causal and proof obligations*. DiscoverPhysics checks the code by running it against the simulator, which is empirical testing of a symbolic artifact — a different route the note explicitly does not cover. Better handled as a gap than as an edge.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — the source is in tension with it rather than corroborating it; routed to Flags instead of being labelled `evidence`.
- [SuperARC AIT benchmark](../../../sources/superarc-ait-benchmark-llm-compression-abstraction.md) — both are anti-recall abstraction benchmarks, but SuperARC measures algorithmic compression on sequences with no experimental-design component. The overlap is "benchmark that frontier models do badly on", which is keyword-level. Weaker than the EsoLang-Bench parallel already kept.
- [AutoSci](../../../../agent-memory-systems/reviews/AutoSci.md) and [Voyager](../../../../agent-memory-systems/reviews/voyager.md) — closest agent-memory entries by topic (automated science; open-ended skill discovery in an environment). Rejected because both are memory-system reviews describing an architecture, while the source is an evaluation instrument; `compares-with` would assert a system parallel that does not hold.
- [Systematic prompt variation serves verification and diagnosis, not explanatory-reach testing](../../../../notes/systematic-prompt-variation-serves-verification-and-diagnosis-not.md) — surfaced by the `explanatory-reach` query and by `evaluation-README`. Rejected: the note is about varying an LLM prompt surface, whereas DiscoverPhysics varies the *world*. Linking them would blur the distinction the note exists to draw.
- [Causal inference using invariant prediction](../../../sources/causal-inference-using-invariant-prediction.md) and [Towards causal representation learning](../../../sources/towards-causal-representation-learning.md) — surfaced by the description scan and conceptually adjacent (cross-environment invariance as the signature of a real mechanism). Rejected as direct `compares-with` edges: they are methodological foundations rather than parallel sources, and the useful relation runs through the reach-assessment notes that already cite them. Re-examine if the ingest ends up arguing the invariance point directly.

## Index Membership

- [discovery](../../../../tags/discovery-README.md) — this tag README carries `complete: true` and lists **notes**, not sources, so the snapshot itself does not belong in it. Recorded here because the mark constrains a downstream action: if the DiscoverPhysics material ever becomes a new note tagged `discovery`, that note must be added to this README in the same change or the `complete` mark becomes false.
- No other index requires an entry. Sources are discovered by `rg` over descriptions, not by a curated head.

## Synthesis Opportunities

**A hard oracle on the output does not make the *explanation* checkable.** Three artifacts converge on this and none states it: `oracle-strength-spectrum` treats oracle strength as one gradient per task; `definitions/reach-assessment` says empirical testing alone is not reach-assessment; and DiscoverPhysics measures a single task where the predictive oracle is hard and executable while the explanatory oracle stays soft and human. The candidate higher-order claim is that **oracle strength is per-property, not per-task** — a domain can be fully verifiable on its outputs and still supply no oracle for the mechanism that produced them, which is why formal domains do not escape the synthesis-oracle gap as cleanly as `automated-synthesis-is-missing-good-oracles` currently allows in its parenthetical scope note ("in formal domains like mathematics or code composition, synthesis verification *can* be cheap"). Simulated physics is exactly a formal domain where the cheap checker does not close the gap. Not authored here.

## Maintenance Observations

- **Collection-contract gap (source labels vs the `definitions/` subtree).** `kb/sources/COLLECTION.md`'s labels table lists `evidence`/`abstracted-from`/`rationale` with destination `notes` and `defined-in` with destination `notes/definitions`. It does not say whether `evidence` may target a file under `kb/notes/definitions/`. Read strictly, corroborating evidence for a definition note has no authorised label. Existing practice cuts the other way — `definitions/reach-assessment.md` already carries `evidence` edges to sources in its own footer — so the table is probably under-specified rather than restrictive.
- **Collection-contract gap (`compares-with` reader-need).** The label's reader-need is "this source covers a similar/parallel system", which does not fit source-to-source pairs whose *findings* are parallel rather than whose systems are. This is the second connect run shape where benchmark papers rhyme without being systems; a widened reader-need would remove the recurring off-authorisation routing.
- **Missing authored surface.** No `discoverphysics-*.ingest.md` exists, so every `Connections Found` entry is currently unactionable — the ingest must be written before any of them can be authored. `cp-skill-ingest kb/sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific-thinking.md` is the prerequisite step.
- **Unnamed recurring mechanism.** "Make the domain counterfactual so pretraining recall cannot carry the score" is a design move now present in at least three captured sources (DiscoverPhysics's non-standard physics, EsoLang-Bench's esoteric languages, SuperARC's binary-vs-integer encodings) and is not named anywhere in `kb/notes/`. `known-target-discovery-benchmarks-*` describes leakage control for *authored targets* but not this recall-defeating variant.

## Flags

- **Split candidate.** The source connects to 9 notes across 4 topic areas (discovery benchmarks, reach-assessment and representational form, oracle strength, conjecture/recognition) and makes more than one independent assertion (the anti-recall benchmark design; the latent-structure failure; the accuracy/explanation dissociation). Per the connect-report type's edge cases, flagging it: a future ingest should probably foreground the accuracy/explanation dissociation and let the benchmark-design material be a secondary thread, rather than trying to serve all four areas at equal weight.
- **Tension, unresolved.** [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) predicts that automation stalls where verification is expensive. DiscoverPhysics has a cheap, hard verifier — run the submitted law against the simulator — and the best agents still fail about half the worlds. That points at a *generation-side* bound (experiment design, latent-variable positing) that the verification framing does not predict. Either the note needs a stated scope ("verification bounds automation where it binds; generation can bind first") or the source is a counterexample worth arguing with. Not resolved here.
- **Uncommitted target.** `kb/notes/reach-assessed-commitments-may-cut-target-observations-under-shifts.md` is untracked in git at the time of this run. It is one of the strongest candidates in the report, but a future writer should confirm it survives to a commit before authoring an edge to it.
