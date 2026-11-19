# Friction check: Cross-task transition policy remains scheduling behind a tool interface

**Note:** kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md
**Central claim (one sentence):** Code that chooses progression among distinct task goals performs scheduling regardless of whether it is exposed as a tool, and that scheduling is hidden only when the interface obscures its progression state or transition authority.

## Filter
**Verdict:** SURVIVES

The claimed properties can coexist: one component can have a tool-call interface while owning cross-task transition decisions, and the visibility of that ownership can vary independently of its scheduler role.

## Signal — thinnest joints
1. **“This is one reason LLM frameworks should keep the tool loop optional.”** — UNSUPPORTED — The need for directly programmable transition control does not by itself require an optional tool loop; a mandatory loop with sufficient transition hooks could expose the same control, so the architectural recommendation needs the missing exclusion argument.
2. **“A framework without first-class progression makes placing that logic inside a tool attractive”** — THIN — The note names the attraction but does not identify the concrete pressure that favors a tool over an application-owned loop or lower-level runtime, both of which it immediately presents as available placements.
3. **“The architectural question is whether a framework makes transition control directly programmable without forcing application code to escape its abstraction.”** — THIN — The preceding list of possible placements establishes that location can vary, but it does not establish when an application-owned loop counts as escaping the framework rather than using its intended extension boundary.
4. **“Once cross-task policy is stable enough to codify, preserving it requires explicit control logic to determine or constrain which transition executes.”** — THIN — Codification supports representing a stable policy explicitly, but the note does not spell out why preserving that policy requires executable transition control rather than, for example, declarative constraints interpreted by an existing scheduler; the broad phrase “control logic” may include that case but leaves the inference underspecified.
5. **“moving it from prompt instructions into exact code makes its execution more consistent”** — THIN — Symbolic code removes some model-level variation, but increased consistency also depends on stable inputs, runtime behavior, and whether the code captures the intended procedure; those conditions are left implicit.

## For the human
Look first at the final move from exposed transition control to an optional tool loop, because the note has not ruled out a mandatory loop with programmable transition hooks.
