---
description: "Pre-ingest discovery for self-modifying policies: retrospective reward selection, evaluation timing, and limits of compounding evidence."
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/reinforcement-learning-self-modifying-policies.md"
source_has_frontmatter: true
date: "2026-09-20"
depth: standard
---

# Connection Report: Reinforcement Learning with Self-Modifying Policies

**Source:** [Reinforcement Learning with Self-Modifying Policies](../../../../sources/.snapshots/reinforcement-learning-self-modifying-policies.md)

Discovery by the executing Codex agent under `cp-skill-connect`. These are pre-ingest candidates for the matching authored ingest; the snapshot remains immutable.

## Discovery Trace

- Read source and reports collection contracts, connect-report type, the complete snapshot, and destination README heads for notes, reference, sources, agent-memory-systems, and agentic-systems. Read the self-improving-systems curated head and followed its compounding and proposal-selection links. The snapshot has no tags, so no tag-membership sweep applies.
- Generated titles with `rg -N --no-heading -m1 '^# ' kb/notes/ kb/reference/ kb/agent-memory-systems/ kb/agentic-systems/ kb/sources/ --glob '*.md'`. The broad display was truncated; repeated the generated surface through `rg -i 'self.modif|compound|self.improv|recursive|gödel|godel|reward|learning algorithm|hyperagent|exo|huxley'` for bounded candidate screening.
- Description screening: `rg -n '^description:.*(self.modif|self.improv|evaluat|revers|learning.*learn|reward)'` over all five destinations. Kept Gödel-machine admission, compounding measurement, HGM, and the historical retrospective as concrete mechanism comparisons; generic memory and evaluation hits lacked a sufficiently specific reason.
- Body search: `rg -n 'SSA|success.story|long.term|Schmidhuber'` over all five destinations. Historical retrospective and Gödel-machine neighborhood were strongest. Broad long-term-memory hits were rejected because memory duration alone does not connect to policy-change credit assignment.
- Notes: read the proposal-selection, compounding-measurement, accumulation-versus-compounding, and Gödel-machine candidates. Followed the self-improving-systems head to these mechanisms. Kept the latter two strongest analytical comparisons below; proposal selection remains a qualification-sensitive follow-up because changes already execute before SSA rejects them.
- Sources: read RSI-since-1987 and HGM ingests. Kept both: the first routes to this original construction; the second evaluates ancestor changes through descendant productivity, with a different experimental and selection architecture.
- Agentic systems: body query `rg -n 'reward|rollback|revert|self.modif' kb/agentic-systems/reviews/exo.md` and read Exo. Kept the contrast between executable-state rollback and the non-resettable record of experience.
- Agent memory systems: README, titles, descriptions, and focused search of HyperAgents identified a possible learned-improver comparison. Deferred it because HGM and the existing compounding note already provide the more direct route for this bounded pass.
- Reference: README, titles, descriptions, and focused search of `tag-readme-trace-as-self-improving-loop.md` yielded only broad loop resemblance. No reference candidate retained: SSA does not establish a Commonplace implementation choice.
- External: evaluated only the source URL already in the capture. No external discovery. Instructions and workshops excluded by the source contract.

## Connections Found

- [Gödel machines are a proof-governed case of reflective self-modification](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) — **compares-with**: SSA admits execution before retrospectively undoing changes that fail a reward-rate criterion; the Gödel machine licenses a switch through a proof under its current formalization. This distinguishes two grounds and timings of admission.
- [Compounding is tested in later improvement, not by the accepting metric](../../../../notes/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md) — **compares-with**: SSA explicitly measures long-term outcomes after earlier changes and lets those changes affect later learning. Its single lived reward history does not supply an independent counterfactual test isolating the productivity contributed by learned update rules.
- [Recursive Self-Improvement Since 1987](../../../../sources/recursive-self-improvement-since-1987.ingest.md) — **compares-with**: the original policy paper specifies the checkpoint, stack, and reward-rate mechanisms that the retrospective summarizes, permitting readers to separate its actual empirical result from the later historical characterization.
- [Huxley-Gödel Machine](../../../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md) — **compares-with**: both value earlier modifications through later consequences, but SSA selects a surviving linear history using lifelong reward per time while HGM selects branches through estimated descendant productivity under repeatable benchmark trials.
- [Exo](../../../../agentic-systems/reviews/exo.md) — **compares-with**: both undo executable changes without undoing lived experience. SSA supplies an explicit reward-rate rejection criterion; Exo preserves canonical history outside sandbox rewinds but its semantic acceptance policy is less determinate.
- [Original paper](https://nic.schraudolph.org/pubs/SchZhaSch98.pdf) — **derived-from**: the future ingest analyzes this captured author manuscript.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [Gödel-machine note](../../../../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md) → future matching ingest — **evidenced-by**: the source can ground the empirical-retention comparison with a primary description of SSA. Notes authorize this label toward sources. Author only after the ingest exists, with retained quotes or an explicit snapshot requirement.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [Proposal-selection loop](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) — deferred as a direct evidence edge: the paper's policy changes act before retrospective rejection. A writer must state that timing rather than silently equating SSA with an evaluate-before-operation gate.
- [Self-improving-systems head](../../../../tags/self-improving-systems-README.md) — useful discovery route, but too general as an additional outbound source connection.

## Index Membership

None

## Synthesis Opportunities

None

## Maintenance Observations

None

## Flags

- The empirical comparison reports about sixtyfold improvement over random behavior in one constructed partially observable task. It does not isolate learned evaluation timing or learned learning rules from the rest of the architecture.
- The guarantee is a surviving history satisfying an empirical reward-rate condition at checkpoints, possibly empty. It is not guaranteed optimal policy discovery, convergence speed, or sustained causal compounding.
- Evaluation timing is policy-influenced, but the supplied SSA rule, reward channel, and instruction set still constrain adaptation.
- PDF extraction flattens exponents and fractions and repeats Figure 4 references. Check the captured PDF when exact numerical or mathematical transcription matters.
