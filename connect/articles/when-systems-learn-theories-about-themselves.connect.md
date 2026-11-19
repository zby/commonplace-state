---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/articles/when-systems-learn-theories-about-themselves.md"
source_has_frontmatter: true
date: "2026-08-27"
depth: standard
---

# Connection Report: When systems learn theories about themselves

**Source:** [When systems learn theories about themselves](../../../../articles/when-systems-learn-theories-about-themselves.md)

## Discovery Trace

**Scope and authorisation:**

- Read the 121-line source, `kb/articles/COLLECTION.md`, and the connect-report type contract in full. The article contract authorises prospecting into notes, reference, sources, agent-memory systems, agentic systems, articles, instructions, and tasks; it excludes work and reports. The source has no `tags:` field.
- The allowed source-to-destination labels used below are: notes (`defined-in`, `evidenced-by`, `extends`, `contrasts`, `see-also`); reference and sources (`evidenced-by`, `see-also`); agent-memory and agentic systems (`evidenced-by`, `compares-with`, `see-also`); articles (`extends`, `contrasts`, `see-also`); and instructions or tasks (`procedure`).
- External attribution is authorised by the collection, but external is not a connect prospecting surface. Per the task constraint, no web search or browsing was performed.
- No scored search was available or used.

**Existing graph:**

- Ran `rg -n 'when-systems-learn-theories-about-themselves' kb/notes kb/reference kb/sources kb/agent-memory-systems kb/agentic-systems kb/articles kb/instructions --glob '*.md'`. The only authored inbound body links are from `what-bound-naurs-theory-to-programmers.md`, `theory-building-inside-the-system.md`, and `moving-revision-decisions-into-the-automatic-system.md`; `kb/articles/README.md` also lists the source.
- Inventoried every existing body link and the `source_notes` lineage in the source. Existing links were excluded from outbound recommendations even when searches surfaced them again.

**Curated heads:**

- Read `kb/notes/README.md`, `kb/reference/README.md`, `kb/sources/README.md`, `kb/agent-memory-systems/README.md`, `kb/agentic-systems/README.md`, `kb/articles/README.md`, and `kb/instructions/README.md` in full.
- The source has no tags, so there was no tag-matched README pass. Because the source itself links [Self-improving systems](../../../../tags/self-improving-systems-README.md), that curated head was followed as a one-hop neighborhood.
- `kb/tasks/` exists, but it has neither `README.md` nor `COLLECTION.md`. Its title, description, and body surfaces were still searched under the source article's explicit `procedure` trigger.

**Complete title and description listings:**

- Ran `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and the same literal command for `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/articles/`, `kb/instructions/`, and `kb/tasks/`.
- Ran `rg --sort path '^description:' kb/notes/ --glob '*.md'` and the same literal command for `kb/reference/`, `kb/sources/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/articles/`, `kb/instructions/`, and `kb/tasks/`. The tasks listing returned descriptions only for its type specs; candidate tasks were therefore evaluated from titles and bodies.

**Focused body searches:**

- Notes: `rg -n -i 'self-theor|theor(y|ies).{0,35}(system|self)|reflective self|self-representation' kb/notes/ --glob '*.md'`; `rg -n -i 'compoun(d|ding)|later improvement|later episode|accumulat(e|ion)' kb/notes/ --glob '*.md'`; `rg -n -i 'what to work on|problem-notic|direction|sub-objective|proximate target|objective.{0,30}(proxy|warrant)' kb/notes/ --glob '*.md'`; `rg -l -i 'self-theor|theor(y|ies).{0,35}(system|self)|reflective self' kb/notes/ --glob '*.md' | sort`; `rg -l -i 'later (improvement|episode)|compounding|accumulation without|counterfactually improve' kb/notes/ --glob '*.md' | sort`; `rg -l -i 'what to work on|problem-notic|sub-objective|choosing a sub-goal|direction stay|direction stays' kb/notes/ --glob '*.md' | sort`; and `rg -l -i 'retained rationale|rationale.{0,30}(transfer|revise|derive)|rules?.{0,30}theor(y|ies)' kb/notes/ --glob '*.md' | sort`. Kept the casebook, faithful-rationale, proposal-selection, repeatable-path, and objective-licensing notes because each supplies a distinct evidential or architectural boundary. Rejected narrower or duplicate paths listed below.
- Reference: `rg -n -i 'reflective self|self-improv|self-theor|theory.{0,25}(system|operation)' kb/reference/ --glob '*.md'`; `rg -n -i 'problem-notic|change candidates|what to work on|direction|function allocation|objective.{0,30}(ablat|proxy|warrant)' kb/reference/ --glob '*.md'`; and `rg -n -i 'tag-readme.{0,40}(loop|causal|search|retention)' kb/reference/ --glob '*.md'`. Kept the tag-README operative trace and the broader candidate-origin survey; rejected workflow closure detail already owned by a linked companion article.
- Sources: `rg -n -i 'computational reflection|causally connected self-representation|embedded self-theory|theor(y|ies).{0,30}(system|itself|self)' kb/sources/ --glob '*.md'`; `rg -n -i 'compounding|later episode|later improvement|recursive self-improvement' kb/sources/ --glob '*.md'`; `rg -n -i 'Prime Agent|Recuris|Apodex' kb/sources/ --glob '*.md'`; and `rg -n -i 'problem choice|what to work on|self-direction|direction.{0,30}(objective|benchmark)|objective.{0,30}(proxy|direction)' kb/sources/ --glob '*.md'`. Kept Maes plus two newer measurement boundary cases. The locally captured Schmidhuber report was evaluated but does not identify itself as the success-story algorithm named by the source; the direct Prime Agent, Recuris, and Apodex ingests were rejected as redundant with the source's existing synthesized evidence path.
- Agent-memory systems: `rg -l -i 'self-theor|theor(y|ies).{0,30}(self|system)|retained rationale|rationale.{0,20}(rule|skill|patch)' kb/agent-memory-systems/ --glob '*.md' | sort`; `rg -l -i 'compounding|later improvement|later episode|recursive self-improvement|self-modification' kb/agent-memory-systems/ --glob '*.md' | sort`; and `rg -l -i 'Prime Agent|Recuris|Apodex' kb/agent-memory-systems/ --glob '*.md' | sort`. The HyperAgents and Exo memory reviews and the trace-learning survey were evaluated, but none offered a more direct path for this article than its existing paper analysis or the system-level comparisons kept below.
- Agentic systems: `rg -n -i 'self-improv|reflective|self-modif|theor(y|ies)|rationale|compounding|later episode' kb/agentic-systems/ --glob '*.md'`. Kept Exo and Compound Engineering because they instantiate different boundaries on the article's named axes; rejected Agno, GBrain, and Autogenesis as less discriminating comparisons for this source.
- Articles: `rg -n -i 'self-theor|reflective|self-improv|compounding|later episode|continual learning|weights|direction' kb/articles/ --glob '*.md'`. Existing companion links were excluded. `continual-learning-outside-the-weights.md` survived because it develops the article's interpreter-plus-artifact premise into a distinct reader-facing substrate comparison.
- Instructions: `rg -n -i 're-record|function allocation|ablation|later episode|compounding|self-improv|self-theor' kb/instructions/ --glob '*.md'` and `rg -n -i 'agentic system|epistemic architecture|external system' kb/instructions/ --glob '*.md'`. The system-analysis and improvement-pass procedures are operator workflows, not a concrete next step for this article's external reader.
- Tasks: `rg -n -i 're-record|function allocation|ablation|later episode|compounding|self-improv|self-theor|faithful rationale|theory-mediat|reflective' kb/tasks/ --glob '*.md'` and `rg -n -i 'faithfulness|rationale|explanatory.reach|self.improv|improvement loop|theory' kb/tasks/ --glob '*.md'`. The faithfulness backlog and explanatory-reach review are repository maintenance, not reader procedures.

**Link following:**

- Followed the self-improving-systems head into the pathway-profile casebook, proposal-selection decomposition, objective boundary, compounding notes, and Commonplace evidence. This retained only targets that add something not already supplied by the article's linked definitions and evidence notes.
- Followed the casebook into Exo, the six-system evidence inventory, and the omitted-versus-frozen analysis. Exo remained a direct comparison; the latter two overlap existing source links or a sharper retained candidate.
- Followed the faithful-rationale note into its intervention test and evidence neighborhood. That confirmed that it adds a condition on the article's “retention with content” claim rather than merely repeating addressability.
- Followed `where-change-candidates-come-from-in-commonplace.md` into `tag-readme-trace-as-self-improving-loop.md` and the proposal-selection note. The two targets separate a concrete allocation trace from the broader qualification to the article's direction account.
- Followed the Agent Optimizers and shōbench ingests into the existing compounding notes. Their protocols are complementary: one has a later optimization episode but no matched fresh-start arm; the other carries whole state through one self-directed adaptation episode and starts to subtract carriers.
- Followed Exo and Compound Engineering into their memory-subsystem reviews and neighboring system comparisons. The system-level analyses remained the right granularity because the article compares whole improvement pathways rather than memory subsystems.
- Followed `continual-learning-outside-the-weights.md` into its Naur, theory-building, and bitter-lesson companions. It is a distinct continuation, while the other three are already linked by the source.

## Connections Found

### Notes

- [Real self-improving systems occupy combinations no single rung captures](../../../../notes/evidence/real-self-improving-systems-occupy-combinations-no-rung-captures.md) -- **extends**: the article profiles theory mediation, reflection, and self-improvement. This thirteen-system casebook broadens that property-grid method to reflection, cumulativity, actor allocation, and evidential limits, showing why those further dimensions also resist a single maturity ladder and adding Exo to the comparison surface.
- [Selective revision needs a faithful rationale, not just a legible one](../../../../notes/selective-revision-needs-a-faithful-rationale-not-just-a-legible-one.md) -- **extends**: the article says a revisable theory must retain the rationale from which rules were derived. The note adds the load-bearing condition that this rationale must faithfully track the basis that actually drove the result, and gives an intervention test for that condition.
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **extends**: the article discusses proposers, judges, admission, and direction in separate sections. The note unifies them as search, reject-capable evaluation, and operative retention, making clear that problem-noticing and candidate formation are parts of search rather than an unnamed function outside the loop.
- [A repeatable operative path keeps a redesign class open to revision](../../../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) -- **extends**: the article's revision-surface test asks what can change and whether the path can still be used. The note turns that into six operational checks—representation, determination, admission, installation, dependence, and continuity—scoped to one redesign class.
- [Revising an improvement objective is licensed from outside it or is not improvement](../../../../notes/revising-an-improvement-objective-is-licensed-from-outside-it.md) -- **extends**: the article says changing a candidate's judging standard is a separately authorised revision. The note supplies the missing licensing account and separates terminal-objective change from proxy revision, re-indexing, and surfaced under-specification.

### Reference

- [The tag-readme trace read as a self-improving loop](../../../../reference/tag-readme-trace-as-self-improving-loop.md) -- **evidenced-by**: the article uses the tag-README change as a codification and actor-allocation case. This operative trace maps the same episode onto search, objective, evaluation, and retention and identifies which parts ran in code and which remained human.
- [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) -- **see-also**: the article's direction section describes the maintainer as noticing the strain and choosing what to work on. This survey gives the material qualification: mechanical checks, freshness status, connect reports, and agent initiative already perform parts of noticing and candidate formation, although none promotes a candidate unattended.

### Sources

- [Computational Reflection](../../../../sources/maes-computational-reflection-1988.ingest.md) -- **evidenced-by**: the article calls computational reflection an established architectural idea and relies on causal connection and aspect-relative self-representation. Maes is the primary captured vocabulary source for those claims and for the procedural/declarative distinction.
- [Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) -- **see-also**: this newer two-phase study directly tests transfer and re-optimisation of retained harness changes. It provides a concrete later-episode protocol while exposing the exact control the article requires but the study lacks: an equally budgeted fresh start on the expanded task set.
- [Toward measuring recursive self-improvement](../../../../sources/toward-measuring-recursive-self-improvement-2090411367819809047.ingest.md) -- **see-also**: shōbench carries complete system state into fresh evaluation sessions and begins localising which carriers matter. Its single improvement episode establishes retained self-directed adaptation, not the recurrent later-episode dependence the article calls compounding.

### Agentic systems

- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo is a running reflective, cumulative, computationally allocated harness with a literal source-tree self-representation and a protected substrate under a rewritable executor. Its build/test gate and missing usefulness oracle test the article's separation of reflection, revision surface, evaluator reach, and theory mediation.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) -- **compares-with**: this analysis separates product change, retained project knowledge, a narrow reflective path through project operating instructions, and the normally frozen installed plugin. It gives a concrete boundary case for the article's warning that accumulation and “compounding” must name what object is improving.

### Articles

- [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) -- **see-also**: this companion develops the frozen-interpreter/revisable-artifact premise assumed by the source into a comparison with continual weight learning, including where the artifact route stops.

## Bidirectional Candidates

- If the outbound candidate above is accepted, [Continual learning outside the weights](../../../../articles/continual-learning-outside-the-weights.md) should also link back to the source -- **see-also**: its artifact-layer argument relies on theory building, governed writes, and interpreter-plus-text composition; the source supplies the reflective specialization, minimum architecture, and later-episode evidence tests.

## Reverse-edge Candidates

None.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Reflection makes retained lessons second-order](../../../../notes/reflection-makes-retained-lessons-second-order.md), [Design rationale must preserve unregenerable decision premises](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md), and [Use tests a decomposition locally; rationale makes transfer testable](../../../../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) -- genuine rationale and revision neighbors, but the source already links addressability and the fixed-decomposition argument. The faithful-rationale candidate supplies the sharper missing condition.
- [Oracle accumulation improves the selection environment](../../../../notes/oracle-accumulation-improves-the-selection-environment.md) -- directly resembles the Tuesday example, but the source already links both accumulation-versus-compounding notes and the tag-README trace. A further example link would not add a distinct reader need.
- [Methodological and computational closure track different changes](../../../../notes/methodological-and-computational-closure-track-different-changes.md) -- materially relevant to actor allocation, but the linked article on moving revision decisions already gives the reader-facing development and points into this distinction.
- [On Learning How to Learn Learning Strategies](../../../../sources/on-learning-how-to-learn-learning-strategies.ingest.md) -- the reward-gated, reversible incremental-self-improvement mechanism is adjacent historical lineage, but neither the ingest nor its retained snapshot identifies it as the success-story algorithm named by the source. It cannot carry that exact attribution without a matching source.
- [Prime Agent](../../../../sources/prime-agent-a-self-improving-rlm-harness.ingest.md), [Recuris](../../../../sources/recursive-experiential-working-memory-evolution.ingest.md), and [Apodex 1.1](../../../../sources/apodex-1-1-scaling-agentic-intelligence-for-complex-work.ingest.md) -- these are the direct analyses behind the named August 2026 systems. The source already links the synthesized three-system evidence note at the start of that comparison, and that note owns the direct source paths; adding three more links would duplicate its onward route.
- [HyperAgents review](../../../../agent-memory-systems/reviews/hyperagents.md) -- the code-grounded review confirms executable patch-lineage retention, but the article's load-bearing HyperAgents claim is an experimental transfer result already linked to the captured paper analysis. The review supplies no missing causal control for that result.
- [Agno AgentOS](../../../../agentic-systems/reviews/agno-agentos.md), [GBrain](../../../../agentic-systems/reviews/gbrain.md), and [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- all are legitimate self-modification cases, but none adds a more discriminating theory/compounding boundary than Exo or Compound Engineering. Keeping them would turn the article's onward path into a catalogue.
- [Run a full improvement pass on a note](../../../../instructions/run-full-improvement-pass-on-note.md) and [Ingest faithfulness literature and restore citations](../../../../tasks/backlog/ingest-faithfulness-literature-for-oversight-cost-note.md) -- both match vocabulary in the source, but neither is a concrete operational next step for the article's external reader, so the only authorised `procedure` relationship does not fit.
- [What bound Naur's theory to programmers](../../../../articles/what-bound-naurs-theory-to-programmers.md), [Theory building inside the system](../../../../articles/theory-building-inside-the-system.md), [Moving revision decisions into the automatic system](../../../../articles/moving-revision-decisions-into-the-automatic-system.md), and [The Bitter Lesson does not require everything to live in weights](../../../../articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md) -- all are genuine companion paths already linked in the source body, so they are not new candidates.

## Index Membership

None. [The articles index](../../../../articles/README.md) already lists the source under “In draft”; the notes-only self-improving-systems head is not an article membership surface.

## Synthesis Opportunities

- [Do Agent Optimizers Compound?](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md), [Toward measuring recursive self-improvement](../../../../sources/toward-measuring-recursive-self-improvement-2090411367819809047.ingest.md), and [the repeatable-path test](../../../../notes/a-repeatable-operative-path-keeps-a-redesign-class-open-to-revision.md) together imply a staged measurement design: carry complete state forward to establish retained adaptation, subtract candidate carriers to localise operative uptake, then compare later improvement from retained versus matched fresh state to identify compounding. No single current artifact states all three stages as one protocol.

## Maintenance Observations

- The article contract authorises `kb/tasks/` as a `procedure` destination, but `kb/tasks/` has neither a curated `README.md` nor a `COLLECTION.md`. Title and body search remained possible, but destination-local routing and intended reader posture were unavailable.

## Flags

- **Direction tension:** [Where change candidates come from in Commonplace](../../../../reference/where-change-candidates-come-from-in-commonplace.md) says the single tag-README trace understates how much problem-noticing and candidate formation already run through mechanical checks, freshness tracking, connect reports, and agent initiative. It agrees that promotion remains explicit, but the source's phrasing can be read as assigning the whole direction function to the maintainer.
- **Historical-source gap:** the source names Schmidhuber's success-story algorithm, while the local 1994/95 capture and ingest describe “incremental self-improvement” and do not use the named term. The mechanisms may belong to the same lineage, but the exact attribution is not locally grounded by the candidate found in this pass.
- **Split candidate:** the source makes independent claims about property taxonomy, theory content, loop architecture, evidence standards, empirical systems, Commonplace allocation, and direction, and this pass found more than five genuine note connections across several of those areas. Its explicit article purpose is synthesis, so this is a review signal rather than an automatic recommendation to split.
