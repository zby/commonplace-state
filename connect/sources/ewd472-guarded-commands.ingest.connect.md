---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/ewd472-guarded-commands.ingest.md"
source_has_frontmatter: true
date: "2026-11-04"
depth: standard
---

# Connection Report: Ingest: Guarded commands, non-determinacy and formal derivation of programs (EWD 472)

**Source:** [EWD 472 ingest](../../../../sources/ewd472-guarded-commands.ingest.md)

## Discovery Trace

**Contract read:** `kb/sources/COLLECTION.md` "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; excluded: `kb/work/`, `kb/instructions/`. Labels for ingests: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting skipped; the only external target is the already-present `source` URL, correctly labelled `derived-from`.

**Existing links verified (all exist, not repeated below):** symbolic-form-holds-consumers-to-a-semantic-reference, implementations-do-not-establish-shared-semantics, fix-what-the-executor-cant-determine-not-what-it-will, commitment-not-derivation-creates-new-ground-truth, formal-systems-assess-explanatory-reach-through-causal-and-proof, bounded-context-orchestration-model, underspecification-and-indeterminism-complicate-programming-for (theory); agent-behavioral-contracts-formal-specification-runtime, toolgate-contract-grounded-and-verified-tool-execution-for-llms, is-ai-the-next-layer-of-abstraction (sources).

**Description / title listing scan:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "semantic|specif|verif|conform|invariant|loop|select|determin|contract|formal|proof|oracle|underspec|permitted"` -- flagged: traditional-software-can-bracket-executor-conformance-llm-systems, execution-indeterminism-is-a-property-of-the-sampling-process, clear-instructions-can-compose-into-an-unsettled-contract, prompting-changes-failure-diagnosis-with-the-semantic-reference, selecting-an-llm-output-fixes-a-result-not-its-interpretation, specification-strategy-should-follow-where-understanding-lives, verification-needs-a-typed-target-before-it-needs-an-oracle, the-practical-scheduler-is-the-host-language.
- `rg -m1 '^description'` on the flagged set -- kept the first three; rejected the rest (see Rejected).

**Topic indexes:**
- `kb/tags/computational-model-README.md` read (source has no `tags:`; read as the nearest topical head). Its foundations already include the bounded-context model and prompting accounts the ingest links; no new target.
- `kb/tags/llm-reliability-README.md` surfaced by keyword rg only; not followed (the source does not treat LLM reliability).

**Body search:**
- `rg -n -i "nondetermin|non-determin|weakest.precondition|dijkstra|guarded|refinement calculus|demonic|angelic|hoare|permitted (variation|outcome|set)|excluded miracle|predicate transformer|total correctness" kb/theory kb/reference kb/sources kb/agentic-systems kb/tags` (excluding retained-archive and reviews-archive) -- hits: execution-indeterminism line 28 ("a governing reference can specify permitted variation"); definitions/codification and definitions/representational-form (four cases a reference leaves open); clear-instructions lines 38, 46; build-systems-a-la-carte ingest (§8.3 set membership for non-deterministic tasks); toolgate (already linked); cost-sensitive-formalisms (nondeterministic Turing machines; rejected); `kb/reference` hits on "guarded" are all mechanical (guarded captures, guarded merges) -- rejected.
- `rg -n -i "miracle|dijkstra" kb/sources/morgan-the-specification-statement.ingest.md` -- confirms Morgan extends Dijkstra's guarded-command language and admits miracles; Morgan ingest does not currently link EWD 472.
- `rg -n -i "permitted|set membership|non-determin" kb/sources/wg14-n1570-behavior-definitions.ingest.md` -- confirms the "permitted alternatives" framing.
- `rg -n "ewd472|EWD 472|guarded-commands" kb --glob '*.md'` -- no inbound links anywhere yet.
- `rg -l -i "nondetermin|non-determin" kb/agentic-systems/reviews kb/agentic-systems/comparisons` -- only memory-systems-table (incidental); agentic-systems skipped.

**Link following:**
- symbolic-form lines 85-90: the "Permitted variation" case uses "Return either A or B" as its only example and cites no formal source -- the strongest reverse-edge target.
- traditional-software line 23: says V is a singleton for deterministic code but symbolic form "can include declared variation" -- with no classical-program instance.
- Morgan ingest line 43 links clear-instructions on settledness of combined requirements; followed to clear-instructions, which contrasts with guarded-command overlap semantics.
- definitions/codification cites N1570 for the four open cases; followed to the N1570 ingest.

**Destinations skipped:** `kb/reference/` (no system-design claim matches the source; hits were lexical), `kb/agentic-systems/` (no review treats nondeterministic choice semantics), `kb/agent-memory-systems/` (frozen historical; no trigger), `kb/tags/` (no tag head whose inclusion condition the ingest meets as a target).

## Connections Found

- [Morgan, Robinson and Gardiner: On the refinement calculus](../../../../sources/morgan-the-specification-statement.ingest.md) -- **compares-with**: on the Law of the Excluded Miracle. EWD 472 imposes `wp(S, F) = F` as a well-formedness condition on every statement; Morgan's specification statement extends the same guarded-command language and deliberately admits miracles (`[true, false]`), replacing the law with a checkable feasibility condition. The pair shows what a calculus gains and must police when a specification may denote an empty permitted set. Sibling ingest from the same occasion; currently neither links the other.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) -- **is-evidence-for**: the note says the valid set V is a singleton for deterministic code under a one-result reference, but that symbolic form "can include declared variation". EWD 472 is a classical, non-LLM program semantics in which V is a declared non-singleton set and correctness still holds, so it bounds the "plurality assumed away" bracket as a convention of ordinary programming, not of formal semantics.
- [LLM output variation depends on decoding and execution conditions](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- **is-evidence-for**: the note concludes "permitted variation does not by itself prevent defined semantics". EWD 472 is a precise instance: unordered guarded choice with a fully defined wp semantics. It also separates semantic non-determinacy (declared in the program) from execution-condition variation, which is the note's central distinction.
- [Clear instructions can compose into an unsettled contract](../../../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) -- **compares-with**: on overlapping applicable rules. In `if ... fi`, overlapping true guards need no precedence because wp requires every eligible branch to establish the postcondition; the note's JSON-only rule and exception rule become unsettled precisely because overlap is resolved by unstated scope and precedence. The contrast names what a contract must declare for overlap to be harmless.
- [WG14 N1570 behavior definitions](../../../../sources/wg14-n1570-behavior-definitions.ingest.md) -- **compares-with**: on how a reference states permitted alternatives. N1570's unspecified behavior lists alternatives in prose with no correctness obligation across them; EWD 472's wp quantifies demonically over the alternatives so every one must satisfy the postcondition. Both are the KB's formal anchors for "permitted variation" (N1570 already anchors the codification definition).
- [Representational form](../../../../theory/definitions/representational-form.md) -- **defined-in**: the ingest's Connections Found and Extractable Value rely on "permitted variation" as a technical term; this definition lists it as one of the four things a symbolic reference can leave open (with required external selection, excluded guarantee, defect). A reader of the ingest may not know the term's boundaries.

## Bidirectional Candidates

- [Morgan refinement calculus ingest](../../../../sources/morgan-the-specification-statement.ingest.md) <-> source -- **compares-with**: Morgan builds directly on Dijkstra's guarded commands; its ingest should link back to EWD 472 as the base language whose excluded-miracle law it relaxes.
- [WG14 N1570 behavior definitions](../../../../sources/wg14-n1570-behavior-definitions.ingest.md) <-> source -- **compares-with**: return path useful for a reader of N1570's permitted alternatives who needs the case where alternatives carry a correctness obligation.

## Reverse-edge Candidates

- [Symbolic form holds consumers to a semantic reference](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) → source -- **evidenced-by** (theory COLLECTION label, destination sources): at the "Permitted variation" case (line ~87), whose only example is "Return either A or B". Matches the ingest's Recommended Next Action; needs retained quotes first (Quotes section is empty). Check the note's five-tracked-source grounding budget (ADR 082) before adding.
- [Traditional software can bracket executor conformance; LLM systems cannot](../../../../theory/traditional-software-can-bracket-executor-conformance-llm-systems.md) → source -- **evidenced-by**: at line 23, as the classical instance of declared variation in symbolic form.
- [LLM output variation depends on decoding and execution conditions](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) → source -- **evidenced-by**: at "permitted variation does not by itself prevent defined semantics".
- [Codification](../../../../theory/definitions/codification.md) → source -- **evidenced-by**: optional second instance beside N1570 for "permitted variation"; lower priority, since the definition already has one anchor.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Prompting changes failure diagnosis with the semantic reference](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md) -- relevant through the symbolic-form note it grounds; a direct link adds nothing beyond the already-linked symbolic-form and underspecification notes.
- [Selecting an LLM output fixes a result, not its interpretation](../../../../theory/selecting-an-llm-output-fixes-a-result-not-its-interpretation.md) -- selection of one output for reuse is not wp choice; keyword overlap on "select".
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- spec-first vs spec-mining phases; EWD 472's derivation method is spec-first but the note's axis is durable-artifact phase, not semantics.
- [Verification needs a typed target before it needs an oracle](../../../../theory/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- different axis (artifact classification).
- [The practical scheduler is the host language](../../../../theory/the-practical-scheduler-is-the-host-language.md) -- the `do`-loop analogy is already carried by the bounded-context-orchestration-model link.
- [Build Systems à la Carte: theory and practice](../../../../sources/build-systems-a-la-carte-theory-and-practice.ingest.md) -- §8.3 set-membership correctness for non-deterministic tasks is a genuine parallel, but it concerns rebuild correctness, not specification semantics; would be a weak compares-with. Keep as a possible later link if a note on set-membership conformance is written.
- [Cost-sensitive formalisms for tentative theory search](../../../../theory/cost-sensitive-formalisms-for-tentative-theory-search.md) -- nondeterministic Turing machines are a complexity notion, not choice semantics.
- `kb/reference/` hits on "guarded" (ADR 051, 106, storage-architecture) -- lexical only.

## Index Membership

- [Computational model tag](../../../../tags/computational-model-README.md) -- sources are outside participating collections; no index change. A source-scoped `tags: [computational-model]` on the ingest is plausible only if the head's inclusion condition (instruction interpretation, scoping, state, orchestration of bounded LLM calls) is read as covering formal choice semantics; it likely is not, so `domains` suffice.

## Synthesis Opportunities

EWD 472 (demonic all-branches-correct choice), N1570 (prose-listed alternatives without cross-alternative obligation), Morgan (specifications as programs, miracles admitted), Build Systems à la Carte (set-membership correctness for non-deterministic tasks), ABC (statistical compliance) and ToolGate (ranked selection with postcondition checks) together suggest a spectrum of how a reference quantifies over its permitted set: all members must be correct, any member is conformant, or the chosen member is probably correct. No theory note currently names that quantifier as a design axis for LLM-call contracts.

## Maintenance Observations

- The two same-day sibling ingests (EWD 472 and Morgan) do not link each other, though Morgan's semantics is defined as an extension of Dijkstra's language.
- The ingest's Quotes section is empty while its Recommended Next Action requires quote-grounded citation from the symbolic-form note; grounding must precede that reverse edge.

## Flags

- Split candidate check: the source links five or more notes across several areas but makes one central assertion (permitted-outcome-set semantics with demonic correctness); not a split candidate.
- Tension: the ingest's claim that "wp correctness must hold for every choice" contrasts with the bounded-context model's treatment of `select` as a policy; already flagged in the ingest, not resolved here.
