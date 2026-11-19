---
description: "Discovery report for possible KB connections from Mathematical discoveries from program search with large language models"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/mathematical-discoveries-program-search-large-language-models.md"
source_has_frontmatter: true
date: "2026-08-29"
depth: standard
---

# Connection Report: Mathematical discoveries from program search with large language models

**Source:** [Mathematical discoveries from program search with large language models](../../../../sources/.snapshots/mathematical-discoveries-program-search-large-language-models.md)

## Discovery Trace

**Collection rules:** Read `kb/sources/COLLECTION.md`. The authored ingest may
prospect notes, reference, agent-memory systems, agentic systems, and other
sources. Snapshots remain immutable. Work and instructions are excluded, so the
series workshop and its register were not prospected as connection targets.
External prospecting was skipped because the collection reserves it for known
targets and the paper's canonical URL is already captured.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`,
  `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
  The notes head routed the paper toward deploy-time learning and retained
  artifacts. The sources head supplied the authored-companion rule. The
  reference, agent-memory, and agentic heads yielded no more specific target
  than the note and source candidates below.
- The snapshot carries no `tags`, so no tag-README or by-tag description scan
  applied.

**Full title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` and
  `rg '^description:' kb/<destination>/ --glob '*.md'` separately for notes,
  reference, sources, agent-memory systems, and agentic systems. The title
  surfaces contained 386, 159, 336, 174, and 12 entries respectively.
- Notes flagged the learned-localized Bitter Lesson claim, representational-form
  coevolution, proposal selection, fixed decomposition, verifiability, oracle
  strength, and localized-retention candidates. Sources flagged DreamCoder,
  Memento-Skills, AVO, and Self-Improving Algorithms. Reference and the two
  system-review collections produced only broad vocabulary overlap.

**Body search:**

- Ran `rg -n -i 'FunSearch|learned.localized|localized forms' kb/notes --glob '*.md'`.
  The direct hits were the Bitter Lesson production-method note,
  representational-form coevolution, and the verifiability gradient.
- Ran `rg -n -i 'proposal.selection|search.*evaluation.*retention|operative retention|programs database' kb/notes --glob '*.md'`.
  The proposal-selection note fit the paper's generated-program, evaluator, and
  program-database loop.
- Ran `rg -n -i 'fixed decomposition|update space|program skeleton|isolated part.*evolv|efficient evaluator|rich.*scor' kb/notes --glob '*.md'`.
  The fixed-decomposition and oracle notes fit as boundaries, not as stronger
  causal conclusions established by this experiment.
- Ran `rg -n -i 'DreamCoder|Memento.Skills|AVO|program search|evolutionary.*program|frozen (LLM|model)' kb/sources --glob '*.ingest.md'`.
  DreamCoder, Memento-Skills, and AVO survived comparison; Self-Improving
  Algorithms uses a direct learned-data-structure update rather than program
  proposal selection and was rejected.
- Ran `rg -n -i 'FunSearch|program search|evolutionary.*program|frozen (LLM|model)' kb/reference kb/agent-memory-systems kb/agentic-systems --glob '*.md'`.
  Reference produced only unrelated frozen-model-partition terminology; the
  review collections produced no direct FunSearch target.

**Candidate evaluation:**

- Kept the Bitter Lesson production-method note because the paper directly
  supplies its bounded existence claim: a pretrained frozen LLM participates
  in search that produces, evaluates, retains, and reuses localized programs.
- Kept the proposal-selection note because invalid or low-scoring programs can
  be discarded, accepted programs enter the database, and later prompts sample
  that retained population.
- Kept representational-form coevolution and the verifiability gradient because
  both already name FunSearch as a fixed-weight symbolic-search instance; the
  paper supplies the primary record and its efficient-evaluator/rich-score
  boundary.
- Kept the fixed-decomposition note only as a comparison. The paper fixes a
  problem specification and program skeleton and evolves an isolated function,
  but it does not demonstrate a needed correction excluded by that boundary.
- Kept DreamCoder as the closest older learned symbolic-library comparison,
  Memento-Skills as the natural-language-plus-code neighboring localized case,
  and AVO as a later agent-directed evolutionary code-search comparison.
- Rejected localized-retention as a direct evidence edge: the selected function
  is localized, but the paper does not measure sparse environmental change,
  dependency closure, or total revision cost.
- Rejected persistent deployment-time adaptation as a direct evidence edge:
  FunSearch retains programs during search and can deploy its final programs,
  but the paper does not show a later deployment episode revising them in
  response to new evidence.
- Rejected exact-implementation and proximate-target notes as direct evidence:
  the correctness and score functions illustrate their distinction, but this
  study does not isolate evaluator-to-deployment mismatch or objective-proxy
  failure.

**Link following:**

- Followed the Bitter Lesson production-method note to localized retention,
  representational-form coevolution, proposal selection, and fixed
  decomposition. This confirmed that the paper supports existence in the
  learned-localized cell but not the cell's scaling, transfer, or credit-
  assignment claims.
- Followed proposal selection to oracle strength and operative retention. The
  program database supplies operative retention for later search iterations;
  it does not by itself establish deployment-time persistence.
- Followed DreamCoder to its symbolic-library and description-length gate,
  Memento-Skills to its rewritten executable skill memory around a frozen LLM,
  and AVO to its code-lineage search under correctness and throughput checks.
  These comparisons vary the retained artifact and gate without collapsing
  them into one transferred mechanism.

## Connections Found

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: FunSearch is a bounded learned-localized instance: a frozen pretrained LLM helps generate symbolic program functions, evaluation rejects candidates, and successful programs are retained and sampled during later search.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: FunSearch realizes candidate generation, reject-capable correctness and score evaluation, and a program database whose retained population shapes subsequent prompts.
- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -- **is-evidence-for**: the paper supplies the primary fixed-weight symbolic-search case already named in the note, while leaving natural-language and parametric update surfaces fixed.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -- **is-evidence-for**: FunSearch works in resettable, repeatedly executable problems with automated correctness checks and rich performance scores, furnishing the note's evaluator-guided program-evolution example without establishing the whole gradient.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- **compares-with**: FunSearch fixes the specification and skeleton and searches only the isolated critical function; the paper shows this factoring can work, not that it can repair omissions outside that update space.
- [DreamCoder ingest](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) -- **compares-with**: both combine a parametric search guide with retained symbolic programs, but DreamCoder grows reusable language primitives under a description-length gate whereas FunSearch evolves task-bound functions under executable scores.
- [Memento-Skills ingest](../../../../sources/memento-skills-let-agents-design-agents.ingest.md) -- **compares-with**: both keep the main LLM frozen and select localized executable artifacts, while Memento rewrites routed natural-language-plus-code skill folders across tasks and FunSearch searches program functions inside a supplied skeleton.
- [AVO ingest](../../../../sources/avo-agentic-variation-operators-autonomous-evolutionary-search.ingest.md) -- **compares-with**: both retain evaluated code through evolutionary search, but AVO delegates lineage inspection, diagnosis, editing, and evaluation timing to a coding agent while FunSearch uses a fixed sampler-evaluator architecture.

## Bidirectional Candidates

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) <-> source -- **evidenced-by** from the note side: replace the direct external FunSearch citation with the tracked ingest once available so the note's existence claim resolves to the local evidence analysis.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) <-> source -- **evidenced-by** from the note side: FunSearch is a non-reflective working instance whose program database makes accepted candidates operative in subsequent search.

## Reverse-edge Candidates

- [Treat continual learning as representational-form coevolution](../../../../notes/treat-continual-learning-as-representational-form-coevolution.md) -> source -- **evidenced-by**: the note already lists FunSearch as symbolic search with frozen weights; the ingest would supply its primary evidence and scope.
- [The verifiability gradient](../../../../notes/verifiability-gradient.md) -> source -- **evidenced-by**: the note names evaluator-guided program evolution, while the paper states that FunSearch depends on efficient evaluation, rich score feedback, and an isolated evolvable function.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Localized retention pays when sparse changes have bounded impact in a matching decomposition](../../../../notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md) -- rejected as direct evidence: localized output is present, but sparse change, explicit dependency closure, and revision-cost advantage are not tested.
- [Retained system-definition artifacts enable persistent deployment-time adaptation](../../../../notes/retained-artifacts-enable-persistent-deployment-time-adaptation.md) -- rejected as direct evidence: within-search retention and final deployability do not demonstrate revision during a later deployment episode.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- rejected as direct evidence: the source distinguishes correctness from performance scores but does not expose a failed requirement-to-objective link.
- [Self-Improving Algorithms ingest](../../../../sources/self-improving-algorithms.ingest.md) -- rejected as a close comparison: it directly learns distribution-specific data structures and then freezes them, rather than evaluating and retaining generated program proposals.
- `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` candidates -- rejected: their hits share only broad fixed-model or improvement-loop vocabulary and add less traversal value than the retained source comparisons above.

## Index Membership

None

## Synthesis Opportunities

None. The relevant synthesis -- learned production can target localized forms
without establishing that such search scales -- is already owned by [The
bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md).

## Maintenance Observations

None

## Flags

- The supplied Nature and PMC Markdown conversions were byte-identical. The
  retained reading copy uses the Nature-named conversion and the canonical
  Nature URL.
- The conversion preserves the complete paper but has some page-order and
  figure/code OCR artifacts. The main prose, methods, results, references, and
  limitations remain available for analysis.
