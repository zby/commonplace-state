---
description: "Discovery report for possible KB connections from one source artifact"
type: kb/cache/types/connect-report.md
source: "kb/sources/fluent-self-improving-software-factory-2081823472016335059.md"
source_has_frontmatter: true
date: "2026-07-28"
depth: standard
---

# Connection Report: How I built a self-improving software factory

**Source:** [How I built a self-improving software factory](../../../sources/fluent-self-improving-software-factory-2081823472016335059.md)

## Discovery Trace

**Description listing scan:**
- Read the self-improving-systems tag head, the agentic-systems README, the agent-memory-systems README, and scoped descriptions/titles across notes, reference, agentic-systems, and agent-memory-systems.
- Retained candidates were the proposal-selection loop, computational autonomy/human-effort relocation, explicit retention, and trace extraction as meta-learning. Each directly matches a load-bearing mechanism in the source.
- Generic matches for `reviewer`, `learner`, `follow-up`, and `work item` in external-system reviews were not retained unless their claim articulated Fluent's specific human-queue, independent-test, or Expertise path.

**Topic indexes:**
- Read [self-improving-systems](../../../../tags/self-improving-systems-README.md) as the primary routing head. Its update-architecture and actor-allocation sections directly cover Fluent's proposal-selection and human/computational split.
- Read the agentic-systems and agent-memory-systems landing pages. They supplied comparison surfaces, but no existing Fluent artifact was present.

**Body search:**
- `rg -l -i "self-improving software factory"` -- no existing local match.
- `rg -l -i "proposal-selection"` -- found the proposal-selection note and adjacent self-improvement definitions; retained the proposal-selection note.
- `rg -l -i "increasing computational autonomy"` -- found the human-effort note and self-improving-systems head; retained the human-effort note.
- `rg -l -i "learner|expertise"` -- found trace-learning and retention material; retained trace extraction and explicit retention where the source names durable project Expertise.
- `rg -l -i "independent tester|human queue|work item"` -- found adjacent operational notes/reviews, but none was a stronger target than the four selected theory notes.

**Link following:**
- Followed the self-improving-systems head to proposal-selection, computational allocation, governance, and retention notes. No existing system-specific Fluent case or comparison entry was found.

## Connections Found

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) -- **is-evidence-for**: Fluent turns observations into shaped Work Items, runs candidates through a deterministic Tester and reject-capable independent Reviewers, and retains accepted changes through merge and project Expertise.
- [Increasing computational autonomy relocates human effort to the frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) -- **is-evidence-for**: Fluent separates a human queue from agent/compute capacity, allowing more implementation and review work between human decisions while preserving authority for context and judgment.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) -- **is-evidence-for**: the source describes project Expertise as explicit files that the Learner writes and later shaping, implementation, and review agents load.
- [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) -- **is-evidence-for**: Fluent's Learner mines accepted changes and Tester/Reviewer evidence into reusable lessons, while follow-ups and observations preserve weaker signals for later shaping rather than granting them immediate authority.

## Bidirectional Candidates

None. The source's authored surface is its ingest report; the useful durable direction is from the existing theory notes to this source as evidence.

## Reverse-edge Candidates

- [A proposal-selection improvement loop requires search, evaluation, and operative retention](../../../../notes/a-proposal-selection-loop-requires-search-evaluation-and-retention.md) → source -- **evidenced-by**: Fluent provides a detailed practitioner instance of the three functions and their separation into shaping, testing/review, and merge/Expertise retention.
- [Increasing computational autonomy relocates human effort to the frontier](../../../../notes/increasing-computational-autonomy-relocates-human-effort.md) → source -- **evidenced-by**: Fluent's two capacity queues and human-question pauses show how automation can increase throughput without eliminating human judgment.
- [Only explicit retention is currently durable, writable, and addressable at once](../../../../notes/only-explicit-retention-is-durable-writable-and-addressable.md) → source -- **evidenced-by**: project Expertise is a named, inspectable, editable, future-readable retention surface.
- [Use Trace Extraction As Meta-Learning](../../../../notes/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) → source -- **evidenced-by**: Fluent extracts reusable lessons from accepted work and evidence, with promotion gated by the completed Tester/Reviewer path.

## Off-authorisation Candidates

None.

## Raw Text Candidates

None.

## Rejected Candidates

- Existing agent-memory reviews matching `learner` or `reviewer` were rejected when they described different implementations without a specific traversal benefit for Fluent.
- The linked Fluent GitHub repository and external software-factory articles were not opened during connect: external prospecting is out of scope, and they are not already-captured local artifacts.

## Index Membership

- [Self-improving systems](../../../../tags/self-improving-systems-README.md) -- the source is a practitioner case for the proposal-selection, actor-allocation, governance, and explicit-retention dimensions; it should enrich the cluster through reverse evidence links rather than a new source-system review in this ingest.

## Synthesis Opportunities

Fluent gives a single worked case in which proposal selection, explicit memory retention, and human/computational actor allocation are designed together: the same accepted attempt supplies both a software change and reusable project Expertise. That combination could sharpen the cluster's distinction between improving the product and improving the machinery that produces later product changes.

## Maintenance Observations

None.

## Flags

- The source is an article-length practitioner account with an open-source repository link, but this ingest is not code-grounded. A later repository review would need to verify which described paths are implemented, optional, or aspirational.
