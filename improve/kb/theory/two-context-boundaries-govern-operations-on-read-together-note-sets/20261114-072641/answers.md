---
type: reports/types/improvement-run-answers.md
description: Five findings the fix-findings run left open on the two-context-boundaries note, each with the change that would act on it and the agent's view
note: kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md
items:
- id: '1'
  atom: kb/instructions/review-gates/prose/source-residue.md
  kind: edit
  proposal: In the description, replace "connect" with "candidate discovery", so that it reads "with consequences for areas, candidate discovery, and whole-KB work".
  where: Frontmatter description
  agent-note: I think the finding is right and the replacement is safe; the body already uses "candidate discovery" as its general term. Left open because the fix procedure sends description edits to their own procedure, and a description is the note's retrieval surface. Fairly sure.
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  state: pending
  applied-in: null
- id: '2'
  atom: kb/instructions/review-gates/prose/proportion-mismatch.md
  kind: edit
  proposal: Compress the library/workshop consequence to its operational claim plus one clause naming ADR 003 as the historical case, removing the ADR biography, the three-bullet strategy and the quality-scores paragraph; use the space to develop the regime above the index boundary.
  where: '### Library/workshop separation keeps index-scan discovery viable; ## Three operational regimes'
  agent-note: 'I think the proportion finding is right: the section is the longest in the note and is mostly history. The collection review makes the same point as an INFO finding. Left open because it removes material and adds new argument about the top regime, which is a structural change and not a framing fix. What the top regime should say is the author''s to write. Sure about the diagnosis, not about the replacement text.'
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  state: pending
  applied-in: null
- id: '3'
  atom: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
  kind: edit
  proposal: 'Where "collection" is introduced, state its relation to the areas note''s "area": either the same read-together set under another name, with "an area" dropped from the list of instances, or a broader concept of which an area is one kind, with what separates an area from other collections.'
  where: Second paragraph of the opening
  agent-note: I think the finding is right, and the reviewer says the choice is the author's. It decides the scope of the model and what the note contributes beyond the areas note, so it is a claim-level choice. I lean to the broader-concept reading, because the paragraph lists a query result and a whole small KB, which the areas note does not call areas. Not sure.
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  state: pending
  applied-in: null
- id: '4'
  atom: kb/instructions/review-gates/semantic/grounding-alignment.md
  kind: edit
  proposal: Narrow the library/workshop consequence from "keeps index-scan discovery viable" to "delays the index boundary", in the heading and the first paragraph, and add that ADR 025 records the curated collection outgrowing a usable complete-index read.
  where: '### Library/workshop separation keeps index-scan discovery viable'
  agent-note: 'I checked ADR 025: its Context says ADR 003''s bet that curation and portioned loading would keep index-first discovery viable no longer holds. The note cites ADR 025 only as supersession, so the narrower claim is the accurate one. Left open because it weakens a claim in a heading, which is the argument and not its framing. It interacts with item 2: if that section is compressed, this narrowing should be made in the compressed text. Fairly sure the finding is right.'
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  state: pending
  applied-in: null
- id: '5'
  atom: kb/theory/COLLECTION.md
  kind: edit
  proposal: Change the footer label of the quality-scores note from "extends" to "contrasts", with a context phrase that names it as a candidate-evaluation limit beside this note's loading limits.
  where: Relevant Notes, third entry
  agent-note: 'I think the label is wrong as the finding says: the body itself calls it "a related limit". The reviewer offers "contrasts" or "mechanism"/"enables", and which relation the note means is the author''s choice. If item 2 removes the quality-scores paragraph from the body, the footer entry is the only mention left and its label matters more. Fairly sure about "contrasts".'
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  state: pending
  applied-in: null
---

# Open items

Five findings were left open. Items 2 and 4 concern the same section and should be decided together: if the library/workshop consequence is compressed, the narrowing of its claim belongs in the compressed text.
