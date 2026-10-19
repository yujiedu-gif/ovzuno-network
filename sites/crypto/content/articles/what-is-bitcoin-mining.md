---
title: "What Is Bitcoin Mining? Blocks, Proof of Work, and Security"
description: "Learn how Bitcoin miners build candidate blocks, search for proof of work, broadcast valid blocks, use mining pools, and contribute to chain security."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["mining-and-consensus"]
tags: ["what is bitcoin mining", "how bitcoin mining works", "bitcoin proof of work", "bitcoin mining pool", "bitcoin mining difficulty"]
author: "editorial_team"
primary_keyword: "bitcoin mining"
owned_question: "How does Bitcoin mining add blocks and help secure the network?"
risk_level: "medium"
---

Bitcoin mining is the process that produces candidate blocks and competes to add one of them to the Bitcoin blockchain. Miners assemble transactions, create a block header, and repeatedly hash that header while changing available fields. A block is eligible only when its header hash is at or below the target required by Bitcoin's proof-of-work rules.

Finding that hash is deliberately difficult and probabilistic. Checking it is comparatively easy. That asymmetry lets the network reject blocks that do not show enough work while making attempts to replace accepted history increasingly expensive as more proof of work accumulates above it.

Mining does not give a miner permission to invent coins, spend other people's bitcoin, or bypass consensus rules. Other network nodes independently validate the proposed block. A miner can choose which valid transactions to include, but an invalid block is rejected even if substantial energy was used to create its hash.

## What Bitcoin mining does

Bitcoin needs a way to order valid transactions into a shared history without appointing one permanent block producer. Mining provides that ordering competition. Each miner works on a candidate that refers to the previous block. The first candidate widely propagated with sufficient proof of work may become the next block, provided nodes accept all of its contents under their consensus rules.

NIST describes proof of work as a model in which a publishing node expends time, energy, and computational cycles on a problem that is hard to solve but easy to verify. In Bitcoin, the problem is not a useful scientific calculation. It is a search for a qualifying block-header hash. The search has no reliable shortcut, so more hashing capacity creates more independent chances to find a result.

This process performs two related jobs. It controls the rate at which candidate blocks can be accepted, and it attaches measurable work to the chain's history. It should not be confused with every form of transaction validation. Full nodes validate transactions and blocks against Bitcoin's rules whether or not they mine.

## How a miner builds a candidate block

A miner or mining-pool operator receives unconfirmed transactions from the peer-to-peer network. Its block-building software selects transactions that fit within protocol limits and satisfy its own policies, commonly considering the transaction fees offered. It then creates a special first transaction called the **coinbase transaction**, which assigns the permitted block subsidy and collected fees to an output chosen by the miner or pool.

The transactions are summarized through a Merkle tree. Its root becomes one field in the block header. The header also contains the previous block's hash, a timestamp, the encoded proof-of-work target, a version field, and a nonce. Referring to the previous block connects the candidate to one particular chain tip.

Bitcoin's developer guide describes mining software obtaining the data needed to build this candidate and supplying header work to specialized hashing hardware. If the transaction set or coinbase data changes, the Merkle root changes, creating another large space of possible headers to test.

The miner does not need to wait for a new ordinary transaction every time it exhausts the four-byte header nonce. Mining systems can alter extra nonce data in the coinbase transaction, rebuild the affected Merkle data, update the header, and continue searching.

## How the proof-of-work search works

Bitcoin applies its proof-of-work hash function to the block header. The resulting number must not exceed the current target. Because cryptographic hash output is unpredictable for practical purposes, a miner changes the nonce or other permitted header inputs and tries again.

A single attempt has a small probability of success. The target determines that probability: a lower target permits fewer acceptable hash values and therefore requires more attempts on average. **Difficulty** is a human-friendly expression of how demanding the current target is relative to a reference level.

A miner with twice as much effective hashrate has roughly twice as many attempts in the same period, not a guaranteed schedule of successful blocks. Randomness remains important. One miner can find a block quickly, while another with comparable equipment can search much longer.

The phrase *solving a block* can therefore be misleading. The miner is not deriving one answer through a sequence of logical steps. It is sampling possible headers until a hash happens to satisfy a public threshold. Once found, any node can hash the header and check the result directly.

## What happens when a miner finds a block

The mining system combines the successful header with its candidate transactions and broadcasts the block. Receiving nodes do more than inspect the proof-of-work hash. They independently check the block structure, transaction rules, spending authorization, subsidy and fee limits, proof-of-work target, and connection to known history.

A valid block can extend the node's selected chain. Sometimes two valid blocks are discovered close together and different nodes see them in different orders. Miners then work on the chain tip they select under Bitcoin's rules. As another block arrives, one branch usually accumulates more proof of work, and transactions in the other branch return to consideration if they remain valid and unconfirmed.

This is why businesses wait for confirmations rather than treating the first network sighting as final. Each additional block adds proof of work above a transaction's block. Confirmation policies should reflect transaction value, attack risk, and operational tolerance rather than assuming one count fits every use case.

## Why mining difficulty changes

Hashing capacity can enter or leave the network. If the target never changed, greater total hashrate would make blocks arrive faster, while lower hashrate would make them arrive more slowly. Bitcoin instead recalculates the proof-of-work target after each 2,016-block difficulty period using the elapsed time represented by block-header timestamps and consensus rules.

The adjustment aims to bring the long-run block interval back toward the protocol's intended cadence. It does not force each individual block to appear on schedule. Block discovery remains random, so short intervals vary even when the target is stable.

Difficulty is a network parameter, not a statement about one machine's efficiency or profitability. Hardware cost, electricity, cooling, uptime, financing, pool terms, and bitcoin-denominated revenue are separate operating variables. This article explains consensus mechanics and does not estimate mining returns.

## Block rewards and transaction fees

A valid coinbase transaction can claim two sources of miner revenue: the protocol-defined block subsidy and transaction fees from the included transactions. The subsidy follows a declining issuance schedule. Fees are derived from the difference between transaction inputs and outputs in the accepted block.

Those rewards create an incentive to spend resources on valid block production. They do not pay merely for running hardware. A miner that never finds a network-valid block receives no solo block reward, and a block rejected by validating nodes cannot create spendable rewards under the accepted chain. Protocol rules also restrict when newly created coinbase outputs can be spent.

The exact subsidy, fee market, fiat value, and operating margin change over time. A technically accurate evergreen explanation should not turn today's reward or profitability into a permanent fact.

## Solo mining and pooled mining

A solo miner builds candidates and searches for a network-valid header on its own. If it finds an accepted block, it receives the full permitted reward, but the time between successes can vary dramatically. For a small share of total hashrate, the expected wait can be very long.

A mining pool coordinates work for many participants. The pool provides work and uses an easier internal target to measure **shares**. A share demonstrates that a participant performed a statistically measurable portion of hashing, even though most shares do not meet the harder Bitcoin network target. When a participant finds a header that also meets the network target, the pool can broadcast the block and distribute proceeds under its payout rules.

Pooling reduces payout variance for participants, but it adds dependence on the pool's block templates, accounting, availability, payment policy, and technical controls. A pool's published hashrate is not the same as a promise that it will find a specific number of blocks.

## What mining secures and what it does not

The Bitcoin whitepaper describes the accepted chain in terms of the greatest cumulative proof of work. Replacing an older transaction history requires constructing an alternative valid chain and catching up with the work added by the rest of the network. New blocks therefore raise the resource cost of rewriting earlier history.

That protection has boundaries. Mining does not prevent private-key theft, dishonest exchanges, wallet malware, erroneous addresses, or false offchain information. It cannot make an invalid transaction valid under nodes' consensus rules. Concentrated hashrate or coordinated pool behavior can affect censorship and reorganization risk, but it still does not provide arbitrary authority over coins without valid signatures.

The precise division is important: miners propose transaction ordering and attach proof of work; validating nodes enforce the rules of the blocks they accept; users and services decide how many confirmations and what surrounding controls they require. Bitcoin security emerges from those interacting roles, not from mining hardware alone.

## Sources and references

- [Proof of work consensus model - Glossary](https://csrc.nist.gov/glossary/term/Proof_of_work_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [Mining — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-18.
