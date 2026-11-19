---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/dreamcoder-wake-sleep-bayesian-program-learning.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: DreamCoder: Growing generalizable, interpretable knowledge with wake-sleep Bayesian program learning

**Source:** [DreamCoder snapshot](../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.md)

The target is an **immutable snapshot** with **no `.ingest.md` companion yet**. Every candidate below is a recommendation for a future `kb/sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md`, or (in `Reverse-edge Candidates`) for the library artifact that should author the inbound edge. Nothing here has been written into any artifact.

**Capture-fidelity caveat that conditions the whole report:** the snapshot is a `web-fetch` of the arXiv landing page — title, authors, abstract, access links. 32 lines. It contains no method section, no numbers, no bibliography. Mechanism vocabulary used below (wake phase enumeration, sleep-abstraction refactoring, description-length / compression gate, amortized neural recognition model, cumulative library depth) is **not present in the captured text**; it comes from the abstract's summary language plus general knowledge of the paper. A future ingest must re-read the PDF before authoring any load-bearing `evidence` edge. See `Flags`.

## Discovery Trace

**Collection contract read first:**
- `kb/sources/COLLECTION.md` — outbound section confirms: snapshots are immutable and never author links; the ingest report carries the outbound surface; the snapshot's own connect payload is the **reverse-edge** set. Authorised labels: `evidence` / `abstracted-from` / `rationale` → notes; `compares-with` → sources, agent-memory-systems, agentic-systems; `defined-in` → notes/definitions; `see-also` → any (sparingly). Excluded destinations: `kb/work/`, `kb/instructions/`.

**Curated heads read (source carries no `tags:`, so heads were picked by topic):**
- `kb/notes/tags-README.md` (`complete: true`) — routed to self-improving-systems, learning-theory children, computational-model.
- `kb/notes/self-improving-systems-README.md` — the highest-yield head. Its "Example placements" list (Homeostat, parametric self-improvers, Gödel machine, KCSI, Commonplace) has a visible gap exactly where DreamCoder sits.
- `kb/notes/constraining-README.md` — surfaced spec-mining, bitter-lesson, codification definition.
- `kb/notes/artifact-analysis-README.md` (`complete: true`) — **by-tag `rg` for `artifact-analysis` skipped** per the completeness mark; the head enumerated the form/lineage/authority definitions directly.
- `kb/notes/deploy-time-learning-README.md` — surfaced the abstraction-boundary note and learning fundamentals.
- `kb/notes/discovery-README.md` (`complete: true`) — **by-tag `rg` for `discovery` skipped**; head gave oracles, known-target benchmarks, minimum-viable-vocabulary, short-composable-notes.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` — complete claim-title surface generated once, then filtered with `grep -i -E "abstract|composab|reusab|compress|library|symbolic|neuro|bitter lesson|self-play|synthes|invent|discover|generaliz"`. 19 title hits; kept the ones below, rejected the rest as keyword-only (e.g. "A functioning knowledge base needs a workshop layer, not just a library" — "library" in the unrelated sense).

**Description listing scan:**
- `rg -N --no-heading '^description:' kb/sources/ --glob '*.ingest.md' -r ''` piped through `rg -i 'self-improv|program|skill librar|abstraction|library|symbolic|neuro|synthes|discover|curricul|self-play|compress'` — 33 ingest reports flagged; kept 8 as `compares-with` candidates. Strongest signal: `self-revising-discovery-systems-agentic-ai.ingest.md` ("MDL/AIC gates") and `superarc-ait-benchmark-llm-compression-abstraction.ingest.md` ("recursive compression and abstraction").

**Body search (actual queries):**
- `rg -ril "dreamcoder|wake-sleep|wake sleep" kb/` — one pre-existing hit outside the snapshot: `kb/sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming.md` cites "Ellis et al. (2021) DreamCoder" in its bibliography (line 914) and "program synthesis research (Gulwani et al., 2017; Ellis et al., 2021)" at line 179. Confirmed with `rg -n -i "dreamcoder|ellis|library learning"` on that file. The paper is already referenced in-KB; no note or ingest cites it.
- `rg -ril "program synthesis|program-synthesis|library learning|domain-specific language|\bDSL\b" kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems` — mostly DSL-as-config-language hits (ABC contracts, ADR 015, thalo). Rejected: none of these use DSL in the learned-vocabulary sense. Real signal only from `unified-calling-conventions-enable-bidirectional-refactoring.md`.
- `rg -ln -i "voyager|skill librar" kb/notes kb/sources kb/agent-memory-systems` — 20 files. Located `kb/agent-memory-systems/reviews/voyager.md` and `kb/agent-memory-systems/reviews/SkillX.md`, the two closest system analogues, plus `kb/agent-memory-systems/trace-learning-techniques-in-related-systems.md`.
- `rg -n -i "MDL|minimum description|compression" kb/sources/self-revising-discovery-systems-agentic-ai.ingest.md` — confirms that ingest already frames discovery as *gated schema extension* (MDL/AIC/peer review). This is the tightest structural match in the KB to what DreamCoder's abstraction step does.

**Link following:**
- From `self-improving-systems-README.md` → `a-proposal-selection-loop-requires-search-evaluation-and-retention.md`, read in full. Its Homeostat/Gödel-machine boundary discussion gives an explicit slot for a compression-gated instance; the note already names oracle strength as the discriminator.
- From that note → `oracle-strength-spectrum.md`, `automated-synthesis-is-missing-good-oracles.md`, `known-target-discovery-benchmarks-show-reachability-not-discovery.md`. The synthesis-oracle note contains an explicit scope carve-out ("in formal domains like mathematics or code composition, synthesis verification *can* be cheap — proof checkers and test suites serve as hard oracles") that DreamCoder instantiates. Kept.
- From `deploy-time-learning-README.md` → `abstract-an-experience-only-when-you-can-state-the-boundary.md`, read in full: it already cites VOYAGER for granular skill libraries and argues boundary-statability is the abstraction criterion. DreamCoder is the compression-gated counterpoint. Kept as a tension.
- From `constraining-README.md` → `codification-and-relaxing-navigate-the-bitter-lesson-boundary.md` and `definitions/codification.md`, read. Codification is defined as the *natural-language → symbolic* crossing; DreamCoder is symbolic → symbolic, so the definition is a near-miss (see `Rejected Candidates`) and the connection routes to spec-mining and the bitter-lesson note instead.
- From `artifact-analysis-README.md` → `definitions/representational-form.md` (path verified, not read in full) and `reflective-coverage-is-graded-across-representational-forms.md`, read in full. Its "selection-grade coverage of the parametric form" argument maps directly onto DreamCoder's split between an inspectable library and an opaque recognition network.
- Path existence verified for all 19 note candidates and all source/agent-memory candidates by `[ -f ]` sweep.

**Destinations prospected and skipped:**
- `kb/agentic-systems/` — **skipped**. Its trigger is external agentic systems and harnesses (execution loops, orchestration APIs, control surfaces). DreamCoder is a program-induction system, not an agent harness; no plausible match, so no `compares-with` candidate.
- `kb/reference/` — prospected; one candidate found but no fitting label (see `Off-authorisation Candidates`).
- `kb/work/`, `kb/instructions/` — excluded by contract, not prospected.

## Connections Found

Candidates for a future `dreamcoder-wake-sleep-bayesian-program-learning.ingest.md`.

**Notes — `evidence`**

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — **evidence**: DreamCoder realises all three functions with visible separation — search generates candidate programs, a compression criterion evaluates candidate abstractions and can reject them, and accepted abstractions are retained in the language where they change later search. It sits between the note's two named poles: a real reject-capable gate (unlike the Homeostat) that is statistical rather than proof-mediated (unlike the Gödel machine).
- [A self-improving system needs a profile, not a ladder](../../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md) — **evidence**: a placement no single rung captures — computationally autonomous, cumulative (later abstractions build on earlier ones), and reflective over its symbolic library while its neural component stays opaque. Exactly the mixed profile the note argues a ladder cannot express.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) — **evidence**: a non-Commonplace worked case of graded coverage — modification-grade over the symbolic library, at best selection/observation-grade over the parametric recognition model, in one system whose behavior genuinely spans both forms.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) — **evidence**: names the note's own scope carve-out with a system. The note concedes that formal domains can have cheap synthesis verification; DreamCoder is what an unsupervised abstraction-synthesis loop looks like once that oracle exists, and so bounds the claim from outside rather than contradicting it.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) — **evidence**: the paper's headline "independently rediscovers ... Newton's and Coulomb's laws" is a reinvention claim with an experimenter-known target, so the note's authored-input leakage controls apply directly — the primitive set and task suite were chosen after the target was known.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — **evidence** (productive tension): DreamCoder abstracts on a compression criterion, not on a statable boundary condition. In a formal domain a description-length gate substitutes for boundary-statability; the note already cites VOYAGER for per-skill applicability conditions, and DreamCoder is the ancestor where the criterion is mechanical instead.
- [Spec mining as codification](../../../../notes/spec-mining-as-codification.md) — **evidence**: the fully automated form of the same move — observe a working solver, extract recurring structure from its traces, commit it to a symbolic artifact, grow the surface monotonically — with the human judgment replaced by a compression gate.
- [Codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — **evidence**: a system that keeps both sides of the boundary live by construction — the learned language is the codified part, the neural recognition model the general learner — and that grows the codified surface continuously rather than committing once and relaxing later.
- [Only explicit retention is durable, writable, and addressable](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) — **evidence**: the system splits its retention across exactly the two channels the note contrasts. The abstraction library is explicit, readable, and transferable across domains; the recognition network carries retained search competence that nothing can read.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) — **evidence**: a clean computational-closure endpoint — no human in the improvement loop — whose methodology (what counts as a good abstraction) is fixed by its authors and never revised by the system. The two properties come apart in one artifact.
- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — **evidence**: the same architecture at a different gate strength — both computationally autonomous self-modifiers, one accepting on proof of improvement, the other on measured description-length reduction. The pair makes gate strength, not autonomy, the discriminating variable.
- [Short composable notes maximize combinatorial discovery](../../../../notes/short-composable-notes-maximize-combinatorial-discovery.md) — **evidence**: the formal-domain demonstration of the artifact-shape argument — small reusable abstractions compose into higher-level ones, and the paper reports hierarchical depth growing with experience rather than a flat set of larger units.
- [Minimum viable vocabulary is the naming set that most reduces extraction cost](../../../../notes/minimum-viable-vocabulary-is-the-naming-set-that-most-reduces.md) — **evidence**: DreamCoder's compression objective is a computable instance of that selection criterion — choose the naming set that most reduces the cost of expressing a corpus — with the observer replaced by an enumerative search.
- [Symbolic context engineering is bounded by symbol availability](../../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) — **evidence**: answers the supply side of the bound. The note's third route (earlier semantic work compiling relevance into symbolic metadata that later selection keys on) here runs as an automated loop that manufactures new symbols from experience.

**Notes/definitions — `defined-in`**

- [Self-improving system](../../../../notes/definitions/self-improving-system.md) — **defined-in**: the membership category any placement claim in the ingest must be read against.
- [Representational form](../../../../notes/definitions/representational-form.md) — **defined-in**: the prose / symbolic / distributed-parametric axis the library-versus-network split is stated on.
- [Discovery lifecycle](../../../../notes/definitions/discovery-lifecycle.md) — **defined-in**: the staged vocabulary needed to say precisely which stages DreamCoder automates (conjecture, test, accept, integrate) and which its task designers supply.

**Sources — `compares-with`**

- [Self-revising discovery systems](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) — **compares-with**: the tightest structural match in the KB. That framework defines discovery as a *gated regime transition* that extends the admissible type schema, committed under MDL/AIC gates; DreamCoder's library growth is that operation implemented and run at scale a decade earlier, without the categorical apparatus.
- [SuperARC](../../../../sources/superarc-ait-benchmark-llm-compression-abstraction.ingest.md) — **compares-with**: same compression-as-abstraction thesis from the measurement side. SuperARC shows frontier LLMs failing to compress; DreamCoder is a system that makes compression the training objective and gets hierarchical abstraction out.
- [Schmidhuber, Gödel Machines](../../../../sources/goedel-machines-schmidhuber.ingest.md) — **compares-with**: parallel self-modifying architectures separated by acceptance criterion — provable improvement versus measured compression.
- [Knowledge-Centric Self-Improvement](../../../../sources/knowledge-centric-self-improvement-2607.19592.ingest.md) — **compares-with**: the LLM-era analogue of the growing library — disposable agents around a curated shared artifact store, cumulative across generations, with benchmark oracles standing in for the compression gate.
- [SkillRL](../../../../sources/skillrl-evolving-agents-recursive-skill-augmented-rl.ingest.md) — **compares-with**: recursive skill-library growth from experience with an RL signal instead of a description-length criterion; the closest LLM-era descendant of the wake/sleep split.
- [Self-improving algorithms (Ailon et al.)](../../../../sources/self-improving-algorithms.ingest.md) — **compares-with**: another retain-an-artifact-from-experience loop with a formal optimality target (entropy-optimal limiting performance), which is the same shape of claim as description-length-optimal library growth.
- [DiscoverPhysics](../../../../sources/discoverphysics-benchmarking-llms-out-of-the-box-scientific.ingest.md) — **compares-with**: directly relevant to the Newton/Coulomb rediscovery claim — DiscoverPhysics authors counterfactual physics worlds precisely to defeat recall, which is the control DreamCoder's rediscovery result lacks.
- [EsoLangBench](../../../../sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric.ingest.md) — **compares-with**: its snapshot's bibliography already cites Ellis et al. 2021 as the inductive-program-synthesis-with-learned-library precedent; the ingest can close that reference now that the snapshot exists in-KB.

**Agent-memory-systems — `compares-with`**

- [VOYAGER review](../../../../agent-memory-systems/reviews/voyager.md) — **compares-with**: the closest system analogue — an executable skill library grown from experience with retrieval over it. The instructive difference is the gate: VOYAGER admits a skill when the task succeeds; DreamCoder admits an abstraction when it shortens the corpus.
- [SkillX review](../../../../agent-memory-systems/reviews/SkillX.md) — **compares-with**: trajectory-derived skill libraries with explicit filtering and merging steps; the merge step is DreamCoder's refactoring without a formal compression criterion behind it.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) — **compares-with**: the cross-system survey of exactly this operation (turning traces into reusable retained units); DreamCoder is the pre-LLM reference point its open question about explanatory-reach-versus-local-patch can be read against.

## Bidirectional Candidates

None. The source is an immutable snapshot and authors no links, so there is no outbound edge for a target to return. Inbound edges are enumerated under `Reverse-edge Candidates`.

## Reverse-edge Candidates

This is the load-bearing section for a snapshot. Each is a link the *target* should author under its own collection contract; nothing has been added to any of them.

- [Self-improving systems tag README](../../../../tags/self-improving-systems-README.md) → source — its "Example placements" list currently runs Homeostat / parametric self-improvers / Gödel machine / KCSI / Commonplace. DreamCoder fills the missing slot: computationally autonomous, cumulative, statistically gated, reflective over one form only.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source — **evidence**: a third boundary case alongside Ashby and the Gödel machine, and the one that shows a non-proof gate can still be genuinely reject-capable.
- [A self-improving system needs a profile, not a ladder](../../../notes/a-self-improving-system-needs-a-profile-not-a-ladder.md) → source — **evidence**: an external system whose profile is mixed across the four dimensions, strengthening the case against a ladder.
- [Reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md) → source — **evidence**: an external instance of the graded-coverage claim, so the note stops resting only on Commonplace's own case.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) → source — **evidence** for the parenthetical scope carve-out, which currently has no cited example.
- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) → source — **evidence**: a reinvention-benchmark instance predating the benchmark literature, useful because the rediscovery claim is made by the system's authors rather than by benchmark designers.
- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) → source — **evidence**: the formal-domain case where a mechanical criterion replaces boundary-statability, which sharpens the note's scope paragraph.
- [Spec mining as codification](../../../../notes/spec-mining-as-codification.md) → source — **abstracted-from** or **evidence**: the automated limit of the spec-mining move.
- [VOYAGER review](../../../../agent-memory-systems/reviews/voyager.md) → source — under `kb/agent-memory-systems/` rules, a precursor reference for the executable-skill-library pattern.
- [EsoLangBench ingest](../../../../sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric.ingest.md) → source — **compares-with**: its snapshot already cites Ellis et al. 2021; the ingest can now point at the in-KB snapshot instead of an uncaptured citation.

## Off-authorisation Candidates

- [Commonplace as a reflective system](../../../../notes/evidence/commonplace-as-a-reflective-system.md) — passes the articulation test: that document classifies Commonplace as modification-grade over prose and symbolic artifacts and selection-grade over the parametric form, and DreamCoder is the sharpest external contrast (a system with the same split but with the symbolic side authored by machine). No label fits: `evidence` / `abstracted-from` / `rationale` are authorised for `notes` only, and `compares-with` is authorised for sources, agent-memory-systems, and agentic-systems but not `reference`. `see-also` would technically apply ("any") but its reader-need is "adjacent companion", which misdescribes a contrast case, and the contract says use it sparingly. **Suggestion:** either extend `compares-with` to `reference` in `kb/sources/COLLECTION.md`, or reject and let the comparison live in the notes-side edge to [reflective coverage is graded across representational forms](../../../../notes/reflective-coverage-is-graded-across-representational-forms.md), which already links the reference document.

## Raw Text Candidates

None. Every candidate above carries frontmatter.

## Rejected Candidates

- [Codification](../../../../notes/definitions/codification.md) — near-miss, rejected as a direct edge. The definition is explicit that codification is the crossing *from natural language* into a symbolic artifact; DreamCoder's abstraction step is symbolic→symbolic (programs → language primitives) and never leaves the formal medium. Citing it as an instance would misuse the term in exactly one of the ways the definition's "Misuse Cases" section warns about. The relationship belongs on [spec-mining-as-codification](../../../../notes/spec-mining-as-codification.md) and the bitter-lesson note instead.
- [Unified calling conventions enable bidirectional refactoring](../../../../notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — surfaced by the DSL and neural/symbolic searches. Rejected: its claim is about a *calling convention* that lets a component be swapped between neural and symbolic implementations. DreamCoder does not refactor across that boundary; it runs both permanently in different roles. Surface match only.
- [Improving an agentic system crosses the prose-symbolic boundary](../../../notes/improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — rejected for the same reason as the codification definition: DreamCoder never crosses the prose boundary. It would be a contrast, and no authorised label for `notes` expresses contrast (`evidence` / `abstracted-from` / `rationale` all assert support).
- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) — rejected as too general to help traversal. Accumulation-with-explanatory-reach describes DreamCoder, but it describes most of this cluster; a reader following the link learns nothing specific to this source.
- [Reverse compression is when LLM output expands without adding information](../../../../notes/reverse-compression-is-when-llm-output-expands-without-adding.md) — surfaced by the "compress" title filter. Rejected: the note is about LLM prose output volume; the shared word is not a shared mechanism. (The genuine compression tie is via SuperARC, kept above.)
- [A functioning knowledge base needs a workshop layer, not just a library](../../../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — keyword-only hit on "library", unrelated sense.
- ABC / ADR 015 / thalo DSL hits from the `\bDSL\b` sweep — all use DSL to mean an authored configuration language, not a learned vocabulary. No mechanism in common.
- `kb/agentic-systems/` as a whole — destination skipped, not a rejected candidate: DreamCoder is not an agent harness and matches no trigger there.

## Index Membership

- [Self-improving systems tag README](../../../../tags/self-improving-systems-README.md) — "Example placements" section. A future writer would add a one-line placement: proposal-selection, computationally autonomous, cumulative, non-proof statistical gate, reflective coverage confined to the symbolic library. This is the single highest-value edit the report suggests.
- [Discovery tag README](../../../../tags/discovery-README.md) — carries `complete: true` over notes, so the source cannot be added there directly; the entry point would be a note under "The operation" or "Conditions for discovery" that cites the source.
- Not `kb/agent-memory-systems/README.md` — DreamCoder is not an agent memory implementation; the comparison belongs inside the VOYAGER and SkillX reviews, not in that index.

## Synthesis Opportunities

- **Compression substitutes for boundary-statability where the domain is formal — and that substitution is what does not transfer.** [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) argues natural-language synthesis has no cheap oracle and explicitly exempts formal domains; [abstract an experience only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) argues the abstraction gate is a statable condition clause. DreamCoder plus [self-revising discovery systems](../../../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) (MDL gates) supply two systems where description length *is* the gate. Together they imply a claim the KB has not stated: description-length reduction is a computable proxy for boundary-statability that exists only where the artifact has formal semantics, which is precisely why prose knowledge bases cannot borrow it. Not created here.
- **Gate strength, not autonomy, discriminates the library-growth family.** The Homeostat, Gödel machines, DreamCoder, VOYAGER, SkillRL, SkillX, and KCSI all grow a retained artifact from experience and are all computationally autonomous; they differ almost entirely in what may reject a candidate (nothing / proof / description length / task success / LLM judgment). The existing notes treat these one at a time. A note owning the family with the gate as its ordering variable would be a genuine synthesis. Not created here.

## Maintenance Observations

- **Unnamed recurring pattern.** "Grow an explicit reusable library of abstractions from experience" appears across at least seven artifacts (VOYAGER, SkillX, SkillRL, KCSI, self-revising discovery systems, SkillOpt, and now DreamCoder) with no note owning the abstraction. Each artifact re-describes the pattern locally. This is the promotion candidate behind the second synthesis opportunity above.
- **Capture-fidelity pattern for `genre: scientific-paper` snapshots.** `capture: web-fetch` against an arXiv `/abs/` URL yields the landing page — title, authors, abstract, links — not the paper. The resulting snapshot cannot support any claim about method or results, yet its `description` frontmatter asserts mechanism ("wake-sleep ... alongside neural search guidance"). Worth checking whether other `web-fetch` arXiv snapshots have the same abstract-only/description-overreach mismatch, and whether the snapshot workflow should prefer the PDF path for arXiv.
- **Pre-existing uncaptured citation.** `kb/sources/esolang-bench-evaluating-genuine-reasoning-via-esoteric-programming.md` cites Ellis et al. 2021 in its bibliography, and its ingest report does not mention it. The KB has been referencing this paper indirectly; the snapshot now makes the reference resolvable.

## Flags

- **Evidence-strength flag (most important).** The snapshot is abstract-only. Every mechanism-level candidate above is justified by reasoning the *captured text does not contain*. Before authoring any `evidence` edge, the ingest author must read the PDF and confirm: that the abstraction gate is a description-length/compression criterion; that the recognition model is an amortized inference network rather than something inspectable; that library depth is reported to grow with experience; and what exactly the "rediscovers Newton's and Coulomb's laws" experiment supplied as primitives. If the PDF is not read, downgrade the candidates to `see-also` or leave them unauthored.
- **Split candidate.** The source meets both thresholds — well over five notes across three distinct areas (self-improving-systems, discovery/oracles, constraining/codification) — and makes more than one independent assertion (a learning architecture; a compression-based abstraction criterion; a rediscovery result). A future ingest should expect to cite it from separate notes rather than one, and the rediscovery claim in particular should be handled independently of the architecture claim, since it carries a much weaker evidential warrant.
- **Unresolved tension, not resolved here.** [Abstract an experience only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) makes boundary-statability the abstraction criterion; DreamCoder abstracts without any statable boundary and reports transfer anyway. Either the criterion is domain-scoped (formal semantics let compression stand in) or the compression gate implicitly encodes a boundary. Flagged, not settled.
- **No authored surface exists.** There is no `dreamcoder-wake-sleep-bayesian-program-learning.ingest.md`. Until one is written, none of the `Connections Found` candidates has anywhere to be authored, and the reverse-edge candidates are the only actionable output of this report.
