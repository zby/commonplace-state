---
type: reports/types/improvement-run-findings.md
description: The ten warning findings the run read on the start text, with their dispositions, and the re-review results on the edited text
note: kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets.md
start-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
findings:
- atom: kb/instructions/review-gates/prose/source-residue.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: f7f1841ea22043d68aeb84728c8d90ce
  output-sha256: 7faee06961a72d74eba0a9d969500bdb7b18621adcf32df3fab9eceef2b0ac47
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The quality-scores paragraph states a Commonplace skill and its candidate sources in the present tense as plain fact inside a general consequence.
  disposition: fixed
  strategy: kb/instructions/fix-warnings/fix-strategy-taxonomy.md#unframed-domain-examples
- atom: kb/instructions/review-gates/prose/source-residue.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: f7f1841ea22043d68aeb84728c8d90ce
  output-sha256: 7faee06961a72d74eba0a9d969500bdb7b18621adcf32df3fab9eceef2b0ac47
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The description lists "connect", a Commonplace skill name, as if it were a general operation.
  disposition: open
  item: kb/reports/state/improve/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets/20261114-072641#1
- atom: kb/instructions/review-gates/prose/proportion-mismatch.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: e8965d9b14fb44adb4bedf2d706a262a
  output-sha256: 1096fd347f005a7af90f1a18a3a31c5fec974749e51babe8d9f776ebd05887e3
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The library/workshop consequence, mostly ADR history, takes about twice the space of the regime analysis, and the top regime gets two sentences.
  disposition: open
  item: kb/reports/state/improve/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets/20261114-072641#2
- atom: kb/instructions/review-gates/sentence/parsing-ambiguity.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: 4661611ea03446298b54fdd96398d0f7
  output-sha256: fccc429c4429e32b6fe95e95d97e71eedf8805fa3156667248f500f6c793283a
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: In the load-bearing-descriptions section, the clause "and can be reached only through body-level search" attaches to "operations" on first reading, not to "a note".
  disposition: fixed
  strategy: 'new-pattern: split a sentence so a trailing clause attaches to its subject'
- atom: kb/instructions/review-gates/sentence/clause-packing.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: 2a983bca91c34902bd14d8f5ca8dbaeb
  output-sha256: 10373457e95fcb669192d16110353dc7d429a3b88b6e6f2ab66096ed34b5b423
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The same sentence runs about 45 words over four clauses and should be split.
  disposition: fixed
  strategy: 'new-pattern: split a sentence so a trailing clause attaches to its subject'
- atom: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: 01f611de74734f2482c9c9e6874d3224
  output-sha256: 097ca90b6015a1d07f37fe7e9c3752563622a25c1a9ae9927f12e15b2620aa9f
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The subject definition does not say whether "collection" renames the areas note's "area" or names a broader concept that areas instantiate.
  disposition: open
  item: kb/reports/state/improve/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets/20261114-072641#3
- atom: kb/instructions/review-gates/semantic/grounding-alignment.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: 246c3647b6d746668a9e0f6c7cc74598
  output-sha256: 5bffc094023f77584fcba8b14d6d082b94df27735c4558beeac636efa9f519c8
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The library/workshop consequence claims separation keeps index-scan discovery viable, while ADR 025 records that the one cited case outgrew a usable index despite curation.
  disposition: open
  item: kb/reports/state/improve/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets/20261114-072641#4
- atom: kb/instructions/review-gates/accessibility/undefined-terms.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: c6d04f635a7c4237b477d922711987a4
  output-sha256: cf4beddd990fcf48c6fc32461c55a60502f3fc8fbd34733fe65ee00bc2b2d7ba
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: '"Candidate discovery" is used before the reader learns what is discovered.'
  disposition: fixed
  strategy: 'new-pattern: gloss a term inline at first use'
- atom: kb/instructions/review-gates/accessibility/undefined-terms.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: c6d04f635a7c4237b477d922711987a4
  output-sha256: cf4beddd990fcf48c6fc32461c55a60502f3fc8fbd34733fe65ee00bc2b2d7ba
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: '"Per-window degradation" is a link with no gloss of what degrades.'
  disposition: fixed
  strategy: 'new-pattern: gloss a term inline at first use'
- atom: kb/theory/COLLECTION.md
  run: kb/reports/state/review/runs/20261112T094905Z
  launch: 5b8be8d984e0436193ae6753407a42f3
  output-sha256: d7440cfd3643df165ffe7d2aadf378eb39474b31101466f54030a02ef10d9840
  text-sha256: d30b10dbe927ec10d798b0b1993550231721d6fa6734892bc726eebb490c9548
  outcome: warn
  finding: The footer labels the quality-scores note "extends", but its context phrase describes a neighbouring limit, not a development of this argument.
  disposition: open
  item: kb/reports/state/improve/kb/theory/two-context-boundaries-govern-operations-on-read-together-note-sets/20261114-072641#5
- atom: kb/instructions/review-gates/accessibility/jargon-persistence.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 6eaf03502699437b92e393fc25646712
  output-sha256: 5bcf3d2be2b502946667c68b69043652497cee22e773f1186e98b4058c759818
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/accessibility/notation-opacity.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 82d295a739344dd4976377a33260ca43
  output-sha256: 9789c9249440fef0f6cbbefd3c8745877f66e9fcd3b1d5cc5868b09834d843ed
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/accessibility/undefined-terms.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 3fa6bac59e93429cba60c9290023e681
  output-sha256: 057e65675101bec54b8737f029607437f178cb1d6e8d7f4c9ae2601b94eb799f
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/instructions/review-gates/accessibility/unidentified-references.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: ccdec2d06c7c4b719f648a406f8a6695
  output-sha256: e99581c060b21848aea3a70634ce3167f1ae83a03e2a30a43cef7db34b0fc168
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/complexity/claim-to-section-ratio.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 1ce71bb3a2054246a342c3fd3f024a95
  output-sha256: d74020d4858a492a7c57ee62bc58c9d0d63573b38f0c024157684460ce5dd7bd
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/complexity/connection-inflation.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 00834d553e0448d48a55ccc1289296cf
  output-sha256: 909e225bf31e7c7b4493df24cbe8646259b64d7da6e6eb4efaf8ee520cb90730
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/complexity/could-be-a-paragraph.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 78649d3cc2e0425587677b6b141d61c5
  output-sha256: 63d5c03fa93597fd8887604c86a1daf24c3429b1d4900697cb1bd1772f3165a7
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/complexity/framework-decoration.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 5a2bc23f206140b19f74538c79cf83ca
  output-sha256: c87ed8c6e889d9c763bc65286f621cfdc8aa697c6631b6305455245ccc68d6b4
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/frontmatter/title-body-alignment.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: c3979274ab974431a99645e35a56e65c
  output-sha256: 38383284f1bc5390f31f24f58221516380f26beaaca814f8a4c20374758d1ee6
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/theory/COLLECTION.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 26e9fd7cd78e4de7a0a5239000c88552
  output-sha256: 86170b05fe3b9d2bdcee5637a7e313d3363d47624ed5f8dfb33c7722fa4672fb
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/types/note.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 22c84277cacb48f4962e4b4b828e9116
  output-sha256: 74722c4e60f4ff982445dd9bffd2fec9fb327b0a0bf7673ebe7646f1c10fbe4b
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/anthropomorphic-framing.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: f2620e2f7795429582158f81ec59a0a1
  output-sha256: 1c62af1ef9640fd851f47d4fc97646c5987ea7ff1fd58b04078a6f91814ecb0f
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/bridge-paragraph-duplication.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 96c84f36ea46451da64001e87865ccbc
  output-sha256: 4126394278b4b1aae13db2ecf898383ef23e673fdc03f97ddab41f3eb8d2c75c
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/confidence-miscalibration.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 1d58a19db2064c6da6ae86c68f84001e
  output-sha256: 75072908df50de913517ce9e17e73e60f7799c405f2563de3553f92d2a1f158c
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/instructions/review-gates/prose/mannered-prose.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 1b38bc9cb1a6421285e21c5af05111c5
  output-sha256: ed86aa7d5dedfb04b9810b4a6ff01b6313aa39e743dbd07fd30b7ff8e07e053d
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/orphan-references.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: e6c408e601224d85b7cd69f91b1ff0bf
  output-sha256: 54851f4759bdddcf7aee21788027c1948da1d874f5d8e6dd5de9d174e78d522a
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/proportion-mismatch.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 3600ce80064a485b9a7f0c4a138ea256
  output-sha256: 90f58ba70fff7d39e61e19ce95b4a09bf90c18af07c015c93091dd4535dec4a6
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/instructions/review-gates/prose/pseudo-formalism.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: fd347041894547fe8fc70bb0c53d409e
  output-sha256: 5fba4d32647bbcacb916705bf958ee72476cc7bf68bc02f283e817aa92179294
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/redundant-restatement.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: d55047221a284066948d22055dfb6532
  output-sha256: 7eb09e5c31d2165b08ba8805618ac8e1e25808046874a9e99eb199a309dfa8d5
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/source-residue.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 034f8dae5baf46128a0629e4db76b755
  output-sha256: 042a0ca1593616d5ae65eafcc2e7824ca186bbacf1584c29ff6084fb888aa03b
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/prose/unbridged-cross-domain.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 919f82bb58d74c118b79e16e289b0b78
  output-sha256: 689feaeee4bb765f57b6ee9baab28c537922540d7f258775a96cb6ccf8104ec5
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/completeness-boundary-cases.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: dacc48bb5ab447e99c92df897873d6ad
  output-sha256: bb050ae9504109029fc618aa9a1479b3f7e2e8632cb4059d7c6fd59558e6aa43
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/conceptual-role-conflation.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: d2d3c10774d349b89d577f1d3077371f
  output-sha256: 5238d6f049aa0504bae857416dee2e35f722f902e2aeaf07421e1dfef906adb2
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/epistemic-status-blur.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 69cd133672bb4ba3a0b36b4f6d299e04
  output-sha256: 4f5f83acfe62d4802f88602c0dbad0aff7fe99e3c74dbc56b38efcf3af57c54a
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/explanatory-reach.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 4df8929fbb934b6785e7400255ab4126
  output-sha256: e18b581fd06eafae73c9accf1ef68e5d0b4a3a8493591d66996322e7c025b056
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/grounding-alignment.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: b374f09843b542e9b42eb096bc630670
  output-sha256: b3ecb7a26367bf148e80f2ab8076407bca8dd44565b5d2b1c7f5017a661bf5db
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/instructions/review-gates/semantic/internal-consistency.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 6e06884f63b34bb9813735472095ed9b
  output-sha256: 84ee7fc44ed040c33cfdd45a46567e5938315b75618f0c27d49fd6b5eb5e0ac5
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/load-bearing-qualifiers.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: ebacf7654e904ca0b590ab8d7134b73a
  output-sha256: 92faec60afd822a31a5002a7cc912b5f3ff30e197da17caf128ed454766cb845
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/underspecified-assertions.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 836a9a33bbd7486da1e1bc2eee1dc09b
  output-sha256: a47a1f25d8cd674accd11263e2cc807fdeb4c3bb38ef06511c72882463aaf80b
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/unearned-generality.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 50df98e564ca4814b8ac5335d805752c
  output-sha256: dd68b666b1670cfaf312f752a101d096081cfe6d981e69fe9f643c9de7968d93
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/semantic/unwarranted-scope.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 097f383c372c4dafa58d401cb4632be4
  output-sha256: c37160b7a213106d92d6a727e9fa47b9d12d079ce6c3782fc198689bb132d2d7
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/sentence/clause-packing.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: fa9c3c3baaf34d43bfc995721b2ae78e
  output-sha256: 53f26080df0715772f5ca10f6bbcde3d39289d0891ef3b032a30ad9aac174229
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/instructions/review-gates/sentence/concept-attribution.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 4ced713babf144d99b3fbc433b8b3c41
  output-sha256: 04990c241f104f9496135de56e0416937c67973520ae1a54026f81ce8969e656
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/sentence/framing-mismatch.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: ea3b22968b2e4bc58c1502e40fc6e483
  output-sha256: af5ae65af352e1951a16ddde6f888e042e502c8cb778a90e08e793bb9134e03b
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/sentence/misleading-link-text.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: c2a8ac549efd49bfb7a595c11f1a56cd
  output-sha256: 6230d17c57879abe800cdd7739666daa1ed94d9678b0a876c4984d861182b164
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/sentence/parsing-ambiguity.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 627f480994c54771819b59d37bb23271
  output-sha256: 6b40e1be82644ae823f55ebb0a8c5a0c959eb3b2ef24d9f1c1e9c83504e26624
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/sentence/stock-phrases.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: b5de3f5946a748afb9bd78f5a070dca5
  output-sha256: a6f547519cdec5b6c4616ce51532a93e04e83db622abaf34106544ee02375586
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: warn
  disposition: none
  finding: Re-review after the edits; not worked in this run. See the cited launch output.
- atom: kb/instructions/review-gates/structural/bullet-capitalization.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 7f8112aa2e8c4ba6bbbe6cd4dbb73264
  output-sha256: fe1208fe9569f0b21aa1d57a7aa13c95a9f8912483a417c6ff75d48a9b4706f0
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/structural/compound-bullet.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: b62ba3386e5f439ab314f5dce07d6439
  output-sha256: b036c52b4461f486211f4a563054b25150e45b58c96e1ced1bb7ccfaa4823e38
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
- atom: kb/instructions/review-gates/structural/general-before-specific.md
  run: kb/reports/state/review/runs/20261114T072646Z
  launch: 0daf3a82dbc44bda8c103c301c7d01d5
  output-sha256: 35b1427bc99794bf4fdcac05a2bf2f076d853828be365f5fec6a52b20b64f8b1
  text-sha256: 5af541016c3d66eddaec7cc185c486b712b2ab60c571fab7d1bb1cd12a295f47
  outcome: pass
  disposition: none
---

# Findings

The first ten entries are the warning-level findings of the eight fresh warnings the run started from. The remaining entries cite the re-review of the edited text; none of those was worked.
