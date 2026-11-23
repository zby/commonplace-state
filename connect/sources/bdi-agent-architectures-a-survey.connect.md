---
description: "Discovery report for possible KB connections from one source artifact"
type: types/connect-report.md
source: "kb/sources/.snapshots/bdi-agent-architectures-a-survey.md"
source_has_frontmatter: true
date: "2026-11-21"
depth: standard
---

# Connection Report: BDI Agent Architectures: A Survey

**Source:** BDI Agent Architectures: A Survey (`kb/sources/.snapshots/bdi-agent-architectures-a-survey.md`; unlinked because snapshots are Git-ignored and no paired ingest exists yet)

The source is an immutable snapshot. No tracked `bdi-agent-architectures-a-survey.ingest.md` exists yet. Every outbound candidate below is for that future ingest, which is the source's authored connection surface under `kb/sources/COLLECTION.md`. Reverse edges name the future ingest as their target and therefore carry no link yet.

Source content used for judging: de Silva, Meneguzzi and Logan (IJCAI-20) survey how the BDI architecture's components are realised in agent programming languages. The survey covers beliefs (literals, KR plug-ins, uncertainty, revision) and goals (test, procedural and declarative achievement, maintenance, temporally extended, priorities and deadlines). It covers plan-rules (trigger plus context condition plus body; interleaving, concurrency, control flow) and the deliberation cycle (failure handling, intention scheduling, meta-level plan selection). It grounds "deliberation" in Bratman: deciding which state of affairs to bring about. Means-ends reasoning then adopts a pre-specified plan. Its open questions include learning plan-rules and context conditions, and goal reasoning about whether to adopt a goal.

## Discovery Trace

**Collection contract read:** `kb/sources/COLLECTION.md`, "Outbound links". Authorised destinations: theory, reference, agent-memory-systems, agentic-systems, tags and other sources. `kb/work/` and `kb/instructions/` are excluded. External prospecting is skipped because no external target was supplied. Labels: `is-evidence-for` (theory, agent-memory-systems), `abstracted-from` (theory), `rests-on` (theory), `compares-with` (theory, sources, agent-memory-systems, agentic-systems), `defined-in` (theory/definitions), `see-also` (theory, reference, sources, agent-memory-systems, agentic-systems, external) and `derived-from` (external only). The snapshot has no `tags:`, so no tag-head pass is triggered by source tags.

**Body search (whole KB, excluding work, snapshots, reports):**
- `rg -l -i -e "BDI"` then `rg -n -w 'BDI'` -- the only real hit is `kb/sources/wooldridge-jennings-intelligent-agents.ingest.md` (Extractable Value 7 and Limitations treat PRS/BDI). The case-insensitive hits were substrings and were discarded.
- `rg -l -i "Bratman"` -- `kb/sources/sep-practical-reason.ingest.md` only. Kept.
- `rg -l -i "deliberation"` -- 25 hits. Relevant: `sep-practical-reason`, `wooldridge-jennings-intelligent-agents`, `russell-wefald-principles-of-metareasoning`, `fishkin-mansbridge-deliberative-democracy-intro`. Rest are incidental uses.
- `rg -l -i "means-ends"`, `"belief-desire"`, `"maintenance goal"`, `"goal reasoning"`, `"plan-rule|plan rule"`, `"practical reasoning"` -- no hits outside `sep-practical-reason`. The KB has no vocabulary for plan-rule structure.
- `rg -l -i "plan librar"` -- `kb/agent-memory-systems/reviews/SkillX.md`, `wooldridge-jennings`. SkillX evaluated (see Rejected).
- `rg -l -i "HTN"` -- `legal-drafting-solves-the-same-problem-as-context-engineering.md` (incidental), sutskever list, one analysis. None kept.
- `rg -l -i "AgentSpeak|Jason\b"` -- only the sutskever reference list. None kept.
- `rg -n -i 'plan librar|goal stack|intention stack|subgoal hierarch|hierarchical task|HTN|precondition'` over `kb/agent-memory-systems` and `kb/agentic-systems` -- `voyager.md:116,126` (stored skills lack precondition metadata) kept; SkillX plan library evaluated; AAS archive hits are precondition checks in unrelated runtimes and were rejected.
- `rg -l -i 'deliberativ'` over theory, reference, agentic-systems, agent-memory-systems, tags -- no hits. The "deliberative" term lives only in `kb/work/learning-method-name/` (excluded destination) and the sources.

**Full titles listing (theory):**
- `rg -N --no-filename -m1 '^# (.*)' -r '$1' kb/theory/ --glob '*.md' --glob '!*.brief.md'` (444 titles), filtered with `rg -i 'agent|plan|goal|deliberat|skill|procedur|fail|commit|intent|belief|recover|backtrack|search|retry|library|meta|decompos|subtask|routine|learn|symbolic|precompil|codif'`. Candidates resolved with `rg -l -F -x '# <title>' kb/theory/` and descriptions read:
  - A goal-holding interpreter fails soft -- kept (procedural vs goal-holding execution; BDI is a symbolic counter-case).
  - Backtracking keeps lightweight search control provisional -- kept (BDI goal-level backtracking).
  - A failure explanation becomes search control only when it changes a later branch decision -- kept (context-condition re-checking after plan failure).
  - Skills are instructions plus routing and execution policy -- kept (plan-rule trigger plus context condition as routing).
  - A capable agent needs methodology selection -- kept (meta-level choice among applicable plan-rules).
  - Agent-runtime analysis should separate scheduling, context assembly, and external state -- kept, weaker (interpreter cycle decomposition).
  - Theory building and capacity building make the same kind of fallible commitment -- rejected (direction-of-fit link already supplied via `sep-practical-reason`; the survey adds no belief/intention commitment analysis).
  - Commitment, not derivation, creates new ground truth -- rejected (homonym: KB commitment vs BDI intention-as-commitment).
  - "Agent" is a useful technical convention, not a definition -- rejected (Wooldridge-Jennings already supplies the classical counterpart edge).
  - Stateful tools recover control by becoming hidden schedulers; Semantic sub-goals that exceed one context window become scheduling problems; Intent controls a local choice only when it distinguishes its live alternatives; LLM-executed methodologies are metacircular interpreters -- rejected (shared vocabulary only, see Rejected).
- Read openings of the six kept theory notes to confirm the claim matches.

**Description listing (sources):**
- `rg -N '^description:' kb/sources/*.ingest.md | rg -i 'agent architect|planning|plan |plans|goal|intention|deliberat|symbolic|reactive|cognitive architect|soar|subsumption|procedural|hierarchical|metareason|rational'` -- flagged `wooldridge-jennings-intelligent-agents`, `sep-practical-reason`, `russell-wefald-principles-of-metareasoning`, `plans-and-situated-actions-suchman-1985` (plus Dittrich, Duguid and PD-of-HCI rereadings), `chunking-in-soar-general-learning-mechanism`, `skill-acquisition-compilation-weak-method-solutions`, `fishkin-mansbridge-deliberative-democracy-intro`, `cmmn-1-1-specification`, `gavel-graph-world-models`, `introspective-multistrategy-learning`, `procedural-graphs-self-evolving-execution`.

**Topic indexes / curated heads:**
- `ls kb/tags/` then read `method-guided-action-README.md` (`complete: true`), `goal-prioritization-README.md`, `computational-model-README.md` and `failure-modes-README.md` (`complete: true`). These were read for index-membership fit. By-tag `rg` was skipped because the snapshot carries no tags.
- `kb/agentic-systems/` listing scanned. It holds no BDI or agent-programming-language reviews.

**Link following:**
- `wooldridge-jennings-intelligent-agents.ingest.md` "Connections Found" -> `russell-wefald`, `provably-bounded-optimal-agents`, `agent-is-a-tool-loop`, `constraining-and-extraction-...`. This confirmed the deliberative-agent cluster.
- `sep-practical-reason.ingest.md` "Connections Found" -> wooldridge, russell-wefald, on-balance note, `theory-and-capacity-building-...`, `intent-controls-choices-...`. This revealed the sibling "senses of deliberation" cluster that the BDI survey would join with a third, computational sense.
- `russell-wefald-principles-of-metareasoning.ingest.md` -> `failure-explanation-changes-later-branch-decisions`, `lightweight-search-control-does-not-license-adoption`. This reinforced the search-control candidates.
- `theory/COLLECTION.md` outbound labels toward `sources` were checked so reverse edges use authorised labels (`evidenced-by`, `see-also`).

### Candidate origins

- kb/sources/wooldridge-jennings-intelligent-agents.ingest.md — body-search, descriptions, link-following
- kb/sources/sep-practical-reason.ingest.md — body-search, descriptions, link-following
- kb/sources/plans-and-situated-actions-suchman-1985.ingest.md — descriptions
- kb/sources/chunking-in-soar-general-learning-mechanism.ingest.md — descriptions
- kb/sources/russell-wefald-principles-of-metareasoning.ingest.md — body-search, descriptions, link-following
- kb/theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md — titles
- kb/theory/backtracking-keeps-lightweight-search-control-provisional.md — titles
- kb/theory/failure-explanation-changes-later-branch-decisions.md — titles, link-following
- kb/theory/skills-are-instructions-plus-routing-and-execution-policy.md — body-search, titles
- kb/theory/capable-agents-need-methodology-selection.md — titles, curated-head
- kb/theory/agent-runtime-analysis-should-separate-scheduling-context-state.md — titles
- kb/agent-memory-systems/reviews/voyager.md — body-search

## Connections Found

All edges are proposals for the future `kb/sources/bdi-agent-architectures-a-survey.ingest.md`.

- [Intelligent Agents (Wooldridge and Jennings)](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) -- **compares-with**: the two surveys give the classical and the 2020 account of BDI. Wooldridge and Jennings define "deliberative agent" architecturally (symbolic world model plus logical reasoning) and file PRS as hybrid. The BDI survey instead treats "deliberation" as Bratman's goal-selection step, separate from means-ends plan adoption. The shared axis is what "deliberative" names in agent architecture. A reader resolving that sense needs both.
- [SEP: Practical Reason](../../../../sources/sep-practical-reason.ingest.md) -- **compares-with**: the SEP entry gives the normative philosophical sense of deliberation and cites Bratman's plans as defeasible constraints. The BDI survey shows how Bratman's two steps (deliberation, then means-ends reasoning) were turned into an interpreter cycle with plan libraries. The axis is philosophical versus computational practical reasoning. The SEP ingest notes the entry says little about procedure or cost, and this source fills exactly that gap.
- [Plans and Situated Actions (Suchman 1985)](../../../../sources/plans-and-situated-actions-suchman-1985.ingest.md) -- **compares-with**: the axis is whether plans control action. BDI plan-rules are pre-specified recipes executed by an interpreter, the plans-as-controllers view Suchman criticised. BDI partly answers with context conditions checked at run time, goal-level failure recovery and re-checking applicability after failure. The comparison shows how far a symbolic architecture goes toward situated use of plans.
- [Chunking in Soar](../../../../sources/chunking-in-soar-general-learning-mechanism.ingest.md) -- **compares-with**: the axis is how a fixed symbolic architecture acquires its rules. Soar compiles subgoal experience into productions automatically. The BDI survey reports that plan-rules are hand-written, that learning has been confined to context conditions (Singh and Hindriks) and that learning new rules is open future work. The contrast locates BDI's learning gap precisely.
- [Principles of Metareasoning (Russell and Wefald)](../../../../sources/russell-wefald-principles-of-metareasoning.ingest.md) -- **compares-with**: the axis is meta-level control. BDI meta-level reasoning picks among applicable plan-rules, by priority rules or past success rate, and rewrites failed plans. It has no account of what that computation is worth. Russell and Wefald price computation by whether it changes the next action. Comparing them shows BDI meta-level control is choice of method without a value-of-computation criterion.
- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) -- **compares-with**: the note says a procedure "compiles its goal away", so a blocked step fails hard, while an interpreter holding the end re-routes. BDI is a symbolic middle case. Plans are procedures, but the interpreter retains the triggering goal, retries alternative applicable plan-rules and backtracks to parent goals. Declarative goals are also dropped when believed achieved. The axis is where the goal is held and whether re-routing needs an LLM-style interpreter. This bounds the note's procedure/interpreter dichotomy.
- [Backtracking keeps lightweight search control provisional](../../../../theory/backtracking-keeps-lightweight-search-control-provisional.md) -- **compares-with**: BDI automated failure recovery (CAN, JACK, RAE, HTN-acting) is a worked backtracking design. A failed plan triggers another applicable rule for the same goal, then escalates to the parent goal. The axis is the return path that keeps a chosen branch provisional. The survey also records the costs the note's scope names: true concurrency and external actions are not restored.
- [A failure explanation becomes search control only when it changes a later branch decision](../../../../theory/failure-explanation-changes-later-branch-decisions.md) -- **compares-with**: the survey's three re-check policies are designs for whether failure information changes later branch choice. They are early instantiation, re-check after failure and check before the first step. Ghallab's "more complete" rule re-admits a failed plan-rule only when the conditions responsible for failure no longer hold, which is retained failure explanation acting as branch control. The axis is failure-conditioned re-selection.
- [Skills are instructions plus routing and execution policy](../../../../theory/skills-are-instructions-plus-routing-and-execution-policy.md) -- **compares-with**: a BDI plan-rule is a procedure plus a trigger (relevance) and a context condition (applicability), the classical form of the routing the note says skills add over instructions. The axis is how a procedure declares when it applies. The comparison exposes a gap: skill descriptions carry relevance cues but no checked applicability condition.
- [A capable agent needs methodology selection, not just relevant knowledge](../../../../theory/capable-agents-need-methodology-selection.md) -- **compares-with**: BDI has the selection problem the note describes, several applicable plan-rules for one goal. By default it resolves the problem arbitrarily or by program order, and meta-level plan-rules exist to override that default. The axis is selection among simultaneously applicable methods. The comparison shows that symbolic agent languages treated this as an explicit interpreter extension point.
- [Agent-runtime analysis should separate scheduling, context assembly, and external state](../../../../theory/agent-runtime-analysis-should-separate-scheduling-context-state.md) -- **compares-with** (weaker): the BDI interpreter (Algorithm 1) separates event queue, belief base, plan selection and intention scheduling. That is a symbolic precedent for decomposing a runtime into control progression and state. The axis is runtime decomposition. Keep only if the ingest discusses intention scheduling.
- [Voyager](../../../../agent-memory-systems/reviews/voyager.md) -- **compares-with**: Voyager retrieves learned skills by embedding similarity over generated descriptions, and the review flags missing precondition metadata. BDI plan-rules carry an explicit context condition checked against beliefs before adoption, and again after failure. The axis is how a retained procedure declares applicability. The target collection is frozen-historical, so link only if the ingest's analysis needs a concrete skill-library contrast.

## Bidirectional Candidates

- [Intelligent Agents (Wooldridge and Jennings)](../../../../sources/wooldridge-jennings-intelligent-agents.ingest.md) <-> source -- **compares-with**: the Wooldridge ingest's Limitations say PRS "is a BDI system with a symbolic plan library" that the deliberative/reactive split misfiles. A return link would let a reader check that limitation against a dedicated BDI survey.
- [SEP: Practical Reason](../../../../sources/sep-practical-reason.ingest.md) <-> source -- **compares-with**: the SEP ingest says the entry "says little about how deliberation is carried out as a procedure". The BDI ingest is the KB's procedural counterpart for Bratman's model.

## Reverse-edge Candidates

The target of each edge is the future `kb/sources/bdi-agent-architectures-a-survey.ingest.md`. Author it only after that ingest exists.

- [A goal-holding interpreter fails soft, and its workarounds tax a bounded budget](../../../../theory/a-goal-holding-interpreter-fails-soft-workarounds-tax-a-bounded-budget.md) → future BDI ingest -- **evidenced-by** (theory contract), phrased as *bounds*: BDI interpreters hold goals over hand-written procedures and re-route by plan-rule alternatives, so fail-soft re-routing does not require natural-language interpretation. The source was not a test of the note.
- [Backtracking keeps lightweight search control provisional](../../../../theory/backtracking-keeps-lightweight-search-control-provisional.md) → future BDI ingest -- **evidenced-by**, phrased as an instance that qualifies scope: goal-level backtracking in agent programming languages, including the non-restorable concurrency case.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Deliberative democracy introduction (Fishkin and Mansbridge)](../../../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md) -- the group sense of deliberation. The BDI survey is strictly single-agent. Linking adds a third sense without a shared axis beyond the word.
- [Theory building and capacity building make the same kind of fallible commitment](../../../../theory/theory-and-capacity-building-make-the-same-kind-of-commitment.md) -- the belief/intention direction-of-fit point is already routed through `sep-practical-reason`. The survey adds no analysis of commitment retraction.
- [Commitment, not derivation, creates new ground truth](../../../../theory/commitment-not-derivation-creates-new-ground-truth.md) -- "commitment" is a homonym here; BDI intentions as commitments are not KB ground-truth commitments.
- ["Agent" is a useful technical convention, not a definition](../../../../theory/agent-is-a-tool-loop.md) -- Wooldridge-Jennings already supplies this classical counterpart. A second survey adds nothing to the definitional comparison.
- [SkillX](../../../../agent-memory-systems/reviews/SkillX.md) -- the plan library is keyed by task and retrieved by similarity, which duplicates the Voyager contrast with less explicit precondition discussion.
- [Stateful tools recover control by becoming hidden schedulers](../../../../theory/stateful-tools-recover-control-by-becoming-hidden-schedulers.md), [Semantic sub-goals that exceed one context window become scheduling problems](../../../../theory/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md), [Intent controls a local choice only when it distinguishes its live alternatives](../../../../theory/intent-controls-choices-by-distinguishing-live-alternatives.md), [LLM-executed methodologies are metacircular interpreters, not compilers](../../../../theory/llm-executed-methodologies-are-metacircular-interpreters.md) -- they share vocabulary (scheduler, subgoal, intent, interpreter) but have different mechanisms: framework escape hatches, context-window partitioning, intent statements and self-hosting rules. A reader following the link would not gain anything specific.
- [Skill acquisition: compilation of weak-method solutions (Anderson)](../../../../sources/skill-acquisition-compilation-weak-method-solutions.ingest.md), [Introspective multistrategy learning](../../../../sources/introspective-multistrategy-learning.ingest.md), [CMMN 1.1](../../../../sources/cmmn-1-1-specification.ingest.md), [GAVEL](../../../../sources/gavel-graph-world-models.ingest.md) -- adjacent (production compilation, failure-driven learning goals, plan-item lifecycles, plan repair), but Soar covers the learning contrast better. The survey treats the others only in passing.
- Suchman rereadings (Dittrich, Duguid, PD-of-HCI summary) -- link the primary Suchman ingest only.
- `kb/reference/` -- no shipped-system artifact concerns BDI, plan-rules or deliberation cycles. No `see-also` candidate.

## Index Membership

Tags a future ingest may carry (`kb/sources/COLLECTION.md` "Topic search tags"). Each requires that the ingest's *analysis* treat the topic substantively:

- [goal-prioritization](../../../../tags/goal-prioritization-README.md) -- fits if the ingest analyses §4.5 (priorities, deadlines, priority-maximal goal sets), §6.2 intention scheduling and goal dropping as precedence decisions.
- [method-guided-action](../../../../tags/method-guided-action-README.md) -- fits if the ingest analyses plan-rule relevance/applicability and meta-level selection among applicable rules as method selection.
- [computational-model](../../../../tags/computational-model-README.md) -- fits if the ingest treats the interpreter cycle and intention scheduling as an execution and scheduling architecture.

## Synthesis Opportunities

The KB now holds three sources for three senses of "deliberation": Wooldridge-Jennings (architectural: symbolic model plus logical reasoning), SEP practical reason (normative weighing of reasons) and this survey (Bratman's computational split of goal selection from means-ends plan adoption). Fishkin-Mansbridge adds a group sense. A higher-order claim may follow: "deliberative" in agent literature names the goal-selection step, not the weighing standard or learning. That would bear on the deliberative-learning naming work. The synthesis belongs to that workshop and is not to be authored from connect.

## Maintenance Observations

- The KB has no vocabulary for plan-rule structure (trigger, context condition, applicability re-check). `rg` for "plan-rule", "means-ends", "maintenance goal" and "goal reasoning" returned nothing outside the SEP ingest. Several theory notes on skills, procedures and failure recovery describe these mechanisms without the classical names, so the gap may recur.

## Flags

- The ingest does not exist yet. Re-run connect on `kb/sources/bdi-agent-architectures-a-survey.ingest.md` once written if its analysis narrows to a specific occasion (for example the learning-method-name workshop). The relevant subset may then shrink to the deliberation-sense sources.
- Not a split candidate: the source is a survey with one organising assertion.
