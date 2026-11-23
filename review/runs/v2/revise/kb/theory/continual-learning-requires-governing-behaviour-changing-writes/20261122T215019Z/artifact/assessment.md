# Assessment: Continual learning requires governing behaviour-changing writes

**Proposed purpose (no purpose was named; the operator may correct it):** Agents and
maintainers who design or classify deployed learning systems should be able to tell when a
retained write counts as continual learning, and what a loop must do beyond storing content
for such writes to improve behaviour safely.

**Outcome: stop.** The highest-value change is a decision about the note's central claim.
The passes cannot make that decision. Two connected defects sit in the discriminator
sentences of the final paragraph. Correcting them changes what the title's "requires"
means, and the role report shows that dependents rely on the sense of that discriminator.
No passes are planned.

## Ranked changes

1. **Decide what "requires" claims, and recast the field attribution.** Cost: one operator
   decision, then a rewrite of the opening sentence, the description and two or three
   sentences of the final paragraph. Route: rewrite, not a pass (see Stop).
   - The sentence "Continual learning, as the field uses the term and as this note uses it,
     asks for more: the system does the selecting itself" attributes the self-selection
     condition to the field without a source. Four depth 1 reports and three semantic gates
     converge on this sentence.
   - The discriminator then makes reject-capable evaluation part of what counts as continual
     learning ("for retained candidates, search, reject-capable evaluation, and operative
     retention").
2. **Replace or qualify the support for "continual adaptation compounds silent
   degradation".** Cost: one sentence plus a link change. The cited note
   (`scheduler-llm-separation-exploits-an-error-correction-asymmetry.md`) contains no
   mention of degradation, regression, compounding or continual adaptation; I checked this
   with a search of the target. The fix-strategy-taxonomy pass responds to
   `semantic/grounding-alignment`, so it could take this finding once the run resumes.
   The role report lists ingests that may support the premise instead: dual-nature
   on-policy distillation, DFA-MoE and MerchantBench.
3. **Put the self-selection condition in the opening and description** (synthesis
   opportunity 1). Cost: one sentence and the description. This depends on decision 1, so it
   is a choice for the rewrite, not a pass.
4. **Reorder the final paragraph** (synthesis opportunity 2). Merge the doubled
   human-selection contrast (release engineering, then the incident edit) into one statement
   next to the proposal-selection criterion. Move the codification-and-relaxing aside into
   the forms paragraph. Cost: one paragraph. Pass: readability-and-flow. Deferred, because
   the paragraph is the one decision 1 rewrites.
5. **Split the dash-appended requirement list into its own sentence with a verb**
   (clause-packing and parsing-ambiguity findings). Cost: one sentence. Pass:
   readability-and-flow or plain-wording. Deferred for the same reason as item 4.
6. **Repair the footer labels and stale link texts.** Cost: footer only. Pass:
   fix-strategy-taxonomy cannot take these findings (`kb/theory/COLLECTION`,
   `sentence/misleading-link-text` are not in its `responds-to`), so they need a
   readability or plain-wording packet, or a hand edit. Details:
   - `defines` should be `defined-in`.
   - `sharpens` is not a registered label (two edges).
   - `exemplifies` runs from the general claim to its instance, the wrong direction.
   - `evidenced-by` does not say whether the survey corroborates the claim or only bounds it.
   - Two link texts use stale titles. "Only explicit retention is durable, writable, and
     addressable" is now "Explicit retention provides direct targets for selective
     revision". "Constraining during deployment is continual learning" is now "Constraining
     during deployment can produce learning outside weights". Both stale texts claim more
     than their targets now do.
7. **Add a `## Scope` section** (note-type finding). Cost: moving three or four existing
   limits out of the body. Pass: readability-and-flow. Deferred, because the limits it would
   collect include the learning/maintenance boundary that decision 1 changes.
8. **Gloss "operative retention", "reject-capable evaluation" and "contextual activation"
   inline** (undefined-terms finding). Cost: two short glosses. Pass: abstractions or
   plain-wording. The first two sit in the sentence decision 1 rewrites, so this is deferred.
9. **Cut defensive redundancy in the forms paragraph.** The two sentences are "It need not
   touch all three every time" and "broadening the system boundary does not remove them".
   Cost: two clause cuts. Pass: plain-wording. This is low value against the purpose. "Need
   not touch all three" is also the body's correction of the description's "across the
   representational forms a system can change", so it should not be cut until the
   description matches it.

## The sentence a hostile reviewer would attack first

"Continual learning, as the field uses the term and as this note uses it, asks for more: the
system does the selecting itself."

The machine-learning continual-learning literature defines the term by learning from a
non-stationary stream without catastrophic forgetting. Its paradigm cases are sequential
gradient training with regularization or replay, such as elastic weight consolidation (EWC).
In those cases every update is installed without a reject-capable adoption gate. The note's
own linked proposal-selection note says evidence "may instead determine an update directly",
with "nothing rejectable anywhere in the path"; see
`kb/theory/a-proposal-selection-loop-requires-search-evaluation-and-retention.md`.

## What reads well

The opening argument reads well. Because behavioural authority belongs to a consumption path
rather than to stored bytes, persistence cannot decide which item shapes behaviour or with
what force. The concession that parametric forgetting problems persist keeps the cross-form
argument fair.

## Overclaims: support or divergence

- "as the field uses the term": **support**, and wrong as worded. It should be narrowed to
  the note's own stipulation or sourced. This is part of the stop.
- "because continual adaptation compounds silent degradation": **support**. It may be
  narrowed or re-grounded, but the regression-validation requirement it supports is relied
  on by five dependents (dfa-moe, dual-nature OPD, merchantbench, long-horizon-agents,
  harness-continual-learning), so the requirement itself is **divergence** and must be kept.
- "deployment evidence arrives online and is often sparse, so candidate writes must be cheap
  to propose and install": **support**. Sparsity does not support cheapness; only online
  arrival does (friction report). The sentence may be narrowed to the agent-deployment
  domain.
- "a learning loop must decide which form a lesson belongs in": **support**. It may be
  narrowed to systems with several writable forms, or allow the decision to be made at
  design time (premise report).
- "persistence does not decide which retained item should shape behaviour or with what
  force": **divergence**. This is the note's core; keep it.
- "an updater restricted to weights freezes consequential choices outside its reach":
  **divergence**. Dependents rely on it (token-space, Huxley-Gödel machine); keep it.
- Hand-authored changes are learning by human selection, not continual learning:
  **divergence** in its first half ("the system learned"). The label "maintenance" is part
  of decision 1.

## Stale qualifications (claim questions for the operator, not passes)

- The description says updates must be coordinated "across the representational forms a
  system can change". The body says a loop "need not touch all three every time".
  The description should match the body.
- The footer gloss on the explicit-retention link says "the form-level trade space this note
  defers to". The body defers that trade space to the representational-form coevolution
  note instead.
- Several footer `grounds` glosses name "axes" the body never uses: reach, addressability,
  sample efficiency and verifiability.
- The footer gloss on the scheduler-LLM link ("why symbolic writes are cheaply validated and
  parametric ones are not") extends the target to parametric writes, which it does not
  discuss.

## Claim questions for the operator

These are in addition to the stop. They are one-or-two-sentence corrections that a rewrite
under decision 1 should absorb.

- **Human approval inside the loop.** Source: completeness-boundary-cases finding; premise
  report (`.../reviews`); role report (`.../role`), hyra-2 dependent. Suppose a system
  proposes and evaluates a candidate from deployment evidence, and an operator approves it
  before installation. Does the write remain continual learning? The note lists
  "authorize" among the governance steps but places human selection outside the loop.
- **Write time or read time.** Source: critique report; premise report. Authority belongs
  to a consumption path, and store-everything memory systems select at read time. Does
  "governing behaviour-changing writes" include governing at read time? If it does not, the
  title mis-sorts a recognizable design.
- **No retire or revert step.** Source: role report (agentic-reasoning survey,
  intern-s2-mobius). Two dependents attribute a retire or revert step to the note's
  governance list. The note states none.

## Findings not acted on

- All warn findings are deferred by the stop. Items 4–9 above say which pass each would take
  after the rewrite.
- Info findings are not acted on. They are low value against the purpose:
  - behavioral-authority gloss reads as force only;
  - "some lessons must take effect" reads as stronger than derived;
  - cadence-sentence redundancy;
  - advisory memory writes;
  - the "selection" and "consumption path" glosses.
- **Untaken recommendation from dual-nature OPD** (add a bounded post-training example
  showing that regression validation must reach beyond an update's nominal domain): an
  extension, which the purpose does not ask for.
- **Untaken evidenced-by candidate from faithful-self-evolvers:** an extension.
- **Friction report: authorization is not argued.** The report says the "authorize" step is
  introduced without earlier argument. This is an extension; the step follows from the
  consumption-path premise as a design consequence. A rewrite may still address it.

## Stop

**Defect** (reports: `kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/critique-note.md`,
`kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/premise-decomposition-gate.md`,
`kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/composition-friction-gate.md`;
corroborated by the conceptual-role-conflation, epistemic-status-blur and
underspecified-assertions findings).

**The two readings.** The wording supports two readings of "requires":

- **Constitutive.** An ungoverned durable change is not continual learning. The final
  paragraph reads this way: the system must select, with reject-capable evaluation.
- **Reliability.** Governance is what continual learning needs in order to improve
  behaviour without regression. The regression argument and the note's own grounding
  criterion support this reading: "learning is any durable change in a system's capacity
  to adapt".

**The case.** A deployed model updated online by gradient steps is continual learning as the
field uses the term. Under the constitutive reading the note classifies it as not continual
learning. Under the reliability reading it is continual learning that the note says needs
validation. The note also asserts that the field uses the term in the constitutive sense,
which the field's paradigm cases contradict.

**Why this stops the run.** Correcting this sets the sense of the title claim and of the
system-selected discriminator. The role report (run directory
`kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/role`)
shows dependents relying on that discriminator:

- `kb/sources/hot-take-llm-can-jump.ingest.md`
- `kb/sources/on-learning-how-to-learn-learning-strategies.ingest.md`
- `kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md`

It also shows `kb/sources/hyra-2-next-step-for-auto-research.ingest.md` reading human
approval as governance, which the discriminator leaves open. The operator must decide the
dependents' change too.

**Unsupported premise.** The regression premise "continual adaptation compounds silent
degradation" is unsupported by its only citation (grounding-alignment fail). It should be
re-grounded in the same rewrite.

**Route.** `commonplace-revise rewrite kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md --commission FILE`,
with the commission prepared with `cp-skill-write-multistage`. The commission should:

- state the chosen reading of "requires";
- recast "as the field uses the term" as the note's stipulation, or source it;
- say how direct-update continual learning stands to the claim;
- place operator approval relative to the loop;
- re-ground the regression premise;
- carry the must-keep items in the plan.

After the rewrite, a new run can take items 4–9.
