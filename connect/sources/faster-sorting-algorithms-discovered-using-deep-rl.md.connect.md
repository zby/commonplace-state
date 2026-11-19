---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/faster-sorting-algorithms-discovered-using-deep-rl.md"
source_has_frontmatter: true
date: "2026-08-29"
depth: standard
---

# Connection Report: Faster sorting algorithms discovered using deep reinforcement learning

**Source:** [Faster sorting algorithms discovered using deep reinforcement learning](../../../../sources/.snapshots/faster-sorting-algorithms-discovered-using-deep-rl.md)

## Discovery Trace

**Source reading and authorised surface:**
- Read the full 1,559-line snapshot. Its main result is a learned search process that constructs symbolic assembly programs, evaluates correctness and measured latency, compares reinforcement-learning search with cold- and warm-start stochastic superoptimization, and deploys selected routines in LLVM. The snapshot has frontmatter. Under `kb/sources/COLLECTION.md`, the snapshot is immutable and the matching ingest is its authored connection surface.
- Read `kb/sources/COLLECTION.md`; authorised local prospecting destinations are `notes`, `reference`, `sources`, `agent-memory-systems`, and `agentic-systems`. `work` and `instructions` are excluded. The already-known Nature URL was evaluated under `external`, but no extra edge was kept because the ingest's required `source:` metadata already records that provenance.

**Curated heads and full title surfaces:**
- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, and `kb/agentic-systems/README.md`.
- Followed the notes head into `learning-theory-README.md`, `deploy-time-learning-README.md`, `self-improving-systems-README.md`, `evaluation-README.md`, and `foundations-README.md`. These heads routed the source toward learned localized artifacts, non-generality capacity gains, proposal selection, and oracle-bounded autonomy.
- Generated each complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for all five authorised local destinations.

**Description listing scans:**
- Ran `rg '^description:' kb/<destination> --glob '*.md'` over each authorised local destination. For notes, also ran `rg -n -i '^description:.*(learn|search|select|optimization|objective|reward)' kb/notes --glob '*.md'`, `rg -n -i '^description:.*(oracle|verif|correct|benchmark|experiment|proxy|evidence)' kb/notes --glob '*.md'`, and `rg -n -i '^description:.*(symbolic|code|artifact|representational|retained)' kb/notes --glob '*.md'`.
- The note descriptions retained four candidates: the production-method/form distinction, speed as learning, the search-evaluation-retention loop, and oracle-bounded autonomy. `known-target discovery benchmarks` was evaluated but rejected because its target-reconstruction genre is not the AlphaDev experiment's prospective hard-oracle search.
- The source descriptions retained AVO and Self-Improving Algorithms as comparisons on an explicit shared axis. DreamCoder was evaluated but rejected because cumulative DSL abstraction under description length is less direct than low-level performance optimization.
- The reference descriptions yielded shipped Commonplace architecture and policy documents, not claims the AlphaDev paper materially supports. No reference candidate passed the articulation test.
- Agent-memory descriptions surfaced Meta-Harness and auto-harness; agentic-system descriptions surfaced Autogenesis and Compound Engineering. They were evaluated but rejected: executable-artifact search is shared, but AlphaDev has no memory lifecycle, context read-back, or whole-agent orchestration claim, and AVO supplies the closer code-optimization comparison.

**Body searches:**
- `rg -n -i 'AlphaDev' kb --glob '*.md'` and `rg -n -F 's41586-023-06004-9' kb --glob '*.md'` found the direct AlphaDev use in `the-bitter-lesson-selects-production-methods-not-representational.md` (plus excluded workshop/article copies).
- `rg -n -i 'AlphaDev|program synthesis|superoptimi[sz]|assembly algorithm|measured latency|correctness and latency' kb/notes --glob '*.md'` confirmed that direct anchor; focused searches for `objective function|proxy|benchmark|oracle|verification|search space|local optim|deployment|real-world` supplied the candidate neighborhood but were filtered against actual note claims.
- `rg -n -i 'FunSearch|AlphaEvolve|AlphaGeometry|AlphaCode|program search|program evolution|code evolution|symbolic learn|localized artifact|localized form' kb/sources --glob '*.md'` and `rg -n -i 'search.*(code|program|harness)|optimi[sz].*(code|program|harness)|benchmark.*(code|program|harness)' kb/sources --glob '*.md'` surfaced the learned-program and artifact-search comparisons.
- Equivalent focused searches over `kb/reference`, `kb/agent-memory-systems`, and `kb/agentic-systems` found no additional candidate that survived the destination-specific articulation test.

**Link following:**
- Followed the direct AlphaDev note to `Representational form`, `Learning is not only about generality`, `A proposal-selection improvement loop requires search, evaluation, and operative retention`, `Warranted autonomy is bounded by oracle domain`, and `Learning inside a fixed decomposition inherits its mistakes`. The first four supplied concrete reader needs; the fixed-decomposition note was rejected because the paper exposes a fixed action space but does not show an omitted correction causing failure.
- Followed the program-search cluster through AVO, DreamCoder, Meta-Harness, Autogenesis, and Self-Improving Algorithms. AVO is the nearest performance-oracle comparison; Self-Improving Algorithms supplies a distinct and useful contrast in what is learned and when. The other three were weaker than those retained edges.

## Connections Found

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) -- **is-evidence-for**: AlphaDev is the note's peer-reviewed learned-localized case—a parametric policy and tree search produce symbolic assembly routines that become deployed LLVM code.
- [Learning is not only about generality](../../../../notes/learning-is-not-only-about-generality.md) -- **is-evidence-for**: AlphaDev increases speed and lowers instruction count for substantially the same sorting capability, directly instantiating learning as a reliability/speed/cost capacity change rather than wider task scope.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: AssemblyGame and MCTS generate candidate programs, correctness and latency can reject them, and selected routines become operative through LLVM integration; the neural-policy update and the program-selection layer should remain analytically distinct.
- [Warranted autonomy is bounded by oracle domain](../../../../notes/warranted-autonomy-is-bounded-by-oracle-domain.md) -- **is-evidence-for**: exhaustive small-sort correctness checks and measured latency support unattended search inside a narrow instruction, input, and hardware domain, while the paper's non-exhaustive generalization claims remain explicitly theoretical.
- [AVO: Agentic Variation Operators for Autonomous Evolutionary Search](../../../../sources/avo-agentic-variation-operators-autonomous-evolutionary-search.ingest.md) -- **compares-with**: both autonomously optimize low-level programs under correctness and hardware-performance oracles; AlphaDev uses learned value-guided MCTS and includes a resource-matched stochastic-search comparison, whereas AVO delegates variation to a coding agent and lacks a matched search-mechanism baseline.
- [Self-Improving Algorithms](../../../../sources/self-improving-algorithms.ingest.md) -- **compares-with**: both improve sorting performance through learning, but AlphaDev searches once for a static deployable program while Ailon et al. learn distribution-specific data structures during a training phase for later inputs.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [The bitter lesson selects production methods, not representational forms](../../../../notes/the-bitter-lesson-selects-production-methods-not-representational.md) → the matching tracked ingest after it is created -- **evidenced-by**: the note already cites the AlphaDev Nature URL as its learned-localized existence case; routing that citation through the ingest (never through this immutable snapshot) would make the source use locally checkable under the notes grounding contract.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Known-target discovery benchmarks show reachability, not discovery closure](../../../../notes/known-target-discovery-benchmarks-show-reachability-not-discovery.md) -- rejected because AlphaDev searches prospectively against fixed correctness and latency objectives rather than reconstructing a hidden known insight; the contrast is real but not necessary for traversing either claim.
- [Learning inside a fixed decomposition inherits its mistakes](../../../../notes/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) -- rejected because the x86 subset, pruning rules, test inputs, and reward expose a fixed update space, but the paper does not identify a needed correction excluded by that space.
- [Exact implementation does not validate a requirement against its objective](../../../../notes/exact-implementation-does-not-validate-a-requirement.md) -- rejected because AlphaDev separately checks correctness and measured performance but does not demonstrate a failed requirement-to-objective proxy link.
- [Unsupported proxy scope may explain a structured method's loss under scaling](../../../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md) -- rejected because the human-versus-AlphaDev comparison does not isolate unsupported proxy scope as the cause of the human benchmark's loss.
- [DreamCoder](../../../../sources/dreamcoder-wake-sleep-bayesian-program-learning.ingest.md) -- rejected in favor of AVO and Self-Improving Algorithms: neural-guided program search is shared, but DreamCoder's cumulative DSL abstraction and description-length gate serve a different reader question.
- [Meta-Harness](../../../../agent-memory-systems/reviews/meta-harness.md) -- rejected because its trace-backed evolution of memory systems and agent scaffolds is materially farther from low-level algorithm discovery than the retained AVO comparison.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- rejected because its whole-agent resource lifecycle, orchestration, versioning, and rollback claims are not tested or explained by AlphaDev's bounded program search.
- [Commonplace source adoption policy](../../../../reference/source-adoption-policy.md) -- rejected because it describes this repository's shipped borrowing policy; AlphaDev may be an input to that policy but is not evidence about how the shipped policy works.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The target is an immutable snapshot. Apply accepted outbound candidates to `kb/sources/faster-sorting-algorithms-discovered-using-deep-rl.ingest.md` when the ingest run creates it; do not author any link to the snapshot.
