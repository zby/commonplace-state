---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - the two-copy layout is designed in
  reason: 'ADR 027 is cited as the design source for two tracked `AGENTS.md.template`
    copies, with `src/commonplace/_data` serving editable installs. The ADR never
    mentions `AGENTS.md.template`. It designs the opposite arrangement for editable
    checkouts: the wheel `force-include`s canonical root templates into `commonplace/_data/...`,
    and `commonplace-init` ''fall[s] back to the canonical repository path when running
    from an editable source checkout''. The only real files it keeps under `_data/templates/`
    are the user-collection `COLLECTION.md` templates. The ADR is also amended by
    ADR 086. The attributed design is absent from the linked material and incompatible
    with it on the editable-install role, so the fourth instance''s evidential link
    does not hold.'
  level: fail
- scope: passage
  quotes:
  - holistic rework rather than patching
  reason: The linked note claims something conditional and narrower. A compact, refreshable
    whole-picture narrative can replace fragment reconciliation, but only when the
    picture fits within effective context and can be refreshed in time. This note
    cites it as 'the fix' for managed staleness of dependent knowledge in general.
    The transfer from whole-picture narratives to arbitrary dependent artifacts is
    not articulated.
  level: warn
- scope: passage
  quotes:
  - too costly to run always and too noisy to block on
  reason: The text testing framework characterises Level B as 'medium cost, high coverage'
    and lists judge non-determinism as a failure mode. It does not say Level B is
    too costly to run always or too noisy to block on; those are this note's extensions.
    The transfer is plausible and partly supported by the non-determinism item, so
    this is INFO.
  level: info
- scope: passage
  quotes:
  - This is the sharpest case of
  reason: The indexes note presents itself as the index case of this note's broader
    rule, and states its mechanism conditionally, as no prevalence claim. Calling
    the false copy the 'sharpest case' of the indexes mechanism reverses the specialization
    direction. The mechanism invoked (trusted exhaustive claims suppress the retrieval
    that would find more) is represented accurately, so this is INFO.
  level: info
outcome: fail
description: Retained verdict review of kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
  against kb/instructions/review-gates/semantic/grounding-alignment.md
contract: verdict
note: kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
criterion: kb/instructions/review-gates/semantic/grounding-alignment.md
note-sha256: c00c53aa547c9fec40bc86f6e94410169cda037feb81c9f3d5efa9e0cb9e51f5
criterion-sha256: c6c3b904f6e6d17bc67fcfadb2cb091ce62cdfd0bb33ce30cab047914e6c9a4c
target-sha256: e45d20f1aae9a37f7d05cc3f038b8c988ecf738fc0ddf506320b3b4c640420a8
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/ac13369a5fcddd14477eb550/inputs/target/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/artifact/reviews/ac13369a5fcddd14477eb550/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews
launch: 15b9b9e1c3a24f96a8590fa5462d7eb0
completed-at: '2026-11-16T22:22:11Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent/e45d20f1aae9/reviews/calls/launches/15b9b9e1c3a24f96a8590fa5462d7eb0/outputs/review-grounding-alignment.md
raw-output-sha256: 620a40296f27d0c2b40383fe1caf9a84e4a96b65b87b79aabcf9d0d13df3e89c
format: 2
---

# Review

Most evidential links represent their targets accurately:

- The **tag-readme type spec** supports instance 1 directly. It calls `complete` a validator-enforced mark, describes it as a "validated cache" of membership, and states both "recomputable, therefore never load-bearing" and "enforced-or-omitted".
- **ADR 025** did retire committed complete generated listings in favour of build-time materialization.
- The **lineage-recorded-at-the-source** note supplies the forward-lineage, review-topping-out regime the note says it specializes.
- The **link-graph-plus-timestamps** note supplies make-like detection whose recipe is "re-read and decide", which matches the contrast drawn.
- **Frontloading spares execution context** and **fix what the executor can't determine** are represented at their own scope: inlining known values to save hot-path context, and leaving situational, drift-prone choices open.
- **Keep compiled views aligned** does state provenance, regeneration rules and staleness detection for derived memory surfaces.
- **LLM recompute cost** supports the value half: model-side recomputation can make a checked materialization worth keeping.

The FAIL is the fourth instance. ADR 027, cited as the design source for a byte-identical two-copy `AGENTS.md.template` layout, contains no such design. Its stated arrangement for editable installs (fall back to the canonical repository path) contradicts the note's description of `_data` serving editable installs. The duplicated files may well exist, but the cited material does not ground the claim as made. The WARN is the general use of the holistic-rewrite note, which is conditional on a compact, refreshable whole-picture narrative.
