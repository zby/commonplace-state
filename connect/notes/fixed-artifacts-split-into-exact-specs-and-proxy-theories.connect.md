---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/fixed-artifacts-split-into-exact-specs-and-proxy-theories.md"
source_has_frontmatter: true
date: "2026-07-29"
depth: standard
---

# Connection Report: Exact implementation does not validate a requirement against its objective

**Source:** [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md)

## Discovery Trace

**Description listing scan:**
- Read `kb/notes/tags-README.md`, `kb/notes/learning-theory-README.md`, and `kb/notes/constraining-README.md`. The learning-theory page declares `covered_by`, so its by-tag `rg` was skipped; the constraining descriptions were enumerated with `rg -l '^tags:.*\bconstraining\b' kb/notes/ --glob '*.md' | xargs -r rg -N --no-heading '^description:\s*' -r ''`.
- Generated the fresh complete H1 surface with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'` (1,063 headings). The strongest title matches were the proximate-target, decomposition-warrant, typed-verification, accepted-edit, declared-objective, progressive-constraining, induction-bias, and No Free Lunch artifacts evaluated below.
- Read the destination heads `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/sources/README.md`, and `kb/instructions/README.md`. Reference and instructions had no direct trigger beyond downstream operationalizations; the external-system hits were examples already represented by the final note's Fintool and memory-policy links.

**Topic indexes:**
- `learning-theory-README.md` routes the source through its enforced `constraining` child instead of enumerating it directly.
- `constraining-README.md` still lacks the source in its curated “Deciding and reversing” section; the final note now states the condition that pattern-stability heuristics cannot establish on their own.
- The agent-memory and agentic-system heads surfaced no missing premise stronger than the final note's existing memory-policy and Fintool routes.

**Body search:**
- `rg -n -i 'verification (and|versus) validation|verification.*validation|requirement (chain|graph|path|boundary)|proxy theor|spec (is|equals) the problem|composition failure|constitutive rule|adopted commitment|hard oracle|reversib|blast radius' kb/notes/ --glob '*.md'` — confirmed that the proximate-target and decomposition-warrant notes are the strongest conceptual continuations and are now linked; retained two target-side candidates and rejected the typed-verification and declared-objective notes as indirect.
- `rg -n -i 'verification|validation|requirement|proxy theor|exact spec|composition failure|hard oracle|constitutive|reversib|blast radius|spec is the problem' kb/sources/ --glob '*.ingest.md'` — confirmed the induction-bias, MAKER, SuperARC, and Fintool evidence routes already present; rejected the No Free Lunch explainer as redundant, lower-authority support.
- `rg -n -i 'exact spec|proxy theor|composition failure|hard oracle|requirement|codif|relax|reversib' kb/agent-memory-systems/ kb/agentic-systems/ --glob '*.md'` — confirmed that the existing memory-policy link supplies the most useful system-level example and that Fintool already carries an inbound route.
- `rg -n -i 'exact spec|proxy theor|composition failure|requirement chain|verification.*validation|codif|relax|reversib' kb/reference/ kb/instructions/ --glob '*.md'` — found no direct missing dependency; the comparative-test proposal remains better reached through the linked codification material.
- `rg -n 'fixed-artifacts-split-into-exact-specs-and-proxy-theories|Exact implementation does not validate a requirement against its objective|Fixed artifacts split into exact specs and proxy theories' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ kb/instructions/ --glob '*.md'` — checked inbound coverage, existing footer edges, and duplicate reverse-edge suggestions.

**Link following:**
- Re-read the linked proximate-target and decomposition-warrant notes. Together they supply the declared analysis boundary and the provenance/use account for how a conjectured requirement–objective link can acquire warrant; no additional outbound hop would improve that route.
- Followed `verification-needs-a-typed-target-before-it-needs-an-oracle.md` through oracle-domain and artifact-analysis notes. It concerns the prior classification needed for reusable checking, not whether passing a correctly targeted check validates an upstream objective link.
- Followed `an-accepted-edit-verifies-the-change-not-the-rule.md` through spec mining and trace-extracted memory. Its instance-to-rule gap is a concrete instance of the source's local-conformance/upstream-warrant split, making a target-side edge more useful than another outbound edge from an already well-connected source.
- Re-read progressive constraining and its codification foundation. Cross-run stability remains useful timing evidence but does not validate that the stabilized requirement serves the objective, so it is a strong target-side contrast.

## Connections Found

None. The three strongest initial candidates—the proximate-target extension, decomposition-warrant extension, and induction-bias evidence—are now authored in the source, and the remaining useful directions are inbound.

## Bidirectional Candidates

None. The proximate-target note already authors a grounding edge back to the source, and the final source now supplies the independently useful outbound extension.

## Reverse-edge Candidates

- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) → source — **contrasts**: repeated stability bears on when to harden a behavior, while the source shows that stability does not establish that the hardened requirement serves the objective above it.
- [An accepted edit verifies the change, not the rule](../../../../notes/an-accepted-edit-verifies-the-change-not-the-rule.md) → source — **exemplifies**: acceptance checks the instance while rule extraction posits an upstream generalization, instantiating the same local-correctness versus link-warrant split.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Verification needs a typed target before it needs an oracle](../../../../notes/verification-needs-a-typed-target-before-it-needs-an-oracle.md) — target classification is a prerequisite for reusable checking, but it does not decide whether conformance to the classified target validates the requirement–objective relation.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) — naming an objective reinforces the source's boundary discipline, but the already linked proximate-target note supplies the more direct route without importing the self-improvement cluster.
- [Use tests a decomposition locally; retained rationale is what makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) — directly relevant, but already reached through the linked decomposition-warrant note; another footer edge would duplicate that route.
- [The No Free Lunch Theorem ingest](../../../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) — its distribution-assumption frame is useful pedagogy but adds less authority than the source's linked bitter-lesson argument and induction-bias evidence.
- [Codify-versus-LLM decision heuristics](../../../../notes/codify-versus-llm-decision-heuristics.md) — already grounds itself in this source and packages downstream decision heuristics, so a reciprocal edge would add little traversal value.
- [Bidirectional codification as a comparative test](../../../../reference/proposals/bidirectional-codification-comparative-test.md) — a valid downstream test proposal, but the useful route runs through the source's existing codification and relaxing links rather than a direct `see-also` edge.

## Index Membership

- [Constraining](../../../../tags/constraining-README.md) — candidate for “Deciding and reversing”: the source now states why local exactness and cross-run stability are insufficient to validate the objective link that a hardening decision relies on.

## Synthesis Opportunities

- “Architectural constraints cluster around verifiable formal tasks” could compare the induction-bias, SuperARC, ConvexBench, and Sudoku ingests while preserving their unequal evidence quality and unresolved scale/pretraining confounds. That empirical burden should remain in a synthesis rather than expanding this relational theory note with more benchmarks.

## Maintenance Observations

None. The final source uses authorised relationship labels, and every local link resolves.

## Flags

None. The source is neither a duplicate nor a split candidate, and its strongest outbound gaps from the initial discovery pass are now filled.
