---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "conventions, links, and routing surfaces that lack static reachability checks"
    reason: "\"Routing surfaces\" is KB-internal vocabulary used in the opening without a gloss. A reader outside Commonplace does not know that a routing surface is a place (index, catalogue, instruction) that directs an agent to content. The next bullet's \"extra routes ... raise lookup cost\" gives only a partial hint. Add a short inline paraphrase."
    level: warn
  - scope: passage
    quotes:
      - "verified doctrine, task intent, and execution evidence"
    reason: "\"Doctrine\" here carries the technical sense of Commonplace doctrine, a registered vocabulary term, not ordinary English. It has no gloss and no link to its definition. Per this gate, active vocabulary needs an inline gloss plus a link on first meaningful mention, or should be replaced with plain wording (e.g., \"the KB's verified rules\")."
    level: warn
  - scope: passage
    quotes:
      - "leaving unknown-name routing and cross-component synthesis"
    reason: "\"Unknown-name routing\" and \"cross-component synthesis\" name the residual documentation roles that survived the sweep. Neither is explained, so the reader cannot tell what kind of documentation survived without following the link. A short paraphrase would fix this, e.g., pointing a reader to a component whose name they do not yet know, and explaining how several components fit together."
    level: warn
  - scope: passage
    quotes:
      - "retaining external structure only where frontier difficulty still justifies it"
    reason: "\"Frontier difficulty\" (and the linked title's \"deployment frontier\") is not defined. The sentence explains fixed-task scaffolding but not what the frontier is: tasks at the edge of what current models can do. Without that, the contrast that carries the bullet's point is opaque."
    level: warn
  - scope: passage
    quotes:
      - "targets selection bloat in both prose"
    reason: "\"Selection bloat\" is introduced without definition. The parenthetical examples that follow (\"inflating a compact seed with generic priors\", \"output-matching boilerplate\") illustrate it but never say what is being selected. The heading term \"zero-structure expansion\" is partly recoverable from the linked title, \"expands without adding information\", but the body does not state it. This is a minor gap."
    level: info
outcome: warn
---

# Review

Most of the note's technical terms are either standard software vocabulary (dead-code elimination, linters, YAGNI, call graphs, test coverage) or given enough local context to read alone. Examples are value gate, reachability oracle, encoding distortion and structural entrenchment.

Four terms carry argumentative weight but lack an inline gloss: routing surfaces, the technical sense of doctrine, the residual documentation roles from the sweep, and frontier difficulty. Each one makes the reader follow a link or bring KB context to understand the sentence. A brief paraphrase beside each one would resolve the warnings. Selection bloat is a smaller gap because its examples partly carry the meaning.
