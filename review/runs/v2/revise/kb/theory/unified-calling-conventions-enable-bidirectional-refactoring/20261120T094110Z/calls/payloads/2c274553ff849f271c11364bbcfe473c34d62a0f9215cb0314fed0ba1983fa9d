purpose: "Explain how a shared calling convention lets a team change one component between an LLM-backed prompt and code without changing its callers, both in production and while testing proposed requirements."
must-keep:
  - "A team may temporarily replace working code with a prompt in a test run to compare proposed behaviors behind the same interface. This need not reflect brittleness or scaling. If prompt edits make exploration cheaper, the chosen behavior can still return to code for production."
  - "If neural and symbolic components present the same interface, callers don't need to know which they're talking to, and moving a component across the boundary leaves its call sites unchanged, so the refactoring is a local operation."
  - "llm-do's imperative scheduler contrasts with graph-defined orchestration: agent A calls agent B as a function, and each agent gets only its arguments (local scope)."
passes:
  - pass: narrow-overclaims
    scope: "Four passages only: (1) in the opening paragraph, the sentence 'if neural and symbolic components present the same interface, callers don't need to know which they're talking to' — say that the interface means the name plus the argument and output schema and the description the LLM caller sees, without weakening the unchanged-call-site claim; (2) in 'Why this matters for constraining', the sentences 'But without a unified interface, each codification step is a breaking change … pushes toward big-bang rewrites' — compare against systems that expose agents and tools through different invocation surfaces, and mark the rewrite effect as an expectation; (3) the lead-in 'With unified calling, the progression is smooth:' — mark the progression as an illustration; (4) in 'The scheduler layer', the sentence naming LangGraph and CrewAI — narrow it to graph-defined orchestration such as LangGraph's, keeping the contrast. Do not touch the numbered steps, the test-run paragraph or the table."
  - pass: fix-strategy-taxonomy
    scope: "The opening sentence attributing the constrain/relax framing to the linked note, including its link text (link target unchanged), and the 'Instructions are typed callables … practical rather than just analogical' sentences."
    finding: kb/reports/state/review/results/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md/semantic/grounding-alignment.md
  - pass: fix-strategy-taxonomy
    scope: "The sentence 'This requires **name-based dispatch**: components are identified by string name rather than direct object reference.' and the sentence after it."
    finding: kb/reports/state/review/results/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md/prose/source-residue.md
  - pass: fix-strategy-taxonomy
    scope: "Only the two sentences after the diagram: 'The calling convention is uniform across the chain. Each link can be independently refactored without disturbing the rest.' Leave steps 3 and 4 of the progression untouched; their routing question is open with the operator."
    finding: kb/reports/state/review/results/kb/theory/unified-calling-conventions-enable-bidirectional-refactoring.md/semantic/completeness-boundary-cases.md
  - pass: readability-and-flow
    scope: "Body above the footer, excluding steps 3 and 4 of the numbered progression and the scheduler table rows. Name both directions next to the core claim in the opening, using only what the body states: codifying and extending in production, and switching back to a prompt to test proposed requirements. Remove the recap sentence after the scheduler table that repeats its Refactoring row, and the sentence 'Both are callables with defined interfaces.'"
stop: null
