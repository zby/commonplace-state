---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated, universal: the instruments that measure the declared relation (test suites, evaluators, benchmarks) stay fixed outside the compared states, so declaring the relation in advance fixes what is measured. — The note places tests and evaluators inside the compared states ('prompts, natural-language artifacts, code, tools, workflows, tests, evaluators') and lets the successor improve through any of them. In an ordinary coding-agent factory, the non-regression suite is the factory's own test suite. A successor that weakens, deletes or rewrites those tests passes non-regression 'on the predecessor's prior scope' while regressing. An antecedent declaration of dimensions and thresholds does not stop the measuring instrument from drifting with the successor. The gaming sentence about inspectable acceptance tests names part of this risk, but no declaration requires freezing or externalising the instruments. — LOCAL: add a condition that the assessment instruments are pinned to the predecessor's version or held outside the compared states. — instance"
  - scope: passage
    quotes:
      - "Without the index, the requirement is either unmeetable or vacuous depending on how generously the reader reads \"no worse\"."
    reason: "DOUBTFUL — Universal: indexing non-regression to the predecessor's prior scope ('what that state could already do') makes the requirement determinate and checkable. — For an open production family, 'what the state could already do' is not enumerable. In practice it is approximated by a finite suite, so the declared thresholds cover a sample of the prior scope rather than the scope. A successor can pass on the suite and regress off it, so 'no worse' becomes as generous or strict as the suite chosen. The note's first open question concedes the problem but leaves the body's claim that indexing fixes the ambiguity unqualified. — LOCAL: state that the declared prior scope is a finite proxy and move the determinacy claim onto that proxy. — prevalence"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated, universal: one operative state yields one result under the declared thresholds, so declaring dimensions and thresholds settles pass or fail. — Factories built on sampled LLM calls are ordinarily nondeterministic: the same predecessor and successor give different scores across runs. Without a declared sampling plan and decision rule (run count, confidence or margin), two auditors can apply the same antecedent relation and reach opposite verdicts. The claim is then still open to post-hoc choice, through reruns and through which runs are counted. The four declarations omit this, but the commitment says those four make the claim determinate. — LOCAL: include the statistical decision rule in the declaration of the assessment relation. — prevalence"
  - scope: passage
    quotes:
      - "Measuring whether a realized change helped does not by itself place a person on the causal update path: the measurement follows the update and does not determine it."
    reason: "DOUBTFUL — Universal: measurement over a realized trajectory follows the update and does not determine it, so a measuring evaluator is off the causal path. — The relation is declared in advance, so developers know it while they develop. Under the note's own premise of an interleaved process, earlier measurements feed later changes. Teaching to a known benchmark and iterating on interim scores are ordinary practice. In both cases the antecedent measurement shapes what the factory retains without gating installation. This blurs the line between admission and measurement, which the separation of evaluator location from learner boundary relies on. The Scope bullet that treats routes as readings of an episode fences part of this, but not anticipatory influence. — LOCAL: qualify 'does not determine' as 'does not gate' and say whether anticipatory or interim-score influence counts as being on the path. — prevalence"
  - scope: passage
    quotes:
      - "This is not an extra virtue bolted onto the comparison; it is what scope-indexed non-regression already says once the factory-development path is part of what the predecessor could do."
    reason: "DOUBTFUL — Conditional (when the factory-development path is in the predecessor's prior capability set): preserving that path follows from scope-indexed non-regression. — Non-regression is enforced through thresholds on declared dimensions, not on the idealised capability set. In an ordinary setup, those thresholds cover production tasks, such as passing coding benchmarks, and have none for the factory-development path. A successor that removes its retrospective or rule-revision loop then passes the declared relation. Preservation follows only from an idealised prior scope or from a relation that explicitly declares a factory-development dimension. It does not follow from the relation as operated. — LOCAL: state that preservation follows only when the declared non-regression thresholds include the factory-development path. — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated, universal: the predecessor state stays available for measurement when the comparison is run, as a snapshot or reconstructable state. — In the measurement-over-snapshots route, the process is continuous and the factory keeps changing. External parts such as hosted model versions, tool releases and dependency updates also change underneath it. If the predecessor was not captured when the comparison was declared, non-regression on its prior scope cannot be measured later; it can only be inferred from old logs taken under different conditions. Vendor-side model updates are a common case where the 'predecessor' cannot be re-run. — LOCAL: require the predecessor to be snapshotted or its prior-scope results recorded when the comparison is declared. — instance"
  - scope: passage
    quotes:
      - "that link is established by manipulating it — supplying versus withholding the predecessor's retained state — not by observing that the successor scored higher"
    reason: "DOUBTFUL — Universal as phrased: the experience link is established by manipulating it (supply versus withhold), not by observation. — The contrast is with observing a higher score, which is correct. But the sentence reads as if manipulation were the only route. In software factories, provenance tracing (logs showing that a specific retained note or test was loaded and changed the edit that carries the gain) is ordinary observational mechanistic evidence for the link, without an ablation run. It is weaker than a contrast but not nothing. This premise is peripheral to the central commitment and sits in the attribution section. — LOCAL: narrow to 'not by observing a higher score alone' or name manipulation as the identifying test. — instance"
  - scope: passage
    quotes:
      - "Without antecedence the claim is close to unfalsifiable, because a successor that differs at all differs favourably on some dimension available to be named after the fact."
    reason: "HOLDS — Hedged ('close to'): without an antecedent relation, post-hoc dimension choice makes the claim nearly unfalsifiable. — The obvious counterexample is an independently fixed retrospective criterion that can still fail. The note already prices this in Scope ('An independently supplied retrospective criterion can ground a legitimate improvement claim, just not this audit-proof one'). A hunt for an ordinary unpriced case, where choice of dimension after the fact cannot rescue a changed successor, found none."
  - scope: passage
    quotes:
      - "Retention has no quality requirement: a retained change can degrade the factory as easily as improve it."
    reason: "HOLDS — Universal: experience-responsive retention, as defined, makes no quality requirement, so improvement needs its own claim. — It follows from the linked occurrence definition. Retained regressions such as a bad rule kept after a misread failure are ordinary, and no case was found where retention entails improvement."
  - scope: passage
    quotes:
      - "Judgment that controls installation does, because an admission decision determines what the factory retains."
    reason: "HOLDS — Universal: an evaluation that gates installation is on the causal path of what the factory retains. — This is true by construction of 'gates'. A hunt for an admission judgment that does not affect retention found only rubber-stamp gates that never reject. Those still sit on the path counterfactually."
  - scope: passage
    quotes:
      - "The two-component relation — non-regression plus a named target — is the shape this framework declares, not the only declarable one."
    reason: "HOLDS — Fenced as this framework's declared shape: the relation is non-regression on prior scope plus exceeding a named target. — Deliberate retirement of unsafe or obsolete capability is the counterexample to required non-regression. The note marks this as a priced exception in its own Scope, so it does not dent the premise at its stated modality."
outcome: report
---

# Premise decomposition: A better-factory claim compares operative states under an antecedent assessment relation

**Register:** claim
**Central commitment (one sentence):** A better-factory claim is determinate and auditable only when it compares the predecessor with the operative successor state (not a candidate). The comparison must use a relation declared before the development, made of non-regression on the predecessor's prior scope plus exceeding a named target. The evaluator's location must be declared separately from the learner boundary.

## Premises and counterexamples

The commitment rests on three groups of premises.

**Relata.** Improvement is a separate claim from retention. The compared endpoints are operative states, and the predecessor can still be measured when the comparison runs. That last premise is unstated.

**Relation.** Antecedence is what makes the claim falsifiable. Scope indexing makes non-regression determinate. Declaring dimensions and thresholds is enough to settle pass or fail. The instruments that apply the relation sit outside what the successor can change. The last two premises are unstated. The preserved factory-development path is presented as a consequence of this group.

**Evaluator.** Admission judgments are on the causal path; measurement judgments are not. The attribution section also consumes a premise about how the experience link is established.

The relation group carries the weight. The note says the four declarations "make a better-factory claim determinate". The doubtful premises there are the unstated ones: drifting instruments, stochastic measurement, a predecessor that cannot be re-run, and a prior scope that is only a sample. Each leaves room for after-the-fact choice even though the relation was declared antecedently. None defeats the commitment. Each is repaired by adding a condition to the declared relation, so all are LOCAL. The preserved-path section is doubtful for a related reason: it reasons from the idealised prior capability set, not from the declared thresholds that actually enforce non-regression. The evaluator-location premise is dented by anticipatory influence: a known antecedent measure shapes development without gating it. The premises the note already fences in its Scope (retrospective criteria, capability retirement, route-as-reading) hold at their stated modality.

## For the human

Look first at the unstated premise that the measuring instruments are fixed outside the compared states. The note lets the successor improve its own tests and evaluators, and no declaration stops that from hollowing out the antecedent non-regression check.
