---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/wikipedia-bitter-lesson.md"
source_has_frontmatter: true
date: "2026-04-20"
depth: standard
---

# Connection Report: The Bitter Lesson

**Source:** [The Bitter Lesson](../../../sources/wikipedia-bitter-lesson.md)

## Discovery Trace

**Index scan:**
- Read [sources index](../../../sources/dir-index.md) -- flagged existing source-side connections: [What Survives in Multi-Agent Systems](../../../../sources/voooooogel-multi-agent-future.ingest.md) because it is explicitly an applied bitter-lesson analysis of multi-agent infrastructure; [Evans: AI Components for a Deterministic System](../../../../sources/eric-evans-ai-components-deterministic-system.ingest.md) because it is a practitioner counterpressure toward freezing domain-specific taxonomies; [Pathway Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) because it already applies the bitter-lesson boundary to calculator-class constraint problems; [On the "Induction Bias" in Sequence Models](../../../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) because it tests whether architectural bias persists for calculator-class state tracking.
- Read [notes index](../../../notes/dir-index.md) -- flagged [fixed artifacts split into exact specs and proxy theories](../../../../notes/exact-implementation-does-not-validate-a-requirement.md), [codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md), [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), [spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md), [deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [constraining and distillation both trade generality for reliability, speed, and cost](../../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md), and [first-principles reasoning selects for explanatory reach over adaptive fit](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md).

**Topic indexes:**
- Source tag `encyclopedia-article` has no corresponding curated tag index.
- Read learning-theory-related index hits through `rg "bitter lesson|oracle strength|fixed artifacts|proxy theories|relaxing candidate|spec mining" kb/notes/dir-index.md kb/sources/dir-index.md`. This reinforced the same cluster and identified [learning theory](../../../notes/learning-theory-index.md) as the likely index membership if this source were surfaced beyond sources.

**Semantic search:** qmd unavailable in practice.
- `command -v qmd && qmd --index "$COMMONPLACE_QMD_INDEX" update && qmd --index "$COMMONPLACE_QMD_INDEX" embed` found `/home/zby/.npm-global/bin/qmd` but failed with `SqliteError: unable to open database file`, so discovery used grep/index fallback.

**Keyword search:**
- `rg -n "bitter lesson|Bitter Lesson|Sutton|general methods|scal(e|ing).*compute|domain-specific|search and learning|Moore" kb/notes kb/sources kb/reference kb/instructions --glob '*.md'` -- kept direct bitter-lesson notes and source ingests; rejected generic `domain-specific` hits in reference/control-plane docs and unrelated source limitations because they did not help an agent traverse from Sutton's claim.
- `rg -n "reach|explanatory reach|adaptive fit|oracle strength|fixed artifacts|proxy theories|calculators|vision feature|relaxing candidate|spec mining" kb/notes/dir-index.md kb/sources/dir-index.md kb/reference/dir-index.md --glob '*.md'` -- kept reach, oracle, fixed-artifact, spec-mining, and relaxing-signal candidates; rejected broad context-engineering and evaluation hits that mention reach or oracle strength without explaining the bitter-lesson boundary.

**Link following:**
- Followed [fixed artifacts split into exact specs and proxy theories](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) to [spec mining](../../../../notes/spec-mining-as-codification.md), [operational signals](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), and [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md). This showed the source is not just thematically related; it grounds the calculator/vision-feature distinction that those notes operationalize.
- Followed [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) to [deploy-time learning](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md), [error correction](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md), and [boundary of automation](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md). Kept deploy-time learning because Sutton's search/learning pair maps to durable system adaptation; rejected error correction and automation-boundary as downstream uses too far from the source.
- Followed [first-principles reasoning selects for explanatory reach over adaptive fit](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) because it provides the strongest theoretical explanation for why some knowledge survives scaling and some adaptive fit gets replaced.

## Connections Found

- [fixed artifacts split into exact specs and proxy theories](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- **grounds**: the source supplies the historical AI pattern that the note reframes as exact-spec artifacts versus proxy theories; chess, Go, speech, and vision examples are the empirical material behind the calculator/vision-feature distinction.
- [codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) -- **grounds**: the source is the scaling pressure that makes codification provisional; the note's codify/relax cycle is an operational response to Sutton's claim that scale eventually eats many hand-built theories.
- [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) -- **extends**: the source names search and learning as scale-friendly methods, while the note refines where they should win by asking how strong the verification oracle is.
- [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md) -- **enables**: the source gives the strategic warning; the note turns it into testable signals for deciding when a codified component is behaving like a vision feature.
- [spec mining is codification's operational mechanism](../../../../notes/spec-mining-as-codification.md) -- **extends**: spec mining is a response to the source's hardest caveat, because it tries to codify only regularities observed in working systems rather than inventing brittle hand-coded theories upfront.
- [deploy-time learning is the missing middle](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- **extends**: Sutton's two winning techniques, search and learning, map to deploy-time artifact evolution when a system searches over and hardens prompts, tests, schemas, and tools during deployment.
- [constraining and distillation both trade generality for reliability, speed, and cost](../../../notes/constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md) -- **qualifies**: the source warns that general methods win, while this note explains why narrower artifacts still survive when the reliability/speed/cost compound outweighs generality loss.
- [first-principles reasoning selects for explanatory reach over adaptive fit](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) -- **synthesizes**: reach offers a mechanism for the bitter lesson: high-reach explanations transfer under scale, while low-reach adaptive fit is replaced by general methods.

## Bidirectional Candidates

- [fixed artifacts split into exact specs and proxy theories](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) <-> source -- **grounds**: a return link to the source helps readers recover Sutton's original examples when evaluating the note's boundary claim.
- [codification and relaxing navigate the bitter lesson boundary](../../../../notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) <-> source -- **grounds**: the source is the external frame for the note's codify/relax terminology.

## Raw Text Candidates

None

## Rejected Candidates

- [the boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- rejected as downstream synthesis: it uses oracle-strength reasoning that is compatible with the bitter lesson, but the connection is through existing intermediary notes.
- [error correction works with above-chance oracles and decorrelated checks](../../../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) -- rejected as too operationally distant; it matters after an oracle exists, not for the bitter-lesson claim itself.
- [Pathway Beyond Transformers: Sudoku Bench](../../../../sources/pathway-beyond-transformers-sudoku-bench.ingest.md) -- rejected as a direct connection for this report because it is better treated as an example under the fixed-artifact/oracle cluster, not as a core source-to-source link from Sutton.
- Generic `domain-specific` hits in source limitations and reference docs -- rejected as keyword-only matches without useful traversal value.

## Index Membership

- [learning theory](../../../notes/learning-theory-index.md) -- the source belongs in the learning-theory cluster as the canonical external reference for scale-friendly search/learning versus hand-coded proxy theory.

## Synthesis Opportunities

- "Reach predicts resistance to bitter-lessoning": combine this source with [first-principles reasoning selects for explanatory reach over adaptive fit](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md), [fixed artifacts split into exact specs and proxy theories](../../../../notes/exact-implementation-does-not-validate-a-requirement.md), and [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md) to argue that artifacts survive scaling when they capture high-reach structure or hard-oracle specifications, and fail when they encode adaptive fit to current model limits.

## Flags

- Load-bearing relationships to [oracle strength spectrum](../../../../notes/oracle-strength-spectrum.md), [operational signals that a component is a relaxing candidate](../../../../notes/operational-signals-that-a-component-is-a-relaxing-candidate.md), and [first-principles reasoning selects for explanatory reach over adaptive fit](../../../notes/first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md) are provisional because those targets are `seedling`.
