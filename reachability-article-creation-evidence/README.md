# Reachability article creation evidence

This directory is a replaceable local evidence view for the creation of
`kb/articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md`.
It collects the evidence that was locally available on 2026-09-02. Start with
[`EVIDENCE.md`](./EVIDENCE.md) for the account of what the machinery contributed.

The bundle is intentionally under `kb/reports/cache/`. Its data is ignored by
Git and may be large. The authoritative inputs remain Git objects, the
Commonplace store and review-state directories, and the local Claude and Codex
histories named in the indexes. `collect_evidence.py` regenerates the view from
those inputs without changing the article or the authoritative evidence.

## Contents

- `git/versions/` contains one exact article file for every Git lineage commit,
  in chronological order. `git/version-manifest.tsv` maps each file to its
  commit, historical path, blob, content hash, model trailer, and session URL.
- `git/full-commit-patches/` contains the complete patch for every lineage
  commit, including same-commit changes to navigation, redirects, notes, and
  review records. `git/article-only-history.patch` is the compact article-only
  history.
- `workshops/git-versions/` contains every Git-visible revision of the two
  workshops that refounded and then rebuilt the article.
- `reviews/review-jobs/` contains the sixteen raw review-job directories for
  the two persisted 35-criterion sweeps. `reviews/full-pass/` contains the
  three complete full-pass packets. `reviews/database/` is a JSON and exact
  snapshot export of the relevant Commonplace-store rows. `reviews/cache-reports/`
  preserves the direct connect, friction, and premise-decomposition outputs.
- `sessions/raw/` contains locally available Claude and Codex JSONL sessions
  selected by a historical article path or a Claude session ID recorded in a
  lineage commit. `sessions/session-index.tsv` records provenance, source and
  captured hashes, match terms, and any redaction count.
- `sessions/claude-file-history/` contains the matching editor/file-history
  snapshots found outside Git.
- `github/` contains PR metadata, discussion comments, review summaries, and
  inline review comments for every pull-request number named by a lineage
  commit subject. `collect_github.py` refreshes this network-derived layer.
- `supporting-inputs/` contains collection rules, review-system definitions,
  article-linked notes and sources, and other directly linked inputs. Live
  files are explicitly distinguished from the last Git version of paths that
  have since been retired.
- `MANIFEST.tsv` gives the byte size and SHA-256 digest of every captured file.
  `summary.json` and `collection-results.json` give machine-readable counts.

## Fidelity and limits

Git files, review files, and supporting artifacts are copied byte-for-byte.
Session copies are byte-for-byte unless `session-index.tsv` records a nonzero
redaction count. High-confidence credential-shaped strings are replaced with
`[REDACTED_CREDENTIAL]`; the source path and original SHA-256 remain in the
index so an authorized local operator can verify or re-extract the original.

Session selection is deliberately inclusive. A session qualifies if its raw
JSONL mentions any of the article's five historical filenames or any of the
seven public Claude session IDs present in the article's commit lineage. This
captures direct writing sessions, orchestration sessions, and review workers,
but it can also capture a session that merely loaded or cited an article
version. `EVIDENCE.md` does not treat selection alone as proof that a session
caused a change.

The Git lineage uses `git log --all --follow`; it includes branch and
pull-request-side commits visible in the local object database, not only the
first-parent history of `main`. Repeated article blobs are retained because the
surrounding commit can still carry distinct machinery evidence. The manifest
therefore distinguishes lineage commits from distinct article contents.

External Claude session URLs are recorded, but the main collector uses only
local files and does not claim that every server-side session remained
downloadable. GitHub pull-request evidence is a separate, explicitly
network-derived capture. It is limited to PR numbers named in lineage commit
subjects; it is not an archive of unrelated issues, discussions, actions, or
server-side agent sessions.

## Regeneration

From the repository root:

```bash
python3 kb/reports/cache/reachability-article-creation-evidence/collect_evidence.py
python3 kb/reports/cache/reachability-article-creation-evidence/collect_github.py
```

The collector overwrites derived files at their stable paths and leaves the
human-written `README.md` and `EVIDENCE.md` in place. Review `summary.json` after
regeneration because the article and local session histories may still have
changed.

## Payloads deleted on 2026-11-11

The copied payloads were deleted to keep the ignored report trees small:
`sessions/raw/` and `sessions/claude-file-history/` (428 MB of raw session
logs, which are primary process records and never publishable), `git/versions/`,
`git/full-commit-patches/`, `git/article-only-history.patch` and
`workshops/git-versions/` (all reconstructible from Git objects),
`reviews/review-jobs/`, `reviews/full-pass/`, `reviews/database/` and
`reviews/cache-reports/` (exports of the retired review store, whose originals
are in `../commonplace-archive`), and `supporting-inputs/` (copies of live and
last-Git-version files). What remains is enough to read `EVIDENCE.md` and
verify its counts: the indexes and manifests (`MANIFEST.tsv`,
`collection-results.json`, `summary.json`, `git/version-manifest.tsv`,
`git/lineage-paths.txt`, `git/claude-session-urls.txt`,
`workshops/version-manifest.tsv`, `sessions/session-index.tsv`,
`sessions/file-history-index.tsv`, `sessions/summary.json`,
`reviews/summary.json`), the network-derived `github/` capture and the
collector scripts. Links from `EVIDENCE.md` into the deleted directories no
longer resolve. Regeneration needs the local session histories, which may no
longer exist.
