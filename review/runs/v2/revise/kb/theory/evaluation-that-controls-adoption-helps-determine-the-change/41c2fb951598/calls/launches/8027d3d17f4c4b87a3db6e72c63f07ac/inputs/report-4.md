---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
note-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
criterion: kb/instructions/compression-bundle/high-impact-simplification-synthesis.md
criterion-sha256: e9acb7253e030395c44ec88ee557d44b80dbe4be7a31caa6aed890b2d0206478
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/synthesis
launch: b335d1cd7cac4e1da8496b46b613cced
completed-at: '2026-11-17T13:18:39Z'
findings:
- scope: document
  quotes: []
  reason: The note uses three categories (an actual wait, a specified task, and optional
    assessment) but presents them as two overlapping binary contrasts. The opening
    and 'Name the process being automated' contrast a wait with a specified task.
    The positioning paragraph and the first section's cases contrast required human
    work with optional assessment. The positioning paragraph, which also places related-note
    material before the examples, calls the note's distinction 'human work within
    the process' versus 'optional assessment', which differs from the title's wait-versus-task
    framing. A reader must reconstruct the three-way classification and work out which
    contrast is the thesis. A revision could name the three roles once, near the opening,
    and order the sections against that classification. It could move the causal-credit
    boundary and the link to the factory-claim note after the cases or into Scope,
    so that the cases follow the definitions directly.
- scope: document
  quotes: []
  reason: 'The caveat that an unfulfilled specified task does not show the task is
    necessary appears in four places: the opening (''a separate question''), the second
    paragraph (''not by itself evidence that the system would fail or degrade''),
    after the weekly-review example (''not that skipping review causes harm''), and
    in the second Scope bullet (''not evidence that the evaluation is needed''). Each
    repetition interrupts the argument to guard against a misreading the text has
    already ruled out. A revision could state the boundary once, in the second paragraph
    where the terms are defined. It could then remove the sentence after the weekly-review
    example and reduce the Scope bullet to its distinct point: a habitual, unwritten
    wait still counts as a wait.'
contract: report
target-sha256: 41c2fb95159816cf6bc2a4c7308d794bb413549e264e21787f2221a048788cea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/synthesis/artifact/reviews/dadd1152b98ecbec2be9f708/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/synthesis/artifact/reviews/dadd1152b98ecbec2be9f708/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/41c2fb951598/synthesis/calls/launches/b335d1cd7cac4e1da8496b46b613cced/outputs/review.md
raw-output-sha256: 0132b9c7995d322361814f22fa78dc29ef1fd97422769368524cef4157af8787
---

# Simplification synthesis: Removing approval waits can leave required human evaluation in place

The four checks found the core claim easy to find and no branch material that needs removal. Their findings are local. Read together, they point to two structural simplifications. The revision paragraph's closing restatement ("Making a new human assessment a condition of each revision does.") is a local cut and falls below this synthesis's threshold.

## Opportunities

### 1. Make the three-way classification explicit and let the cases follow the definitions

- Location: the opening three paragraphs ("Optional assessment creates neither…"; "This distinguishes human work within the process from optional assessment of its results, rather than deciding who deserves causal credit for an improvement."), together with the sections "The same activity can perform different roles" and "Name the process being automated".
- Reader problem: The note works with three roles: an actual wait (a blocking dependency), a specified task (a requirement that can go unfulfilled), and optional assessment (neither). It does not present them as one classification. The opening and the second section contrast a wait with a specified task. The positioning paragraph and the first section's cases contrast required work with optional assessment. The positioning paragraph's summary ("human work within the process from optional assessment") also differs from the title's wait-versus-task framing. Because this paragraph comes before the examples, the reader meets the third category and a related-note boundary before seeing the cases.
- Direction: Name the three roles once, after the opening claim. Order the sections against them: the first section separates both kinds of required role from optional assessment, and the second separates a wait from a specified task. Move the causal-credit boundary and the factory-claim link after the cases or into Scope. One possible resolution: "An evaluation activity can play one of three roles: an actual wait, a specified task, or optional assessment. Automation claims usually remove only the first."
- Combines: core-claim-obscured (positioning paragraph delays the cases and introduces a third category early), branch-bloat (positioning paragraph classified as a boundary), plus a cross-cutting observation about the two overlapping contrasts.
- Preserve or decide: The author must decide which contrast is the note's thesis. The title and opening favor wait versus specified task. The positioning paragraph and frontmatter description give optional assessment equal prominence. Moving the factory-claim link must keep its specific point: a judgment that the system improved does not show whether human evaluation was required. The marginal-value check found that point is not made elsewhere in the note.

### 2. State the "specified is not necessary" boundary once

- Location: opening ("Whether a specified task is useful or necessary is a separate question."), second paragraph ("not by itself evidence that the system would fail or degrade without the task"), "Name the process being automated" ("This example establishes a gap against the specification, not that skipping review causes harm."), and the second Scope bullet ("It is an actual wait to remove, not evidence that the evaluation is needed to meet a stated requirement.").
- Reader problem: The same guard against a necessity reading appears four times. The later repetitions interrupt the example and the Scope bullet without adding a new limit. They also suggest that the note expects readers to misread its central distinction.
- Direction: Keep the boundary in the second paragraph, where the blocking-dependency and unfulfilled-requirement terms are defined. Decide whether the opening sentence must also keep it. Delete the hedge after the weekly-review example, or fold "against the specification" into "would conceal an omitted task". Reduce the second Scope bullet to its distinct point: a habitual, unwritten wait still blocks automation.
- Combines: detail-overhang (cumulative repeated caveat), marginal-value-redundancy (defensive hedge after the weekly-review example).
- Preserve or decide: The note must still disclaim any claim that specified tasks are necessary. Both checks treated that boundary as load-bearing. The Scope bullet's point about habitual waits is distinct and must survive the compression.
