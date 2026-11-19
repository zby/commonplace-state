---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/combinatorial-sketching-finite-programs.ingest.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: Ingest: Combinatorial Sketching for Finite Programs

**Source:** [Ingest: Combinatorial Sketching for Finite Programs](../../../../sources/combinatorial-sketching-finite-programs.ingest.md)

The ingest already carries eight footer edges (external paper, five notes, two sources), and all of their targets exist. This report adds candidates that the ingest does not yet link. The strongest is the note that already cites this ingest for the ingest's own occasion.

## Discovery Trace

**Authorisation read:** `kb/sources/COLLECTION.md` § Outbound links. Destinations to prospect: notes, reference, agent-memory-systems, agentic-systems, sources. Excluded: work, instructions. Labels: `is-evidence-for` (notes, agent-memory-systems), `abstracted-from`/`rests-on` (notes), `compares-with` (notes, sources, agent-memory-systems, agentic-systems), `defined-in` (notes/definitions), `see-also` (notes, reference, sources, agent-memory-systems, agentic-systems, external). External prospecting was skipped. The only external target is the original paper, which the ingest already links as `derived-from`.

**Inbound check:**
- `rg -l "combinatorial-sketching-finite-programs" kb --glob '*.md'`: one citer, `kb/notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md`, with an inline section and an `evidenced-by` footer. The ingest does not link back.

**Body search (all destinations):**
- `rg -l -i "counterexample|CEGIS|sketch(ing)? |program synthesis|synthesi[sz]e-verify" kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources`: about 90 files. Flagged: narrowing-bought-to-survive-review, generality-bought-to-avoid-counterexamples, a-proposal-selection-loop-requires-search-evaluation-and-retention, automated-synthesis-is-missing-good-oracles, claim-modality-is-the-inference-form-of-the-refuter, ADR 066, ADR 080, proposals repair-dispositions-for-defeated-claims and gate-learning-from-accepted-edits, error-correction-works-above-chance-oracles, spec-mining-as-codification, and the ingests for agentic automata learning, scaffold-not-vocabulary, AlphaDev, and DreamCoder. Most other hits use "synthesis" in the writing sense or "counterexample" in the ordinary sense.
- `rg -l -i "drift|weaken|empty claim|hollow|vacuous" kb/notes`: this query targets the occasion (review/revise drift toward empty claims). Flagged: an-omitted-loop-function-and-a-frozen-one-need-different-repairs, generality-bought, claim-modality, oracle-accumulation (already linked).
- `rg -n -i "frozen|sketch|FunSearch|AlphaEvolve"` over the omitted/frozen note: it defines "frozen" as outside the loop's update space, and says that a frozen acceptance rule "may therefore be the warranted kernel rather than the defect".
- `rg -n -i "cannot change the claim|keep.*claim|write scope"` over ADR 080: "The pass never changes a title, thesis, or title-as-claim." Claim-changing findings become a pending `revise` hand-back.
- `rg -n -i "sketch|CEGIS|counterexample|SAT solver"` over the Chaff, Bacchus, Gulwani, automata-learning, scaffold-not-vocabulary, and AlphaDev ingests: the automata-learning ingest has equivalence queries that return counterexamples. The scaffold-not-vocabulary ingest discourages ad hoc rescue and leaves counterexample generation as future work. Chaff and Bacchus deal only with SAT/CSP decision ordering.
- `rg -n -i "counterexample|synthes"` over the agent-memory-systems hits (virtual-context, operational-ontology-framework, fintool): ordinary-sense uses only. Rejected.
- `rg -l -i "verifier|equivalence check|reference implementation" kb/agentic-systems`: apache-maka, ai-agent-book. Neither has a synthesis loop or a fixed-specification design. Rejected.

**Description reads:** narrowing, generality, automated-synthesis-oracles, proposal-selection-loop, repair-dispositions proposal, gate-learning proposal, ADR 080, ADR 066, error-correction, spec-mining, specification-strategy, reliability-dimensions, solve-low-degree-of-freedom, claim-modality, false-positive-generation, omitted/frozen, revising-an-improvement-objective, oracle-strength-spectrum, exact-implementation-does-not-validate-a-requirement, warranted-reader-update.

**Link following:**
- narrowing note → its footer (generality-bought, warranted-reader-update, claim-strength gate) and its inbound citer ADR 080 (`rests-on` narrowing). This shows a chain: SKETCH (exact limit) → narrowing note (mechanism) → ADR 080 (shipped policy: the pass cannot change the claim).
- omitted/frozen note → learning-inside-a-fixed-decomposition (already linked) and revising-an-improvement-objective-is-licensed-from-outside-it. Read the opening of the latter: objective change counts as improvement only against a level outside both objectives.
- oracle-strength-spectrum → exact-implementation-does-not-validate-a-requirement (the exact-spec vs proxy foundation).

## Connections Found

- [Narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) -- **is-evidence-for**: this is the KB note the ingest's occasion targets. It already uses SKETCH as the exact-oracle limit: a verifier checks against a fixed specification, and a failed search ends in "no valid completion" instead of a weaker target. The ingest's Extractable Value items 1–3 bear directly on the note's claim that review/revise loops drift toward analytic emptiness. The ingest does not yet link it.
- [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -- **is-evidence-for**: SKETCH's specification and verifier sit outside the loop's update space, which is the note's sense of "frozen". This is a case where freezing the acceptance function is the warranted kernel, not the defect. The note raises that possibility, but its five-system cohort has no clean exact-oracle instance.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: in SKETCH the SAT synthesizer does the search, the all-inputs verifier does reject-capable evaluation, and the accumulated counterexamples do retention, within one run. The fixed hole space illustrates the note's line "Evaluation cannot select a candidate that search never reaches". A wrong sketch yields a proof that no completion exists, not a better sketch.
- [An exact implementation does not validate a requirement](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **is-evidence-for**: SKETCH guarantees only equivalence to the reference specification over the finite instance checked. For Karatsuba it verifies N = 12 and leaves other sizes to the programmer. Exact local correctness therefore coexists with an unvalidated wider requirement, which is the note's split between the implementation path and the requirement path.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- **is-evidence-for** (weaker): the loop cannot revise its objective (the specification P). Its only in-loop revisions are raising unrolling and hole-range bounds, and an assertion failure licenses each one. That is a change to the search space, not to the objective. The case is a clean formal illustration of the "proxy/search revision vs terminal objective" subtraction. Keep only if the note wants a non-LLM example.
- [Can LLM agents infer world models? Agentic automata learning](../../../../sources/can-llm-agents-infer-world-models-agentic-automata-learning.ingest.md) -- **compares-with**: shared axis of an exact equivalence oracle that returns counterexamples. In L*/agentic automata learning the learner builds a hypothesis from queries and the oracle refutes it. In SKETCH the "learner" is a SAT synthesizer constrained by the accumulated counterexamples. Both are exact-oracle, counterexample-driven loops. The benchmark supplies the LLM-proposer contrast (agents degrade as state count grows), which the FunSearch comparison does not cover.
- [Scaffold, not vocabulary: a Popperian code-generation skill](../../../../sources/scaffold-not-vocabulary-popperian-code-generation-skill.ingest.md) -- **compares-with**: shared axis of how a revise loop is kept from rescuing a candidate by weakening. The Popperian skill relies on an instruction (a description-length rule against ad hoc rescue) and leaves counterexample generation as future work. SKETCH enforces the same guard structurally: the specification is outside the revise step's write scope, and every counterexample is retained.
- [ADR 080: full passes hand claim changes back as a pending revise](../../../../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) -- **see-also**: this is the shipped Commonplace policy that realizes the ingest's Extractable Value items 1 and 3. The pass may not change a note's claim (the specification stays outside the revise step), and a finding that requires a claim change becomes an explicit hand-back (the analogue of "buggy sketch"). The ingest's transfer paragraph would gain a concrete KB target.

## Bidirectional Candidates

- [Narrowing bought to survive review is paid for in content](../../../../notes/narrowing-bought-to-survive-review-is-paid-for-in-content.md) <-> source -- **is-evidence-for** / existing `evidenced-by`: the note already links this ingest. Adding the return edge closes the loop between the ingest's occasion and the note that answered it.

## Reverse-edge Candidates

- [ADR 080](../../../../reference/adr/080-full-passes-hand-claim-changes-back-as-a-pending-revise.md) → source -- **evidenced-by** (authorised reference→sources): SKETCH bounds the ADR's design choice. An exact propose-and-counterexample loop stays honest by keeping the specification unwritable and by treating "no completion" as a reportable outcome. The ADR currently cites only the narrowing note (`rests-on`). The ADR predates the ingest, so this would be a corroborating addition, not the ADR's origin; do not use `derived-from`.
- [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) → source -- **evidenced-by**: a non-LLM, exact-oracle case where the frozen evaluator is plainly warranted. It would counterweight the cohort's unevenly justified frozen gates. Check the note's ADR 082 unquoted-source budget first, since the note already cites several ingests.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) → source -- **evidenced-by**: the ingest links this note as `is-evidence-for` and states that the note has no program-synthesis evidence. The note currently links no `kb/sources/` ingest at all (`rg -n "sources/"` returns nothing), so this would be its first source edge.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Chaff: engineering an efficient SAT solver](../../../../sources/chaff-engineering-an-efficient-sat-solver.ingest.md) and [Bacchus & van Run](../../../../sources/bacchus-van-run-dynamic-variable-ordering-csps.ingest.md) -- SKETCH runs on SAT solvers, but these ingests are about decision ordering. They share no named axis with the ingest's occasion; a link would be substrate-only.
- [Solve low-degree-of-freedom subproblems first](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) -- the pop-count result (fixing shifts and masks collapses solve time) is superficially an ordering result. But it is about the user fixing the candidate space, not about the ordering of commitments. Too weak.
- [Generality bought to avoid counterexamples is paid for in precision](../../../../notes/generality-bought-to-avoid-counterexamples-is-paid-for-in.md) -- the widening escape. SKETCH cannot widen because the hole space is fixed, but the narrowing note already carries this contrast and links generality-bought. A direct link would duplicate one hop.
- [Claim modality is the inference form of the refuter](../../../../notes/claim-modality-is-the-inference-form-of-the-refuter.md) -- gives vacuity a precise reading, but SKETCH has no modality axis. Reached better via the narrowing note.
- [Automated synthesis is missing good oracles](../../../../notes/automated-synthesis-is-missing-good-oracles.md) -- "synthesis" here means cross-note knowledge synthesis. A link would be a keyword collision.
- [Oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- SKETCH sits at the exact-spec end, but the ingest already links boundary-of-automation and warranted-autonomy, which cover this. The more specific foundation, exact-implementation-does-not-validate-a-requirement, was kept instead.
- [Spec mining as codification](../../../../notes/spec-mining-as-codification.md) -- runs in the opposite direction: it extracts a verifier from behaviour, while SKETCH takes a verifier as given. There is no concrete reader gain.
- [Repair dispositions for defeated claims (proposal)](../../../../reference/proposals/repair-dispositions-for-defeated-claims.md) and [ADR 066](../../../../reference/adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md) -- adjacent repair policy, but ADR 080 is the specific artifact that realizes "specification outside the revise step". One reference `see-also` is enough under "use sparingly".
- Agent-memory-systems and agentic-systems hits (virtual-context, fintool, operational-ontology-framework, apache-maka, ai-agent-book) -- ordinary-sense keyword matches with no synthesis-verification loop.

## Index Membership

- [kb/sources/README.md](../../../../sources/README.md) -- curated source navigation. It lists only two ingests, so it is not a per-ingest index. No membership recommended.

## Synthesis Opportunities

The ingest plus the narrowing note, ADR 080, and the omitted/frozen note imply a higher-order claim that none of them states in full. A revise loop keeps repairs honest only if three things hold. Its target sits outside the revise step's write scope (frozen evaluation as a warranted kernel). It has an explicit "cannot be repaired within this target" exit (SKETCH's "buggy sketch", ADR 080's `revise` hand-back). It retains earlier refutations as regression checks. ADR 080 implements the first two; nothing in the KB implements the third (carrying earlier review findings forward as checks on later revisions). Per the fold-claims preference, this may belong as a bounded paragraph in the narrowing note rather than as a new note.

## Maintenance Observations

- The ingest's Recommended Next Action ("add one bounded paragraph citing this ingest" to the fixed-decomposition note "or the KB note that will treat review/revise drift") appears to have been executed. `narrowing-bought-to-survive-review-is-paid-for-in-content.md` now has a "What an exact repair loop holds fixed" section citing this ingest. The next action is stale and could be updated to point at the remaining gap: refutation retention (Extractable Value item 2).
- The ingest has no retained quotes. The narrowing note cites it without a verbatim quote, so it counts toward that note's ADR 082 unquoted-source budget.

## Flags

- Tension to keep visible: the ingest's Limitations section warns that retaining refutations under a soft oracle can lock in errors. Any KB adoption of Extractable Value item 2 (carrying review findings forward as regression checks) should weigh this against [error correction works above chance oracles with decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), where individual verdicts are fallible.
- Not a split candidate: the ingest is a single-source analysis.
