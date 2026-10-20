---
title: "Crypto Market Makers: How They Support Exchange Liquidity"
description: "Learn how crypto market makers place and manage buy and sell quotes, influence spreads and order-book depth, and face inventory and execution risks."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["crypto market making", "digital asset exchange liquidity", "bid-ask spread", "order book depth", "market maker inventory risk", "automated market making"]
author: "editorial_team"
primary_keyword: "crypto market makers"
owned_question: "What do crypto market makers do, and how do they support liquidity on digital asset exchanges?"
risk_level: "medium"
---

# What Do Crypto Market Makers Do?

Crypto market makers are part of the infrastructure that can make trading interest available on an exchange. In a centralized-exchange setting, market making generally refers to maintaining buy and sell interest in a market. The available evidence here supports a narrower explanation of the surrounding mechanics than a complete account of how every market maker operates: centralized crypto exchanges commonly maintain off-chain records of outstanding buy and sell orders in a limit order book, though individual venues can use additional matching models and order types [claim_bis_cex_order_books].

A market maker’s role should not be confused with guaranteeing that a trade will occur or establishing an asset’s fair value. Visible orders describe trading interest recorded at a particular time. Whether a particular order can trade, and on what terms, depends on the orders available and the venue’s rules and conditions. Liquidity is therefore better understood through several dimensions than through the presence of a market maker alone.

## What a crypto market maker does

In an order-book market, buy and sell orders record participants’ willingness to trade. A buy order is commonly called a bid, and a sell order an ask. The best bid is the highest displayed buy price; the best ask is the lowest displayed sell price. The difference between those two prices is the quoted bid-ask spread. These are useful descriptions of an order book, but a spread is only one observable part of liquidity, not a complete measure of the cost or ease of trading.

Market making involves maintaining trading interest that may provide a potential counterpart for other participants. A buyer and seller may have different timing or intentions; available buy and sell interest can make a trade possible when their orders are compatible under the venue’s matching rules. This does not mean a market maker is necessarily on the other side of every trade, that every displayed quote will remain available, or that all venues use an identical order-book model. Centralized exchanges commonly use off-chain limit order books, but venue-specific matching models and order types can differ [claim_bis_cex_order_books].

Nor does a quote establish an asset’s fair value. It indicates trading interest at a stated price and quantity, subject to remaining available and being eligible to match. Market making contributes to the trading environment; it does not guarantee a buyer, seller, or execution at a particular price.

## How market makers support exchange liquidity

Liquidity is multidimensional. A general market-liquidity framework includes the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. These dimensions vary with transaction size and market conditions [claim_market_liquidity_dimensions]. In other words, a narrow quoted spread may be useful information, but it cannot by itself show how much an order can trade, how quickly, or with what effect on prices.

Order-book depth is a measure of displayed quantities at different price levels. It answers a different question from the spread: rather than showing the gap between the best displayed buy and sell prices, depth describes the amounts of trading interest shown at levels on each side of the book. Because it concerns displayed orders, depth is a snapshot of recorded interest, not a promise that the quantities will remain available when an order is submitted.

Price impact and execution-price variation should also be kept distinct. Price impact refers to the effect of a trade on market prices. Execution-price variation, sometimes discussed as slippage, compares an execution price with a chosen benchmark, such as a price observed before the trade. The two can be related, but they are not interchangeable: a benchmark comparison describes an execution outcome, while price impact concerns how trading affects prices. The broader liquidity framework treats price impact as one dimension among spread, transaction cost, and immediacy [claim_market_liquidity_dimensions].

Displayed depth can help describe the quantities visible at a moment, but the accepted evidence does not establish a universal rule for how a particular order will interact with multiple levels. A reader should not infer that nearby quotes guarantee a better execution or a particular price impact. The applicable venue rules, order characteristics, and changing market conditions matter. Liquidity can change with transaction size and market conditions, so a single observation is not a complete description [claim_market_liquidity_dimensions].

## How to interpret liquidity measures

Spread and depth are separate, limited indicators. Spread describes the gap between the best displayed bid and ask; depth describes displayed quantities at price levels. Neither alone captures all the time and expense of trading. A broader assessment can also consider transaction costs, price impact, and immediacy, with the understanding that these dimensions change with order size and market conditions [claim_market_liquidity_dimensions].

For a technical or operational review, define what is being assessed before interpreting a liquidity figure:

- **Trading pair:** Which two assets and which market does the observation describe?
- **Order size:** What quantity is relevant? Liquidity for one size need not characterize another.
- **Time period:** Is the figure a snapshot or an observation across changing conditions?
- **Measure:** Does it report spread, displayed depth, or a broader estimate that includes other dimensions of trading?
- **Execution assumptions:** Does the measure describe displayed interest, or does it report actual outcomes under specified conditions?

These questions help distinguish a visible order-book snapshot from a broader assessment. Comparing relevant pairs, sizes, and time periods can make an assessment more informative, but no measure guarantees that a future order will execute at a particular price or at all.

## Limits of what the evidence establishes

A useful account of market making should distinguish established order-book facts from operational details that vary by operator and venue. The available accepted claims establish that centralized crypto exchanges commonly maintain off-chain records of outstanding buy and sell orders in limit order books, with additional matching models and order types possible [claim_bis_cex_order_books]. They also establish that liquidity is multidimensional and changes with transaction size and market conditions [claim_market_liquidity_dimensions].

Those claims do not establish a universal workflow for quote placement, monitoring, or updates; a general account of how centralized-exchange operators manage inventory; or specific risks such as adverse selection for order-book market makers. AMM liquidity research in the source pack discusses inventory and adverse-selection risk for AMM liquidity providers, but that scope does not establish the same mechanisms for centralized-exchange market makers [claim_bis_amm_liquidity]. It would therefore be inappropriate to treat those AMM findings as evidence about every market-making operation on a centralized venue.

Likewise, the accepted claims do not support a universal assertion that market makers withdraw quotes during volatility, outages, or other disruptions. Visible depth can change as the orders recorded in a book change, and liquidity varies with market conditions, but the specific causes and operational responses cannot be inferred from those facts alone [claim_bis_cex_order_books] [claim_market_liquidity_dimensions].

## Order-book market making and automated market makers

Order-book market making and automated market maker (AMM) liquidity provision are different infrastructure models. In the centralized-exchange context, outstanding buy and sell orders are commonly recorded in an off-chain limit order book [claim_bis_cex_order_books]. In one specific pool-based example, Uniswap v2 pools use deposited reserves of a token pair as the inventory from which swaps execute; liquidity-provider shares represent contributions. Other AMMs can use different curves, assets, fees, and accounting [claim_amm_pool_reserves].

The comparison should remain scoped: Uniswap v2 illustrates one pool-based AMM mechanism, not a definition of every AMM. The source pack also describes AMM liquidity providers as contributing assets to pools and potentially receiving a share of trading fees while bearing inventory and adverse-selection risk, with pool formulas, fee tiers, price ranges, and loss allocation varying by protocol and position [claim_bis_amm_liquidity]. Those AMM-specific statements should not be transferred to centralized-exchange market makers without separate evidence.

The practical takeaway is that “liquidity” is not a guarantee supplied by a label. Order books, displayed orders, spreads, and depth offer ways to describe trading interest, while the full time and expense of buying or selling can depend on size and market conditions. Market makers can contribute trading interest to exchange infrastructure, but the available measures and claims do not promise continuous depth, a specific execution, or a particular price outcome.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Pools](https://developers.uniswap.org/docs/protocols/v2/concepts/pools) — Uniswap Developers; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
