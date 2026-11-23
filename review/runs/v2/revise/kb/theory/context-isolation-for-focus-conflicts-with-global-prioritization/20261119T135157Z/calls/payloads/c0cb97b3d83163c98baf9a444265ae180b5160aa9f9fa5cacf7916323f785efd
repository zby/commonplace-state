---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
  against kb/instructions/compression-bundle/marginal-value-redundancy.md
note: kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization.md
note-sha256: 7a6f9106f19b3e96bc06338a1aa5f6ac6eef97041b3db55e50a5b60a31ecceda
criterion: kb/instructions/compression-bundle/marginal-value-redundancy.md
criterion-sha256: a4a481e4011441b80abc2140583e88da024aba95b0b14bbb973dca94c303dbb7
outcome: warn
profile:
  harness: antigravity
  launch-model: gemini-4-neon
  effort: high
model: null
run: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews
launch: 62ec20c7c4bc4a26a73dbf1e5b7616b5
completed-at: '2026-11-19T13:48:11Z'
findings:
- scope: passage
  quotes:
  - 'Three mechanisms in Commonplace illustrate this split at different scales (scoped
    as local design examples, not corroboration that the split outperforms alternatives):'
  reason: 'Defensive redundancy: calling the Commonplace mechanisms illustrations
    already marks them as design examples rather than corroboration, and the absence
    of a controlled comparison is stated again later. Cut the parenthetical and leave
    the lead-in plain.'
  level: warn
- scope: passage
  quotes:
  - '## Scope


    - The conflict requires bounded effective context and a competing workload whose
    combined live state does not fit beside deep task context. On a small, single-thread
    task that fits wholly inside one usable window, isolation is unnecessary and the
    conflict disappears.

    - The claim applies to *relational* prioritization—relative scale, opportunity
    cost, and escalation triage. Purely intrinsic local checks (validation failures,
    hard invariants, explicit stop rules) need no global comparison set and operate
    reliably inside an isolated worker.

    - Separating execution from triage supplies a comparison surface for allocation;
    it does not choose or revise objectives, which remain outside allocation ([open-ended
    knowledge work shares one epistemic layer across roles](./open-ended-knowledge-work-shares-one-epistemic-layer-across-roles.md)).

    - The practitioner account and Commonplace mechanisms cited above explain the
    claim''s origin and illustrate one architectural response; neither supplies a
    controlled comparison measuring execution quality, triage error, or saved operator
    attention.'
  reason: 'This standalone section mostly recaps boundaries and epistemic disclaimers
    already established earlier: bullet 1 repeats the claim-mode condition and its
    direct converse, bullet 2 recaps paragraph 2 and the static-rules/stop-condition
    points, and bullet 4 repeats the inline origin and illustration framing. Delete
    the section and fold its small non-redundant pieces elsewhere: merge the relational-prioritization
    versus intrinsic-local-checks contrast into paragraph 2, fold the objective-choice
    boundary (bullet 3) into the split or residual-friction section, and state the
    lack of a controlled comparison once if needed.'
  level: warn
- scope: passage
  quotes:
  - '## Open Questions


    - What minimal set of scale-bearing local facts lets a wide-shallow triage pass
    separate high-stakes exceptions from low-stakes ones without re-reading deep execution
    context?

    - How much compressed global state (active bottlenecks, tolerances, budgets) can
    be injected into a focused worker''s handoff to improve within-episode branch
    choices before context load degrades task solving?

    - How can a global scan over compressed frontier items prevent tractable, well-specified
    tasks from crowding out harder, higher-stakes bottlenecks without re-introducing
    unbounded assessment cost?'
  reason: Each bullet restates one of the three trade-offs from 'Residual friction
    at the interface' in question form without introducing a new failure mode, boundary,
    or decision criterion. Delete the section; if any open design parameter (such
    as the minimal fact set or handoff context threshold) needs explicit emphasis,
    fold a concise phrase into the corresponding residual-friction bullet.
  level: warn
contract: verdict
target-sha256: d533bfc27666a34d81a20f68d47c9909d4d940766ffb5e4a80255bd0c2bbb2ea
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/62ec20c7c4bc4a26a73dbf1e5b7616b5/inputs/note.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/artifact/reviews/04ea3f843b0e9c5d08076c93/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/context-isolation-for-focus-conflicts-with-global-prioritization/20261119T133929Z/reviews/calls/launches/62ec20c7c4bc4a26a73dbf1e5b7616b5/outputs/review.md
raw-output-sha256: b6ac6a165cc9ac818f9a074ea1fe715527c53244ced795e2e098faa756f685e4
---

# Review

The core argument—the opening tension, the separation between missing context and default-driven failure direction, the narrow-deep versus wide-shallow split, the three-decision unbundling, and the residual interface frictions—earns its space. Marginal-value redundancy is concentrated in one defensive inline caveat and the two trailing sections, which largely recap conditions, disclaimers, and interface trade-offs already established in the body rather than doing new work.

One non-obvious pass worth noting to avoid over-pruning: the paired quotes and causal caveat in the first two failure-mode bullets earn their place. The second Anthropic quote anchors the babysitting analogy directly to multiple Claudes, the second Nostalgebraist quote introduces the broader priority-flattening diagnosis, and the closing remark that the account does not isolate worker behavior from workflow ping defaults supports the section's own distinction between indiscrimination and default-set failure direction rather than acting as defensive armoring.
