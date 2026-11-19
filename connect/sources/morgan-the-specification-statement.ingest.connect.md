---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/morgan-the-specification-statement.ingest.md"
source_has_frontmatter: true
date: "2026-11-04"
depth: standard
---

# Connection Report: Ingest: The specification statement (Morgan 1988, first paper of PRG-70)

**Source:** [Ingest: The specification statement](../../../../sources/morgan-the-specification-statement.ingest.md)

The ingest already carries an inline `## Connections Found` section with eight links. All eight targets exist. This report evaluates them against the authorised label set in `kb/sources/COLLECTION.md`, proposes labels, and adds candidates the ingest does not yet name. The ingest is untracked (new) as of this run; so is its sibling [EWD 472 ingest](../../../../sources/ewd472-guarded-commands.ingest.md).

## Discovery Trace

**Outbound rules read:** `kb/sources/COLLECTION.md`, section "Outbound links". Destinations: theory, reference, agent-memory-systems, agentic-systems, tags, other sources; `kb/work/` and `kb/instructions/` excluded. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external), `derived-from` (external). External prospecting skipped: no external target supplied; the source URL is already in frontmatter.

**Topic indexes:**
- `kb/tags/constraining-README.md` (source carries `tags: [constraining]`). Not `complete: true`. Sources are outside participating collections, so no index membership. Flagged from it: [constraining](../../../../theory/definitions/constraining.md), [specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md), [prompting changes failure diagnosis](../../../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md).

**Titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/theory/ --glob '*.md' | rg -i "spec|contract|compos|invariant|permitted|variation|refin|nondetermin|indetermin|interface|decompos|semantic reference|codif|verif|abstraction|feasib|satisf"` -- ~60 hits. Flagged: symbolic-form, near-decomposability, clear-instructions, underspecification/indeterminism, specification-strategy, out-of-spec-output, verification-needs-a-typed-target, llm-context-is-composed-without-scoping, specification-level-separation. Rejected the rest as topical only (memory, scheduling, review automation).

**Description listing:**
- `rg -m1 '^description:'` on the flagged theory files and on `kb/sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md`, `kb/sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md`.

**Body search:**
- `rg -n -i "refinement|weakest.precondition|dijkstra|guarded command|nondetermin|miracle|monoton|predicate transformer|hoare|pre.?condition|postcondition|design by contract" kb/theory kb/sources kb/reference kb/agentic-systems kb/agent-memory-systems -l` -- ~80 files, mostly generic "refinement" or "precondition" usage; too broad.
- `rg -n -i "weakest.precondition|dijkstra|guarded.command|miracle|predicate transformer|refinement calculus|hoare|design by contract|\bwp\b" ...` -- substantive hits only in `ewd472-guarded-commands.ingest.md` and `toolgate-...ingest.md` (Hoare-style derivation sketches). Others were URL `wp-content` false positives.
- `rg -n -i "monoton" kb/theory` -- only `thresholding-monotone-transforms-does-not-add-an-independent-check.md` (monotone transforms of a probability; unrelated sense) and `spec-mining-as-codification.md` ("grows monotonically"; ordinary sense). Rejected.
- `rg -n -i "invariant|certificate|open question|replacement" kb/theory/near-decomposability-may-make-local-inspection-affordable.md` -- confirms the note separates locating a repair from establishing invariant preservation (line 62) and lists certificate checking without near-decomposition as an open question (line 78).
- `rg -n -i "permitted variation|may leave" kb/theory/symbolic-form-holds-consumers-to-a-semantic-reference.md kb/theory/definitions/constraining.md` -- symbolic-form names permitted variation explicitly (lines 87, 110); constraining definition does not state composition/monotonicity.
- `rg -n -i "refinement|specification statement|monoton" kb/agentic-systems kb/agent-memory-systems kb/reference -l` -- 10 files, all generic uses of "refinement" (note refinement, memory refinement). No candidate.
- `rg -l "morgan-robinson|ewd472" kb` -- no inbound links to either ingest yet.

**Link following:**
- From the EWD 472 ingest's Connections Found: [implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md), [fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md), [commitment, not derivation](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md), ABC and ToolGate ingests. Evaluated each for Morgan specifically; kept implementations-do-not-establish-shared-semantics and ToolGate, rejected the others for Morgan (their axis is non-deterministic choice, which EWD 472 owns).

## Connections Found

Existing inline links in the ingest, with proposed labels:

- [Symbolic form holds consumers to a semantic reference](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) -- **is-evidence-for**: Theorem 3 makes conformance to a reference that declares permitted variation an exact relation (satisfaction = refinement of `[pre, post]`), and the two-direction refinement ordering matches the note's separation of permitted variation from excluded guarantees.
- [Constraining](../../../../theory/definitions/constraining.md) -- **defined-in**: the ingest uses "constraining" as each refinement step narrowing permitted behaviors; a reader needs the KB term. (The ingest's added point, that the definition omits the monotonicity condition, is a candidate edit to the definition, not a label.)
- [Near-decomposability may make local inspection affordable](../../../../theory/near-decomposability-may-make-local-inspection-affordable.md) -- **is-evidence-for**: Theorem 2 gives a sufficient formal condition for the note's second step (a local repair preserves required properties): replacement refines the fragment's specification and every enclosing constructor is monotonic; the non-monotonic `if ... fi` shows the condition can fail. It also bears on the note's open question about certificate checking without near-decomposition.
- [Clear instructions can compose into an unsettled contract](../../../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) -- **compares-with**: axis is whether a combination of requirements is settled; in the calculus every combination has a meaning and an unsatisfiable one is a detectable miracle (feasibility test `pre ⇒ ∃w · post`), separating settled-but-infeasible from unsettled.
- [Programming practices for prompts need evidence matched to the question](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) -- **compares-with**: axis is where multiple valid outcomes live; here they are a first-class formal object removed step by step by refinement, not a natural-language peculiarity. Note: this target is currently being edited in the working tree (with a new brief), so re-check the axis against its revised text.
- [Specification strategy should follow where understanding lives](../../../../theory/specification-strategy-should-follow-where-understanding-lives.md) -- **compares-with**: axis is when to commit a specification; the calculus is the formal extreme of spec-first, and miracles from mistaken tactics are a precise version of a spec step that later proves unworkable.
- [Ingest: Is AI the next layer of abstraction?](../../../../sources/is-ai-the-next-layer-of-abstraction.ingest.md) -- **compares-with**: axis is what makes moving between abstraction layers trustworthy; the calculus relates layers by a correctness-preserving ordering rather than a deterministic translation.
- [Ingest: Program synthesis (Gulwani, Polozov, Singh 2017)](../../../../sources/program-synthesis-gulwani-polozov-singh-2017.ingest.md) -- **compares-with**: axis is how a program is obtained from stated intent: human-directed derivation by laws versus search over a program space; the synthesis ingest also supplies the specification-cost limitation the Morgan ingest cites.

New candidates not yet in the ingest:

- [Ingest: Guarded commands, non-determinacy and formal derivation of programs (EWD 472)](../../../../sources/ewd472-guarded-commands.ingest.md) -- **compares-with**: the two ingests are adjacent layers of one formalism. Axis: the status of miracles. EWD 472 imposes the Law of the Excluded Miracle (`wp(S, F) = F`) as well-formedness; Morgan's specification statement deliberately violates it so specifications can sit in program text, and gains refinement as one relation over all programs. A reader of either needs the other to see what the extension buys and costs. Strongest new candidate.
- [Implementations do not establish shared semantics](../../../../theory/implementations-do-not-establish-shared-semantics.md) -- **is-evidence-for**: the note separates conformance claims from formal models of implemented consumers. Morgan defines conformance (satisfaction) purely through the reference semantics, as refinement of a specification that need not be executable, so a specification can have exact meaning before any implementation exists. Moderate; EWD 472 already carries the stronger version of this edge for nondeterminism.
- [Ingest: ToolGate](../../../../sources/toolgate-contract-grounded-and-verified-tool-execution-for-llms.ingest.md) -- **compares-with**: axis is how a pre/post contract is used. ToolGate checks Hoare-style admissibility before execution and verifies results after; Morgan makes the pre/post pair itself a program and derives code that provably refines it. Names the gap between run-time checking and derivation-time refinement. Moderate; also covers the ingest's Extractable Value item 5 ("contract-grounded tool execution") which currently has no link.

## Bidirectional Candidates

- [EWD 472 ingest](../../../../sources/ewd472-guarded-commands.ingest.md) <-> source -- **compares-with**: the EWD 472 ingest's Extractable Value item 3 (Excluded Miracle) is exactly what Morgan relaxes; a return link tells its reader where the law is deliberately dropped and why.

## Reverse-edge Candidates

- [Near-decomposability may make local inspection affordable](../../../../theory/near-decomposability-may-make-local-inspection-affordable.md) → source -- **evidenced-by** (theory-side label; check `kb/theory/COLLECTION.md`): at the line separating locating a repair from establishing invariant preservation, and at the open question on certificate checking. Note that the related "invariant preservation under composition" inquiry was recently parked (commit 107bc063b) in the workshop layer; sources must not link into `kb/work/`, but the workshop may want to consume this ingest.
- [Symbolic form holds consumers to a semantic reference](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md) → source -- evidence at the "Permitted variation" bullet (line 87), alongside the EWD 472 edge already recommended by that ingest. Morgan adds the refinement ordering, which EWD 472 lacks.
- [Constraining](../../../../theory/definitions/constraining.md) → source -- possible evidence/example link if the definition gains a sentence on composition (narrowing a part narrows the whole only under monotonic composition). Conditional on that edit.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [An author should fix what the executor can't determine](../../../../theory/fix-what-the-executor-cant-determine-not-what-it-will.md) -- relevant to leaving bounded choices open, but that axis belongs to EWD 472's nondeterministic choice; Morgan's contribution (specification-as-program, refinement) adds nothing specific for this note.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- tempting (refinement steps commit choices), but the note's derivation/commitment split is about unentailed resolutions in knowledge work; mapping refinement onto it would be an unstated analogy.
- [Out-of-spec output is a failure of the interpreter, not the spec](../../../../theory/out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) -- keyword overlap on "spec"; the calculus has no interpreter-failure category, so no concrete gain.
- [Verification needs a typed target before it needs an oracle](../../../../theory/verification-needs-a-typed-target-before-it-needs-an-oracle.md) -- generic "spec as target" overlap only.
- [LLM context is composed without scoping](../../../../theory/llm-context-is-composed-without-scoping.md) and [Specification-level separation recovers scoping](../../../../theory/specification-level-separation-recovers-scoping-before-it-recovers.md) -- the frame `w` in `w: [pre, post]` is a scoping device, but the ingest does not analyze it; would need ingest revision first.
- [Thresholding monotone transforms](../../../../theory/thresholding-monotone-transforms-does-not-add-an-independent-check.md) -- "monotone" in an unrelated sense.
- [Agent Behavioral Contracts ingest](../../../../sources/agent-behavioral-contracts-formal-specification-runtime.ingest.md) -- its axis (statistical vs demonic compliance) is owned by EWD 472; Morgan adds nothing beyond ToolGate's comparison.
- All agentic-systems, agent-memory-systems and reference hits -- generic "refinement" usage; no candidate.

## Index Membership

None. Sources are outside the participating collections of `kb/tags/COLLECTION.md`; the `constraining` tag on the ingest is already the source-scoped search surface.

## Synthesis Opportunities

The EWD 472 and Morgan ingests together, with [near-decomposability](../../../../theory/near-decomposability-may-make-local-inspection-affordable.md) and [symbolic form](../../../../theory/symbolic-form-holds-consumers-to-a-semantic-reference.md), imply a higher-order claim: local replacement in any artifact system is safe only when (a) the part has a reference that declares permitted variation, (b) the replacement narrows within it, and (c) every enclosing composition is monotonic with respect to that ordering. Agent-system composition operations (context concatenation, instruction stacking) are candidates for failing (c), which is what [clear instructions can compose into an unsettled contract](../../../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md) observes informally. This is the substance of the parked invariant-preservation inquiry; not a note yet.

## Maintenance Observations

- The ingest's inline Connections Found uses prose links without labels and has no labelled footer; a future edit could add the labels above.
- [Constraining](../../../../theory/definitions/constraining.md) does not state the composition condition under which narrowing a part narrows the whole; the ingest flags this gap.
- Both formal-semantics ingests are untracked and have empty Quotes sections; their recommended `cp-skill-ground` passes are prerequisites before theory notes cite them for formula-level claims (OCR caveats in both).

## Flags

- Target [underspecification-and-indeterminism-complicate-programming-for.md](../../../../theory/programming-practices-for-prompts-need-question-specific-evidence.md) is modified in the working tree; its title now reads "Programming practices for prompts need evidence matched to the question". The ingest's link text still says "Underspecification and indeterminism complicate programming for prompts in distinct ways" -- link text is stale relative to the current title.
- Not a split candidate: the ingest has one central contribution with derived results.
