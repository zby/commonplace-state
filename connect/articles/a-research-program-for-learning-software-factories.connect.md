---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/reports/types/connect-report.md
source: "kb/articles/a-research-program-for-learning-software-factories.md"
source_has_frontmatter: true
date: "2026-09-02"
depth: standard
---

# Connection Report: A research program for learning software factories

**Source:** [A research program for learning software factories](../../../../articles/automated-software-houses-with-fixed-llms.md)

## Discovery Trace

**Description listing scan:**

- Read the curated heads [notes/README.md](../../../../notes/README.md), [reference/README.md](../../../../reference/README.md), [sources/README.md](../../../../sources/README.md), [agent-memory-systems/README.md](../../../../agent-memory-systems/README.md), [agentic-systems/README.md](../../../../agentic-systems/README.md), [articles/README.md](../../../../articles/README.md), and [instructions/README.md](../../../../instructions/README.md). `kb/tasks/` has neither `README.md` nor `COLLECTION.md`, so it had no curated head. The source has no `tags:` field, so no matching tag-README or by-tag `rg` pass applied.
- Generated every destination's fresh title surface with `rg -N --no-heading -m1 '^# ' kb/<destination>/ --glob '*.md'` for `notes`, `reference`, `sources`, `agent-memory-systems`, `agentic-systems`, `articles`, `instructions`, and `tasks`. The note surface exposed the factory-learning, theory-mediation, causal-evidence, compounding, and oracle clusters; the other surfaces exposed Commonplace's declared frame, empirical rival mechanisms, whole-system self-improvement cases, the two companion articles, and no relevant instruction or task.
- Ran whole-destination description listings with `rg '^description:' kb/<destination>/ --glob '*.md'` over the same eight destinations. Kept the note candidates evaluated below, [Commonplace's declared frame](../../../../reference/commonplace-declared-frame.md), [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md), [Exo](../../../../agentic-systems/reviews/exo.md), and [The decisions that stay human, and what would move them](../../../../articles/the-decisions-that-stay-human-and-what-would-move-them.md). Source descriptions surfaced the three historical factory-constructor ingests, the Gödel-machine ingest, Agent Optimizers, and Harness Updating, but their source-level details are already carried by linked notes or would introduce a new empirical claim rather than support one the article currently makes.

**Topic indexes:**

- [Articles](../../../../articles/README.md) identifies this source as the series opener and the human-decision and Bitter-Lesson pieces as its two live companions. The Bitter-Lesson article is already linked in both directions; the human-decision article links back to this source but the source does not yet offer its readers that distinct continuation.
- [Notes](../../../../notes/README.md) routes the source's main question into the deploy-time-learning and self-improving-system theory. No matching tag index was required because the article carries no tags.
- [Agent Memory Systems](../../../../agent-memory-systems/README.md) routes competing trace-derived artifact and policy mechanisms through its trace-learning survey; [Agentic Systems](../../../../agentic-systems/README.md) supplies whole-harness cases, of which Exo is the strongest comparison on rewrite reach and oracle limits.
- [Reference](../../../../reference/README.md) identifies [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md), already linked from the article, and the declared-frame record behind its human-inclusive boundary claim. The source, instructions, and task heads supplied no additional index membership.

**Body search:**

- `rg -n -i 'software factor|factory learn|better factor|successor factor|project theor|theory[- ]mediat|theory[- ]holding|retained theor|self[- ]improv|oracle problem|learning transition|experience-responsive|production experience|fact-matched|plain retention|trajectory reuse|delayed feedback|recursive self|compounding' kb/notes/ --glob '*.md'` -- kept [Factory-learning mechanisms should be compared on the same causal job](../../../../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md), [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md), [Disconnected witnesses do not establish a full causal path through theory](../../../../notes/disconnected-witnesses-do-not-establish-a-theory-mediated-path.md), and [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md). [Citing retained theory at the decision point is a mediation trace](../../../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) passed the articulation test but was rejected as a narrower constituent of the disconnected-witnesses/full-path candidate. [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) was rejected because the article already links the more specific better-factory comparison that applies the same condition.
- `rg -l -i 'software factor|project theor|theory[- ]mediat|retained theor' kb/<destination>/ --glob '*.md'`, `rg -l -i 'self[- ]improv|continual learn|experience-responsive|successor factor|production experience' kb/<destination>/ --glob '*.md'`, and `rg -l -i 'oracle|ablation|withhold|trajectory reuse|compounding|fact-matched' kb/<destination>/ --glob '*.md'` were run separately over `reference`, `sources`, `agent-memory-systems`, `agentic-systems`, `articles`, `instructions`, and `tasks`. Reference kept the declared frame; source hits were rejected as already discharged through the article's linked notes or as new empirical branches; agent-memory kept the trace-learning survey; agentic-systems kept Exo and rejected Autogenesis as a second broad self-evolving-harness example with less incremental reader value; articles kept the human-decision companion; instructions and tasks had no concrete next-step candidate.
- `rg -n 'a-research-program-for-learning-software-factories' kb/ --glob '*.md' --glob '!articles/a-research-program-for-learning-software-factories.md' --glob '!reports/**'` -- confirmed existing inbound links from both companion articles and from [Theory-mediated learning joins self-modeling and theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md), plus current index membership. The note-to-article edge is outside the notes collection's authorised destination set and is recorded under Maintenance Observations rather than treated as a valid reverse-edge candidate.

**Link following:**

- Followed [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) one hop to its mediation-trace and delayed-feedback notes. This confirmed that the full functional decomposition is the best onward path, while [Citing retained theory at the decision point is a mediation trace](../../../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) is useful evidence detail but too narrow to add independently.
- Followed [Factory-learning mechanisms should be compared on the same causal job](../../../../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) to [Open-ended improvement must allocate search before decisive evaluation is available](../../../../notes/open-ended-improvement-allocates-search-before-evaluation.md) and the article's already-linked experiment-contrast note. The mechanism comparison remains the higher-value target because it names the rival families, fact-matching requirement, and common causal job together.
- Followed [Disconnected witnesses do not establish a full causal path through theory](../../../../notes/disconnected-witnesses-do-not-establish-a-theory-mediated-path.md) to the interpretation/retention/read-back decomposition and mediation trace. It directly develops the article's production-time-recording requirement and staged diagnostic path, rather than merely sharing terminology.
- Followed [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) to its Agent Optimizers and Harness Updating source analyses. The note is the appropriate reader path because it states what the studies establish and do not establish; direct article-to-ingest links would make the article carry empirical comparisons it currently does not make.
- Followed the article's existing [Commonplace as an instrument](../../../../reference/commonplace-as-an-instrument.md) link to [Commonplace's declared frame](../../../../reference/commonplace-declared-frame.md). The latter is the operative boundary record for the article's statement that current Commonplace evidence is human-inclusive.
- Followed [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) to Trajectory-Informed Memory Generation, Incremental Self-Improvement, and several code-grounded trace-to-artifact systems. The survey gives the article a concrete comparison surface for its named trajectory-reuse, direct-update, and learned-policy rivals without selecting one implementation as representative.
- Followed [Exo](../../../../agentic-systems/reviews/exo.md) to its memory-subsystem review and oracle discussion. Exo passes the articulation test as a whole-system comparison on editable reach and weak semantic evaluation; Compound Engineering is already linked by the article, and Autogenesis would add a second broad example without a distinct reader need.
- External prospecting was skipped as required. The already-loaded external targets are the issue tracker and Sutton's essay; both are already linked, so neither creates a candidate.

## Connections Found

- [Theory-mediated self-improvement needs interpretation, retention, and independent read-back](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) -- **extends**: the article names interpretation, addressable retained theory, intervention, consequence, revision, and later use; this source note, already declared in `source_notes` but not linked in the body, gives the reader the complete co-indexed functional path and evidence ladder.
- [Factory-learning mechanisms should be compared on the same causal job](../../../../notes/factory-learning-mechanisms-should-be-compared-on-the-same-causal-job.md) -- **extends**: the article calls natural-language theory a first implementation bet and names trajectories, learned policies, direct search, and raw-record retention as rivals; this note supplies the shared experience-responsive-retention comparison, fact-matching controls, and limits on what a winning result would establish.
- [Disconnected witnesses do not establish a full causal path through theory](../../../../notes/disconnected-witnesses-do-not-establish-a-theory-mediated-path.md) -- **extends**: the article says attribution requires recording which retained state entered which production-time decision; this note specifies why separate witnesses do not compose and which joins the retained record must identify.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) -- **extends**: the article carefully limits one passing successor to one learning transition; this note gives readers the displaced later-episode measures and causal traces needed to test the stronger compounding claim.
- [Commonplace's declared frame](../../../../reference/commonplace-declared-frame.md) -- **evidenced-by**: the article's claim that current Commonplace evidence is human-inclusive depends on the operative record of which people, model-mediated actions, files, tools, and provider services are inside or outside the assessed boundary.
- [Trace-learning techniques in related systems](../../../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) -- **compares-with**: the article names trajectory reuse, learned policies, and raw-record retention as rival learning mechanisms; this survey compares concrete trace-to-artifact and trace-to-policy systems on retained form, extraction, promotion, read-back, and oracle dependence.
- [Exo](../../../../agentic-systems/reviews/exo.md) -- **compares-with**: Exo supplies a running non-weight self-improvement harness with broad rewrite reach, protected retention, and a weak semantic acceptance boundary, giving readers a concrete comparison with the article's theory-mediated and better-factory requirements.
- [The decisions that stay human, and what would move them](../../../../articles/the-decisions-that-stay-human-and-what-would-move-them.md) -- **extends**: the research program repeatedly identifies operator-supplied branch choice, blame assignment, evaluator construction, and acceptance as its current boundary; this companion article develops the conditions under which those residual decisions could move with warrant. Its existing return link does not remove the source reader's independent need for this continuation.

## Bidirectional Candidates

None

## Reverse-edge Candidates

None

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Citing retained theory at the decision point is a mediation trace](../../../../notes/citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md) -- passes the articulation test for the article's production-time-recording claim, but the retained full-path candidate includes this narrower first join and prevents two adjacent links from competing for the same reader need.
- [Self-improvement is relative to a declared objective](../../../../notes/self-improvement-is-relative-to-a-declared-objective.md) -- the declared-objective condition is material, but the article already links [A better-factory claim compares operative states](../../../../notes/a-better-factory-claim-compares-operative-states.md), which applies antecedence and objective indexing directly to its predecessor/successor comparison.
- [The boundary of automation is the boundary of verification](../../../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) -- the oracle problem is a strong thematic match, but the article's linked better-factory note already owns the exact oracle dilemma and the human-inclusive consequence; another general oracle link would add little traversal value.
- [Theory-mediated learning may improve sample efficiency under structured shifts](../../../../notes/theory-mediated-learning-may-improve-sample-efficiency-under-shifts.md) -- nearby conjecture, but the article does not currently claim sample-efficiency improvement; linking it would widen the program beyond the comparison it declares.
- [Broad software demands create pressure for agentic factory development](../../../../notes/broad-software-demands-create-pressure-for-agentic-factory-development.md) -- supplies motivation for acquiring family-specific production knowledge, but the article's present argument does not depend on widening demand classes, so the link would introduce a side thesis.
- [Greenfield and Short's software-factory ingest](../../../../sources/greenfield-short-software-factories-oopsla-2003.ingest.md), [Cook and Kent's Tool Factory ingest](../../../../sources/cook-kent-tool-factory-2003.ingest.md), and [Langlois and Exertier's MDSoFa ingest](../../../../sources/langlois-exertier-mdsofa-software-factory-factory-2004.ingest.md) -- primary evidence for the opening historical examples, but the article already links the note that represents and grounds their shared construction-without-acquisition claim. Direct links would duplicate grounding rather than give a distinct onward path.
- [Agent Optimizers](../../../../sources/agent-optimizers-compound-terminal-bench.ingest.md) and [Harness Updating Is Not Harness Benefit](../../../../sources/harness-updating-is-not-harness-benefit.ingest.md) -- relevant empirical protocols, but the article makes no claims about these studies. The compounding note is the better path because it states both their contribution and their causal limits.
- [Autogenesis](../../../../agentic-systems/reviews/autogenesis.md) -- a legitimate whole-system comparison with versioned symbolic mutation and weak selection validity, but Exo already supplies the broad-rewrite/weak-oracle comparison more directly; keeping both would turn one comparison need into a system list.
- [Publish an article](../../../../instructions/publish-an-article.md) -- an authorised procedure destination in general, but the research article offers no concrete publication action to an external reader.

## Index Membership

None. The source is already listed in [Articles](../../../../articles/README.md) and the site landing index.

## Synthesis Opportunities

None. The higher-order claims found during traversal already have homes in the full-path, mechanism-comparison, compounding, and human-decision artifacts above.

## Maintenance Observations

- The article collection authorises `kb/tasks/` as a procedure destination, but `kb/tasks/` has neither `COLLECTION.md` nor `README.md`. This makes the destination lack both a linking contract of its own and the curated head expected by repo-local discovery.
- [Theory-mediated learning joins self-modeling and theory refinement](../../../../notes/theory-mediated-learning-joins-self-modeling-and-theory-refinement.md) currently links to this article with a `context` footer relation, but `kb/notes/COLLECTION.md` neither authorises `kb/articles/` as a destination nor defines `context`. This is an existing contract gap, not a reverse-edge candidate the connect report can validate.

## Flags

- Split candidate: the article deliberately integrates at least four independent areas -- software-factory ontology, theory-bearing mechanism, experimental identification, and evaluator/human-allocation limits -- and has more than five genuine onward connections across them. If external-reader load becomes a problem, the experiment and causal-evidence protocol is the cleanest separable article; this report does not recommend changing the current source.
