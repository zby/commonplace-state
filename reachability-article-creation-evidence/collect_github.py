#!/usr/bin/env python3
"""Capture GitHub PR evidence named by the local article lineage."""

from __future__ import annotations

import csv
import json
import re
import subprocess
from pathlib import Path


BUNDLE = Path(__file__).resolve().parent
OUT = BUNDLE / "github"
REPOSITORY = "zby/commonplace"


def gh(*args: str) -> object:
    result = subprocess.run(
        ["gh", *args], check=True, capture_output=True, text=True
    )
    return json.loads(result.stdout)


def main() -> None:
    rows = list(csv.DictReader(
        (BUNDLE / "git/version-manifest.tsv").open(encoding="utf-8"), delimiter="\t"
    ))
    numbers = sorted({
        int(number)
        for row in rows
        for number in re.findall(r"#(\d+)", row["subject"])
    })
    OUT.mkdir(parents=True, exist_ok=True)
    index = []
    errors = []
    for number in numbers:
        try:
            pr = gh(
                "pr", "view", str(number), "--repo", REPOSITORY,
                "--json",
                "number,title,url,state,isDraft,author,body,createdAt,updatedAt,closedAt,mergedAt,baseRefName,headRefName,commits,comments,reviews,files",
            )
            inline_comments = gh(
                "api", "--paginate", f"repos/{REPOSITORY}/pulls/{number}/comments"
            )
            payload = {
                "pull_request": pr,
                "inline_review_comments": inline_comments,
            }
            destination = OUT / f"pr-{number}.json"
            destination.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
            index.append({
                "number": number,
                "title": pr["title"],
                "url": pr["url"],
                "state": pr["state"],
                "mergedAt": pr.get("mergedAt"),
                "comments": len(pr.get("comments", [])),
                "reviews": len(pr.get("reviews", [])),
                "inline_review_comments": len(inline_comments),
                "captured_file": destination.name,
            })
        except (subprocess.CalledProcessError, json.JSONDecodeError, KeyError) as error:
            errors.append({"number": number, "error": str(error)})
    (OUT / "index.json").write_text(json.dumps({
        "repository": REPOSITORY,
        "selection": "PR numbers in article-lineage commit subjects",
        "pull_requests": index,
        "errors": errors,
    }, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "requested": len(numbers),
        "captured": len(index),
        "errors": len(errors),
        "comments": sum(item["comments"] for item in index),
        "reviews": sum(item["reviews"] for item in index),
        "inline_review_comments": sum(item["inline_review_comments"] for item in index),
    }))


if __name__ == "__main__":
    main()
