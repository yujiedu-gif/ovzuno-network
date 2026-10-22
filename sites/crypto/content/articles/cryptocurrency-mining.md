---
title: "Cryptocurrency mining: how proof-of-work networks reach agreement"
description: "Learn how cryptocurrency mining supports proof-of-work consensus, from proposing blocks and performing computational work to network verification and rewards."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["mining_consensus"]
tags: []
author: "editorial_team"
primary_keyword: "cryptocurrency mining"
owned_question: "How does cryptocurrency mining help a proof-of-work network agree on blocks, and what does the process require?"
risk_level: "medium"
---

For builders and operators, cryptocurrency mining is a proof-of-work process used by some networks to propose candidate blocks. In the Bitcoin example, mining software turns block-template information into header work, hardware searches for a hash that meets the network’s target, and nodes still determine whether the resulting block follows protocol rules. Computational work helps select among competing valid histories; it does not make an invalid block acceptable.

## What cryptocurrency mining does in a proof-of-work network

Mining connects computational work with proposing blocks and ordering transaction history. A miner prepares a candidate block, then searches for proof that satisfies the network’s prescribed condition. A qualifying result allows a candidate to be presented for consideration. It does not mean the miner has independently settled which history every participant must accept.

Bitcoin provides a concrete illustration, not a universal specification. Its original design uses hash-based proof of work, while other cryptocurrency networks can use different consensus mechanisms. Even among proof-of-work systems, the specific hashing method, data committed in a block, and acceptance rules are defined by each protocol. “Mining” should therefore be read in context: it describes a process in networks that use proof of work, not a required step in every cryptocurrency system.

For Bitcoin, when histories compete, nodes select the valid chain representing the greatest cumulative proof of work. Both parts of that description matter. The chain must be valid under Bitcoin’s rules, and cumulative work is used to choose among valid histories. Work does not override those rules.

## From transactions to a candidate block

Before hashing begins, mining software constructs a proposed block and its header. In the Bitcoin workflow, software transforms block-template information into header work that hashing hardware searches. The candidate block includes transactions and links to the prior block history; its header is the compact object searched in the proof-of-work process.

A template is input to construction, not a guarantee that every proposed transaction or block detail will be accepted. Network rules determine what is valid. Software may assemble a candidate from transactions, but this step does not itself establish that the transactions meet all applicable rules or that the full block will be accepted by other nodes.

The workflow can be understood as three separate stages. First, software prepares candidate information and forms the block and header. Second, hashing hardware searches for a header result meeting the proof-of-work condition. Third, the proposal is subject to network validation and chain-selection rules. Keeping these stages separate helps avoid treating “a miner found a result” as equivalent to “the network accepted the block.”

The precise construction process is protocol-specific. Bitcoin documentation describes its own process, and the same terminology should not be used to assume that another network has identical transaction selection, header fields, or block rules.

## Why miners perform computational work

In Bitcoin, proof of work requires a block-header hash at or below the current target threshold. Mining hardware repeatedly searches candidate header values for a result meeting that condition. The target is part of the protocol’s rule for what counts as qualifying work; merely performing computation without a result that meets it does not satisfy the condition.

The result is useful because it is straightforward to check against the target: a participant can assess whether the proposed header meets the stated proof-of-work requirement. But successful work demonstrates only that the target condition has been met. It does not establish that the transactions are compliant, that all block data is acceptable, or that the block is the history nodes should select.

That distinction also explains why proof of work is not the same as transaction verification. A miner’s computational search concerns the block header and target condition. Validation concerns whether the transactions and block satisfy protocol rules. A miner may perform more than one network role, but mining and rule validation remain conceptually distinct functions.

## How the network checks a mined block

After a qualifying result is found, the candidate block is a proposal for the network to evaluate. In Bitcoin, nodes enforce transaction and block-validity rules. When histories compete, they select the valid chain with the greatest cumulative proof of work. A block that fails a consensus rule is not made valid by having a qualifying hash or by being accompanied by substantial work.

This divides responsibility between block production and independent rule enforcement. Mining software constructs candidate work, and hashing hardware searches for a qualifying result. Nodes apply the protocol’s validity rules and participate in selecting the accepted history. A miner can propose a block, but the proof-of-work result alone does not compel nodes to accept it.

The chain-selection statement is specifically about Bitcoin’s design. It should not be treated as a universal description of consensus or finality across cryptocurrency networks. Protocols can set different rules for how participants validate blocks and resolve competing histories. For a network other than Bitcoin, the relevant protocol documentation is needed to determine what “accepted” means and which participants perform each check.

## Rewards, resource inputs, and operational limits

Mining operations can require computational hardware, electricity, and software infrastructure to perform and coordinate hashing and block construction. These are broad resource categories, not a specification for a particular operation. Equipment requirements and operating conditions depend on the implementation. This account does not compare devices or recommend a setup.

In Bitcoin, a solo miner who finds a block is assigned the full block reward and transaction fees under the described mining model. That protocol-level allocation should not be confused with a forecast of how often a particular miner will find a block, a claim about net earnings, or a profitability estimate. Those questions would require assumptions and evidence beyond the block-production mechanism, so no expected yield or financial conclusion follows here.

The central operational limit is that computational effort and protocol validity answer different questions. Work establishes whether a candidate meets the proof-of-work condition; validation determines whether the candidate complies with network rules; chain selection determines which valid competing history is preferred in Bitcoin’s model. Keeping those steps distinct explains mining’s role without implying that work guarantees acceptance, rewards in every attempt, or any particular operational or financial outcome.

## Sources and references

- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Block Chain — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/block_chain.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
- [Mining](https://developer.bitcoin.org/devguide/mining.html) — Bitcoin Developer Documentation; retrieved 2026-10-19.
