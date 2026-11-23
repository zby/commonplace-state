---
description: Tells apart a learning system that acquired or revised a rule governing future decisions from one that retained new evidence under unchanged rules, by tracing how the deployed system consumes the write
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, self-improving-systems, continual-learning, improvement-loop]
---

# Continual learning requires governing behaviour-changing writes, not just storing content

A learning system can change its future behaviour in two different ways. It can retain new evidence that its unchanged rules then consult. Or it can acquire or revise a rule — an instruction, a check, or a routing rule — that governs later decisions. Both are learning in the broad sense of [durable change in capacity to adapt](./learning-is-not-only-about-generality.md). This note concerns only the second. Output that depends on history does not by itself show it, because rules that never change can still consult a growing record.

What separates the two is how the deployed system uses the write, not what the write says or where it is stored. [Behavioral authority](./definitions/behavioral-authority.md) names the consumer, the channel and the force of one consumption path, and "declared intent is not enough" ([behavioral authority](./definitions/behavioral-authority.md)). A [knowledge artifact](./definitions/knowledge-artifact.md) can change behaviour by changing what a consumer considers, but it "does not by itself bind the next action". A [system-definition artifact](./definitions/system-definition-artifact.md) is consumed with instruction, routing, validation or enforcement force, whatever its substrate.

## One incident, three interpretations

A wiki-maintaining agent proposes pages; a reviewer model accepts or rejects them. A page is accepted with a figure that its cited source does not contain. Afterwards the system writes something. Three writes are possible, and each implies a different later decision when the old and new rules disagree. The test case is a new page with a numeric claim and no quoted source passage.

| Interpretation | Consumer, channel, force | What changed | When old and new disagree |
|---|---|---|---|
| Incident kept as advice | Reviewer model; retrieval into context; advice | Nothing in the rule. The acceptance criterion is the same; the reviewer now has one more case to weigh. | No rule disagreement exists. The reviewer may or may not judge the incident relevant and may accept the page. |
| Standing reviewer prompt changed | Reviewer model; prompt assembly as standing instruction; instruction | The acceptance criterion now says to reject numeric claims without a quoted passage. | The old prompt permits acceptance; the new one instructs rejection. The reviewer can still fail to follow it, because an instruction is not guaranteed enforcement. |
| Validator changed | Validator runtime; validation before acceptance; fail force | A check now fails such pages. | The page is blocked whatever the reviewer concludes. |

A rule can also change while consumer, channel and force all stay fixed. If a validator that already checked quotes on source summaries is rescoped to all pages, only the cohort it acts on changes. That is still a revised rule. [Consumer, channel and force can stay fixed while the governed use changes](./evidence/consumer-channel-and-force-can-stay-fixed-while-the-governed-use.md) shows this shape with a trait-scoped review gate and a type-scoped validator. Those cases illustrate a rule's scope; they are not observed learning episodes.

Saving `policy.md` with the new requirement changes no rule if no component loads it. Conversely, the incident record from the first row can acquire instruction-like effective authority if the harness always places it late in the reviewer's prompt. Classification follows the actual path, so the same text can count differently in two systems.

## The diagnostic

For an actual system, ask three separate questions:

1. **Did a governing rule change?** Name the path that consumes the write and a case where the old and new rule decide differently. If no such case exists, or the write reaches the decision only as one consideration among others, the system retained evidence.
2. **Did deployment experience lead to it?** A changed rule may have been hand-authored after the incident. Showing that the system's own loop proposed and retained it is a separate lineage claim (see [a proposal-selection improvement loop](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md)).
3. **Does it help?** Neither of the first two answers shows that the new rule makes better decisions. That needs evaluation on cases the change was not built from.

## The universal-machine objection

The strongest objection says the distinction is not real. Any learned rule, including arbitrary learned code, is data to a fixed universal interpreter: the model weights, the Python runtime or the harness. At that level every case is new evidence processed under unchanged rules. Executable syntax does not rescue the distinction either. Suppose the system writes a nearly executable validator that needs an LLM to add a wrapper before it can run. Whether it is code or advice is not settled by its syntax.

The objection is correct at the interpreter level, and this note does not dispute it. The distinction is drawn at a different level: the components of the deployed system and how each treats the write. If the pipeline wraps and runs that validator as a gate before acceptance, it is a check. If a model reads it and decides whether to apply it, it is advice or instruction, depending on the path. The choice of level is practical. It identifies which artifact to audit, roll back or test when a decision changes, and where a disagreement between old and new rules gets decided.

## Scope

- This note does not define learning or continual learning as revising governing rules. Retaining evidence under unchanged rules is also learning.
- It does not require a reject-capable gate, human exclusion from the loop, or a self-modifying interpreter. An instruction change with no gate is a rule change.
- It makes no claim that a revised reviewer outperforms a fixed reviewer with access to advisory history. A general fixed reviewer that consults the whole incident record may reach the same decisions.
- The current title states the target more broadly than this body argues; the body's contribution is the distinction and its diagnostic.

## Open Questions

- Under what workload, time or reliability constraint, or cost of error would consulting retained experience not suffice, so that a system needs to change its governing rules? Candidate conditions include a history too large for retrieval to surface the relevant incident, decisions that must stay consistent across many reviewer calls, and errors costly enough that a consideration the reviewer may ignore is not acceptable. None of these is shown here to make rule revision necessary.

---

Relevant Notes:

- [Behavioral authority](./definitions/behavioral-authority.md) — defined-in: consumer, channel and force, and effective use versus declared intent
- [Knowledge artifact](./definitions/knowledge-artifact.md) — defined-in: evidence and advice that change behaviour without binding the next action
- [System-definition artifact](./definitions/system-definition-artifact.md) — defined-in: instruction, validation and enforcement uses, regardless of substrate
- [Consumer, channel and force can stay fixed while the governed use changes](./evidence/consumer-channel-and-force-can-stay-fixed-while-the-governed-use.md) — evidenced-by: scoped gate and validator cases that bound the authority record; they illustrate rule scope, not learning
- [Learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: the broad learning criterion under which both evidence retention and rule revision count
- [A proposal-selection improvement loop requires search, evaluation, and operative retention](./a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — extends: what it takes to show the system's own loop selected a changed rule
- [LLM contexts interpret instructions and content through the same token medium](./llm-context-interprets-instructions-and-content-through-one-medium.md) — mechanism: why advisory text can acquire instruction-like force by placement
