---
title: "ZK Rollup Privacy: What Zero-Knowledge Proofs Hide—and What They Don’t"
description: "Learn how zero-knowledge proofs support zk-rollups, why they do not automatically make transactions private, and what data may still be visible on-chain."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["privacy_identity_zk"]
tags: ["zk-rollup data visibility", "zero-knowledge proofs and privacy", "zk-rollup on-chain metadata", "privacy limitations of zk-rollups"]
author: "editorial_team"
primary_keyword: "zk rollup privacy"
owned_question: "How does privacy work in zk-rollups, and what information can still be visible on-chain?"
risk_level: "medium"
---

# ZK Rollup Privacy: How It Works and What Can Still Be Visible On-Chain

A zero-knowledge proof can let a verifier check a claim without receiving the private witness used to establish it. In a zk-rollup, however, that property does not automatically make every transaction confidential. Privacy depends on what the proof treats as private, what the rollup publishes to Ethereum, and what other information the system exposes.

The useful distinction is between **validity** and **confidentiality**. A validity proof can establish that a proposed state transition satisfies the rules checked by the proof system and verifier. It does not, by itself, establish that the transaction data associated with that transition is hidden. To assess privacy, examine the proof’s role and the system’s published record separately.

## What “zero-knowledge” means in a zk-rollup

In the Ethereum zk-rollup model, execution and state storage take place off the base layer, while the rollup submits state-change summaries and cryptographic validity proofs to Ethereum. A verifier contract accepts a proof for a proposed off-chain state transition before the canonical rollup state is updated. Rollups therefore separate transaction execution from Ethereum while posting data to Ethereum, where base-layer consensus establishes the published record. [1][2][3]

At a high level, a validity proof answers a correctness question: does the proposed transition satisfy the rules checked by the system? The verifier can check the proof rather than re-executing the off-chain transition. That is distinct from asking whether the transition’s underlying information is confidential. A proof may be designed to keep specified inputs private, but information separately submitted as public data is not made private simply because a proof accompanies it. [2][4]

A simplified workflow illustrates the distinction. The rollup processes activity off-chain and forms a proposed state transition. It generates a proof for that transition and submits the proof along with state-change summaries to Ethereum. The verifier checks the proof; if accepted, the canonical rollup state can be updated. The proof’s privacy properties concern information encoded as private inputs in that proof system. They do not automatically cover every item in the accompanying publication. [1][2]

A zero-knowledge privacy application can use a related arrangement: private witness data and off-chain proof generation are separated from a public commitment and an on-chain verifier. The verifier checks the proof against the public commitment without necessarily receiving the witness itself. This example describes a possible privacy-application architecture, not a feature guaranteed by every zk-rollup. The circuit, proof system, and the information published alongside the proof determine what the arrangement protects. [4]

## What may remain visible on-chain

The general Ethereum zk-rollup model includes state-change summaries and validity proofs submitted to Ethereum. The published record can therefore contain information about rollup activity even though execution occurs off-chain. The exact contents and format of those summaries depend on the implementation; the general architecture does not establish that every rollup publishes the same fields. [1][3]

A technical review should distinguish the proof from the other records submitted with it. The proof is evidence that a proposed transition passes the verifier’s checks. The state-change summary is part of the rollup’s published data. Whether that summary reveals particular transaction details depends on its design and contents. A validity proof alone does not answer whether sender or recipient identifiers, amounts, assets, or contract interactions are public. Those fields must be checked in the specific protocol’s documentation and published data rather than inferred from the term “zero-knowledge.” [1][2][3]

The base-layer record is also distinct from information presented by other system components. Ethereum’s consensus establishes the published record, while a rollup may have additional interfaces or data sources. When reviewing an explorer, sequencer interface, or data-availability arrangement, determine separately what information it provides and whether that information is part of the Ethereum record. These components and their behavior vary by design. [3]

This distinction helps avoid a common overstatement. A proof can verify a transition without revealing a private witness, while the rollup may still publish state-change summaries. Conversely, a summary’s existence does not alone show that every transaction field is exposed. The relevant questions are what the summary contains, which values the proof treats as private, and what other system components make available. [1][3][4]

## How privacy-focused designs differ

A privacy-focused design can treat selected information as private witness data and use a public commitment as part of the verification process. A commitment is a public value used in a claim or proof relationship; it is not necessarily the underlying private data itself. The verifier can check the proof against the commitment without necessarily learning the witness. Which facts this conceals depends on the circuit and on what the system makes public. [4]

This is a design choice, not a default property of all zk-rollups. To understand a specific privacy claim, identify the private witness, the public inputs and outputs, and the commitment involved. Then examine what the rollup publishes separately. A private witness in one part of the proof does not imply that related information is absent from every other record or interface. [1][4]

Privacy properties also depend on components beyond the proof’s high-level description. The accepted architecture identifies proof-system and data-publication policies as implementation-dependent. For privacy applications, proof soundness, circuit design, setup assumptions, metadata, key management, and data availability are system-specific considerations. Documentation should state which information is intended to remain private and the assumptions behind that claim. [1][4]

## Metadata and practical privacy limits

Even when a design keeps some witness data private, the overall privacy question includes metadata: information about the system’s operation or context beyond the private witness itself. Metadata is a system-specific risk to assess, not a guarantee that an observer can identify a person or recover concealed information. The proof’s correctness and the privacy of the broader system are separate properties. [4]

A careful assessment should therefore avoid treating “the proof reveals no witness” as equivalent to “the system reveals nothing relevant to privacy.” Instead, inspect what the protocol identifies as private, what it publishes as a commitment or other record, and what its documentation says about metadata and data availability. A possible inference should not be presented as a verified identity or as a guaranteed outcome; its significance depends on the system and the evidence available. [4]

## Questions to ask when assessing a zk-rollup

Use the specific protocol’s documentation and published records to answer these questions. General descriptions explain the architecture, but implementation details determine what information is visible.

- **What does the rollup submit to Ethereum?** Identify the state-change summaries and validity proofs, and consult the protocol’s documentation for the contents and format of its published data. [1][3]
- **Which values are private inputs?** Determine what the proof treats as private witness data and what it exposes as public inputs, outputs, or commitments. Do not infer confidentiality from the “zero-knowledge” label alone. [4]
- **What does the proof establish?** Check the claim the verifier evaluates and the proposed transition it covers. Do not treat proof acceptance as evidence that all associated transaction information is confidential. [2]
- **What other information is available?** Review the base-layer record separately from the information supplied by interfaces, sequencers, or data-availability arrangements. The components and their behavior vary by rollup. [3]
- **What limitations does the privacy documentation state?** Examine the stated assumptions and system-specific considerations, including circuit design, proof soundness, setup assumptions, key management, metadata, and data availability. [4]

The central point is that a validity proof can establish that a proposed state transition meets the rules checked by the system, while transaction confidentiality depends on what the design treats as private and what it publishes. To understand zk-rollup privacy, assess the proof, the state-change summaries, and other information channels as separate parts of the system. [1][2][3][4]

## Sources and references

- [Zero-knowledge rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Zero-Knowledge Rollups](https://ethereum.org/developers/docs/scaling/zk-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [How to build privacy apps on Ethereum with zero-knowledge proofs](https://ethereum.org/latest/privacy-apps-on-ethereum/) — ethereum.org; retrieved 2026-10-19.
