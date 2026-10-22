---
title: "amm blockchain: How Automated Market Makers Work"
description: "Learn how an amm blockchain enables swaps through smart contracts and liquidity pools, how execution works, and which operational risks to consider."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["blockchain_payment_foundations"]
tags: []
author: "editorial_team"
primary_keyword: "amm blockchain"
owned_question: "How does an automated market maker work on a blockchain, and how do its smart contracts, liquidity pools, and transaction execution fit together?"
risk_level: "medium"
---

An automated market maker (AMM) on a blockchain enables swaps by using smart contracts and a pool of assets: the contract applies programmed rules to the pool, and the blockchain records the swap when its transaction is included and settles. The exact pool structure, pricing logic, and accounting depend on the AMM design, so this is a general explanation rather than a description of every system.

## What an AMM does on a blockchain

An AMM is a mechanism for arranging trades against assets held in a liquidity pool. A liquidity pool is a reserve of assets available to execute swaps under rules implemented by a smart contract. This differs from a model that depends on matching each trader with a named buyer or seller: the pool provides the trading inventory, while the contract defines how a swap uses it.

The term “AMM” covers designs that can differ in their assets, pool structures, pricing logic, fees, and accounting. For a concrete but limited example, a Uniswap v2 pool holds reserves of a token pair and uses those reserves as the inventory from which swaps execute. Liquidity-provider shares represent contributions to that pool. This example describes Uniswap v2’s constant-product model; it should not be treated as a rule for every AMM.

The word “automated” refers to the contract applying its programmed rules. It does not mean that a trade happens without a user or application initiating an action, or that every trade request will succeed. A user-facing application may help construct or submit a request, while the contract and pool supply the mechanism for executing it. The details of that interaction depend on the particular system.

## How a swap moves through a liquidity pool

A useful conceptual sequence has three parts: a swap request, contract execution against pool assets, and a resulting blockchain record. The sequence describes the components, not a universal interface or transaction path.

1. **A request is prepared.** A user interacts with an application or interface that can submit a transaction calling the relevant contract. A request presented by an interface is not itself proof that a swap has been completed.
2. **The contract applies its rules.** In an AMM that trades through a liquidity pool, the contract uses the pool’s assets and its programmed mechanics to determine the exchange outcome. The specific calculation depends on that design. There is no basis here for assuming that all AMMs use one formula or produce quotes in the same way.
3. **The transaction settles through blockchain execution.** In the AMM model described by the BIS, smart contracts and liquidity pools implement trading, and transactions settle when included in a blockchain block. Submission and settlement are therefore distinct: initiating a request does not establish that it was included and settled.

This sequence separates the responsibilities involved. An interface provides an interaction path. The smart contract applies its programmed rules. The pool supplies the assets used for swaps. The blockchain supplies the transaction-recording and settlement context described for the AMM model. These roles fit together, but their implementation can vary across networks and protocols.

For infrastructure analysis, it helps to ask which part of the sequence a statement concerns. A displayed request or quote concerns the application’s interaction with the user; pool mechanics concern the assets and contract rules; and settlement concerns a transaction’s inclusion in a block. Without implementation-specific evidence, those stages should not be collapsed into a claim that every request is executed, that every swap uses the same route, or that a transaction can be recovered or reversed.

## The role of smart contracts and pool assets

A smart contract is the on-chain component that applies the AMM’s defined rules. In a pool-based design, those rules govern how the pool’s assets are used when trades execute. The pool is not merely a display of prices: its deposited reserves provide the inventory for swaps. In the Uniswap v2 example, token-pair reserves and liquidity-provider shares are part of that pool’s mechanics. Other AMMs can use different curves, assets, fees, and accounting.

Liquidity providers are participants who contribute assets to pools. Their role differs from that of a trader requesting a swap: providers supply pool inventory, while a swap uses pool inventory under contract rules. AMM liquidity providers can receive a share of trading fees, but they also bear inventory and adverse-selection risk. The exact arrangement and outcome depend on the protocol and position.

One commonly discussed exposure is inventory-value loss relative to holding the assets. An AMM liquidity provider can experience such loss when pool prices move, and trading fees may or may not offset it. The result depends on factors such as the pool design, price path, range, fees, timing, and withdrawal state. This explains a risk category; it does not establish the result for a particular pool or imply a return.

The distinction between contract and pool matters when assessing how an AMM works. Contract rules describe how the system acts on a request, while the pool’s assets provide the inventory available for execution. Neither component alone tells a reader every implementation detail. Claims about a specific pool’s pricing, asset composition, fee treatment, or permissions require evidence about that pool and protocol.

## How AMMs differ from order-book exchanges

An order book organizes trading around buy and sell orders that are matched under the venue’s rules. An AMM-based decentralized exchange, by contrast, can implement trading through smart contracts and liquidity pools, with transactions settling when included in a blockchain block. The difference is how the trading mechanism organizes liquidity and execution: orders are matched in an order-book model, while an AMM pool supplies assets that a contract uses under its rules.

This is a structural distinction, not a judgment about performance. It does not establish that an AMM or an order-book venue is universally cheaper, safer, faster, or more effective. Those claims would require evidence about a particular system and operating conditions. Nor does the label “decentralized” mean that every part of a system has the same design or dependencies; the bounded point here is that the AMM execution model described uses contracts and pools.

## Operational risks and what to verify

The basic mechanics do not provide a security guarantee. A contract applying programmed rules does not establish that the code is free of defects, and on-chain execution alone does not establish that a transaction will succeed or that an action can be reversed or recovered. A general description of AMMs also cannot substantiate claims about audits, vulnerabilities, or security assurances for a particular system. Those claims need current, attributable evidence scoped to the relevant implementation.

Pool-related risk is separate from the mechanics of an individual swap. Liquidity providers can experience inventory-value loss relative to holding assets when pool prices move, and fees may or may not offset it. This is a conditional exposure whose outcome depends on pool and position details, not a prediction about a specific result. The AMM mechanism itself does not establish an expected yield or make a recommendation to trade or provide liquidity.

For an implementation-specific assessment, identify the protocol and pool, then verify documentation for the contract rules, pool assets, and transaction path. Claims about fees, asset availability, recovery options, security reviews, yields, or legal and tax treatment need current evidence with the appropriate scope. None of those details follows automatically from the definition of an AMM. The central infrastructure relationship is narrower: a pool supplies assets, a contract applies its rules to a swap request, and blockchain execution records settlement when the transaction is included in a block.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
