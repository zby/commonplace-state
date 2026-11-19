---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/explanation-based-generalization-unifying-view.md"
source_has_frontmatter: true
date: "2026-08-31"
depth: standard
---

# Connection Report: Explanation-Based Generalization: A Unifying View

**Source:** [Explanation-Based Generalization: A Unifying View](../../../../sources/.snapshots/explanation-based-generalization-unifying-view.md)

## Discovery Trace

**Source analysis:**

- The paper defines EBG from four explicit inputs: a goal concept, one positive training example, a domain theory, and an agent-and-task-relative operationality criterion. It constructs a proof of concept membership, regresses the goal through that proof, and returns an operational sufficient condition. Its distinct secondary claims concern specialization rather than complete re-expression, imperfect theories, combinations with empirical learning, and learning-task formulation.
- `kb/sources/COLLECTION.md` authorizes prospecting in `notes`, `reference`, `agent-memory`, `agentic-systems`, and `sources`; it excludes `work` and `instructions`. The snapshot is immutable, so every outbound candidate below is for a future authored companion, normally the matching ingest.

**Curated heads and full-title scans:**

- Read `kb/notes/README.md` and, after following the strongest candidate's `learning-theory` tag, `kb/notes/learning-theory-README.md`. Generated the full title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'`. The strongest title-level candidates concerned theory-mediated learning, actionability, instance-to-rule warrant, and theory-derived operational fast paths.
- Read `kb/reference/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/reference/ --glob '*.md'`. No shipped-system document depends specifically on EBG; generic source-adoption and codification documents were rejected as destination-trigger mismatches.
- Read `kb/agent-memory-systems/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/agent-memory-systems/ --glob '*.md'`. The cross-system trace-learning synthesis survived; individual trajectory learners did not, because selecting one would be arbitrary and the synthesis owns the shared comparison axis.
- Read `kb/agentic-systems/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/agentic-systems/ --glob '*.md'`. No whole-harness analysis had a specific EBG dependency or comparison worth authoring.
- Read `kb/sources/README.md` and ran `rg -N --no-heading -m1 '^# ' kb/sources/ --glob '*.md'`. Theory refinement and the Bitter Lesson were the strongest source-level comparisons.

**Description listing scans:**

- Ran `rg '^description:' kb/notes/ --glob '*.md'`, `rg '^description:' kb/reference/ --glob '*.md'`, `rg '^description:' kb/agent-memory-systems/ --glob '*.md'`, `rg '^description:' kb/agentic-systems/ --glob '*.md'`, and `rg '^description:' kb/sources/ --glob '*.md'`.
- Notes scan kept the two theory-mediated notes and the actionability definition. Reference and agentic-systems produced no articulated candidate. Agent-memory kept only the trace-learning synthesis. Sources kept the proof-guided theory-refinement paper and Sutton's scaling counterpoint.

**Body search:**

- `rg -n -i 'explanation-based|explanation based|goal regression|operationality criterion|domain theory|theory-guided' kb/notes/ --glob '*.md'` -- found the exact DOI use in the theory-mediated-system-learning note plus neighboring theory-guided claims.
- `rg -n -i 'single (positive )?(training )?example|generaliz(e|ation).*example|example.*generaliz(e|ation)|analytic(al)? and empirical|empirical and analytic(al)?|similarity-based' kb/notes/ --glob '*.md'` -- surfaced the single-instance warrant boundary and theory-mediated sample-efficiency conjecture; the former was rejected because it concerns outcome/process fidelity rather than proof-relative concept membership.
- `rg -n -i 'operationali[sz]|reformulat|partial evaluation|compile.*knowledge|search heuristic|heuristic.*search' kb/notes/ --glob '*.md'` -- kept the actionability antecedent and rejected frontloading as a surface analogy.
- `rg -n -i 'explanation-based|explanation based|goal regression|operationality criterion|domain theory|theory-mediated' kb/reference/ --glob '*.md'` -- no specific reference candidate.
- `rg -n -i 'explanation-based|explanation based|goal regression|operationality criterion|domain theory|theory-mediated|generaliz(e|ation).*example|example.*generaliz(e|ation)' kb/agent-memory-systems/ --glob '*.md'` and the focused follow-up `rg -n -i 'distill.*(rule|lesson|skill)|trajectory.*(rule|lesson|skill)|proof-guided|explanation.*general|generaliz.*(trajectory|experience|lesson)' kb/agent-memory-systems/ --glob '*.md'` -- kept the survey-level analytic-versus-empirical comparison and rejected individual-system links.
- The equivalent EBG query over `kb/agentic-systems/` produced no articulated candidate.
- `rg -n -i 'explanation-based|explanation based|goal regression|operationality criterion|domain theory|similarity-based' kb/sources/ --glob '*.md'`, `rg -n -i 'single (positive )?(training )?example|generaliz(e|ation).*example|example.*generaliz(e|ation)|analytical and empirical|analytic and empirical|empirical and analytic|theory refinement' kb/sources/ --glob '*.md'`, and `rg -n -i 'operationali[sz]|reformulat|search heuristic|heuristic.*search|incomplete theor|intractable theor|inconsistent theor' kb/sources/ --glob '*.md'` -- kept the EITHER theory-refinement ingest and the Bitter Lesson; No Free Lunch was rejected as a broader, less discriminating inductive-bias companion.
- `rg -n -i '10\.1023/A:1022691120807|Explanation-Based Generalization: A Unifying View|Explanation-based generalization' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- found one current durable use: the theory-mediated-system-learning note's direct DOI link.

**Link following:**

- Followed [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) to the EITHER ingest and the sample-efficiency conjecture. This confirmed that EBG supplies the established complete-theory antecedent while EITHER owns imperfect-theory repair.
- Followed [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) through its trajectory-run, readable-artifact, and open-problem sections. Individual systems such as ExpeL repeat the empirical trace-to-rule pattern; the synthesis is the useful comparison target because it names the shared missing evaluation problem.
- Followed the learning-theory curated head. It routes both the theory-derived fast-path note and discovery/reach notes, but no index claims membership for source artifacts, so no index-membership candidate was retained.

## Connections Found

These are candidate edges for the snapshot's future authored companion, not edits to the immutable snapshot.

- [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) -- **is-evidence-for**: EBG is the note's named historical case in which an explicit domain theory determines how an experience is interpreted and generalized; the paper also bounds that lineage to a complete theory of an external task rather than reflective theory revision.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- **is-evidence-for**: EBG supplies a proof-relative mechanism for extracting a justified sufficient condition from one example, bearing on the theory-mediated pathway while providing no empirical test of retained-theory reuse across a shift.
- [Actionable methodology](../../../../notes/definitions/actionable-methodology.md) -- **is-evidence-for**: the paper explicitly treats operationality as relative to an agent and task and requires the learned definition to be usable there, supplying a narrow historical antecedent for the definition's operator-relative relation without establishing its fuller access-and-authority conditions.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with**: EBG makes goal, domain theory, proof, and output form explicit before generalization, whereas the surveyed trajectory-to-rule systems usually use successful or failed traces plus heuristic or judge-mediated distillation; the comparison isolates explanation-grounded generalization as a missing or alternative evaluation path.
- [Theory Refinement Combining Analytical and Empirical Methods](../../../../sources/theory-refinement-analytical-empirical-methods.ingest.md) -- **compares-with**: EITHER directly addresses EBG's open imperfect-theory and analytic-plus-empirical agenda by using proof structure to localize defects and induction to repair a fallible Horn theory.
- [The Bitter Lesson](../../../../sources/sutton-the-bitter-lesson-original-essay.ingest.md) -- **compares-with**: Sutton supplies the later scaling counterpressure to EBG's reliance on supplied domain knowledge, making the shared axis whether explicit theory is learned and tested by a scalable meta-method or remains hand-built structure that limits growth.

## Bidirectional Candidates

None. A durable return link must target a tracked ingest rather than the immutable local snapshot, and no matching ingest path exists yet.

## Reverse-edge Candidates

None. The source contract forbids durable links to `.snapshots/`, and candidate paths must already exist.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A checked outcome licenses retaining an episode, not abstracting its explanation](../../../../notes/checked-outcome-licenses-episode-retention-not-abstraction.md) -- rejected because it concerns whether an execution trace faithfully produced an outcome; EBG instead proves concept membership relative to a supplied formal theory, so the apparent single-example overlap does not establish the same relation.
- [Frontloading is partial evaluation, not divide-and-conquer](../../../../notes/frontloading-is-partial-evaluation-not-divide-and-conquer.md) -- rejected because both specialize a general object with known inputs, but EBG goal regression is not the note's execution-context-saving instruction materialization mechanism.
- [The No Free Lunch Theorem](../../../../sources/no-free-lunch-theorem-no-universal-learning-algorithm.ingest.md) -- rejected because its broad inductive-bias point is genuine background but does not discriminate EBG as sharply as the direct imperfect-theory successor and Sutton's domain-knowledge scaling counterpoint.
- [ExpeL](../../../../agent-memory-systems/reviews/expel.md) -- rejected as an arbitrary individual instance; the trace-learning synthesis already carries the reader-useful comparison across ExpeL and its peers.
- [Source-adoption policy](../../../../reference/source-adoption-policy.md) -- rejected because Commonplace's current adoption procedure does not depend specifically on EBG's learning mechanism.

## Index Membership

None.

## Synthesis Opportunities

None. The higher-order combination of EBG's theory-mediated inference, EITHER's fallible-theory repair, and contemporary editable artifacts is already owned by [Theory-mediated system learning combines runtime self-modeling with empirical theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md).

## Maintenance Observations

- The exact DOI is cited directly by the theory-mediated-system-learning note, but this snapshot has no matching tracked ingest. Because durable source links may not target `.snapshots/`, the authored source surface needed to replace or qualify that direct citation is absent. This report records the gap without creating that ingest.

## Flags

- **Split-candidate signal:** the six retained candidates span the core EBG mechanism, situated operationality, modern trace-learning comparison, imperfect-theory repair, and scaling critique. Any future authored source analysis should keep those independent contributions visibly separated rather than presenting one undifferentiated claim.
