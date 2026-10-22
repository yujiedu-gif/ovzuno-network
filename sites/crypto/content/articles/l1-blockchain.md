---
title: "L1 blockchain: its role in blockchain architecture"
description: "Learn what an l1 blockchain is, which core functions it may provide, and how it fits into blockchain architecture without conflating it with scaling layers."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_scaling"]
tags: ["1 blockchain"]
author: "editorial_team"
primary_keyword: "l1 blockchain"
owned_question: "What is an L1 blockchain, what functions does it perform, and how does it relate to other blockchain layers?"
risk_level: "medium"
---

An **L1 blockchain**, or **Layer 1 blockchain**, is the foundational blockchain layer in an architecture: the base network that maintains a ledger and applies its own protocol rules. “L1” describes an architectural role, not a single technical design. It does not, by itself, specify how a network reaches agreement, processes transactions, handles data, or relates to additional layers. Those details must be established from documentation about the particular network.

## What an L1 blockchain means

“Layer 1” is commonly used to refer to a base blockchain network and its protocol. It is a useful shorthand for discussing where a system’s foundational ledger and protocol sit in a larger architecture, but it is not a separately standardized technical category with one universal definition. The term therefore needs context: a writer or project may use it to distinguish a base network from additional systems, while the label alone does not describe the network’s complete technical structure. [Claim: `claim_09800d602e84223528e0`]

A blockchain can be understood as a shared database maintained across networked computers. Blocks cryptographically reference earlier blocks, and nodes use consensus to agree on state. This general description provides a starting point, not a complete specification: blockchain designs differ in who may participate, which consensus rules apply, what data is visible, how finality works, and whether the network supports execution. [Claim: `claim_blockchain_shared_database`]

The L1 designation is also not the name of a particular coin or token. It identifies a network’s architectural position, while the network’s own protocol defines its components and operation. In particular, the term does not say that all L1 networks are open to the same participants, use the same consensus model, or combine the same functions. [Claim: `claim_nist_permission_models`]

## Core functions an L1 may provide

At a high level, an L1 protocol establishes how proposed transactions or other state changes are handled and how a shared network state is recognized. The precise sequence and mechanisms vary by network. Ethereum provides one specific example: Ethereum nodes use a consensus mechanism to agree on new blocks and the continuing chain. That statement describes Ethereum’s architecture; it is not a universal rule for every network called an L1. [Claim: `claim_eth_nodes_consensus`]

Some architecture discussions distinguish four functions: **execution**, **settlement**, **consensus**, and **data availability**. Execution processes transactions under a system’s rules. Consensus is the mechanism for agreeing on the accepted record or state. Settlement concerns establishing relevant changes on a base layer. Data availability concerns the handling and publication of data needed by participants to inspect or verify changes. These terms help map a system, but there is no requirement that every network implement them in the same way or use identical boundaries.

One architectural model places execution, settlement, consensus, and data availability together in a monolithic base layer. A modular architecture can assign those functions to specialized layers instead. These are patterns for describing architecture, not performance ratings and not a statement that every real deployment fits neatly into one category. A system may combine or separate functions according to its design. [Claim: `claim_integrated_separated`]

This distinction matters when reading a network description. The word “L1” does not prove that every transaction is executed on the base layer, that all relevant data is published there, or that a single component handles every protocol responsibility. Ask which function the document is discussing and which network or component performs it. If documentation describes a function without explaining its placement, the general L1 label does not fill in that missing detail.

Network-specific examples should remain scoped. Ethereum documentation describes Ethereum’s nodes and consensus. Hyperledger Fabric, by contrast, documents a permissioned-network model coordinating organizations, certificate authorities, peers, orderers, channels, policies, ledgers, smart contracts, and client applications. Fabric is an example of one permissioned architecture, not a basis for assuming that all L1 networks share its organization or roles. [Claim: `claim_fabric_component_roles`]

## How an L1 blockchain fits with other layers

An L1 can serve as the base of an architecture that also includes other systems. Those systems may build on or interact with the base network, and their responsibilities can differ from the responsibilities assigned to the L1. The relationship is specific to the architecture; “another layer” does not automatically mean one fixed design or one set of guarantees.

A rollup is one documented example in Ethereum’s scaling architecture. It separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. This describes the cited rollup pattern. It should not be generalized to every secondary system or treated as a complete survey of scaling designs. [Claim: `claim_rollup_separation`]

Data placement is one useful question when mapping that relationship. In L2BEAT’s terminology, a rollup uses an L1 for consensus and data availability; systems that publish data elsewhere add external data-availability assumptions and are classified differently. Because industry usage of “L2” is not fully uniform, the architecture is more informative than the label by itself. [Claim: `claim_rollup_vs_external_da`]

For a reader trying to understand a particular network, the practical task is to trace which layer performs each function and what the documented connection is. Do not assume that a system inherits the same security or settlement properties merely because it interacts with an L1. The specific architecture needs to establish those properties; the general term does not.

## What the L1 label does not tell you

The label alone does not establish transaction speed, fees, decentralization, or security. It does not specify whether execution, settlement, consensus, and data availability are combined or divided among layers. The monolithic and modular models show why a broad architectural label cannot substitute for a network’s technical description. [Claim: `claim_integrated_separated`]

Nor does the term establish legal or tax treatment, availability in a particular location, or suitability for a particular purpose. Those questions require relevant evidence about the network, activity, and jurisdiction. No such conclusion follows from calling a network an L1.

A claim about an L1 should therefore be read with its subject and scope intact. A statement about Ethereum consensus is not automatically a statement about another blockchain. A description of one permissioned design does not establish that all permissioned or base-layer networks use the same roles. An architectural category can orient a discussion, but it cannot replace an implementation-specific explanation.

## Questions to ask about a specific L1

When examining a named network, use primary technical documentation to answer the questions the label leaves open:

- **Consensus and state updates:** What documented rules govern agreement on new blocks or state changes? If a source describes a particular network, keep the description limited to that network.
- **Execution:** Where does the system process transactions, and which protocol rules govern that processing?
- **Data handling:** Where is relevant data handled or published, and which layer or component is responsible?
- **Architecture boundaries:** Are execution, settlement, consensus, and data availability performed together or assigned to specialized layers?
- **Scope of claims:** Does a statement describe the protocol, a separate system, or one named implementation? Do not extend it to other networks without evidence.
- **Evidence for other assertions:** Claims about fees, availability, security, recovery, regulation, tax, or compliance require evidence that addresses the relevant network and circumstances; they cannot be inferred from “L1.”

This is an architecture-reading checklist, not a comparison or recommendation. The L1 designation identifies a commonly used base-layer role. To understand what a specific network actually does, follow its documented protocol and identify where each function is assigned, while keeping network-specific facts separate from general terminology.

## Sources and references

- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Celestia's data availability layer](https://docs.celestia.org/learn/celestia-101/data-availability/) — Celestia Documentation; retrieved 2026-10-19.
- [Glossary](https://l2beat.com/glossary) — L2BEAT; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [How Fabric networks are structured](https://hyperledger-fabric.readthedocs.io/en/latest/network/network.html) — Hyperledger Fabric Documentation; retrieved 2026-10-19.
