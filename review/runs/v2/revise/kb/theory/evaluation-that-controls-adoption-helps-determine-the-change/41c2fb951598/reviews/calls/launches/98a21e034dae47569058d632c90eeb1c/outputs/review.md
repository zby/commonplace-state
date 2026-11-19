---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["Adoption continues if the maintainer does nothing, but the specified review goes undone. Calling the whole process automated would conceal an omitted task."]
    reason: "THIN — The inference treats the process specification as the boundary of \"the whole process\". Under an executed-process reading, \"automated\" is accurate: nothing waits on a person. The note does not argue why the specification sets the boundary. It also does not separate a concealed omitted task from a requirement that has been retired without announcement. Its own later taxonomy (\"ceased to be required\") counts that second case as a change in requirements, so the example could describe either one. The joint holds only if the specification is still authoritative, and the note leaves that condition unstated."
  - scope: passage
    quotes: ["A claim of full automation must say which tasks it preserves and which requirements it retires."]
    reason: "THIN — The preceding sentence shows that removing a wait and removing a specified task are different changes. That difference does not by itself establish the normative \"must\". The note also needs to show that a reader of an automation claim would otherwise misread which change occurred. Support for that comes only later, from the weekly-review example, which inherits the specification-boundary gap above. \"Full automation\" is also unscoped at this point: is the claim about adoption or the wider process? The scope is narrowed only later (\"A claim about automated adoption alone need not include monitoring or revision\"), so the opening obligation reads broader than the argument supports."
  - scope: passage
    quotes: ["Using an optional study's available findings does not itself require future studies. Making a new human assessment a condition of each revision does."]
    reason: "HOLDS — The claim is narrow (\"does not itself require\") and true by the note's definitions. It leaves one case open. A revision process designed to consume such findings may lose quality when the studies stop, without formally requiring them. That is a dependency of performance, not of execution. The scope bullet (\"not every human influence\") partly covers this case, so the joint holds, but it is where a skeptical reader would push."
  - scope: passage
    quotes: ["Optional assessment creates neither when the process can proceed without it and its specification does not require it."]
    reason: "HOLDS — The conclusion follows because the conditions restate the two definitions just given. No wait exists because the process can proceed. No unfulfilled requirement exists because the specification does not require the assessment. The joint is sound but nearly definitional. It classifies an assessment once its status is known, but it does not help a reader tell whether an assessment is optional."
  - scope: passage
    quotes: ["Repeated acceptance does not settle that choice"]
    reason: "HOLDS — The note delegates this inference to its linked note, which supplies the mechanism. Routine approvals may never have met the exceptional case, or the operator may have approved without checking. So a history of approvals cannot show whether the check should be kept, automated or retired."
outcome: report
---

# Friction check: Removing approval waits can leave required human evaluation in place

**Central claim (one sentence):** Removing a blocking human approval wait is a different change from automating or retiring a specified human evaluation task, so a full-automation claim must say which human tasks remain and which requirements were dropped.

## Filter
**Filter:** SURVIVES

The note holds three properties at once: a blocking dependency (a wait), an unfulfilled requirement (a specified task left undone while execution continues) and optional assessment (neither of the first two). They are defined on two independent axes: whether execution blocks and whether the specification requires the task. They can coexist, and the two hypothetical cases instantiate distinct cells. The note also keeps the usefulness or necessity of a task out of scope, which avoids the tempting conflation of "required" with "needed". Concretization does not split the claim.

## Thinnest joints

The two thinnest joints share one gap. The note's distinction between waits and requirements is clean. Its normative step, that a full-automation claim must report retained tasks and retired requirements, depends on the specification being treated as authoritative for what "the process" is. The weekly-review example is the only grounding for the "conceal" inference. The opening "must" leans on that example. Neither says why a reader should prefer the specification-relative reading over an executed-process reading. Neither distinguishes an omitted task from a requirement that was retired without announcement. The remaining three joints hold under the skeptical default. One is narrowly scoped, one is close to definitional, and one is supported by its linked note. They rank lower for that reason, not because the ranking required a weak rating.

## For the human
Look first at "Calling the whole process automated would conceal an omitted task". State why the specification, rather than executed behavior, fixes what "the process" is. Also say how an omitted task differs from a quietly retired requirement.
