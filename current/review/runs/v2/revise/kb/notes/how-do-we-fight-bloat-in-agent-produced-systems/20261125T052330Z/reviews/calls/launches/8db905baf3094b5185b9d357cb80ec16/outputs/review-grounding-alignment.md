---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "found that naive shortening dropped technical relations while clearer rewrites sometimes added words"
    reason: "The sentence attributes this finding to both linked evidence notes. The three-passes note supports it: the Churchill-and-Zinsser pass shortened the article by 29 words and weakened several technical relations, while the best-ranked pass added 28 words. The two-rewrites note does not report shortening. Its failed first pass was unguarded sentence splitting that lost relations while lengthening the note (+3.7%), and the guarded pass added 4.9%. Citing it for 'naive shortening' misrepresents what that experiment varied: syntactic simplification, not brevity. The supporting route is therefore plausible for one link but not articulated accurately for both."
    level: warn
  - scope: passage
    quotes:
      - "a model can keep all the content while squeezing the wording into denser, harder-to-parse syntax"
    reason: "The two paired verbatim quotes support that AI text overuses processing-difficult features relative to content-preserving round-trip paraphrases, and that a length penalty causes 'divergence from human-like linguistic behavior'. Neither quoted passage establishes that brevity pressure preserves content while changing wording. The first quote is about AI models in general, not under brevity pressure. The second reports linguistic divergence without a content-preservation measure. The note qualifies human reading cost but not this transfer, and the footer repeats it ('distort encoding without cutting content'). The claim is plausible but goes beyond the quoted support without saying so."
    level: warn
  - scope: passage
    quotes:
      - "every retained artifact, copy, or structure must be reconciled when neighboring code or claims change"
    reason: "The linked target concerns capacity to neutralize the risk-weighted inflow of harmful retained artifacts and states that gross artifact volume is only a proxy; the cheap-adoption note explicitly separates that queue from cost accumulated by locally sound structures. Invoking it for maintenance load from every retained artifact is a modest scope extension. It is plausible because unreconciled copies drift into harmful ones, but that route is unstated. It is supporting context in Stakes rather than the note's main claim."
    level: info
outcome: warn
---

# Review

## Summary

Most invoked library artifacts are represented at the scope they claim:

- The determinability note supports leaving determinable choices open.
- The seven-case sweep supports source access displacing exact-fact prose while routing and synthesis survived, and the note keeps its "bounded" scope.
- Reverse compression covers prose inflation and the print-statement code case.
- Cheap adoption covers locally sound additions, weak retirement and the missing trigger after a named target.
- Current-task fit separates reversible adoption from entrenchment.
- The scaling note separates fixed-task absorption from frontier persistence.
- The validity/value-gates note supports the clutter argument.

Two evidential routes are weaker than the page suggests. First, the brevity bullet in Current answer cites two rewrite experiments for "naive shortening dropped technical relations". Only the three-passes experiment involved shortening; the two-rewrites experiment found relation loss from syntactic splitting that lengthened the text. Second, the source-quoted brevity-pressure bullet in Unsettled carries good qualifications on reader cost and conjecture. Its core "keep all the content" claim is still an unarticulated transfer from quotes that show linguistic divergence, not content preservation.

The Stakes use of the maintenance-capacity note is a mild scope stretch and is reported as INFO.
