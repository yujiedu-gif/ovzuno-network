---
title: "Memory Pool Blockchain: How Pending Transactions Reach a Block"
description: "Learn how a memory pool blockchain handles pending transactions, why node views can differ, and what changes when a transaction is included in a block."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["mempool", "pending blockchain transactions", "transaction validation"]
author: "editorial_team"
primary_keyword: "memory pool blockchain"
owned_question: "What is a blockchain memory pool, and how can pending transactions move from a node’s mempool into a block?"
risk_level: "medium"
---

A blockchain memory pool, or **mempool**, is a node’s temporary holding area for transactions it has received but that have not yet been included in a block. A transaction can move from a local pending pool toward block inclusion when a block producer selects it and the network processes the proposed block, but the mempool is not one universal queue and pending status does not guarantee inclusion.

## What “memory pool blockchain” means

“Memory pool blockchain” is an informal phrase for the way a blockchain network handles transactions before block inclusion. **Mempool** is the more common term. Here, it means a node’s local view of pending transactions—not a shared list that every participant necessarily maintains in identical form.

That local pool is distinct from the blockchain’s recorded history. A transaction can be known to a node and still be waiting for inclusion. For Ethereum, a state-changing transaction is broadcast, selected for a block, executed, and may later gain stronger confirmation or finality. Its receipt can report failed execution even when the transaction was included. This illustrates why “pending,” “included,” and “successful” describe different points or results in a transaction’s lifecycle, rather than interchangeable labels. [1]

The boundaries of this explanation matter. “Mempool” does not specify one set of rules shared by all blockchains. Network protocols and node software determine what transactions are accepted, how they are shared, and what can happen to them before inclusion. A description of a specific chain should not be treated as a universal rule.

## How a transaction enters a node’s mempool

A node first receives a transaction, either from a connected peer or through another route provided by the network’s software. It evaluates the transaction according to the applicable protocol rules and its own configuration. If accepted, the transaction may appear in that node’s local pending view. The exact checks and policies depend on the network and implementation; the evidence here does not support one exhaustive admission checklist for every chain.

The important distinction is between **receipt**, **local acceptance**, and **block inclusion**. A node receiving a transaction does not mean the transaction has been added to the ledger. Likewise, acceptance into one node’s pool does not establish that every other node has received or accepted it. The Ethereum lifecycle provides a concrete example: broadcast comes before block selection and execution, which are separate stages. [1]

A node’s local pool is therefore not an approval issued by the entire network. Nor does local acceptance promise that a block producer will choose the transaction. The transaction still has to pass through the network’s block-processing path. The precise behavior—and the meaning of any node or application status label—must be checked against the relevant network and software rather than inferred from the word “mempool.”

## Why mempool contents differ between nodes

A transaction may reach different nodes at different times, and each node maintains its own view. Nodes can also have different configurations and policies. As a result, one node may show a transaction as pending while another does not show it. This difference does not, on its own, establish which node has a complete view or explain why the transaction is absent from one of them.

The Bitcoin network offers a specific illustration of temporary local status: a Bitcoin mempool transaction has no permanent ledger status until it is included in a valid block on the accepted chain. Nodes maintain local mempools and can drop, replace, or later re-accept transactions according to their state and policies. [2] Those details are Bitcoin-specific. They do not establish that another network uses the same pool rules, reasons for removal, or retention behavior.

For that reason, there is no basis here for assuming a universal retention period or a globally synchronized pending-transaction list. A node’s mempool is best understood as a snapshot of that node’s current local state. Its contents may differ from another node’s view, and those differences are subject to the network’s own rules and the node’s software and configuration.

## From pending transaction to block

A block producer can select transactions available to it when constructing a proposed block. Selection is not guaranteed simply because a transaction appears in one node’s pool. The producer’s available transactions and the applicable network rules determine what proceeds toward inclusion; selection criteria and block constraints are network-specific, not a universal mempool policy.

Once a transaction is selected and included, its status changes: it is no longer merely a transaction waiting in that node’s pool. Ethereum’s transaction lifecycle then includes execution and may include later confirmation or finality. But inclusion and successful execution remain distinct: an included Ethereum transaction can have a receipt reporting failed execution. [1] So block inclusion alone does not establish that the intended operation succeeded, and the broader lifecycle should not be assumed identical across networks.

A transaction that is not selected may remain in a node’s pending view or leave it, depending on the relevant network and implementation conditions. The Bitcoin example documents local pools that can change, but it does not establish a shared lifecycle or a fixed rule for every blockchain. [2] The general point is limited: temporary pool status precedes block inclusion, while the transition and the consequences of inclusion are governed by the particular network.

## What a mempool can—and cannot—tell you

A mempool view can tell you that a particular node currently lists a transaction as pending. By itself, it cannot show that every node has the same view, guarantee that a block producer will include the transaction, or establish that an included transaction will execute successfully. Conversely, absence from one node’s view alone does not establish that no other node has received or retained it.

Pending status also does not, by itself, explain why a transaction has not appeared in a block. A local pool is not a complete diagnosis of the network’s processing decisions. Determining what a status means in a particular case requires the relevant network and client documentation; this explanation does not provide transaction troubleshooting or explorer instructions.

The practical interpretation is deliberately narrow: a mempool is a node-level, temporary view of transactions awaiting inclusion. Transactions can proceed from that view into a block, but the admission, propagation, selection, and retention rules belong to specific networks and implementations. Treating one node’s list as a universal queue—or one chain’s behavior as a rule for all chains—goes beyond what the term supports.

[1] Ethereum transaction lifecycle: `claim_transaction_lifecycle`.

[2] Bitcoin mempool behavior: `claim_bitcoin_mempool_nonpermanent`.

## Sources and references

- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-19.
