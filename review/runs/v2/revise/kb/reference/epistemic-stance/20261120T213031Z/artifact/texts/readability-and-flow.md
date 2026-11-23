---
description: "The philosophical tradition Commonplace's assertions assume — Popperian: fallibilism, methodological rules as conventions, anti-essentialism, intersubjective testability — and what it does not inherit"
type: types/note.md
tags: []
---

# Epistemic stance

Commonplace works in the Popperian tradition. Its assertions about claims,
definitions, types and the meaning of instructions are true only under these
four commitments.

1. **Fallibilism.** Claims are conjectures. Observations never establish a
   universal statement. Corroboration is a survived attempt at refutation
   ([Popper, *Logic of Scientific Discovery*](../sources/popper-logic-of-scientific-discovery.ingest.md)).
   Applied in the [theory contract](../theory/COLLECTION.md) and
   [claim modality](./adr/066-claims-declare-modality-in-text-and-passes-repair-mode-mismatch.md).

2. **Methodological rules are conventions** (*Logic of Scientific Discovery*,
   §11). Commonplace treats ADRs, contracts, type specs and definitions as
   such rules. They are adopted by decision and judged by their fruits.
   Unlike the conjectures of point 1, they are not refuted by counterexample.
   They are contested by proposing a better convention.

3. **Anti-essentialism** (*Open Society*, ch. 11; *Poverty of Historicism*,
   §10). The KB does not ask what a term or text really means. A definition is
   a stipulation read right to left: the term labels the definiens. Applied in
   [verifiable document types](../theory/document-types-should-be-verifiable.md)
   and [taxonomies as defaults](../theory/a-universal-knowledge-framework-demotes-content-taxonomies-to-defaults.md).
   Commonplace takes the meaning of an instruction to be the reading that a
   designated reference set of interpreters converges on, under a stated rule
   for when two outputs count as the same answer; see
   [prompting changes failure diagnosis with the semantic reference](../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md).

4. **Objectivity is intersubjective testability** (*Logic of Scientific
   Discovery*, §8), and knowledge lives in artifacts
   ([Popper 1968](../sources/popper-epistemology-without-a-knowing-subject-1968.ingest.md)).
   Applied in the [theory builder](../theory/definitions/theory-builder.md).
   This commitment keeps point 3 from relativism. The reference set is
   chosen, but choosing it does not make its interpreters converge. Whether
   they converge is a fact, and a test can find that they do not.

Commonplace does not inherit the propensity interpretation of probability,
verisimilitude measures, or Popper's political writings beyond their
anti-essentialist argument.

*Open Society* and *Poverty of Historicism* are not ingested. Cite them
without quotes until they are.
