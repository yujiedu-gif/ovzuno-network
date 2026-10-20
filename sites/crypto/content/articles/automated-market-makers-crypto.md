---
title: "Automated Market Makers Crypto: How It Works"
description: "Understand Automated Market Makers Crypto, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "automated market makers crypto"
owned_question: "How do automated market makers work in crypto, and how do their liquidity pools and pricing mechanisms differ from order-book exchanges?"
risk_level: "medium"
---

# Automated Market Makers Crypto: How It Works

Automated market makers (AMMs) are a way to execute trades through liquidity pools and pricing rules rather than by matching each buyer’s order with a seller’s order. In a crypto AMM, users trade against assets held in a pool, and smart-contract logic calculates the exchange according to the pool’s state and its pricing mechanism. This is one model used by decentralized exchanges (DEXs), not a description of every DEX or every AMM.

That distinction matters for system design. An order-book exchange represents bids and asks and matches compatible orders. A pool-based AMM instead exposes a pool’s available inventory to a swap and updates its state when the transaction executes. The two approaches differ in how liquidity is represented, how a trade obtains a price, and where execution and settlement occur. They also have different operational dependencies and risks.

## What Automated Market Makers Crypto means

An AMM is a trading mechanism in which a programmed rule uses pool state to determine the terms of a swap. In the Uniswap v2 model, for example, a pool holds deposited reserves of a token pair, and those reserves supply the inventory used for swaps. Liquidity-provider (LP) shares represent contributions to that pool. This is a concrete constant-product AMM example; other AMMs may use different curves, assets, fees, and accounting.

In an AMM-based DEX model discussed by the Bank for International Settlements (BIS), smart contracts and liquidity pools implement trading, and transactions settle when included in a blockchain block. The contract-mediated path means the trade is not simply an internal update to a centralized venue’s order book. The exact execution path remains design-dependent: order-book, auction, intent-based, cross-chain, and hybrid DEXs can work differently.

“Automated” describes how the pricing and execution rules are applied, not a promise that a trade will execute at a fixed price, immediately, or without external dependencies. A pool’s state changes as swaps and other pool operations occur. A quote is therefore tied to a particular state and execution context; it should not be treated as a guarantee of the eventual result.

## Core components of Automated Market Makers Crypto

A pool-based AMM typically brings together several functional pieces, although their implementation varies by protocol:

- **Pool inventory and state:** The pool holds assets available for swaps. In Uniswap v2, the relevant inventory is the deposited reserves of a token pair. The state used by the pricing rule changes as transactions execute.
- **Pricing rule:** A contract applies a defined mechanism to the pool state to calculate a swap. The constant-product example is only one design; the source evidence does not establish one universal AMM formula.
- **Smart contracts:** In the AMM DEX model described by BIS, contracts implement trading. Their behavior is specific to the deployed protocol and version.
- **Liquidity providers:** LPs contribute assets to a pool. In Uniswap v2, shares represent those contributions. The value and composition of a position can change as pool prices and activity change.
- **Transaction and blockchain infrastructure:** A user’s transaction must be submitted and included in a block for settlement in the BIS model. Public transaction visibility and execution ordering can affect some public-blockchain AMM trades before inclusion.
- **User-facing and integration software:** Wallets, interfaces, routers, or other applications may help users construct or submit transactions. Their exact role and trust assumptions depend on the implementation; an interface is not itself proof of what the on-chain contract will execute.

These components form a boundary between the pricing mechanism and the surrounding system. The pool rule can define how a swap changes pool state, but it does not by itself ensure that a submitted transaction is included, that a displayed quote remains current, or that an interface accurately communicates all execution parameters.

## How Automated Market Makers Crypto works

A typical pool-based swap can be understood as a sequence. Exact steps, fee handling, routing, and user protections vary by protocol and application.

1. **A user selects a swap.** The user specifies the assets and amount through a wallet or application. The application may read pool state and present an estimated exchange, but the source pack does not establish a universal interface or quote method.
2. **A transaction is formed and submitted.** The transaction calls the relevant smart-contract path. The user’s chosen parameters and the contract’s rules determine what the transaction permits; those details must be checked for the particular implementation.
3. **The transaction competes for block inclusion.** In public-blockchain AMM execution analyzed by BIS, public transaction visibility, execution ordering, pool depth, and price impact before block inclusion can affect a swap. Private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model, so this observation should not be generalized to every AMM deployment.
4. **The contract applies the pricing rule to pool state.** The pool’s inventory and the selected mechanism determine the exchange. A swap changes pool state; the output depends on the state and execution conditions when the transaction is processed, rather than only on an earlier interface display.
5. **The transaction is included and settles.** In the BIS AMM DEX model, settlement occurs when the transaction is included in a blockchain block. This differs from an exchange that records a trade internally before any later asset withdrawal or on-chain transfer.
6. **Pool accounting reflects the operation.** The pool’s reserves and related accounting are updated according to its implementation. LP claims or shares represent contributions in the Uniswap v2 example, but other protocols may account for positions differently.

A simple illustration is a swap against a two-token pool. A trader supplies one token and receives the other according to the pool’s rule and current inventory. A larger trade relative to available pool depth can have greater price impact. The exact output cannot be derived from the phrase “AMM” alone: it requires the specific curve, pool balances, fees, transaction parameters, and execution state.

## How pool pricing differs from an order book

In an order book, participants submit bids and asks at stated prices, and the venue’s matching process pairs compatible orders. A trade’s available counterparties and execution price depend on the orders present and the venue’s matching rules. In an AMM pool, the pool’s inventory and pricing rule provide the trading counterparty mechanism; the swap changes the pool state and can move the price implied by that state.

This creates a different meaning for liquidity. Order-book liquidity is represented by resting orders at price levels. Pool liquidity is represented by assets committed to the pool under its design. Pool depth and the size of a swap relative to that depth affect price impact. The labels are not interchangeable, and neither model guarantees stable liquidity under all conditions.

The operational contrast is also important. BIS describes centralized exchanges as able to provide near-real-time trading, liquid order books, and advanced order functionality after assets are deposited, while noting that performance and liquidity vary by venue, pair, and market conditions. The AMM DEX model instead uses smart contracts and pools, with transactions settled when included in a blockchain block. This is a general model comparison, not a claim that every centralized exchange or DEX has identical performance or features.

## Trust and control boundaries

A technical review should separate what the pool contract specifies from what the complete trade path assumes. A contract’s documented pricing and accounting rules concern its own logic. They do not establish the reliability of a wallet, interface, transaction-submission path, block production, or other integration. Nor does the AMM label indicate who controls every component or whether a system is fully decentralized in every operational sense.

Likewise, a pool is not a guarantee of a particular execution price. A user-facing quote can become stale as pool state or execution conditions change. For public-blockchain AMM execution covered by BIS, visibility and ordering can affect trades before inclusion; alternative designs may change that exposure. Teams should identify which execution model applies rather than assume that all chains, pools, or routing paths share the same ordering properties.

LP participation introduces a separate exposure. BIS describes LPs as potentially experiencing inventory-value loss relative to holding the assets when pool prices move; trading fees may or may not offset it. The outcome depends on pool design, price path, range, fees, timing, and withdrawal state. This is commonly called impermanent loss, but the label does not imply that a later recovery or fee offset is assured.

## Limitations and failure modes

AMMs do not eliminate the need to assess liquidity, execution, and implementation. A pool may have limited depth for a particular trade, and price impact can be material relative to that depth. The precise effect depends on the pool’s design and state, so a generic description cannot establish an expected output for a live transaction.

Block inclusion and transaction ordering are additional dependencies for public-blockchain AMM execution. A transaction may encounter a changed pool state or a different position in the ordering than the user expected. BIS identifies public visibility, ordering, depth, and price impact before inclusion as relevant factors in its analyzed setting. The stated exceptions matter: private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model.

LPs face exposure that differs from simply holding the deposited assets. Price movement can change the inventory value of a pool position relative to holding, and fees may or may not offset the difference. No single outcome applies across pools because the result depends on design, price path, range, fees, timing, and withdrawal state.

Finally, the word AMM does not identify a single formula or complete system architecture. Uniswap v2’s reserve-based token-pair pool is one example. Other AMMs can differ in curves, assets, fees, and accounting; DEXs can also use order books, auctions, intents, cross-chain mechanisms, or hybrids. Applying assumptions from one implementation to another without checking documentation can lead to incorrect conclusions.

## What teams should verify

Before integrating with or evaluating an AMM, technical and operations teams can build an evidence trail around the particular deployment:

1. **Identify the exact design and version.** Confirm whether the system is a pool-based AMM and which pool and pricing model apply. Do not infer a constant-product mechanism merely from the AMM label.
2. **Inspect pool state and accounting.** Determine which assets make up the pool, how reserves or positions are represented, and what LP shares or claims mean in that version. For Uniswap v2, the documented example uses deposited token-pair reserves and LP shares representing contributions; do not assume other protocols use the same accounting.
3. **Trace the swap path.** Follow how an application constructs a transaction, which contract receives it, how the pricing rule is applied, and when the transaction is considered settled. Establish whether routing or other intermediaries change the path.
4. **Check execution assumptions.** Determine the relevant chain and transaction-ordering model. For a public-blockchain path, assess how visibility, ordering, pool depth, and price impact can affect execution before inclusion. Verify whether an alternative design changes those conditions rather than assuming it does.
5. **Separate quote from execution.** Establish which pool state and parameters a displayed quote reflects, what the submitted transaction actually encodes, and how a state change before inclusion is handled. The available source claims do not define universal slippage controls or transaction protections, so those require version-specific documentation.
6. **Evaluate LP accounting and exposure separately.** Confirm how contributions, fees, withdrawals, and position value are computed in the implementation. Assess inventory-value movement relative to holding using the relevant design and conditions; do not assume fees will offset it.
7. **Document dependencies and evidence dates.** Record the protocol documentation, deployed version, chain, interface or integration path, and date of verification. Recheck when any of those change, because implementation-dependent assumptions should not be carried over automatically.

The central distinction is architectural: an AMM uses pool inventory and a pricing mechanism to make trades, while an order book expresses liquidity as bids and asks matched under a venue’s rules. That difference shapes how price is formed and how liquidity is exposed, but it does not by itself determine execution quality, control, or risk. Those depend on the specific pool, contracts, transaction path, and operating environment.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
