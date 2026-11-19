purpose: "Agents and maintainers deciding whether to remove a human approval wait from a KB procedure should be able to tell whether the change only removes a wait or also automates or retires a required evaluation task, and should report which."
must-keep:
  - "A claim of full automation must say which tasks it preserves and which requirements it retires."
  - "Whether a specified task is useful or necessary is a separate question."
  - "Retiring an unnecessary review may be justified, but it is a change in requirements, not automation of that review."
passes:
  - pass: fix-strategy-taxonomy
    scope: "The sentence 'This example establishes a gap against the specification, not that skipping review causes harm.' in 'Name the process being automated'; leave 'Calling the whole process automated would conceal an omitted task.' unchanged (open claim question)."
    finding: kb/reports/state/review/results/kb/theory/removing-approval-waits-can-leave-required-human-evaluation-in-place.md/kb/instructions/compression-bundle/marginal-value-redundancy.md
stop: null
