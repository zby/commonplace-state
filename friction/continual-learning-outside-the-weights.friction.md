# Friction check: Continual learning outside the weights

**Note:** `kb/articles/continual-learning-outside-the-weights.md`
**Central claim (one sentence):** For deployments whose failures and needed revisions can be stated at the level of describable events, continual learning can occur outside model weights through a frozen interpreter over a governed, revisable artifact layer.

## Filter
**Verdict:** SURVIVES

The claim wants several things to hold at once: the deployed model weights stay fixed; the system still genuinely learns from its own experience; the learning can include concept maintenance and coherence work; and Sutton and Javed remain right below the level of describable, criticizable content. Those properties can coexist once the claim is read in the article's narrowed scope: the article is not claiming weight-free feature formation in general, only a second substrate for governable, addressable revisions.

## Signal — thinnest joints
1. **"Sutton and Javed's stated criterion for learning is that the weights change. This article uses a functional one ... because that is the criterion the big-world premise motivates"** — UNSUPPORTED — The big-world premise establishes that a deployed system must keep revising its approximations, but it does not by itself justify replacing a substrate-specific definition of learning with a functional one. The article needs an argument that the premise is neutral over substrates, not just compatible with that reading.
2. **"When this project needed a concept it did not have ... it wrote a definition ... That is concept maintenance continued after the weights froze"** — THIN — The examples show explicit retention, naming, and revision of concepts by the human-agent composite, but Sutton and Javed's target is formation of new abstractions by the learning substrate itself. The article partly concedes this later, which leaves the earlier inference overstated.
3. **"Every claim is addressable, so it can be criticized one at a time ... What keeps the knowledge correct is explicit."** — THIN — The mechanisms support local criticism and revision, but Sutton's question is about what keeps the whole knowledge system coherent over time. The article itself immediately admits missing whole-system contradiction checks, drift measurement, and artifact-selection logic after failures, so the stated reason only partly establishes the conclusion.
4. **"A trained model can apply a natural-language theory to a case with a judgment no rubric formulates ... If that is right, the product of weight learning ... can be held fixed, and what it consumes can carry the continued learning."** — THIN — Even if a fixed model can competently apply retained theory, that shows interpretive competence, not that revising the artifact layer constitutes continued learning in the contested sense. The bridge from "can read and apply" to "this is a learning substrate" is asserted rather than demonstrated here.
5. **"The artifact-only variant should recover from shifts that preserve a structure the retained theory names, using fewer target observations and less collateral change"** — UNSUPPORTED — This is a concrete comparative prediction, but the article gives no evidence in the piece that artifact updates actually have those sample-efficiency or collateral-change properties under controlled comparison.

## For the human
Look first at the criterion shift from "learning means weight change" to "learning means experience-driven capacity change"; that redefinition carries most of the article's load and is the least-earned step.
