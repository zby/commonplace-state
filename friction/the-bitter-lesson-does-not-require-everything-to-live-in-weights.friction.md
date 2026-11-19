# Friction check: The Bitter Lesson does not require everything to live in weights

**Note:** kb/articles/the-bitter-lesson-does-not-require-everything-to-live-in-weights.md
**Central claim (one sentence):** Sutton's Bitter Lesson selects against directly protected human knowledge as a production method, but it does not entail that all learned or retained behavior-shaping content must be encoded in model weights rather than in localized natural-language, symbolic, or mixed artifacts.

## Filter
**Verdict:** SURVIVES

The claim commits to one consistent distinction: production method and representational form are separable axes, even though they interact in scaling behavior. The article does not require learned localized artifacts to beat weight-based learning; it only requires that Sutton's historical pattern not be overread as a weights-only mandate. That narrower claim can coexist with the article's concessions that localized artifacts still need credit assignment, evaluation, maintenance, and decomposition-revision machinery.

## Signal — thinnest joints
1. **"That distinction is categorical: it does not show whether learned natural-language or symbolic artifacts are competitive at scale, or whether a mixed system is best."** — THIN — The examples establish that representation and production method can vary independently in constructed pairs, but the conclusion moves from conceptual separability to Sutton-interpretation relevance. The missing step is why Sutton's historical failures should be classified mainly by production method rather than by the representations those failed methods tended to use.
2. **"Existing systems already populate the lower-right cell in bounded settings."** — THIN — FunSearch and AlphaDev support the broad category of search-selected explicit artifacts, but they are very different from long-lived prompts, skills, harnesses, and KB artifacts. The reason establishes existence of some learned localized artifacts, not yet that the lower-right cell is populated in the sense most relevant to agent knowledge infrastructure.
3. **"Parametric learning therefore has a default update mechanism that artifact learning lacks."** — HOLDS — The preceding contrast between gradient-based update assignment inside a fixed differentiable graph and heterogeneous artifact repositories supports the conclusion. The joint is still somewhat compressed because backpropagation's limits are acknowledged but not compared against the partial substitutes with equal precision.
4. **"The useful comparison is what can change, what accepts an update, and what designers still supply."** — HOLDS — This follows from the article's two-axis framing plus the concern that fixed decompositions can hide designer commitments. The inference is supported because those three questions operationalize production method, acceptance rule, and residual direct specification.
5. **"The Bitter Lesson sets the research program rather than deciding its outcome"** — HOLDS — The article has repeatedly narrowed its claim to an open scaling test and has named conditions under which localized artifact learning would fail. The concluding inference is earned, assuming the reader accepts the earlier separation between Sutton's production-method lesson and weights-only extrapolation.

## For the human
Look first at the bridge from "production method and representational form are categorically separable" to "Sutton's lesson should be read as selecting production methods, not representational forms"; that is where the article most needs the author's missing concretization.
