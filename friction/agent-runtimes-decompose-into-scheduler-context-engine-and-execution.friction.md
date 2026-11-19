# Friction check: Agent-runtime analysis should separate scheduling, context assembly, and external state

**Note:** `kb/notes/agent-runtimes-decompose-into-scheduler-context-engine-and-execution.md`
**Central claim (one sentence):** For runtimes organized as repeated bounded model calls, treating scheduling, context assembly, and external state or action services as distinct analytical responsibilities helps locate failures even when one implementation or feature spans those responsibilities.

## Filter
**Verdict:** SURVIVES

The claim asks analytical separation, implementation overlap, and diagnostic usefulness to hold at once. Those properties can coexist because the categories classify decisions and causal roles rather than requiring separate implementation modules; a shared component can therefore participate in more than one category without collapsing the distinctions.

## Signal — thinnest joints
1. **“The three questions route failures to different repair surfaces.”** — **THIN** — The categories say where a symptom appears, but the note does not establish that the symptom locates its underlying cause: missing call evidence, for example, could result from a scheduling choice, a context-selection defect, or an external retrieval failure. The proposed routing may need a second causal trace before it identifies the repair surface.
2. **“The separation also prevents category errors.”** — **THIN** — The filesystem, tool-schema, execution, transcript-retention, and excerpt-selection examples show that the roles are conceptually different. They do not show that adopting the three-part vocabulary is sufficient to prevent misclassification in a coupled runtime or when one failure crosses the categories.
3. **“choosing the next operation and assembling the chosen call's input can fail separately even when one scheduler performs both.”** — **THIN** — Conceptual separability makes separate failure descriptions possible, but the note gives no worked failure in which the two diagnoses lead to demonstrably different repairs inside a single scheduler.
4. **“Files are one useful implementation because files can defer schema commitment”** — **THIN** — Deferring schema commitment supports flexibility, but it does not by itself establish the property doing the work in this section: that files provide inspectable, exact external state suitable for diagnosis. That usefulness is supported by the preceding inspectability claim, not by this stated reason alone.
5. **“The mappings show that the three questions can re-express features from two practitioner accounts and expose responsibilities hidden inside compound features.”** — **HOLDS** — The two tables directly perform that re-expression, and the mixed rows explicitly separate retrieval from retention, descriptions from execution, and delegation from input scoping. The note appropriately limits this to a retrospective demonstration rather than treating it as evidence of convergence or exhaustiveness.

## For the human
Look first at whether “routing” means classifying the visible failure or locating its causal repair surface; the note currently moves between those stronger and weaker meanings without a worked causal trace.
