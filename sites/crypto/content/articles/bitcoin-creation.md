---
title: "Bitcoin creation: how mining issues new bitcoin"
description: "Learn how Bitcoin creation works at the protocol level: how valid blocks authorize new bitcoin, how issuance changes over time, and how fees differ."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["Bitcoin mining", "block reward", "Bitcoin issuance"]
author: "editorial_team"
primary_keyword: "bitcoin creation"
owned_question: "How does the Bitcoin protocol create new bitcoin through mining, and what rules limit its issuance?"
risk_level: "medium"
---

Bitcoin’s protocol creates new bitcoin when a valid block includes an allowed block subsidy. Miners construct and work on candidate blocks, but proof of work alone does not authorize an excessive claim: network rules determine which blocks are valid. The subsidy follows a block-height schedule that halves every 210,000 blocks, while transaction fees are transfers of existing bitcoin rather than new issuance.

## What “Bitcoin creation” means in the protocol

Here, “creation” means the protocol-authorized issuance of bitcoin in the ledger. It does not mean creating a wallet, an address, or a screen that displays a balance. A cryptocurrency system includes protocol rules, a transaction ledger, and participants that update, store, and read that ledger. Issuance is part of the protocol’s rules for updating the ledger, not an action that a user interface can make authoritative by itself. ([source](<https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype>))

The discussion is specific to Bitcoin’s proof-of-work issuance model. Proof of stake is a distinct consensus model in which cryptocurrency committed as stake influences consensus participation or weight; it should not be treated as a description of how Bitcoin mining issues bitcoin. ([source](<https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model>))

It is also useful to separate the protocol from the services people use to interact with it. A wallet or exchange can present balances or help users interact with a network, but those services are not the protocol mechanism that authorizes issuance. This article concerns the rules governing valid Bitcoin blocks, not how to acquire, store, or trade bitcoin.

## How mining makes a block eligible for a subsidy

Mining software assembles a candidate block from transactions and constructs work for hashing hardware. In Bitcoin’s original design, hashes link blocks, and hash-based proof of work helps order transaction history; replacing accepted history requires renewed computational work. These functions make mining part of proposing and ordering a candidate block, but they do not mean that every attempted block is accepted. ([source](<https://bitcoin.org/bitcoin.pdf>))

A miner’s proposal is subject to the network’s consensus rules. The key distinction is between producing a candidate and producing a valid block: proof of work does not make a block valid if it violates another consensus rule. The block subsidy is authorized only within the rules governing valid ledger updates. In practical terms, a miner cannot make an excessive issuance claim valid merely by finding proof of work.

Bitcoin’s issuance schedule is described by block height, the block’s position in the chain, rather than by a calendar date. The subsidy halves after each 210,000-block subsidy era. This defines a repeating rule for reducing the subsidy as the chain advances; it does not specify a predictable date for each reduction, because the rule is keyed to block count.

The supplied evidence establishes the block-height interval and halving rule, but not the initial subsidy amount or a complete calculation table for every block. Those details should not be supplied from memory in an evidence-limited explanation. The important mechanism is that the subsidy is governed by a programmed schedule tied to block height, and a valid block must conform to the applicable rule.

## Bitcoin issuance and the subsidy schedule

The subsidy schedule limits new issuance by specifying how the block subsidy changes over successive eras. Because each era is defined by a number of blocks, a description of the rule should identify the boundary block height rather than assume a specific calendar date. For historical reporting, the relevant boundary block and its chain timestamp are a better-defined reference than an unsupported date assumption.

A schedule is not the same thing as a point-in-time count of bitcoin in circulation. A current supply figure needs a dated data source and a clear measurement definition. The authorized evidence does not provide such a figure, so this article does not state one. The schedule alone also does not tell a reader how much bitcoin is accessible to users; the protocol issuance rule and practical accessibility are different questions.

This distinction prevents a common overstatement: a rule limiting valid issuance is not by itself a measurement of circulating or usable supply. Any such measurement needs its own method and date. Without that context, presenting a precise total would make the number appear more definitive than the evidence allows.

## Block subsidy versus transaction fees

A miner’s revenue can include both the block subsidy and transaction fees. The subsidy is the newly issued component permitted by the protocol schedule. Fees are paid in existing bitcoin through transactions and are not new issuance. Thus, a block may include both sources, but only the subsidy represents protocol-authorized creation of new bitcoin.

This distinction matters when discussing how miner revenue might change over time. As the subsidy declines under the schedule, fees may form a larger share of revenue, but their future level is uncertain. The issuance rule establishes the subsidy schedule; it does not guarantee a particular fee amount or total miner revenue. This article therefore does not predict fees, profitability, or what a miner will earn.

## What the issuance rules do—and do not—guarantee

Issuance rules describe what a valid block may add under the protocol. They do not, on their own, guarantee a transaction’s confirmation speed, determine mining profitability, or establish how much bitcoin is accessible. Those are separate questions and should not be inferred from the subsidy schedule.

Nor should a description of the present rule be mistaken for proof that protocol rules can never change. The available evidence does not establish Bitcoin’s complete rule-change process or that issuance rules are legally or technically immutable. A documented Ethereum protocol-change process, for instance, includes proposal, technical review, implementation, coordination, and adoption among stakeholders, but that Ethereum-specific account cannot be transferred to Bitcoin as evidence of Bitcoin governance. ([source](<https://ethereum.org/governance/>))

The practical takeaway is narrow: Bitcoin mining proposes candidate blocks, and consensus rules determine whether a block and its subsidy claim are valid. The subsidy declines at protocol-defined block-height intervals; transaction fees are separate transfers of existing bitcoin. Current circulating-supply totals and claims about future fees require evidence beyond the issuance schedule itself.

## Sources and references

- [Introduction to Ethereum Governance](https://ethereum.org/governance/) — ethereum.org; retrieved 2026-10-18.
- [Cryptocurrencies: Looking Beyond the Hype](https://www.bis.org/publications/aer-2018/cryptocurrencies-looking-beyond-hype) — Bank for International Settlements; retrieved 2026-10-18.
- [Bitcoin: A Peer-to-Peer Electronic Cash System](https://bitcoin.org/bitcoin.pdf) — Bitcoin.org; retrieved 2026-10-19.
- [Proof of stake consensus model - Glossary](https://csrc.nist.gov/glossary/term/proof_of_stake_consensus_model) — National Institute of Standards and Technology; retrieved 2026-10-19.
