## Fix Report: known-target-discovery-benchmarks-show-reachability-not-discovery-closure

| # | Check | Strategy | Summary | Status |
|---|-------|----------|---------|--------|
| 1 | Accessibility / unidentified-references | new-pattern | Identified GIANTS as a benchmark on first mention. | fixed |
| 2 | Sentence / clause-packing | new-pattern | Split the overloaded proxy-oracle sentence so the conceptual move and GIANTS controls are separate. | fixed |

### Warning-to-fix mapping

- **#1 (Accessibility / unidentified-references):** The review warned that "In GIANTS, a model receives summaries..." explains the mechanics but not the identifier type. The first mention now identifies GIANTS as a benchmark for reconstructing downstream scientific insights from parent-paper summaries.
- **#2 (Sentence / clause-packing):** The review warned that the sentence combining the no-oracle-to-proxy-oracle move with GIANTS controls was overloaded. The passage now separates the proxy-oracle claim from the list of GIANTS hardening mechanisms.

### Deferred items

- (none)

### New patterns

- **identifier-type-on-first-mention:** A named external system, dataset, benchmark, or project is linked and mechanically described, but not identified by artifact type on first mention.
- **split-compound-concept-and-controls:** A sentence combines a conceptual classification with a long list of implementation or evaluation controls; split the conceptual move from the control list without changing the claim.
