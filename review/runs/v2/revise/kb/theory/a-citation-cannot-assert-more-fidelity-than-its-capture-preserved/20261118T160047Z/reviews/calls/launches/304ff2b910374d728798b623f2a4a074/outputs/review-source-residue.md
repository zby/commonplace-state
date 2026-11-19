---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "no mechanism here checks that the capture faithfully represents the original or that the named author wrote it"
    reason: "'Here' refers to one particular checking system, the ADR-described implementation. The rest of the sentence reads as a general statement about quote checking. The note claims general scope (its description reads 'Quote checking in general'). The general point is that a capture-identity check does not establish the capture's faithfulness or authorship. Say that, or mark the sentence explicitly as describing the cited implementation."
    level: warn
  - scope: passage
    quotes:
      - "An \"unresolved\" outcome covers recognized quote candidates the checker could not pair with a source. Quotations the extractor never recognized appear in no outcome, and their rate is unmeasured."
    reason: "The bullet uses one implementation's outcome vocabulary ('unresolved') and pipeline component ('the extractor') as if every quote checker had them. In a general note, it should either state the general limit or say whose checker it describes. The general limit is that a checker reports only on candidates it recognizes, so unrecognized quotations escape every outcome. The 'rate is unmeasured' claim applies only to a specific system."
    level: warn
  - scope: passage
    quotes:
      - "A checksum against a recorded capture, with explicit name pairing between citation and file, binds the compared bytes to that capture"
    reason: "Checksums and explicit citation-to-file name pairing are a concrete mechanism from ADR 073. They are presented as how source identity is established, not as one way to establish it. The general requirement, binding the compared bytes to a declared capture rather than to whatever sits at a path, transfers. The specific mechanism could be marked as an example."
    level: info
outcome: warn
---

# Review

## Summary

The title and description claim general scope for quote checking ("Quote checking in general"), and the Scope section says transfer rests on reasoning, not external evidence. Most of the body is phrased generally. It cites ADRs as instances, and the casebook corpus is introduced as "one" corpus, which marks it as an example.

Two passages carry vocabulary from the Commonplace implementation without framing it as an example. "No mechanism here" refers to an unnamed system. The final Scope bullet uses that system's outcome labels and extractor component. Each should be either restated as a general limit or attributed to the cited implementation. The checksum-plus-name-pairing passage is a milder case: the requirement generalizes, but the mechanism is presented as if it were the only one.
