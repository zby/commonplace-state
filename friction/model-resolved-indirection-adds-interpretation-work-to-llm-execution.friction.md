# Friction check: Model-resolved indirection adds interpretation work to LLM execution

**Note:** `kb/notes/model-resolved-indirection-adds-interpretation-work-to-llm-execution.md`
**Central claim (one sentence):** A reference adds model-side interpretation and failure costs only when the model must resolve it; upstream resolution can remove that work but shifts binding, authority, token, and regeneration costs, so resolver and binding time should be chosen by the complete delivered forms.

## Filter
**Verdict:** SURVIVES
The claim combines reduced model-side interpretation with retained runtime authority and explicit generation and maintenance costs; it does not require upstream binding to be both free and universally preferable.

## Signal — thinnest joints
1. **“Natural-language instructions have no equivalent procedure unless the surrounding harness supplies one.”** — UNSUPPORTED — The code comparison shows that a runtime resolver exists, but it does not establish that a natural-language convention or model-side procedure cannot provide an equivalent resolution rule, nor that the absence of a harness resolver by itself creates the claimed extra work.
2. **“In both cases, semantic work moves upstream. It does not disappear.”** — THIN — The search-command and conditional examples show that selection or classification can be done before consumption, but they do not define “semantic work” or establish that every omitted branch or fixed command represents work relocated rather than work made unnecessary by a known fact.
3. **“the literal form’s token and maintenance costs, including regeneration, do not exceed the binding and failure costs that upstream resolution removes.”** — THIN — The condition states the desired cost ordering but gives no way to estimate the terms, account for drift introduced by regeneration, or show which failure costs upstream resolution actually removes.
4. **“Generated instructions create a derived-copy obligation. Their producer needs a validity rule and a regeneration or drift check.”** — THIN — A generated artifact can require synchronization, but the note does not establish that every generated instruction has a mutable source or validity window, or why regeneration or drift checking is necessary rather than a property of one generation workflow.

## For the human
Look first at the resolver-boundary definition and the cost comparison: specify what procedure the model lacks, what work is transferred, and how binding, failure, and regeneration costs are compared.
