---
title: "Mining mechanism in blockchain: how proof-of-work adds blocks"
description: "Learn how the mining mechanism in blockchain uses proof of work to propose blocks, how nodes verify them, and when accepted miners may receive rewards."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: ["proof of work", "miners", "block validation", "mining rewards"]
author: "editorial_team"
primary_keyword: "mining mechanism in blockchain"
owned_question: "How does the mining mechanism in a proof-of-work blockchain select a block, and how do other participants verify and add it to the chain?"
risk_level: "medium"
---

In a proof-of-work blockchain, a miner builds a candidate block and repeatedly hashes its data, changing a value such as a nonce until a result satisfies the network’s target condition. The miner then proposes the block, but other participants must independently verify it under the protocol rules. Bitcoin provides a concrete example of this mechanism; its details should not be treated as universal rules for every blockchain.

## What mining means in a proof-of-work blockchain

Mining is the work of preparing a proposed block and searching for a proof that meets a network-defined condition. Proof of work is one component used for Sybil resistance and block-author selection; it works alongside validation, networking, incentives, and a fork-choice rule. It is therefore not the entire consensus process, and mining does not describe every blockchain. [source](<https://ethereum.org/developers/docs/consensus-mechanisms>)

The distinction between proposing and validating is central. A miner constructs a candidate and searches for a qualifying proof. Other nodes check whether the candidate follows the network’s rules. Proof of work cannot make an invalid block valid: a candidate may satisfy the hash target and still fail other protocol checks.

The following steps use Bitcoin’s documented mining process to make the mechanics concrete. Bitcoin-specific structures, target rules, and other operational details should not be assumed to apply to other networks.

## How miners build a candidate block

Before searching for a proof, mining software needs information about the block it is trying to build. In Bitcoin, the `getblocktemplate` interface provides information needed to construct a coinbase transaction and inspect a proposed set of block transactions. The miner uses that information to form a candidate; this does not mean every transaction awaiting inclusion will appear in the block. [source](<https://developer.bitcoin.org/devguide/mining.html>)

The candidate includes transactions and the data needed to identify its place in the chain and support the proof search. The proposed set of transactions can change, and the protocol determines which block structures and transactions are valid. Candidate construction is therefore constrained by network rules, not just by a miner’s preferred transaction list.

Once assembled, the candidate supplies the data over which the proof-of-work search operates. In Bitcoin, the miner varies a nonce in the block and hashes the resulting header, looking for a result that meets the network’s target condition. The nonce is a changeable input to the search; it does not itself certify that the candidate’s transactions or structure are valid. [source](<https://bitcoin.org/bitcoin.pdf>)

This separation helps clarify what the mining step proves. The search tests whether the candidate data produces a hash meeting a numerical condition. It does not decide whether each transaction is authorized or whether the full block complies with all rules. Those questions remain part of independent validation.

## How proof of work selects a block

For Bitcoin, a block-header hash must be at or below the current target threshold to meet the proof-of-work requirement. Mining software repeatedly tries variations of the candidate data, including a changed nonce, and checks the resulting hash against that threshold. A hash that passes makes the candidate eligible to be proposed; it is not, by itself, a guarantee that the block will become accepted history. [source](<https://bitcoin.org/bitcoin.pdf>)

The target is network-specific and can change. On Bitcoin mainnet, the proof-of-work target is adjusted after each 2,016-block difficulty period using block-header timestamps and consensus rules. This adjustment interval is a Bitcoin-specific rule, not a general schedule for all proof-of-work systems. [source](<https://developer.bitcoin.org/devguide/block_chain.html>)

After a qualifying result is found, the miner can propose the candidate to the network. The proof supplies evidence that the candidate satisfies Bitcoin’s work condition, but the network still needs to check the block and its contents. The proof search and the rule checks are related parts of block acceptance, not interchangeable ones.

## How nodes verify and accept a mined block

When a proposed block reaches a node, that node checks it against the applicable protocol rules rather than accepting it solely because the miner reports a qualifying hash. For Ethereum, as a separate example of independent node checking, a node receiving a proposed block checks the block and re-executes its transactions to verify the resulting state change before accepting it. This illustrates the general distinction between block proposal and verification, but Ethereum’s execution details are not Bitcoin mining rules. [source](<https://ethereum.org/developers/docs/blocks/>)

The evidence available here supports a specific Bitcoin target-search process and a separate Ethereum example of node verification. It does not establish a complete, uniform validation checklist for every proof-of-work blockchain. Each network’s protocol specifies its own block structure, transaction checks, and acceptance behavior; those details require network-specific evidence.

A valid proposed block is also not the same thing as an unconditional promise that its place in history can never change. Proof-of-work determines whether a candidate meets a target, while a network’s broader rules determine how nodes treat valid blocks and competing histories. The evidence cited here does not provide a universal finality guarantee or a single confirmation policy for all networks. Readers should treat confirmation and finality as network-specific operating concepts rather than infer an absolute guarantee from the existence of a qualifying hash.

## Mining rewards and what they depend on

Mining is often discussed alongside rewards, but reward eligibility and mechanics are defined by the particular protocol. The allowed evidence for this explanation does not establish a Bitcoin reward amount, a universal reward formula, or how transaction fees are allocated. It would therefore be inaccurate to infer a particular payment just from the fact that a miner found a hash that met the target.

The process yields a narrower conclusion: a miner has found a candidate proof that satisfies a network condition. Whether the proposed block is accepted, and whether protocol rules associate rewards with it, depend on that network’s rules and the candidate’s acceptance. This is a description of protocol conditions, not an estimate of income, profitability, or financial return.

For a network-specific account of rewards, a reader would need current authoritative documentation for that network and its applicable protocol version. Without that evidence, keep the explanation at the level of the mechanism: candidate construction, proof search, independent checks, and protocol-defined acceptance.

## Mining, validation, and limits of the explanation

The process can be summarized as a sequence: the miner forms a candidate from proposed transactions and required data; mining software searches by varying a nonce and hashing candidate data; a qualifying result allows the miner to propose the block; and nodes apply their own protocol checks before accepting it. Mining is the proposal and proof-search role. Validation is the checking role performed by network participants under the rules they run.

The Bitcoin proof-search and target-adjustment details described here are specific to Bitcoin, while the node re-execution example is specific to Ethereum. Neither example establishes universal claims about energy use, security, block timing, fees, rewards, or finality. Those properties must be assessed against the relevant network’s current authoritative documentation and operating conditions, rather than transferred from one protocol to another.

When evaluating a claim about mining, separate four questions: what information is used to build a candidate, what proof condition the network requires, what checks nodes perform, and what protocol rules govern acceptance and any associated reward. Keeping these questions distinct avoids conflating a successful hash search with full validation or treating a proposed block as automatically accepted history.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Blocks](https://ethereum.org/developers/docs/blocks/) — ethereum.org; retrieved 2026-10-18.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
- [Consensus Mechanisms](https://ethereum.org/developers/docs/consensus-mechanisms) — ethereum.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
