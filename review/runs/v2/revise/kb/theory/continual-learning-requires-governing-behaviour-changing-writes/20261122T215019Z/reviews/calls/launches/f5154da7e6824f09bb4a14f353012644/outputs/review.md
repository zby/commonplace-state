---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "The Writing Shape asks that the claim's limits be stated under their own `## Scope` heading, omitting it only when no limit is known. This note knows several limits but leaves them in body prose: the applicability condition to deployed systems whose loop must close during deployment; the exclusion of hand-authored incident edits as maintenance rather than continual learning; the remark that a loop need not touch all three forms every time; that parametric plasticity-stability problems persist; and that storage, contextual activation and parametric adaptation remain separate subproblems. Without a Scope section, a rescoping edit has to rewrite the argument, and scope-testing gates cannot find these limits where they look."
    level: warn
  - scope: passage
    quotes:
      - "the addressability axis — the form-level trade space this note defers to"
    reason: "The footer gives several `grounds` edges to 'axes' (reach, addressability, sample efficiency, verifiability) that the body never names or uses. This annotation also says the note defers the form-level trade space to the explicit-retention note, but the body defers it to the representational-form coevolution note. The Writing Shape asks for links where the relationship helps traversal, and these relation glosses misdescribe what the body actually draws on."
    level: info
outcome: warn
---

# Review

The note mostly follows the `note` type's authoring instructions. The title is a strong compressed handle for the claim. The first paragraph states the main claim: continual learning means governing behaviour-changing writes, not only persisting content. The note gives design rationale rather than imperative procedure, and it links densely to adjacent notes, both inline and in a Relevant Notes footer that matches the template's shape.

The unmet instruction is the `## Scope` section. The type spec makes it a requirement whenever a limit is known, so that a later edit can narrow the limits without rewriting the claim. This note knows and states its limits, but only inside the argument. They include the restriction to deployed systems with a loop that closes during deployment, the boundary between continual learning and maintenance, the point that not every update touches all three forms, and the persistence of parametric forgetting problems. Moving these limits into a Scope section would resolve the warning.

A minor traversal issue: several footer annotations describe "axes" that the body does not develop. One annotation also names a different deferral target from the one the body uses. This is informational only.

The `## Open Questions` section is optional and its absence is not a finding.
