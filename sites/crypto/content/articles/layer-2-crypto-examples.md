---
title: "Layer 2 crypto examples: networks and scaling designs"
description: "Explore layer 2 crypto examples by scaling design, how they relate to Layer 1, and why sidechains and other networks may not qualify as Layer 2."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "layer 2 crypto examples"
owned_question: "What are representative Layer 2 crypto examples, and how do their scaling approaches and relationships to Layer 1 differ?"
risk_level: "medium"
---

Layer 2 crypto examples are systems that move some transaction execution away from a Layer 1 blockchain while using that base chain for a defined role, such as publishing data or establishing a settlement record. Ethereum optimistic rollups and validity rollups illustrate two different designs. Their labels describe architectural approaches, not a ranking or a guarantee of security, speed, fees, or availability.

## What makes a blockchain a Layer 2?

A Layer 1 is the base blockchain in a relationship; a Layer 2 is a separate system designed to scale activity while relying on that Layer 1 for a defined role. The role may involve settlement or data publication. To classify a system, look at what it executes away from the base chain and what it sends back, rather than relying only on its name.

A rollup separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. This means the rollup does not execute every transaction directly on Ethereum. It uses a particular relationship with Ethereum to support its own processing and record of state changes. The specific relationship must be checked in the system's documentation. [source](<https://ethereum.org/developers/docs/scaling/>)

The distinction matters because a separate blockchain is not automatically a Layer 2 simply because it connects to another chain or aims to handle more activity. A classification depends on the mechanisms linking the systems, including where data is published and which chain's consensus establishes the relevant record. Technical sources can also use labels differently, so readers should treat a project’s preferred terminology as a starting point, not the final test.

## Layer 2 crypto examples by design

The evidence-supported examples here are architectural categories associated with Ethereum rather than a current directory of named network deployments. The two useful categories are optimistic rollups and validity rollups, often called zero-knowledge rollups. Both execute and store state off Ethereum, but they describe different ways to check proposed state changes.

**Optimistic rollups** move execution and state storage off Ethereum while publishing transaction data and results to Ethereum. Their model treats proposed state transitions optimistically and provides a challenge period with a fraud-proof process for disputing an incorrect execution. This design therefore depends on both offchain processing and a way to raise and resolve a challenge about the proposed result. [source](<https://ethereum.org/developers/docs/scaling/optimistic-rollups/>)

**Validity rollups** also move execution and state storage offchain, but submit state-change summaries and cryptographic validity proofs to Ethereum. The proposed state transition is accepted after a base-layer verifier contract accepts the proof. This is a different verification route from challenging an optimistically accepted transition. The description identifies the proof-based mechanism; it does not establish that every implementation has identical operating or recovery arrangements.

These examples answer the architecture question, but they should not be mistaken for a list of currently operating named networks. The claims available for this article establish the two rollup patterns, not the current deployment status, implementation details, or independently corroborated classification of particular projects. A reliable named-network list would need dated project documentation and technical corroboration for each network’s Layer 1 relationship, data publication, and verification mechanism.

## How the main scaling approaches differ

The most useful comparison is the method used to check state changes. In the optimistic pattern, a challenge period and fraud-proof process provide a route for disputing an incorrect transition. In the validity pattern, a cryptographic proof is submitted and accepted by a verifier contract before the transition is accepted. Both approaches place execution and state storage off the base layer, but their described verification processes differ. [source](<https://ethereum.org/developers/docs/scaling/optimistic-rollups/>)

Data publication is another part of the comparison. A rollup posts data to Ethereum, where base-layer consensus establishes the published record. But not every system associated with scaling publishes its data there. Under L2BEAT’s terminology, a rollup uses a Layer 1 for consensus and data availability; systems publishing data elsewhere have additional external data-availability assumptions and are classified differently. This is a particular technical taxonomy, not a universal rule for every use of the word “Layer 2.” [source](<https://ethereum.org/developers/docs/scaling/>) [source](<https://l2beat.com/glossary>)

Keep these mechanism descriptions separate from claims about user experience. The design descriptions do not establish current transaction fees, speed, availability, performance, or overall security for an individual network. Those are system-specific questions, and the evidence needed to answer them goes beyond identifying an optimistic or validity-proof pattern. A proof mechanism or challenge process describes one aspect of how proposed transitions are handled; it should not be expanded into a general assurance about all risks or operating conditions.

## Layer 2s, sidechains, and other scaling networks

A connection between chains does not, by itself, make one chain a Layer 2 of the other. Bridges coordinate token, message, data, or contract-call activity between otherwise isolated blockchain environments. A destination chain changes only after its bridge-side logic accepts a cross-chain message or transfer condition. That describes coordination across ledgers, not necessarily a rollup-style relationship in which a base chain receives transaction data and establishes the published record. [source](<https://ethereum.org/developers/docs/bridges>)

This distinction is useful when considering sidechains. The evidence here supports describing bridges as mechanisms that coordinate activity between separate blockchain environments, but it does not provide enough detail to classify any named sidechain or make a universal statement about every sidechain’s security design. Do not infer that a chain is a Layer 2 solely because assets or messages can pass between it and another network. Verify what the base chain actually does in the architecture.

Other scaling-related approaches also require precise classification. For example, the Cosmos SDK is a modular framework for building customized application-specific blockchains from reusable and custom modules. That establishes software modularity, but not that a particular chain uses Ethereum or another Layer 1 for settlement or data availability. A framework’s ability to support application-specific chains is not enough to establish Layer 2 status.

## How to verify a Layer 2 example

For a particular network, start with its technical documentation and establish the architecture before accepting the label. Identify the Layer 1 it claims to use, the work performed away from that base chain, what transaction data or summaries are published, and how the system checks or disputes proposed state changes. These questions map the project’s description to concrete mechanisms.

Next, examine data availability and settlement separately. A system’s documentation should make clear where relevant data is published and what the Layer 1 contributes. If the data is published elsewhere, the cited L2BEAT terminology treats that as an external data-availability assumption and distinguishes the system from a rollup in that taxonomy. Do not treat those labels as interchangeable without checking the underlying design. [source](<https://l2beat.com/glossary>)

If the classification is disputed, compare project documentation with independent technical material and describe any disagreement rather than presenting one label as settled fact. Date-check statements about whether a named network is deployed or operational; a design description does not establish current status. The evidence used here does not supply current status for named deployments, so no such status is asserted.

Finally, keep an architecture finding narrow. Confirming an optimistic challenge design or a validity-proof design does not establish a network’s fees, speed, availability, or complete security. Readers can use the categories to understand how examples differ, then investigate those separate operational questions with current, network-specific evidence. That approach makes “Layer 2” a useful starting classification without treating it as a guarantee.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Optimistic rollups](https://ethereum.org/developers/docs/scaling/optimistic-rollups/) — ethereum.org; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
- [Bridges](https://ethereum.org/developers/docs/bridges) — ethereum.org; retrieved 2026-10-18.
