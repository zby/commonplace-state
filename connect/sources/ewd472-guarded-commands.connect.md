---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/ewd472-guarded-commands.md"
source_has_frontmatter: true
date: "2026-11-04"
depth: standard
---

# Connection Report: Guarded commands, non-determinacy and formal derivation of programs (EWD 472)

**Source:** [Guarded commands, non-determinacy and formal derivation of programs (EWD 472)](../../../../sources/.snapshots/ewd472-guarded-commands.md)

The source is an immutable snapshot. No `ewd472-guarded-commands.ingest.md` exists yet. Every outbound candidate below is meant for that future ingest report, which is the authored surface under `kb/sources/COLLECTION.md`. The snapshot itself must never author links, and no durable artifact should link to `.snapshots/`.

Source claims used for judging candidates:
- A guarded command set gives an unordered set of alternatives. The `if` construct aborts when no guard is true; the `do` loop terminates exactly when no guard is true. Selection among the true guards is arbitrary, and the final state may also be undetermined: "only permissible final states are possible and each permissible final state is possible".
- Weakest-precondition semantics: a statement's meaning is its predicate transformer `wp(S, R)`. The `wp` must hold for every permitted selection, so correctness is guaranteed rather than probable.
- Theorems 1–4 give a compositional proof rule: if each guarded list preserves the invariant P and decreases the variant t under its guard, the loop establishes `P and non BB`.
- The paper offers a calculus, not an algorithm. Deriving an alternative construct is "reasonably straightforward", but a loop needs "the invention" of an invariant and a variant function.
- Non-determinacy avoids premature choices. The traditional versions A and B of Euclid's algorithm force a choice that can only be justified by timing assumptions. Removing the non-determinacy later, mechanically or by the programmer, is "left entirely to the circumstances". The non-deterministic program is "a helpful steppingstone".
- The method transferred from operating-system synchronization. There, the state in which all guards are false means deadlock; in a sequential program it means termination.

## Discovery Trace

**Outbound section read:** `kb/sources/COLLECTION.md` § Outbound links. The authorised local destinations are theory, reference, agent-memory-systems, agentic-systems, tags and sources. `kb/work/` and `kb/instructions/` are excluded. `external` is authorised for `derived-from` and `see-also`, but no external target was supplied, so external prospecting was skipped. The labels by destination are:
- theory: `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `see-also`
- theory/definitions: `defined-in`
- sources: `compares-with`, `see-also`
- agentic-systems: `compares-with`, `see-also`
- agent-memory-systems: `is-evidence-for`, `compares-with`, `see-also`
- reference: `see-also`

**Existing-coverage check:**
- `ls kb/sources/ | grep -iE 'ewd|dijkstra|hoare|parnas|simon|liskov|meyer|contract'` found no EWD ingest. Its adjacent hits were the ABC, ToolGate, Parnas and Simon ingests.
- `rg -il 'dijkstra|weakest.precondition|guarded command|hoare' kb --glob '*.md' --glob '!kb/sources/.snapshots/**'` returned only incidental hits:
  - Seemann ingest: mentions Dijkstra
  - ToolGate ingest: mentions "Hoare-style"
  - continual-harness ingest: refers to Dijkstra's shortest-path algorithm, which is a different subject
  - pratiyush runtime analysis
- No theory note cites Dijkstra or wp semantics.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md'` returned 439 titles.
- That listing was filtered with `rg -i 'invariant|precondition|contract|specif|determin|verif|deriv|guard|terminat|composition|decompos|oracle|routine|invent|calcul|formal|correct|program|loop|constrain|underspecif|interpret|semantic'`. About 95 titles matched and were scanned by title.
- Shortlisted titles:
  - fix-what-the-executor-cant-determine
  - underspecification-and-indeterminism
  - symbolic-form
  - implementations-do-not-establish-shared-semantics
  - commitment-not-derivation
  - formal-systems-assess-explanatory-reach
  - progressive-constraining
  - near-decomposability
  - bounded-context-orchestration-model
  - select/call program
  - a-guard-against-a-conjectured-requirement
  - boundary-of-automation
  - oracle-strength-spectrum
  - verification-needs-a-typed-target
  - derivation-and-inheritance

**Description listing scan:**
- `rg -N '^description:'` was run over the 12 shortlisted theory notes. It also covered bounded-context-orchestration-model, select-call-program, statecharts, execution-indeterminism, prompting-changes-failure-diagnosis, warranted-autonomy, codifying-predictable-choices, exact-implementation and implementations-do-not-establish-shared-semantics.
- The same scan covered the ingests for ABC, ToolGate, Parnas, Simon, Seemann and continual-harness.

**Topic indexes:**
- Read `kb/tags/computational-model-README.md`. It is tag-scoped to the interpretation and orchestration of LLM instructions. The Foundations and Scheduling sections pointed to the bounded-context orchestration model and the select/call lemma.
- The tags list was scanned. No tag covers formal program semantics or verification of classical programs.

**Body search:** the hit counts are files across theory, reference, agentic-systems, agent-memory-systems, source ingests and tags.

| Query | Files | What it showed |
|---|---|---|
| `invariant` | 187 | Too broad. A per-file count in theory surfaced formal-systems (8), a-framework-rule-with-a-boundary-preserving-rival (6), agents-md-control-plane (6) and near-decomposability (4). |
| `precondition\|pre-condition\|postcondition` | 63 | Tool and skill contexts. ToolGate and Voyager (agent-memory-systems) were the only Hoare-sense hits. |
| `non-determin\|nondetermin` | 20 | In theory: implementations-do-not-establish-shared-semantics, line 18 ("Nondeterminism can be represented as permitted transitions"). Also commitment-not-derivation, execution-indeterminism, select-call-program and cost-sensitive-formalisms (Turing-machine nondeterminism, a different sense). |
| `weakest` | 49 | Ordinary-English uses. No predicate-transformer use. |
| `predicate transformer\|Hoare` | 1 | ToolGate ingest only. |
| `derivation of programs\|program derivation\|correct by construction\|correct-by-construction` | 0 | No hits. |
| `deadlock` | 0 | No hits. |
| `guard(ed)? ` | 132 | Mostly the protective-rule sense of guard. |
| `routine\|invention\|invent` (theory, `-l`) | 20 files | None uses the routine-versus-invention split for formal derivation. |

`rg -n -i 'invariant'` was also run on near-decomposability, the framework-rule note, agents-md and vocabulary-collisions to check which sense of invariant each uses.

**Candidate reads:**

| Candidate | Read | Result |
|---|---|---|
| formal-systems-assess-explanatory-reach | Full note | Kept |
| fix-what-the-executor-cant-determine | First about 40 lines | Kept |
| underspecification-and-indeterminism | Full note | Kept, with a tension flag |
| symbolic-form | Opening sections | Kept |
| implementations-do-not-establish-shared-semantics | Lines 8–30 | Kept |
| commitment-not-derivation | Opening sections | Kept |
| bounded-context-orchestration-model | Grep for select, guard and choice | Kept |
| ToolGate ingest | Summary and Extractable Value | Kept |
| ABC ingest | Classification and Summary | Kept |
| Seemann ingest | Classification, Summary and Connections | Kept |
| a-guard-against-a-conjectured-requirement | Opening | Rejected |
| near-decomposability | Grep | Rejected |
| progressive-constraining | Description | Rejected |

**Link following:**
- underspecification-and-indeterminism links to prompting-changes-failure-diagnosis, progressive-constraining and llm-debugging-triage. None adds a sharper EWD axis than the note itself.
- symbolic-form links to implementations-do-not-establish-shared-semantics, which confirmed a second semantics-reference candidate.
- The Seemann ingest links to prompting-changes-failure-diagnosis. That target is already covered by the underspecification candidate and was not added separately.
- The ToolGate ingest links to bounded-context-orchestration-model and verification-needs-a-typed-target. This confirmed the orchestration-model candidate.

**Other destinations:**
- reference: `rg -il 'precondition|postcondition|non-determin|nondetermin' kb/reference` returned only proposal and archive documents about pipeline steps. Nothing describes guarded selection or wp semantics. Skipped.
- agentic-systems: the only hit was `beads-rust.md`, line 69, where "non-determin" appears inside a classifier description. It is keyword-only and was rejected.
- agent-memory-systems: `voyager.md` lines 116–126 discuss missing preconditions on learned skills. This is a weak keyword match; see Rejected.
- external: skipped. No supplied or loaded target.

## Connections Found

These are candidate edges for the future `kb/sources/ewd472-guarded-commands.ingest.md`.

**Theory**
- [An author should fix what the executor can't determine, not what it will](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- **compares-with**: The shared axis is leaving a choice open among permitted alternatives. Guards delimit which alternatives are eligible, and the semantics leaves selection among them to execution. Dijkstra also leaves later determinization, for example on efficiency grounds, "entirely to the circumstances". This is a formal precedent for the note's rule that a harmless, bounded choice can stay open when its alternatives are all acceptable.
- [Symbolic form holds consumers to a semantic reference](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) -- **is-evidence-for**: wp semantics is a reference that is fully formal and still permits variation: "only permissible final states are possible and each permissible final state is possible". It is a canonical case of the note's statement that "the reference may leave permitted variation".
- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) -- **compares-with**: The axis is how variation in a specification is represented. Guarded-command non-determinacy is a third case alongside the note's two. It is neither natural-language ambiguity nor sampling noise: a precise semantics declares a set of permitted outcomes, and correctness quantifies over all of them. This sharpens the note's "testing targets" half. See Flags for a tension with one of the note's sentences.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- **compares-with**: The axis is deferring choices the source does not entail. Dijkstra's symmetric Euclid program avoids the version A/B choice, which "can only be justified by making assumptions" about timing. Determinizing later is exactly the kind of unentailed addition the note classifies as commitment, so the non-deterministic program is the derived, commitment-free form.
- [Causal and proof obligations are two formal routes to assessing explanatory-reach](../../../../theory/formal-systems-assess-explanatory-reach-through-causal-and-proof.md) -- **compares-with**: The axis is what a formal calculus mechanizes and what stays upstream judgment. Dijkstra's split between "formal routine" for alternative constructs and "invention" of invariant and variant for loops matches the note's formalization boundary. The calculus checks a chosen invariant but does not supply it.
- [Bounded-context orchestration model](../../../../theory/bounded-context-orchestration-model.md) -- **compares-with**: The axis is a guarded loop that terminates when nothing is eligible. The model's `while (B := select(K)) is not None` loop has the shape of a `do ... od` that ends when no guard holds. The two treat selection differently. wp semantics is independent of the selection policy because correctness must hold for every choice. The orchestration model instead makes `select` an explicit policy for designers to compare.
- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) -- **is-evidence-for**: This is a worked example of a compact semantics authored separately from any implementation. Predicate transformers define meaning, guard evaluation order is semantically irrelevant, and concurrent evaluation is admitted ("nothing in our semantics excludes that"). Nondeterminism appears as permitted outcomes, as the note's line 18 describes, so several implementations can conform to one reference.

**Sources**
- [ToolGate](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) -- **compares-with**: The axis is guards that filter an admissible set before an underdetermined choice. ToolGate's Hoare-style preconditions prune tool candidates, and probabilistic ranking chooses among the rest. That is a guarded command set whose arbitrary selection has been replaced by a learned policy. The comparison exposes what ToolGate gives up: its guarantee now depends on the postcondition check, not on wp holding for every selection.
- [Agent Behavioral Contracts](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- **compares-with**: The axis is how a specification handles non-determinism. wp is demonic: the result must be guaranteed for every permitted selection. ABC's (p,delta,k)-satisfaction instead treats LLM non-determinism probabilistically. Together they mark the two ends of contract semantics under non-determinism.
- [Is AI the next layer of abstraction?](../../../../sources/is-ai-the-next-layer-of-abstraction.ingest.md) -- **compares-with**: The axis is what a precise translation contract requires. Seemann requires a translation that is well defined and deterministic. Dijkstra, whom Seemann cites, shows that a fully defined semantics can be non-deterministic. This separates Seemann's two requirements: definedness, not determinism, is the part that carries the weight.

## Bidirectional Candidates

- [Underspecification and indeterminism complicate programming for prompts in distinct ways](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) <-> source -- **is-evidence-for** (theory to source, under the theory collection's rules; verify that the theory COLLECTION authorises the label): the note says "In deterministic code there's no gap between what the code says and what it does". A return link would let the note cite guarded commands as the formal-semantics case where permitted variation exists without ambiguity.

## Reverse-edge Candidates

- [Symbolic form holds consumers to a semantic reference](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) → source ingest -- The note asserts that a formal reference "may leave permitted variation" but gives no classical instance. EWD 472 is the standard one. Add the link only after the ingest exists, and point it at the ingest, never at the snapshot.
- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) → source ingest -- Its statement that "nondeterminism can be represented as permitted transitions" currently has no citation. The ingest would supply one.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [A guard against a conjectured requirement removes the experiment that would test it](../../../../theory/a-guard-against-a-conjectured-requirement-removes-the-experiment-that.md) -- The match is keyword-only. "Guard" there means a protective rule added against a conjectured harm, not a boolean condition that makes an alternative eligible. Linking would conflate two senses.
- [Near-decomposability may make local inspection affordable](../../../../theory/near-decomposability-may-make-local-inspection-affordable.md) -- Its invariant paragraph (line 54) concerns whether a local intervention preserves a required property. EWD's Theorem 3 is a compositional invariant-preservation rule, which is related. But the note's subject is inspecting learned systems, and the connection would run through the parked invariants-under-composition workshop rather than through either artifact's claim. Revisit if that inquiry produces a theory note.
- [Progressive constraining commits only after patterns stabilize](../../../../theory/progressive-constraining-commits-only-after-patterns-stabilize.md) -- Both defer determinization, but the note's mechanism is observing many LLM runs before committing. EWD gives no observation-driven criterion. The commitment-not-derivation candidate carries the deferral axis more precisely.
- [Execution indeterminism is a property of the sampling process](../../../../theory/execution-indeterminism-is-a-property-of-the-sampling-process.md) -- Its subject is runtime sampling and numerical variation. EWD's non-determinacy is a specification property, so the contrast is already better placed in the underspecification note.
- [The boundary of automation is the boundary of verification](../../../../theory/the-boundary-of-automation-is-the-boundary-of-verification.md) -- The calculus's self-certifying property ("it will tell us that we have reached such a goal") is adjacent, but the note is a cross-domain economic synthesis. The formal-systems candidate carries the routine-versus-invention point more precisely.
- [Parnas 1972](../../../../sources/parnas-1972-criteria-decomposing-systems-modules.ingest.md) -- It is a contemporaneous classic, but its axis (hiding likely changes behind module boundaries) has no named shared axis with guarded-command derivation.
- `kb/agent-memory-systems/reviews/voyager.md` and `kb/agentic-systems/reviews/beads-rust.md` -- Both are keyword hits on "preconditions" and "non-determin" with no shared mechanism.

## Index Membership

- [Computational model tag head](../../../../tags/computational-model-README.md) -- This applies only if the future ingest analyses EWD 472's transfer to LLM orchestration, for example guarded selection compared with `select(K)` or demonic compared with probabilistic contracts. The inline `tags:` would then go on the ingest. Sources are outside tag participation, so this is a search tag, not a membership listing. Do not tag if the ingest only summarises the paper.

## Synthesis Opportunities

The underspecification note, the symbolic-form note and the ABC ingest, read with EWD 472, suggest a higher-order claim the KB has not written. There may be three distinct ways a specification can leave behaviour open:
- natural-language ambiguity, where the permitted set is itself unsettled
- formally declared non-determinacy, where the permitted set is precise and correctness quantifies over all of it (EWD)
- probabilistic compliance, where the permitted set is precise but conformance is statistical (ABC)

Each implies a different test target. This is a candidate only. Do not write it during connect.

## Maintenance Observations

- The KB has no source for classical formal program semantics: Hoare, Dijkstra, Meyer or refinement calculus. Several theory notes appeal to "contracts", "permitted variation" and "invariants" without a citation for the originating formalism. This ingest would be the first.
- The `invariants-under-composition` workshop is parked and is an excluded link destination. EWD's Theorems 3 and 4, which compose per-branch invariant preservation into loop correctness, are a likely reading lead for it. A workshop maintainer may want to know the ingest exists, but no link should be authored from sources into `kb/work/`.

## Flags

- **Tension:** [the underspecification note](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) says "In deterministic code there's no gap between what the code says and what it does". EWD 472 shows formally specified code whose text deliberately leaves both the activity and the final state undetermined. The note's sentence is scoped to "deterministic code", so this is not a contradiction. It does show that the note's two-way split omits a third, formally specified kind of variation. Flagged, not resolved.
- **No ingest yet:** every Connections Found entry is for the future `kb/sources/ewd472-guarded-commands.ingest.md`. If the ingest is written with a narrower analytical focus, re-filter these candidates against that focus.
