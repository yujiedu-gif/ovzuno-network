---
title: "Mining blockchain: how proof-of-work orders transactions"
description: "Learn how mining blockchain systems use proof of work to propose blocks, order transactions, and support agreement, plus what mining does not guarantee."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "mining blockchain"
owned_question: "How does mining work on a proof-of-work blockchain, and what role does it play in validating and ordering transactions?"
risk_level: "medium"
---

On a proof-of-work blockchain, mining is the process of proposing blocks by searching for a proof that meets the network’s target. Other network participants check the proposed block against protocol rules, and the protocol determines how competing histories are ordered. Mining contributes to agreement about transaction order, but it does not make an invalid transaction valid or guarantee that inclusion is permanent. The details below are limited to the allowed evidence about Bitcoin’s proof-of-work search and Ethereum’s block checking and finality; they are not a universal description of every blockchain.

## What mining means in a proof-of-work blockchain

Mining is a block-production role, not a synonym for every kind of blockchain validation. In Bitcoin’s original network design, a miner varies a nonce in a block until its resulting hash satisfies the network’s target condition. This repeated search produces a candidate block proposal that can be presented to the network. The process is computational; it is not a judgment about whether the transaction is appropriate outside the protocol’s rules. ([source](<https://bitcoin.org/bitcoin.pdf>))

The details matter: Bitcoin’s nonce-and-hash description is specific to Bitcoin. Other proof-of-work networks may define different hash functions, block fields, targets, and target-adjustment rules. The available evidence does not support treating Bitcoin’s exact mining procedure as a rule for every network. Nor does it establish that every blockchain uses mining.

It is also important to distinguish proposing a block from checking it. A miner can search for a proof and propose a block, while network participants apply the relevant protocol rules to decide whether that proposal is acceptable. Ethereum illustrates the checking role: an Ethereum node receiving a proposed block checks it and re-executes its transactions to verify the resulting state change. That example explains the distinction between proposal and validation; it does not describe Ethereum as a proof-of-work network. ([source](<https://ethereum.org/developers/docs/blocks/>))

## From pending transactions to a candidate block

A candidate block is a miner’s proposed grouping and ordering of transactions for a particular point in the network’s history. A transaction’s presence in that proposal is not, by itself, proof that the transaction satisfies protocol rules or that the network has accepted the block. The proposed block must still meet the applicable proof condition and pass the network’s validity checks.

This distinction separates three stages that are often collapsed into the phrase “mining validates transactions.” First, transactions are considered for a block proposal. Second, a miner searches for the required proof for that proposal. Third, participating nodes check whether the block and its transactions comply with the protocol before accepting the block. The proof addresses the proof-of-work condition; it does not replace transaction and block validation. The available evidence supports this broad sequence but does not establish a universal transaction-selection policy, a universal ordering rule within a candidate block, or common block-size limits across networks.

For a business or technical reader, the operational question is therefore not merely whether a transaction appears in a proposed block. It is whether the relevant network has accepted the block under its own rules and what that network’s policy treats as sufficient confirmation or finality. Those policies are network-specific, so Bitcoin and Ethereum mechanics should not be combined into a single assumed workflow.

## How proof of work helps order blocks

In the Bitcoin proof-of-work example, miners search for a block-header hash that meets the current target. The search is difficult because miners must find a qualifying result; the resulting proof can then be checked against the target. The target is part of the network’s rules, rather than a discretionary approval by an individual miner. Bitcoin’s target adjustment follows its own consensus rules, but the evidence allowed for this article does not specify an adjustment schedule. That detail should not be inferred or generalized to other networks. ([source](<https://bitcoin.org/bitcoin.pdf>))

A proof helps a proposed block participate in the ordering of history, but it does not alone determine whether the block becomes part of the accepted history. The block must also satisfy the network’s validity rules. Ethereum’s documented process provides a concrete illustration of this separation: an Ethereum node checks a proposed block and re-executes transactions to verify the resulting state change before accepting it. Proof of work and that Ethereum checking example refer to different network-specific mechanics, not interchangeable consensus designs. ([source](<https://ethereum.org/developers/docs/blocks/>))

Once a network has accepted a block, the transaction order recorded in that block forms part of the chain’s ordered history. Ethereum’s block structure references the parent block cryptographically, creating an ordered chain of network state. This establishes the structural link between blocks, but by itself it does not describe how every network resolves competing histories or what confirmation threshold a payment application should require. ([source](<https://ethereum.org/developers/docs/intro-to-ethereum/>))

Consequently, a block proposal should not be confused with a universal guarantee of agreement at that instant. To explain how competing histories are resolved, one must use the specific chain-selection rules of the network in question. The allowed evidence here does not provide Bitcoin’s chain-selection rule, so this article does not claim that the greatest-cumulative-work rule applies across proof-of-work networks or state it as a supported Bitcoin fact.

## What mining validates—and what it cannot guarantee

Mining does not give miners authority to override protocol validity rules. A proof can satisfy the network’s proof-of-work condition, but the proposed block must still pass the checks that participating nodes apply. In Ethereum’s documented example, nodes check the block and re-execute its transactions before accepting it. This illustrates why block production and validation are distinct functions; it is not a statement that Ethereum uses Bitcoin’s mining process. ([source](<https://ethereum.org/developers/docs/blocks/>))

Block inclusion also needs to be distinguished from finality. In Ethereum, proof of stake uses validator votes on checkpoint blocks to distinguish finalized history from blocks that are merely included. That is an Ethereum-specific finality mechanism, not a general rule for proof-of-work systems. It shows why readers should ask which network’s finality and recovery rules apply rather than assume that the word “mined” means “irreversible.” The available evidence does not establish a confirmation threshold for Bitcoin or a universal time after which any blockchain transaction cannot be reorganized. ([source](<https://ethereum.org/developers/docs/consensus-mechanisms/pos/>))

A careful explanation therefore separates a transaction’s inclusion in a block from later network-specific confirmation or finality. It also separates protocol records from external outcomes: the mechanism described here does not establish that a payment obligation has been discharged, that identities have been verified, or that disputes and errors can be resolved. Mining can contribute to a network’s process for proposing and ordering blocks, but readers should not treat it as a guarantee of anonymity, settlement, or permanent finality.

## Mining’s costs and external impacts: evidence to check

Bitcoin’s documented proof-of-work search requires varying a nonce and repeatedly testing whether the resulting hash meets the target. That supports describing mining as a computational search, but the allowed evidence does not quantify electricity use, emissions, equipment expenses, rewards, transaction fees, or profitability. Those topics need current, attributable evidence specific to the network and period being discussed; this article does not estimate them or assess mining economics.

The same evidence boundary applies to operation and policy. No conclusion about mining’s legality, licensing, taxes, compliance obligations, or availability in a particular place follows from explaining its protocol mechanism. Those questions require current, jurisdiction-specific evidence. The relevant scope here is narrower: proof-of-work mining proposes blocks, while network rules and participant checks determine whether a proposal is accepted and how its transaction history is treated.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
- [Proof-of-stake (PoS)](https://ethereum.org/developers/docs/consensus-mechanisms/pos/) — ethereum.org; retrieved 2026-10-19.
