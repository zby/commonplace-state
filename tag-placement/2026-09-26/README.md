# Tag placement review — 2026-09-26

Status: complete. Review 388 tagged notes under `kb/notes/`, covering 848 assigned tags, against the frozen openings of all 29 heads from the current worktree after commit fe905c66. No note edits are authorized by a reviewer finding.

The Commonplace review pipeline owns 20 jobs (8790–8809), each with captured note and criterion bytes. Fresh gpt-6-sol workers assess each assigned tag as keep, mismatch, or uncertain. Note outcomes are PASS, FAIL, or WARN respectively. Obvious additions are optional INFO findings, not an exhaustive missing-tag audit. The 27 typed artifacts without assigned tags are outside this first sweep; `run.json` lists them explicitly.

- `run.json`: source state, scope, input hashes, frozen catalogue location, and status.
- `selector.json`: the requested pairs used to create jobs.
- `jobs.json`: canonical job paths returned by creation.
- `dispatch.json`: parent scheduling progress.
- `criterion-library/`: retained copy of the run-specific criterion, including tag-head openings.

The command invocation uses the outside-checkout copy named by `library_override` in `run.json`, through COMMONPLACE_LIBRARY_ROOT. This gives the criterion a supported library identity without modifying the shipped gate catalogue. Restore that copy from `criterion-library/` if needed before finalization or freshness checks. Do not delete the run inputs while results still need disposition. Preserve job snapshots and their database state.

The output is an operator review queue. No gate verdict by itself licenses changing tags, and a clean assigned-tag review does not establish that every useful tag is present.

Completed 388 notes / 848 assigned tags: 780 keep, 67 mismatch proposals, 1 uncertain. Canonical note outcomes: 327 PASS, 60 FAIL, 1 WARN. Job 8810 refreshed one concurrently edited note. Final freshness selection is empty and all live placement openings match the frozen criterion. See [operator report](../../../cache/tag-placement/2026-09-26.md) and `aggregate.json`. Thirteen kept-child/rejected-parent conflicts require disposition before retagging.
