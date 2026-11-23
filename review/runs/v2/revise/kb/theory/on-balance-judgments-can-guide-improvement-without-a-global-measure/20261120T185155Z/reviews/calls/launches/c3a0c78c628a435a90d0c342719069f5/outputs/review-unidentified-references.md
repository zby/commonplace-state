---
type: types/review-result.md
findings:
  - scope: passage
    quotes:
      - "For Commonplace, we choose changes by asking whether they yield more useful and better-warranted knowledge work for the human judgment spent, on balance."
    reason: "Commonplace is named for the first time in a section heading and in this sentence without saying what it is. A reader who arrives without KB context cannot tell whether it is a project, a tool, an organization or a knowledge base, so the stated objective has no clear subject. Add a short inline identification, such as Commonplace, the framework for agent-operated knowledge bases that this note belongs to."
    level: warn
  - scope: passage
    quotes:
      - "one line in `AGENTS.md` reliably directs agents to instructions"
    reason: "`AGENTS.md` is not identified as the project instruction file that agent runtimes load into their prompts. The next sentence (\"Other prompts load that line too\") partly supplies that context, so the example remains followable. An explicit gloss on first mention would make it clear at once."
    level: info
outcome: warn
---

# Review

## Summary

The external names are identified adequately. Python and CPython are the subject of a worked comparison. TOML is introduced as "a TOML configuration". `asyncio.TaskGroup`, `tomllib` and `inspect.getargspec` are each described by what they do or what changed.

The gap is Commonplace. The note's normative section depends on it, but the note never says what kind of thing it is. `AGENTS.md` is a lesser case: the surrounding text largely implies what the file does.
