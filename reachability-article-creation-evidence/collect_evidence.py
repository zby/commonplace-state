#!/usr/bin/env python3
"""Collect the locally available creation evidence for the reachability article.

The output is deliberately a cache view. Git, the Commonplace store, review
job directories, full-pass packets, and local agent histories remain the
authoritative inputs.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import sqlite3
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[4]
BUNDLE = Path(__file__).resolve().parent
TARGET = "kb/articles/reachability-conjecture-the-llm-stays-fixed-the-software-house-learns.md"
ARTICLE_PATHS = {
    TARGET,
    "kb/articles/the-reachability-conjecture-train-the-house-not-the-llm.md",
    "kb/articles/a-research-program-for-learning-software-factories.md",
}
WORKSHOP_PREFIXES = (
    "kb/work/factory-theory-restart/",
    "kb/work/agentic-system-learning-refoundation/",
)
REVIEW_JOB_IDS = (
    8736, 8745, 8746, 8747, 8748, 8749, 8750, 8751,
    8776, 8777, 8778, 8779, 8780, 8781, 8782, 8783,
)
FULL_PASS_DIRS = (
    "kb/reports/state/full-pass/a-research-program-for-learning-software-factories/20260831T215211Z-db2ad4",
    "kb/reports/state/full-pass/a-research-program-for-learning-software-factories/20260901T221819Z-aa7ecf",
    "kb/reports/state/full-pass/the-reachability-conjecture-train-the-house-not-the-llm/20260902T145819Z-fd6963",
)
CACHE_REPORTS = (
    "kb/reports/cache/connect/articles/a-research-program-for-learning-software-factories.connect.md",
    "kb/reports/cache/connect/articles/the-reachability-conjecture-train-the-house-not-the-llm.connect.md",
    "kb/reports/cache/friction/a-research-program-for-learning-software-factories.friction.md",
    "kb/reports/cache/friction/the-reachability-conjecture-train-the-house-not-the-llm.friction.md",
    "kb/reports/cache/premise-decomposition/a-research-program-for-learning-software-factories.premises.md",
    "kb/reports/cache/premise-decomposition/the-reachability-conjecture-train-the-house-not-the-llm.premises.md",
)
SYSTEM_INPUTS = (
    "AGENTS.md",
    "kb/articles/COLLECTION.md",
    "kb/articles/types/article.md",
    "kb/reports/COLLECTION.md",
    "kb/reports/cache/README.md",
    "kb/reference/README-REVIEW-SYSTEM.md",
    "kb/reference/review-architecture.md",
    "kb/reference/freshness-architecture.md",
    "kb/reference/commands.md",
    "kb/instructions/critique-note.md",
    "properdocs.yml",
    "kb/articles/README.md",
    "kb/index.md",
)
CURRENT_REQUEST_MARKERS = (
    b"we need to record all evidence for how kb/articles/reachability-conjecture",
    b"reachability-article-creation-evidence/collect_evidence.py",
)
SECRET_PATTERNS = (
    re.compile(rb"sk-[A-Za-z0-9]{20,}"),
    re.compile(rb"ghp_[A-Za-z0-9]{20,}"),
    re.compile(rb"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(rb"xox[baprs]-[A-Za-z0-9-]{20,}"),
    re.compile(rb"AKIA[0-9A-Z]{16}"),
    re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
)


def run_git(*args: str, text: bool = True) -> str | bytes:
    result = subprocess.run(
        ["git", *args], cwd=REPO, check=True, capture_output=True, text=text
    )
    return result.stdout


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def write_text(path: Path, data: str) -> None:
    write_bytes(path, data.encode("utf-8"))


def copy_file(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def copy_tree(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)


def parse_lineage() -> list[dict[str, str]]:
    raw = run_git(
        "log", "--all", "--follow", "--format=@@%H", "--name-status", "--", TARGET
    )
    current_path = TARGET
    records: list[dict[str, str]] = []
    for block in raw.split("@@")[1:]:
        lines = [line for line in block.splitlines() if line.strip()]
        commit = lines[0].strip()
        statuses = [line.split("\t") for line in lines[1:]]
        path_at_commit = current_path
        older_path = current_path
        status_text = ""
        for fields in statuses:
            if fields[0].startswith("R") and len(fields) == 3:
                old, new = fields[1], fields[2]
                if new == current_path or old == current_path:
                    path_at_commit = new
                    older_path = old
                    status_text = "\t".join(fields)
                    break
            elif len(fields) == 2 and fields[1] == current_path:
                path_at_commit = fields[1]
                status_text = "\t".join(fields)
                break

        meta = run_git(
            "show", "-s",
            "--format=%H%x1f%P%x1f%an%x1f%ae%x1f%aI%x1f%s%x1f%B", commit,
        ).rstrip("\n")
        fields = meta.split("\x1f", 6)
        if len(fields) != 7:
            raise RuntimeError(f"Unexpected metadata for {commit}")
        record = {
            "commit": fields[0],
            "parents": fields[1],
            "author": fields[2],
            "email": fields[3],
            "date": fields[4],
            "subject": fields[5],
            "body": fields[6],
            "path": path_at_commit,
            "status": status_text,
        }
        try:
            record["blob"] = run_git("rev-parse", f"{commit}:{path_at_commit}").strip()
            record["content"] = run_git("show", f"{commit}:{path_at_commit}")
        except subprocess.CalledProcessError:
            record["blob"] = ""
            record["content"] = ""
        records.append(record)
        current_path = older_path
    return records


def export_git_evidence(records: list[dict[str, str]]) -> set[str]:
    git_dir = BUNDLE / "git"
    versions = git_dir / "versions"
    commits_dir = git_dir / "full-commit-patches"
    versions.mkdir(parents=True, exist_ok=True)
    commits_dir.mkdir(parents=True, exist_ok=True)

    chronological = list(reversed(records))
    titles: set[str] = set()
    manifest_rows: list[dict[str, str | int]] = []
    for ordinal, record in enumerate(chronological, start=1):
        content = record["content"]
        version_name = ""
        if content:
            date = record["date"][:10].replace("-", "")
            version_name = f"{ordinal:04d}-{date}-{record['commit'][:12]}.md"
            write_text(versions / version_name, content)
            title_match = re.search(r"^# (.+)$", content, re.MULTILINE)
            if title_match:
                titles.add(title_match.group(1).strip())

        patch = run_git("show", "--format=fuller", "--stat", "--patch", record["commit"])
        write_text(commits_dir / f"{ordinal:04d}-{record['commit']}.patch", patch)

        public_sessions = ";".join(sorted(set(re.findall(
            r"Claude-Session:\s*(https://claude\.ai/code/session_[A-Za-z0-9]+)",
            record["body"],
        ))))
        models = ";".join(sorted(set(re.findall(r"(?m)^Model:\s*(.+)$", record["body"]))))
        manifest_rows.append({
            "ordinal": ordinal,
            "commit": record["commit"],
            "parents": record["parents"],
            "date": record["date"],
            "author": record["author"],
            "email": record["email"],
            "path": record["path"],
            "status": record["status"],
            "blob": record["blob"],
            "content_sha256": sha256_bytes(content.encode()) if content else "",
            "version_file": f"versions/{version_name}" if version_name else "",
            "subject": record["subject"],
            "models": models,
            "public_sessions": public_sessions,
        })

    with (git_dir / "version-manifest.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(manifest_rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(manifest_rows)

    history = run_git(
        "log", "--all", "--follow", "--date=iso-strict", "--format=fuller",
        "--stat", "--patch", "--", TARGET,
    )
    write_text(git_dir / "article-only-history.patch", history)
    write_text(
        git_dir / "lineage-paths.txt",
        "\n".join(dict.fromkeys(record["path"] for record in records)) + "\n",
    )

    all_bodies = "\n".join(record["body"] for record in records)
    session_urls = sorted(set(re.findall(
        r"Claude-Session:\s*(https://claude\.ai/code/session_[A-Za-z0-9]+)", all_bodies
    )))
    write_text(git_dir / "claude-session-urls.txt", "\n".join(session_urls) + "\n")
    return titles


def export_workshop_evidence() -> None:
    raw_paths = run_git(
        "log", "--all", "--format=", "--name-only", "--",
        "kb/work/factory-theory-restart", "kb/work/agentic-system-learning-refoundation",
    )
    paths = sorted({
        line.strip() for line in raw_paths.splitlines()
        if line.strip().startswith(WORKSHOP_PREFIXES)
    })
    out = BUNDLE / "workshops" / "git-versions"
    rows: list[dict[str, str | int]] = []
    ordinal = 0
    for path in paths:
        commits = run_git("log", "--all", "--reverse", "--format=%H", "--", path).splitlines()
        for commit in commits:
            try:
                blob = run_git("rev-parse", f"{commit}:{path}").strip()
                content = run_git("show", f"{commit}:{path}")
            except subprocess.CalledProcessError:
                continue
            ordinal += 1
            rel_dir = Path(path).relative_to("kb/work")
            name = f"{ordinal:04d}-{commit[:12]}-{Path(path).name}"
            dest = out / rel_dir.parent / name
            write_text(dest, content)
            rows.append({
                "ordinal": ordinal,
                "commit": commit,
                "path": path,
                "blob": blob,
                "content_sha256": sha256_bytes(content.encode()),
                "captured_file": str(dest.relative_to(BUNDLE)),
            })
    (BUNDLE / "workshops").mkdir(exist_ok=True)
    with (BUNDLE / "workshops" / "version-manifest.tsv").open(
        "w", encoding="utf-8", newline=""
    ) as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def export_review_evidence() -> dict[str, object]:
    reviews = BUNDLE / "reviews"
    for job_id in REVIEW_JOB_IDS:
        source = REPO / f"kb/reports/state/review-jobs/review-job-{job_id}"
        copy_tree(source, reviews / "review-jobs" / source.name)
    for rel in FULL_PASS_DIRS:
        source = REPO / rel
        copy_tree(source, reviews / "full-pass" / Path(rel).relative_to("kb/reports/state/full-pass"))
    for rel in CACHE_REPORTS:
        source = REPO / rel
        if source.exists():
            copy_file(source, reviews / "cache-reports" / Path(rel).relative_to("kb/reports/cache"))

    store = REPO / "kb/reports/state/commonplace-store.sqlite"
    connection = sqlite3.connect(store)
    connection.row_factory = sqlite3.Row
    placeholders = ",".join("?" for _ in ARTICLE_PATHS)
    jobs_query = f"""
        SELECT DISTINCT j.*
        FROM review_jobs j JOIN review_pairs rp USING(review_job_id)
        WHERE rp.note_path IN ({placeholders})
        ORDER BY j.created_at, j.review_job_id
    """
    pairs_query = f"""
        SELECT rp.*
        FROM review_pairs rp JOIN review_jobs j USING(review_job_id)
        WHERE rp.note_path IN ({placeholders})
        ORDER BY j.created_at, rp.review_job_id, rp.pair_ordinal
    """
    jobs = [dict(row) for row in connection.execute(jobs_query, tuple(sorted(ARTICLE_PATHS)))]
    pairs = [dict(row) for row in connection.execute(pairs_query, tuple(sorted(ARTICLE_PATHS)))]
    write_text(reviews / "database" / "review-jobs.json", json.dumps(jobs, indent=2) + "\n")
    write_text(reviews / "database" / "review-pairs.json", json.dumps(pairs, indent=2) + "\n")

    snapshot_ids = sorted({
        value
        for pair in pairs
        for value in (pair["reviewed_note_snapshot_id"], pair["reviewed_criterion_snapshot_id"])
        if value is not None
    })
    snapshot_meta = []
    for snapshot_id in snapshot_ids:
        row = connection.execute(
            "SELECT * FROM artifact_snapshots WHERE snapshot_id = ?", (snapshot_id,)
        ).fetchone()
        if row is None:
            continue
        item = dict(row)
        content = item.pop("content_text")
        suffix = Path(item["artifact_path"]).suffix or ".txt"
        name = f"{snapshot_id}-{item['content_sha256'][:16]}{suffix}"
        write_text(reviews / "database" / "artifact-snapshots" / name, content)
        item["captured_file"] = f"artifact-snapshots/{name}"
        snapshot_meta.append(item)
    write_text(
        reviews / "database" / "artifact-snapshots.json",
        json.dumps(snapshot_meta, indent=2) + "\n",
    )

    baseline_query = f"""
        SELECT * FROM current_review_freshness_baselines
        WHERE note_path IN ({placeholders})
        ORDER BY note_path, criterion_path, model_partition
    """
    baselines = []
    for row in connection.execute(baseline_query, tuple(sorted(ARTICLE_PATHS))):
        item = dict(row)
        item.pop("baseline_note_text", None)
        item.pop("baseline_criterion_text", None)
        baselines.append(item)
    write_text(reviews / "database" / "freshness-baselines.json", json.dumps(baselines, indent=2) + "\n")
    connection.close()

    outcomes = Counter(pair["outcome"] or "report" for pair in pairs)
    summary = {
        "article_paths_with_persisted_reviews": sorted({pair["note_path"] for pair in pairs}),
        "review_job_count": len(jobs),
        "review_pair_count": len(pairs),
        "outcomes": dict(sorted(outcomes.items())),
        "artifact_snapshot_count": len(snapshot_meta),
        "full_pass_count": len(FULL_PASS_DIRS),
        "cache_report_count": sum((REPO / rel).exists() for rel in CACHE_REPORTS),
    }
    write_text(reviews / "summary.json", json.dumps(summary, indent=2) + "\n")
    return summary


def redact_if_needed(data: bytes) -> tuple[bytes, int]:
    redactions = 0
    for pattern in SECRET_PATTERNS:
        data, count = pattern.subn(b"[REDACTED_CREDENTIAL]", data)
        redactions += count
    return data, redactions


def export_session_evidence(records: list[dict[str, str]], titles: set[str]) -> dict[str, object]:
    sessions = BUNDLE / "sessions"
    capture_cutoff = datetime.fromisoformat(records[0]["date"])
    lineage_terms = sorted({Path(record["path"]).name for record in records})
    public_session_ids = sorted(set(re.findall(
        r"session_[A-Za-z0-9]+", "\n".join(record["body"] for record in records)
    )))
    search_terms = [term.encode() for term in lineage_terms + public_session_ids]

    roots = (
        ("claude", Path("/home/zby/.claude/projects/-home-zby-llm-commonplace")),
        ("codex", Path("/home/zby/.codex/sessions/2026/08")),
        ("codex", Path("/home/zby/.codex/sessions/2026/09")),
    )
    selected: dict[Path, tuple[str, Path, bytes]] = {}
    for platform, root in roots:
        if not root.exists():
            continue
        for source in root.rglob("*.jsonl"):
            try:
                data = source.read_bytes()
            except OSError:
                continue
            if any(marker in data.lower() for marker in CURRENT_REQUEST_MARKERS):
                continue
            timestamp = re.search(rb'"timestamp":"([^"]+)"', data[:100_000])
            if timestamp:
                started = datetime.fromisoformat(timestamp.group(1).decode().replace("Z", "+00:00"))
                if started > capture_cutoff:
                    continue
            if any(term in data for term in search_terms):
                selected[source] = (platform, root, data)

    desired_destinations = {
        sessions / "raw" / platform / source.relative_to(root)
        for source, (platform, root, _data) in selected.items()
    }
    raw_root = sessions / "raw"
    if raw_root.exists():
        for stale in raw_root.rglob("*.jsonl"):
            if stale not in desired_destinations:
                stale.unlink()

    rows = []
    redaction_rows = []
    for source in sorted(selected):
        platform, root, original = selected[source]
        copied, redaction_count = redact_if_needed(original)
        rel = source.relative_to(root)
        destination = sessions / "raw" / platform / rel
        write_bytes(destination, copied)
        matches = [term.decode() for term in search_terms if term in original]
        row = {
            "platform": platform,
            "source_path": str(source),
            "captured_file": str(destination.relative_to(BUNDLE)),
            "source_bytes": len(original),
            "source_sha256": sha256_bytes(original),
            "captured_sha256": sha256_bytes(copied),
            "redactions": redaction_count,
            "selection_terms": ";".join(matches),
        }
        rows.append(row)
        if redaction_count:
            redaction_rows.append(row)

    with (sessions / "session-index.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    write_text(sessions / "redactions.json", json.dumps(redaction_rows, indent=2) + "\n")

    history_root = Path("/home/zby/.claude/file-history")
    history_rows = []
    title_terms = [title.encode() for title in titles]
    if history_root.exists():
        for source in history_root.rglob("*"):
            if not source.is_file():
                continue
            try:
                data = source.read_bytes()
            except OSError:
                continue
            if b"type: kb/articles/types/article.md" not in data:
                continue
            if not any(term in data for term in title_terms):
                continue
            copied, redaction_count = redact_if_needed(data)
            rel = source.relative_to(history_root)
            destination = sessions / "claude-file-history" / rel
            write_bytes(destination, copied)
            history_rows.append({
                "source_path": str(source),
                "captured_file": str(destination.relative_to(BUNDLE)),
                "source_bytes": len(data),
                "source_sha256": sha256_bytes(data),
                "captured_sha256": sha256_bytes(copied),
                "redactions": redaction_count,
            })
    if history_rows:
        with (sessions / "file-history-index.tsv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(history_rows[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(history_rows)

    summary = {
        "raw_session_count": len(rows),
        "raw_session_source_bytes": sum(row["source_bytes"] for row in rows),
        "redacted_session_count": len(redaction_rows),
        "redaction_count": sum(row["redactions"] for row in rows),
        "claude_file_history_snapshot_count": len(history_rows),
        "session_start_cutoff": capture_cutoff.isoformat(),
        "public_claude_session_ids_from_commits": public_session_ids,
    }
    write_text(sessions / "summary.json", json.dumps(summary, indent=2) + "\n")
    return summary


def export_supporting_inputs(records: list[dict[str, str]]) -> dict[str, object]:
    supporting = BUNDLE / "supporting-inputs"
    paths = set(SYSTEM_INPUTS)
    markdown_link = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")
    repo_path = re.compile(r"(?m)^\s*-\s+(kb/[^\s]+\.md)\s*$")
    for record in records:
        content = record["content"]
        for match in markdown_link.finditer(content):
            target = match.group(1)
            if "://" in target or target.startswith("#"):
                continue
            resolved = (REPO / Path(record["path"]).parent / target).resolve().relative_to(REPO.resolve())
            paths.add(str(resolved))
        paths.update(repo_path.findall(content))

    copied = []
    historical = []
    missing = []
    for rel in sorted(paths):
        source = REPO / rel
        if source.is_file():
            destination = supporting / "live-checkout" / rel
            copy_file(source, destination)
            copied.append({
                "path": rel,
                "captured_file": str(destination.relative_to(BUNDLE)),
                "sha256": sha256_bytes(source.read_bytes()),
            })
        else:
            recovered = False
            for commit in run_git("log", "--all", "--format=%H", "--", rel).splitlines():
                try:
                    content = run_git("show", f"{commit}:{rel}")
                    blob = run_git("rev-parse", f"{commit}:{rel}").strip()
                except subprocess.CalledProcessError:
                    continue
                destination = supporting / "historical-last" / rel
                write_text(destination, content)
                historical.append({
                    "path": rel,
                    "last_available_commit": commit,
                    "git_blob": blob,
                    "captured_file": str(destination.relative_to(BUNDLE)),
                    "sha256": sha256_bytes(content.encode()),
                })
                recovered = True
                break
            if not recovered:
                missing.append(rel)
    write_text(supporting / "manifest.json", json.dumps({
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "semantics": "Live-checkout snapshots at collection time; not necessarily the historical revision used by a particular edit.",
        "files": copied,
        "historical_last_available_files": historical,
        "unrecoverable_paths": missing,
    }, indent=2) + "\n")
    return {
        "live_captured": len(copied),
        "historical_last_available_captured": len(historical),
        "unrecoverable": len(missing),
    }


def write_bundle_manifest() -> dict[str, object]:
    excluded = {"MANIFEST.tsv", "summary.json"}
    rows = []
    for path in sorted(BUNDLE.rglob("*")):
        if not path.is_file() or path.name in excluded:
            continue
        data = path.read_bytes()
        rows.append({
            "path": str(path.relative_to(BUNDLE)),
            "bytes": len(data),
            "sha256": sha256_bytes(data),
        })
    with (BUNDLE / "MANIFEST.tsv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    summary = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "bundle_file_count_excluding_manifest_and_summary": len(rows),
        "bundle_bytes_excluding_manifest_and_summary": sum(row["bytes"] for row in rows),
        "manifest_sha256": sha256_bytes((BUNDLE / "MANIFEST.tsv").read_bytes()),
    }
    write_text(BUNDLE / "summary.json", json.dumps(summary, indent=2) + "\n")
    return summary


def main() -> None:
    records = parse_lineage()
    titles = export_git_evidence(records)
    export_workshop_evidence()
    review_summary = export_review_evidence()
    session_summary = export_session_evidence(records, titles)
    supporting_summary = export_supporting_inputs(records)
    pre_manifest = {
        "article_lineage_commit_count": len(records),
        "article_lineage_distinct_blob_count": len({r["blob"] for r in records if r["blob"]}),
        "article_lineage_paths": list(dict.fromkeys(r["path"] for r in records)),
        "article_titles": sorted(titles),
        "reviews": review_summary,
        "sessions": session_summary,
        "supporting_inputs": supporting_summary,
    }
    write_text(BUNDLE / "collection-results.json", json.dumps(pre_manifest, indent=2) + "\n")
    print(json.dumps(write_bundle_manifest(), indent=2))


if __name__ == "__main__":
    main()
