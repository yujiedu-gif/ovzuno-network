---
title: "LP tokens crypto: what they represent in liquidity pools"
description: "Learn what LP tokens crypto protocols may issue for liquidity-pool deposits, what position they represent, and why redemption rights and risks vary."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["lp token crypto"]
author: "editorial_team"
primary_keyword: "lp tokens crypto"
owned_question: "What are LP tokens in crypto, what claim do they represent in a liquidity pool, and what can affect their value or use?"
risk_level: "medium"
---

LP tokens are protocol-specific representations of a liquidity provider’s position in a pool, not universal receipts for a fixed quantity of crypto. What the token accounts for, what a holder can do with it, and which assets may be available on withdrawal depend on the pool’s rules and changing balances.

## What LP tokens represent in a liquidity pool

A **liquidity pool** is a collection of assets held for a protocol’s trading or other defined operations. In a Uniswap v2 example, a pool pairs two tokens, holds deposited reserves as swap inventory, and uses liquidity-provider shares to represent contributions. Those shares are one specific pool design, not a definition that applies to every token called an LP token. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>) [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>)

“LP” means **liquidity provider**: a participant who contributes assets to a pool. An LP token or share is associated with that participant’s pool position. Its meaning is determined by the protocol’s implementation and accounting rules. It should not automatically be read as a receipt that promises the return of the same quantities originally contributed, or as a claim to a fixed amount of each pool asset.

Automated market makers, or **AMMs**, are protocols that use liquidity pools to facilitate trades. The Uniswap v2 example uses paired-token reserves, but other AMMs can use different curves, assets, fees, and accounting. Those differences affect how a position is represented and how its pool operates. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

The practical starting point is therefore to identify the specific protocol, pool, and position representation. The general phrase “LP token” names a broad role in pool accounting; by itself, it does not tell a reader exactly what rights or functions a particular token has.

## How a liquidity contribution can result in LP tokens

At a high level, a provider contributes assets to a pool, and the protocol records that contribution according to its accounting rules. Some protocols represent contributions with pool shares or tokens. In Uniswap v2, liquidity-provider shares represent contributions to a pool whose reserves serve as inventory for swaps. That documented example illustrates the connection between a contribution and a position representation; it does not establish an identical issuance formula for other pools. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

After contribution, the position remains tied to the pool’s accounting rather than being a static copy of the original deposit. In the Uniswap v2 model, swaps execute against deposited reserves. As pool activity changes those reserves, the assets associated with a provider’s position can differ from the assets initially contributed. The precise accounting and any issuance or withdrawal calculations depend on the protocol and pool design. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

This is why the word “token” can be misleading if it is taken to mean a simple deposit slip. A deposit receipt might suggest that the holder can present it to recover an unchanged deposit. An LP representation instead connects a holder to a protocol-defined pool position. The protocol’s rules determine what the representation tracks and what actions it enables; the label alone does not establish a fixed amount owed.

For an unfamiliar pool, check its documentation for the relationship between contributions, shares, and reserves. A familiar design can provide a useful illustration, but it cannot substitute for the rules of a different pool.

## What an LP token may let its holder do

An LP token may be used to account for a share of a pool position. Whether the holder can use it to request withdrawal—and what the withdrawal returns—depends on the pool’s rules. The token’s existence alone does not establish a guaranteed redemption amount, immediate access to assets, or availability of a particular quantity of either pool asset.

In the Uniswap v2 example, shares represent contributions while pool reserves supply inventory for swaps. That explains the relationship between shares and the pool, but it does not establish universal redemption terms, a fixed value, or a guaranteed amount for every pool position. Other AMMs can use different accounting and pool structures. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

A position representation may also have additional uses in some designs. Those uses should be treated as protocol-specific capabilities, not assumed from the general term “LP token.” To establish a capability, look for documentation describing the relevant token and the operation it supports. This article does not prescribe procedures for minting, staking, redeeming, or recovering a particular token.

It is useful to separate three questions: what the token represents in the pool’s accounting, what actions the protocol permits for its holder, and what assets might be available under the applicable withdrawal rules. A description of the first does not automatically answer the second or guarantee the third.

## Why the value and recoverable assets can change

Pool reserves are used as trading inventory in the Uniswap v2 example. When swaps change those reserves, the composition of the pool changes too. A provider’s position is associated with the pool’s accounting, so the assets associated with that position need not remain in the same proportions as the original contribution. Other AMMs can use different pool designs, so the exact mechanics are not universal. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

One risk commonly called **impermanent loss** is an inventory-value loss relative to holding the contributed assets when pool prices move. Whether trading fees offset that loss depends on the pool design, price path, range, fees, timing, and withdrawal state. The term describes a risk mechanism; it does not say that a provider will experience a particular result. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

Fees also depend on the pool’s rules and the position’s status. In Uniswap’s documented fee model, swap fees are allocated proportionally to liquidity providers with active positions, while out-of-range concentrated positions do not earn those fees. Fee tiers, protocol fees, active ranges, and distribution mechanics vary by pool and version and can change. These scoped mechanics should not be treated as a promise that every LP position earns fees. [source](<https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee>)

Other risks identified for liquidity provision include smart-contract vulnerabilities, untrusted tokens, liquidity withdrawal by others, and management or network costs. The list is not exhaustive, and exposure differs by protocol, token, network, pool, and position configuration. [source](<https://support.uniswap.org/hc/en-us/articles/37113550065549-What-are-the-risks-when-providing-liquidity>)

Taken together, these mechanisms mean that a position’s associated assets, potential fee allocation, and exit conditions can vary. A token label does not guarantee that a pool can return a specific quantity on demand, and fee availability does not establish that fees will offset other risks.

## What to verify before interacting with an LP token

Start with authoritative documentation for the specific protocol and pool. Confirm how the pool accounts for contributions and shares, and how its rules describe the position. For a Uniswap v2 pool, for example, the documented model links provider shares to contributions and uses the pair’s reserves as swap inventory; that is not evidence that a different pool uses the same design. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

Then check the details that determine what the position may represent in practice:

- **Pool assets and accounting:** Identify the assets in the pool and the documented relationship between a provider’s contribution, the position representation, and changing reserves.
- **Withdrawal rules:** Find the protocol’s stated withdrawal conditions and what the rules say about the assets returned. Do not infer a fixed redemption amount from the token label.
- **Fee mechanics:** Check whether the pool documents fees, how they are allocated, and whether eligibility depends on the position’s status. For the documented Uniswap fee model, active positions receive proportional fee allocation and out-of-range concentrated positions do not earn those fees. [source](<https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee>)
- **Position-specific risks:** Review applicable disclosures concerning contract vulnerabilities, tokens, liquidity, and management or network costs. Risk lists can differ and are not exhaustive. [source](<https://support.uniswap.org/hc/en-us/articles/37113550065549-What-are-the-risks-when-providing-liquidity>)
- **Exact representation:** Use protocol materials to identify the particular pool and position token rather than assuming similarly named tokens have interchangeable rules.

These checks clarify documented mechanics; they do not predict an outcome. An LP token can represent a pool position, but its accounting, possible uses, fee treatment, and withdrawal conditions are specific to the relevant protocol and design. Understanding those boundaries is the first step in distinguishing a pool-position representation from a simple receipt.

This explanation does not determine legal, tax, or compliance treatment, which requires separate, applicable guidance.

## Sources and references

- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [What is a liquidity provider (LP) fee?](https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee) — Uniswap Labs Support; retrieved 2026-10-19.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [What are the risks when providing liquidity?](https://support.uniswap.org/hc/en-us/articles/37113550065549-What-are-the-risks-when-providing-liquidity) — Uniswap Labs Support; retrieved 2026-10-19.
