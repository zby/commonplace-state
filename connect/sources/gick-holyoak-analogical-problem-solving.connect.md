---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/gick-holyoak-analogical-problem-solving.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Analogical Problem Solving

**Source:** [Analogical Problem Solving](../../../../sources/.snapshots/gick-holyoak-analogical-problem-solving.md)

## Discovery Trace

**Description and title scans:**
- Read `kb/notes/README.md`, `tags-README.md`, `agent-memory-README.md`, `context-engineering-README.md`, `failure-modes-README.md`, `evaluation-README.md`, and `learning-theory-README.md`. Generated the complete notes title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and filtered it with `storage|access|retriev|recall|activation|context|knowledge|memory|transfer|analogy|cue`. This surfaced the activation note, recognition note, psychology-transfer note, and experiment-scope notes.
- Read the destination heads for `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`; generated their title surfaces with the same `rg -N --no-heading -m1 '^# '` query. The source collection scan surfaced the transformer analogy ingest as a useful human/model comparison.

**Body search:**
- `rg -n -i 'inert knowledge|spontaneous transfer|analogical transfer|notic(e|ing).*relevance|hint.*story|stored.*action|available.*action' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- kept the activation, recognition, psychology-transfer, and transformer-analogy candidates.
- `rg -n -i 'read-back|contextual activation|behavioral activation|storage-to-context|context-to-action' ...` -- confirmed that the paper reaches observable task use after prior encoding but does not instantiate an agent-memory `read-back` channel.
- `rg '^description:' ... | rg -i 'retriev|activation|stored|memory|transfer|analogy|context.*action|action.*context'` -- surfaced the same focused cluster and many implementation reviews whose shared vocabulary alone was insufficient.

**Link following:**
- Followed the activation note to its LLM solution-injection evidence and to the agent-memory review contract. Gick and Holyoak provide a human analogue with explicit hint/no-hint contrasts, not evidence about LLM read-back direction or faithfulness.
- Followed the recognition note to its discovery-lifecycle framing and the psychology-transfer note to its failure-mode matching rule. The paper supplies a bounded human recognition/use case for both, but does not license direct human-to-agent mechanism transfer.
- Read the transformer analogy ingest. It studies learned relational alignment in a controlled model task, making it a useful contrast with the paper's human story-to-problem transfer paradigm.

**Per-destination result:**
- `notes`: four useful candidates, with the activation note the only direct disposition target.
- `reference`: no candidate; shipped architecture does not depend directly on the human experiment.
- `agent-memory-systems`: no outbound candidate; individual implementation reviews use the local read-back vocabulary but are not evidenced by this study.
- `agentic-systems`: skipped after title and body scans exposed no matching whole-system analysis trigger.
- `sources`: one settled comparison with the transformer analogy ingest.
- `external`: authorized but not prospected; no already-known external target beyond the captured paper itself needed an edge.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: participants could recall and apply a memorized analogy when its relevance was hinted, yet usually failed to notice and use it without that cue; this reaches task use more closely than a recall-only study while remaining a bounded human experiment.
- [Recognition, not linking, is the hard problem in knowledge systems](../../../../notes/recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md) -- **compares-with**: the hint/no-hint contrast isolates noticing a shared relational structure as a bottleneck after the source story had been encoded and could be used.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) -- **compares-with**: the study establishes a human failure mode and intervention, while this methodology supplies the missing test before importing that mechanism into LLM-agent design.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **compares-with**: Experiment IV contrasts a relevance hint with no hint after matched story encoding, but the result remains indexed by one target problem, story family, scoring scheme, and participant population.
- [Emergent Analogical Reasoning in Transformers](../../../../sources/emergent-analogical-reasoning-transformers.ingest.md) -- **compares-with**: compare human failure to notice a remote story analogy with a synthetic transformer study that operationalizes analogy as learned relational-role alignment.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidenced-by**: cite the hint/no-hint and recall checks as a human baseline for available knowledge failing to alter problem-solving behavior until relevance is cued.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → source -- **evidenced-by**: use this as a worked primary case where the human failure mode is established but the agent-side transfer still needs separate evidence.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) -- rejected: the note concerns repository discovery routes in a reflective system; Gick and Holyoak manipulate human noticing and analogy use after story encoding.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- rejected: the paper does not bear on the architecture-level decomposition of storage, context engineering, and learning.
- [Review framework and comparison matrix: design and decisions](../../../../agent-memory-systems/review-framework-design.md) -- rejected: a human hint manipulation does not establish how an implementation reads accumulated agent memory back into a model call.

## Index Membership

None.

## Synthesis Opportunities

None. The useful synthesis is the bounded human baseline already needed by the activation note, not an independent Commonplace theory claim.

## Maintenance Observations

None.

## Flags

- The paper's strongest activation-adjacent result is human and task-specific. Any LLM-agent inference must be marked as transfer, not presented as direct evidence.
