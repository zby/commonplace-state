---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "skip the by-tag `rg` membership search"
    reason: "`rg` is a named tool that the note never identifies. The surrounding words (\"by-tag ... membership search\") show that it is some search command, so the reader knows what kind of thing it is, but not what it is. A brief identification, such as \"a text search with `rg`\", would remove the remaining guess."
    level: info
outcome: pass
---

# Review

## Summary

The note names almost no external systems, tools, people or organizations. The KB itself and its internal artifacts are described functionally, not by proper name. The only named tool is `rg`. Its sentence shows that it performs a membership search, which is enough to know what kind of thing it is. The finding is therefore information only.
