---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The first is a blocking dependency; the second is an unfulfilled requirement"
    reason: "A timed veto window (execution proceeds after a deadline unless a person objects) sits between the two roles. The stated wait criterion, 'prevents execution from proceeding until a person acts', does not strictly fit it, because execution proceeds without any act; nor is it only a specified task, because execution does pause. It can be mapped as a bounded wait, but only with a strained reading of the criterion."
    level: info
outcome: pass
---

# Review

## Summary

The note builds a three-way distinction: an actual wait (a blocking dependency), a specified task (an unfulfilled requirement when undone) and optional assessment (neither). It adds a list of ways a check can change: moved, partly or wholly automated, replaced by a different control, or no longer required. It states that these changes can be combined.

Boundary cases tested against the stated criteria:

- **Simplest instance.** The required-approval case maps cleanly to an actual wait.
- **Unwritten wait.** The Scope section explicitly covers a habitual wait with no written rule as an actual wait.
- **Requirement enforced later.** A specified review enforced only as a precondition of a later revision is covered by the subsequent-revisions paragraph as a dependency of that later process.
- **Hybrid automation.** An automated check that escalates exceptions to a person maps to "partly automated", so the change list covers it.
- **Timed veto window.** Execution pauses for a set period and then proceeds unless someone objects. This case strains the wait criterion as worded and is recorded as INFO.

The taxonomy is short and matches its argumentative role. No case clearly falls outside the claimed coverage.
