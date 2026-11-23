---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself."
    reason: "The opening states that continual learning requires governing behaviour-changing writes, but release engineering also governs such writes. The commitment that distinguishes this note's claim, that the system's own loop does the selecting, appears only in the final paragraph. It follows a form-placement aside and a release-engineering contrast. Moving one plain clause into the opening sentence, such as 'the system's own loop must select, validate, and authorize them', would make the full claim memorable on first read. The current text supports that clause, so this is a placement change, not a new claim."
    level: info
  - scope: passage
    quotes:
      - "Form placement is itself revisable. A stable natural-language rule may be codified, while a brittle symbolic rule may be relaxed back into prose"
    reason: "The last paragraph restates the governance claim, then adds several asides: form-placement revisability, release engineering, selection-based learning, the maintenance discriminator, cadence, and the subproblems governance relates. The form-placement aside belongs with the representational-form paragraph above, and moving it there would let the closing paragraph serve the core claim directly."
    level: info
  - scope: passage
    quotes:
      - "belongs to a consumption path, not to stored bytes"
    reason: "The opening paragraph states the claim in its first two sentences, then introduces the learning criterion, behavioral authority, knowledge artifact, and system-definition artifact before the persistence conclusion. Each definition supports the argument, but together they make the opening read as terminology. Folding the artifact-role distinction into one short clause, with the links kept, would keep the claim in front."
    level: info
outcome: pass
---

# Review

## Summary

The core claim is easy to find. The title states it, and the first two sentences state it plainly. In one sentence: in a deployed system, continual learning requires the system's own loop to select, validate, authorize, and coordinate durable behaviour-changing writes across representational forms; persistence alone does not do this. The later paragraphs serve that claim. They give the deployment constraints (cheap installation and regression validation), the forms a write can touch, and the governance problem.

The note's shape makes the claim less memorable than it could be, so the findings are INFO rather than WARN. The opening sentence leaves out the self-selection condition, which is what separates continual learning from ordinary governed software change. That condition appears only near the end of the final paragraph, among several asides. The simplest fix is to put the self-selection clause in the opening sentence and move the form-placement aside into the representational-form paragraph. Compressing the opening's run of definitions would also help. None of these changes needs a new claim. They only reorder commitments the note already makes.
