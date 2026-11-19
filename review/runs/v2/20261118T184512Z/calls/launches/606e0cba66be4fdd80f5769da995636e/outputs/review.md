---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The Test routes WARN, INFO and PASS but never says when to return FAIL. The type spec asks for a procedure for choosing PASS, WARN or FAIL. A gate that tops out at WARN is compatible with the spec's statement that FAIL is an escalation signal, so this is not an unmet instruction. Still, the gate does not say that it deliberately caps at WARN, so a reviewer cannot tell an intended ceiling from an omission."
    level: info
  - scope: passage
    quotes:
      - "Draft in kb/work/concrete-cases-for-abstract-notes/. Not in the catalog."
    reason: "The type spec says the catalog discovers gates at kb/instructions/review-gates/{lens}/{name}.md and that gate_id matches that path. The gate_id names the intended catalog location, and the note openly marks itself as a workshop draft. The file therefore does not yet take part in the catalog. That is expected for a draft. Promotion should move it to kb/instructions/review-gates/semantic/distinction-case-test.md."
    level: info
outcome: pass
---

# Review

The note follows the review-gate authoring instructions.

**Closed-ended verdict assay.** The note is one Markdown criterion. It tells the reviewer what failure to look for and how to reach a final decision. It is not a report-kind assay. INFO appears only as a finding label: the PASS clause is stated separately, and INFO does not take its place.

**`## Failure mode`.** The section names a concrete pattern. A distinction that reads well in general terms fails on a particular case in one of five ways: a case fits both sides, fits neither, sorts only by an unfixed word, sorts cleanly but yields an unsupported conclusion, or the two sides make no practical difference. This meets the instruction to state "the concrete pattern that should not appear."

**`## Test`.** The six-step procedure tells the reviewer what to copy from the note, which cases to build, how to sort each case using only the criteria the note states, and how to credit a note that handles or excludes the hard case. Decision rules follow for WARN, INFO and PASS. Step 1 also covers notes where the gate does not apply. As the type spec requires, the "Do not flag here" paragraph explicitly names its exceptions against four adjacent gates. The test is self-contained: it relies on no type spec or collection convention outside the gate's own text. Because the gate does not declare `requires_type`, it owes no boundary statement with the conformance pair. Neither recorded finding is an unmet instruction (see the frontmatter).

**Examples.** The note has both `## Example (fail)` and `## Example (pass)`, in the shape the template shows. The pass example reuses the fail case and shows how the note's own text resolves it. This makes the test concrete as the spec intends.

**Force and warrant.** The gate is written as a detector. "Do not repair. Do not propose a new criterion" keeps it to noticing the failure. It claims no blocking authority.
