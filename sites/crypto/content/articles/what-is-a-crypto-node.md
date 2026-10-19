---
title: "What Is a Crypto Node? Full, Archive, Light, and Validator Roles"
description: "Learn what blockchain nodes verify, store, and relay, and how full nodes, archive nodes, light clients, miners, and validators differ."
date: "2026-10-18"
draft: false
content_type: "definition"
topics: ["blockchain-foundations"]
tags: ["what is a crypto node", "blockchain node", "full node", "archive node", "light client"]
author: "editorial_team"
primary_keyword: "crypto node"
owned_question: "What is a crypto node, and what does it verify, store, relay, or propose?"
risk_level: "low"
---

A crypto node is a computer process running software that participates in a blockchain network. It connects to peers, follows the network's protocol rules, and performs a configured combination of verifying, storing, relaying, or serving blockchain data. Some nodes also help produce or finalize blocks, but that is a separate role rather than a property of every node.

The word node is broad. A phone using a light client, a server maintaining current state, an archive system answering historical queries, and a validator proposing blocks can all be nodes, yet they provide different guarantees and require different resources.

## A node is a running protocol participant

A blockchain protocol is a set of rules. A **client** is software that implements those rules, while a **node** is a running instance of that software connected to the network. Multiple client implementations may follow the same protocol.

When a node receives a transaction or block, it does not accept it merely because a peer sent it. Its client applies the checks appropriate to its role: transaction format and signatures, spending or account rules, block structure, state transitions, consensus conditions, and links to prior blocks. Valid data can be stored and relayed to other peers; invalid data is rejected.

This local rule enforcement is a central property of public blockchains. Nodes can reach compatible results without relying on one central database operator, provided they follow the same protocol and receive the necessary data.

## What a node can do

A node's functions may include:

- **Verify:** check transactions, blocks, state transitions, proofs, and consensus data against protocol rules.
- **Store:** retain current state, blocks, transactions, receipts, indexes, or historical state according to configuration.
- **Relay:** send valid transactions and blocks to connected peers.
- **Serve:** answer peer requests or expose an RPC interface used by wallets, applications, explorers, and internal systems.
- **Propose or attest:** participate in consensus or block production when separate eligibility, keys, stake, or mining work is configured.

A node does not necessarily perform all five functions. A pruned node can fully validate current chain data while discarding older data. A private RPC node may serve only approved applications. A validator may depend on full-node components but add signing duties and protected keys.

## Full, archive, and light nodes

A **full node** validates blocks and relevant state changes according to the protocol. Full refers primarily to validation, not permanent storage of every historical database state. For example, Ethereum full nodes can retain current and recent state while pruning older intermediate states. Bitcoin full nodes may also be configured to prune old block files after validation.

An **archive node** performs full validation and additionally retains or indexes historical states. That makes questions such as an account or contract's state at an old block faster to answer. Explorers, analysts, auditors, and data services may need this capability. The network normally does not require every participant to keep an archive, and archive storage does not give a node extra consensus authority.

A **light client** downloads much less data. It typically follows block headers or consensus updates and requests transactions, proofs, or state data from full nodes or providers. Bitcoin's simplified payment verification model uses headers plus a Merkle branch to check that a transaction is included in a block. This is useful, but it does not reproduce every check made by a full node. Light-client guarantees depend on the protocol, proof design, sync starting point, and the data sources available.

Names are not perfectly portable between chains. One network's light client may verify cryptographic state proofs; another product marketed as light may mostly forward requests to a remote RPC service. The latter shifts more trust and privacy to the provider.

## A node is not automatically a miner or validator

A full node verifies the chain it receives. A **miner** or **validator** performs an additional consensus or block-production role.

In proof-of-work systems, miners assemble candidate blocks and perform the required computation. Full nodes independently decide whether a mined block obeys the rules. A machine may run mining and full-node software together, but mining is not required to validate.

In proof-of-stake systems, validators may propose blocks or attest to chain state using staking credentials. Ethereum explicitly separates its execution and consensus clients from validator software. A node can follow and verify the network without operating a validator, while a validator needs the node components required to understand the chain and submit valid consensus messages.

This distinction matters operationally. Consensus keys may create slashing or financial risk and demand stricter availability and key controls. An ordinary full node has no equivalent signing duty merely because it is online.

## How applications use nodes

Wallets and applications communicate with nodes through interfaces such as JSON-RPC. A node can return balances, contract state, transaction receipts, fee data, or new blocks; simulate transactions; and broadcast signed transactions. The wallet holds or uses the signing key, while the node supplies network data and transport.

Using a third-party RPC endpoint is convenient, but the application depends on that operator's availability, data integrity, rate limits, chain view, logging, and privacy practices. Running an owned node can provide independent verification and reduce data exposure, although it adds synchronization, monitoring, patching, backup, capacity, and incident-response work.

Explorers and analytics systems often need additional indexes beyond a normal node. Payment systems may operate several nodes or providers, compare results, wait for defined confirmation conditions, and separate broadcast infrastructure from accounting. Those controls are application architecture, not automatic node features.

## Questions for choosing a node setup

Start with the required guarantee and workload:

- Must the system independently validate data, or is a remote provider acceptable?
- Is current state enough, or are frequent historical-state queries required?
- Which transactions, blocks, receipts, traces, logs, or proofs must be available?
- Does the workload need public RPC, private RPC, peer service, indexing, or consensus participation?
- Which sync checkpoints, client implementations, or providers are trusted?
- What uptime, latency, privacy, geographic, and recovery requirements apply?
- How will client updates, disk growth, corruption, forks, reorganization, and monitoring be handled?
- If validator or miner duties are added, how are keys and failure penalties isolated?

A crypto node is not simply a copy of a blockchain and not automatically a revenue-producing machine. It is a running protocol participant whose real function is defined by what it verifies, retains, relays, serves, or signs. Identifying those functions is the reliable way to compare node types and design infrastructure.

## Sources and references

- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients) — ethereum.org; retrieved 2026-10-18.
- [Ethereum Archive Node](https://ethereum.org/developers/docs/nodes-and-clients/archive-nodes) — ethereum.org; retrieved 2026-10-18.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Satoshi Nakamoto via bitcoin.org; retrieved 2026-10-18.
- [P2P Network](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin Developer Documentation; retrieved 2026-10-18.
