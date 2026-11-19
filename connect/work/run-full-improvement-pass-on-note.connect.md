---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/work/agent-note-improvement/run-full-improvement-pass-on-note.md"
source_has_frontmatter: false
date: "2026-07-07"
depth: standard
---

# Connection Report: Run a full improvement pass on one note

**Source:** [Run a full improvement pass on one note](../../../work/agent-note-improvement/run-full-improvement-pass-on-note.md)

**Provisional** — the source is a workshop `text` file with no frontmatter (no `type`, `tags`, `description`). Discovery ran from its title and body. There are no `tags:` to drive tag-README sweeps, so all curated-head reads were description-level and topical.

The source is an orchestration runbook: it sequences the compression bundle, `critique-note`, the optional production `semantic` bundle, and `cp-skill-connect` over one note, reconciles their reports into one editorial packet (step 6), applies the packet (step 7), and closes with an isolated flow/coherence copyedit (step 8). Its load-bearing design commitments are (a) running several methods that test *different, orthogonal* properties, and (b) reconciling their disagreement by *keeping both* findings rather than picking a winner. Candidate hunting targeted the theory behind those two commitments plus the concrete method for step 8.

The source already references `compression/README.md`, `run-compression-bundle-on-note.md`, `kb/instructions/critique-note.md`, `kb/instructions/run-review-batches.md`, and `cp-skill-connect` (and names `instruction-prune-weak-expansions.md` / `instruction-split-rehome-critique.md`, which exist as case-01 workshop files). Those are excluded as existing links; this run hunts for *new* candidates.

`kb/work/COLLECTION.md` outbound posture: **permissive** — workshops freely cite the library (`kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/instructions/`, `kb/sources/`, and peer workshops). Labels are explicitly *suggestions, not authoritative*; the articulation test still governs. Library collections do **not** link into `kb/work/` — workshops are sinks — so there are no reverse-edge or bidirectional candidates.

## Discovery Trace

**Collection routing / heads read:**
- `kb/work/COLLECTION.md` outbound section — permissive, loose label authorisation, `kb/work/` is a link sink (no inbound).
- `kb/work/agent-note-improvement/README.md` — workshop framing; confirms this instruction is the promotion candidate, drafted from cases 01–03, first live run in case 04. Case 04 notes connect's own value (reciprocal links, one unauthorised footer label).
- `kb/work/agent-note-improvement/compression/README.md` — the compression bundle's lens is "edit-strategy / context-cost," explicitly *separate* from truth/grounding — corroborates the orthogonality claim the source leans on.
- `kb/cache/types/connect-report.md` — report contract.

**Body / description searches (actual queries):**
- `rg -i 'orthogonal|different propert|test different|distinct axis' kb/notes/` — surfaced `error-correction-works-above-chance-oracles-with-decorrelated-checks` (decorrelated/orthogonal check dimensions). Kept.
- `rg -i 'reconcil|disagree|arbitrat|conflicting finding' kb/notes/ kb/reference/ kb/instructions/` — surfaced `synthesis-is-not-error-correction`, `critique-note.md` (already linked), `reasoning-production-is-not-reasoning-evaluation`. Evaluated below.
- `rg -i 'copyedit|flow pass|readability|separate.*pass' kb/notes/ kb/instructions/` — surfaced `revise-note` (via `cp-skill-revise-*` neighbours); confirmed by `rg '^description:' kb/instructions/revise-note.md` → "rewrites for logic, flow, and cohesion. Edits the file in place." Direct match to step 8. Kept.
- `rg -N '^description:' kb/instructions/*.md kb/instructions/gates/*.md kb/instructions/review-gates/*.md` — enumerated sibling procedures; surfaced `composition-friction-gate` (report-only adversarial gate) and re-confirmed `critique-note` / `run-review-batches` are already cited.
- `rg -N '^description:' kb/notes/reasoning-production-is-not-reasoning-evaluation.md kb/notes/an-accepted-edit-verifies-the-change-not-the-rule.md kb/notes/verifiable-subroles-before-reviewer-identity.md` — evaluated for the reconciliation/decomposition angle; see Rejected.

**Link following:**
- From `error-correction-...decorrelated-checks` footer → `synthesis-is-not-error-correction` (cross-linked pair: redundant calls→vote, complementary calls→synthesize). This pair maps cleanly onto the source: its four methods are *complementary* checks, so its "keep both, don't pick a winner" reconciliation is the synthesis branch, not the voting branch. Both kept as separate candidates.
- `synthesis-is-not-error-correction` → `bounded-context-orchestration-model` / `decomposition-heuristics-...` — too general (scheduler theory) to help an operator of this runbook; not kept.

## Connections Found

- [error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — **rationale**: the runbook runs several methods that test *different* properties (compression = context cost, `critique-note` = defensibility, `semantic` = truth/grounding, connect = links) precisely because orthogonal check dimensions each catch a different class of error; this note is the theory ("combine structural with semantic with metamorphic checks... each catches a different class of errors, so their failures are structurally independent"). Following it explains why four different-property passes give broader coverage than iterating one gate. **Target `status: seedling` and the label is load-bearing — flag before authoring.**
- [synthesis is not error correction](../../../../notes/synthesis-is-not-error-correction.md) — **rationale**: step 6 reconciles the four reports by *synthesis* ("do not just concatenate"), and the rule "keep both findings rather than picking a winner" is exactly this note's design rule that *complementary* calls (different sub-problems) need synthesis, not voting. It grounds why the runbook must not resolve a compression-vs-semantic disagreement by dropping a finding. **Target `status: seedling` and the label is load-bearing — flag before authoring.**
- [revise-note](../../../../instructions/revise-note.md) — **draws-on**: step 8's isolated copyedit ("revise the note for flow, coherence, logic and readability") is operationally this instruction — "Editorial revision of a single KB note — rewrites for logic, flow, and cohesion... edits in place." A future edit could name it as the concrete step-8 method. Caveat for the author: `revise-note` *reads linked notes for context*, whereas step 8 deliberately restricts the sub-agent's input to the note text plus the prompt — so cite it as the closest existing method, not a drop-in.
- [composition-friction-gate](../../../../instructions/composition-friction-gate.md) — **see-also**: a sibling experimental, report-only gate that probes yet another orthogonal property (does the central claim survive concretization; which inferential joints are least supported) and, like the sequenced methods, runs in a fresh sub-agent and emits no acceptance state. Named so a future author can weigh adding it as a fifth report-only pass; the runbook does not currently sequence it.

## Bidirectional Candidates

None. `kb/work/` is a link sink under `kb/work/COLLECTION.md` ("Library collections do not link into `kb/work/`"), so no library note should author a return link to this workshop file.

## Reverse-edge Candidates

None — same sink rule. If this instruction is promoted into `kb/instructions/`, reverse-edge prospecting should be re-run against the promoted path.

## Off-authorisation Candidates

None. Workshop label authorisation is explicitly loose (working-state labels plus borrowed theoretical/descriptive labels, "or use a local phrase"), so every candidate that passed the articulation test found an authorised label.

## Raw Text Candidates

None. All candidate targets carry frontmatter. (The *source* is a raw workshop text file, which is why this report is marked provisional — that concerns the source, not the targets.)

## Rejected Candidates

- [reasoning-production-is-not-reasoning-evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) — real thematic overlap (the runbook runs `critique-note` in a *fresh* sub-agent, which is the process-validity separation this note argues for), but the note is about reviewer *authority* and answer-reconstruction in evaluation systems; an operator of this runbook gains little concrete beyond the fresh-runner rationale already stated inline. Borderline; excluded to keep the set tight. Reconsider if the runbook grows an explicit "why fresh sub-agents" rationale.
- [verifiable-subroles-before-reviewer-identity](../../../../notes/verifiable-subroles-before-reviewer-identity.md) — the runbook does decompose improvement into separately-runnable single-property checks before any edit (a subrole-decomposition pattern), but the note is scoped to scholarly peer-review automation and reviewer-level authority; the parallel is topical, not operationally useful here.
- [an-accepted-edit-verifies-the-change-not-the-rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) — relevant to the *workshop's* experiment/promotion framing (compare against an accepted delta), which lives in the workshop `README.md`, not to this instruction's operation. Route from the README if wanted, not from this file.

## Index Membership

None new. The workshop's own [`README.md`](../../../../work/agent-note-improvement/README.md) already lists this instruction under "Combined instruction," "Fourth case," and "What would close this workshop." No library index applies while it stays in `kb/work/`.

## Synthesis Opportunities

None new. The higher-order claim ("redundant checks → vote; complementary checks → synthesize; this runbook is the complementary/synthesize instance") is already captured by the existing `error-correction-...decorrelated-checks` ↔ `synthesis-is-not-error-correction` cross-links; the runbook is an application of it, not a new synthesis.

## Maintenance Observations

- Both strongest grounding candidates (`error-correction-...decorrelated-checks`, `synthesis-is-not-error-correction`) are `status: seedling`. Load-bearing `rationale` edges onto seedlings are acceptable from a workshop draft, but if this instruction is promoted to `kb/instructions/`, those grounding edges should be re-examined against the destination collection's stricter authorisation and the seedlings' status at that time.

## Flags

- **Provisional report** — source is a workshop `text` file with no frontmatter; re-run connect after any promotion that adds frontmatter and a real `type`.
- **Promotion pending** — per the workshop `README.md`, promotion of this instruction awaits a case where compression and `critique-note` actually disagree on the same passage. On promotion into `kb/instructions/`, the label authorisation switches from `kb/work/`'s permissive set to `kb/instructions/COLLECTION.md`, and both reverse-edge prospecting and the seedling-grounding check above should be redone.
