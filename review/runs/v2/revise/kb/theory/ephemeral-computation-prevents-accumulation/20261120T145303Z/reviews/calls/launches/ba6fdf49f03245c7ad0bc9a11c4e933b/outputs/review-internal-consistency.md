---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "cross-run accumulation fails only when no experience-dependent state survives to affect later work"
      - "artifact discarded + retained useful lesson  -> learning remains possible"
    reason: "Summary/body contradiction: the frontmatter description asserts that cross-run accumulation fails only when no experience-dependent state survives to affect later work (making surviving causal state sufficient to prevent failure), whereas the body treats surviving causal state as necessary rather than sufficient ('learning remains possible' even for a retained useful lesson, and persistent state changes do not imply learning or safety)."
    level: warn
  - scope: passage
    quotes:
      - "Conversely, retaining every script establishes storage, not learning: unused files may change nothing."
      - "A retained natural-language procedure accumulates knowledge without becoming executable code."
    reason: "Internal tension with the note's own causal-use rule: the first passage establishes that retaining an artifact yields storage rather than learning unless later runs use it causally, whereas the second asserts unconditionally that a retained natural-language procedure accumulates knowledge without requiring later causal use."
    level: warn
  - scope: document
    quotes: []
    reason: "Mild terminology drift across sections: the prose shifts between 'cross-run accumulation', 'learning', 'change the second run's behaviour', and 'accumulates knowledge' without separating neutral or harmful behavioral change from improvement, and shifts from 'deployed system' in the opening to an unintroduced 'The house' / 'A house' in lines 26 and 70."
    level: info
outcome: warn
---

# Review

The core causal-isolation argument in `## What must survive` and the boundary conditions in `## Scope` are mutually consistent. However, two passages conflict with the note's own distinction between storage, causal effect, and learning: the frontmatter description compresses a necessity claim into an `"only when"` sufficiency claim, and the retention-vs-codification section treats a retained natural-language procedure as accumulating knowledge without stating the later-causal-use condition insisted on earlier.
