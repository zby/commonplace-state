---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The claim compares two operative states of the factory under an assessment relation fixed before the development it judges."
    reason: "DOUBTFUL — Universal, as stated in the title and opening: a better-factory claim is one made under an assessment relation fixed before the development it judges. — The note's own Scope concedes that 'an independently supplied retrospective criterion can ground a legitimate improvement claim, just not this audit-proof one.' A retrospective but independently specified criterion, for example one taken from an external benchmark published after the change, then grounds a legitimate claim that the factory got better without satisfying the title's antecedence condition. Any reader can rederive this from the note's own text. It defeats the title read universally. The commitment survives only if 'better-factory claim' is read as a term of art for the audit-grade claim this framework disciplines. The opening sentence ('better means better under the declared relation') points toward that reading, but the title and the relation section ('Both are declared while only the predecessor exists') state antecedence without that restriction. The remaining doubt is whether the term is stipulative or descriptive; the counterexample itself is checkable. — GLOBAL — instance"
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated, universal: after the successor is installed, the predecessor remains measurable under conditions comparable to the successor's, so that comparing the two operative states can be carried out. — A factory state includes things the operator cannot freeze or replay: a hosted model version that the vendor deprecates, accumulated retained artifacts that later work has modified, and a production workload that drifts over time. In such cases the predecessor cannot be re-run after installation. Measuring it at declaration time instead compares it against a different workload and environment. In agent factories built on hosted models this is the ordinary situation, not an edge case. The first Open Question (baseline, measurement procedures, comparable conditions) names the gap, but the body treats the comparison as available. — LOCAL — prevalence"
  - scope: passage
    quotes:
      - "Prior declaration prevents that form of post-hoc selection."
    reason: "DOUBTFUL — Universal: declaring dimensions and thresholds before development prevents selecting requirements the successor happens to satisfy. — The relation passes when the successor improves on 'at least one named production dimension.' A declarer who names many dimensions in advance, each with a small threshold, will often see one pass by noise alone. That is the same selection effect produced entirely by prior declaration, the familiar multiple-comparisons problem. The sentence's narrow reading, which covers only choosing after seeing the result, holds. The auditability purpose it serves is dented unless the relation also bounds or corrects for the number of declared target dimensions. — LOCAL — instance"
  - scope: passage
    quotes:
      - "This framework uses the predecessor's prior capabilities as that scope."
    reason: "DOUBTFUL — Universal: the predecessor's prior capabilities form a non-regression scope that can be checked. — The description says 'declared prior capabilities', while the body says 'prior capabilities' without restriction. If the scope means every prior capability, then for an open production family it cannot be enumerated or checked, a problem the second Open Question concedes. If it means a declared subset, then a successor can lose an undeclared capability and still pass, which weakens the claim that naming the scope 'makes explicit which losses would cause the comparison to fail'. Either reading leaves a gap, and the note does not choose between them. Capability retirement is separately fenced in Scope. — LOCAL — instance"
  - scope: passage
    quotes:
      - "The compared states span the whole production environment."
    reason: "DOUBTFUL — Universal: comparing whole production environments attributes the difference to the factory. — If the compared states span the whole environment, they also include things that are not the factory's reusable machinery: the incoming task distribution and external services the factory does not control. Suppose the workload becomes easier, or an upstream API improves without any factory change. The successor then passes the declared comparison even though the factory's machinery is unchanged. The note intends to count the scheduled search-tool upgrade as factory improvement. Workload drift and external improvements are not the factory, however, and the note does not fence them out. — LOCAL — instance"
  - scope: passage
    quotes:
      - "Comparing otherwise equivalent runs with and without the retained instruction tests its contribution"
    reason: "DOUBTFUL — Universal: an ablation that runs with and without the retained change tests whether the experience-derived change contributed to the improvement. — Retention is path-dependent. Retained artifacts created later through the synonym-search instruction, such as notes found and linked through it, persist when the instruction is removed. The 'without' arm is therefore not otherwise equivalent, and the ablation underestimates indirect contribution. The reverse also occurs: if the instruction helps only in combination with a later change, a single-factor ablation misattributes the effect. The linked contrast note's principle holds, but the 'otherwise equivalent' arm is hard to construct in an accumulating factory. — LOCAL — instance"
  - scope: passage
    quotes:
      - "a retained change can degrade the factory as easily as improve it"
    reason: "DOUBTFUL — As stated, retention is symmetric with respect to quality: degradation is as likely as improvement. — The argument needs only that retention does not entail improvement, and that holds. The 'as easily' symmetry is stronger. In ordinary factories, retained changes pass adoption gates such as tests, review and evaluators, which bias retention toward non-degradation; the note itself mentions 'internal controls on what the factory retains'. The overstatement does not carry any load. Reading it as 'can degrade it as well as improve it' removes the problem. — LOCAL — prevalence"
  - scope: passage
    quotes:
      - "A candidate that is generated and discarded never enters the comparison"
    reason: "HOLDS — By the note's own terms, a candidate is not a state of the factory, so a claim that the factory got better concerns the installed state. Staging and shadow evaluations are placed correctly as evidence for adoption. The hunt for a counterexample found ordinary claims that a candidate is better than the current factory. Those are claims about a candidate, not claims that the factory improved, so they do not defeat this premise."
  - scope: passage
    quotes:
      - "holding model weights fixed does not put the comparison out of reach"
    reason: "HOLDS — Universal: changes to prompts, artifacts, code, tools, workflows or evaluators can make an operative state differ from its predecessor while the weights stay fixed. The linked unit-of-learning note supports this. No counterexample was found: any operative non-weight change yields a different compared state."
  - scope: passage
    quotes:
      - "non-regression requires the successor to preserve that capability"
    reason: "HOLDS — Conditional: if the checked scope includes an operative factory-development path, non-regression requires preserving it. This follows from the definition of non-regression over a declared scope. The note confines the consequence to that condition and, in Scope, drops it when a relation permits retirement. No counterexample was found."
outcome: report
---

# Premise decomposition: A better-factory claim compares operative states under an antecedent assessment relation

**Register:** claim
**Central commitment (one sentence):** A claim that a factory got better compares two operative states, the predecessor and the installed successor rather than a candidate or the change that produced it. The comparison uses a relation declared before development: non-regression on the predecessor's prior scope plus a declared improvement on at least one named dimension. This keeps the claim relation-relative and auditable, and keeps it distinct from retention and learning.

## Premises and counterexamples

The commitment rests on three groups of premises.

- **The relata:** candidates are excluded, and operative states can be compared. This group includes the unstated premise that the predecessor remains measurable under comparable conditions, as well as the boundary of what counts as the compared state.
- **The relation:** antecedence blocks selection, the two-component shape holds, and the non-regression scope can be checked.
- **The separation of improvement from retention and learning:** retention carries no quality requirement, and an ablation identifies contribution.

The strongest pressure is on the title's universality. The note's Scope admits retrospective improvement claims that are independently grounded, so the commitment holds only as a stipulated, audit-grade sense of "better-factory claim". The relation premises are dented by ordinary practice rather than refuted: multiple named dimensions reintroduce selection, and an ambiguous non-regression scope cannot both be checked and be exhaustive. The relata premises are weakest where factories run on hosted, drifting environments. The learning-distinction premises largely hold, though the ablation's "otherwise equivalent" arm is hard to build when retained artifacts compound.

## For the human

Look first at the title's unrestricted antecedence. The Scope bullet conceding retrospective criteria either requires the title and opening to be narrowed to "auditable" better-factory claims, or requires the note to say explicitly that "better-factory claim" is this framework's term of art.
