---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/frontmatter/description-discrimination.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 67cbbf61daa25d07b853b60b81514a82c51e5241fb64a67523d5bfbc65afaa63
criterion: kb/instructions/review-gates/frontmatter/description-discrimination.md
criterion-sha256: 17cbbd1fca45e6be71ce6750fe85980667f4958045e3610c4bb9378b13702bcf
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 9e4621d985924b9791f602ad3ce4570c
completed-at: '2026-11-25T05:24:05Z'
findings:
- scope: document
  quotes: []
  reason: The description adds scope (code, prose and structural bloat; mixed natural-language
    and code systems) and context (software anti-bloat advice falls short) beyond
    the title, but it names none of the mechanisms the Current answer gives, such
    as retirement paths, value gates or not restating live source. A reader looking
    for those mechanisms could not tell from the description that this note covers
    them. This is optional retrieval value, not a failure.
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/9e4621d985924b9791f602ad3ce4570c/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/b0eba2fcae18c53b08dc0be9/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/9e4621d985924b9791f602ad3ce4570c/outputs/review-description-discrimination.md
raw-output-sha256: fb40bece5ca0b4e2c6cbe7d19247282c48779f70c5a1acc72f8b60e2053723fe
---

# Review

## Summary

The title is a bare question: "How do we fight bloat in agent-produced systems?" The description does more than paraphrase it. It marks the note as a standing query. It widens "bloat" into three kinds: code, prose and structural. It narrows the domain to mixed natural-language and code systems. It also says why the question stays open: software anti-bloat advice falls short there. That scope and context would help an agent pick this note over a general software-bloat note or a note that only covers prose verbosity.

The description could be stronger if it named one or two current mechanisms. It still passes the gate's test, because it does not merely restate the title or say "this note discusses bloat."
