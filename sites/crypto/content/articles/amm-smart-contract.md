---
title: "How an amm smart contract prices and executes token swaps"
description: "Learn how an amm smart contract uses pool reserves to set swap terms, update state, and expose users and liquidity providers to distinct risks."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["automated market maker", "liquidity pool", "decentralized exchange", "constant-product formula"]
author: "editorial_team"
primary_keyword: "amm smart contract"
owned_question: "How does an automated market maker smart contract use a liquidity pool to quote and execute token swaps, and what assumptions and risks shape that process?"
risk_level: "medium"
---

An automated market maker (AMM) smart contract applies programmed rules to token swaps against assets held in a liquidity pool. The pool’s reserves—the quantities of its assets—provide the swap inventory. The contract’s design determines how those reserves shape a trade and how pool accounting changes when a swap executes. A constant-product pool is one example, not a rule for every AMM. Pool terms and outcomes depend on the specific design and state; a quote or completed swap does not establish that a trade is favorable.

## What an AMM smart contract does

A liquidity pool is inventory held for swaps. In one familiar arrangement, a pool pairs tokens in a smart contract. The reserves are the assets from which swaps execute, while liquidity-provider shares represent contributors’ portions of the pool. These are features of the Uniswap v2 pool model, not a universal specification for every AMM. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The contract, pool, and application have different roles. The contract is code that applies defined operations according to its program, inputs, and current state. The pool is the particular asset inventory and associated accounting that the swap mechanism uses. A user interface may show a proposed trade and help prepare a request, but the interface is not itself the pool or the contract. This distinction matters because a screen’s estimate describes a proposed interaction; the deployed contract applies its rules when the transaction is executed.

AMMs are not all built alike. Pool formulas, assets, fees, and accounting can vary. A description of a reserve-based, two-token pool can explain one mechanism, but it cannot establish the details of another pool or deployment. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## How pool reserves shape swap pricing

In a reserve-based pool, a swap exchanges one asset for another held in the pool. The pool’s relative quantities change: it receives the asset supplied and gives out the asset requested, subject to the pool’s rules. The quantities available in the reserves and the size of the requested swap therefore matter to the terms the mechanism can offer.

A constant-product formula is one way to relate the quantities of two pool assets. It constrains how the reserves can change as a trade occurs and can be used to derive an exchange amount from the pool’s state. It is an illustrative design rather than a definition of all AMMs. Other AMMs may use different curves, assets, fees, or accounting, so one should not infer a particular formula from the AMM label alone. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The quote is a view of potential execution based on the pool information and parameters used to calculate it. Pool state may change before a transaction executes, so a previously displayed amount is not necessarily the amount the contract will accept. The actual result depends on the implementation and state encountered at execution, along with the conditions specified for the request. A quote describes neither a guaranteed outcome nor the value of an asset outside that pool.

Pool pricing and external prices are also separate concepts. The pool’s reserves and rules generate its swap terms; they do not by themselves establish an external reference price. In public-blockchain AMM execution, transaction visibility, ordering, pool depth, and price impact before block inclusion can affect a swap. The relevance of those factors depends on the system and execution design.

## From swap request to on-chain state update

A user or application first prepares a transaction request for a proposed exchange. The interface may display assets, an estimated amount, or other trade constraints, but those details are not proof that a swap has taken place. The request must be submitted for the contract to act on it. The contract then applies its deployed rules to the request and the pool state available during execution.

If the applicable rules and conditions allow execution, the contract carries out the swap and updates the pool’s accounting according to its implementation. If those conditions are not met, the intended swap does not complete. The exact checks and accounting are design-specific; without examining a particular implementation, a general explanation cannot say precisely which conditions it enforces or how it handles every failure.

Keep three moments distinct when following a trade: the interface’s estimate, the submitted transaction, and the state change the contract actually makes. A submission is a request, not confirmation that the pool has changed. To understand an individual interaction, identify the pool and assets involved, inspect the request conditions presented by the application, and distinguish the proposed amount from the executed result. Those steps help clarify what the mechanism did; they do not establish that the contract or trade is safe.

## AMM pools compared with order-book matching

An AMM pool uses deposited reserves as swap inventory and applies programmed rules to determine how a trade changes that inventory. An order-book model organizes offers to buy and sell for matching. The conceptual difference is where the terms are derived: from pool state and rules in a reserve-based AMM, or from offers and matching in an order book.

The contrast is useful, but it is not a claim that every exchange fits one of two simple templates. AMM designs differ, and order-book, auction, intent-based, cross-chain, and hybrid DEX designs can follow different execution paths. A label alone does not specify how a particular system handles requests or settles trades.

## Risks and assumptions to assess

**Contract and implementation risk.** A pool’s basic mechanism does not prove that its deployed code is correct, that its accounting matches a reader’s expectations, or that every connected component behaves appropriately. Smart contracts can call or reuse other on-chain components through public interfaces, but each dependency adds behavior, availability, upgrade, permission, and economic assumptions. Reviewing a pool therefore means looking beyond the generic description of an AMM and understanding the implementation and its dependencies.

**Pool and liquidity-provider risk.** A liquidity provider contributes assets to a pool and can receive a share of trading fees, while bearing inventory and adverse-selection risk. If pool prices move, a provider can experience an inventory-value loss relative to holding the assets outside the pool; fees may or may not offset that loss. Outcomes depend on pool design, the price path, timing, and withdrawal state, among other conditions. These are risks to assess, not predictions about any particular pool’s result. [source](<https://www.bis.org/publ/work1227.pdf>) [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

**Execution and user risk.** Pool state and transaction conditions both matter, so an estimate should not be treated as a guaranteed final amount. Before authorizing a request, a user can check that the asset identities and transaction parameters shown by the application match the intended action. The user interface communicates the proposed interaction; the contract and pool determine what happens on execution under their rules. Neither a familiar interface nor the existence of a pool establishes that a specific interaction is risk-free.

The central mechanism is straightforward but bounded: reserves provide inventory, programmed rules determine swap terms, and execution can update pool state. The formula, checks, accounting, and dependencies are specific to the implementation. Understanding those distinctions explains how a reserve-based AMM works without treating a displayed quote as a completed trade or treating the AMM label as evidence of safety.

## Sources and references

- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
