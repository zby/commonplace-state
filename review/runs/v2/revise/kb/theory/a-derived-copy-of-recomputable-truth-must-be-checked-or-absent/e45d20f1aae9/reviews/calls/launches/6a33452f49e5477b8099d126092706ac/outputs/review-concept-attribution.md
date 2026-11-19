---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "wants the same value left out, since anything the situation determines goes stale by drift or ignorance"
      - "(safe to pin)"
    reason: "The note identifies its recomputable value with the target's 'situational' class and casts the target's 'arbitrary' class as 'safe to pin'. The target defines a situational choice as one that task intent and live or actively produced execution evidence can distinguish; its 'Search cost and frontloading' section explicitly says to frontload a known value that remains valid for the call and only forbids freezing a situational value that execution evidence could overturn. A value recomputable from a ground-truth source before the call is not situational in that sense. The target's arbitrary class is one no evidence selects, which 'need not be fixed' unless coordination requires one selection, not a class that is 'safe to pin'. The asserted tension between the two notes, and the 'third class between arbitrary and situational', therefore rest on a reading the target does not support."
    level: warn
  - scope: passage
    quotes:
      - "recompute being dear to a model is what makes a checked derived copy worth keeping in the first place"
    reason: "The context phrase attributes to the target the claim that costly model-side recomputation is what makes a checked copy worth keeping. The target (now titled 'LLM recompute cost shifts the store-vs-recompute balance') says expensive model-side derivation 'does not by itself justify persistence' and compares three paths, including external on-demand derivation. Readable as a necessary rather than sufficient condition, so INFO."
    level: info
outcome: warn
---

# Review

Checked identity claims against: indexes-lower-recall (the false copy as the sharpest case of suppressed retrieval matches the target's control-flow mechanism, which it extends to any artifact treated as exhaustive); tracked lineage and the lineage definition (both match); make-like staleness detection (cheap detection plus re-read-and-decide review matches); the text testing framework (Level A deterministic/cheap and Level B LLM rubric graders match); keep-compiled-views-aligned (provenance, regeneration rules and staleness detection match its source-of-truth rules); the tag-readme spec (the `complete` mark as a validated cache, enforced-or-omitted, matches); and the frontloading note (inlining known values to spare execution context matches). All targets resolved.

The one substantive mismatch is the use of the executor-determinability note: the note builds its "third class" on a tension the target already resolves, by placing pre-call recomputable values in the target's situational class.
