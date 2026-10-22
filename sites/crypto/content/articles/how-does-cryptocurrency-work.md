---
title: "How does cryptocurrency work: transactions, validation, and consensus"
description: "Learn how does cryptocurrency work, from transaction submission and network validation to consensus and ledger updates, with proof-of-work and proof-of-stake basics."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["mining_consensus"]
tags: ["cryptocurrency work"]
author: "editorial_team"
primary_keyword: "how does cryptocurrency work"
owned_question: "How does cryptocurrency work from transaction submission through network validation and ledger updates, and how do consensus mechanisms differ?"
risk_level: "medium"
---

Cryptocurrency works through network-specific software rules that check submitted transactions, coordinate ledger updates, and record accepted changes. Validation and consensus are separate: validation checks whether a transaction or update follows the protocol, while consensus helps participants agree on which update to recognize. The details differ by network, so no single transaction path or finality signal applies to every cryptocurrency.

## What a cryptocurrency network records

A blockchain is one form of shared ledger. In Ethereum, each block cryptographically references its parent block, creating an ordered chain of network state. Other networks can use different data structures and consensus rules, so this Ethereum example should not be treated as a universal specification. [source](<https://ethereum.org/developers/docs/intro-to-ethereum/>)

It helps to distinguish three things. The protocol is the set of rules that defines acceptable network behavior. The ledger is the history or state maintained under those rules. Nodes are software participants that communicate with the network and perform roles specified by the protocol. The network’s native asset, when it has one, is not the protocol itself: it is represented and handled according to that network’s rules.

The precise division of work among nodes varies. In Ethereum, a full node independently verifies blocks and transactions against protocol rules rather than relying entirely on another node. That statement describes Ethereum’s full-node role; it does not establish that every cryptocurrency has the same node types or verification requirements. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)

## How does cryptocurrency work when a transaction is sent?

A transaction begins with an instruction prepared for a network, often through a wallet or another application. The application submits it to network software. The transaction must satisfy the protocol’s requirements before it can be accepted as part of a ledger update. The specific requirements depend on the network and transaction; this overview does not assume one universal format or signing workflow.

Once software receives a transaction, it can check the transaction according to the applicable rules. For example, Ethereum full nodes independently verify transactions and blocks against protocol rules. This is a protocol-facing check; it is distinct from whether an application displays a transaction as pending, or whether another service chooses to present or relay it. [source](<https://ethereum.org/developers/docs/nodes-and-clients/>)

Bitcoin illustrates how peer-to-peer communication can support transaction propagation. Bitcoin full nodes use a peer-to-peer protocol to exchange transactions and blocks and synchronize validated chain data. This describes Bitcoin’s network operation, not the exact relay behavior of all cryptocurrencies. [source](<https://developer.bitcoin.org/devguide/p2p_network.html>)

In Bitcoin, a node generally relays a received transaction after checking that it meets applicable validity and relay-policy rules. Node policies can differ, and a transaction accepted or relayed by one node is not necessarily accepted into every node’s local transaction pool. Relay is therefore not the same as ledger inclusion.

A transaction may consequently be visible to network software before it is recorded in an accepted ledger update. Bitcoin’s mempool—the node’s local collection of pending transactions—does not give a transaction permanent ledger status. Nodes can drop, replace, or later re-accept transactions according to their state and policies. This is a Bitcoin-specific example of the distinction between propagation and recording.

## How nodes validate and agree on ledger updates

Validation asks whether a proposed transaction or block follows the rules of a particular protocol. Consensus addresses a different question: how network participants coordinate which valid update becomes part of the shared history. A consensus mechanism does not make an invalid update valid; participants still apply their network’s validity rules.

Ethereum provides a concrete example of block validation. When an Ethereum node receives a proposed block, it checks the block and re-executes its transactions to verify the resulting state change before accepting it. That describes this Ethereum processing step, while other networks may define different checks and node roles. [source](<https://ethereum.org/developers/docs/blocks/>)

After checks, the protocol’s consensus rules determine how participants coordinate on ledger updates. The mechanics and the meaning of a confirmed or finalized update are network-specific. The allowed evidence does not support one universal number of confirmations, one common finality model, or a claim that every network resolves competing updates in the same way.

## Proof of work and proof of stake at a high level

Proof of work and proof of stake describe different approaches to organizing participation in consensus. They do not, by themselves, describe every validation rule, communication step, or feature of a cryptocurrency network.

Bitcoin is a proof-of-work example. Its full-node and peer-to-peer operations are part of a larger protocol: nodes exchange chain data, independently apply rules, and use the network’s consensus design. The process should not be generalized to networks that use different consensus approaches. [source](<https://developer.bitcoin.org/devguide/p2p_network.html>)

Proof of stake is another broad category, but the allowed evidence here does not establish a protocol-specific description of its participation, selection, or finality rules. Those details must be checked against documentation for the particular network. In either case, the labels “proof of work” and “proof of stake” are not a substitute for examining transaction validation and the rest of the protocol.

This bounded comparison also does not show that one approach is universally safer, faster, cheaper, or more decentralized. Those conclusions would require evidence about a specific protocol and the conditions being compared.

## What changes after a transaction is recorded

When a transaction is included in an accepted ledger update, the network’s recorded history or state changes according to its rules. What a user sees depends on the network and the application presenting that information. For Bitcoin, a transaction in a node’s mempool has no permanent ledger status until it is included in a valid block on the accepted chain; nodes may also drop, replace, or later re-accept pending transactions.

Applications may show inclusion, confirmations, or other protocol-specific status signals. Those signals do not have one universal interpretation across networks. The technical status of a transaction in a ledger should also be kept distinct from legal settlement, reversibility, or guaranteed recovery: this overview does not establish any of those outcomes.

## What varies across cryptocurrency networks

To understand a particular cryptocurrency, check its own documentation for the transaction rules, the node roles that apply them, the consensus process that coordinates ledger updates, and the network’s description of confirmation or finality. Ethereum’s block re-execution and Bitcoin’s peer-to-peer relay are examples from specific networks, not interchangeable descriptions of all cryptocurrencies. [source](<https://ethereum.org/developers/docs/blocks/>) [source](<https://developer.bitcoin.org/devguide/p2p_network.html>)

Other protocol characteristics likewise cannot be inferred from the general lifecycle. Fees, transaction capacity, security assumptions, and availability require evidence tied to the specific network and relevant timeframe. Keeping transaction submission, validation, consensus, and ledger recording separate provides a practical way to read protocol documentation without assuming that every network works identically.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [P2P Network](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin Developer Documentation; retrieved 2026-10-18.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
- [Nodes and Clients](https://ethereum.org/developers/docs/nodes-and-clients/) — ethereum.org; retrieved 2026-10-18.
