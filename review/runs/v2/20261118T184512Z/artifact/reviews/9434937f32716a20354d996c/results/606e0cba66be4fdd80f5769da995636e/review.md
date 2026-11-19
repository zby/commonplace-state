---
type: types/review-result.md
findings:
- scope: document
  quotes: []
  reason: The Test routes WARN, INFO and PASS but never says when to return FAIL.
    The type spec asks for a procedure for choosing PASS, WARN or FAIL. A gate that
    tops out at WARN is compatible with the spec's statement that FAIL is an escalation
    signal, so this is not an unmet instruction. Still, the gate does not say that
    it deliberately caps at WARN, so a reviewer cannot tell an intended ceiling from
    an omission.
  level: info
- scope: passage
  quotes:
  - Draft in kb/work/concrete-cases-for-abstract-notes/. Not in the catalog.
  reason: The type spec says the catalog discovers gates at kb/instructions/review-gates/{lens}/{name}.md
    and that gate_id matches that path. The gate_id names the intended catalog location,
    and the note openly marks itself as a workshop draft. The file therefore does
    not yet take part in the catalog. That is expected for a draft. Promotion should
    move it to kb/instructions/review-gates/semantic/distinction-case-test.md.
  level: info
outcome: pass
description: Retained verdict review of kb/work/concrete-cases-for-abstract-notes/distinction-case-test.md
  against kb/types/review-gate.md
contract: verdict
note: kb/work/concrete-cases-for-abstract-notes/distinction-case-test.md
criterion: kb/types/review-gate.md
note-sha256: d641f215f8fee9f14187984815d61d9f3c4e5b3d8819b592f2e0e1d579bb84b3
criterion-sha256: e1c9e54fabee72f5a5064ffaf36272337fd257fd044de0e4a85de2a9a5b6a6ae
target-sha256: d641f215f8fee9f14187984815d61d9f3c4e5b3d8819b592f2e0e1d579bb84b3
target-capture: kb/reports/state/review/runs/v2/20261118T184512Z/artifact/reviews/9434937f32716a20354d996c/inputs/target/kb/work/concrete-cases-for-abstract-notes/distinction-case-test.md
observation: kb/reports/state/review/runs/v2/20261118T184512Z/artifact/reviews/9434937f32716a20354d996c/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/20261118T184512Z
launch: 606e0cba66be4fdd80f5769da995636e
completed-at: '2026-11-18T18:45:45Z'
raw-output: kb/reports/state/review/runs/v2/20261118T184512Z/calls/launches/606e0cba66be4fdd80f5769da995636e/outputs/review.md
raw-output-sha256: f2d835cfccbb7c2eb6fc287a11ca603fb70d5f172877c008d8a0be201870135b
format: 2
---

# Review

The note follows the review-gate authoring instructions.

**Closed-ended verdict assay.** The note is one Markdown criterion. It tells the reviewer what failure to look for and how to reach a final decision. It is not a report-kind assay. INFO appears only as a finding label: the PASS clause is stated separately, and INFO does not take its place.

**`## Failure mode`.** The section names a concrete pattern. A distinction that reads well in general terms fails on a particular case in one of five ways: a case fits both sides, fits neither, sorts only by an unfixed word, sorts cleanly but yields an unsupported conclusion, or the two sides make no practical difference. This meets the instruction to state "the concrete pattern that should not appear."

**`## Test`.** The six-step procedure tells the reviewer what to copy from the note, which cases to build, how to sort each case using only the criteria the note states, and how to credit a note that handles or excludes the hard case. Decision rules follow for WARN, INFO and PASS. Step 1 also covers notes where the gate does not apply. As the type spec requires, the "Do not flag here" paragraph explicitly names its exceptions against four adjacent gates. The test is self-contained: it relies on no type spec or collection convention outside the gate's own text. Because the gate does not declare `requires_type`, it owes no boundary statement with the conformance pair. Neither recorded finding is an unmet instruction (see the frontmatter).

**Examples.** The note has both `## Example (fail)` and `## Example (pass)`, in the shape the template shows. The pass example reuses the fail case and shows how the note's own text resolves it. This makes the test concrete as the spec intends.

**Force and warrant.** The gate is written as a detector. "Do not repair. Do not propose a new criterion" keeps it to noticing the failure. It claims no blocking authority.
