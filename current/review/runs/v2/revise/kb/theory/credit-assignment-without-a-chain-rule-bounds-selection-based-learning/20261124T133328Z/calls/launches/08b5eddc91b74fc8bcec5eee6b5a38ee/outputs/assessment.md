# Assessment: credit assignment without a chain rule is a debugging problem

**Proposed purpose (no operator purpose was given):** A reader of the
continual-learning article, or an agent designing a selection-based learner,
should come away understanding why credit assignment over a retained store is
a debugging problem rather than a gradient problem, which three properties make
a prose-and-code store harder to debug than software, and which levers keep it
debuggable, without being told those levers are stronger than they are.

## What reads well

The three-property list is the note's strongest part: it names the obstacle as
weakened debugging tools (softer traces, implicit coupling, noisier failures)
rather than missing gradients, and the dependent article relies on exactly that
framing.

## Sentence a hostile reviewer attacks first

"[Near-decomposability] and explicit dependency links bound how many artifacts
can interact." The note's own implicit-coupling bullet says prose conventions
interact "without any explicit link in the store", so declared links cannot
bound that interaction. Four stored findings and all three depth 1 reports
attack this sentence.

## Ranked changes

The highest-value changes against the purpose are claim corrections. The passes
cannot make them, so they are under *Claim questions for the operator* below.
The thesis and the argument's structure stand, and each correction is a
sentence-level sharpening, so the run does not stop. The passes are scoped away
from those passages.

1. **Make the addressable-theory lever match its source.** "A failed prediction
   names a specific premise to check" claims single-premise localization. The
   linked definition says a located part is a candidate and that a failure rarely
   identifies one faulty commitment. Rewording to "narrows the suspects to the
   premises behind that prediction" keeps the mechanism. Cost: one clause.
   Pass: `fix-strategy-taxonomy` on the grounding-alignment finding, scoped to
   that sentence only. (The finding's other quote, about dependency links, is a
   claim question and is out of scope.)
2. **Gloss or replace two terms.** On first mention, "selection-based learning"
   has a link but no gloss, although it is registered vocabulary. "Accretion
   plateau" is a coined label that the linked note does not use, and three
   findings flag it at info level. A short inline gloss for the first and
   ordinary words for the second ("store bloat that stops helping and starts
   degrading use") would let the reader follow without opening links.
   Cost: two phrases, decided per item. Pass: `abstractions`, scoped to the
   opening's first two sentences up to "far less scalable than gradient
   learning", and to the clause containing "accretion plateau". The
   near-decomposability gloss sits in the sentence with an open claim question
   and is excluded.
3. **Fold the first Scope bullet into the body.** The bullet repeats the second
   paragraph's condition. Its only new content is the flat-lookup-table boundary
   case, which can become the concrete instance of "a few isolated rules".
   Keep the second Scope bullet, which separates store attribution from
   interpretability. Cost: one sentence moved, one bullet cut. Pass:
   `readability-and-flow`, scoped to the second paragraph and the Scope section.

Not recommended: `plain-wording` (the prose is already plain; the one depth 5
finding is a claim question), `opening-and-title` (the opening carries an open
claim question; the H1 is sound), `narrow-overclaims` (every overclaim it would
touch is held for the operator below), and `split-out-a-treatment`.

## Overclaims: support or divergence

- "credit assignment without a chain rule is a debugging problem over an
  interdependent store": **divergence**, the thesis. Keep.
- "What makes a mixed prose-and-code store harder to debug than ordinary
  software is not the lack of gradients, but three properties that weaken
  ordinary debugging tools": **divergence**. The dependent article's open
  question rests on it. Keep.
- "its credit assignment is far less scalable than gradient learning":
  **divergence**. The article relies on it, and the closing sentence names the
  comparison basis. Keep.
- "Yet that does not block full automation" / "routinely localize faults":
  **support**, may be narrowed. See claim question 3.
- "explicit dependency links bound how many artifacts can interact": **support**,
  may be narrowed. See claim question 1.
- "verifies causal responsibility directly": **support**, may be narrowed. See
  claim question 2.
- "a failed prediction names a specific premise to check": **support**. Narrowed
  by the `fix-strategy-taxonomy` entry.

## Claim questions for the operator

1. **Dependency links cannot bound implicit coupling (defect).** Passage:
   "[Near-decomposability] and explicit dependency links bound how many
   artifacts can interact." The two statements that cannot both hold are this
   one and "Prose conventions can interact semantically across unrelated tasks
   without any explicit link in the store." The sentence also has two readings
   that lead to different interventions: links enforced as a loading or
   dependency restriction, or links that only record declared dependencies and
   tell a debugger where to look. The linked near-decomposability note is
   conjectural ("may make local inspection affordable") and claims no bound on
   the interacting set. Suggested correction: make the sentence conditional and
   limit it to declared dependencies, for example "Near-decomposability, where it
   holds, and explicit dependency links narrow where to look for declared
   interactions; implicit coupling stays outside them." Sources:
   `.../results/.../semantic/internal-consistency.md`,
   `.../semantic/underspecified-assertions.md`,
   `.../semantic/grounding-alignment.md`, `.../semantic/epistemic-status-blur.md`;
   reports `kb/instructions/composition-friction-gate.md`,
   `kb/instructions/critique-note.md` and
   `kb/instructions/premise-decomposition-gate.md` under the same results
   directory. No dependent relies on this lever (role report, run directory
   `.../20261124T133328Z/role`).
2. **One replay does not verify causation under noisy failures (defect).**
   Passage: "Replaying the failing case with a shortlisted entry withheld or
   modified verifies causal responsibility directly." Case: a quiet degradation
   under stochastic decoding, which the note's own third property names. A
   single withheld-entry replay neither confirms nor refutes it, and
   withholding one entry at a time misses a cause that needs a "combination of
   edits", which the note itself allows. Suggested correction: "verifies causal
   responsibility, with repeated replays where failures are noisy." Reports:
   `critique-note.md`, `composition-friction-gate.md`,
   `premise-decomposition-gate.md`. No dependent relies on it.
3. **The opening's strength drifts from the close, and the coding-agent premise
   is unsupported (defect, two readings).** Passages: "Yet that does not block
   full automation: … engineers and coding agents routinely localize faults
   across hundreds of interdependent modules" against "it gives a plausible path
   to fully automated credit assignment" and the second open question. Reading A:
   the missing chain rule is not itself the blocker. Reading B: full automation
   is established. The note supports A, but the opening's register reads as B.
   "Coding agents routinely" also has no source, and agents usually start from a
   supplied failing test. Suggested correction: hedge the agent half ("and
   coding agents increasingly do so, usually starting from a failing test"), and
   state the debuggability condition in the opening at the close's strength.
   The dependent `kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md`
   relies on "coding agents already automate much of that debugging". A hedge of
   this kind leaves that intact, but the operator should check the article's
   wording when deciding. Findings: `.../prose/orphan-references.md`,
   `.../semantic/epistemic-status-blur.md`, `.../semantic/internal-consistency.md`
   (info); synthesis opportunity 1 (run directory `.../20261124T133328Z/synthesis`).
4. **Misattributed cause in the workarounds paragraph (defect).** Passage:
   "Because of those three differences, naive workarounds still break down at
   scale." Exhaustive ablation fails because of cost at scale, and appended
   exceptions fail through coupling and bloat. Both would fail in ordinary code
   too, so the connective names the wrong cause. Suggested correction: "At
   scale, naive workarounds break down." Finding:
   `.../sentence/framing-mismatch.md`; report `composition-friction-gate.md`.
5. **File name no longer matches the title (stale qualification).** The file is
   `credit-assignment-without-a-chain-rule-bounds-selection-based-learning.md`,
   but the H1 now claims the problem "is a debugging problem over an
   interdependent store". The renaming falls outside `repair-claim-title`. A
   relocation would need the article's link updated, as a separate
   `commonplace-relocate-*` commit.
6. **Pair each remedy with the property it answers (choice, no defect shown).**
   Synthesis opportunity 2, with the friction report's "for each remedy, say
   which of the three obstacles it answers". This restructures the closing
   paragraph. It is not ranked first because claim questions 1 and 2 must be
   settled before a pairing can be written honestly. The operator may decline
   it. Source: `.../20261124T133328Z/synthesis`.

## Findings and proposals not acted on

- `accessibility/undefined-terms`: the near-decomposability gloss is not
  planned, because it sits in claim question 1's sentence. The "addressable
  theory" item is info-level and its clause already conveys the idea.
- `semantic/grounding-alignment`, the near-decomposability quote: held as claim
  question 1. The info items (rationale faithfulness transfer, "accretion
  plateau" label) are left to the abstractions entry or not acted on; the
  faithfulness transfer is plausible as stated.
- `semantic/epistemic-status-blur`, the info item on "far less scalable": the
  closing sentence already names the comparison basis, and the article relies
  on the sentence.
- `semantic/underspecified-assertions`, the info item on "accretion plateau":
  covered by the abstractions entry.
- Critique: scope credit assignment to failure attribution and name positive or
  graded credit as a separate problem. **Extension.** The second Scope bullet
  and the description already restrict the note to attributing failures. Naming
  graded credit as excluded would be a useful addition, but the purpose does not
  require it.
- Critique and premise decomposition: name a crisp failure oracle or detection
  fixtures as a precondition. **Extension.**
- Premise decomposition: omission faults (missing or unretrieved entries) and
  base-model errors that no store entry causes. **Extension.**
- Premise decomposition: an always-loaded core blunts trace narrowing.
  **Extension**, a boundary condition the claim as scoped does not need.
- Premise decomposition: delta debugging makes ablation cheaper. **Extension.**
  The sentence is about *exhaustive* one-by-one ablation, which stays
  expensive.
- Critique: sample cost of counterfactual estimation as the real bottleneck.
  The part that bears on replay is claim question 2. The rest is an extension.
- Role report, DUPLICATED with the article: no action. The report judges both
  versions fit for their readers.
