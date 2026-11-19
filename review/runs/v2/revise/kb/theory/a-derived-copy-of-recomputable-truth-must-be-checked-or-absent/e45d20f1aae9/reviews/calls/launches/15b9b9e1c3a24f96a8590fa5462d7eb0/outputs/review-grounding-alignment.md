---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "the two-copy layout is designed in"
    reason: "ADR 027 is cited as the design source for two tracked `AGENTS.md.template` copies, with `src/commonplace/_data` serving editable installs. The ADR never mentions `AGENTS.md.template`. It designs the opposite arrangement for editable checkouts: the wheel `force-include`s canonical root templates into `commonplace/_data/...`, and `commonplace-init` 'fall[s] back to the canonical repository path when running from an editable source checkout'. The only real files it keeps under `_data/templates/` are the user-collection `COLLECTION.md` templates. The ADR is also amended by ADR 086. The attributed design is absent from the linked material and incompatible with it on the editable-install role, so the fourth instance's evidential link does not hold."
    level: fail
  - scope: passage
    quotes:
      - "holistic rework rather than patching"
    reason: "The linked note claims something conditional and narrower. A compact, refreshable whole-picture narrative can replace fragment reconciliation, but only when the picture fits within effective context and can be refreshed in time. This note cites it as 'the fix' for managed staleness of dependent knowledge in general. The transfer from whole-picture narratives to arbitrary dependent artifacts is not articulated."
    level: warn
  - scope: passage
    quotes:
      - "too costly to run always and too noisy to block on"
    reason: "The text testing framework characterises Level B as 'medium cost, high coverage' and lists judge non-determinism as a failure mode. It does not say Level B is too costly to run always or too noisy to block on; those are this note's extensions. The transfer is plausible and partly supported by the non-determinism item, so this is INFO."
    level: info
  - scope: passage
    quotes:
      - "This is the sharpest case of"
    reason: "The indexes note presents itself as the index case of this note's broader rule, and states its mechanism conditionally, as no prevalence claim. Calling the false copy the 'sharpest case' of the indexes mechanism reverses the specialization direction. The mechanism invoked (trusted exhaustive claims suppress the retrieval that would find more) is represented accurately, so this is INFO."
    level: info
outcome: fail
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
