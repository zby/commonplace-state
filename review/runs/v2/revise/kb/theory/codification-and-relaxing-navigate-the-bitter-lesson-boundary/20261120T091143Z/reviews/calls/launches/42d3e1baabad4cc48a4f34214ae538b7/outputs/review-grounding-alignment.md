---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - 'distribution shift, paraphrase brittleness, and isolation-vs-integration gaps reveal when a codified component encodes an accident rather than a spec'
    reason: 'The linked relaxing-signals note says its signals "shift confidence — they detect badly-fitting theories, not the theory/spec distinction itself, since a well-regularised learned component can pass all five early signals yet still encode a proxy theory." The note cites it as showing that these signals "reveal" an accident-vs-spec status, which is stronger than and partly contrary to the target''s stated scope.'
    level: warn
  - scope: passage
    quotes:
      - 'This means codification bets in the arithmetic regime are not merely safe-for-now; the step-by-step structure that codification encodes is the kind of regularity that persists under scaling'
    reason: 'Ebrahimi et al. is linked directly to arXiv, outside kb/sources, with no ingest or verbatim quotation, so the reviewer could not open a retained supporting passage within the allowed reading scope. On the page, the transfer is unarticulated: a result about architectural induction bias in sequence models on calculator-class state tracking is used to ground the durability of code-extraction codification (scripts, tests, validators) across the arithmetic regime. The source setting (model architecture/supervision) and the note''s setting (committing rules to code) differ, and the note does not explain the bridge.'
    level: warn
  - scope: passage
    quotes:
      - 'High-epiplexity regularities are genuinely structural — codifying them is safer because they reflect real patterns, not artefacts of the observer''s computational budget'
    reason: 'Finzi et al. is likewise an untracked arXiv link with no quotation, so source support could not be checked. On the page, the transfer from a measure of learnable information under computational bounds to the relative safety of codifying a regularity is not articulated; the note does not say which observer''s bounds apply or why high epiplexity implies the regularity is spec rather than accident.'
    level: warn
  - scope: passage
    quotes:
      - 'separates exact specs (the spec is the problem) from proxy theories (the spec is a theory about a larger capability)'
    reason: 'The linked note attaches exactness and proxyhood to links in a named artifact–requirement–objective path, and calls artifact-level shorthand safe only when the path is named. The opening represents the distinction as two regimes a practitioner is "in", and adds that only scale tests it, whereas the target lists constitutive scope, outcome data, predictive tests, ablations and composition as evidence. Heuristic 1 later restores path relativity, so this is a modest scope shift rather than a contradiction.'
    level: info
  - scope: passage
    quotes:
      - 'one case-level conjecture offers as the diagnosis of a structured method''s loss under scaling'
    reason: 'The target states its selection criterion universally ("the criterion is claimed universally"), with case-level evidence and a historical tendency. Describing it as a "case-level conjecture" narrows its stated scope. The conjectural status the note attaches is accurate; the scope label is slightly off and non-load-bearing.'
    level: info
outcome: warn
---

# Review

## Linked library artifacts

- **Codification definition** — represented accurately: symbolic form by rewriting or adopting a governing reference; prose conventions alone are not codification; adopted model packages can codify. Pass.
- **Constraining and extraction** — the target supports codification trading generality for reliability, speed or cost under task fit; the note's qualification ("when the committed procedure fits and its execution and maintenance are cheaper") matches the target's conditions. Pass.
- **Spec mining** — the target describes watching a system and extracting regularities into deterministic artifacts; the note's use (bottom-up extraction from a working system) matches. The footer's "avoids the vision-feature failure mode" is stronger than the body's "improves the odds", but the body governs and the footer is link annotation.
- **Bitter-lesson note** — the conjectural status the note attaches is accurate; the "case-level" label is noted as INFO. Identification of this note's "accident" property with the target's unearned reach is a concept-attribution question for another gate.
- **Fixed-artifact distinction** — modest path-relativity flattening, INFO.
- **Relaxing signals** — overstated as revealing the spec/accident status; the target explicitly disclaims that. WARN.
- **Verifiability gradient** — footer-only, adjacent. Pass.

## External sources

Both papers are linked directly to arXiv with no tracked ingest and no verbatim quotation. Under this invocation's reading scope and no-delegation rule, the reviewer could not retrieve their supporting passages, so source-level support is unverified. Independently of the sources' content, each use relies on a transfer from the paper's setting to code-extraction codification that the note does not articulate. That is enough for WARN. A reviewer with the source text should check whether either paper speaks to codification at all.
