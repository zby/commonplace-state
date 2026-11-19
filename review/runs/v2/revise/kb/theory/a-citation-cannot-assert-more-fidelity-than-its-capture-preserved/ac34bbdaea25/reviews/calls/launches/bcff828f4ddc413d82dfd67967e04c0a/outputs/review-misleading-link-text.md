---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "and no rival capture design drops the layering while preserving the commitments"
    reason: "The inline link to 'A framework rule with a boundary-preserving rival is not an inherited constraint' is placed as the support for 'The layering is not a design choice'. A reader who does not follow it will think the target gives a way to establish that a rule is inherited once no rival is found. The target's opening paragraph says the opposite: finding no rival leaves the rule 'only undemoted — not proven inherited.' The link text is accurate, but the sentence gives the wrong impression of what the link supports."
    level: warn
  - scope: passage
    quotes:
      - "The one chance here is ingest"
    reason: "The sentence leads the reader to expect a general rule about irreversible loss at capture. The target's head is about production history (how an artifact was made and what was consulted) becoming checkable only at production time. That fits the claim only partly, because this note says lost fidelity can be recovered by re-capture."
    level: info
outcome: warn
---

# Review

I checked all seven link targets: trace-extracted memory, the boundary-preserving-rival rule, derived copy, history has one chance, structure inference, ADR 046 and collection prototypes. All resolve. Most link texts are the target titles, and their sentences match the target heads. The trace-extracted-memory note does place authority in post-capture operations. The derived-copy note does require a mechanical derivation rule. ADR 046 does report the 18-of-87 result. The collection-prototypes page does describe the dialectical/evidential prototype's grounding marker. One link is misleading in context: the boundary-preserving-rival rule is used to support a conclusion that its own test disclaims.
