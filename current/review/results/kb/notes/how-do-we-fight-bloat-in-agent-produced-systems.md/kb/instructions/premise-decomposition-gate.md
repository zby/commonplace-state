---
type: types/review-result.md
format: 2
description: Retained report review of kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
  against kb/instructions/premise-decomposition-gate.md
note: kb/notes/how-do-we-fight-bloat-in-agent-produced-systems.md
note-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
criterion: kb/instructions/premise-decomposition-gate.md
criterion-sha256: 116fc35b1e54759064658a1172d7ed0a3007bf576f6744f6f016f473d477805d
outcome: report
profile:
  harness: claude-code
  launch-model: opus
  effort: medium
model: claude-opus-5-5
run: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews
launch: f4f526e4770546bc9cf63f3a61b51e62
completed-at: '2026-11-25T05:28:03Z'
findings:
- scope: document
  quotes: []
  reason: 'DOUBTFUL — Unstated premise, universal: the five listed mechanisms are
    operative in Commonplace now, not only argued in theory notes; the note asserts
    that ''Commonplace currently counters bloat'' with them. — Two of them depend
    on things the note itself leaves open. The value gate is ''connected to'' How
    do we value notes?, which is another open standing query, not a working gate.
    The two retirement mechanisms (operative retirement path; retire fixed-difficulty
    scaffolding) rely on retirement triggers that the Unsettled section says ''we
    lack''. The linked scaffolding note calls recurrence ''a live hypothesis, not
    a measured trend'' and gives no Commonplace retirement procedure. If any mechanism
    is only a theory claim, ''currently counters'' overstates the answer. Rewording
    the claim as the current partial theory, or naming the procedure or check that
    implements each mechanism, keeps the commitment. — LOCAL — instance'
- scope: passage
  quotes:
  - Empirically, agents default to additive changes — adding a helper, guard, section,
    or new note — rather than deleting or consolidating existing structure.
  reason: 'DOUBTFUL — Tendency claim, called empirical: agents default to additive
    changes instead of deletion or consolidation. — The note cites no observation,
    log entry or source for it, so the word ''empirically'' has nothing to point to.
    There is also well-known opposite behaviour under check pressure: coding agents
    delete or weaken failing tests, or remove code paths, to make a check pass. That
    is subtraction, though not useful consolidation. These cases do not defeat the
    tendency, but they show the bias depends on which pressure the agent is under.
    The premise needs evidence and a boundary such as ''when no check rewards removal''.
    The open question survives either way. — LOCAL — instance'
- scope: passage
  quotes:
  - Natural language has no comparable reachability check
  reason: 'DOUBTFUL — Universal: natural language has no reachability check comparable
    to code''s unused-symbol checks, call graphs and coverage. — Partial analogues
    exist: link validation and orphan or backlink detection over the note graph, read
    logs from retrieval, and the attempted-recovery assay in the linked seven-case
    sweep. That assay decided which prose was recoverable from live source, so it
    worked like a reachability test for exact-fact prose. None of these checks decides
    whether a passage changes a decision. But code checks don''t decide that either,
    as the note concedes (''even those miss live but over-engineered code''). So the
    gap is narrower than ''no comparable check''. The repair is to say which property
    lacks a check (decision relevance, not graph reachability). — LOCAL — instance'
- scope: passage
  quotes:
  - Bloat in these mixed systems compounds through three channels
  reason: 'DOUBTFUL — Universal: bloat compounds, meaning cost grows with accumulated
    bloat, through context and routing cost, maintenance and drift, and recursive
    exposure. — ''Compounds'' implies more than linear accumulation, and the note
    does not argue for that. In a retrieval-gated system, context cost scales with
    what gets routed into a task, not with total store size. An unretrieved, unlinked
    redundant note costs little context. The recursive-exposure channel (retained
    material ''anchors later generations'') is asserted without a linked mechanism
    or observation. The maintenance channel is grounded through the maintenance-capacity
    link. Restating ''compounds'' as ''accumulates cost'', or conditioning it on material
    that is routed or co-maintained, keeps the stakes. — LOCAL — instance'
- scope: passage
  quotes:
  - Pushing models to write shorter text does not automatically reduce content bloat
  reason: 'DOUBTFUL — Universal in form, covering any way of pushing for shorter text:
    brevity pressure can keep content while distorting the wording. — The cited evidence
    comes from two sources: a corpus comparison of frontier output against round-trip
    paraphrases, and a length penalty applied during RL fine-tuning. The common Commonplace
    case is different: a prompt-time or review-time instruction to shorten an existing
    note. The note''s own evidence entries (two rewrites; three simplification passes)
    report naive shortening that dropped relations, not wording squeezed into dense
    syntax. So for prompt-level pressure, the premise extrapolates the training-time
    mechanism. The repair is to scope the premise to training-time pressure or mark
    prompt-level transfer as a conjecture. — LOCAL — instance'
- scope: passage
  quotes:
  - showed in a bounded sweep that direct access to live source and CLI help eliminated
    exact-fact prose copies
  reason: 'DOUBTFUL — Bounded: in one Commonplace sweep, direct access to live source
    and CLI help removed exact-fact prose copies. — The linked evidence supports the
    result, but it also records a precondition the note omits. Removal was safe only
    after `commonplace-source` and help paths were repaired; the evidence note says
    ''source access is a prerequisite''. The sweep covered one Python CLI repository.
    Without that precondition, the ''Do not write what the live source already supplies''
    mechanism would fail for source-inaccessible artifacts. The phrase ''cutting six
    candidate pages by 53 percent and retiring two'' also reads as eight artifacts.
    There were seven, and the six byte-counted pages include a retired one. — LOCAL
    — instance'
- scope: passage
  quotes:
  - Local rewrites confirm that raw brevity is the wrong target
  reason: 'HOLDS — Bounded by the cited local cases: naive shortening dropped technical
    relations, and clearer rewrites sometimes added words, so word count does not
    measure information. — A hunt for a case where cutting words always kept structure
    found nothing that defeats the premise as scoped. ''Confirm'' is slightly strong
    for five passes, but the claim is about targeting, not prevalence.'
- scope: passage
  quotes:
  - even locally sound additions (tags, schemas, templates, conventions) accumulate
    routing and migration debt when adding is local and retiring needs distributed
    evidence and migration
  reason: 'HOLDS — Conditional: when adding is local and retiring needs distributed
    evidence and migration, locally sound additions accumulate debt. — The condition
    carries the claim. A counterexample would need cheap retirement under those conditions,
    and that would violate the antecedent. No defeater found.'
- scope: passage
  quotes:
  - without a value gate, valid redundant artifacts still accumulate
  reason: 'HOLDS — Conditional: validity checks alone do not stop valid but redundant
    artifacts. — Structural and grounding checks test well-formedness and support,
    not marginal contribution, so a valid duplicate passes them. Whether Commonplace
    has such a value gate is a separate premise, covered by the operative-mechanisms
    finding.'
- scope: passage
  quotes:
  - Agents make generating both code and natural-language artifacts — notes, documentation,
    specifications, instructions, tests, and schemas — cheap.
  reason: HOLDS — Agents lower the cost of producing code and prose artifacts, which
    raises potential inflow. — No counterexample found. Review and maintenance costs
    may not fall, but that supports the note's inflow-versus-capacity framing rather
    than defeating the premise.
contract: report
target-sha256: a15f8c0577e0b2e9b5670af47e741dc81ad6f48a78b442cb75a20f783a995c36
target-capture: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/f4f526e4770546bc9cf63f3a61b51e62/inputs/note.md
observation: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/artifact/reviews/5fc9a8202b6f7b2ba99c9a2c/observation.json
contract-sha256: e1833bb74645a85c69185c6f1cb536109cd143c1cc2f37344fbbdda8582ef082
raw-output: kb/workflow-state/data/current/review/runs/v2/revise/kb/notes/how-do-we-fight-bloat-in-agent-produced-systems/20261125T052330Z/reviews/calls/launches/f4f526e4770546bc9cf63f3a61b51e62/outputs/review.md
raw-output-sha256: 44b8700c45cfeaa9bca1d24d13f979bad46e81ed0b471f169e270a19c1645c41
---

# Premise decomposition: How do we fight bloat in agent-produced systems?

**Register:** claim
**Central commitment (one sentence):** In agent-produced systems that mix natural language and code, bloat accumulates costly context, maintenance and recursive-exposure load that software anti-bloat defences do not cover. Commonplace currently controls it only partly, with five mechanisms: omit content the executor or live source supplies; target expansion that adds no structure; give additions a retirement path; retire scaffolding for fixed-difficulty tasks; and gate inflow by value.

## Premises and counterexamples

The note is a standing query, so it has two commitments. The Stakes section argues that bloat in mixed systems is costly and that existing defences miss it. The Current answer section says Commonplace already has five mechanisms against it. The Stakes rest on cheap generation, the three cost channels and the missing reachability check for prose. The Current answer rests on each mechanism's own premise. It also rests on one premise the note never states: that the mechanisms are operative in Commonplace, not just argued in linked theory notes. I counted the Unsettled items as premises only where the note asserts a fact while posing the question: the claim about agents' additive bias and the claim about brevity distortion. The other Unsettled items are open questions, not premises.

No premise fails globally. Every doubt can be answered by narrowing a modality, adding a precondition or rewording 'currently counters'. The conditional premises about adoption and retirement and about value gates hold because their conditions are stated. The doubts sit in universal or 'empirical' wording that outruns the cited evidence, and in a tension the note creates: the Current answer presents retirement and value gating as working mechanisms, while the Unsettled section and a linked open query say their triggers and tests are missing.

## For the human

Look first at the unstated premise that the five mechanisms are operative. The note's own Unsettled section says retirement triggers are missing, and value gating is still an open query, which undercuts 'Commonplace currently counters bloat'.
