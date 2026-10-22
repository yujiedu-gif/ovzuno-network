---
title: "List of blockchain protocols: roles, designs, and examples"
description: "Explore a list of blockchain protocols grouped by role and design, with a neutral framework for distinguishing networks without ranking them."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["blockchain protocols list", "list blockchain protocols"]
author: "editorial_team"
primary_keyword: "list of blockchain protocols"
owned_question: "What are examples of blockchain protocols, and how can they be grouped by their design and intended function?"
risk_level: "medium"
---

Blockchain protocols are the rules and mechanisms that coordinate a network’s ledger, participation, and state updates. The evidence available for this guide supports a focused list rather than a broad inventory: Ethereum as a base network, and rollups as systems that separate transaction execution from the base layer while posting data to Ethereum. These examples illustrate different architectural roles, not a ranking of protocols.

## What counts as a blockchain protocol?

A blockchain protocol is the set of network rules that governs how participants coordinate the ledger and its updates. The examples here are limited to what the authorized evidence establishes: Ethereum nodes use a consensus mechanism to agree on new blocks and the continuing chain, while rollups separate transaction execution from the base layer and post data to Ethereum. Those descriptions identify network and system roles; they do not justify treating every blockchain-related product as a protocol.

A **node** is a running instance of protocol client software connected to other peers. Its behavior depends on the client it runs and its configured mode. The distinction matters because a network protocol and the software implementing it are related but not interchangeable: one describes rules, while the other is a particular implementation operating under those rules.

A **rollup**, as used in this guide, is a system that separates transaction execution from the base layer while posting data to Ethereum, where base-layer consensus establishes the published record. It is therefore useful to describe a rollup in relation to Ethereum rather than treating the word as another name for Ethereum itself. The categories below are an editorial organization of these roles, not a claim that every blockchain architecture fits into one universal taxonomy.

## How to compare blockchain protocols

A practical comparison starts by asking what role a system performs and which network or layer supplies each function. For the two examples supported here, the most useful attributes are the relationship to consensus and the location of execution and data publication.

- **Consensus relationship:** Ethereum nodes use consensus to agree on new blocks and the continuing chain. In the rollup architecture described here, data is posted to Ethereum, where base-layer consensus establishes the published record.
- **Execution location:** A rollup separates transaction execution from Ethereum’s base layer. This is an architectural distinction, not a measured claim about speed, cost, or transaction capacity.
- **Implementation:** A node runs protocol client software, and the client and its configured mode shape node behavior. This is separate from the network’s role or the architecture of a system built around it.

Consensus is the mechanism by which network participants agree on new blocks and the continuing chain. Execution location answers a different question: where a system carries out transaction processing relative to the base layer. Keeping those questions separate avoids comparing a base network and a system built around it as though they necessarily served the same function.

Design attributes should not be mistaken for measured outcomes. For example, the fact that a rollup posts data to Ethereum does not, by itself, establish its complete security properties or performance. Likewise, the potential benefit of client diversity does not prove that a specific network currently has a particular distribution of clients. A useful comparison records what the design description says, then separately identifies any outcome that requires current, independent evidence.

## List of blockchain protocols by role

This is a deliberately short, non-ranked catalog. It includes only the examples supported by the evidence authorized for this article. It does not attempt to provide an exhaustive list of payment networks, application platforms, or other blockchain systems.

### Base network: Ethereum

Ethereum is the base network in the examples covered here. Its nodes use a consensus mechanism to agree on new blocks and the continuing chain. That describes a network-level function. It does not make claims here about fees, transaction speed, availability, adoption, or comparative security.

When examining Ethereum’s implementation, distinguish the network from the client software run by nodes. Each node is an instance of client software connected to peers, and its behavior depends on its client and configured mode. Independently maintained Ethereum clients can reduce dependence on a single codebase and the potential network-wide impact of a bug or attack against a dominant implementation. This describes a possible architectural benefit of diversity, not the current degree of diversity or a complete measure of security.

The distinction also helps define what a list entry can tell a reader. “Ethereum” identifies the network in this catalog; “client” identifies software used to participate in that network. The available evidence does not support an inventory of client implementations or a claim about their current share of network use, so those details are not included.

### Execution layer built around Ethereum: rollups

Rollups are grouped here by their relationship to Ethereum, not as another base-network category. The architecture described in the evidence separates transaction execution from the base layer and posts data to Ethereum, where base-layer consensus establishes the published record. The location of execution and the destination for published data are the distinguishing attributes in this entry.

This description is intentionally limited. It does not establish that every system called a rollup uses an identical implementation, or that the category alone proves a particular security or performance result. Nor does it support conclusions about costs, throughput, availability, withdrawals, or recovery. Those properties would require separate, current evidence about the specific system and its implementation.

The entries are not mutually exclusive classifications of every possible blockchain system. They are a compact way to distinguish the base-network role represented by Ethereum from the execution-and-data-publication role represented by rollups. A reader comparing two systems can use the same questions—what is the base network, where does execution take place, and where is data published—without assuming that the answers establish which system is preferable.

## How protocol designs differ

These examples show why “protocol” does not describe just one architectural layer. Ethereum is described here as a network whose nodes use consensus to agree on blocks and the continuing chain. Rollups are described by how they divide execution from the base layer and publish data to Ethereum. The first description concerns agreement on network history; the second concerns how a system’s execution and data publication relate to that base network.

A further distinction is between a design property and an observed outcome. Client diversity can reduce dependence on one codebase, but that does not demonstrate that a particular deployment has broad client diversity. Posting data to Ethereum is part of the rollup model described here, but that single architectural fact is not enough to make a complete security judgment. A comparison should state the evidenced design clearly and leave unverified outcomes open.

Descriptions also need a time reference when protocol designs have changed. Ethereum previously used proof of work. In that design, finality was probabilistic: simultaneous valid blocks could create temporary forks, and later blocks increased confidence in one history. The evidence states that Ethereum switched to proof of stake in 2022 and no longer uses proof of work. The historical example illustrates why older descriptions should not be presented as though they necessarily characterize the current design.

These distinctions provide a neutral comparison framework without creating a score. A reader can classify an example by its role, note the consensus relationship described, and identify where execution and data publication occur. Claims about measured performance, security, or suitability are different kinds of claims and need their own evidence. Nothing in these categories supplies a universal ranking.

## Limits of a protocol list

This catalog includes only Ethereum and rollups in relation to Ethereum because those are the examples supported by the evidence authorized for this guide. It is not exhaustive. In particular, the available evidence does not justify adding a broad set of payment-focused networks or other smart-contract platforms, so the article does not name them. The categories are an editorial aid rather than a permanent or universal classification scheme.

Protocol descriptions and implementations can change. Before using a list for research or infrastructure planning, verify current protocol documentation and seek independent technical evidence for the attributes relevant to the decision. Confirm that a source is describing the network, a client implementation, or a system built around a network; otherwise, unlike layers or roles can be accidentally compared as if they were equivalent.

A category label alone does not establish performance, fees, availability, security, recovery, adoption, or suitability. Those questions require current, protocol-specific evidence and are outside the claims made in this reference guide. The list is therefore a starting framework for distinguishing roles and design descriptions—not a substitute for evaluating a particular implementation or operational requirement.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Client Diversity](https://ethereum.org/developers/docs/nodes-and-clients/client-diversity/) — ethereum.org; retrieved 2026-10-18.
- [Scaling](https://ethereum.org/developers/docs/scaling/) — ethereum.org; retrieved 2026-10-19.
- [Proof-of-Work](https://ethereum.org/developers/docs/consensus-mechanisms/pow) — ethereum.org; retrieved 2026-10-19.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients) — ethereum.org; retrieved 2026-10-18.
