# Assessment: Unified calling conventions enable bidirectional refactoring between neural and symbolic

**Purpose (operator's):** Explain how a shared calling convention lets a team change one component between an LLM-backed prompt and code without changing its callers, both in production and while testing proposed requirements.

The artifact declares no write brief, so this run's must-keep list holds the operator's item and the divergence claims below.

## What reads well

The four-step `sanitize_filename` progression and the `ticket_classifier` test-run paragraph show concretely that the name and the set of outputs stay fixed while the implementation changes. That is the purpose in miniature.

## Sentence a hostile reviewer attacks first

"The [underspecified instructions framing](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) says components should move between underspecified (LLM-interpreted) and precise (code) semantics as systems evolve — constrain patterns to code, relax rigid code back to LLM."

Two stored results fail this sentence (grounding-alignment, concept-attribution), and misleading-link-text warns on it. The linked note does not state that prescription, so a reader who follows the link finds no support for the premise that frames the whole note. The next target is "Each link can be independently refactored without disturbing the rest." The critique attacks it as the location-transparency fallacy, and three other reports flag it.

## Ranked changes (highest value against the purpose first)

1. **Fix the misattributed opening premise and the overstated typed-callables attribution.** Cost: two sentences. Pass: `fix-strategy-taxonomy` on `semantic/grounding-alignment` (finding-14). This fix also resolves the same passages flagged by `sentence/concept-attribution` (finding-16) and finding 1 of `sentence/misleading-link-text` (finding-17), because the fix rewrites the link text along with the attribution. The likely strategies are `unsourced-addition` or `hedge-strength-mismatch`: present the constrain/relax movement as the note's own premise, or attribute only what the target says. The typed-callables sentence keeps the target's limited, document-typed sense. Link targets stay unchanged. The operator may later prefer to point the opening at a note that does state the constrain/relax movement. That would be a separate edit.
2. **State the interface-preservation precondition where the note claims independent refactoring.** Cost: one clause. Pass: `fix-strategy-taxonomy` on `semantic/completeness-boundary-cases` (finding-12), using `boundary-case-acknowledged`. Scope: the two sentences after the diagram only. This change serves "without changing its callers" directly. Callers stay unchanged only when the replacement keeps the same arguments and output set. The note's own test-run example already assumes this condition ("receive the same set of queue labels"). The info finding on step 3 is left to a claim question (see below).
3. **Say what "the same interface" covers, and narrow the motivating overclaims.** Cost: four sentences. Pass: `narrow-overclaims`.
   - In the opening, "if neural and symbolic components present the same interface" has two readings: name only, or name plus argument and output schema plus the description the LLM caller sees (`semantic/underspecified-assertions`, finding-15). Under the first reading the central claim is false for every codification that changes a schema. Narrow it to the second reading.
   - "each codification step is a breaking change … pushes toward big-bang rewrites" is a universal claim and an unobserved causal one (`semantic/epistemic-status-blur` finding-13 item 1; the critique and premise reports). Wrappers already keep call sites stable without a shared namespace. Narrow the comparison to systems that expose agents and tools through different invocation surfaces, and mark the rewrite effect as an expectation.
   - "With unified calling, the progression is smooth:" presents a constructed scenario as an observed outcome (finding-13 item 2). Mark it as an illustration.
   - "declarative agent frameworks (LangGraph, CrewAI) where orchestration is defined as node-edge graphs" is inaccurate for CrewAI (`prose/orphan-references`, finding-10). Narrow it to graph-defined orchestration such as LangGraph's. Keep the contrast between graph DSLs and an imperative scheduler, because a dependent relies on it.
4. **Scope the name-based-dispatch requirement to LLM callers.** Cost: one sentence. Pass: `fix-strategy-taxonomy` on `prose/source-residue` (finding-11). The premise report shows the universal form is false: ordinary polymorphism lets a code caller switch implementations without string names. Names are required because an LLM emits the call as text, and that is the case the purpose concerns. This is a narrowing, which the strategy taxonomy permits. It is not a change of thesis.
5. **Surface both directions and remove local recaps.** Cost: one pass over the body. Pass: `readability-and-flow`.
   - The purpose names two occasions: production, where the note codifies and then extends by relaxing, and testing proposed requirements, where the team switches back to a prompt. The opening names neither direction. The reverse move appears only in a late paragraph (compression synthesis, opportunity 2). The purpose settles the synthesis's open question: "bidirectional" covers both occasions. The pass should name both next to the core claim, using only what the body already says.
   - Remove the closing scheduler sentence that repeats the table's Refactoring row, and "Both are callables with defined interfaces.", which the previous sentence already entails (`compression-bundle/marginal-value-redundancy`, finding-6 items 1–2).
   - Keep the test-run paragraph and every table row.

The run order follows depth: `narrow-overclaims`, then the three `fix-strategy-taxonomy` entries (all depth 2), then `readability-and-flow` (depth 4).

## Overclaims: support or divergence

- **Divergence, must keep:** "if neural and symbolic components present the same interface, callers don't need to know which they're talking to, and refactoring across the boundary becomes a local operation." This is the thesis, and most dependents rely on it (role report). A pass may define the interface. It may not weaken the claim that call sites stay unchanged.
- **Divergence, must keep:** the test-run paragraph, from the operator's must-keep list.
- **Divergence, must keep:** the contrast between graph-defined orchestration and llm-do's imperative scheduler, including local scope, where each agent gets only its arguments. Two dependents rely on it: `kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md` and `kb/theory/llm-context-is-composed-without-scoping.md`.
- **Support, may be narrowed:**
  - "This requires name-based dispatch"
  - "each codification step is a breaking change … big-bang rewrites"
  - "the progression is smooth"
  - "Each link can be independently refactored without disturbing the rest"
  - "(LangGraph, CrewAI) where orchestration is defined as node-edge graphs"
  - "makes the type-theoretic view practical rather than just analogical"

## Claim questions for the operator

1. **Behavioural contract and a `## Scope` section** (defect, correctable by a boundary statement).
   - Sources: `kb/types/note` (finding-8); the critique (`.../results/.../kb/instructions/critique-note.md`); the premise report (`.../kb/instructions/premise-decomposition-gate.md`); the composition-friction report (`.../kb/instructions/composition-friction-gate.md`).
   - The case: an upstream agent that retried around a lenient agent callee is disturbed when that callee becomes code that raises. The call site stays unchanged, yet the caller's behaviour changes. The same applies to determinism, latency, cost and failure modes.
   - The proposal: add a Scope section saying that call-site stability is syntactic, and that callers that depend on the callee's behaviour must be checked again after a swap. Such a section would leave every claim that dependents rely on intact.
   - The passes add only the interface precondition (change 2). They do not add a Scope section.
2. **Where routing lives after partial codification** (defect).
   - Passages: step 3, "The agent still handles ambiguous cases. The call site doesn't change.", and step 4, "Add an LLM call for the new cases. Again, the call site doesn't change."
   - Sources: the friction, critique and premise reports, and the info item in finding-12.
   - The two readings: if a wrapper under the old name routes inputs between code and agent, the call site is preserved by an added dispatcher. If the caller must choose between two names, the call site changes. Code-then-fallback routing also fails when the code gives a wrong answer without raising an error.
   - One sentence naming the router would settle it. The passes are scoped away from steps 3 and 4.
3. **Compressing or moving the scheduler section** (choice, no defect shown beyond the CrewAI wording that change 3 narrows).
   - Sources: branch-bloat (finding-4), detail-overhang (finding-5), framework-decoration (finding-3), `kb/theory/COLLECTION` composability (finding-7), and synthesis opportunity 1 (`.../20261120T094110Z/synthesis`).
   - The case for it: the section is off-purpose.
   - Why it is not ranked first, and why no pass is planned: removing the State row or the graph-DSL contrast would alter what two dependents rely on, `kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md` and `kb/theory/llm-context-is-composed-without-scoping.md` (role report: `.../20261120T094110Z/role`). No receiving artifact exists yet.
   - The Python-specificity open question would move with the section. The operator may decline this proposal.
4. **Description wording** (`kb/theory/COLLECTION` finding-7, info): "llm-do demonstrates this". llm-do is the case the claim was built from, so "illustrates" or "exhibits one such convention" would fit its role.
5. **Identify llm-do on first mention** (`accessibility/unidentified-references`, finding-1). The fix is a short factual gloss, for example "a runtime that lets LLM agents and Python tools call each other". No pass owns adding that fact, and the operator can state it accurately.

## Stale qualifications for the operator

- In the footer, the "Abstracted into" link text uses an old title. The target is now titled "RLM, λ-RLM, Tendril, and llm-do separate restriction from persistence" (finding-17, info). "Abstracted into" is also not a label in the collection's table and mirrors the target's own edge (finding-7).
- The footer gloss on programming-practices says refactorings "transfer directly". The target's thesis is that transfer needs evidence matched to the question (finding-17, info).
- The footer gloss on codification calls it "the phase transition", a figure that contradicts the locality claim (`prose/mannered-prose`, finding-9). A one-phrase swap would fix it: "the step that moves a component from neural to symbolic".
- Four footer entries lack relation labels and repeat the body's framing (finding-7; `complexity/connection-inflation`, finding-2). The relaxing-candidate footer entry duplicates the dependent's own annotation (role report).

These are link-maintenance edits for their own commit. No pass owns them.

## Findings and proposals not acted on

| Finding or proposal | Reason not acted on |
|---|---|
| `accessibility/unidentified-references` (finding-1) | Claim question 5; no pass adds facts. |
| `complexity/connection-inflation` (finding-2) | Footer link maintenance; little value against the purpose. |
| `complexity/framework-decoration` (finding-3) | The ASCII diagram adds little but costs little. The branch-bloat review reads it as supplying the premise. The table rows are protected by dependents (claim question 3). |
| `compression-bundle/branch-bloat` (finding-4), `compression-bundle/detail-overhang` (finding-5) | Claim question 3. |
| `compression-bundle/marginal-value-redundancy` (finding-6) items 3–4 (info) | Item 3 concerns table rows that dependents rely on. Item 4 is handled by the finding-12 fix. |
| `kb/theory/COLLECTION` (finding-7) | Footer labels are link maintenance. Composability is claim question 3. The description is claim question 4. |
| `kb/types/note` (finding-8) | Claim question 1. |
| `prose/mannered-prose` (finding-9) | Footer phrase. `plain-wording` is a per-item pass that would stop the run for one footer swap, so it is listed as a stale qualification instead. |
| `prose/orphan-references` (finding-10) item 2 (info) | Covered by the `narrow-overclaims` scope on the same sentence. |
| `semantic/underspecified-assertions` (finding-15) item 2 (info) | The ambiguity of "local" is not material once the interface is defined. |
| `sentence/concept-attribution` (finding-16), `sentence/misleading-link-text` (finding-17) item 1 | Resolved by the finding-14 fix on the same passages. Finding-17 items 2–3 are stale qualifications. |
| Extension (critique): engage the RPC location-transparency precedent; say what a native namespace buys over an adapter | The claim as scoped stands without it. `narrow-overclaims` instead narrows the adapter contrast. |
| Extension (role report): the Brichau and Gybels ingests' qualification that a shared surface needs semantic, data and protocol mappings; iii's FSM rewrite as a second piece of evidence | Neither the purpose nor a brief asks for this coverage. |
| Extension (friction report): the typed view becomes practical only with output validation | Handled by narrowing the typed-callables attribution (finding-14). The validation requirement is not added. |
| Role report: the anatomy ingest attributes a co-training brittleness prediction to this note | The prediction is the ingest's, not the note's. If anything needs correcting, it is the dependent. |
