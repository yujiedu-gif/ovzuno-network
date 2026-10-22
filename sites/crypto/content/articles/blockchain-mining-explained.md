---
title: "Blockchain mining explained: how proof of work adds blocks"
description: "Blockchain mining explained: see how proof-of-work miners propose blocks, how nodes check them, and how mining differs from staking."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["blockchain mining"]
author: "editorial_team"
primary_keyword: "blockchain mining explained"
owned_question: "How does mining help proof-of-work blockchains propose and validate blocks, and how is it different from staking?"
risk_level: "medium"
---

Proof-of-work mining is the process miners use to propose blocks by searching for a computational result that meets a network’s target. Other participants check the proposed block against that network’s rules; performing the work does not make an invalid block acceptable. Staking is a different approach, but the evidence available for this article does not support a detailed comparison of staking mechanics. The key point is that mining is specific to proof-of-work networks, not a universal blockchain process.

## What blockchain mining means in a proof-of-work network

Mining is a block-production method: participants compete to produce a candidate block whose proof satisfies a target set by the network. In Bitcoin’s original design, miners vary a nonce in the block header and calculate hashes until the result satisfies the target condition. This repeated search is the proof-of-work step. Other networks may define different mechanisms, so Bitcoin’s details should not be treated as a description of all blockchains.

Mining is not synonymous with the entirety of consensus. It describes how proof-of-work miners search for a qualifying block proposal. The network’s rules also determine what makes a block valid and how participants treat proposed blocks. Work can qualify a proposal for consideration, but it cannot override those rules.

This distinction helps clarify the word “miner.” In this context, a miner is a participant or system performing the proof-of-work search and preparing block proposals. The term does not mean that the miner alone determines the network’s accepted state. The specific tasks and rules depend on the protocol and its software.

## How miners propose a block and nodes check it

The process has two distinct parts: producing a qualifying proposal and checking whether that proposal follows the rules. For Bitcoin, the work search proceeds by varying a nonce in a block header until its hash meets the current target. The target is adjusted after each 2,016-block difficulty period using block-header timestamps and consensus rules. That adjustment is specific to Bitcoin’s mainnet mechanism; it is not a general schedule for other proof-of-work networks.

A miner’s candidate includes transactions it is proposing to place in a block. The transaction-selection rules and block format are network-specific, so there is no single universal list of selection criteria to apply to every chain. The important operational point is that a candidate block is a proposal. Finding a qualifying proof does not settle whether the transactions and block satisfy all applicable rules.

Other participants check the proposal under the protocol’s validity rules. Ethereum provides a separate example of network verification: a node receiving a proposed block checks the block and re-executes its transactions to verify the resulting state change. This is Ethereum-specific evidence and should not be mistaken for a description of Bitcoin mining or a universal implementation pattern.

The distinction between proof and validity is fundamental. A qualifying proof shows that the specified computational target was met. A network’s block and transaction rules still determine whether the proposal is valid. Computation does not confer authority to bypass those rules, and the details of checking and acceptance must be established from the relevant network’s technical documentation.

## What miners may receive—and what incentives do not guarantee

Mining incentives are defined by individual protocols. The evidence available here does not establish a general reward formula, universal treatment of transaction fees, or a guaranteed payment for a mining attempt. Those details should be checked in the current documentation for the particular network rather than inferred from the word “mining.”

A block-production mechanism and its incentives are separate from the validation step. Even where a protocol specifies incentives, those rules do not turn an invalid proposal into a valid block. This article does not estimate expenses, earnings, or profitability, and it makes no prediction about returns. Understanding the mechanism is not the same as deciding whether to participate financially.

Protocol rules also provide the appropriate boundary for any explanation of rewards: identify which network and rule set is being discussed, then verify how it defines block production and incentives. Without that network-specific evidence, claims about amounts, timing, or predictability would go beyond what can be established here.

## Mining versus staking: different ways to participate

Mining refers to a proof-of-work block-production process, in which participants search for a result meeting a computational target. Staking refers to a different consensus approach, but the allowed evidence for this article does not establish its mechanics, the role of stake, or the duties assigned to participants. A detailed technical comparison would therefore require additional network-specific evidence.

For the reader’s basic distinction, do not use “mining” as a synonym for all block production. First identify the network’s consensus design. If it uses proof of work, mining may describe its block-proposal process; if it does not, mining terminology may not apply. The label alone does not establish how a network validates proposals or reaches its own consensus decisions.

Network-specific detail matters even within proof of work. Bitcoin’s nonce search and difficulty adjustment are Bitcoin mechanisms. Ethereum’s block re-execution example describes verification on Ethereum, not mining. Keeping these examples separate avoids combining mechanics from different networks into a single assumed model.

## What mining can and cannot establish about network security

Proof of work requires computational work to produce a result that meets a target, but this fact alone does not establish a universal security guarantee. The evidence in this article supports a description of Bitcoin’s search method and adjustment period and an Ethereum-specific example of block checking. It does not support general claims about attack resistance, confirmation behavior, or the security of every proof-of-work network.

A qualifying proof and a valid block are different questions. The proof concerns whether the target condition was met; validity depends on the network’s rules. Neither statement, by itself, establishes that a transaction is private, reversible, or free from risk. Avoid extending a mechanism description into assurances about outcomes that require separate, network-specific evidence.

When assessing a particular system, start with its official technical documentation and identify the consensus design, proof conditions, block-validity rules, and any protocol-specific adjustments. Do not import Bitcoin’s target adjustment or Ethereum’s verification example as if they governed every network. Mining is one way proof-of-work systems propose blocks; what counts as valid and how a network handles proposals are defined by that network’s own rules.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
