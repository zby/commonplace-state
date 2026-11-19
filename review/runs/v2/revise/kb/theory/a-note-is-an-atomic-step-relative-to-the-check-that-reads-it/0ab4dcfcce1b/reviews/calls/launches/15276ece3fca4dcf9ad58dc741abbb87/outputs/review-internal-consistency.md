---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "into a check that costs the reviewer nothing"
    reason: "The closing summary says the validator turns 'this passage says this' into a check that costs the reviewer nothing. Earlier, the note says the reviewer still has the support judgment after quoting ('It costs attention, and nine quoted passages cost more than one'), and that occurrence is not representativeness. The closing sentence is true only if 'says this' means bare occurrence. Read as support, which is how the earlier sections use 'this passage ... this claim', it contradicts them and drops a tension the body keeps."
    level: warn
  - scope: passage
    quotes:
      - "for two reasons that have nothing to do with each other"
    reason: "The opening says the two bounds have nothing to do with each other. The mechanism section later says they are 'independent as constraints but coupled through this remedy', because quoting spends against the co-loading bound. The later qualification is consistent with independence as constraints, but the opening wording is stronger than the body supports."
    level: info
  - scope: passage
    quotes:
      - "The two placements differ in their failure mode, not in the constraint they express."
    reason: "The step-size section then names a second difference: a small artifact-side step buys auditability 'that a well-calibrated reviewer budget does not'. The constraint the two placements express may therefore also differ (a per-note bound versus a per-review reading limit). This may be definition drift and needs the author to confirm."
    level: info
  - scope: passage
    quotes:
      - "They are not atomic steps for the grounding check, because checking one means opening six to nine artifacts"
    reason: "The mechanism section counts only unquoted sources against the step. This paragraph counts every cited source and assumes each must be opened. The two agree only if none of the eight notes quotes its sources, which the paragraph does not say."
    level: info
outcome: warn
---

# Review

The note's main claims are consistent with one another:

- the two bounds are distinct;
- atomicity is relative to a check;
- the grounding check's unit is the unquoted source;
- the artifact-side placement fails loudly;
- N is a convention, while the note leaves its value undecided.

The Scope section matches the body. Calling N "a convention" is consistent with "does not decide N", because the note fixes what kind of number N is, not its value.

The clearest inconsistency is in the closing sentence of the precedent paragraph, which works as a summary of what the knowledge-base case adds. It says the validator makes the common step free for the reviewer. The body instead says that the validator removes the finding step, and that a support judgment remains which costs attention. The other findings concern wording drift that the body partly resolves: the bounds' independence, what differs between the two placements, and how sources are counted in the corpus example.
