# Report state

## Repository and backup scope

Public repository: <https://github.com/zby/commonplace-state>. Check it out
at `kb/reports/state/` inside a Commonplace checkout. It is an independent
repository, not a submodule; the main repository ignores its payloads.

This repository excludes `stochastic-operation-testing/`, subprocess
`stdout.log` and `stderr.log` files, and the validation marker owned by the
main repository. Excluded files may remain locally but are not backed up here.
Native harness session stores are outside this repository too. A clone does
not therefore contain every trace needed to replay or audit a historical run.

## Retention policy

Operational state of Commonplace workflows. The main repository ignores every
payload here to keep it out of the library's record: a failed candidate would
look like an ingest to search, presence in the main tree would read as
endorsement, and every run would dirty the tree and mix with library history.
Being ignored does not make the material disposable or local to one machine.
Each producing workflow owns authority, integrity and cleanup for its
directory; Git ignore status never licenses deletion. The
[reports collection](../COLLECTION.md) sets the class rules.

This README is tracked by the state repository, not by the main repository,
which ignores it. The validation marker beside it,
`.commonplace-validation-ignore`, is tracked by the main repository and
ignored by the state repository; it tells the main repository's validator to
skip this tree.

## What a reader should assume

Everything here is unreviewed model output or workflow bookkeeping, kept so
that work can continue and be inspected. Presence does not endorse content.
Expect failed candidates, stopped runs and records from methods that have
since changed. No library file in the main repository depends on anything
here, and nothing here records which main-repository commit it belongs to.

## Directories

| Directory | Owner | Holds | Lifetime |
|---|---|---|---|
| `review/results/` | `commonplace-review` | one result per reviewed (note, criterion) pair: the judgment and the hashes of the exact texts judged | until a later review of the pair replaces it or it is removed as orphaned; deleting one makes the pair eligible for review again |
| `review/packets/` | `commonplace-review` | each note's current full-pass packet with its disposition and the resolution of a pending hand-back; `commonplace-review decisions` reads them as part of the operator-decision record | until a later pass replaces it; preserve while work is unresolved |
| `review/runs/` | `commonplace-review` | one directory per sweep (`<UTC stamp>/`) or per full pass and revision (`<workflow>/<note path>/<start-hash prefix>/`): call records, operator answers and accepted artifacts; `commonplace-review decisions` reads the operator answers as the operator-decision record | replay inside the run; a run continues only from a checkout at the path its records name. Freshness never reads runs, so check continuation needs before removing one |
| `fixes/` | the [fix system](../../instructions/FIX-SYSTEM.md) | one `<note-stem>.fix-report.md` per fixed note, mapping each warning to its disposition | until the fix system retires the report |
| `ingest/` | `commonplace-ingest-handoff` | one working directory per open ingest: the handoff record and the candidate of its last drafting run; a record without an outcome marks a run that stopped midway | `prune` deletes published runs; keeping finished runs is provisional, see the [workshop case](../../work/decision-lifecycle-evidence/ingest-working-directory.md) |
| `connect/` | `cp-skill-connect` | one discovery report per artifact, `<collection>/<artifact-name>.connect.md`, listing candidate connections | a paid judgment read once by the agent drafting or improving the artifact; no freshness accounting, so an input change leaves it silently outdated. Remove when no ongoing work or decision depends on it; rerun replaces it |
| `critique/` | the [critique pass](../../instructions/critique-note.md) | one adversarial critique per note | read once and acted on; remove like a connect report, or promote to `retained/` when it becomes standing context |
| `friction/` | the [composition-friction gate](../../instructions/composition-friction-gate.md) | one friction report per note, read by the full pass | a paid judgment the next full pass regenerates; remove when no pass or decision depends on it |
| `premise-decomposition/` | the [premise-decomposition gate](../../instructions/premise-decomposition-gate.md) | one premises report per note, read by the full pass | as `friction/` |
| `promotion-candidates/` | `commonplace-promotion-candidates` | one ranking report per collection | deterministic from the current checkout; delete freely and rebuild |
| `multistage/` | [`cp-skill-write-multistage`](../../instructions/cp-skill-write-multistage/SKILL.md) and the [literature-disposition assessment](../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) | one run per artifact, `multistage-write-<short-topic>-<YYYYMMDD>/`: brief, original, source reconstruction, candidate, independent reviews, repairs and, for assessments, source comparisons and dispositions | kept; closure no longer removes the run. Deleting one loses the reviews and reconstruction behind a promoted or abandoned artifact, which main's history does not carry ([ADR 129](../../reference/adr/129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md)) |
| `revise-autoreason/` | [`cp-skill-revise-autoreason`](../../instructions/cp-skill-revise-autoreason/SKILL.md) | one bundle per revision, `<source basename>.<YYYYMMDD-HHMMSS>/`: incumbent, critiques, candidates, audits, blind packets, judgments, ranking and sidecars. Also holds two historical runs from 2026-04-13, made before the skill moved to `kb/work/` | kept; apply and decline no longer delete it. Deleting one loses the critiques, rejected candidates and judgments behind a revision; only the applied text survives in main |
| `staging/` | [article staging](../../instructions/stage-an-article-package.md) and [publication](../../instructions/publish-an-article.md) | one package per staging run, `<slug>/<YYYYMMDD-HHMMSS>/`: inventory, appendices, references, link map and closure check; restaging adds a new timestamped package | kept; publication copies appendix and reference files into `kb/articles/` and leaves the package. Deleting one loses the inventory and closure evidence for a published or abandoned article |
| `agent-memory-landscape/` | [`synthesize-agent-memory-landscape`](../../agentic-systems/instructions/synthesize-agent-memory-landscape/SKILL.md) | one directory per synthesis run, `<YYYYMMDD-HHMMSS>/`: matrix, working query ledger with executed queries and outputs, and draft | kept. Deleting one loses the executed query outputs and drafts; the published synthesis records the matrix hash, so the matrix can be rebuilt from its inputs commit but the run's bytes cannot |
| `snapshot-web/` | `cp-skill-snapshot-web` | capture working directories while a snapshot is being assembled | scratch; empty between captures |

Details of the review state and its freshness rules are in the
[review architecture](../../reference/review-architecture.md) and the
[review system](../../reference/README-REVIEW-SYSTEM.md).

## Leftovers without a current producer

- `tag-placement/`: one tag-placement sweep from 2026-09-26 by a pipeline that
  no longer exists, with its two summary reports.
- `reachability-article-creation-evidence/`: the indexes, manifests and
  collector scripts of the evidence bundle for the reachability article; its
  payloads were deleted on 2026-11-11 and its README says what remains.

Neither is read by current code. They stay until the operator removes them;
removal loses only those runs' records.

## Material moved out of this directory

Until 2026-11-11 a sibling `kb/reports/cache/` held the connect, critique,
friction, premise-decomposition and promotion-candidate reports as a separate
"regenerable" class. The classes were merged here because the outputs are
read the same way and only the promotion ranking is actually rebuildable
([ADR 128](../../reference/adr/128-one-ignored-operational-tree-under-kb-reports-state.md)).

On 2026-11-11 the following went to `../commonplace-archive/kb/reports/state/`,
outside the checkout, keeping their names: the SQLite review stores and their
backups with `review-jobs/`, `reviews/`, `bundle-reviews/` and `full-pass/`
(the system ADR 127 replaced); the 96 run directories of the retired
agentic-analysis method (`agentic-system-analysis/`, minus the source
extractions three runs had made, which were deleted); and the meta-analyser
pilot traces (`meta-analyser-pilot-20261021/`), whose adjudication ADR 121
records. The X likes inbox and its sync state moved to the private snapshots
repository under `kb/sources/.snapshots/x-likes/`, because they hold other
people's posts.

Agentic-system analysis does not yet use this directory. Each analysis runs
in a dedicated worktree and keeps its process record there, under
`kb/agentic-system-analyses/state/<run-id>/`; accepted results integrate into
tracked `retained/` sets. It is the one ignored operational tree outside this
one, recorded as an exception in
[ADR 129](../../reference/adr/129-workflow-run-bundles-live-under-the-state-tree-and-are-kept.md)
until integration copies the process record here. The eight runs under
`kb/agentic-systems/reports/state/` are from an earlier layout and cannot
resume under the current method.
