---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md"
source_has_frontmatter: true
date: "2026-07-26"
depth: standard
---

# Connection Report: A proximate target is checked for achievement, not for warrant

**Source:** [A proximate target is checked for achievement, not for warrant](../../../../notes/a-proximate-target-is-checked-for-achievement-not-for-warrant.md)

Source collection: `kb/notes/` (theoretical profile). Authorised destinations read from `kb/notes/COLLECTION.md`: `notes` (`extends`, `grounds`, `enables`, `exemplifies`, `mechanism`, `contradicts`, `contrasts`), `notes/definitions` (`defined-in`), `reference` / `agent-memory-systems` / `agentic-systems` / `sources` (`evidence`, `derived-from`, `abstracted-from`, `see-also`), `instructions` (`operationalized-from`, `see-also`; rare, usual direction inverse). `kb/work/` excluded.

Already linked from the source (not re-proposed): `self-improvement-is-relative-to-a-declared-objective`, `fixed-artifacts-split-into-exact-specs-and-proxy-theories`, `weakly-discriminated-qualities-tend-to-be-underselected`, `oracle-strength-spectrum`, `warranted-autonomy-is-bounded-by-oracle-domain`, `first-principles-are-inherited-constraints-not-design-choices`, `reflection-buys-addressability`, `first-principles-reasoning-selects-for-explanatory-reach-over` (inline), `../reference/design-rationale-management.md`.

Existing inbound edges (backlink sweep `rg -l "a-proximate-target-is-checked-for-achievement-not-for-warrant" kb/`): `kb/notes/self-improvement-is-relative-to-a-declared-objective.md` (`extends`) and `kb/notes/self-improving-systems-README.md` (Membership section). Both already authored; not proposed again.

## Discovery Trace

**Curated heads read:**
- `kb/notes/self-improving-systems-README.md` — selective head, no `complete` mark. Already links the source in `## Membership`. Its `## Pathway profile` and `## Placements` sections routed to `real-self-improving-systems-occupy-combinations-no-rung-captures.md`, `revising-an-improvement-objective-is-licensed-from-outside-it.md`, `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md`, `methodological-and-computational-closure-track-different-changes.md`.
- `kb/notes/foundations-README.md` — no `complete` mark; source not listed. Flagged `technical-constraints-make-kb-objective-choice-engineering` is absent here too; routed instead via title listing. Head surfaced `first-principles-are-inherited-constraints-not-design-choices` (already linked) and `../reference/design-rationale-management.md` (already linked).
- `kb/notes/evaluation-README.md` — no `complete` mark; source not listed; head is scoped to empirical observations and surfaced only `brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md` (rejected below).
- No tag-README declared `complete: true`, so no by-tag `rg` sweeps were skipped.

**Full titles listing:**
- `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` (~37KB, full claim-title surface), then filtered with `grep -iE "proxy|goodhart|objective|target|oracle|verdict|warrant|rationale|justif|gate|criteri"` — 26 hits. Kept for evaluation: `revising-an-improvement-objective-is-licensed-from-outside-it`, `technical-constraints-make-kb-objective-choice-engineering`, `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one`, `measuring-autonomy-...`, `brainstorming-maintainability-oracles-for-agentic-development`, `criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts`, `verification-needs-a-typed-target-before-it-needs-an-oracle`.
- `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'` — surfaced `commonplace-as-a-reflective-system`, `commonplace-declared-frame`, `tag-readme-trace-as-self-improving-loop`, `full-improvement-pass-closure`, `where-change-candidates-come-from-in-commonplace`, `control-plane-goals`.
- `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ kb/agent-memory-systems/ kb/notes/definitions/ kb/instructions/ --glob '*.md'` — no candidate cleared the articulation test in `agentic-systems`, `agent-memory-systems`, `definitions`, or `instructions`.

**Description listing scan:**
- Batched `rg -N -m1 '^description:'` over 18 shortlisted `kb/notes/` paths and 5 `kb/reference/` paths. Kept on description alone: `technical-constraints-...` ("goals set the loss, contracts and profiles specialize it, and oracle strength differs per profile") and `tag-readme-trace-as-self-improving-loop` ("showing which half of each step runs in code and which stays human").

**Body search:**
- `rg -l -i "Goodhart" kb/notes/` → `brainstorming-maintainability-oracles-for-agentic-development.md`, `verifiability-gradient.md`, `inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md`, `quality-signals-for-kb-evaluation.md`. Read the surrounding context in all four; only the first survived (see Rejected).
- `rg -n -i "held to serve|linking claim" kb/ --glob '*.md'` → the source itself, `self-improving-systems-README.md`, `self-improvement-is-relative-to-a-declared-objective.md:46`, and `kb/log.md:25` (the origin log entry for this note). The vocabulary is not reused anywhere else — confirms the source is the sole owner of the term.
- `rg -l -i "proxy" kb/notes/` → 22 files; most are oracle-level (verdict position) and were filtered out by the source's own daylight argument.
- `rg -l -i "structural propert" kb/notes/ kb/reference/` → 12 notes, 0 reference. Kept `document-types-should-be-verifiable.md`.
- `rg -n -i "petrovska|self-adaptive|adaptation goal|domain goal" kb/sources/ kb/work/` → `defining-self-adaptive-systems-systematic-literature-review.ingest.md` and `weyns-software-engineering-self-adaptive-systems-tour.md` carry the domain-goal / adaptation-goal split that `kb/log.md:25` records as the *route not taken* when this note was drafted. Not proposed as an edge (see Maintenance Observations).
- `rg -n -i "calibrat" kb/notes/brainstorming-maintainability-oracles-for-agentic-development.md` → located its `### Oracle strength versus target alignment` section, which states the source's distinction independently.

**Link following:**
- From `real-self-improving-systems-occupy-combinations-no-rung-captures.md` one hop → `measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md` (its footer's `extends` target). Re-filtered and kept: that note is where the source's closing "profiles cannot rank architectures" consequence is left unresolved.
- From `selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` one hop → `../sources/concept-bottleneck-models.ingest.md` and `../sources/towards-faithfully-interpretable-nlp-systems.ingest.md`. Both are reachable via the rationale note rather than needed directly; not proposed (the source's need is the *stated-ness* of the linking claim, and the faithfulness note already carries that chain).
- From `brainstorming-maintainability-oracles-for-agentic-development.md` one hop → `../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md` (evaluated, rejected — see Rejected).
- From `tag-readme-trace-as-self-improving-loop.md` one hop → `tag-readme-trace-observed-causal-connection.md` and `commonplace-as-a-reflective-system.md`; neither adds beyond the trace note itself.

## Connections Found

- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md) — **contrasts**: that note's first subtraction ("proxy revision") disposes of most apparent objective changes by pointing out that replacing a gate is assessed empirically against an unchanged objective — "an ordinary empirical question with a determinate answer, no meta-criterion required." The source names a proxy the subtraction cannot reach: a proximate target is not in the verdict position, so there is no discrimination to compare and no verdict stream to assess a replacement against. Neighbouring shapes, sharply different consequences — exactly the `contrasts` reader-need.

- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) — **grounds**: the source's closing section asserts "A profile of structural properties selects no ordering by itself; that much is a claim about the descriptive space." The casebook is where that premise is established rather than asserted — eight placements showing "No canonical ordering follows from the profile alone." A reader who wants to verify the premise goes here. Note the casebook's next sentence ("A declared objective can supply those priorities; the profile cannot") is precisely what the source qualifies; see Flags.

- [Measuring autonomy well enough to see it improve is an open problem](../../../../notes/measuring-autonomy-well-enough-to-see-it-improve-is-an-open-problem.md) — **extends**: the source ends by saying a linking claim is doing the work wherever architectures are ranked. That note is where the ranking is actually attempted and fails: a per-function allocation profile locates one system but supports no comparison across systems or time, and its second open question floats adopting "a rough, admittedly imprecise proxy" weighted by scope — a proximate target being considered for adoption with its linking claim unstated. The developed case of the source's closing consequence.

- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) — **extends**: the source requires that "the linking claim has to be stated" because an unrecorded justification cannot be found false, and its third open question asks whether a pathway can hold its linking claims addressably. That note develops exactly this requirement one step further and sharpens it: stating the rationale is not sufficient, because a legible-but-unfaithful rationale makes repair *confidently wrong* rather than merely uninformed, and the test is intervention rather than inspection. A reader who accepts the source's stated-ness requirement needs this to know what stating it has to achieve.

- [Brainstorming: maintainability oracles for agentic development](../../../../notes/brainstorming-maintainability-oracles-for-agentic-development.md) — **extends**: its `### Oracle strength versus target alignment` section reaches the source's distinction independently in a concrete domain — "A check can be reliable and still measure the wrong target... an exact complexity threshold may be a hard oracle for its metric while remaining a weak oracle for future change cost" — and turns it into a two-test procedure (does the signal discriminate its stated observable; does that observable predict the target and horizon we care about). Its leading/lagging calibration architecture is a candidate answer to the source's second open question, whether calibration against delayed outcomes can reach the linking claim.

- [Technical constraints turn KB objective-function choice from philosophy into engineering](../../../../notes/technical-constraints-make-kb-objective-choice-engineering.md) — **contradicts**: that note's fourth constraint makes verifiability a first-class *selection* criterion — "an objective you can score cheaply beats an objective you merely believe is deeper." The source says that a strong achievement check "delivers exactly the signature of a verified property" while supplying no evidence for the linking claim, and that this is how a target outcompetes the objective it was adopted to serve. The same design decision, pulled in opposite directions. See Flags — the writer should decide whether this is a genuine contradiction or a scope refinement before authoring.

- [Abstract an experience into a lesson only when you can state where the lesson stops](../../../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md) — **grounds**: the source's first open question conjectures that a good proximate target is one whose linking claim has explanatory-reach — "ones that say why the property produces the outcome, and so predict where it would stop." That note is where the boundary-statement test is argued for retained lessons, so the conjecture is not free-standing: the premise it rests on is already worked one level down. Lower confidence than the entries above; the writer should check whether the transfer from lessons to targets survives before committing an inline edge.

- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) — **evidence**: a shipped, worked instance of the source's central claim inside Commonplace. The `complete` mark is a structural property with a validator-enforced achievement check, and that document states the gap in its own words: "the validator passing means the marks are consistent, not that the type split actually made the KB better. Evaluating the *objective* is mechanical; evaluating whether the objective was worth adopting is not." That is the achievement-versus-warrant split, observed rather than theorized.

## Bidirectional Candidates

- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) ↔ source — **extends**: the casebook's "A declared objective can supply those priorities" is stated without the qualification the source adds (an objective over outcomes still cannot rank architectures without a structure-to-outcome claim). The parent note `self-improvement-is-relative-to-a-declared-objective.md` already carries that qualification inline; the casebook does not, and a return edge would keep the two consistent.

- [Technical constraints turn KB objective-function choice from philosophy into engineering](../../../../notes/technical-constraints-make-kb-objective-choice-engineering.md) ↔ source — **contradicts** is symmetric in `kb/notes/COLLECTION.md`, so if the outbound edge is authored the return edge follows by the label's kind. Independently useful: that note's three-level objective hierarchy (global goals → collection quality goal → profile bundle) is a live instance of the source's "a target can stand in for another target, and the chain terminates wherever the analysis declares its objective."

## Reverse-edge Candidates

- [Document types should be verifiable](../../../../notes/document-types-should-be-verifiable.md) → source — **exemplifies** (authorised instance→general edge in `kb/notes/COLLECTION.md`): that note argues for verifiable structural properties as the design target for document types and closes by conceding the linking claim is unmeasured — "Types are an optimization for navigation, not a correctness requirement... an agent that ignores the type field entirely and reads every document should still work — just less efficiently." Verifiability is pursued because it is held to serve navigation efficiency; whether it does is not what the type validator checks. Same collection, so this is a candidate for a future connect run on that note rather than an edit here.

- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) → source — **rationale** (`kb/reference/COLLECTION.md` authorises `rationale` into `kb/notes/` as the primary theory-ward edge): the paragraph quoted above currently states the achievement/warrant gap without citing the claim that names it. The reference collection's own rules make this the natural direction; the outbound `evidence` edge proposed above is the complement, not a substitute.

## Off-authorisation Candidates

None. Every candidate that passed the articulation test found a label in the source's authorised set for its destination.

## Raw Text Candidates

None. All candidates carry frontmatter.

## Rejected Candidates

- [Huxley-Gödel Machine (ingest)](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) — the closest external hit ("immediate benchmark score is a weak parent-selection signal... clade-metaproductivity better predicts productive lineages"), and rejected on the source's own argument. Benchmark score there is a *selection* signal — a proxy in the verdict position that mis-ranks. That is the criterion-to-objective relation the source explicitly calls "the well-worked case" and sets aside. Using it as `evidence` would corroborate the neighbouring claim, not this one, and would blur the daylight the note is built to draw.

- [Quality signals for KB evaluation](../../../../notes/quality-signals-for-kb-evaluation.md) — catalogues structural proxies (orphan rate, index coverage, title-as-claim ratio) and raises Goodhart directly, but every signal is proposed for a composite *oracle*: "the proxy correlates with the real objective but doesn't guarantee it, so you can satisfy the signal without satisfying quality." Verdict position throughout. The contrast is already carried by `oracle-strength-spectrum`, which the source links.

- [Verifiability gradient](../../../../notes/verifiability-gradient.md) — its loosen rule ("a test passing while quality regresses... When the check that justified a constraint breaks, the constraint loses its warrant") is the closest structural rhyme found, but it is stated over checks, and its remedy (move the artifact down the gradient) presupposes the verdict stream a proximate target does not have.

- [Inspectable artifact, not supervision, defeats the blackbox problem](../../../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — "Goodharting on evals" appears only as one row of an ML-failure-mode analogy table. Keyword-only match.

- [Brainstorming: how to test whether pairwise comparison can harden soft oracles](../../../../notes/brainstorming-how-to-test-whether-pairwise-comparison-can-harden.md) — surfaced by the `evaluation` tag head. Entirely about hardening a judge in the verdict position; nothing about the goal position.

- [The declared Commonplace frame](../../../../reference/commonplace-declared-frame.md) — declares boundary and actor partition, not an objective or a target. No purchase on the source's claim.

- [Defining Self-adaptive Systems: A Systematic Literature Review (ingest)](../../../../sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md) — carries the domain-goal / adaptation-goal split, which is the nearest external vocabulary. `kb/log.md:25` records it as a *route not taken* and deflated during drafting ("those goals are instrumental to the objective rather than a second objective"). Linking it now would reopen a settled decision without new evidence; recorded in Maintenance Observations instead.

- `kb/instructions/` — swept the full title listing; no procedure adds ordering, defaults, or stopping conditions to this methodology, so no `operationalized-from` candidate exists. The collection's stated rarity for this direction holds.

- `kb/agentic-systems/`, `kb/agent-memory-systems/`, `kb/notes/definitions/` — swept; no candidate cleared the articulation test. The source's four levels are all defined in-line, so no `defined-in` edge is needed.

## Index Membership

- [foundations-README](../../../../tags/foundations-README.md) — the source carries `tags: [foundations, ...]` and the head does not list it. It would belong under the head's `### Self-improving systems` grouping, or alongside `first-principles-are-inherited-constraints-not-design-choices` (which the source contrasts with). The head carries no `complete` mark, so the omission is not a mark violation.
- [self-improving-systems-README](../../../../tags/self-improving-systems-README.md) — already links the source in `## Membership`; no entry needed.
- [evaluation-README](../../../../tags/evaluation-README.md) — the source carries `tags: [..., evaluation]` but the head is scoped to "empirical observations about KB operations and prompt design," which this theoretical claim is not. Adding an entry would strain the head's stated scope; see Maintenance Observations.

## Synthesis Opportunities

`selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md` plus this source together imply a claim neither states: the intervention test for rationale faithfulness is the only available check on a *target's* linking claim, because the linking claim has no verdict stream of its own. That would answer the source's second and third open questions jointly — a linking claim held addressably is testable exactly to the extent that intervening on it moves the pathway's commitments. Not written; flagged only.

## Maintenance Observations

- **Route-not-taken record is at risk of being lost.** `kb/log.md:25` records that the Petrovska et al. domain-goal / adaptation-goal split was considered and deflated when this note was drafted, and that the salvage came from "the profile note's Petrovska paragraph, which is otherwise redundant and pending deletion." That deletion appears not to have happened — `kb/sources/defining-self-adaptive-systems-systematic-literature-review.ingest.md` still carries "Domain goals versus adaptation goals... [quick-win]" as an open follow-up action, and its integration section still proposes updating the self-improving-systems head with the domain-goal dimension. Either the ingest's follow-up should be marked resolved-and-declined, or the decision should be recorded somewhere the ingest's reader will see it.

- **Tag/head scope mismatch.** The source carries `tags: [foundations, self-improving-systems, evaluation]`, but `evaluation-README.md` declares itself "empirical observations about KB operations, prompt design, and techniques from other systems." A theoretical claim about what a check establishes does not fit that description. Either the tag is wrong on this note or the head's scope statement is narrower than the tag's actual membership.

- **Report-template link depth is wrong.** `kb/cache/types/connect-report.md`'s template writes candidate links as `../../notes/target.md`, which from `kb/cache/connect/<collection>/` resolves to `kb/reports/notes/` and does not exist. Correct depth is `../../../notes/`. Several committed connect reports (e.g. `a-knowledge-base-holds-theories-descriptions-and-prescriptions-with-asymmetric-linking.connect.md`) copied the template's depth. This report uses the correct depth. Reports are gitignored and regenerable, so the fix belongs in the type template rather than in the existing reports.

## Flags

- **Unresolved tension, `technical-constraints-make-kb-objective-choice-engineering`.** Its fourth constraint treats an objective's cheap verifiability as a legitimate reason to prefer it; the source treats the resulting green gate as the mechanism by which a target displaces the objective. Both are defensible and they do not obviously reduce to each other — one is about choosing *what to steer on* under a verification budget, the other about what the steering then establishes. Proposed as `contradicts`, but a writer may instead conclude the tension dissolves once the technical-constraints claim is read as scoped to the criterion level. Flagged rather than resolved.

- **Direction ambiguity, `real-self-improving-systems-occupy-combinations-no-rung-captures`.** The casebook is proposed as `grounds` outbound and `extends` inbound. If only one edge is authored, the inbound one is more load-bearing: the casebook currently states the unqualified version of a claim the source narrows.

- Not a split candidate. The source makes one assertion (the target level is checked for achievement, not warrant) and its five candidate destinations across three topic areas all serve that single assertion.

- No no-connections finding: eight outbound candidates, two bidirectional, two reverse-edge.
