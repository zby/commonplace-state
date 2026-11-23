---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "A release judgment: Python 3.11 over 3.10"
      - "Three choices fix the comparison:"
    reason: "The case-study section on Python 3.11 versus 3.10 (with the library-hours example) comes immediately before 'What analysis can settle', which states the general pattern those cases instantiate: fix the alternative, who gains and who loses, and the period; investigate an unknown only if a plausible answer could reverse the choice. The specific section exemplifies that rule rather than qualifying it: whole-release choice, losses on identifiable callers, and 'test its dependencies before deciding' are instances of the three choices and the reversal test. Under the tiebreaker this is a WARN. The example-first order looks deliberate, since the intro is also built on cases. A fix could keep the cases while stating the three choices briefly before the release table, or could open the release section by saying which of the general choices it illustrates."
    level: warn
outcome: warn
---

# Review

The body has four sections after the introduction:

1. "A release judgment: Python 3.11 over 3.10": specific, with proper nouns, version numbers and a hypothetical library case.
2. "What analysis can settle": general. It covers the limits of analysis, the three choices that fix a comparison, and the rule for investigating an unknown.
3. "What Commonplace chooses to count": specific to Commonplace's objective.
4. "What to do with an incomplete comparison": procedural guidance illustrated with Commonplace cases.

Pair 1→2 fits the failure mode. Section 1 presents instances, and section 2 then states the rule they illustrate. The release section does not challenge or limit that rule. Its points about whole-release alternatives, distributed losses and testing a dependency before acting are the rule applied. That makes it exemplifying, so the result is WARN rather than INFO.

Pair 2→3 runs from general to specific, which is the order the gate expects.

Pair 3→4 is not a specific-then-general inversion. Section 4 does not state a general pattern that Commonplace's chosen objective exemplifies. Instead, it applies the objective and the earlier rules to Commonplace examples.
