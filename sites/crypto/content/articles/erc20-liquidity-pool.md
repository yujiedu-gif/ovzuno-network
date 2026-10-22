---
title: "ERC20 Liquidity Pool: How Token Pools Work"
description: "Learn how an erc20 liquidity pool uses a smart contract, token reserves, and liquidity providers to enable swaps, and what risks its mechanics leave unresolved."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["smart_contract_dapps"]
tags: ["automated market maker", "liquidity providers", "pool reserves", "smart contract risk"]
author: "editorial_team"
primary_keyword: "erc20 liquidity pool"
owned_question: "How does an ERC-20 liquidity pool hold and exchange tokens, and what roles do its smart contract, reserves, and liquidity providers play?"
risk_level: "medium"
---

An ERC-20 liquidity pool is an application-level arrangement in which a smart contract holds token reserves and applies programmed rules to exchange them. ERC-20 provides a token interface, not the pool itself: the pool’s pricing, provider accounting, fees, and withdrawal behavior depend on its particular design. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## What an ERC-20 liquidity pool is

A liquidity pool is a contract-based inventory of tokens used to execute swaps. In a common example, a pool pairs two tokens, holds them in a smart contract, and uses that inventory for exchanges on a decentralized exchange. The pool’s assets are called its reserves. Some designs track contributions using liquidity-provider shares, but that is a pool mechanism, not a property established by the token label. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The distinction between a token and a pool is central. A token is an asset represented and managed under its own contract rules; a pool is a separate application component that uses token balances to provide an exchange function. The pool may hold more than one token, and its own logic determines how it handles those assets. The fact that tokens are described as ERC-20 does not, by itself, specify the pool’s pricing rule, fee policy, or provider rights.

A pool is also different from an order book. In the pool model described here, a user swaps against token inventory held by the contract, rather than relying on the pool description to imply a matched buy order and sell order. This is a useful mental model, but implementations vary: the pool example does not define every decentralized exchange or every automated market maker. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## How the pool contract and token reserves interact

The contract’s rules govern how the pool uses its inventory for swaps. Reserves are the deposited token assets available for exchanges. When a swap executes, the pool draws from those reserves, and its token inventory changes according to the transaction and the pool’s accounting. In the Uniswap v2 example, reserves are the inventory from which swaps execute, and provider shares represent contributions. This illustrates one design rather than a universal accounting rule. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

At a high level, a user supplies one token and requests another according to the pool’s terms. The contract applies its programmed logic to the current pool state and the requested operation. The pool’s token balances and the pool’s own accounting therefore matter together: the reserves describe available inventory, while the contract rules describe how the swap uses it.

Exact mechanics require implementation-specific verification. Different AMMs can use different curves, assets, fees, and accounting. A description of one pool’s reserves cannot establish the accounting methods used by another, and a label such as “ERC-20 pool” does not supply those missing details. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## How automated market makers set swap terms

An automated market maker (AMM) is a pool-based arrangement in which programmed rules use pool state to determine swap terms. A constant-product pool is one example of an AMM design, not a universal requirement. Other AMMs can use different curves, assets, fees, and accounting, so the constant-product example should be treated as an illustration rather than a general description of all pools. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

A swap changes the token reserves used by the pool. As a result, trade size relative to the available inventory can affect the terms produced by a particular pool’s rule. The pool’s current state and design are therefore part of the swap mechanism; the general idea of a token pool does not imply one fixed price or one common formula across implementations. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The execution environment can matter as well. For public-blockchain AMMs, transaction visibility, execution ordering before block inclusion, pool depth, and price impact can affect a swap. These factors describe possible influences on execution, not a claim that every pool or transaction behaves identically. A pool’s own design and the surrounding execution conditions must be considered separately.

## What liquidity providers do—and what they receive

Liquidity providers contribute assets to pools. In the Uniswap v2 example, provider shares represent those contributions. The share mechanism is an accounting feature of that pool design; it should not be assumed to describe all ways a pool tracks a provider’s position. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

An AMM liquidity provider can receive a share of trading fees while contributing assets to the pool. The possibility of a fee share does not specify its amount, how it is calculated, or when it is available. Those details depend on the pool and position. Pool formulas, fee arrangements, price ranges, and loss allocation vary across protocols and positions. [source](<https://www.bis.org/publ/work1227.pdf>)

A provider’s pool position can also change in value relative to simply holding the contributed assets when pool prices move. This effect is commonly called impermanent loss. It is a comparison with holding, not a guarantee that the difference will later reverse. Trading fees may or may not offset the inventory-value loss. The outcome depends on factors including pool design, price path, position range, timing, and withdrawal state. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

This is why “providing liquidity” alone does not determine what a participant receives or the outcome of participation. The pool’s share records, fee rules, and withdrawal terms are implementation-specific. Neither a share mechanism nor the possibility of fees establishes a particular return or protects against changes in the value of the pool’s inventory. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>) [source](<https://www.bis.org/publ/work1227.pdf>) [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## Risks and limits to check before relying on a pool

The pool mechanism explains how contract-held token inventory can support swaps; it does not establish that a particular contract is correct or secure. Nor does the general model determine what administrative controls, upgrades, recovery options, or external integrations a particular implementation may have. These properties must be checked for that specific pool rather than inferred from its use of tokens or from the term “AMM.”

A practical review should identify the exact pool and token contracts, then examine how reserves and provider contributions are accounted for. Check the stated swap and fee rules, the method for tracking a provider’s claim, and the conditions for withdrawing assets. If the design uses external components, its documentation and contracts must be examined to understand how those dependencies affect operation. The general pool concept alone does not answer these questions.

Also distinguish a technical token position from rights associated with an underlying asset or a third party. In a U.S. federal securities-law context, a third-party tokenized security may represent an indirect custodial entitlement, a contractual claim, or synthetic exposure rather than direct ownership of the referenced security; its rights can differ from direct ownership. That example is not a general legal conclusion about liquidity pools, and the pool mechanism does not establish the rights attached to any particular token. [source](<https://www.sec.gov/newsroom/speeches-statements/corp-fin-statement-tokenized-securities-012826-statement-tokenized-securities>)

Finally, do not infer security, availability, fees, yields, token support, or compliance from the pool label. Those are implementation- and context-specific matters that require separate verification. The core mechanism is narrower: a contract uses token reserves for swaps, and providers contribute assets under rules that determine how their participation is represented and handled. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>) [source](<https://www.bis.org/publ/work1227.pdf>)

## Sources and references

- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [Statement on Tokenized Securities](https://www.sec.gov/newsroom/speeches-statements/corp-fin-statement-tokenized-securities-012826-statement-tokenized-securities) — U.S. Securities and Exchange Commission staff divisions; retrieved 2026-10-19.
