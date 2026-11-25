purpose: "For agents and maintainers designing a fixed-weight selection-based learning loop: see which loop functions harness code can take over, which three semantic competences the frozen base LLM must still supply, and that this split is a revisable working hypothesis."
must-keep:
  - "Harness code can take over much of the loop's machinery: enforcement and context assembly, evidence capture and replay, and store bookkeeping."
  - "Three semantic competences remain on the frozen base LLM: interpreting unformalized text into action; diagnosing novel failures and synthesizing candidates across text and code; judging unformalized trade-offs and recognizing missing evidence."
  - "Clearing these competences is proposed as necessary for operating the loop autonomously, not sufficient for sustained continual learning."
  - "Store-level maintenance and criterion revision do not require a separate model competence."
passes: []
stop: >-
  Stop before any pass, on two grounds.
  (1) A dependent relies on the claim that most needs changing. Defect (two readings), from
  kb/workflow-state/data/current/review/results/kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md/kb/instructions/critique-note.md
  and
  kb/workflow-state/data/current/review/results/kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md/kb/instructions/premise-decomposition-gate.md:
  the Harness Evolution paragraph offers a "base-model floor" as an illustration for the three loop competences. In the cited
  paper, however, a frontier proposer (Kimi K3) did the diagnosing and proposing, and the weak models only executed tasks.
  Under one reading the evidence misdescribes the source. Under the other, the floor is an executor's task-capability floor
  outside the three competences. The ingest also retains no quotes (semantic/grounding-alignment fail). Recasting or dropping
  the paragraph changes the sense of the "base-model floor" that
  kb/articles/continual-learning-with-fixed-model-weights-llm-selected-updates.md relies on for its below-floor sentence (role
  report: kb/workflow-state/data/current/review/runs/v2/revise/kb/theory/base-llm-competences-for-autonomous-selection-based-learning/20261124T131431Z/role).
  The operator must decide the article's change too.
  (2) Further claim defects, each fixable in a sentence or two, together cover nearly every paragraph, so passes scoped away
  from them would edit only text the corrections will rewrite:
  "irreducible ... remain on the frozen base LLM" conflicts with the Scope revision rule and goes beyond the relocation note,
  which allows another processor (critique-note, composition-friction-gate, premise-decomposition-gate);
  the independence claim "These three competences can fail independently and sit at different capability thresholds." is
  unhedged (critique-note; semantic/epistemic-status-blur);
  the criterion-revision reduction to competences 2 and 3 conflicts with competence 3 judging "against stated commitments"
  (critique-note, composition-friction-gate, premise-decomposition-gate);
  relevance routing is placed on the harness side although it depends on meaning (semantic/completeness-boundary-cases);
  and the threshold for "clearing" is undefined (semantic/underspecified-assertions).
  Route: commonplace-revise rewrite kb/theory/base-llm-competences-for-autonomous-selection-based-learning.md --commission FILE,
  with the commission prepared with cp-skill-write-multistage, covering the dependent article's floor sentence. After that,
  rerun the quick procedure for the deferred readability, gloss and description findings listed in the assessment.
