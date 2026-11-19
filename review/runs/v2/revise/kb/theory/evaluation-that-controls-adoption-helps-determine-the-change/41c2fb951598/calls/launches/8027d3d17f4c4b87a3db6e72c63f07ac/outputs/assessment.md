# Assessment: Removing approval waits can leave required human evaluation in place

**Proposed purpose** (the operator named none): A KB maintainer or agent who reads or makes a claim that a process is automated can tell whether a human wait was removed, a specified human task still remains, or a requirement was retired, and so can state what the claim covers.

## Decision

Stop. The highest-value changes are a change to the claim and a restructuring of the argument. Passes do not make either change. No passes are planned.

1. **The normative claim is missing a condition (claim-level; route: rewrite).** The note says "A claim of full automation must say which tasks it preserves and which requirements it retires" and "Calling the whole process automated would conceal an omitted task." Both depend on the process specification being authoritative for what "the process" is. The note never states that condition. It does not say what separates a live requirement from stale text, or whether a specification that the automated process can edit itself still counts. The critique (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/critique-note.md`) proposes adding that condition and tying the "conceal" charge to it. The composition-friction report rates both joints THIN for the same reason (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/composition-friction-gate.md`). This changes what the note claims, so the passes cannot do it. Cost: a rewrite of the opening and of "Name the process being automated".
2. **Unwritten tasks are handled asymmetrically (claim-level; route: rewrite or operator scope decision).** Scope counts a habitual, unwritten *wait* as a dependency. On the task side the note recognises only *specified* tasks, so a relied-on but unwritten weekly check is classed as optional assessment. The critique and the premise decomposition (`kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/premise-decomposition-gate.md`) both raise this. Premise decomposition also says conditional, exception-path waits fit neither side cleanly; the note's own rollback example is one. Each repair either adds a scope limit or classifies a new case, and that is the operator's claim decision. Cost: one or two Scope bullets, possibly a paragraph.
3. **The three roles are not presented as one classification (restructuring).** The note works with three roles: an actual wait, a specified task and optional assessment. It presents them as two overlapping contrasts, and the positioning paragraph frames the thesis differently from the title (synthesis, `kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/synthesis`). The synthesis leaves to the author which contrast is the thesis. That is a restructuring of the argument and depends on items 1–2, so a pass over the current text would be replaced. Cost: reordering the opening and both sections.
4. **The necessity caveat is repeated four times (readability-and-flow / fix-strategy-taxonomy).** This is worth doing only after the rewrite. Both marginal-value findings (the hedge after the weekly-review example and the closing restatement in the revision paragraph) are local cuts against the current text. Cost: two sentence cuts and one shortened Scope bullet.
5. **Title qualifiers (opening-and-title, after the rewrite).** "approval" narrows the title more than the argument does: the body covers non-binding and habitual waits (load-bearing-qualifiers finding). "required" reads as "necessary" in an index, which the body disclaims (critique). The title change reaches `kb/theory/README.md`, whose entry repeats the title (role report, `kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/role`). Cost: the title, the description and the index entry.

**Sentence a hostile reviewer would attack first:** "Calling the whole process automated would conceal an omitted task." Ordinary usage scopes "automated" to the execution path, and the note does not say why the specification rather than executed behaviour sets the boundary of the process.

**What reads well:** The wait-versus-specified-task distinction is clean and well bounded, and the two hypothetical cases, together with the boundary cases about non-binding recommendations and mechanically applied human-authored rules, make it concrete.

## Overclaim candidates: support or divergence

- "A claim of full automation must say which tasks it preserves and which requirements it retires." — **support**; it may be narrowed to wider-process claims under an authoritative specification. The rewrite owns this.
- "Calling the whole process automated would conceal an omitted task." — **support**; it may be narrowed by the condition in item 1.
- "Removing a human approval wait and removing a specified evaluation task are different changes." — **divergence**; must be kept.
- "A specified task can remain undone while execution continues." — **divergence**; must be kept.
- "The process depends on human intervention even if the maintainer always approves." — **divergence**; must be kept.
- "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review." — **divergence**; must be kept.

## Stale qualifications (operator questions, not passes)

- The file name `evaluation-that-controls-adoption-helps-determine-the-change` asserts a different claim from the title "Removing approval waits can leave required human evaluation in place" (critique, secondary). Rename through `commonplace-relocate-*`, committed alone, after the title is settled.
- The frontmatter description leads with "automating or retiring a specified evaluation task" and "optional assessment", which gives the optional-assessment contrast equal standing with the wait contrast. Re-check it once item 3 picks the thesis.

## Findings not acted on in this run

- `kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/kb/instructions/compression-bundle/marginal-value-redundancy.md` (warn): valid, but its passages sit inside text the rewrite will replace. Re-review after the rewrite.
- `kb/reports/state/review/results/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md/semantic/load-bearing-qualifiers.md` (warn): widening "approval" to "waits" in the title changes the headline claim. It also interacts with the critique's request to make "required" visible. Decide it together with the rewrite. The "evaluation" item is INFO and needs no action.

## Rewrite route

`commonplace-review run rewrite kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md --commission FILE`. Prepare the commission with `cp-skill-write-multistage`. It should cover the specification-authority condition, the classification of unwritten and exception-path tasks, the three-role structure and the title's "approval" and "required". The only dependent is the index entry in `kb/theory/README.md`.
