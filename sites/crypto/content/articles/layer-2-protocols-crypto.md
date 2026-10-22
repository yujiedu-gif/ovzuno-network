---
title: "Layer 2 protocols crypto: how scaling systems work"
description: "Learn how layer 2 protocols crypto process transactions, connect to layer 1, and differ in settlement, data availability, and security assumptions."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["Ethereum layer 2", "rollup", "data availability"]
author: "editorial_team"
primary_keyword: "layer 2 protocols crypto"
owned_question: "How do crypto layer 2 protocols process transactions, interact with a layer 1, and differ in their security and data-availability designs?"
risk_level: "medium"
---

Crypto layer 2 protocols process transactions outside a base blockchain and connect to layer 1 for specified functions, such as recording published data or providing consensus for that record. How much layer 1 verifies, what information is available there, and what happens when a claim is disputed depend on the design; the layer 2 label alone does not establish those properties.

## What a crypto layer 2 protocol is—and is not

A **layer 1** is the base blockchain. A **layer 2** is a system built to handle activity in relation to that base layer, but the term does not specify one universal architecture. This article focuses on rollups: a rollup separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. That description applies to the rollup model, not automatically to every network described as a layer 2. [source](<https://ethereum.org/developers/docs/scaling/>)

The distinction is about which functions happen where. A rollup processes transactions outside layer 1; layer 1 provides a place to publish information and establish a record of that publication. The rollup’s design determines what is published and what verification is performed. Therefore, it is inaccurate to assume that layer 1 re-executes every layer 2 transaction simply because the system uses layer 1.

A separate blockchain, a bridge, and a rollup should not be treated as synonyms. A bridge coordinates activity between otherwise separate blockchain environments, while the rollup model described here publishes information to a base layer. Labels used in the broader ecosystem can vary, so a technical description should identify the architecture and its actual dependencies rather than relying on a name alone.

## How a layer 2 transaction moves from submission to settlement

A conceptual transaction flow can be described in three stages. It is a framework for reading protocol documentation, not a universal sequence of operators or steps.

1. **Submission:** A user or application sends a transaction into the layer 2 system. The available evidence does not establish a single submission route or identify one required transaction-processing operator for all designs.
2. **Layer 2 execution:** The system processes transactions outside the base layer and updates state according to its own design. “Execution” means applying transaction rules to determine the resulting state.
3. **Publication to layer 1:** The system posts data or other information to the base layer. Layer 1 consensus establishes the published record, but the exact information and verification responsibilities depend on the protocol. [source](<https://ethereum.org/developers/docs/scaling/>)

This flow separates execution from settlement. In this context, **settlement** means the base layer’s role in establishing a record of what was published. It does not mean that every layer 2 transaction has been independently executed by layer 1. Ethereum nodes use consensus to agree on new blocks and the continuing chain, but that general behavior does not itself tell us what a particular rollup’s verification process checks. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

A protocol may describe proofs, challenges, or other mechanisms for checking claims. The evidence available here does not establish one verification method as universal. For a specific system, documentation needs to explain what is checked, which component performs the check, and what the protocol does if a claim is challenged or rejected. Without those details, the transaction flow remains a high-level model rather than a complete operational account.

## Rollups, data availability, and verification choices

Rollups separate execution from the base layer, but the word “rollup” does not settle every question about data or verification. One key distinction is whether the layer 1 is used for both consensus and data availability. In L2BEAT’s terminology, a rollup uses layer 1 for consensus and data availability, while a system that publishes data elsewhere adds external data-availability assumptions and is classified differently. This is a terminology-specific distinction, not evidence that every project uses labels consistently. [source](<https://l2beat.com/glossary>)

**Data availability** concerns whether the information needed by a system’s participants is available where and when the system requires it. For an evaluation, do not stop at asking whether a protocol posts something to layer 1. Establish what is posted, where else relevant information may be held, and how the design’s participants can obtain what they need to verify or reconstruct activity. The available evidence does not support a general guarantee that every layer 2 makes the same information available in the same way.

Verification is another design choice. A technical description may discuss validity checks, challenges, or other mechanisms, but those terms should not be treated as interchangeable without examining the protocol’s documentation. The permitted evidence does not specify a universal validity-proof or fraud-proof flow. It supports a narrower conclusion: rollups separate execution from the base layer, and both the verification method and data-publication assumptions need to be established for the particular design. [source](<https://ethereum.org/developers/docs/scaling/>) [source](<https://l2beat.com/glossary>)

The practical implication is that “posted to layer 1” is not enough information to infer what layer 1 can verify. A reader should locate the protocol’s description of the published record, then determine how the design connects that record to its state and verification process. If the documentation does not answer those questions, the uncertainty should remain explicit rather than being filled in from the layer 2 label.

## What layer 2 security depends on

A layer 2’s security depends on the functions it assigns to layer 1 and on the assumptions made by its own design. The rollup model places execution outside the base layer while publishing information to it; the external data-availability distinction shows that some systems rely on data arrangements beyond layer 1. Those differences mean that layer 1’s role cannot be treated as a blanket guarantee for every aspect of a layer 2. [source](<https://ethereum.org/developers/docs/scaling/>) [source](<https://l2beat.com/glossary>)

For a specific protocol, examine the documented connection between its layer 2 state and the information published to layer 1. Then check what the protocol says about verification and data availability. These questions identify important boundaries, but the allowed evidence does not establish universal behavior for sequencer operation, upgrade controls, proof or challenge participation, withdrawal timing, or recovery. Do not assume that these mechanisms are decentralized, permissionless, immediate, or enforceable by layer 1 unless the protocol documentation supports that conclusion.

Keep the responsibilities distinct. Layer 1 consensus establishes its own published record; the layer 2 design defines how its execution and state relate to that record. Tools, applications, or services around a protocol may have their own behavior, but the available evidence does not specify those components for all layer 2 systems. A security conclusion about a particular implementation therefore requires evidence about its specific mechanisms and dependencies.

## Questions to ask when evaluating a layer 2 design

Use technical documentation to answer these questions before characterizing a particular system:

- **Where are transactions executed?** Identify whether execution happens outside the base layer and where the resulting state is maintained.
- **What is published to layer 1?** Look for the kind of information recorded and the role base-layer consensus plays in establishing that record.
- **What does layer 1 verify?** Find the stated verification mechanism. Do not assume that publication means layer 1 re-executes every layer 2 transaction.
- **Where is data available?** Determine whether the design uses layer 1 for data availability or introduces an external data-availability assumption. [source](<https://l2beat.com/glossary>)
- **Which details remain implementation-specific?** Check the protocol’s own account of submission, verification, upgrades, and recovery. The available evidence does not support universal answers for those mechanisms.

These questions support a precise description without ranking networks or assuming a standard design. The core model is that rollups move execution off the base layer and publish information to it; the exact verification and data-availability arrangements must be checked for each system. [source](<https://ethereum.org/developers/docs/scaling/>)

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
