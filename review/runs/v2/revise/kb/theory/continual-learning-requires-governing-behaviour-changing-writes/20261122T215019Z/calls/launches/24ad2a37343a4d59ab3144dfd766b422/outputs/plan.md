purpose: "Agents and maintainers who design or classify deployed learning systems should be able to tell when a retained write counts as continual learning, and what a loop must do beyond storing content for such writes to improve behaviour safely."
must-keep:
  - "Persistence does not decide which retained item should shape behaviour or with what force; behavioural authority belongs to a consumption path, not to stored bytes."
  - "If prompts, tools, validators, and runtime policy also determine behaviour, then an updater restricted to weights freezes consequential choices outside its reach."
  - "Candidate writes in a deployed learning loop must be validated against regression."
  - "Hand-authored changes are learning too: the software learns by selection that people perform on it."
passes: []
stop: >-
  Defect (critique report kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/critique-note.md;
  premise report kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/premise-decomposition-gate.md;
  friction report kb/reports/state/review/results/kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md/kb/instructions/composition-friction-gate.md).
  The wording supports two readings of "requires".
  Constitutive: an ungoverned durable change is not continual learning, as the final paragraph's system-selection discriminator with reject-capable evaluation implies.
  Reliability: governance is what continual learning needs to avoid regression, as the regression argument and the note's broad learning criterion imply.
  Case: a deployed model updated online by gradient steps is continual learning as the field uses the term.
  It is excluded under the first reading and included under the second.
  The sentence "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself" asserts the field uses the constitutive sense, which the field's paradigm cases (sequential training with regularization or replay, such as elastic weight consolidation) contradict.
  The linked proposal-selection note also allows direct updates with nothing rejectable.
  Correcting this sets the sense of the title claim and of the system-selected discriminator.
  Dependents rely on that discriminator (role report run directory kb/reports/state/review/runs/v2/revise/kb/theory/continual-learning-requires-governing-behaviour-changing-writes/20261122T215019Z/role):
  kb/sources/hot-take-llm-can-jump.ingest.md, kb/sources/on-learning-how-to-learn-learning-strategies.ingest.md, kb/sources/knowledge-centric-self-improvement-2607.19592.ingest.md;
  kb/sources/hyra-2-next-step-for-auto-research.ingest.md reads human approval as governance, which the discriminator leaves open.
  The operator must decide those dependents' change too.
  In the same rewrite, the regression premise "continual adaptation compounds silent degradation" is unsupported by its only citation (scheduler-LLM separation note; grounding-alignment fail) and needs re-grounding.
  Route: commonplace-revise rewrite kb/theory/continual-learning-requires-governing-behaviour-changing-writes.md --commission FILE, with the commission prepared with cp-skill-write-multistage.
  Wording passes (readability-and-flow, plain-wording, footer and label repairs) are deferred until after the rewrite, because they would edit the opening and final paragraph that the rewrite replaces.
