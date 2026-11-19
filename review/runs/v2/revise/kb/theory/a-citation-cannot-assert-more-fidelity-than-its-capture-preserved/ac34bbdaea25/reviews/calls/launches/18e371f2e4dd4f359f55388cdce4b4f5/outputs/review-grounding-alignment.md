---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The layering is not a design choice"
    reason: "The note cites 'a framework rule with a boundary-preserving rival is not an inherited constraint' to support the conclusion that layering is not a design choice, alongside the claim that no rival drops the layering. The target says its test 'cuts one way only': finding no rival leaves a rule 'only undemoted — not proven inherited', and certifying inheritance requires a positive derivation from independently stated invariants. The note's route from 'no rival' to 'not a design choice' is the inference the target denies. The adjacent context-window and copyright argument may supply the positive derivation, but the note does not frame it against the framework's stated boundary invariants, and it does not present the rival search."
    level: warn
  - scope: passage
    quotes:
      - "This is the citation-fidelity instance of a general rule"
    reason: "The target 'History has one chance to become checkable' concerns production history, meaning how an artifact was produced. After production it is unrecoverable by a bounded reviewer. The note applies it to source content, which the note itself says is 'recoverable only by returning to the authoritative artifact and capturing again'. The target lists that situation as a boundary: a snapshot 'stays re-checkable against its source URL until that source changes', so verifiability decays rather than vanishing. The fidelity case therefore matches the target's decay boundary more closely than its one-chance claim. Calling it an 'instance' overstates the fit, and the transfer from production history to source content is not articulated."
    level: warn
  - scope: passage
    quotes:
      - "it produces precisely the hand-maintained-and-trusted copy that rule forbids"
    reason: "The derived-copy rule's precondition 1 does say that natural-language summaries lack a derivation rule, so the representation is accurate. However, the linked ADR 046 makes the verbatim mark itself mechanically checked. A paraphrase marked verbatim then fails validation rather than remaining a trusted, unchecked copy. The inference holds for an unchecked marking regime; the note does not say which regime it assumes."
    level: info
  - scope: passage
    quotes:
      - "found eighteen of eighty-seven"
    reason: "The figures match ADR 046's prototype run (63 match, 18 mismatch, 6 unresolved across 87, with no false mismatch on audit). ADR 046 attributes the mismatches mainly to editorial omission and bracketed substitution, not to paraphrases marked verbatim. The footer cites the result as evidence for 'the layering', which ADR 046 does not address."
    level: info
outcome: warn
---

# Review

Linked material checked (title, opening and the relevant interior passage of each):

- **Trace-extracted memory earns authority per operation, not at capture.** The note represents it accurately: the target says authority is earned after capture by operations such as verify, abstract and consult. The note's "complement" framing is a fair contrast and does not stretch the target's scope.
- **A framework rule with a boundary-preserving rival is not an inherited constraint.** This is misrepresented in direction. The target can demote a rule but cannot certify it; the note uses it to certify ("not a design choice"). WARN.
- **A derived copy of recomputable truth must be checked or absent.** The note accurately invokes the mechanical-derivation precondition. The application to verbatim marking leaves out that ADR 046 now checks such marks. INFO.
- **History has one chance to become checkable.** The instance relation is not shown. The target's claim concerns unrecoverable production history, while the note's case is recoverable source content, which falls under the target's own decay boundary. WARN.
- **ADR 046.** The numbers are reported correctly. The extension to "the layering" goes beyond what the ADR covers. INFO.
- **Collection prototypes.** The link is adjacent. The target says only that the dialectical/evidential prototype requires a grounding marker, which matches the link's gloss.

The "epistack casebook work in the sibling `epistack-casebooks` repository" has no link and cannot be checked. It is cited as evidence alongside ADR 046, but this gate can verify only the linked half.

No `kb/sources/` ingests are linked, so no snapshot routes apply.
