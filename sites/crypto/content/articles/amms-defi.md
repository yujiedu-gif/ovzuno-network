---
title: "AMMs DeFi: How Pool-Based Trading Works in Protocols"
description: "Learn how AMMs DeFi protocols use liquidity pools to facilitate swaps, how pricing relates to pool balances, and what liquidity providers do."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "amms defi"
owned_question: "What role do AMMs play in DeFi protocols, and how do their pool-based trading mechanics connect swaps, liquidity, and pricing?"
risk_level: "medium"
---

AMMs in DeFi protocols use pools of contributed assets to execute swaps according to programmed rules. Liquidity providers supply assets to those pools; the AMM’s pool state and design-specific rules shape swap terms. The central connection is that pool inventory enables trades, trades change inventory, and those changes can affect later trades. The details vary by protocol, so no single pool structure or pricing method describes every AMM.

## AMMs DeFi: the protocol-level role

An automated market maker, or AMM, is a mechanism a protocol can use to facilitate trades through liquidity pools. A liquidity pool is a collection of assets held under rules that make them available for swaps. In a Uniswap v2 pool, for example, a token pair’s deposited reserves provide the inventory for swaps, and liquidity-provider shares represent contributions to the pool. This is one specific constant-product AMM example, not a universal template: other AMMs can use different curves, assets, fees, and accounting. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

A protocol’s rules and contracts are distinct from the interface a person may use to interact with them. The interface can display information or offer a way to submit a transaction, but it is not itself the pool’s inventory or the rules that govern the pool. When describing an AMM, it is therefore useful to separate the protocol-level mechanism from the user-facing path into it.

The term “AMM” does not, by itself, specify which assets a protocol supports or precisely how a particular pool operates. Those details depend on the implementation. A mechanism described for one pool should not be treated as a claim about all DeFi protocols that use pool-based trading. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## How a pool-based swap is structured

A pool-based swap draws on assets that have already been contributed to the pool. The pool’s reserves are the inventory from which a swap can be executed. In a two-token example, a trader supplies one asset and receives another according to the pool’s rules. The trade changes the amounts held in the pool: one asset is added while the other is removed. The resulting balances become part of the pool state for later swaps. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

This is execution through a pool, rather than a direct match between two individual traders’ orders. The pool’s contract logic applies the relevant rules, and the assets available in the pool form the inventory for the exchange. That description is specific to pool-based execution; other exchange designs can have different paths, and even AMMs differ in their assets, curves, fees, and accounting. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

For a builder or operator, the distinction helps clarify what must be described or verified. The pool and its rules define the mechanism; an interface is a separate way to present or access it. A description of the interface alone does not establish the pool’s exact behavior, while an example of one pool does not establish how every other protocol executes swaps.

## Where AMM pricing comes from

In a pool-based AMM, the terms of a swap are connected to the pool’s state and the protocol’s rules. Because a swap changes the pool’s asset balances, the state after one trade can affect the terms available for a subsequent trade. A swap rate is therefore not simply a fixed property of the token pair: it reflects how the particular pool and its design handle the trade. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

A pool’s swap terms should also be distinguished from an external market price. The pool’s mechanism determines the exchange terms available through that pool under its rules and current state. That fact alone does not establish that the terms match a price observed elsewhere. The distinction is important when interpreting a quote: it describes an exchange through a particular pool, not a universal valuation of either asset.

No one formula should be assumed across all AMMs. The Uniswap v2 example uses a particular pool design, while other AMMs can use different curves, assets, fees, and accounting. Those design choices affect how pool state relates to swap terms, so a technical explanation or integration needs to be tied to the particular protocol and pool rather than relying on the AMM label alone. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## Liquidity providers and pool changes

A liquidity provider contributes assets to a pool under that pool’s rules. In AMM designs, providers can receive a share of trading fees, while bearing inventory and adverse-selection risk. The pool formula, fee tiers, price ranges, and allocation of losses vary by protocol and position. The possibility of fee income is not a guarantee of profit or a complete account of the provider’s exposure. [source](<https://www.bis.org/publ/work1227.pdf>)

Contributions and withdrawals affect the pool’s assets and composition. In the Uniswap v2 example, provider shares represent contributions to a reserve-holding pool; this accounting should not be generalized to every AMM. Because pool state is relevant to swap terms, changes in inventory can also affect later trades under the applicable rules. The specific accounting for deposits, withdrawals, and provider positions must be checked for the design in question. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

Liquidity provision can involve a change in inventory value relative to holding the contributed assets. An AMM liquidity provider can experience such a loss when pool prices move, and trading fees may or may not offset it. The outcome depends on pool design, the price path, range, fees, timing, and withdrawal state. This describes a type of exposure, not a prediction of any provider’s result. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## Protocol design choices and risk boundaries

The pool mechanism connects three elements: contributed assets supply inventory, swaps use that inventory under protocol rules, and those swaps alter pool balances. Liquidity providers contribute to the inventory and may receive a share of fees, but their position can also carry inventory and adverse-selection risk. The precise relationship among pool state, swap terms, accounting, and provider exposure depends on the particular design. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>) [source](<https://www.bis.org/publ/work1227.pdf>)

An AMM description alone does not establish a protocol’s security, audit status, incident history, recovery options, current fees, yields, or availability. Those are distinct questions about a specific implementation and require current, authoritative evidence. This explanation also makes no legal, compliance, or tax conclusion. Its purpose is to explain how pool inventory, swaps, pricing rules, and liquidity provision relate—not to assess a particular protocol or recommend participation.

## Sources and references

- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
