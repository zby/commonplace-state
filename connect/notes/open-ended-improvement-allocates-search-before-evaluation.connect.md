---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/notes/open-ended-improvement-allocates-search-before-evaluation.md"
source_has_frontmatter: true
date: "2026-08-30"
depth: standard
---

# Connection Report: Open-ended improvement allocates search before decisive evaluation

**Source:** [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md)

## Discovery Trace

**Curated heads:**

- Read `kb/notes/README.md`, `kb/notes/tags-README.md`, and the source's three tag heads: `foundations-README.md`, `computational-model-README.md`, and `self-improving-systems-README.md`. None of the three tag heads declares `complete: true`, so no by-tag description scan was skipped. The self-improving-systems head exposed a missing prior-allocation step beside proposal selection; the computational-model head supplied a second plausible placement under scheduling and orchestration.
- Read the destination heads for `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/`. They supplied no candidate as direct as the notes cluster.

**Title and description listing scans:**

- Generated the complete notes title surface with `rg -N --no-heading -m1 '^# ' kb/notes --glob '*.md'`. It exposed the lightweight-control, controller-evaluation, backtracking, failure-explanation, natural-language-state, candidacy-evidence, bootstrap, intent, and productive-deferral candidates evaluated below.
- Generated complete title surfaces with the same command for `kb/types`, `kb/reference`, `kb/agent-memory-systems`, `kb/agentic-systems`, `kb/sources`, and `kb/instructions`.
- Ran `rg '^description:' kb/<destination> --glob '*.md'` for every authorised local destination: `notes`, `types`, `reference`, `agent-memory-systems`, `agentic-systems`, `sources`, and `instructions`.
- Ran the required by-tag scans for `foundations`, `computational-model`, and `self-improving-systems` with `rg -l '^tags:.*\bTAG\b' kb/notes --glob '*.md' | sort | xargs -r rg -N --no-heading '^description:\s*' -r ''`. These scans retained the search-control cluster and rejected broader learning, evaluation, and orchestration matches that did not explain allocation before decisive evidence.

**Body search:**

- `rg -n -i 'search control|search controller|allocate.*search|search allocation|decisive evaluation|exhaustive counterfactual' kb/notes --glob '*.md'` -- retained lightweight search control and its controller-evaluation, backtracking, failure-feedback, and project-state refinements. The controller-evaluation note directly addresses the source's open question without presupposing exhaustive counterfactual search.
- `rg -n -i 'candidacy evidence|pursuit-worth|worth investigating|escalation.*acceptance' kb/notes --glob '*.md'` -- retained candidacy evidence as the epistemic basis for using weak evidence to spend stronger-assessment effort without granting adoption authority.
- `rg -n -i 'backtracking|branch decision|search heuristic|live alternatives' kb/notes --glob '*.md'` -- kept backtracking, failure explanation, and natural-language project state; rejected the live-alternatives note because its intent test is narrower and the retained candidates already carry its useful routing signal.
- `rg -n -i 'proof search|proof gate|Gödel machine' kb/notes --glob '*.md'` -- confirmed that the source already links the closest Gödel-machine interpretation. The underlying ingest was evaluated but rejected as a duplicate direct lineage path.
- `rg -n -i 'open-ended improvement|open-ended search' kb/notes --glob '*.md'` -- surfaced the hand-crafted-bootstrap application and the two notes that already author return paths to the source.
- For every non-notes destination ran `rg -n -i 'search allocation|allocate.*search|search controller|branch selection|decisive evaluation|candidacy evidence|pursuit-worth|proof search|open-ended improvement|exhaustive counterfactual' kb/<destination> --glob '*.md'`. `types`, `agentic-systems`, and `instructions` produced no direct candidate. Reference hits merely cite candidacy evidence; agent-memory hits use branch-selection language for implementation details; source hits included the Gödel-machine ingest and less direct system cases. None added a distinct reader path.
- External prospecting was skipped because no external target was supplied or already loaded, and the collection contract treats external as an authorised destination rather than an open-web search surface.

**Link following:**

- Followed all four authored links from the source and inspected the `Relevant Notes` neighborhoods of the proposal-selection loop, Gödel-machine interpretation, verification boundary, and program-theory note. They confirmed that the source already carries its function-separation, proof-gate, acceptance-boundary, and delayed-feedback context; none displaced the new search-control candidates.
- Followed the retained lightweight-control cluster one hop. Backtracking supplies reversibility, failure explanation supplies feedback into later allocation, natural-language project state proposes a model-mediated carrier, and controller evaluation supplies a practical assessment method.
- Searched inbound links with `rg -n --fixed-strings 'open-ended-improvement-allocates-search-before-evaluation.md' kb --glob '*.md'`. [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) and [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) already author useful return paths, so no duplicate return-link candidates are proposed for them. Workshop hits were excluded by the collection contract.
- Read the full claims, caveats, and footers of every retained candidate. All retained and rejected targets below have frontmatter, and every listed path was verified to exist.

**Per-destination disposition:**

- `notes` (including `notes/definitions`): seven outbound candidates passed the articulation and label tests. One warrants an unauthored reciprocal path. No term required a `defined-in` edge.
- `types`: no type contract bears on the source's theoretical distinction between prior allocation and decisive evaluation.
- `reference` (including `reference/definitions`): no Commonplace implementation record or definition adds a distinct reader path; the lexical hits merely consume the retained notes.
- `agent-memory-systems`: branch-selection cases describe system-specific routing but do not establish the source's general necessity claim or a reusable evaluation mechanism.
- `agentic-systems`: no candidate adds evidence or a mechanism beyond the notes abstracted from system cases.
- `sources`: the Gödel-machine ingest is already mediated by the source's authored Gödel-machine note link; other hits do not directly establish the prior-allocation claim.
- `instructions`: no procedure adds ordering, defaults, or stopping conditions to this methodology strongly enough to warrant `operationalized-from`.

## Connections Found

- [Lightweight search control allocates further search without licensing adoption](../../../../notes/lightweight-search-control-does-not-license-adoption.md) -- **extends**: names the limited-authority control role required by the source and makes explicit that routing a branch to more work does not license its adoption.
- [A search controller is tested by what it brings to stronger evaluation](../../../../notes/a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) -- **extends**: develops a way to compare allocation policies through the candidates, probes, discriminating evidence, and recoverable failures they bring downstream, without assuming exhaustive counterfactual search.
- [Candidacy evidence licenses escalation to assessment, not acceptance](../../../../notes/candidacy-evidence-licenses-escalation-not-acceptance.md) -- **grounds**: supplies the epistemic reason weaker evidence can allocate scarce assessment effort before adoption-quality evidence exists without inheriting verdict authority.
- [Backtracking keeps lightweight search control provisional](../../../../notes/backtracking-keeps-lightweight-search-control-provisional.md) -- **mechanism**: explains how an allocation process can preserve prior state and redirect after contrary evidence so an early branch choice does not become a hidden commitment.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../notes/failure-explanation-changes-later-branch-decisions.md) -- **mechanism**: identifies one feedback path by which evidence from a reached branch revises what later branches are tried, scoped, prioritized, probed, continued, or abandoned.
- [Natural-language project state may specialize weight-resident search heuristics](../../../../notes/natural-language-project-state-specializes-search-heuristics.md) -- **extends**: proposes a model-mediated implementation in which retained intent, constraints, and branch history specialize general search heuristics while remaining below acceptance authority.
- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) -- **extends**: applies the prior-allocation constraint to theory-mediated self-improvement, where computation must choose theories and experiments before a complete global-fit judgment exists.

## Bidirectional Candidates

- [A hand-crafted bootstrap fits the Bitter Lesson only if learning can outgrow it](../../../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md) <-> source -- source to bootstrap is **extends**; bootstrap to source is **grounds**, because the return path explains why an incomplete global-fit oracle leaves a necessary computational search-allocation problem rather than eliminating selection.

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Intent controls a local choice only when it distinguishes its live alternatives](../../../../notes/intent-controls-choices-by-distinguishing-live-alternatives.md) -- rejected because it tests whether retained intent constrains one local choice, while the source concerns the prior allocation function generally; the natural-language-state and lightweight-control candidates carry the useful signal more directly.
- [Productive deferral requires a preserved option, discriminating evidence, and a convergence rule](../../../../notes/productive-deferral-requires-option-evidence-and-convergence.md) -- rejected because it governs whether postponing a commitment remains controlled, not why open-ended search must allocate work before decisive evidence exists.
- [Reasoning production is not reasoning evaluation](../../../../notes/reasoning-production-is-not-reasoning-evaluation.md) -- rejected because its distinction is specific to producing and reviewing reasoning, while the source already links the more general proposal-selection loop that separates search from reject-capable evaluation.
- [Weakly discriminated qualities tend to be underselected](../../../../notes/weakly-discriminated-qualities-tend-to-be-underselected.md) -- rejected because it concerns which qualities survive an acceptance regime with weak discrimination, not which candidates receive the prior opportunity to reach that regime.
- [An omitted improvement-loop function and a frozen one need different repairs](../../../../notes/an-omitted-loop-function-and-a-frozen-one-need-different-repairs.md) -- rejected because its casebook includes a relevant parent-selector failure but does not add a general mechanism beyond the retained search-controller note.
- [System use is an initial selection environment when theory fit lacks a fixed oracle](../../../../notes/system-use-selects-theory-fit-without-a-fixed-oracle.md) -- rejected because it supplies one narrower selection environment for theory fit; the bootstrap candidate applies the source's allocation constraint more completely and already leads into that neighborhood.
- [Ingest: Gödel Machines — Provably Optimal Self-Improvements](../../../../sources/goedel-machines-schmidhuber.ingest.md) -- rejected as a direct edge because the source already links the Gödel-machine note that owns and bounds this interpretation; another lineage edge would duplicate grounding rather than add a new reader path.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- candidate for the `Update architecture` section beside proposal selection: the source states the prior allocation obligation that applies before a generated candidate can enter reject-capable evaluation.
- [Computational model](../../../../tags/computational-model-README.md) -- candidate for `Scheduling & Orchestration`: the source identifies allocation across a dynamically generated branch set as a scheduler obligation that cannot be delegated to a decisive evaluator alone.

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

None
