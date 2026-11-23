---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "selecting a candidate update, validating it, and deciding how it enters the behaviour-determining system"
    reason: "DEFEATED — Premise (unmoded, so universal): every continual-learning update is a selected candidate that is validated before or while it enters the behaviour-determining system. — Counterexample: canonical parametric continual learning (online fine-tuning, EWC, experience replay) installs each gradient update directly; no candidate stands to be rejected. The linked proposal-selection note itself classifies online gradient descent (Zinkevich's Greedy Projection) as a direct update whose step 'contains no candidate-adoption decision'. This note also treats parametric continual learning as continual learning ('Parametric continual learning keeps its own plasticity-stability ... problems'). Read universally, the requirement excludes a case the note counts. — LOCAL: scope the selection-and-validation requirement to proposal-selection writes (retained candidate artifacts), or say that for direct updates governance sits at the update rule and its deployment gate rather than at each write. Either repair keeps the core claim that persistence is not governance. — instance"
  - scope: passage
    quotes:
      - "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself."
    reason: "DEFEATED — Premise (unmoded, so universal): the field's usage of 'continual learning' requires that the system itself select retained writes on deployment evidence. — Counterexample: the standard continual-learning literature and its benchmarks (task-incremental and class-incremental streams such as Split-MNIST) define the problem as learning from a nonstationary sequence without catastrophic forgetting. The task stream is curated and sequenced by researchers, usually offline, and every update is applied by the learning rule with no per-write selection or rejection. Any reader can check that this usage involves neither deployment evidence nor self-selected writes. The note's discriminator is therefore a stipulation, not field usage. — LOCAL: drop the 'as the field uses the term' attribution, or present the discriminator as this note's narrowing for deployed systems; the governance argument does not depend on the attribution. — instance"
  - scope: passage
    quotes:
      - "The same edit hand-authored in reaction to an incident is maintenance: the system learned, and people outside its loop did the selecting."
    reason: "DOUBTFUL — Premise (unmoded): whether the system or people outside its loop did the selecting is a determinate fact that sorts behaviour-changing writes into continual learning versus maintenance. — Reason: the ordinary production pattern is mixed. An agent proposes a memory, rule or patch from deployment evidence, and a human approves or rejects it. The linked proposal-selection note explicitly allows one declared socio-technical loop in which 'a maintainer may choose the problem, a model may draft a candidate'. Whether the approver is inside the loop then depends on where the boundary is declared. Declare the boundary to include release engineers, and incident-driven hand edits become continual learning. The discriminator is boundary-relative, and this note does not fix the boundary. — LOCAL: add a boundary condition, for example that the loop is triggered by deployment evidence without per-incident human initiation and that human approval counts as one evaluator. This keeps the distinction. — prevalence"
  - scope: passage
    quotes:
      - "because continual adaptation compounds silent degradation"
    reason: "DOUBTFUL — Premise (unmoded): candidate writes must be validated against regression, because continual adaptation compounds silent degradation. — Reason: widely deployed memory features install natural-language writes, such as user facts and preferences appended to always-loaded context, with no regression check. For natural-language writes judged against 'open-ended behaviour', no regression oracle exists in the ordinary case. In practice, post-install monitoring and rollback stand in for pre-install validation. The compounding-degradation mechanism is plausible as a tendency but is not argued here. The linked scheduler-LLM note grounds an error-correction asymmetry, not compounding under continual adaptation. — LOCAL: widen 'validated' to include post-install evaluation that can roll back, which the linked proposal-selection note already allows, and state the degradation claim as a tendency under named conditions. Alternatively, accept that unvalidated memory writes fall outside governed continual learning and say so. — prevalence"
  - scope: passage
    quotes:
      - "persistence does not decide which retained item should shape behaviour or with what force"
    reason: "HOLDS — Premise (unmoded): persistence alone does not decide a retained item's behavioural authority; the consumption path does. — Hunt: an always-loaded memory file seems to make persisting the item equal to giving it authority. In that case, though, the authority comes from the writer choosing a location that has a fixed consumption path. Storage does not make that decision, so the counterexample confirms the premise."
  - scope: passage
    quotes:
      - "deployment evidence arrives online and is often sparse"
    reason: "HOLDS — Premise (tendency: 'often'; 'some lessons'): deployment evidence is often sparse and online, so some lessons must take effect before a full retraining cycle. — Hunt: high-traffic systems with dense telemetry, such as large recommenders, weaken the sparseness claim. However, the premise is stated as a tendency and asks only for some early-installed lessons, so these cases do not reach prevalence against it."
  - scope: passage
    quotes:
      - "an updater restricted to weights freezes consequential choices outside its reach"
    reason: "HOLDS — Premise (conditional on prompts, tools, validators and policy determining behaviour): a weights-only updater freezes the consequential choices made by those artifacts. — Hunt: weight updates can partly compensate for a bad prompt by learning to override soft instructions. They cannot change what a schema, validator or tool interface accepts, so some consequential choices stay frozen, and the conditional holds."
  - scope: passage
    quotes:
      - "The forms differ in installation cost and verifiability"
    reason: "HOLDS — Premise (unmoded): representational forms differ in installation cost and verifiability, so a loop that writes several forms must decide where a lesson belongs. — Hunt: when a loop can write only one form, as in a memory-only agent, the placement decision is degenerate. The note's 'may include' and 'need not touch all three' already scope the premise to multi-form writable surfaces. The revisability of placement is also conceded through codification and relaxing."
outcome: report
---

# Premise decomposition: Continual learning requires governing behaviour-changing writes, not just storing content

**Register:** claim
**Central commitment (one sentence):** In a deployed system, continual learning requires the system's own evidence-responsive loop to govern durable behaviour-changing writes. Governing means selecting a write, validating it against regression, assigning it an authority path and coordinating it across representational forms; persisting content is not enough.

## Premises and counterexamples

The commitment has two layers. The negative layer says persistence is not governance, and it rests on the authority-by-consumption-path premise. That premise survived the hunt. The positive layer defines what governance is. It consumes four premises:

- every continual-learning update passes through selection and validation;
- validation against regression is required;
- the multi-form writable surface makes form placement a decision;
- self-selection by the system's own loop separates continual learning from maintenance.

The note's scope also rests on two enabling premises: deployment evidence is sparse and online, and a weights-only updater leaves choices frozen.

The defeats fall on the positive layer, where the note generalizes. Read without a stated mode, the requirement to select and validate every candidate excludes direct-update parametric continual learning. The note elsewhere counts that as continual learning, and its own linked proposal-selection note classifies it as having no candidate-adoption decision. The appeal to 'the field's' usage also fails: the standard continual-learning literature involves neither deployment evidence nor self-selected writes. Neither defeat breaks the mechanism. Scoping the requirement to proposal-selection writes, and presenting the self-selection discriminator as a stipulation for deployed systems, keeps the note's explanatory reach.

Two premises are dented. The self-selection discriminator depends on where the loop boundary is drawn, and human-approval gates are the ordinary case. The regression-validation requirement conflicts with common unvalidated memory writes and with the lack of an oracle for open-ended natural-language behaviour. Each is repaired by a boundary condition or by widening 'validation' to post-install rollback.

## For the human

Look first at the first-paragraph requirement to select and validate every candidate update. Its conflict with direct-update parametric continual learning, which the note counts as continual learning, is the load-bearing defeat. Scope that requirement to proposal-selection writes, and drop or reword 'as the field uses the term' to match.
