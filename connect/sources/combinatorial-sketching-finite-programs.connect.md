---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/combinatorial-sketching-finite-programs.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Combinatorial Sketching for Finite Programs

**Source:** [Combinatorial Sketching for Finite Programs](../../../../sources/.snapshots/combinatorial-sketching-finite-programs.md)

The source is an immutable snapshot (Solar-Lezama et al., ASPLOS'06). No `combinatorial-sketching-finite-programs.ingest.md` existed at report time, so every outbound candidate below is for the future ingest report. The sources `COLLECTION.md` forbids durable links to `.snapshots/`, so the ingest, not the snapshot, is the link target for the reverse-edge candidates.

Source claims used for judging: (1) a sketch is a partial program with holes (`??`) plus a separate specification; the synthesizer fills the holes. (2) Combinatorial synthesis relies on a verifier that "filters out" incorrect completions, so it can enumerate every completion rather than only those derivable by hand-written domain rewrite rules (StreamBit's transformational synthesis). (3) The result is complete for finite programs: it completes any sketch, or shows the sketch is "buggy" (no completion exists). (4) Synthesis is 2QBF (`∃c ∀x P(x)=S(x,c)`), solved by a counterexample-driven loop of two SAT solvers, and each counterexample input is added to the synthesizer's constraint set. On real problems the loop terminates after a few SAT instances. (5) The motivation is programmability: StreamBit's rule-level sketches were so hard to write that only one author could write non-trivial ones.

## Discovery Trace

**Setup:**
- `kb/sources/COLLECTION.md` outbound section read. Destinations: notes, reference, sources, agent-memory-systems, agentic-systems, external. Excluded: `kb/work/`, `kb/instructions/`. Labels: `derived-from` (external), `is-evidence-for` (notes, agent-memory-systems), `abstracted-from` (notes), `rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), `see-also` (all, sparingly). The snapshot is never the link author, so all edges are for the ingest.
- External: the only already-known external target is the snapshot's own `source` URL (`https://people.csail.mit.edu/asolar/papers/asplos06-final.pdf`). The ingest's `derived-from` to it is standard; no open-web prospecting was done.

**Description listing scan / titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (444 titles), filtered with `rg -i "verif|oracle|search|spec|synthes|degree|freedom|skeleton|scaffold|generat|constrain|codif|symbolic|solver|hole|partial|template|bitter|domain knowledge|rule|test|falsif|counterex|decid|order"`. Flagged: the-boundary-of-automation-is-the-boundary-of-verification, warranted-autonomy-is-bounded-by-oracle-domain, oracle-strength-spectrum, oracle-accumulation-improves-the-selection-environment, false-positive-generation-is-filtered-before-retention, unformalized-improvements-need-a-pre-formal-stage-in-the-loop, the-bitter-lesson-selects-production-methods-not-representational, solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking, specification-strategy-should-follow-where-understanding-lives, frontloading-is-partial-evaluation-not-divide-and-conquer, specification-level-separation-recovers-scoping-before-it-recovers, a-proposal-selection-loop-requires-search-evaluation-and-retention, automated-synthesis-is-missing-good-oracles.
- `rg -N '^description:'` on 25 flagged notes to judge the claims. `automated-synthesis-is-missing-good-oracles` concerns KB note synthesis (cross-note insight), not program synthesis; it was dropped as a word-sense match.
- `ls kb/sources | grep -i -E "solar|sketch|synth|cegis|bacchus|csp|sat|program"` found sibling source ingests: chaff-engineering-an-efficient-sat-solver, bacchus-van-run-dynamic-variable-ordering-csps, program-synthesis-gulwani-polozov-singh-2017, dreamcoder-wake-sleep-bayesian-program-learning, mathematical-discoveries-program-search-large-language-models (FunSearch).

**Topic indexes:**
- The snapshot has no `tags:`, so no tag-README was prospected by tag. `rg -l "oracle-strength-spectrum|warranted-autonomy" kb/notes/*README.md` shows the oracle notes are curated under `self-improving-systems-README.md` and `llm-reliability-README.md`. These are index heads for notes, not membership targets for a source ingest.

**Body search:**
- `rg -n -i "sketch|partial program|\bholes?\b|counterexample|synthesi[sz]e-verify|generate-and-test|generate and test|SAT solver|program synthesis|synthesizer" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems`: no existing KB artifact discusses Sketch or CEGIS. Hits were claim-counterexample vocabulary (ADR 066, generality/narrowing notes), which is a different sense. Other hits: `specification-level-separation...` ("judgment holes are marked"), `task-families-and-product-families...` (cites the Gulwani ingest), `program-theory-sustains-search...` ("generate and test").
- `rg -l -i "solar-lezama|\bsketching\b|CEGIS|counterexample-guided" kb` matched only the DreamCoder ingest (Solar-Lezama is a coauthor) and an unrelated LRM ingest.
- `rg -n -i "sketch|CEGIS" kb/sources/.snapshots/program-synthesis-gulwani-polozov-singh-2017.md` matched 68 lines. The survey credits Sketch with pioneering partial-program sketches and with inventing counterexample-guided inductive synthesis (CEGIS), and describes CEGIS as an outer loop used across frameworks.
- `rg -l -i "program synthesis|SAT solver|verifier-guided|synthesi[sz]er" kb/agent-memory-systems kb/agentic-systems` matched agent-r, SkillWeaver, wuphf, and Pratiyush--llm-wiki. SkillWeaver line 70 ("feeds violations back to the synthesizer before accepting code") is the only CEGIS-shaped mechanism. `rg -l -i "counterexample|verifier-in-the-loop|synthesize-verify|formal verif" kb/agentic-systems` returned nothing.

**Link following:**
- The FunSearch ingest links to the-bitter-lesson-selects-production-methods..., a-proposal-selection-loop..., learning-inside-a-fixed-decomposition-inherits-its-mistakes, and verifiability-gradient. It frames the human-fixed skeleton and evaluator as outside the update space. That led to learning-inside-a-fixed-decomposition, which matches SKETCH's "buggy sketch" outcome.
- The Gulwani ingest links to warranted-autonomy-is-bounded-by-oracle-domain through its separation of oracle kinds, which confirms that candidate.
- unformalized-improvements-need-a-pre-formal-stage-in-the-loop, opening section: "Choosing among such candidates by counterexample is revision after formal representation … the pre-formal work was done by whoever designed the language rich enough to contain the answer." This describes the sketch/CEGIS division of labour.
- oracle-accumulation-improves-the-selection-environment was read in full to check whether CEGIS's counterexample set fits its "retained check" channel (see Flags for the nuance).
- the-boundary-of-automation-is-the-boundary-of-verification was read through "The practical implication". It has no program-synthesis evidence, and the paper's verifier-as-filter design is a direct instance of its claim.

## Connections Found

All edges are candidates for the future `kb/sources/combinatorial-sketching-finite-programs.ingest.md`.

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- **is-evidence-for**: SKETCH is a clean mechanistic case. The paper says the verifier "filters out" incorrect implementations, "which allows the synthesizer to enumerate all possible candidate implementations". An exact, cheap-enough equivalence check (2QBF over finite inputs) is what turns code writing inside the hole space into automation. The note currently has no program-synthesis evidence.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: the completeness guarantee is scoped exactly to the oracle's domain. It holds for finite programs (bounded input, bounded operations), where equivalence to the specification is decidable. Loops that exceed the unrolling bound surface as assertion failures rather than silent acceptance.
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) -- **is-evidence-for**: SKETCH splits the work as the note describes. The programmer's sketch fixes the admitted candidate space at design time, and the solver chooses among completions by counterexample. "Complete" means complete relative to that human-chosen hole space. A sketch whose space lacks the answer is reported as buggy, not repaired.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **is-evidence-for**: the synthesizer can only assign hole values. When the sketch's structure is wrong, the best output is a proof of no completion. Restructuring stays with the programmer. This is a formal, fully decidable instance of the note's update-space boundary. Scope caveat: SKETCH is search, not learning across runs, so this supports the update-space limit, not a claim about retained learning.
- [Oracle accumulation improves selection for later candidates in its maintained domain](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- **is-evidence-for**: inside one synthesis run, CEGIS keeps every counterexample input and constrains every later candidate with it. Cheap specialized clauses therefore pre-filter candidates before the expensive full verifier runs, and the paper reports termination after only a few SAT instances. Scope caveat: this is within-run accumulation over an exact oracle, not a maintained check across later tasks. See Flags.
- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: the paper replaces hand-written, incomplete domain rewrite rules (StreamBit's transformational synthesis) with general verifier-backed search. That gains completeness and programmability while the product stays symbolic code. It is bounded existence evidence that the hand-crafted-to-search move applies to symbolic artifacts. It is search without cross-task learning, and the human-authored sketch structure remains.
- [FunSearch ingest](../../../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md) -- **compares-with**: on the axis of a human-authored program skeleton that delimits machine search over holes. SKETCH fills constant-valued holes by exact 2QBF equivalence against a reference specification. FunSearch evolves one function body with an LLM proposer under a graded score. Together they bracket the evaluator end (exact equivalence vs. graded score) under the same fixed-skeleton design.
- [Program synthesis (Gulwani, Polozov, Singh 2017) ingest](../../../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) -- **see-also**: the survey credits this paper with sketching and the invention of CEGIS, and places it among constraint-based methods. The primary paper and the survey are companion reading for anyone citing either one for synthesis-as-search.

## Bidirectional Candidates

- [Program synthesis (Gulwani, Polozov, Singh 2017) ingest](../../../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) <-> source -- **see-also**: the survey's ingest currently has no link to Sketch or CEGIS despite 68 snapshot lines on them. A return link from the survey ingest to this primary source would let a reader go from the map to the originating mechanism.
- [FunSearch ingest](../../../../sources/mathematical-discoveries-program-search-large-language-models.ingest.md) <-> source -- **compares-with**: FunSearch's ingest stresses that the skeleton and evaluator are fixed outside the update space. This paper is the decidable, exact-oracle version of that design, so the comparison helps from either side.

## Reverse-edge Candidates

- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → this source's ingest -- **evidence**: the note's evidence section lists oracle theory, Bainbridge, Tam, Amodei, and in-toto. Program synthesis with an exact verifier is a sixth, independent, pre-LLM path to the same structural claim, and the ingest (not the snapshot) would be the citation.
- [Improvements outside the admitted formal language need a pre-formal stage somewhere](../../../../notes/unformalized-improvements-need-a-pre-formal-stage-in-the-loop.md) → this source's ingest -- **evidence**: the note's "chosen among candidates by counterexample" example uses automata learning and model grammars. CEGIS over a sketch is the canonical program-synthesis case and could be cited alongside them.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- SKETCH sits at the hard-oracle end. That placement is already carried by the boundary-of-automation and warranted-autonomy candidates, and a third oracle-theory edge would be a spray.
- [False-positive generation is filtered; false-positive acceptance becomes operative](../../../../notes/false-positive-generation-is-filtered-before-retention.md) -- the verifier-filters-generation point is true of SKETCH but repeats the boundary-of-automation candidate. The paper says nothing about the acceptance side.
- [A proposal-selection improvement loop requires search, evaluation, and retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- SKETCH has search and evaluation but no operative retention across tasks. The loop's defining third element is missing.
- [Solve low-degree-of-freedom subproblems first](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- the sibling solver sources (Chaff, Bacchus & van Run) land here, but this paper makes no ordering or most-constrained-first claim. "Increasing ranges of holes" is a scalability tactic, not DOF ordering.
- [Frontloading is partial evaluation, not divide-and-conquer](../../../../notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md) -- keyword match only. SKETCH uses a partial evaluator to define hole semantics, but the note's claim concerns instruction and data sharing one token medium, which the paper does not bear on.
- [Specification-level separation recovers scoping before error correction](../../../../notes/specification-level-separation-recovers-scoping-before-it-recovers.md) -- "judgment holes" there are LLM-interpreted at runtime. SKETCH holes are constants resolved before execution by exact search. The shared word "hole" hides a different mechanism, and a link would mislead.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) -- SKETCH assumes a complete executable spec already exists (a reference implementation). The paper does not address when a spec-first strategy fits, so it adds nothing to the phase distinction.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- "synthesis" there means cross-note insight generation in a KB, not program synthesis. Linking would conflate the two senses.
- [DreamCoder ingest](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) -- the shared author (Solar-Lezama) and program-synthesis lineage are real, but the only comparison axis (fixed hole grammar vs. learned library) is already covered more directly by the learning-inside-a-fixed-decomposition candidate.
- [Chaff ingest](../../../../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) -- SKETCH uses MiniSAT and ABC as back-ends. SAT-solver internals do not bear on any claim the ingest would make about sketching.
- [SkillWeaver review](../../../../agent-memory-systems/reviews/SkillWeaver.md) -- its "retry synthesis against deterministic shape checks" loop is CEGIS-shaped. It is only an analogy, though: SkillWeaver checks shape, not equivalence to a spec, and the review draws no oracle-completeness conclusion that SKETCH would inform.

## Index Membership

None

## Synthesis Opportunities

None beyond what the reverse-edge candidates name. The paper plus the FunSearch ingest suggest a bounded claim: a human-authored skeleton that fixes the candidate space is what lets an exact or graded evaluator run unsupervised, and the evaluator's strength sets how much of the skeleton may be left open. That claim is currently distributed across warranted-autonomy, learning-inside-a-fixed-decomposition, and unformalized-improvements. It likely belongs folded into one of them rather than as a new note.

## Maintenance Observations

- The Gulwani survey ingest does not mention Sketch or CEGIS, although its snapshot treats them as a central, repeatedly cited method (68 matching lines). If CEGIS becomes load-bearing anywhere in the KB, the survey ingest's analysis has a gap.

## Flags

- **Tension on the oracle-accumulation edge.** In CEGIS, retained counterexamples become constraints on the *synthesizer* (the proposal side), while the verifier stays fixed. The oracle-accumulation note separates the proposal-side "lesson" channel from the selection-side "check" channel. CEGIS fits the note's mechanism (a cheap, exhaustively enforced retained constraint that spares expensive validation), but it blurs the channel distinction. The ingest author should state which reading is intended, or drop the edge.
- **No ingest yet.** All outbound candidates assume the future `combinatorial-sketching-finite-programs.ingest.md`. A concurrent `cp-skill-ingest` run may be writing it. That run's Connections Found section is where these candidates would be authored.
