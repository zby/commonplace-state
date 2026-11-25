---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Systems like Commonplace combine **natural language and code**, which adds prose,
    conventions, links, and routing surfaces that lack static reachability checks.
  reason: 'The body focuses on mixed natural-language and code systems such as Commonplace.
    Its stakes, current answer and unsettled items are about prose, conventions and
    the code–prose boundary. The H1 says only "agent-produced systems" and does not
    show that mixed focus. This is a mild scope difference: the body still answers
    the H1''s question, and the description carries the qualifier.'
  level: info
outcome: pass
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/frontmatter/title-body-alignment.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/instructions/review-gates/frontmatter/title-body-alignment.md
note-sha256: 5abe427b7f741c90bfa58aa42a78dddfd8f8cc3a9aef9a29a7af6a8778fe6385
criterion-sha256: de8c42250a2824eafffe5172cc56ff93a0335bd97feeb86ac9e95d7f94441a3d
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/9e4621d985924b9791f602ad3ce4570c/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/bfac76846f3cb9aa17126d25/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 9e4621d985924b9791f602ad3ce4570c
completed-at: '2026-11-25T05:24:05Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/9e4621d985924b9791f602ad3ce4570c/outputs/review-title-body-alignment.md
raw-output-sha256: 09535940b791e0e496f663fc410755ff8f3af05d3d5f3bd17610ca0437ccdb6f
format: 2
---

# Review

## Summary

The H1 asks: "How do we fight bloat in agent-produced systems?" The body answers it as a standing query. The Stakes section explains why bloat compounds. The Current answer section lists five partial countermeasures. The Unsettled section names open problems, including no reachability check for natural language, bloat that crosses the code–prose boundary, missing retirement triggers, brevity distortion and agents' bias toward adding things. Every section deals with fighting bloat in agent-produced artifacts, so there is no claim drift.

There is a small scope difference. The body is mostly about mixed natural-language and code systems, while the H1 is broader. Because the body still answers the H1's question and does not drift to a different question, this is informational only.
