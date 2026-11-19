# Friction check: Bounded-context orchestration model

**Note:** kb/notes/bounded-context-orchestration-model.md
**Central claim (one sentence):** A joint LLM-code system with symbolic inter-call execution, explicit transition-relevant state, and completed calls can be represented as a scheduler that repeatedly selects a feasible bounded call and incorporates its result, while comparisons between selection strategies require independently stated invariants and ordering criteria.

## Filter
**Verdict:** SURVIVES

The properties can coexist. Explicit scheduler state may exceed any single call's context because `select` places only a feasible view in `C`, completed results can return to that state before later scheduling, and the common representation need not itself rank the strategies it represents. The claim is conditional on symbolic inter-call execution, explicit resumable state, and completed-call boundaries; streaming interaction and independently changing environments are expressly outside it.

## Signal — thinnest joints
1. **“Parallel calls fit when the scheduler selects an independent batch from `K`”** — THIN — The defined `select(K)` returns one call specification and the minimal loop executes `call(C)` before the next selection. A batch can fit through a generalized batch-valued `select`, a batch call specification, or a behavior-preserving sequentialization argument, but the note does not choose or define one of those concretizations.
2. **“Because information value is observer-relative, material selection and task framing cannot generally be optimized independently.”** — THIN — Observer-relative value establishes that framing can change a call's usefulness, but dependence on a common observer does not by itself establish interaction between the selected material and its framing. The conclusion needs either the narrower claim that both must be evaluated relative to the same task and model, or evidence that optimizing either while holding the other fixed can miss the joint optimum.
3. **“Such workflows are unlikely to admit one useful global objective: goals are underspecified, calls are stochastic, and latency, context cost, reliability, and auditability trade off.”** — THIN — These premises make a global objective difficult to specify and validate, but they do not preclude one: uncertainty can be represented in an expected objective and competing quantities can be combined by constraints or explicit weights. The inference needs a criterion for “useful” or the narrower conclusion that the model does not supply a canonical global objective.
4. **“These observations motivate an external symbolic scheduler.”** — HOLDS — Scarce per-call context gives a reason to retain state outside calls, and avoiding stochastic mutation gives a reason to execute fully specified transitions in code. The note limits this to motivation, acknowledges the costs of exact code, and does not claim that the observations prove this architecture optimal.
5. **“Inter-call symbolic execution can be collapsed into `select` when `K` represents the complete resumable machine state.”** — HOLDS — With complete control and data state in `K`, the symbolic computation between completed calls can advance that state until it either emits the next `C` or halts. The stated completeness condition carries the inference, and the later exclusions identify cases where that condition is not available.

## For the human
Look first at the parallelism paragraph: specify how a batch is represented by the singular `C` and loop, or narrow “fit” to a behaviorally equivalent sequential execution under explicit independence assumptions.
