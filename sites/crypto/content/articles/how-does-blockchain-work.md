---
title: "How Does Blockchain Work? From Transaction to Shared Ledger"
description: "Learn how does blockchain work as a transaction moves through network checks, consensus, and ledger updates, and why processes vary across chains."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["blockchain work"]
author: "editorial_team"
primary_keyword: "how does blockchain work"
owned_question: "How does a blockchain process a transaction, reach agreement on its validity, and add it to a shared ledger?"
risk_level: "medium"
---

A blockchain processes a transaction by receiving a proposed instruction, checking it against network rules, and recording it through the network’s consensus process. The exact checks and agreement mechanism vary by blockchain. A transaction’s submission—or even its inclusion in a block—does not mean every network treats it as final at the same point.

## The transaction lifecycle at a glance

A common process can be summarized as: a user or application creates and signs an instruction; it is broadcast to the network; participants check it; the protocol orders and includes accepted transactions in a ledger update; and later network activity or protocol rules determine how settled that update is. This is a general model, not a universal sequence shared in identical form by all chains.

The stages answer different questions. Signing concerns authorization. Validation concerns whether an instruction meets the applicable rules. Consensus concerns which ledger update becomes part of the shared history. Inclusion means the transaction is recorded in a block or equivalent update. Confirmation and finality describe how the network treats that recorded history afterward, with meanings that depend on the protocol.

## How a transaction reaches the blockchain network

A transaction is an instruction that proposes a change to network state. Depending on the system, it may represent a payment or request an operation. The user or application authorizes the instruction using a cryptographic signature, then submits it to the network through a connected service or participant. A signed transaction can still fail later checks or remain unrecorded; signing does not itself update the ledger.

For Bitcoin, transactions can wait in a mempool, a node’s temporary holding area for transactions not yet included in a valid block on the accepted chain. Mempool status is not permanent ledger status: nodes maintain local mempools and can drop, replace, or later re-accept transactions under their state and policies. This Bitcoin example should not be treated as evidence that every blockchain uses a mempool or manages pending transactions the same way.

Broadcast is also distinct from settlement. It means an instruction has been submitted for network handling, not that it has been accepted into the ledger. For an operator or application, the useful distinction is between a submitted transaction and a transaction whose status has been established under the relevant network’s rules.

## How nodes validate proposed transactions

Validation is the rule-checking step. A network participant checks whether a proposed transaction is acceptable under the protocol—for example, whether its authorization is valid and whether the requested change is permitted. The specific data format and conditions differ by chain, so there is no single universal checklist to apply to every transaction.

In Ethereum’s block-processing model, a node receiving a proposed block checks the block and re-executes its transactions to verify the resulting state change before accepting it. This illustrates that validation can include checking the result of execution, not merely recognizing that a transaction was signed. Other networks use their own validation procedures and data models.

Validity and inclusion are separate. Passing applicable checks means a transaction may be eligible for processing; it does not, by itself, establish that the network has ordered it into the shared ledger. A transaction can therefore be valid yet still be waiting for the next step, depending on the chain’s process.

## How blockchain consensus determines ordering and inclusion

Consensus is the protocol process for accepting ledger updates and maintaining an agreed history. It operates alongside transaction validation: participants apply network rules, while the consensus mechanism determines which proposed update or history the network treats as accepted. These functions are related but not interchangeable. A consensus process does not make an invalid transaction valid.

Blockchains differ in how they produce and accept updates. Bitcoin, for example, adjusts its proof-of-work target after each 2,016-block difficulty period under its consensus rules. That is a network-specific mechanism, not a general rule for blockchain timing or transaction inclusion. The broad point is that block-production and agreement rules are defined by each protocol rather than by one shared procedure.

This explanation does not require every participant to communicate directly with every other participant. The relevant question is how the particular network propagates information and applies its rules to choose or accept a shared history. Competing histories and reorganizations are also protocol-specific; their detailed mechanics belong in a separate explanation of blockchain forks.

## What changes when a transaction is added to a block

When a transaction is included, it becomes part of a ledger update accepted under that network’s rules. In a blockchain, blocks reference earlier blocks, creating an ordered history. The ledger can be described as a database shared and updated across networked computers, with nodes using consensus to agree on state. The details of what a block contains are separate from its role in recording accepted transactions.

Inclusion is an important status change, but it is not automatically synonymous with finality across all networks. A protocol may treat later updates as relevant to how firmly an included transaction belongs to the accepted history. What an application or operator should report as complete therefore depends on the chain and the status information it provides.

## Why confirmation and finality vary by blockchain

Confirmation and finality are not universal labels with one shared threshold. A network’s protocol defines how it recognizes accepted updates and whether later activity can change the status of an earlier one. Bitcoin’s pending-transaction and block rules, for example, should not be used to infer the finality model of another chain.

For operational decisions, consult documentation for the specific network and the application’s own settlement policy. A transaction’s presence in a queue, its inclusion in a block, and a protocol-defined finalized state are distinct kinds of evidence. This article does not prescribe a number of confirmations or a universal completion threshold; the available evidence does not establish one that applies across blockchains.

## A worked transaction trace: from submission to ledger update

Consider this hypothetical, generic payment. It is an illustration only, not a report of an observed transaction, and it does not assume a specific blockchain.

1. **Creation and authorization:** A user or application prepares an instruction and signs it. At this point, the instruction has been authorized in a cryptographic sense, but network acceptance is not yet established.
2. **Submission:** The signed instruction is sent to a network participant. Submission shows that it was handed off for processing; it does not prove ledger inclusion.
3. **Validation:** Participants apply the relevant network rules. If the instruction does not satisfy them, it will not be accepted under those rules. If it passes, it may proceed, but it still needs ordering and inclusion.
4. **Ordering and inclusion:** The network’s consensus process determines how an update enters the accepted history. If the transaction is included, it is recorded as part of a ledger update.
5. **Later status:** The application or operator checks the status defined by that chain. Depending on the protocol, inclusion and the point considered final may be separate milestones. No universal threshold follows from this generic trace.

This sequence helps separate what is known at each stage from what remains conditional. A system might label an instruction pending before inclusion, included after a block records it, and finalized only when the relevant protocol condition is met. Those labels and their exact meanings must be established for the actual network and application, not assumed from this example.

## What this process explains—and what it does not

The process connects transaction authorization, network checks, consensus, and ledger updates. Its shared outline is useful, but implementation details—including pending-transaction handling and the meaning of finality—are chain-specific.

This is not a transaction-lookup guide, an explanation of anonymity, or a comparison of blockchain providers. For broader components, see the blockchain basics overview; for block structure, see the block-in-blockchain guide; and for lookup or fork mechanics, consult the dedicated explorer, address-lookup, and blockchain-forks resources.

## Sources and references

- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [P2P Network — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
