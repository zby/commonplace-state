---
type: types/review-result.md
findings:
- scope: passage
  quotes:
  - Human evaluation remains a dependency when omitting it either prevents that process
    from proceeding in practice or leaves an evaluation task specified by those requirements
    undone.
  reason: 'The definition joins two different relations under one term. The first
    prong is causal blocking: without the person, the process stops. The second is
    a stipulated obligation: the process runs, but a written task goes undone. The
    note never separates them. The central claim depends almost entirely on the second
    prong, where it is true by stipulation. Name the two relations separately, for
    example a blocking dependency and an obligation dependency, and say which one
    each later sentence uses.'
- scope: passage
  quotes:
  - Adoption continues if the maintainer does nothing, but the required monitoring
    task goes undone. The process including that task is not fully automated
  reason: This sentence is the note's only worked case of a non-blocking dependency,
    and it settles the question by definition. The process counts as not fully automated
    only because it was defined to include the maintainer's task. A builder can't
    use this case to tell whether the review is needed for the system to keep working
    well; only the written requirement decides. Either add a case where omitting the
    monitoring has an operational consequence (harmful changes accumulate with no
    rollback) or limit the claim to compliance with stated requirements.
- scope: passage
  quotes:
  - Identifying these dependencies does not establish that each specified task is
    useful or adequate.
  reason: 'This concession is the note''s answer to the stipulation objection, but
    it sits deep in the body and the opening paragraph and description do not reflect
    it. Move it into the opening so the reader knows from the start that the note
    sorts tasks by role, not by need. Then say what that sorting changes for someone
    building a KB: for example, a claim that a revision loop is ''fully automated''
    must name which required tasks it includes.'
- scope: document
  quotes: []
  reason: The file is named for a causal claim, 'evaluation that controls adoption
    helps determine the change'. The title and body disavow that claim ('rather than
    deciding who deserves causal credit for an improvement'). Readers and links that
    rely on the filename will expect a different claim from the one the note makes.
    Rename the file to match the title, with a separate relocation commit.
outcome: report
attack-outcome: partially lands
description: Retained report review of kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
  against kb/instructions/critique-note.md
contract: report
note: kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
criterion: kb/instructions/critique-note.md
note-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
criterion-sha256: 9552184ef532f9321fa4aec6015d5d8509eea15091f70300cc2c9e7a0fcaf771
target-sha256: c3b814e077eaa68b1c25e9a772e98ac41b6b9bb452044d02fd88b442ed7f747f
target-capture: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/281bd31ddc10b24f4e6e92ca/inputs/target/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
observation: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/artifact/reviews/281bd31ddc10b24f4e6e92ca/observation.json
contract-sha256: ee169e3ac7d6d67feaa7d5a948051910000eafc22cefea9ccc806a63ca142161
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews
launch: a1b594240d1e445a8035fd60b37f4336
completed-at: '2026-11-17T07:56:08Z'
raw-output: kb/reports/state/review/runs/v2/revise/kb/theory/evaluation-that-controls-adoption-helps-determine-the-change/c3b814e077ea/reviews/calls/launches/a1b594240d1e445a8035fd60b37f4336/outputs/review.md
raw-output-sha256: f664b665f188a80192cf05188ba0373662bbd6e763f23c7549baf503ee683159
format: 2
---

# Critique: Removing approval waits can leave required human evaluation in place

**Note:** kb/theory/evaluation-that-controls-adoption-helps-determine-the-change.md
**Central commitment:** Automating adoption by removing an approval wait does not by itself automate the wider process, because human evaluation can remain a dependency for monitoring or later revision. A dependency here means that omitting the evaluation either blocks the process or leaves a task undone that the process's stated requirements specify.
**Critique mode:** claim
**Attack outcome:** partially lands

## Strongest case against it

An operations or reliability engineer would say the distinction is partly idle because the "stated requirements" prong makes the result true by definition. For them, a process depends on a human step when the process fails, stops or degrades without it. Under that standard, the weekly sample review in the note's example is not a dependency. Adoption continues, and the note itself says "Adoption continues if the maintainer does nothing". The review is an obligation written in a runbook. Whether skipping it matters depends on facts the note excludes, such as whether harmful changes actually accumulate.

The note defines dependency as either blocking or "leaves an evaluation task specified by those requirements undone". Because of that disjunction, any human task anyone writes down becomes an operating dependency. The headline "removing approval waits can leave required human evaluation in place" then reduces to "if the requirements specify a human task, the requirements specify a human task". The modal "can" guarantees the claim is never false. The engineer's conclusion: the note offers a vocabulary for sorting tasks by the role a document assigns them. It does not support a claim about what automation requires, and the word "operating" in "operating dependency" borrows causal weight that the obligation prong lacks.

The objection matters for this KB's quality bar. A note earns its place when it changes how someone builds or operates a KB. If the distinction tells a builder only to read their own requirements, it changes little.

## How the note engages it

The note partially engages the objection.

- It makes the definition relative explicitly: "The distinction is relative to the process being automated and its stated requirements." This openly accepts the requirements-relative framing rather than hiding it.
- It concedes the key gap: "Identifying these dependencies does not establish that each specified task is useful or adequate." It also says that removing an unnecessary requirement "changes the process being automated", while skipping the task does not fulfill it. Together these grant that the note does not judge need.
- The "Required approval" case and the link to [routine approvals do not establish that human judgment is dispensable](./routine-approvals-do-not-show-that-human-judgment-is-dispensable.md) add real content on the blocking prong. A wait that always ends in approval is still a dependency, and repeated approval does not show it can be removed. That part does not reduce to stipulation.
- The Scope bullet on habitual waits correctly places an unwritten wait under the blocking prong, not the requirements prong.

What the note does not do is separate the two prongs. As a result, its concession about usefulness does not reach the headline or the description. Both present "required human evaluation" as if it named one kind of dependency. The "Name the process being automated" section, which carries the claim beyond adoption, uses only the obligation prong. So the objection lands on that section and on the framing, but not on the blocking-wait analysis.

## Constructive findings

- Split the definition into two named relations: one where the process cannot proceed without the person, and one where a specified task goes undone. Say which relation the title asserts. If it asserts both, say that the second is true by specification and why that is still worth tracking. For example, an automation claim that silently drops a specified task misstates what was automated.
- Give the monitoring example an operational consequence, or state that it shows only the obligation case. A version with consequences would say that without the weekly sample review, harmful adopted changes have no rollback path, so the change history drifts. That would make the non-blocking case do causal work instead of definitional work.
- Bring the concession ("does not establish that each specified task is useful or adequate") into the opening paragraph. Add one sentence on what a builder does differently because of the distinction, such as declaring which required tasks a "fully automated" claim covers.
- Rename the file to match the title; the current filename names a causal-credit claim the note explicitly sets aside.

## Secondary objections (optional)

- "A non-binding recommendation still creates a dependency if the agent must wait for it" is correct under the blocking prong. Next to "Conversely, a program can apply human-authored acceptance rules without requiring a new human judgment for each change", though, it leaves open a case: a human who reviews only exceptions the program routes to them. The linked routine-approvals note covers this ("routing exceptions to a person reduces interruptions, but does not fully automate the original scope"). This note could cite that case directly instead of leaving the reader to connect them.
- The description says "adoption can run unattended while monitoring or subsequent revision still requires a person". Under the note's own definitions, "requires" there carries only the obligation sense unless a blocking case is shown. That is the same equivocation at the retrieval surface.
- The note has no Relevant Notes footer, even though it links two neighbours inline with clear roles: it complements one and relies on the other.
