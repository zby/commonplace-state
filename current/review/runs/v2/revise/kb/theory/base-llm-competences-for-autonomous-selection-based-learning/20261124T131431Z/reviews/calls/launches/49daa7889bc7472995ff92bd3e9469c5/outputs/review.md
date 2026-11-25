---
type: types/review-result.md
findings:
  - scope: document
    quotes: []
    reason: "DOUBTFUL — Unstated premise, read as universal within the note's working-hypothesis frame: the three listed competences exhaust what must remain on the base model once harness code takes the mechanical work. — The note's own cited evidence points to a floor outside the list. In the linked Harness Evolution Hits a Ceiling ingest, a separate proposer model (Kimi K3) read the evidence package and proposed every harness edit for all lines. The weak Qwen lines therefore had diagnosis and candidate synthesis supplied from outside. They still produced no held-out gains, and the ingest reads the ceiling as plan quality (F4), confounded with general model weakness. What bound was the acting model's object-level task competence: producing an adequate plan. None of competences 1-3 names that, unless competence 1 ('let them govern its behavior') is stretched to cover doing the task well. Adding an object-level task competence, or saying explicitly that competence 1 includes it, keeps the split's mechanism. — LOCAL — instance"
  - scope: passage
    quotes:
      - "three irreducible semantic competences remain on the frozen base LLM"
    reason: "DOUBTFUL — The premise, stated as a working hypothesis, is that semantic work harness code cannot absorb has to sit on the frozen base LLM. — The linked semantic-work note says a meaning-dependent judgment can be placed on a different processor, not only that it cannot be eliminated. Being irreducible to code does not fix where the judgment runs. The cited harness-evolution loop gives a concrete instance: competences 2 and 3 ran on a proposer model, and competence 1 ran on a different acting model. In multi-model loops the floor is spread across components, and each component has a different threshold. Restating the location as 'on some model in the loop' and asking which competence binds on which model keeps the claim. — LOCAL — instance"
  - scope: passage
    quotes:
      - "Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning."
    reason: "DOUBTFUL — Necessity, stated as a proposal: a loop cannot run autonomously unless the base model clears all three competences. — Selection-based loops can run autonomously and gain without causal diagnosis. The cited harness-evolution loop is described in its ingest as 'variant-and-select with a bare failure signal'. It had no formulated diagnosis, and its 4B and 9B lines still produced held-out gains. That loop ran on a fixed benchmark, not in the open-ended setting the note specifies, so the counterexample dents the premise but does not defeat it. The revision is to say what the competences are necessary for: escaping variant-and-select plateaus, or handling novel failure modes, rather than operation as such. That keeps the mechanism. — LOCAL — instance"
  - scope: passage
    quotes:
      - "reduces to competences 2 and 3 applied to the store and its criteria"
    reason: "DOUBTFUL — The premise is that store-level semantic maintenance and criterion revision need no competence beyond 2 and 3. — Competence 2 is defined as triggered by a failure: turning 'an unanticipated failure and its trace' into a diagnosis. Some of the maintenance the note assigns to it has no triggering failure. Examples are noticing a latent conflict between two prose rules before either misfires, refactoring rules into a cleaner abstraction, and inducing a reusable procedure from successful episodes. These need abstraction and generalization over the store, not failure diagnosis. Either competence 2 widens to cover failure-free synthesis and abstraction, or a store-level abstraction competence is added. Both preserve the split. — LOCAL — instance"
  - scope: passage
    quotes:
      - "routing and loading the relevant artifacts"
    reason: "DOUBTFUL — The premise is that context assembly, including choosing the relevant artifacts, is mechanical work harness code can take over. — Deciding which store entries are relevant to a new situation is a meaning-dependent judgment. Rule-based routing works only where a pre-existing signal (a path, a type, a tag) already encodes that relevance, and the linked semantic-work note says so. In the open-ended setting the note specifies, novel situations lack such signals, so relevance selection falls back to a model. The same holds for 'flagging rising failure rates', which presupposes semantic failure labels. The fix is to restrict the harness column to routing over signals that already exist and to place novel relevance judgment under a competence, most plausibly 1 or 3. — LOCAL — instance"
  - scope: passage
    quotes:
      - "people temporarily supply the missing semantic step while transfer tests check each kind of decision on its own"
    reason: "DOUBTFUL — The premise, a possibility claim, is that the competences can be tested and supplied separately, so the binding one can be identified. — Competences 2 and 3 are exercised through competence 1. Diagnosing a trace or weighing commitments means reading unformalized text and acting on it, so a test of diagnosis also exercises interpretation. A failed transfer test may come from the prerequisite competence rather than the one under test. Shared general capability also confounds them: in the cited source the weakest models failed together. Separation stays possible with tests that hold competence 1 fixed, for example by supplying a human-verified reading, but the note should state that design condition. — LOCAL — instance"
  - scope: passage
    quotes:
      - "In open-ended work where new failure modes, commitments, and remedies keep arriving"
    reason: "HOLDS — The premise, conditioned on open-ended work, is that the semantic residue cannot be codified away in advance. — The hunt looked for codification that covers future cases. The semantic-work note's informational invariant says reliable output about a case needs upstream access to the case or its regularity. Under a stream of genuinely new failure modes, that regularity has not been paid for upstream, so the judgment falls due at use-time. No defeater was found within the stated condition."
  - scope: passage
    quotes:
      - "the frozen model does not need to keep track of budgets, traces, or regression suites in its head"
    reason: "HOLDS — The premise is that budgets, trace records, regression suites, validators, schemas and rollbacks can be enforced by code rather than held by the model. — These are explicit state and specified transitions, the scope where the linked scheduler-LLM separation note places code enforcement. The hunt considered tool code that an LLM writes with bugs. That cost moves to building and testing the tools, which the note already assigns to competence 2. It does not reinstate per-use tracking by the model."
outcome: report
---

# Premise decomposition: Harness code may offload much of a selection loop, leaving three base LLM competences

**Register:** claim
**Central commitment (one sentence):** In open-ended, fixed-weight selection-based learning, harness code can take over enforcement, evidence capture and store bookkeeping, and three semantic competences remain on the frozen base LLM as necessary conditions for running the loop autonomously: interpreting unformalized text into action, diagnosing and synthesizing remedies, and judging unformalized trade-offs.

## Premises and counterexamples

The commitment has two halves, and each consumes different premises.

The offloading half needs two things. Harness code must reliably do the jobs listed for it. Code built by the model itself must not bring per-use tracking back onto the model. The bookkeeping and enforcement items survive. Relevance-based routing and failure labelling do not, because they hide semantic work inside the harness column.

The residue half needs four things:

- What harness code cannot absorb is truly irreducible in open-ended work. This holds.
- The residue sits on the base LLM specifically.
- The three listed competences exhaust the residue, including store maintenance and criterion revision.
- They are necessary for autonomous operation.

The bootstrap claim adds a measurement premise: the competences can be isolated in tests.

The unstated premises carry the most weight. The note never argues that the list is exhaustive or that the residue's location is the base model; it assumes both. The only cited evidence turns out to be a loop in which a separate proposer model supplied diagnosis. In that loop the weak acting models were blocked by object-level task quality, which is a floor the list does not name.

None of the dents is global. Each can be repaired by:

- adding or widening a competence;
- relocating the residue to "some model in the loop";
- narrowing what necessity is claimed for;
- narrowing the harness column.

These repairs leave the mechanism intact: semantic residue that code cannot absorb, split into separable competences.

## For the human

Look first at exhaustiveness. The cited harness-evolution evidence shows a floor in the acting model's task competence while a separate proposer supplied diagnosis, so it argues for a missing competence and for the residue being spread across models rather than sitting on one base LLM.
