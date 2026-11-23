
# Report

Two sentences changed, both within the supplied scope. No links, quoted spans, must-keep claims or relied-on terms were touched.

1. After the 3.11 table.
   - Before: "The compatibility cost falls on identifiable callers: for a particular application we can test its dependencies before deciding to move it."
   - After: "A loss like the removed `getargspec` can be found before moving: for a particular application we can test its dependencies before deciding to move it."
   - Evidence bounding it: the table records one compatibility loss, a removed interface that fails on call. A dependency test can find that kind of loss. The note has no evidence that every compatibility cost falls on callers who can be identified in advance.

2. Closing paragraph.
   - Before: "Those reasons can be checked independently of who offered them."
   - After: "The factual parts of those reasons, such as which work changed, can be checked independently of who offered them; the weighing of whose costs count cannot be checked that way."
   - Evidence bounding it: the note's own section "What analysis can settle" says analysis cannot supply the weights. The library-hours case says the same evidence supports different choices under different commitments. So only the factual reasons can be checked. The next sentence, which says the reasons make a judgment criticizable, stays unchanged and covers the weighing.

Noticed, not applied: nothing else outside the scope.
