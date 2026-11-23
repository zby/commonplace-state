---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "The loop itself is not new."
    reason: "The contract asks that each material qualification be stated once. The previous paragraph already says 'The process itself is not new' and gives the handbook and PRODIGY precedents. Repeating the same limit at the start of the bet paragraph does no new work. The later section opener ('If selection-based learning over readable stores is not new') then works as a transition, so the middle repetition is the one to cut."
    level: warn
  - scope: passage
    quotes:
      - "Legible prose can diverge from what actually steers the model's outputs"
    reason: "The faithfulness limit is already stated with its mechanism and link in the costs paragraph ('legibility does not guarantee faithfulness ... can send repair to the wrong rule'). The hazard list repeats it without changing the claim. The contract's review test asks whether each qualification does new work. Either point this bullet to the earlier statement and add what is new here (masking the cause of gains as well as losses), or drop the earlier treatment and keep this one."
    level: warn
  - scope: passage
    quotes:
      - "represents the hard-oracle extreme"
    reason: "'Hard-oracle' is undefined for a reader with no KB context, and the article does not use it again. The next sentences explain the mechanism literally: admission only through a formal proof. Plainer wording such as 'represents the extreme where only a formal proof can admit a change' loses nothing, so the prose-register test requires the replacement."
    level: warn
  - scope: passage
    quotes:
      - "The three precedents raise the same question"
    reason: "At this point the reader has not yet been told which three precedents are meant. The section then presents four bolded items, and the fourth, robust comparison, is the article's own proposal, not a precedent. A plain forward reference would make the transition explicit, for example 'The three precedents below (formal proof, a fixed formula, and changing heuristics)'."
    level: info
  - scope: passage
    quotes:
      - "Even consistent answers can neglect a cost the stated purpose requires"
    reason: "This sentence relies on consistency before the next paragraph introduces it as part of the bet ('Consistency is part of the bet'). Moving it after that paragraph, or merging the two, would keep the causal order explicit."
    level: info
outcome: warn
---

# Review

## Placement and lifecycle

The article belongs in `kb/articles/`. It is an outward-facing explanation of a paradigm claim and an empirical bet. It links into the theory notes that carry the transferable claims, so it does not duplicate them. It is a `draft` at the collection root. It opens with an authored blockquote banner that says the claims and structure may change and names GitHub Discussions as the place to send comments. The banner promises no stability. The title is a reader-facing headline, not a claim title. The description works as an agent retrieval filter, and the opening paragraphs act as the reader's abstract.

## Linking and reader-only body

The body has no footer link tables, visible relation labels or graph-traversal glosses. In-prose links go only to authorized destinations: `kb/theory/` for definitions and arguments, `kb/sources/` for externally attributed claims (AlphaZero, PRODIGY, EURISKO, Greco et al., the harness-evolution study), and `kb/articles/` for companion articles. External links cover primary attribution: the AlphaGo Zero paper, Sutton's essay and the interview. Nothing points into `kb/work/` or into non-retained reports. The closing "Where to go next" section gives the onward path the quality goal asks for.

## Explanatory tests

A technical reader can state the two main claims, how they are supported and their material limits. The two claims are that selection needs a comparison, not a single score, and the bet that a fixed-weight LLM can build the preference model and make the robust comparison. The article gives no completed end-to-end run, five named hazards and an explicit failure condition. The routing-line example comes before the abstraction. "That sequence establishes three things" turns the example into general claims, and the robust-comparison and evidence sections return to the example. The gradient-training table, the precedent sequence and the Bitter Lesson section each advance the argument.

## Unmet conventions

Most of the gaps fall under the contract's rule against repeating qualifications. The "not new" limit appears three times near the top, and the middle instance adds nothing. The faithfulness limit is stated in full twice. One unexplained elevated term, "hard-oracle extreme", has a plain literal replacement available. Two smaller ordering issues are recorded as info: "the three precedents" is referenced before they are introduced, and consistency is relied on one paragraph before it is introduced. None of these issues affects placement or makes the article's conformance systematically fail, so the outcome is WARN.
