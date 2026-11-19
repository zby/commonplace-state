# Judge 1

## Candidate 1

**Right:** Frontmatter, links, caveats, and claims are preserved perfectly — this candidate is effectively byte-identical to the original, so fidelity is maximal and nothing was invented, dropped, or altered.

**Wrong:** It offers essentially no editorial contribution. The original has a mild flow issue in the Three Timescales opening (the orthogonality caveat interjects between the table and the core "system-level adaptation" characterization); the candidate declines to address it. A revision pass that produces zero diffs signals either failure to find leverage or excessive timidity. Conservative restraint isn't the same as inaction.

## Candidate 2

**Right:** Reorders the opening so the "system-level adaptation" characterization precedes the orthogonality caveat, which improves flow. Folds the Commonplace-backend aside into the caveat paragraph cleanly. Introduces the constrain/relax cycle earlier, so the Failure Modes callback has a referent. The "That blind spot is the 'missing middle' the title names" sentence ties the section to the title without overreach. Related Work gains a useful framing sentence.

**Wrong:** Drops the "Moving down the table, verification gets cheaper and sharper. Restructured prompts need a human to judge quality; deterministic module tests run in milliseconds and return a boolean." pair — a concrete explanation of the gradient, not filler. Softens the explicit `**TODO:**` callout into ordinary prose, losing an actionable marker. Adds a new `## Summary` heading that wasn't in the original, introducing structural noise. Changes "This note focuses on the verifiability gradient that runs across both" into a claim that "Both mechanisms operate as a constrain/relax cycle" — a subtle reframing of scope.

## Candidate 3

**Right:** Applies the same beneficial reorderings as Candidate 2 (opening flow, Commonplace-backend consolidation, earlier constrain/relax introduction, title-anchoring line, Related Work intro sentence) while retaining the "Moving down the table…" explanatory sentence and the explicit `**TODO:**` callout. No structural headings added. Fidelity on links and frontmatter is intact.

**Wrong:** Shares Candidate 2's subtle reframing from "This note focuses on the verifiability gradient" to "Both mechanisms operate as a constrain/relax cycle" — a light claim shift, though the constrain/relax cycle is already present in Failure Modes so the reframing is defensible. Otherwise the improvements are all conservative.

RANKING: 3, 1, 2
