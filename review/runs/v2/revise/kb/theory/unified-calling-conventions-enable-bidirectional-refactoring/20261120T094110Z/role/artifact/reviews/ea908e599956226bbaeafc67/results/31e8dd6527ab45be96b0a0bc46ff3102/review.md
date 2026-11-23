---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - if neural and symbolic components present the same interface, callers don't need
    to know which they're talking to
  reason: PARTLY SUPPLIED — kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md
    — names the note its strongest landing point and needs the claim that a common
    call surface lets components be swapped; the note supplies that claim but grounds
    the interface only in shared names, while the ingest reports that a common call
    surface also needs semantic mappings.
- scope: passage
  quotes:
  - if neural and symbolic components present the same interface, callers don't need
    to know which they're talking to
  reason: UNTAKEN — kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md
    — the ingest's qualification that a common call surface needs semantic mappings,
    not only shared names, does not appear in the note, which presents name-based
    dispatch as sufficient for an implementation-agnostic interface.
- scope: passage
  quotes:
  - implementation-agnostic interfaces (the same name can resolve to either neural
    or symbolic)
  reason: PARTLY SUPPLIED — kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md
    — needs the shared-callable-surface claim as the object of its qualification;
    the note supplies the shared surface but not the data and protocol mappings the
    ingest says are required when regimes disagree about values and behavior.
- scope: passage
  quotes:
  - implementation-agnostic interfaces (the same name can resolve to either neural
    or symbolic)
  reason: UNTAKEN — kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md
    — the ingest offers 'a useful qualification' that sharing a callable surface requires
    both data mappings and protocol mappings; the note states no such condition and
    does not cite the source.
- scope: passage
  quotes:
  - Each link can be independently refactored without disturbing the rest.
  reason: SUPPLIED — kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md
    — needs the mechanism claim that components behind a uniform calling convention
    can be rewritten while neighbours stay unchanged, which the note states. One of
    its three passages is cut at 1200 characters, so part of what it attributes to
    the note is unseen.
- scope: document
  quotes: []
  reason: UNTAKEN — kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md
    — the ingest offers iii's FSM rewrite as concrete production evidence for the
    note and observes that the note 'currently grounds the claim only on llm-do';
    the note still cites only llm-do. Its other recommendation, a new note in kb/notes/
    that links to this one, targets a different artifact.
- scope: passage
  quotes:
  - if neural and symbolic components present the same interface, callers don't need
    to know which they're talking to
  reason: PARTLY SUPPLIED — kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md
    — cites the note as the reason stable interfaces matter and says model/harness
    co-training overfitting is a brittleness 'the unified-calling-conventions note
    predicts'; the note supplies stable call sites but makes no prediction about model–harness
    coupling or co-training.
- scope: passage
  quotes:
  - implementation-agnostic interfaces (the same name can resolve to either neural
    or symbolic)
  reason: SUPPLIED — kb/sources/upml-framework-for-knowledge-system-reuse.ingest.md
    — compares UPML with the note on treating an explicit interface as the boundary
    that permits recomposition; the note supplies that interface claim.
- scope: document
  quotes: []
  reason: SUPPLIED — kb/tags/computational-model-README.md — needs only a citation
    for calling conventions that let components move between neural and symbolic implementations;
    the title and mechanism section supply it.
- scope: passage
  quotes:
  - A team can also switch back to a prompt to test a proposed change while the code
    still meets its current requirement.
  reason: SUPPLIED — kb/tags/constraining-README.md — lists the note as 'how to commit
    reversibly'; the codify steps with unchanged call sites and the switch-back-to-prompt
    paragraph supply reversibility.
- scope: passage
  quotes:
  - define an agent to handle a task. Quick to add, handles ambiguity.
  reason: PARTLY SUPPLIED — kb/theory/ad-hoc-prompts-extend-the-system-without-schema-changes.md
    — needs the claim that one can start with a prompt and later extract to a skill
    without changing call sites; the note's progression extracts to Python code, not
    to a skill, so the prompt-to-skill move is supplied only through the general shared-interface
    claim.
- scope: passage
  quotes:
  - refactoring across the boundary becomes a local operation
  reason: SUPPLIED — kb/theory/code-complements-weight-prompt-with-symbolic-operations.md
    — needs the claim that movement between model interpretation and executed code
    is local while the interface is preserved; the note states it.
- scope: passage
  quotes:
  - implementation-agnostic interfaces (the same name can resolve to either neural
    or symbolic)
  reason: SUPPLIED — kb/theory/llm-context-interprets-instructions-and-content-through-one-medium.md
    — needs the claim that one interface can resolve names to neural or symbolic implementations;
    the note states it in those terms.
- scope: passage
  quotes:
  - Local scope — each agent gets only its arguments
  reason: SUPPLIED — kb/theory/llm-context-is-composed-without-scoping.md — needs
    llm-do's per-agent prompts and arguments as an existing approximation of frame-local
    context; the note supplies it in one scheduler-table cell and the .agent-file
    description, without further argument.
- scope: passage
  quotes:
  - A team can also switch back to a prompt to test a proposed change while the code
    still meets its current requirement.
  reason: SUPPLIED — kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md
    — needs the claim that refactoring from codified to learned is a local, cheap
    operation; the opening framing, step 4 and the switch-back paragraph supply the
    reverse direction.
- scope: passage
  quotes:
  - unified calling makes the relaxing refactoring cheap once the signal fires
  reason: DUPLICATED — kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md
    — the note's footer annotation and the dependent's passage state the same relation
    ('unified calling makes acting on relaxing signals cheap'); the dependent's version
    is slightly more useful to its readers because it names the mechanism, that refactoring
    from codified to learned is a local operation.
- scope: passage
  quotes:
  - implementation-agnostic interfaces (the same name can resolve to either neural
    or symbolic)
  reason: SUPPLIED — kb/theory/reflective-coverage-is-graded-across-representational-forms.md
    — needs the note as one interface-level mapping; the note supplies that mapping,
    and the obligations the dependent says it leaves open (aspect coverage, authority,
    lineage) are the dependent's own claim.
- scope: passage
  quotes:
  - refactoring across the boundary becomes a local operation
  reason: PARTLY SUPPLIED — kb/theory/research/adaptation-agentic-ai-analysis.md —
    needs the claim that moving learned behavior between neural, natural-language
    and symbolic surfaces is cheaper when call boundaries stay stable; the note supplies
    stable boundaries across a two-way neural/symbolic split in which LLM-interpreted
    prompts count as neural, so the dependent's three-way distinction is not supplied.
- scope: passage
  quotes:
  - implements this through a hybrid VM where agents (`.agent` files, LLM-backed)
    and tools (Python functions) share a single namespace
  reason: SUPPLIED — kb/theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md
    — needs the llm-do call-boundary side of its comparison; the mechanism section
    supplies it.
- scope: passage
  quotes:
  - Python code that owns control flow rather than a graph DSL
  reason: SUPPLIED — kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md
    — needs the graph-DSL versus imperative-scheduler comparison as an instance of
    its representation choice; the scheduler section and table supply it.
outcome: report
description: Retained report review of kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
  against kb/instructions/role-in-the-kb-gate.md
contract: report
note: kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md
criterion: kb/instructions/role-in-the-kb-gate.md
note-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
criterion-sha256: 86d5c3082fa3fb82afab97a45faf7c7ae3265ce3a43ae7791051657759ca54bd
target-sha256: 9d348be14b8e3bb5f30d7e6d46280ddec06cdfbfe1c1274c5ec382876cdbbaa0
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/role/calls/launches/31e8dd6527ab45be96b0a0bc46ff3102/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/role/artifact/reviews/ea908e599956226bbaeafc67/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/role
launch: 31e8dd6527ab45be96b0a0bc46ff3102
completed-at: '2026-11-20T09:52:02Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring/20261120T094110Z/role/calls/launches/31e8dd6527ab45be96b0a0bc46ff3102/outputs/review.md
raw-output-sha256: afab03d3fb14c4b0b04b9be6a9b8d8b78bef1423129ffc919ed9728bef184be8
format: 2
---

# Role in the KB: Unified calling conventions enable bidirectional refactoring

## Role

The note is the KB's main citation for one mechanism: when neural and symbolic components share a name-based interface, an implementation can move across the boundary without changing call sites. Theory notes cite it as a premise or as an applied example of this claim. Four source ingests use it as the landing point for external evidence and qualifications. Separately, two dependents draw on its llm-do scheduler details: frame-local arguments and the graph-DSL contrast.
Relied on: shared interface / same name resolves to either implementation; refactoring across the boundary as a local operation with unchanged call sites; reversibility (relaxing back to a prompt); llm-do's hybrid VM as the call-boundary example; the imperative-scheduler versus graph-DSL contrast; per-agent local scope. Unused: the connection to typed callables, the spec-mining step's specifics, the friction-toward-big-bang-rewrites claim, the "Native Python" control-flow and refactoring rows of the table, and the open questions.

## Dependents

- `kb/sources/brichau-et-al-2002-towards-linguistic-symbiosis.ingest.md` — shared call surface, qualified by semantic mappings.
- `kb/sources/gybels-et-al-2006-inter-language-reflection.ingest.md` — shared callable surface, qualified by data and protocol mappings.
- `kb/sources/how-to-build-your-own-agent-harness-2060069083878408689.ingest.md` — independent-replacement mechanism; one passage cut at 1200 characters.
- `kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.ingest.md` — stable interfaces, plus a prediction about co-training brittleness that it attributes to the note.
- `kb/sources/upml-framework-for-knowledge-system-reuse.ingest.md` — explicit interface as the recomposition boundary.
- `kb/tags/computational-model-README.md` — citation.
- `kb/tags/constraining-README.md` — citation for reversible commitment.
- `kb/theory/ad-hoc-prompts-extend-the-system-without-schema-changes.md` — prompt-to-skill extraction without changing call sites.
- `kb/theory/code-complements-weight-prompt-with-symbolic-operations.md` — local movement between execution paths.
- `kb/theory/llm-context-interprets-instructions-and-content-through-one-medium.md` — names resolving to either implementation.
- `kb/theory/llm-context-is-composed-without-scoping.md` — llm-do's frame-local context.
- `kb/theory/operational-signals-that-a-component-is-a-relaxing-candidate.md` — cheap codified-to-learned refactoring.
- `kb/theory/reflective-coverage-is-graded-across-representational-forms.md` — one interface-level mapping.
- `kb/theory/research/adaptation-agentic-ai-analysis.md` — stable boundaries across three surfaces.
- `kb/theory/rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md` — llm-do's call-boundary side.
- `kb/theory/statecharts-and-programs-differ-in-what-they-show-not-compute.md` — graph-DSL versus imperative scheduler.

## Duplication

The note's footer annotation on `operational-signals-that-a-component-is-a-relaxing-candidate.md` and that dependent's annotation on this note restate the same relation. The dependent's version also names the mechanism: refactoring from codified to learned is a local operation. No other duplication is visible in the supplied passages.

## Untaken recommendations

- Brichau et al. ingest: a common call surface needs semantic mappings, not only shared names.
- Gybels et al. ingest: sharing a callable surface requires data and protocol mappings when regimes disagree.
- iii harness ingest: iii's rewrite is production evidence for a claim the note grounds only on llm-do. Part of this ingest's first passage is cut and unseen.

## Reach

- The claim that the same name resolves to either a neural or a symbolic implementation reaches `llm-context-interprets-instructions-and-content-through-one-medium.md`, `reflective-coverage-is-graded-across-representational-forms.md`, the UPML ingest, and the Brichau and Gybels ingests.
- The claim that refactoring across the boundary is local, with unchanged call sites, reaches `code-complements-weight-prompt-with-symbolic-operations.md`, `ad-hoc-prompts-extend-the-system-without-schema-changes.md`, `research/adaptation-agentic-ai-analysis.md`, `tags/constraining-README.md`, `tags/computational-model-README.md`, and the iii and anatomy ingests.
- The reverse direction (relaxing back to a prompt) reaches `operational-signals-that-a-component-is-a-relaxing-candidate.md` and `tags/constraining-README.md`.
- The llm-do hybrid VM description reaches `rlm-tendril-and-llm-do-place-symbolic-work-at-different-persistence.md`.
- The scheduler table reaches `statecharts-and-programs-differ-in-what-they-show-not-compute.md` (graph-DSL contrast) and `llm-context-is-composed-without-scoping.md` (local scope row).
- The two-way neural/symbolic vocabulary reaches every theory dependent. `research/adaptation-agentic-ai-analysis.md` already uses a three-way split.
- The typed-callables section, the open questions and the big-bang-rewrite friction claim reach no dependent.
