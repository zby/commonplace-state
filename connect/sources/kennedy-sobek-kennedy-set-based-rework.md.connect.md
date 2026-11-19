---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/kennedy-sobek-kennedy-set-based-rework.md"
source_has_frontmatter: true
date: "2026-08-28"
depth: standard
---

# Connection Report: Set-Based Practices for Reducing Systems-Engineering Rework

**Source:** [Reducing Rework by Applying Set-Based Practices Early in the Systems Engineering Process](../../../../sources/.snapshots/kennedy-sobek-kennedy-set-based-rework.md)

The snapshot is immutable. Every outbound candidate below is for the matching ingest report's authored surface, not for an edit to the snapshot.

## Discovery Trace

**Source analysis:**

- Read the complete 1,491-line snapshot. Its central claim is that three common causes of late rework—late critical learning, decisions made before the required knowledge exists, and one specialty prematurely constraining another—can be addressed by test-before-design, reusable limit/trade-off knowledge, ranged requirements and specifications, parallel alternatives, and evidence-gated convergence before detailed design.
- The source has frontmatter and is a typed full-source scientific-paper snapshot, so this report is not provisional.
- Read `kb/sources/COLLECTION.md`. It authorizes local prospecting in `notes`, `reference`, `agent-memory-systems`, `agentic-systems`, and `sources`; it excludes `work` and `instructions`. The usable labels here are `is-evidence-for`, `abstracted-from`, `rests-on`, `compares-with`, `defined-in`, and sparse `see-also` according to destination. No open-web prospecting was performed.

**Curated heads and complete listings:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, and `kb/sources/README.md` in full.
- The source carries no `tags:` field, so there were no matching tag-README heads or by-tag searches to run.
- Generated the fresh complete title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'`: notes 376 titles; reference 157; agent-memory-systems 174; agentic-systems 12; sources 333.
- Generated the whole-destination description surface with `rg '^description:' kb/<destination>/ --glob '*.md'`: notes 374 description lines; reference 156; agent-memory-systems 172; agentic-systems 10; sources 333.

**Notes body search and evaluation:**

- `rg -n -i 'set-based|point-based|test-before-design|limit curve|trade[- ]?off curve|design window' kb/notes/ --glob '*.md'` — no exact terminology match; candidate discovery therefore depended on adjacent mechanisms rather than keyword identity.
- `rg -n -i 'premature decision|delay(ed|ing)? (a |the )?(critical )?decision|latest possible|decision.*knowledge|knowledge.*decision|irreversib|optionality|preserv(e|ing).*option|design space' kb/notes/ --glob '*.md'` — kept the information-timing and optionality cluster; rejected generic design-space uses.
- `rg -n -i 'knowledge gap|front[- ]?load|learn(ing)? first|accelerat(e|ed|ing) learning|rework|gradual(ly)? converg|evidence.*narrow|narrow.*evidence|commit.*after' kb/notes/ --glob '*.md'` — kept late-learning, specification-timing, and progressive-constraining candidates.
- `rg -n -i 'trade[- ]?offs?|range(s)? of (valid|possible|acceptable)|space of (valid|possible)|constraint.*range|uncertaint(y|ies)' kb/notes/ --glob '*.md'` — re-filtered broad overlap against the paper's actual mechanism.
- Kept [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md): the source independently identifies late customer/market learning as a cause that is often reported as changed requirements and distinguishes rework from intentional learning iterations.
- Kept [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md): set-based ranged requirements and specifications are a peer-reviewed worked method for keeping a durable specification provisional while execution generates the knowledge needed to narrow it.
- Kept [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md): the paper explicitly recommends planning backward to the latest convergence date and refusing decisions unsupported by knowledge produced during the run.
- Kept [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) as a comparison, not evidence: both delay narrowing until observations support it, but the note concerns recurring LLM interpretations and codification while the paper concerns engineering trade spaces and specifications.

**Other local destinations:**

- `rg -n -i 'set-based|rework|premature decision|delayed commitment|evidence.*narrow|narrow.*evidence|knowledge.*commit' kb/reference/ --glob '*.md'` — hits concerned Commonplace's shipped review/design-rationale machinery, not the paper's product-development mechanism; no reference candidate passed articulation.
- The same query over `kb/agent-memory-systems/` returned incidental uses of commitment, promotion, and storage rework; none gives a system-comparison reader a concrete reason to traverse from this paper.
- The same query over `kb/agentic-systems/` returned only incidental rollback/commit wording; no whole-system analysis shared the paper's set-based narrowing mechanism closely enough to keep.

**Sources body search and evaluation:**

- `rg -n -i 'set-based|point-based|test-before-design|limit curve|design window|concurrent engineering' kb/sources/ --glob '*.md'` — no prior ingest covers this method directly.
- `rg -n -i 'irreversib|option value|optionality|value of waiting|delay(ed|ing)? (commit|decision|investment)|defer(ring|red)? (commit|decision|investment)|latest responsible|last responsible' kb/sources/ --glob '*.md'` — kept Pindyck as the formal option-value comparison.
- `rg -n -i 'rolling wave|adaptive pathway|adaptation tipping|decision space|minimum constraint|room to (explore|adapt)|progressive elaboration|staged narrowing|convergence.*evidence|evidence.*convergence' kb/sources/ --glob '*.md'` — kept DAPP and Githens as distinct planning-method comparisons.
- `rg -n -i 'rework|premature decision|knowledge gap|front[- ]?load|trade[- ]?off.*range|range.*trade[- ]?off|uncertainty.*commit|commit.*uncertainty' kb/sources/ --glob '*.md'` — confirmed that the kept sources share the information-timing mechanism rather than merely the word “uncertainty.”
- Kept [Irreversibility, Uncertainty, and Investment](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md): it supplies the formal conditions and waiting cost; the set-based paper supplies an applied method that actively buys information before full commitment.
- Kept [Dynamic Adaptive Policy Pathways](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md): DAPP narrows through monitored signposts, triggers, and prepared pathway switches; set-based engineering narrows through tests, limit curves, trade spaces, and alternative elimination.
- Kept [Manage Innovation Programs With a Rolling Wave](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md): both defer detail until relearning, but set-based practice adds explicit feasible sets and evidence-based elimination rather than only planning horizons and phase replanning.

**Link following:**

- Followed the kept notes one hop. `changing-requirements` led to specification strategy, underspecification, silent disambiguation, and deploy-time learning; only specification strategy added a distinct source-use. `fix-what-the-executor-cant-determine` led to low-degree-of-freedom ordering and frontloading; both clarified boundaries but did not warrant another kept connection. Specification strategy led back to changing requirements and onward to spec mining/deploy-time learning; those latter notes concern recurrence and codification rather than this paper's project-level narrowing. Progressive constraining led to the spec-projection and codification cluster and confirmed that its connection should remain comparative.
- Followed the kept sources one hop. Pindyck linked to costly entrenchment, the author/executor note, and Githens; DAPP linked to the author/executor note, Githens, Pindyck, and fixed-decomposition limits; Githens linked to the author/executor note, changing requirements, PMI terminology, and PDSA. These neighborhoods revealed the four-source synthesis recorded below.
- Read `kb/notes/COLLECTION.md` before proposing inbound note links. It authorizes `evidenced-by` from notes to tracked source ingests. Reverse candidates therefore point to the future matching ingest, never to the immutable snapshot.

## Connections Found

- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) — **is-evidence-for**: the paper's practitioner-derived root-cause classification and examples bear on the note's distinction between genuine change and late discovery of an earlier bad requirement interpretation, while remaining weaker than controlled prevalence evidence.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) — **is-evidence-for**: set-based requirements and specifications provide a peer-reviewed worked case in which durable specifications remain ranged and are narrowed only when testing and cross-functional learning supply the missing premises.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) — **is-evidence-for**: the paper operationalizes the same timing rule by planning knowledge generation backward from the latest safe convergence dates and rejecting unsupported early decisions.
- [Progressive constraining commits only after patterns stabilize](../../../../notes/progressive-constraining-commits-only-after-patterns-stabilize.md) — **compares-with**: both methods preserve a wider valid set until observations warrant narrowing, but they stabilize different objects—repeated LLM interpretations versus engineering limits, requirements, specifications, and alternatives.
- [Irreversibility, Uncertainty, and Investment](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md) — **compares-with**: Pindyck explains when waiting has option value and what waiting costs; set-based engineering shows how early low-cost experiments can purchase discriminating information without making the full irreversible design commitment.
- [Dynamic Adaptive Policy Pathways](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md) — **compares-with**: DAPP prepares state-triggered pathway switches under deep uncertainty, whereas set-based engineering prepares feasible trade spaces and eliminates alternatives as tests close named knowledge gaps.
- [Manage Innovation Programs With a Rolling Wave](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md) — **compares-with**: both defer future detail until relearning, but rolling-wave planning organizes when detail is revisited while set-based practice specifies what evidence and feasible-set knowledge justify convergence.

## Bidirectional Candidates

- [Irreversibility, Uncertainty, and Investment](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md) ↔ the future matching ingest — **compares-with**: the reciprocal path would let readers move from the option-value conditions to a concrete test-before-design method that distinguishes passive waiting from acting to learn.
- [Dynamic Adaptive Policy Pathways](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md) ↔ the future matching ingest — **compares-with**: the reciprocal path exposes two operational forms of deferred commitment, one trigger/pathway-based and one trade-space/convergence-based.
- [Manage Innovation Programs With a Rolling Wave](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md) ↔ the future matching ingest — **compares-with**: the reciprocal path distinguishes progressive plan elaboration from evidence-gated narrowing of requirements, specifications, and design alternatives.

## Reverse-edge Candidates

- [Changing requirements conflate genuine change with disambiguation failure](../../../../notes/changing-requirements-conflate-genuine-change-with-disambiguation.md) → the future matching ingest, never the snapshot — **evidenced-by**: the paper supplies bounded practitioner evidence for the note's currently open empirical question about late learning reported as requirement change.
- [Specification strategy should follow where understanding lives](../../../../notes/specification-strategy-should-follow-where-understanding-lives.md) → the future matching ingest, never the snapshot — **evidenced-by**: the paper gives a sustained systems-engineering case for specifications whose precision tracks where knowledge becomes available.
- [An author should fix what the executor can't determine, not what it will](../../../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md) → the future matching ingest, never the snapshot — **evidenced-by**: the set-based front end is an external methodological witness for deferring situational choices while fixing goals, constraints, and convergence criteria.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Solve low-degree-of-freedom subproblems first to avoid blocking better designs](../../../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md) — rejected: both preserve optionality, but the paper orders work by knowledge gaps, test cost, and evidence for elimination rather than establishing the note's smallest-feasible-set-first rule.
- [Current-task fit alone does not warrant costly structural entrenchment](../../../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md) — rejected: the generic delay/optionality analogy articulates, but the paper does not address cross-question transfer or KB structural entrenchment; Pindyck is already the more precise source for that note.
- [First-principles analysis maps a design space before selecting within it](../../../../notes/first-principles-analysis-maps-design-space-before-selection.md) — rejected: parallel alternatives and trade spaces overlap, but the paper does not derive independent axes from boundary constraints or test rival decompositions.
- [PMI Lexicon of Project Management Terms, Version 4.0](../../../../sources/pmi-lexicon-project-management-terms-v4.ingest.md) — rejected: progressive elaboration is adjacent terminology, but Githens provides the more useful substantive comparison and the lexicon adds no evidence-gating mechanism.
- `kb/reference/`, `kb/agent-memory-systems/`, and `kb/agentic-systems/` candidates — rejected after complete title/description scans and focused body search because the hits were shipped-system, storage/promotion, or rollback uses of similar words rather than the paper's learning-before-convergence mechanism.

## Index Membership

None.

## Synthesis Opportunities

- The set-based paper together with [Pindyck](../../../../sources/pindyck-irreversibility-uncertainty-investment.ingest.md), [DAPP](../../../../sources/haasnoot-dynamic-adaptive-policy-pathways-2013.ingest.md), and [rolling-wave planning](../../../../sources/githens-manage-innovation-programs-rolling-wave.ingest.md) implies a higher-order claim: deferral is productive only when it preserves a valuable alternative, names how later information can discriminate among choices, and schedules or triggers narrowing early enough to act. The sources contribute different missing pieces—option-value conditions and delay cost; monitored thresholds and lead time; planned relearning horizons; and active experiments, feasible sets, and convergence gates. No single inspected note currently states that composition.

## Maintenance Observations

None.

## Flags

- The paper's case evidence is methodological and practitioner-derived rather than a controlled comparison. Any note-side `evidenced-by` use should retain that boundary and should not turn the reported rework reductions or Toyota/Wright/Teledyne examples into prevalence or causal-effect estimates.
