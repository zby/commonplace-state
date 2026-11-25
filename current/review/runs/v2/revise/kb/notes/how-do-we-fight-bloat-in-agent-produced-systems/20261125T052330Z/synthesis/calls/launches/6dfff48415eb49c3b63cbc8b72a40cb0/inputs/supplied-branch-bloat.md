---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/compression-bundle/branch-bloat.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/compression-bundle/branch-bloat.md
criterion-sha256: 1984e1c08f0a39fa170a712fc49d4db74dc06709ba84c1b8e9cc2e3214e6f397
outcome: pass
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 0c5a72854fbb424aaba6c0c00101cbdc
completed-at: '2026-11-25T05:25:46Z'
findings:
- scope: passage
  quotes:
  - An unconfirmed conjecture in `kb/log.md` is that thoroughness pressure paired
    with superficial length pressure produces both failures at once
  reason: 'The brevity-distortion frontier belongs in the query because it bounds
    the Current answer''s ''not word count'' mechanism. But this bullet is now the
    longest in the note: two verbatim source quotes, a caveat about the study''s measurement,
    and a separate log conjecture about paired thoroughness and length pressure. The
    conjecture is a second causal hypothesis with its own evidence needs. It does
    not state the open question itself. The quote-level evidence already sits in the
    linked ingest. The bullet could shrink to the frontier statement plus one citation.
    The conjecture''s right destination is unclear: it could stay in the log, move
    to the linked source analysis, or become a workshop lead. So this is INFO, not
    WARN.'
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/0c5a72854fbb424aaba6c0c00101cbdc/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/caae0b5f042af91dd900a5e7/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/0c5a72854fbb424aaba6c0c00101cbdc/outputs/review.md
raw-output-sha256: 29359f7f1ffe12ca12f89205cb0df10f0039ed213803d53888c8310394eda72d
---

# Review

The note is a standing query. Its main commitment has three parts: why bloat in mixed natural-language and code systems compounds, which partial mechanisms Commonplace uses against it now, and which frontiers keep the query open. Judged by that commitment, nearly all the side material does work for the main claim.

- The three Stakes channels give the reasons the query matters. The retirement condition sets the scope of the query.
- Each Current-answer bullet names a mechanism and links its theory note. The evidence details inside those bullets support the claims they sit beside: the 53 percent documentation sweep and the two tradeoff studies. They are not branches.
- The scaling-absorbs-scaffolding bullet is about retiring structure, so it is on-topic and not an excursion.
- The Unsettled bullets are frontiers of the main question. The additive-bias bullet lists possible causes only to show why the countermeasure is still unknown, so it stays.

The one place where side material gains weight is the brevity-distortion bullet. It supports the query's frontier, but it also carries source quotes and a separate log conjecture that need different evidence. Because the right home for that material is unclear, this is recorded as INFO rather than a rehoming WARN.
