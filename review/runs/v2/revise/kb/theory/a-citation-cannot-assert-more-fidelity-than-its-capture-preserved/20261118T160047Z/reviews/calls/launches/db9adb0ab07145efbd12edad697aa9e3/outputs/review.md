---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The binding stops at the capture: no mechanism here checks that the capture faithfully represents the original or that the named author wrote it."
    reason: "DOUBTFUL — Premise (scoped by 'here', but generalised by the description's 'what stays unverified — attribution upstream' and by the title's 'cannot'): a quote check's fidelity and attribution claims cannot reach past the capture it compares against. — Counterexample: a source published with a verifiable signature or content address, such as a signed git tag or release note or an author-signed PDF, keeps that signature in the capture. Checking it against the author's key binds the captured bytes to the named author, so attribution reaches past the capture by a mechanism the capture preserved. The title survives, because the signature is part of what the capture preserved. The general claim that upstream attribution 'stays unverified' does not survive: it holds only for unsigned sources or for this system's mechanisms. — LOCAL: state in Scope that the limit describes unsigned captures and this check's mechanisms, not every possible capture. — instance"
  - scope: passage
    quotes:
      - "Each exact check in a chain, such as capture to extract and extract to note, verifies only its own pair."
    reason: "DOUBTFUL — Premise (universal): exact checks in a chain do not compose, so each verifies only its own pair. — Counterexample: occurrence is transitive. Suppose the extract is one contiguous span that occurs exactly in the capture, and the note's quote occurs exactly in the extract, both under the same idempotent normalization rule. Then the note's quote occurs in the capture, and two passing checks certify the end-to-end wording relation. Composition fails only when the extract is non-contiguous (elided or concatenated), or when the two hops use different normalization rules. Those failure conditions are the real limit. The note's own contrast 'Semantic hops compound instead' already implies exact hops behave differently. The second-hand provenance point stands, because who read which text is a different relation from whether the words occur. — LOCAL: name the conditions under which exact hops compose. — instance"
  - scope: passage
    quotes:
      - "A pass means \"agrees with the evidence this check used\"."
    reason: "DOUBTFUL — Premise (universal): a pass is relative to the evidence the check used. — The opening section defines the check as relative to a span, a resolved source text and a normalization rule, but this sentence and the reuse sentence ('accepting the risk of changes since it ran') name only the evidence. Instance: the shipped rule strips emphasis (ADR 046). If that rule is tightened, a retained pass becomes a mismatch with no change to the source or the capture. So a pass is relative to the evidence and the rule, and a reused result carries the risk that the rule has changed as well as the source. — LOCAL: add the rule to what a pass is relative to. — instance"
  - scope: passage
    quotes:
      - "A string check answers only the wording question."
    reason: "HOLDS — Premise (universal): wording, attribution, context and truth are separable questions, and a string check answers only wording. Hunt: does a uniqueness-in-range requirement answer the context question? No. It fixes which occurrence is meant but does not judge whether the passage supports the citing use, and the note says so ('Uniqueness does not establish that the author intended this occurrence'). No string-level case answered attribution or truth either."
  - scope: passage
    quotes:
      - "Wording agreement is deterministic, cheap and binary, so it can run on every pass."
    reason: "HOLDS — Premise (universal, given a fixed rule): wording agreement is deterministic, cheap and binary. Hunt: candidate extraction is heuristic, so coverage is not deterministic. But extraction comes before the comparison, and Scope concedes its gap ('Quotations the extractor never recognized appear in no outcome'). Very large sources raise the cost of each comparison but keep it linear and mechanical. No defeater for the comparison itself."
  - scope: passage
    quotes:
      - "Too little normalization fails correct quotes on quote marks or whitespace"
    reason: "HOLDS — Premise (universal): normalization can err in both directions, and under-normalization produces false mismatches on correct quotes. The linked ADR 046 states exactly this ('an under-normalized checker would produce false mismatches on correct quotes, which is worse than no check'). Its prototype found the real mismatches dominated by editorial omission, bracketed substitution and case changes, which matches the note's 'mostly'. Hunt for a rule that needs no specification: none was found, because any fixed rule either ignores some difference or does not."
  - scope: passage
    quotes:
      - "Requiring exactly one occurrence, or exactly one complete occurrence inside a checked range, removes ambiguity about which passage the span equals."
    reason: "HOLDS — Premise (universal): uniqueness removes ambiguity about which occurrence the span equals. Hunt: short or formulaic quotes that legitimately repeat will fail uniqueness. That is a cost of the requirement, not a case where the requirement leaves ambiguity, and a checked range is the stated remedy. The note also keeps intent apart from uniqueness."
  - scope: passage
    quotes:
      - "A checksum against a recorded capture, with explicit name pairing between citation and file, binds the compared bytes to that capture"
    reason: "HOLDS — Premise (universal): checksum plus explicit pairing binds the compared bytes to the recorded capture, and equal bytes at an arbitrary path do not. Hunt: hash collision is negligible for a cryptographic digest. Pairing errors are excluded by requiring explicit pairing. No defeater found."
  - scope: passage
    quotes:
      - "Missing bytes therefore report as unverified, never as passed."
    reason: "HOLDS — Premise (normative): when the bytes are absent from the checking environment, the check must report unverified, because a silent fallback would make the outcome depend on undeclared cache state. Hunt: a model's context holding the text looks like an exception, but the note excludes it explicitly, and with reason: that text has no identity binding. No defeater found."
  - scope: passage
    quotes:
      - "Checking current bytes catches a changed or removed passage at the next check, but misses a changed surrounding context when the quoted words survive."
    reason: "HOLDS — Premise (conditional on a later check running): comparing current bytes with a pin detects passage change or removal, but not context change around surviving words. Hunt: if no later check runs, nothing is caught, but the premise already conditions on 'the next check'. A context change that removes the quoted words is caught as removal. No defeater found."
  - scope: passage
    quotes:
      - "Each excerpt can preserve the wording exactly while omitting context needed to judge the quotation"
    reason: "HOLDS — Premise (possibility claim): chunked reading can preserve exact wording while losing the context needed to judge support. Hunt: a fully self-contained quotation needs no surrounding context, but the premise claims only that loss 'can' happen, and ordinary cases such as a quote whose next sentence negates it confirm it."
outcome: report
---

# Premise decomposition: A citation cannot assert more fidelity than its capture preserved

**Register:** claim
**Central commitment (one sentence):** A quote check can certify only that a quoted span occurs, under a stated normalization rule, in the identity-bound evidence the check actually used (usually a capture), so a passing citation establishes wording fidelity no further upstream than that evidence and leaves upstream attribution, contextual support and truth unverified.

## Premises and counterexamples

The commitment consumes three groups of premises:

- **What the check tests.** The four citation questions are separable, a string check answers only wording, and wording agreement is mechanical.
- **What "exact" and "pass" mean.** The normalization rule must be specified. Uniqueness or range removes ambiguity about the occurrence. A pass is relative to the evidence the check used.
- **What the evidence is bound to.** A checksum with explicit pairing binds the bytes to a capture and no further. Missing bytes are unverified. Rechecks catch passage change but not context change. Exact chains verify only their own pairs.

Most premises survived an active hunt, mainly because the note already concedes the cases a hunter would reach first: extractor gaps, untested locators, and context loss when a source is read in chunks.

Three premises are dented. None propagates to the commitment.

- **The upper bound.** The strongest dent is to the claim that attribution cannot be verified past the capture. The body scopes this with "here", but the description generalises it. Signed or content-addressed sources are a checkable counterexample to the general reading. They support the title and contradict the description, because a signature is something a capture can preserve.
- **Exact chains.** The claim that exact chains do not compose overlooks that occurrence is transitive. The note's real point is about non-contiguous extracts and mismatched rules.
- **What a pass is relative to.** The "relative to evidence" section drops the normalization rule from what a pass depends on, although the opening paragraph includes it.

All three repairs narrow or complete a premise. None weakens the commitment.

## For the human

Look first at the attribution premise ("The binding stops at the capture…"). The description promises that "attribution upstream" stays unverified in general, but a signed source's capture can carry attribution. Scope the claim to unsigned captures or to this check's mechanisms.
