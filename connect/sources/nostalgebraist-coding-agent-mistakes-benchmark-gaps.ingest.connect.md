---
description: "Connection candidates for the Nostalgebraist ingest on operator correction, cross-session carryover, and what coding-agent benchmarks measure."
type: types/connect-report.md
source: kb/sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md
source_has_frontmatter: true
date: "2026-11-19"
depth: standard
---

# Connection Report: Nostalgebraist on persistent coding-agent mistakes and benchmark gaps

**Source:** [Nostalgebraist on persistent coding-agent mistakes and benchmark gaps](../../../../sources/nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md)

Repo-local discovery by `gpt-6.2-sol` using `cp-skill-connect/SKILL.md`. The ingest separates firsthand reports of correction and redirection, recurrence of corrections in later sessions, and a conjecture about selection pressure from benchmarks. It does not establish an error-rate trend or trace a particular correction into later behavior.

## Discovery Trace

**Curated heads and scope.** Read the root `README.md` in theory, reference, agent-memory-systems, agentic-systems, tags, and sources. The tags landing led to the Goal prioritization head, which already lists this ingest and also surfaces the unattended-work note and Goedecke. The source has `domains:` but no `tags:`, so no by-tag query ran. The theory landing surfaced the retained-adaptation note; the agentic-systems landing surfaced Compound Engineering. Work and instructions are excluded by the source contract. No external prospecting: the known LessWrong URL already serves as the source's provenance and needs no duplicate edge.

**Titles and descriptions.** For each destination `d`, generated fresh titles with `rg -N --no-filename -m1 '^# (.*)' -r '$1' "kb/$d/" -g '*.md' -g '!*.brief.md'`. Screened the streams case-insensitively for `benchmark|priorit|unattended|ablation|human judgment|reflexion|compound engineering|pilot|crux|retained system-definition|requirements don.t|weakly discriminated`; counts in the order above were 439, 256, 175, 156, 35, and 609. Resolved the fixed-client benchmark title with `rg -l '^# A benchmark that holds the client fixed exports the least-warrantable decisions by design$' kb/theory/`. For each destination ran `rg '^description:' "kb/$d/" -g '*.md' | rg -i 'human (effort|judgment|attention|supervis)|benchmark.*(judgment|fixed client|gap|audit)|priorit[iz].*(effort|goal|requirement)|unattended|live (steering|self-improvement)|underselect|tolerances|cross-session.*(feedback|correction)'`. Any brief match would count toward its main artifact. There were no search scores.

**Body search.** For all six destinations ran `rg -il "$q" "kb/$d/" -g '*.md' -g '!nostalgebraist-coding-agent-mistakes-benchmark-gaps.ingest.md'` with both queries:

- `low.value (work|tangent)|stopping decisions|operator intervention|human steering|unrequested requirements`
- `benchmark optimiz|fixed client|weak selection|repeated correction|live self-improvement|same benchmark instance`

**Evaluation by destination:**

- **Theory:** kept the two existing connections as scope checks, not as requests to add duplicate links. The fixed-client note distinguishes leaving a decision outside measurement from measuring it and selecting weakly for it. The fixed-decomposition note and theory-builder definition already serve the ingest's learning analysis; neither supports a stronger classification or diagnosis.
- **Reference:** the description and title scans found the ablation proposal. Its matched comparisons explicitly meter human decisions and minutes. The cost-per-yield proposal surfaced in descriptions but concerns comparing routine search controllers, not the broader labor of supervising and correcting a KB workflow. Neither body query added a reference candidate.
- **Agent-memory-systems:** Reflexion surfaced by title and body. Also screened hits from `rg -il 'same benchmark instance|cross.task.*(lesson|failure)|benchmark optimiz' kb/agent-memory-systems -g '*.md'`. The corpus is historical; Reflexion retries a particular instance, and auto-harness documents benchmark-driven improvement without a corresponding measure of operator work. Neither offers a better comparison than PILOT on the ingest's specific carryover question.
- **Agentic-systems:** `rg -il 'operator.*(redirect|stop)|human.*(steer|abort)|success.gated.*(skill|memory)|project.knowledge retention' kb/agentic-systems -g '*.md'` returned Compound Engineering and archive/table hits. Compound Engineering shows a path for retaining and retrieving project knowledge, not whether comparable corrections reduce later operator interventions. No new edge retained.
- **Tags:** the Goal prioritization head already provides the useful inbound navigation. Neither body query surfaced another head with a comparably specific reader need. The sources contract permits looking through tags but declares no outbound label to them.
- **Sources:** kept Goedecke for the explicit-tolerance intervention and PILOT for its separate live and later update paths. The benchmark-auditing ingest surfaced by title and description; it examines grader and task defects, not the selection history or operator decisions at issue here.

**Link following and reverse direction.** Followed the unattended-work note to the effort-relocation note: recurring interventions can identify a decision still supplied by the operator, but the ingest has no matched effort or task comparison that would show effort relocating. Followed the unequal-selection note to Goedecke, which reinforces the specific comparison on corrections that a final check may miss. Followed PILOT to retained adaptation and intended-path health: the former separates exposure from operative use; the latter treats a different concealment case (tool fallback), so no separate link is proposed. Checked theory's outbound rules for the reverse evidence edge. `rg -l -F 'nostalgebraist-coding-agent-mistakes-benchmark-gaps' kb/{theory,reference,agent-memory-systems,agentic-systems,tags,sources} -g '*.md'` found only the Goal prioritization head. The unattended-work note can use the ingest to bound its claim with an example of what was supplied; the fixed-client note cannot use the ingest to establish what any actual benchmark held fixed.

### Candidate origins

- kb/theory/unattended-work-needs-the-functions-that-interaction-supplied.md — known, curated-head, titles, descriptions, link-following
- kb/theory/weakly-discriminated-qualities-tend-to-be-underselected.md — known, titles, descriptions
- kb/theory/holding-the-client-fixed-exports-the-least-warrantable-decisions.md — titles
- kb/reference/proposals/ablation-baselines-for-the-declared-objective.md — titles, descriptions
- kb/sources/sean-goedecke-what-requirements-dont-you-have.ingest.md — curated-head, titles, descriptions, body-search, link-following
- kb/sources/pilot-live-self-improvement-long-horizon-agents.ingest.md — titles, body-search

## Connections Found

- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) — **is-evidence-for**: the operator reports correcting mistakes and stopping low-value directions. This illustrates two contributions that an acceptable final result can hide; it does not establish that each intervention was necessary. Already linked; keep the scoped treatment rather than duplicate it.
- [Weakly discriminated qualities tend to be underselected](../../../../theory/weakly-discriminated-qualities-tend-to-be-underselected.md) — **compares-with**: the note specifies when a quality can improve more slowly because acceptance favors other qualities more strongly. The ingest conjectures this for prioritization but does not identify the actual acceptance rule or show better candidates losing. Already linked; do not promote the conjecture to evidence of unequal selection.
- [A benchmark that holds the client fixed exports the least-warrantable decisions by design](../../../../theory/holding-the-client-fixed-exports-the-least-warrantable-decisions.md) — **compares-with**: both concern what a benchmark leaves unmeasured. The note gives a distinct testable possibility: a benchmark can supply or omit an internal production decision rather than measure how well the agent makes it. Check which decisions the benchmark supplies before treating score gains as evidence about prioritization. The ingest does not identify a benchmark with this design.
- [Ablation baselines for the declared objective](../../../../reference/proposals/ablation-baselines-for-the-declared-objective.md) — **see-also**: the proposed Commonplace comparison meters human decisions and minutes alongside outcome quality. It gives a reader a way to measure the supervision the ingest describes but does not quantify. It is a proposal, not a completed measurement.
- [What requirements don't you have?](../../../../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md) — **compares-with**: compare when the operator sets limits on effort. Nostalgebraist reports stopping tangents in flight; Goedecke proposes stating tolerances up front and reviewing for unnecessary coordination. Stating tolerances is a candidate intervention when the missing boundary is known, not a remedy established for the reported tangents.
- [PILOT in the Loop](../../../../sources/pilot-live-self-improvement-long-horizon-agents.ingest.md) — **compares-with**: compare steering the current run with making a correction available to later runs. PILOT has separate routes for live steering and retained skill updates. Its bundled results on repeated benchmark sweeps do not isolate whether any retained correction changes a later prioritization decision.

## Bidirectional Candidates

None. The useful return is a separate evidence use, listed below.

## Reverse-edge Candidates

- [Unattended work needs the functions that interaction supplied](../../../../theory/unattended-work-needs-the-functions-that-interaction-supplied.md) → source — **evidenced-by**: a body-level practitioner case would bound what the operator is reported to supply (correction and stopping), without claiming a test of necessity, prevalence, or an unattended replacement. The ingest has no retained quotes; a future author needs adequate retained support or an explicit `(snapshot required)` citation. No grounding was performed here.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Learning inside a fixed decomposition inherits its mistakes](../../../../theory/learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — keep the existing analytical reference, but do not propose a stronger evidence link. The reported errors do not show that the necessary distinction, action, or mapping was unavailable to the learner.
- [Increasing computational autonomy relocates human effort to the frontier instead of reducing it](../../../../theory/increasing-computational-autonomy-relocates-human-effort.md) — the report of recurring interventions identifies a candidate dependency but does not trace a change in workload or show where freed attention went. The unattended-work note already supplies the route to measuring that distinction.
- [Reflexion](../../../../agent-memory-systems/reviews/reflexion.md) — lessons fed into retries of a single benchmark instance do not address reuse on later comparable tasks. PILOT provides a closer comparison on timing without implying a fix.
- [Compound Engineering plugin](../../../../agentic-systems/reviews/compound-engineering-plugin.md) — a documented project-knowledge route, but not a comparison that separates live correction from later uptake.
- [Automated Benchmark Auditing for AI Agents and Large Language Models](../../../../sources/automated-benchmark-auditing-ai-agents-llms.ingest.md) — auditing mismatches among prompts, environments, and graders does not itself test whether benchmarks measure the task choices the operator reports supplying. No particular benchmark is identified in the ingest for such an audit.

## Index Membership

None to add. The [Goal prioritization head](../../../../tags/goal-prioritization-README.md) already lists the ingest. Sources are outside generated tag membership.

## Synthesis Opportunities

None. These connections suggest separate tests of supervision, later reuse, and evaluation coverage, not a demonstrated mechanism that unifies them.

## Maintenance Observations

None.

## Flags

- Split signal for any future theory extraction: the candidate set spans operator functions, cross-session reuse, and benchmark coverage. Preserve the ingest as one source record, but do not use evidence about one of those questions to settle the others.
- Treat recurring correction as a reason to test carryover, not as evidence that the workflow cannot learn. Treat benchmark optimization as a conjecture about incentives, not as an explanation established by the practitioner episodes.
