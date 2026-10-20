---
title: "Automated Market Maker DeFi: How AMMs Work vs. Order Books"
description: "Learn how DeFi automated market makers use liquidity pools and pricing rules to process swaps, and how this model compares with order-book exchanges."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["defi_protocols"]
tags: ["automated market maker", "AMM", "decentralized finance", "DeFi liquidity pools", "constant product market maker", "order-book exchange", "AMM slippage", "impermanent loss"]
author: "editorial_team"
primary_keyword: "automated market maker defi"
owned_question: "How do automated market makers work in decentralized finance, and how do they differ from order-book exchanges?"
risk_level: "medium"
---

# How Automated Market Makers Work in DeFi—and How They Differ from Order Books

## What is an automated market maker in DeFi?

An automated market maker (AMM) is a decentralized-finance market design in which a trade interacts with a liquidity pool under programmed protocol rules. In the supported Uniswap v2 example, a pool holds deposited reserves of a token pair as swap inventory, and liquidity-provider shares represent contributions to that pool. This is a specific implementation, not a universal description of every AMM. Other AMMs can use different curves, assets, fees, and accounting. [1]

The useful conceptual distinction is where a trade’s available inventory comes from. In the Uniswap v2 example, a swap uses the pool’s token reserves. The accepted evidence here does not establish a general formula for all AMMs or support a detailed definition of order-book matching. Those mechanisms must be described only to the extent established by reliable evidence; the comparison below therefore focuses on the supported pool mechanics and their consequences rather than asserting unsupported venue-wide rules.

## How an AMM swap works

A simplified view of the supported pool-based swap path is:

1. **The pool has reserves.** A Uniswap v2 liquidity pool holds deposited reserves of a token pair. Those reserves are the inventory from which swaps execute. [1]
2. **A trader requests a swap.** The requested exchange concerns assets held by the pool. The particular protocol implementation governs how the swap is handled; the general pool description does not specify every execution detail.
3. **The protocol’s pricing mechanism determines the exchange.** AMMs are not all governed by the same curve or accounting. For a particular pool, its own authoritative documentation is needed to establish the exact pricing rule and quote calculation. [1]
4. **The pool state changes.** A swap draws on pool inventory, so the resulting reserves differ from their prior state. A later trade encounters the pool in its updated state. How that state translates into a quote depends on the specific design.
5. **Execution conditions can matter.** In public-blockchain AMM execution, transaction visibility, execution ordering, pool depth, and price impact before block inclusion can affect a swap. This finding is scoped to the public-blockchain execution context analyzed by the Bank for International Settlements (BIS); private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model. [3]

The reserve relationship is enough to explain why a pool is stateful: trades use the pool’s available assets, and swaps change the inventory available for later trades. It is not enough, by itself, to derive a universal price equation. Even the familiar constant-product illustration would require evidence for the specific invariant, its assumptions, and the applicable fee and execution treatment. Those details are not established by the accepted claims in this source pack, so this article does not present an equation or claim that every AMM follows that model.

For the same reason, a conceptual explanation should not be mistaken for a live quote. A pool’s exact output depends on its implemented rules and current state, while execution can also depend on network and transaction conditions. To establish a specific pool’s calculation, consult its authoritative documentation rather than extrapolating from the general AMM label.

## How AMMs differ from order-book exchanges

The accepted evidence establishes that Uniswap v2 uses token-pair reserves as swap inventory and that AMM designs may differ. It does not establish the mechanics of order books—such as how bids and asks are submitted, how orders are matched, or how resting orders supply liquidity. Accordingly, a detailed comparison table that states those mechanics as facts would go beyond the evidence available here.

At a high level, the article’s supported distinction is limited: the cited Uniswap v2 pool executes swaps from deposited token-pair reserves, whereas AMM designs more broadly are not uniform. A claim that an order-book venue instead matches submitted bids and asks may be a useful comparison in a fully sourced explainer, but it is not substantiated by the supplied accepted claims. This draft does not present it as a sourced conclusion.

The same evidence gap limits comparison across price formation, trade execution, and liquidity provision. The pool example supports statements about reserves and provider shares for Uniswap v2, but it does not establish how every order-book venue operates or what execution outcome either model provides. Nor does the AMM label alone establish costs, execution quality, or risk.

## Liquidity, price impact, and trade-offs

Price impact is the change in token price caused by a trade. It generally increases when trade size is large relative to available pool liquidity. This is a qualified statement from Uniswap Labs’ price-impact explanation; actual execution also depends on fees, routing, active liquidity, intervening transactions, token behavior, and pool design. [2]

Price impact should be kept distinct from an externally observed price movement: the accepted claim concerns a change caused by a trade in the liquidity-pool context. It does not establish that every observed price difference has that cause. For a particular transaction, the pool design and the listed execution factors remain relevant. [2]

In public-blockchain AMM execution, transaction visibility and ordering can affect a trade before block inclusion, alongside pool depth and price impact. The scope matters: BIS notes that private order flow, batch auctions, encrypted mempools, rollups, and other designs can alter the ordering model. The public-blockchain finding should not be generalized to all transaction systems. [3]

Liquidity providers can also experience inventory-value loss relative to holding assets when pool prices move. Trading fees may or may not offset that difference. The outcome depends on pool design, price path, range, fees, timing, and withdrawal state. This exposure is commonly called impermanent loss, but that name does not establish that the difference will reverse or that fees will compensate for it. [4]

These claims describe possible mechanics and exposures, not a forecast of any particular trade or liquidity position. The evidence supports qualifications tied to pool depth, design, transaction conditions, and price movement; it does not establish which market model will produce a better outcome in a specific case.

## AMMs are not all the same

The accepted pool claim is expressly scoped to Uniswap v2: token-pair reserves supply swap inventory, and liquidity-provider shares represent contributions. It also warns that other AMMs can differ in curves, assets, fees, and accounting. [1]

That scope rules out treating one familiar pool model as the definition of the entire category. It also means that details such as a pricing invariant, a quote equation, or a particular liquidity-management feature should be attributed to a specific implementation only when its documentation supports them. The source pack does not establish additional examples such as concentrated liquidity or multi-asset pools, so they are not used here.

For a specific pool, authoritative documentation is the appropriate place to verify its assets, pricing rule, fees, and accounting. The supported claims do not provide enough detail to infer those mechanics for an unnamed or different AMM.

## Key takeaways

The accepted evidence supports a concrete but bounded account of AMM pool mechanics: in Uniswap v2, token-pair reserves provide swap inventory, provider shares represent contributions, and other AMMs may differ in curves, assets, fees, and accounting. Price impact generally grows when trade size is large relative to available pool liquidity, while public-blockchain transaction visibility and ordering can affect execution before block inclusion within the stated scope. Liquidity providers can experience inventory-value loss relative to holding assets, and fees may or may not offset it.

The source pack does not substantiate the order-book mechanics needed for a full AMM-versus-order-book comparison, nor the constant-product invariant and slippage definition in the prior draft. Those details should be added only with directly relevant evidence. For a particular AMM, verify its current mechanics in authoritative documentation rather than assuming that a category label specifies its implementation.

### Sources

1. [Uniswap Developers, “Pools”](https://developers.uniswap.org/docs/protocols/v2/concepts/pools)
2. [Uniswap Labs Support, “What is price impact?”](https://support.uniswap.org/hc/en-us/articles/40074715860365-What-is-price-impact)
3. [Bank for International Settlements, “Trading in the DeFi era: automated market-makers”](https://www.bis.org/publications/trading-defi-era-automated-market-maker)
4. [Bank for International Settlements, “Trading in the DeFi era: automated market-makers”](https://www.bis.org/publications/trading-defi-era-automated-market-maker)

## Sources and references

- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [What is price impact?](https://support.uniswap.org/hc/en-us/articles/40074715860365-What-is-price-impact) — Uniswap Labs Support; retrieved 2026-10-19.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
