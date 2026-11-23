---
type: types/review-result.md
findings:
  - scope: passage
    quotes: ["It requires governing durable changes to future behaviour: selecting a candidate update, validating it, and deciding how it enters the behaviour-determining system."]
    reason: "The opening states that continual learning requires governed writes, but mature release engineering also governs writes, so the reader cannot yet tell what distinguishes the claim; the distinguishing condition, that the system's own loop does the selecting, appears only late in the final paragraph. A revision could put the self-selection condition in the opening statement, so that the later maintenance contrast confirms a boundary the reader already holds instead of introducing it."
  - scope: passage
    quotes: ["The resulting problem is governance: autonomously *choosing* a behaviour-changing write"]
    reason: "The final paragraph carries seven moves: the governance task list, a form-placement aside, the release-engineering contrast, the proposal-selection discriminator, a restatement of the same contrast via the incident edit, cadence, and the subproblem scoping. The argument from governance to the continual-learning discriminator is hard to follow. A revision could move the form-placement aside into the representational-form paragraph, state the human-selection versus system-selection boundary once next to the proposal-selection criterion, and end on the scoping sentence."
  - scope: passage
    quotes: ["belongs to a consumption path, not to stored bytes"]
    reason: "The opening paragraph states its claim, then runs through the learning criterion, behavioral authority, knowledge artifact and system-definition artifact, and closes by restating its opening. It reads as terminology rather than as the premise that storage does not decide behavioural force. A revision could fold the artifact-role distinction into one clause, keep the links, and end the paragraph on the consumption-path premise rather than on the restatement."
outcome: report
---

# Simplification synthesis: Continual learning requires governing behaviour-changing writes, not just storing content

The note is compact, and its links carry most mechanisms. The gate findings that matter converge on two places: the opening paragraph, which does not yet state what separates the claim from ordinary governed software change, and the final paragraph, which carries that separation among several asides and states it twice. The defensive clauses in the form paragraph ("It need not touch all three every time", "broadening the system boundary does not remove them") are local cuts and fall below this synthesis's threshold.

## Opportunities

### 1. Surface the self-selection condition in the claim

- Location: opening paragraph, "It requires governing durable changes to future behaviour: selecting a candidate update, validating it, and deciding how it enters the behaviour-determining system."; the condition currently sits in the final paragraph, "Continual learning, as the field uses the term and as this note uses it, asks for more: the system does the selecting itself."
- Combines: core-claim-obscured (opening omits self-selection); bears on detail-overhang and marginal-value-redundancy findings on the doubled maintenance contrast, since a claim stated up front lets that contrast shrink.
- Preserve or decide: The body supports the self-selection condition, so surfacing it is a placement change, not a new claim. The title and description, however, say only "governing" and "select, validate, authorize, and coordinate" without naming who governs. The author must decide whether the note's thesis is that continual learning requires governance as such, with self-selection as the boundary that makes it *continual* learning, or that it requires the system's own loop to govern. Under the first reading, the opening clause names the boundary; under the second, the title and description may need to follow. Preserve the claim that hand-authored changes still count as learning under the broad criterion from the opening; only the "continual" label is withheld. One possible resolution: "It requires the system's own loop to govern durable changes to future behaviour: selecting…"

### 2. Untangle the final paragraph into governance plus one boundary statement

- Location: final paragraph, from "The resulting problem is governance" to the end.
- Combines: branch-bloat (form-placement aside, info); core-claim-obscured (form-placement aside, info); detail-overhang (doubled maintenance boundary, warn; form-placement aside, info); marginal-value-redundancy (incident-edit restatement, warn; cadence sentence, info).
- Preserve or decide: Moving "Form placement is itself revisable…" into the representational-form paragraph keeps its content; marginal-value-redundancy judged that it adds a dynamic the note does not otherwise state, so relocate it or reduce it to a clause rather than delete it. Merging the release-engineering and incident-edit sentences requires choosing which carrier to keep: the general release-engineering framing or the concrete incident example. Either works, but the merged sentence must keep both halves: such edits are learning by human selection, and they are not continual learning. The author must decide whether the cadence sentence states a new operational requirement or repeats paragraph 2's install-before-retraining constraint; keep it only in the first case. Keep the closing scoping sentence (storage, activation and parametric adaptation remain subproblems that governance relates), which every gate treated as load-bearing.

### 3. Fold the opening's terminology run into its premise

- Location: opening paragraph, from "This note uses the broad criterion" to "Persistence alone therefore does not create a governed behaviour-changing write."
- Combines: core-claim-obscured (definitions crowd the opening, info); marginal-value-redundancy (closing restatement, warn).
- Preserve or decide: The learning criterion must stay because the final paragraph's claim that hand-authored changes "are learning too" depends on it. The consumption-path premise — the same stored object is evidence under one path and system definition under another — is the reason persistence cannot settle behavioural force, so it must survive the fold even if the two artifact-type names become one clause. If opportunity 1 is taken, re-check that the opening still leads with the claim and not with definitions.
