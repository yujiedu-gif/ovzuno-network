---
title: "Crypto AMM: How Pool-Based Trading and Pricing Work"
description: "Learn how a crypto amm uses liquidity pools and pricing rules to facilitate trades, and understand key design trade-offs and risks."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "crypto amm"
owned_question: "What does “crypto AMM” refer to as a protocol design, and how do its pool-based trading and pricing mechanisms work at a high level?"
risk_level: "medium"
---

A **crypto automated market maker (AMM)** is a protocol design that uses a programmed pricing mechanism to facilitate trades against assets held in a liquidity pool. The pool supplies trade inventory, and the pricing rule determines exchange terms from the pool’s state or other design-specific inputs. Because pool structures and rules vary, the label “AMM” alone does not identify a universal formula, fee, or execution outcome.

## What the term crypto AMM describes

An AMM describes how a protocol organizes trades; it is not itself the name of a particular application, blockchain, or token. In a pool-based design, a trader exchanges assets against inventory held in a pool rather than being directly matched with a named counterparty. A smart contract may implement the pool and the rules governing swaps, while an application interface presents information and helps communicate with that system. These components have related but distinct roles.

A liquidity pool is a supply of assets available for trading under the protocol’s rules. In one specific example, a Uniswap v2 liquidity pool uses deposited reserves of a token pair as swap inventory, and liquidity-provider shares represent contributions to those reserves. That example describes one constant-product AMM model. Other AMMs can use different curves, assets, fees, and accounting, so it should not be treated as a definition of every pool.

The pricing mechanism is the programmed rule connecting a pool’s state to the exchange terms it offers. Some rules use pool balances as inputs, but the general AMM label does not specify which curve or accounting method is used. To understand a particular system, a reader needs its technical documentation and the applicable implementation details, not just its category name.

## How a pool-based trade changes the pool

At a high level, a pool-based trade has three conceptual parts. First, the trader supplies an asset to the pool. Second, the pool provides another asset from its available inventory. Third, the pool’s balances change to reflect what entered and left. In the Uniswap v2 example, deposited reserves of a token pair are the inventory from which swaps execute. The precise accounting and execution path depend on the design.

This sequence differs from describing a trade as a direct exchange between two specifically identified traders. The pool makes inventory available, and the protocol’s pricing rule calculates the exchange terms for the trade. This description is conceptual: it does not specify a transaction procedure, a particular contract, or a guaranteed outcome.

Consider a two-asset pool as an illustration. When a trade adds some of one asset and removes some of the other, the relative pool balances change. If the pricing rule uses those balances, the updated state can affect the terms available for a subsequent trade. The example explains the relationship between a trade and pool state; it does not establish a universal formula or predict a particular rate.

Pool inventory also places a limit on what the mechanism can supply at a given moment. A pool’s available reserves are not interchangeable with an unlimited supply of either asset. The amount and composition of inventory are part of the pool state, and the protocol’s own rules determine how that state affects a proposed exchange. Readers should avoid assuming that two pools with similar names, assets, or displayed information behave identically.

## Pricing rules, liquidity, and execution

A pricing rule determines how a protocol relates the pool’s state or other inputs to an offered exchange rate. Different AMMs can use different curves and accounting, which is why “AMM” does not disclose the underlying formula. In a balance-based design, a trade that changes balances can also change the state used by the pricing rule. The effect of a given trade depends on that rule and the pool’s available inventory.

Liquidity is relevant to execution, but it is not a single fixed property that can be inferred from the word “pool.” Pool depth, trade size, and the implementation’s pricing method affect the relationship between an indicated rate and the trade’s result. A relatively large trade compared with available inventory can encounter a different price impact than a smaller trade. The available evidence does not establish a universal threshold or numerical relationship, so exact effects must be checked for the particular implementation and conditions.

A displayed quote and an executed trade are also distinct concepts. A quote is information presented before execution; what the protocol ultimately records depends on the implementation and the conditions under which the trade is processed. In public-blockchain AMM execution, transaction visibility, ordering before block inclusion, pool depth, and price impact can affect a swap. This does not mean every AMM uses the same ordering model: private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter it.

Fees are another implementation-specific detail. A general AMM description does not establish whether a fee applies, its amount, how it is calculated, or how it is allocated. The Uniswap v2 pool example is useful for understanding reserves, but it does not establish fee rules for other systems. A technical review should therefore treat pricing, fees, and execution as separate items to verify in the relevant protocol documentation.

## Design trade-offs and protocol risks

Pool-based trading links execution to the inventory and rules of a particular pool. That relationship makes pool depth and trade size relevant to price impact. Public visibility and transaction ordering can also affect an AMM swap before block inclusion in some execution models. As a result, a displayed rate is not evidence, by itself, that a particular execution result is guaranteed.

Providing assets to a pool is a separate role from trading against it. A liquidity provider contributes assets to a pool and can receive a share of trading fees, while bearing inventory and adverse-selection risk. A provider can experience an inventory-value loss relative to holding the assets when pool prices move; fees may or may not offset that difference. The outcome depends on pool design, the price path, fees, timing, and the position’s withdrawal state. This describes possible protocol exposure, not a forecast about a pool or a recommendation to trade or provide liquidity.

Risk assessment should stay specific to the system being considered. The evidence supporting this explainer does not establish security reviews, incident histories, access controls, recovery options, upgrade processes, or protections for any named AMM. Nor does a description of pool mechanics demonstrate that an implementation is safe or that an application will behave as expected. Those claims require attributable, current evidence about the relevant contracts, application, and operational arrangements.

## What to verify before relying on an AMM

Start by identifying the system and the exact pool design being described. Primary technical documentation should clarify what assets the pool holds, how the pool accounts for them, which inputs the pricing rule uses, and how a trade changes pool state. A token-pair reserve model is one possible example, not a universal template.

Next, check the implementation’s own descriptions of fees, price-impact handling, and transaction execution. Where documentation shows an indicative quote, do not assume it guarantees the final outcome. The relevant conditions may include pool inventory, trade size, and the execution model. Avoid inferring supported assets, routing behavior, or protective features from the general AMM label.

Finally, separate protocol behavior from application and operational claims. An interface may present information about a pool, but that does not independently establish the underlying contract’s security, recovery process, or administrative controls. The evidence used here does not establish those details for a specific AMM. It also does not establish jurisdiction-specific availability, regulation, compliance obligations, or tax treatment; those issues require appropriate current sources beyond this technical overview.

The core mechanism is straightforward to describe but implementation-dependent: a pool supplies trade inventory, a programmed rule sets exchange terms, and a trade changes the pool state. Understanding a particular crypto AMM requires examining the pool structure and pricing rules that actually govern that system, rather than assuming all AMMs share one design.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
