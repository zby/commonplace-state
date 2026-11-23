---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "says components should move between underspecified (LLM-interpreted) and precise (code) semantics as systems evolve — constrain patterns to code, relax rigid code back to LLM"
    reason: "The sentence credits the linked note (prompting-changes-failure-diagnosis-with-the-semantic-reference) with a prescription: components should move in both directions between LLM interpretation and code as systems evolve. The target never makes that claim. It compares two accounts of prompting: programming in a language defined by a model package, and executing English through a fallible interpreter. It explains how the choice of semantic reference changes the diagnosis of a failure. It does not use the term 'underspecified'. It mentions code extraction only as a trade-off to assess, with no bidirectional constrain/relax rule. The English-execution account (an instruction permits a set of behaviors) loosely supports the 'underspecified' half. The note's main premise, that this framing calls for movable boundaries, is not in the target."
    level: fail
  - scope: passage
    quotes:
      - "argues that prompts, skills, and tools share a callable structure with typed inputs and outputs"
    reason: "The target (instructions-are-typed-callables) argues something narrower. Skills, tasks and workflows are callable 'in this limited sense' and declare document-type signatures such as note → connection-report. The target does not discuss tools or prompts generally as sharing a callable structure. It also warns that declaring a signature does not turn a procedure into a conventional function. The note then calls llm-do the operationalisation that makes 'the type-theoretic view practical rather than just analogical'. That claim stretches the target's document-type interface checks into a general neural/symbolic function equivalence that the target explicitly declines to assert."
    level: warn
  - scope: passage
    quotes:
      - "describe the learning mechanisms — narrowing the interpretation space, changing medium"
    reason: "Constraining as 'narrowing the interpretation space' matches its definition, which also counts constraining as learning in Simon's sense. Glossing codification as 'changing medium' is looser. The definition says codification moves a rule into symbolic form, either by rewriting it or by adopting a consumer as the governing reference. In the adoption case the text does not change. The gloss is close enough for a passing reference."
    level: info
outcome: fail
---

# Review

## Summary

I checked every identity claim against its linked target. The spec-mining attribution holds: spec-mining is "discovering that an underspecified spec consistently resolves to one interpretation, then committing to it in code". The target's pattern (watch behavior, extract regularities into deterministic artifacts) supports it. The constraining attribution also holds.

The opening attribution fails. The note's motivating premise comes from a "framing" that the linked note does not state. That note is about the semantic reference and failure diagnosis, not about a boundary that should move in both directions. A reader who follows the link to find the constrain/relax prescription will not find it. The typed-callables attribution overstates its target's scope by adding tools and prompts. It also turns the target's limited, document-typed sense of "callable" into a general equivalence.

The external llm-do repository link makes no identity claim about another note's concept, so it was not checked.
