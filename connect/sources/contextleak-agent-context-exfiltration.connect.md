---
description: "Discovery for ContextLeak's tool-metadata attack and the distinction between tool selection and contextual-data disclosure"
type: kb/reports/types/connect-report.md
source: "kb/sources/.snapshots/contextleak-agent-context-exfiltration.md"
source_has_frontmatter: true
date: "2026-09-24"
depth: standard
---

# Connection Report: ContextLeak

**Source:** [ContextLeak paper](../../../../sources/.snapshots/contextleak-agent-context-exfiltration.md)

## Discovery Trace

- Read all 2,185 snapshot lines in five consecutive bounded reads, including appendix prompts, per-domain results, references, and defense evaluation. Embedded attack prompts were treated as source data.
- Reused this batch's fully read collection contracts, curated destination README heads and complete fresh title listings for notes, reference, sources, agent-memory-systems, and agentic-systems. The source has no tags; no tag-completeness shortcut applies.
- Notes and reference searches included `rg -l -i 'prompt injection|exfiltrat|\btaint\b|untrusted'` and `rg -n -i '^description:.*(authority|quarantine|privilege|permission|security|trust)'`. Fully read the privilege-quarantine, shared-token-medium, flat-scoping, and four-field-risk notes; recovered the output-limited portion of the scoping read separately. The shared-medium note directly explains the metadata-to-instruction crossing; quarantine is a proposed defense comparator, not a defense tested by this paper. The broader four-field risk framing adds less than those direct edges.
- Sources, memory-system and agentic-system description query: `rg -i '^description:.*(injection|exfiltrat|security|tool metadata|untrusted)'`. Focused body search: `rg -l -i 'prompt injection|exfiltrat|\btaint\b|tool metadata'`. Many memory matches concern benign context insertion rather than adversarial exfiltration. No direct system comparison retained: the paper does not test those systems, and a shared use of MCP or memory injection is insufficient evidence of comparable vulnerability.
- Source discovery found and fully read Fences, not Sandboxes: its cooperative-governance premise makes a precise threat-model comparison. Other harness permission discussions added no stronger connection than the quarantine note.
- Reference query `rg -n -i '^description:.*(security|quarantine|privilege|untrusted)'` returned no matches. The generic gap-plan body hit concerns broader memory governance and was not retained as a direct companion.
- Link following: quarantine → four-field risk explains untrusted content gaining behavioral force; shared-medium → scoping distinguishes authority confusion from mere context availability. These links were read and evaluated, not inferred from titles alone.
- Candidate paths verified; source labels follow the sources collection contract. The notes contract authorizes the reverse evidence suggestion. External discovery was skipped; only the supplied arXiv source was evaluated.

## Connections Found

- [LLM contexts interpret instructions and content through the same token medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) — **is-evidence-for**: attacker-controlled tool names and descriptions change both tool choice and disclosed arguments, providing a concrete case of descriptive metadata gaining instruction-like force through a shared context.
- [Agent orchestration needs a privilege quarantine](../../../../notes/orchestration-needs-privilege-quarantine-not-permission-scope.md) — **compares-with**: ContextLeak distinguishes getting a tool selected from causing context to be placed in its arguments. That supplies a concrete threat to compare with the note's distinction between allowed tool identity and the provenance of the judgment that calls it. The paper does not test role quarantine or prove its effectiveness.
- [LLM context is composed without scoping](../../../../notes/llm-context-is-composed-without-scoping.md) — **compares-with**: limiting what a role can see bounds the material available for disclosure, while an in-scope tool may still receive unauthorized arguments. Context boundaries and disclosure controls answer different parts of this attack path; the paper tests the attack, not that architectural response.
- [Fences, not Sandboxes](../../../../sources/steve-yegge-fences-not-sandboxes.ingest.md) — **compares-with**: the practitioner source assumes cooperative agents honoring policy refusals, whereas ContextLeak tests adversarial metadata that redirects a tool-using agent. This comparison bounds the former's containment claim without treating the studies as a matched experiment.
- [Original paper](https://arxiv.org/abs/2608.27800) — **derived-from**: primary external source for the eventual ingest.

## Bidirectional Candidates

None

## Reverse-edge Candidates

- [LLM contexts interpret instructions and content through the same token medium](../../../../notes/llm-context-interprets-instructions-and-content-through-one-medium.md) → eventual tracked ingest — **evidenced-by**: supplies a measured tool-metadata case for the authority-confusion paragraph, provided the citation retains the installed-malicious-tool assumption and the conditional disclosure metric. The note should not infer failure of every architecture from this tested harness.

## Off-authorisation Candidates

None

## Raw Text Candidates

None

## Rejected Candidates

- [The four-field risk triad](../../../../notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md) — its security question fits, but the shared-medium and quarantine notes provide more specific traversal value; adding the general frame would duplicate the direct edges.
- Evidence that role quarantine works: no role-split defense is evaluated.
- Evidence that persistent KB memory is vulnerable in general: the tested history is short synthetic conversation context; persistent memory stores and retrieval pipelines are not evaluated.
- Direct comparisons with individual memory-system reviews: shared interfaces do not establish shared attack success or comparable security guarantees.

## Index Membership

None

## Synthesis Opportunities

None. The existing authority and scoping notes already own the distinctions.

## Maintenance Observations

None

## Flags

- The threat model assumes the malicious tool has already entered the candidate tool set. The attack controls its name and description; actual network exfiltration by tool code is outside the main measured mechanism, and some tests use a benign stub.
- Malicious-tool selection rate is measured across victim cases. Argument similarity and tool-list precision/recall are conditional on selection; do not present conditional similarity as an unconditional leak rate.
- Main prompt results report selection 0.92 and conditional edit similarity 0.99. The Claude Code deployment reports 22 selections in 100 cases and conditional edit similarity 0.77; these are different settings, not a universal 92% production success rate.
- The strategy-library ablation changes a guidance package used during training and inference while model weights also change. It does not isolate a pure retained-memory mechanism or establish conjectural learning.
- The printed length-reward expression lacks an absolute value around the length difference, so overlong arguments appear to receive reward above one despite prose claiming penalties in both directions. This is an unresolved paper/code discrepancy; implementation was not inspected.
- MCPScan evaluation covers the metadata-monitor prompt because the stub has no malicious flow for taint analysis. Do not claim a bypass of every component of a complete code-inspecting scanner.
- Defense results show low clean task utility as well as lower attack success. They do not isolate degraded utility as the sole cause of defense performance.
- Keep short conversation/tool-list tests, first-call emphasis, and unmeasured long execution trajectories explicit. More capable-model vulnerability claims do not arise from a controlled capability intervention.
