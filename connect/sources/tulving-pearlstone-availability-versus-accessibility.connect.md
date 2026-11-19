---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/.snapshots/tulving-pearlstone-availability-versus-accessibility.md"
source_has_frontmatter: true
date: "2026-08-26"
depth: standard
---

# Connection Report: Availability versus accessibility of information in memory for words

**Source:** [Availability versus accessibility of information in memory for words](../../../../sources/.snapshots/tulving-pearlstone-availability-versus-accessibility.md)

## Discovery Trace

**Description and title scans:**
- Read `kb/notes/README.md`, `tags-README.md`, `agent-memory-README.md`, `context-engineering-README.md`, `failure-modes-README.md`, `evaluation-README.md`, and `learning-theory-README.md`. Generated the notes title surface with `rg -N --no-heading -m1 '^# ' kb/notes/ --glob '*.md'` and filtered it with `storage|access|retriev|recall|activation|context|knowledge|memory|transfer|analogy|cue`. This surfaced the activation note, the retrieval-miss note, the psychology-transfer note, and the unrelated Tulving-taxonomy note.
- Read the destination heads for `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/`; generated the corresponding title surfaces with the same `rg -N --no-heading -m1 '^# '` query. No reference or agentic-system artifact needed this word-recall experiment as direct evidence. The agent-memory review framework uses Commonplace's local `read-back` definition, which this source does not define.

**Body search:**
- `rg -n -i 'availability|accessibility|retrieval cue|stored.*retriev|recall.*cue|not accessible|memory storage' kb/notes kb/reference kb/agent-memory-systems kb/agentic-systems kb/sources --glob '*.md'` -- kept the activation note; rejected broad retrieval and system-review matches whose mechanisms concern artifact discovery or prompt assembly rather than human word recall.
- `rg -n -i 'read-back|contextual activation|behavioral activation|storage-to-context|context-to-action' ...` -- confirmed that `read-back` and action-level activation are local Commonplace distinctions downstream of, but not supplied by, the paper's availability/accessibility distinction.
- `rg '^description:' ... | rg -i 'retriev|activation|stored|memory|transfer|analogy|context.*action|action.*context'` -- surfaced the psychology-transfer methodology and the activation requirement as possible bounds, not additional direct targets.

**Link following:**
- Followed the activation note into the agent-memory review type, collection README, and review-framework design. These artifacts depend on the note's local operational definition, not on Tulving and Pearlstone's vocabulary.
- Followed the psychology-transfer note to the three-space Tulving note. The latter concerns semantic/episodic/procedural taxonomy, not availability/accessibility, so the shared author name is not a substantive connection.

**Per-destination result:**
- `notes`: two useful candidates and three informative rejections.
- `reference`: no candidate after inspecting the review-system and storage-title matches.
- `agent-memory-systems`: no outbound candidate; the review contract's use of `read-back` is narrower and locally constituted.
- `agentic-systems`: skipped after the title and body scans exposed no matching whole-system analysis trigger.
- `sources`: no settled source-to-source edge; existing psychology commentary is too indirect to improve traversal.
- `external`: authorized but not prospected; no already-known external target beyond the captured paper itself needed an edge.

## Connections Found

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) -- **is-evidence-for**: the cued-versus-uncued recall experiment supplies a classic human baseline for information being available in storage yet inaccessible for retrieval, while stopping before the note's stronger context-to-action and `read-back` claims.
- [An experiment identifies only the contrast it actually runs](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md) -- **compares-with**: the paper varies retrieval-cue conditions while holding presentation fixed, so its result identifies accessibility under those recall conditions rather than preservation, action, or a general theory of activation.

## Bidirectional Candidates

None.

## Reverse-edge Candidates

- [Knowledge storage does not imply contextual activation](../../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) → source -- **evidenced-by**: cite the experiment for the storage/availability-to-retrieval/accessibility baseline and state explicitly that it does not establish action-level activation.
- [Psychology-to-agent transfer needs per-principle failure-mode testing](../../../../notes/psychology-to-agent-transfer-needs-per-principle-failure-mode-testing.md) → source -- **evidenced-by**: use the experiment as a primary human-side failure-mode baseline while keeping any transfer to agent context selection conditional.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- [Three-space agent memory echoes Tulving's taxonomy but the analogy may be decorative](../../../../notes/three-space-agent-memory-echoes-tulvings-taxonomy-but-the-analogy.md) -- rejected: it concerns a different Tulving taxonomy; author-name overlap is not a shared claim or mechanism.
- [A retrieval miss is a local reflective-path failure](../../../../notes/a-retrieval-miss-is-a-local-reflective-path-failure.md) -- rejected: its causal path is repository artifact discovery in a reflective system, not human mnemonic accessibility; the activation note is the proper transfer boundary.
- [Agent memory is a crosscutting concern, not a separable niche](../../../../notes/agent-memory-is-a-crosscutting-concern-not-a-separable-niche.md) -- rejected: it cites the local activation distinction and does not need a human word-recall experiment as direct support.
- [Review framework and comparison matrix: design and decisions](../../../../agent-memory-systems/review-framework-design.md) -- rejected: its load-bearing term is Commonplace's operational `read-back`, which this paper neither names nor defines.

## Index Membership

None.

## Synthesis Opportunities

None. The useful synthesis already belongs in the activation note as a bounded historical baseline rather than in a new note.

## Maintenance Observations

None.

## Flags

- The paper supports only the stored-versus-retrievable transition. Treating it as support for context-to-action activation would exceed its experimental contrast.
