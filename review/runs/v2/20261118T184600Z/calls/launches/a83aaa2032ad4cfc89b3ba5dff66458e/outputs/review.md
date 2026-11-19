---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "State the note's central contribution in one sentence, from the title, the description and the opening."
    reason: "The type spec defines `watches` as the parts of the target the gate inspects, and says review freshness hashes only those parts. Test step 1 reads the target's title and description, but the gate declares `watches: [body]`. A stored result would stay fresh after a title or description edit that changes what the central contribution is. Either add `title` and `description` to `watches`, or have step 1 draw the contribution from the body alone."
    level: warn
outcome: warn
---

# Review

## Summary

The draft gate mostly follows the review-gate authoring instructions. Its failure mode names a concrete pattern: a distinction or mechanism stated without a case. Its `## Test` is a self-contained procedure. It reaches PASS or WARN and says outright that it never returns FAIL, which matches the type spec's "Force and warrant" section: FAIL is an escalation signal, and the gate is a detector, not an acceptance authority. INFO appears only as a finding label under PASS. The test names the adjacent gates it must not double-flag and states which artifact kinds it does not apply to. The gate has fail and pass examples, plus a second pass example for wording that is already particular. The test does not rely on contract text kept elsewhere.

One instruction is unmet. The type spec ties `watches` to what the gate actually inspects, because review freshness hashes only the watched parts. Step 1 of the test derives the central contribution from the title and the description as well as the body. The gate declares only `body`, so a title or description edit would not make its results stale.

The gate sits in `kb/work/` and is marked as a draft outside the catalog. Its `gate_id` path is therefore not yet a discoverable catalog location. That is a placement question for promotion and is not judged here.
