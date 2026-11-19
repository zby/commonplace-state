# Friction check: Access burden and transformation burden are distinct query dimensions

**Note:** kb/notes/access-burden-and-transformation-burden-are-independent-query.md
**Central claim (one sentence):** A query's access burden and transformation burden are distinct, independently varying diagnostic dimensions even though execution can make them interact and alternate.

## Filter
**Verdict:** SURVIVES

Distinctness and interaction can coexist: the burdens classify different work relative to the currently available inputs and requested output, while an execution step can change what inputs or transformation are required next.

## Signal — thinnest joints
1. **“This separates three responsibilities that the original query may combine: specifying the intended operation, executing it, and validating that its result answers the query.”** — UNSUPPORTED — Asking whether an operation is specified well enough for mechanical execution distinguishes specification from execution, but it does not establish validation as a third responsibility or show how validation is separated from specification.
2. **“Distinguishing transformation burden enables a second routing question: is the next operation specified well enough for mechanical execution?”** — THIN — Isolating transformation work makes the specification question easier to pose, but the access/transformation distinction alone does not establish that degree of specification is the next routing axis; that requires the additional claim about differing execution error profiles.
3. **“When a trustworthy symbolic implementation exists, it should execute a fully specified operation.”** — THIN — Full specification and a trustworthy implementation establish exact executability and remove model execution variance, but the unconditional preference still needs its relevant cost and reliability assumptions; the linked separation argument supplies support for bookkeeping, not automatically for every operation called fully specified here.
4. **“These examples establish separability, not isolation. Either burden can be high while the other is low, so reducing one does not necessarily reduce the other.”** — HOLDS — The examples supply both required witness patterns: locating an answer can be hard while returning it is trivial, and known records can be easy to access while aggregation or causal explanation remains difficult. The later interaction account correctly limits the conclusion to separability rather than isolation.
5. **“Because transformation can expose missing inputs, routing is a loop rather than a fixed two-stage pipeline.”** — HOLDS — Once a transformation step can create a new access requirement, a single access-then-transform pass is insufficient; the proposed return to the relevant step follows directly.

## For the human
Look first at the jump from the specification test to three supposedly separated responsibilities, especially the ungrounded status of validation as an independently routed stage.
