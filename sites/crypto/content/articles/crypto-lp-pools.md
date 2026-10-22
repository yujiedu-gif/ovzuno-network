---
title: "Crypto LP Pools: How Liquidity Provision Works and What to Check"
description: "Learn how crypto lp pools hold contributed assets, how provider positions may be accounted for, and which design details and risks to examine."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: []
author: "editorial_team"
primary_keyword: "crypto lp pools"
owned_question: "What are crypto liquidity-provider (LP) pools, how do participants supply liquidity, and what risks and design choices shape how these pools work?"
risk_level: "medium"
---

Crypto LP pools hold assets supplied by liquidity providers under pool-specific rules. Participants contribute assets and receive a position or accounting claim defined by the implementation; that claim is distinct from the pool’s total reserves. Pool design determines how contributions are recorded, how activity changes the asset mix, whether fees apply, and what a provider can withdraw. The mechanics and risks therefore need to be checked for the particular pool rather than inferred from the general label “LP pool.”

## What a crypto LP pool represents

A liquidity pool is a reserve of assets used by a protocol for activities such as swaps. In one concrete example, a Uniswap pool pairs tokens held in a smart contract for decentralized-exchange swaps. A Uniswap v2 pool uses reserves of a token pair as swap inventory, and liquidity-provider shares represent contributions to those reserves. These describe that pool model, not every design used in decentralized finance. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

It helps to separate three things: the pool’s assets, the pool’s rules, and a provider’s position. Reserves are the assets held by the pool at a particular time. The rules specify how the pool uses those assets and keeps its accounting. The provider’s position represents a claim or contribution recorded according to those rules. In the Uniswap v2 example, provider shares represent contributions to reserves; they are not the reserves themselves. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

A pool’s position record should not be read as a promise to return the exact quantities originally contributed. When pool activity changes reserves, the pool’s current asset composition may differ from the composition at the time of deposit. The position’s accounting and the pool’s withdrawal rules determine what a provider can claim. Other AMMs can use different curves, assets, fees, and accounting, so the Uniswap v2 description is an illustration rather than a universal template. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

## How providers contribute and account for assets

A provider needs to identify what assets a particular pool accepts and how it defines a contribution. For the Uniswap pool example, the pool is a pairing of tokens; the v2 example uses deposited reserves of a token pair. Those facts do not establish that all pools require two assets, require equal-value deposits, or use the same contribution process. Other pool structures can differ, and the available evidence does not specify universal eligibility conditions. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

After assets are contributed, the pool’s accounting defines the provider’s position. In Uniswap v2, liquidity-provider shares represent contributions to reserves. A different implementation may use a different form of position accounting, so a reader should check the relevant protocol documentation or contract specification for how it records a contribution and calculates a claim. The term “share” should be used for the Uniswap v2 example, not assumed to describe all LP positions. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

Withdrawal is also implementation-specific. The basic question is not simply whether a provider can withdraw, but how the pool calculates the assets and amounts available under its rules and current state. A provider should verify whether a withdrawal is represented as a changing mix of assets and whether any conditions apply to that position. The evidence here establishes that reserve-based swaps can use pool inventory and that LP outcomes depend on pool and position conditions; it does not establish uniform withdrawal procedures or guarantees across protocols. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>) [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## How pool activity can affect a provider’s position

In a reserve-based swap pool, a trade uses assets held in the pool. The Uniswap v2 pool’s reserves are the inventory from which swaps execute. As that inventory is used, the quantities of the paired assets can change. A provider’s position is therefore tied to the pool’s accounting and current state, not simply to a static copy of the original deposit. [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>)

Fees are another pool-specific feature. In the documented Uniswap fee model, swap-input fees are allocated proportionally to liquidity providers with active positions; out-of-range concentrated positions do not earn those fees. This is a specific rule for the described Uniswap mechanics, not a statement that every LP pool charges fees, distributes them the same way, or treats every position as eligible. Check the current rules for the exact pool and position. [source](<https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee>)

Liquidity provision can also change a provider’s asset exposure. Providers contribute assets to pools and can receive a share of trading fees, while bearing inventory and adverse-selection risk. The fee share does not establish a fixed return, and the presence of fees does not show that they will offset a change in the provider’s inventory value. [source](<https://www.bis.org/publ/work1227.pdf>)

One way to describe this exposure is inventory-value loss relative to holding the assets when pool prices move, commonly called impermanent loss. The name does not mean the difference is certain to reverse or that fees will cover it. The outcome depends on factors including pool design, price path, position range, fees, timing, and withdrawal state; fees may or may not offset the loss. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## Risks and design details to examine

Start by distinguishing the pool’s mechanics from the provider’s exposure. A pool’s reserve model describes what assets it holds and how those assets are used. A position model describes how a provider’s contribution is represented. A fee model describes whether and how a share of fees is allocated. Those are related but separate questions: understanding one does not establish the rules or risks of the others. Pool formulas, fee arrangements, position conditions, and loss allocation vary by protocol and position.  [source](<https://www.bis.org/publ/work1227.pdf>)

Next, consider how changing asset composition could affect the provider’s position. A provider’s inventory value can fall relative to holding the assets, and the result may depend on the route prices take, the position range, fees, timing, and withdrawal state. That is a possible outcome, not a fixed result for every pool. The available evidence supports this inventory and adverse-selection risk; it does not substantiate security ratings, audit outcomes, incident histories, recovery procedures, oracle or bridge controls, or governance protections for a particular pool. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>) [source](<https://www.bis.org/publ/work1227.pdf>)

Finally, verify current terms rather than extrapolating from a familiar pool or interface. In the Uniswap fee example, active-position status matters, and out-of-range concentrated positions do not earn the described fees. Fee tiers, active ranges, protocol fees, and distribution mechanics can vary by pool and version and can change. Do not treat a fee description as a promised return or assume it applies to a different implementation. [source](<https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee>)

## Questions to answer before interacting

Use the documentation for the specific pool to answer these mechanics-focused questions:

- Which assets does the pool hold, and what assets or conditions apply to a contribution?
- How is a provider’s position recorded, and how does that accounting relate to the pool’s reserves?
- How does pool activity change the reserve composition, and what asset mix can the position represent afterward?
- What rules determine the amounts and assets available on withdrawal?
- Do fees apply to this position? If so, how are they allocated, and are there position conditions that affect eligibility?
- Which risks follow from this pool’s particular formula, assets, and accounting rather than from LP pools as a broad category?

These questions are a way to organize a technical review, not a recommendation to use any pool. The evidence here supports a Uniswap reserve-and-share example, pool-dependent mechanics, a specific fee allocation example, and the possibility of inventory-value and adverse-selection risks. It does not establish universal eligibility, contribution ratios, withdrawal guarantees, returns, security outcomes, or jurisdiction-specific treatment. Those details require current evidence about the pool and position being considered. [source](<https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool>) [source](<https://developers.uniswap.org/docs/protocols/v2/concepts/pools>) [source](<https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee>) [source](<https://www.bis.org/publ/work1227.pdf>) [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [What is a liquidity pool?](https://support.uniswap.org/hc/en-us/articles/8829880740109-What-is-a-liquidity-pool) — Uniswap Labs Support; retrieved 2026-10-19.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [What is a liquidity provider (LP) fee?](https://support.uniswap.org/hc/en-us/articles/20901935681677-What-is-a-liquidity-provider-LP-fee) — Uniswap Labs Support; retrieved 2026-10-19.
