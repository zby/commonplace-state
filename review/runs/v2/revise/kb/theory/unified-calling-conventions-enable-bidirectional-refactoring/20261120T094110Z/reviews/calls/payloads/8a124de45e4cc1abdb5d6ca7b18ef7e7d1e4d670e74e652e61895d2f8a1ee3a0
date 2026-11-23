---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The [underspecified instructions framing](./prompting-changes-failure-diagnosis-with-the-semantic-reference.md) says components should move between underspecified (LLM-interpreted) and precise (code) semantics as systems evolve — constrain patterns to code, relax rigid code back to LLM."
    reason: "The linked target, 'Prompting changes failure diagnosis with the semantic reference', is about two accounts of prompting (model-defined prompt language versus English executed by a fallible interpreter) and how each assigns failures. It contains no prescription that components should move between LLM and code as systems evolve, and it does not mention relaxing code back to an LLM. Its only related passage treats code extraction as one intervention whose trade-off 'should be assessed', and points elsewhere for that. The note's opening premise, and the problem it says the framing leaves unsolved, have no support in the cited target."
    level: fail
  - scope: passage
    quotes:
      - "[Instructions are typed callables](./instructions-are-typed-callables.md) argues that prompts, skills, and tools share a callable structure with typed inputs and outputs."
    reason: "The target argues that skills, tasks and workflows are callable 'in this limited sense' and can declare document-type signatures. It explicitly says that declaring a signature does not turn those procedures into conventional functions. It does not discuss tools or Python functions sharing that structure. The note cites it for a broader claim (prompts, skills and tools share one callable structure) and then calls it a 'type-theoretic view' that llm-do makes 'practical rather than just analogical'. That stretches the target's scope and strengthens what it claims."
    level: warn
  - scope: passage
    quotes:
      - "[llm-do](https://github.com/zby/llm-do) implements this through a hybrid VM where agents (`.agent` files, LLM-backed) and tools (Python functions) share a single namespace."
    reason: "The llm-do implementation claims rest on an external repository link with no tracked ingest and no paired quotation. The reviewer could not inspect it within this invocation's constraints, so the implementation details (shared namespace, `.agent` frontmatter, imperative scheduler) remain unverified against the source."
    level: info
outcome: fail
---

# Review

Linked library artifacts checked for representation:

- **Prompting changes failure diagnosis with the semantic reference** (FAIL). The note attributes to it a prescription about moving components across the LLM/code boundary in both directions. The target does not make that claim; its subject is how the choice of semantic reference changes failure diagnosis. The footer gloss ("the English account, under which an instruction permits several readings") describes the target more accurately than the body does. The body's attribution, which frames the note's whole problem, is unsupported.
- **Constraining** and **Codification**. These definitions support the note's use: narrowing permitted readings, and moving a rule into symbolic form. The note's gloss "changing medium" is loose but compatible.
- **Spec mining is codification's operational mechanism**. This supports the note's use: extracting observed regularities into deterministic code.
- **Instructions are typed callables** (WARN). The note cites it for a broader view that includes prompts and tools, and for a stronger one ("type-theoretic"), than the target states.
- **Footer-only links** (RLM/Tendril/llm-do, programming practices, relaxing signals). The body uses them for no evidential claim, so they pass as adjacent links.

The external llm-do repository carries the note's implementation claims but is neither ingested nor quoted. It was not inspected here (INFO).
