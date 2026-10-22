---
title: "Layer 2 blockchain: architecture, transaction flow, and trade-offs"
description: "Learn how a layer 2 blockchain processes activity alongside an underlying chain, how data or proofs support settlement, and which trade-offs matter."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: []
author: "editorial_team"
primary_keyword: "layer 2 blockchain"
owned_question: "What is a layer 2 blockchain, how does it interact with its underlying layer, and what trade-offs shape its scaling approach?"
risk_level: "medium"
---

A Layer 2 blockchain is a system that handles some activity outside an underlying blockchain’s direct execution path while relying on that underlying chain for specified functions. In a rollup, for example, transactions execute separately and information is posted to the base layer; the exact information and the role it plays vary by design. “Layer 2” is not one uniform architecture, nor does the label alone establish performance or security properties.

## What the term layer 2 blockchain means

An **underlying blockchain** is the network a Layer 2 is designed to rely on for particular functions. In common crypto usage, “Layer 1” refers to the base blockchain network and its protocol, although the term is not a separately standardized technical category. A rollup is one architecture in which transaction execution is separated from the base layer while data is posted to the underlying chain. The relationship—not merely the label—determines what work happens on each layer and what the Layer 2 relies on the base chain to do.  [source](<https://ethereum.org/developers/docs/scaling/>)

A Layer 2 should not be treated as simply another independent Layer 1. The relevant distinction is whether the system is designed to rely on an underlying blockchain for specified functions, and what those functions are. In Ethereum’s terminology, a Layer 2 derives some of its security from Ethereum’s Layer 1 consensus rather than operating only under a separate validator set. The exact guarantee depends on the system’s proof, data-availability, settlement, governance, and exit mechanisms. This is a conditional description, not a claim that every system using the Layer 2 label has the same relationship.

The label also does not settle how data is handled. Rollups differ in proof systems, data formats, sequencing, upgrades, and bridge design. In L2BEAT’s terminology, a rollup uses a Layer 1 for consensus and data availability, while systems that publish data elsewhere add external data-availability assumptions and are classified differently. Architecture matters more than terminology alone. [source](<https://l2beat.com/glossary>)

## Follow a transaction from execution to settlement

A useful conceptual flow is: a user initiates activity, a Layer 2 processes it, and the system publishes information to its underlying chain. That outline describes a relationship, not a fixed procedure shared by every design. A rollup separates transaction execution from the base layer and posts transaction data or commitments there, so batches can use the base layer for consensus and settlement. Publication formats and proof designs differ; this description does not establish a universal order, timing, or outcome.

**Execution** is the processing of transactions and associated state changes. **Settlement** refers here to the base layer’s role in establishing or resolving the published record under the system’s design. These are distinct functions: the underlying chain can establish a record of posted information without itself executing every Layer 2 transaction. The rollup architecture describes that separation, but the actual settlement role and its conditions must be checked for the particular system. [source](<https://ethereum.org/developers/docs/scaling/>)

What gets posted can also differ. Some systems publish transaction data; others may publish commitments or summaries of state changes, with proofs or other mechanisms supporting the claimed result. A commitment is a concise reference to information or a state claim, not the full transaction history itself. The source documentation for any specific system is needed to identify its publication format and how that information supports verification. This explanation does not assume a single sequence in which every user transaction is immediately posted or settled.

## Where the underlying blockchain fits

A rollup can use the base chain for consensus and data availability while carrying out execution separately. **Data availability** means that the information needed to inspect or verify the published record is available under the design’s stated assumptions. Consensus concerns how participants agree on the chain’s accepted record. These functions are related but not interchangeable: a chain’s role in recording a publication does not, by itself, explain how transaction execution is checked or whether all required data is available.

The underlying chain may also be part of settlement, verification, or dispute handling, but these roles should not be assumed from the word “Layer 2.” The broad rollup model supports the distinction between off-base-layer execution and information posted to the base layer; it does not specify a universal proof or challenge method. Documentation for a particular protocol must establish which function the underlying chain performs and what the system relies on elsewhere.

For comparison, the modular blockchain model separates execution, settlement, consensus, and data availability into functions that can be assigned to specialized layers. That is a useful way to ask what each component does, not a claim that every Layer 2 uses the same modular architecture or assigns every function to a separate component.

## Scaling benefits and architectural trade-offs

The general rationale is to organize some activity outside the underlying chain’s direct execution path while still using that chain for defined roles. The intended design goal of blockchain scaling work is to increase transaction speed and throughput without sacrificing decentralization or security. This is a design objective, not evidence that a particular Layer 2 achieves a fixed improvement or preserves every property of its underlying chain.

Separating execution from publication can add dependencies and coordination points. The system relies on the components that perform its off-chain or Layer 2 processing and on the underlying chain for the functions assigned to it. If transaction data is published elsewhere, the system also has external data-availability assumptions. Rollups differ in sequencing, proof systems, data formats, upgrades, and bridge design, so neither the trade-offs nor the resulting guarantees can be inferred from a category name. [source](<https://l2beat.com/glossary>)

A monolithic architecture performs execution, settlement, consensus, and data availability together at a base layer; a modular stack can assign those functions to specialized layers. This distinction helps frame the design question: which functions remain together, which are separated, and what dependencies follow? It does not show that one arrangement is universally preferable. [source](<https://docs.celestia.org/learn/celestia-101/data-availability/>)

No fixed throughput, lower fee, availability level, or security equivalence follows from the general architecture. Rollup publication formats and proof designs differ, and lower fees or higher throughput are not guaranteed for every transaction or operating condition. Such claims require current, system-specific evidence rather than an inference from the term Layer 2.

## Security, withdrawals, and user responsibilities

Security cannot be evaluated from the Layer 2 label alone. For Ethereum Layer 2 systems, the amount and kind of security derived from Layer 1 depend on the specific proof, data-availability, settlement, governance, and exit mechanisms. Rollups also differ in sequencing, proof design, upgrades, data publication, and bridge arrangements. A general architecture description therefore cannot establish whether a particular system’s funds are recoverable, how withdrawals work, or what happens during a failure.  [source](<https://ethereum.org/developers/docs/scaling/>) [source](<https://l2beat.com/glossary>)

Separate the protocol’s documented behavior from the services surrounding it. A protocol’s architecture does not establish how a particular wallet or application presents an action, or how an external service handles access. Likewise, a user should not infer an exit path, recovery procedure, or upgrade authority from the Layer 2 designation. Those claims require system-specific technical documentation. No guarantee of access or recovery is implied here.

## Questions to ask when assessing a Layer 2 design

A focused technical review can start with these questions:

- **What executes transactions?** Identify the component that processes activity and updates the relevant state.
- **What information reaches the underlying chain?** Check whether documentation specifies transaction data, commitments, summaries, or another publication format.
- **What does the underlying chain do?** Separate its documented role in consensus, data availability, verification, dispute handling, or settlement; do not assume it performs all of them.
- **Where is data available?** Determine whether the design relies on the underlying chain for data availability or introduces an external assumption.
- **How are correctness and disputes addressed?** Find the system’s documented proof or dispute mechanism instead of inferring one from the rollup label.
- **What are the operational assumptions?** Review system-specific documentation for sequencing, upgrades, bridges, withdrawal paths, and stated failure assumptions.

These questions identify what the architecture claims and where evidence is still needed; they do not rank systems or recommend one. Fees, yields, availability, regulation, tax, and compliance are separate matters that require current, system- and context-specific evidence. The core assessment remains the transaction flow: what executes away from the base layer, what is published, and what the underlying chain is actually relied on to do.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
