---
type: types/review-result.md
format: 2
description: Retained report review of kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
  against kb/instructions/critique-note.md
note: kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
note-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
criterion: kb/instructions/critique-note.md
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews
launch: 2854965b24b149008e0ab04215ff1110
completed-at: '2026-11-18T16:04:04Z'
findings:
- scope: passage
  quotes:
  - A citation cannot assert more fidelity than its capture preserved
  - Unchecked, that assertion rests on the author's word.
  reason: 'The title states a universal limit on what a citation can assert, but the
    opening paragraph says a citation''s assertion of exact wording is made by the
    author and can exceed anything checked. The body''s actual claim is narrower:
    a check can establish fidelity only relative to the evidence it compared. Rename
    the claim so the title says what a check can establish or a reader can rely on,
    not what a citation can assert.'
- scope: passage
  quotes:
  - 'The binding stops at the capture: no mechanism here checks that the capture faithfully
    represents the original or that the named author wrote it.'
  reason: The capture-bounded limit is local to the mechanisms 'here' (a checksum
    pin of one capture). Sources signed by their author or publisher, content-addressed
    or versioned originals, and agreement among independent captures can carry evidence
    about the original and its attribution beyond one capture. The title generalizes
    past this hedge. Either name these mechanisms as outside the claim, or state that
    the limit holds for a single-capture check and that corroboration or signatures
    move the bound, not remove it.
- scope: passage
  quotes:
  - Checking against verified source extracts avoids judging a paraphrase of a paraphrase.
  reason: A verified extract is exact in wording but is itself a selection; the note's
    own excerpt paragraph says excerpts can omit the context needed to judge use.
    Checking support against extracts therefore avoids paraphrase compounding but
    can inherit selection loss. The sentence should carry that condition.
contract: report
target-sha256: 5bd25a2d9c50c0e46dda61815e0a6dffc5483866bf01c603f83ba973ed830a23
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/73bb276589149b3284dd6260/inputs/target/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/artifact/reviews/73bb276589149b3284dd6260/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved/20261118T160047Z/reviews/calls/launches/2854965b24b149008e0ab04215ff1110/outputs/review.md
raw-output-sha256: a9f201b10e1c065f12f05e4035dbbab99c1411eef28a1c28fb93149484f109e5
attack-outcome: partially lands
---

# Critique: A citation cannot assert more fidelity than its capture preserved

**Note:** kb/theory/a-citation-cannot-assert-more-fidelity-than-its-capture-preserved.md
**Central commitment:** A quote check establishes only that the quoted words occur, under a stated normalization rule, in the specific evidence it compared, so a passing citation is no more faithful to the original than the capture it was checked against.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

Two objections reinforce each other.

First, the title is false as worded, and the note's first paragraph shows why. A citation is a speech act by its author. It asserts whatever its author claims: exact wording, attribution and implied faithful context. The note says this directly: "Unchecked, that assertion rests on the author's word." So citations routinely *assert* more fidelity than any capture preserved. What the body defends is a different claim: a *check* can *establish* fidelity only relative to the evidence it used ("A pass means 'agrees with the evidence this check used'"). The title confuses what is asserted with what can be verified. A reader who retrieves the note by its title gets a claim that the first paragraph contradicts.

Second, even the corrected claim ("a verified citation cannot establish more fidelity than its capture preserved") is a universal that a digital-provenance practitioner would reject. That practitioner might come from web archiving (Memento, multiple independent archives), content-authenticity work (signed manifests in the C2PA style, PGP-signed releases) or scholarly versioning (DOIs and versioned preprints with publisher hashes). In their view, fidelity to the original and attribution to an author are not bounded by one capture. Three mechanisms carry evidence past it:
- **Author or publisher signatures.** A signature over the bytes binds them to a key holder, so a check against a signed capture establishes attribution, the question the note says no mechanism answers.
- **Independent corroboration.** Two or more captures taken independently, by different parties at different times, that agree on the passage give evidence about the original that exceeds any one of them.
- **Content-addressed or immutable originals.** When the original itself is identified by hash, a capture that matches the hash *is* the original's bytes, so the capture-to-original gap closes.

On this view the note has presented a feature of its own mechanism, a checksum pin of one local capture, as a law about citations.

## How the note engages it

**Partially engaged.** On the second objection, the body is careful where the title is not. It limits the gap to "no mechanism *here*", lists attribution as a separate question that an identity check answers only "in part", and scopes transfer beyond agent-operated KBs as resting on reasoning alone. These hedges make the body consistent with the provenance practitioner's position: the body never claims that signatures or corroboration cannot close the gap; it simply does not use them. The title and the universal framing ("cannot") remove that hedge. The note names none of the three mechanisms, so a reader cannot tell whether the claim is "this system's checks stop at the capture" (true and well argued) or "no check can exceed its capture" (false for signed or content-addressed sources).

On the first objection, the note does not engage at all. Paragraph 1 distinguishes asserting from making the assertion falsifiable, which is exactly the distinction the title collapses.

The core mechanism survives: the separation of four questions, the "pass is relative to its evidence" principle, unverified-not-passed for missing bytes, and the location-versus-occurrence argument. The attack lands on the title's scope and wording, not on the body's reasoning.

## Constructive findings

- Retitle so the claim is about what a check establishes, for example "A quote check verifies fidelity only to the evidence it compared". The current title is contradicted by the note's own opening.
- In "Which evidence a pass is relative to", name the mechanisms that can carry evidence past one capture: author or publisher signatures, content-addressed originals and agreement among independent captures. Then say either that they are out of scope or that they move the evidential bound rather than abolish it. That turns the local "here" into an explicit, inspectable boundary.
- Qualify the closing sentence about verified source extracts: extracts avoid paraphrase compounding but can inherit the selection loss described two paragraphs earlier.

## Secondary objections (optional)

- "Wording agreement is deterministic, cheap and binary" holds only once a normalization rule is fixed. The next section shows that choosing the rule involves judgments about meaning (case, emphasis, typography). The sentence could say "binary given a fixed normalization rule", so it does not suggest that the wording question is free of judgment.
- The description emphasizes quote checking in general, while the title emphasizes the capture limit. The four-question decomposition, arguably the note's most reusable contribution, does not appear in the title. Retrieval by the decomposition may miss the note.
