---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - This query stays open as long as bloat control relies on periodic manual sweeps
    and ad-hoc restraint
  reason: The notes contract says a note serves a recognizable occasion with 'No further
    work or promotion is expected', and routes material that still serves an investigation
    to kb/work/. This note declares itself an open standing query with an Unsettled
    agenda. The Current answer section is usable as written, so the placement is defensible,
    but the note's open-investigation framing sits in tension with the collection's
    finished-reply purpose. The note should either state its occasion as a finished
    reply (for example, a reply to the recurring question of how Commonplace controls
    bloat) or have the collection contract name standing queries explicitly.
  level: warn
- scope: passage
  quotes:
  - Empirically, agents default to additive changes
  reason: The contract requires a link to the evidence for factual examples. This
    sentence asserts an empirical pattern but links no source, log entry, report or
    evidence note. Readers cannot inspect what supports it.
  level: warn
- scope: passage
  quotes:
  - An unconfirmed conjecture in `kb/log.md`
  reason: The note points to the log entry as plain code text, not as a link to the
    specific entry. Linking it would make the reference resolvable. This is minor
    because the note marks the conjecture as unconfirmed.
  level: info
outcome: warn
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/notes/COLLECTION.md
contract: verdict
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
criterion: kb/notes/COLLECTION.md
note-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
criterion-sha256: 4e28fa28099a5eceaece18aa0d3c0e610964838c3b0acd8ed5ca0591717bbb60
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/3376095e90d34334b3ace3cc9c784f94/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/3619d2fb655b1f26bf1755b5/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 3376095e90d34334b3ace3cc9c784f94
completed-at: '2026-11-25T05:25:47Z'
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/3376095e90d34334b3ace3cc9c784f94/outputs/review.md
raw-output-sha256: dab266391bf0f6055f49aa5c305905f3dc8351d2dd55cea080c00581ee5c6ae3
format: 2
---

# Review

## Summary

The note mostly follows the `kb/notes/` contract. Its title is the question a reader would look up. Its description separates it from the companion valuation query by naming bloat in mixed code and prose. The body works without the conversation that produced it. It links to existing theory and doesn't rebuild it: each Current answer bullet summarises a theory note in a sentence or two and links it. The borrowed quotations are attributed to the ingested source. The outbound footer uses only the labels the contract allows: `see-also` points to notes and theory, including `theory/evidence/`, and `evidenced-by` points to a source.

Two conventions are not fully met.

1. **Placement.** The contract describes finished pieces for which no further work is expected, and it sends live investigations to `kb/work/`. This note calls itself a standing query that stays open, which pulls against that purpose. The Current answer section can stand as a usable reply, so the placement is not wrong. The tension still needs to be resolved, either in the note's framing or in the contract.
2. **Evidence for factual claims.** The Unsettled section says agents add things by default rather than delete or consolidate, and presents this as an empirical fact without linking any evidence. A smaller issue: the note mentions a `kb/log.md` conjecture without linking to it.
