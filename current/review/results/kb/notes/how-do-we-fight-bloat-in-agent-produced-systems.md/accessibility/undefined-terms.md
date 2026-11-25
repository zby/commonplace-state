---
type: types/review-result.md
format: 2
description: Retained verdict review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/review-gates/accessibility/undefined-terms.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: 901f84fdf556f6aa26c2f135c5ddbad38fd74e06d116a410c9211d1ea637c5ef
criterion: kb/instructions/review-gates/accessibility/undefined-terms.md
criterion-sha256: a29bd905ec12b7a7c8375529e490cfde6711bb4feef5529546a92fda0419af38
outcome: warn
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: 97ca715986f94b258b5f76d768f736d5
completed-at: '2026-11-25T05:24:32Z'
findings:
- scope: passage
  quotes:
  - conventions, links, and routing surfaces that lack static reachability checks
  reason: '"Routing surfaces" is KB-internal vocabulary used in the opening without
    a gloss. A reader outside Commonplace does not know that a routing surface is
    a place (index, catalogue, instruction) that directs an agent to content. The
    next bullet''s "extra routes ... raise lookup cost" gives only a partial hint.
    Add a short inline paraphrase.'
  level: warn
- scope: passage
  quotes:
  - verified doctrine, task intent, and execution evidence
  reason: '"Doctrine" here carries the technical sense of Commonplace doctrine, a
    registered vocabulary term, not ordinary English. It has no gloss and no link
    to its definition. Per this gate, active vocabulary needs an inline gloss plus
    a link on first meaningful mention, or should be replaced with plain wording (e.g.,
    "the KB''s verified rules").'
  level: warn
- scope: passage
  quotes:
  - leaving unknown-name routing and cross-component synthesis
  reason: '"Unknown-name routing" and "cross-component synthesis" name the residual
    documentation roles that survived the sweep. Neither is explained, so the reader
    cannot tell what kind of documentation survived without following the link. A
    short paraphrase would fix this, e.g., pointing a reader to a component whose
    name they do not yet know, and explaining how several components fit together.'
  level: warn
- scope: passage
  quotes:
  - retaining external structure only where frontier difficulty still justifies it
  reason: '"Frontier difficulty" (and the linked title''s "deployment frontier") is
    not defined. The sentence explains fixed-task scaffolding but not what the frontier
    is: tasks at the edge of what current models can do. Without that, the contrast
    that carries the bullet''s point is opaque.'
  level: warn
- scope: passage
  quotes:
  - targets selection bloat in both prose
  reason: '"Selection bloat" is introduced without definition. The parenthetical examples
    that follow ("inflating a compact seed with generic priors", "output-matching
    boilerplate") illustrate it but never say what is being selected. The heading
    term "zero-structure expansion" is partly recoverable from the linked title, "expands
    without adding information", but the body does not state it. This is a minor gap.'
  level: info
contract: verdict
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/97ca715986f94b258b5f76d768f736d5/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/cf470126cb330d60cd56b348/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/97ca715986f94b258b5f76d768f736d5/outputs/review-undefined-terms.md
raw-output-sha256: ee6f92d2f5ea1ed7af5a8c4f11111b0751924a873ec92a950d5fa9a3fe67eabb
---

# Review

Most of the note's technical terms are either standard software vocabulary (dead-code elimination, linters, YAGNI, call graphs, test coverage) or given enough local context to read alone. Examples are value gate, reachability oracle, encoding distortion and structural entrenchment.

Four terms carry argumentative weight but lack an inline gloss: routing surfaces, the technical sense of doctrine, the residual documentation roles from the sweep, and frontier difficulty. Each one makes the reader follow a link or bring KB context to understand the sentence. A brief paraphrase beside each one would resolve the warnings. Selection bloat is a smaller gap because its examples partly carry the meaning.
