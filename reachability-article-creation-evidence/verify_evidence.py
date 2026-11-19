#!/usr/bin/env python3
"""Verify hashes and internal counts in the reachability evidence bundle."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path


BUNDLE = Path(__file__).resolve().parent


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    failures: list[str] = []
    source_drift: list[str] = []

    manifest_rows = list(csv.DictReader(
        (BUNDLE / "MANIFEST.tsv").open(encoding="utf-8"), delimiter="\t"
    ))
    for row in manifest_rows:
        path = BUNDLE / row["path"]
        if not path.is_file():
            failures.append(f"missing bundle file: {row['path']}")
            continue
        if path.stat().st_size != int(row["bytes"]):
            failures.append(f"size mismatch: {row['path']}")
        if digest(path) != row["sha256"]:
            failures.append(f"hash mismatch: {row['path']}")

    version_rows = list(csv.DictReader(
        (BUNDLE / "git/version-manifest.tsv").open(encoding="utf-8"), delimiter="\t"
    ))
    for row in version_rows:
        if row["version_file"] and digest(BUNDLE / "git" / row["version_file"]) != row["content_sha256"]:
            failures.append(f"article version mismatch: {row['commit']}")

    session_rows = list(csv.DictReader(
        (BUNDLE / "sessions/session-index.tsv").open(encoding="utf-8"), delimiter="\t"
    ))
    for row in session_rows:
        captured = BUNDLE / row["captured_file"]
        if digest(captured) != row["captured_sha256"]:
            failures.append(f"captured session mismatch: {row['captured_file']}")
        source = Path(row["source_path"])
        if source.is_file() and digest(source) != row["source_sha256"]:
            source_drift.append(row["source_path"])

    review_pairs = json.loads((BUNDLE / "reviews/database/review-pairs.json").read_text())
    review_summary = json.loads((BUNDLE / "reviews/summary.json").read_text())
    if len(review_pairs) != review_summary["review_pair_count"]:
        failures.append("review pair count mismatch")

    summary = json.loads((BUNDLE / "summary.json").read_text())
    if hashlib.sha256((BUNDLE / "MANIFEST.tsv").read_bytes()).hexdigest() != summary["manifest_sha256"]:
        failures.append("manifest digest mismatch")
    if len(manifest_rows) != summary["bundle_file_count_excluding_manifest_and_summary"]:
        failures.append("manifest file count mismatch")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print(
        f"PASS: {len(manifest_rows)} files, {len(version_rows)} lineage versions, "
        f"{len(session_rows)} sessions, {len(review_pairs)} review pairs"
    )
    if source_drift:
        print(f"NOTICE: {len(source_drift)} authoritative session sources changed after capture")


if __name__ == "__main__":
    main()
