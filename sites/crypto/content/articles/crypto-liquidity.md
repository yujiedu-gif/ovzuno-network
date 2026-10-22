---
title: "Crypto liquidity: how trading venues support execution"
description: "Learn how crypto liquidity forms across trading venues, which measures help assess executable depth, and why infrastructure affects execution quality."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "crypto liquidity"
owned_question: "How is crypto liquidity produced and assessed across trading venues, and which market-infrastructure factors affect whether an order can be executed with limited price impact?"
risk_level: "medium"
---

Crypto liquidity describes how readily market interest can support a trade, but it is not a single market-wide constant. It varies by asset, venue, trading pair, buy or sell side, and time. To assess whether an order may execute with limited price impact, compare the relevant market’s spread, available depth, and execution conditions rather than treating reported volume or a broad liquidity label as a guarantee.

## What crypto liquidity describes at market level

For an operator or researcher, the useful question is not simply whether an asset is listed or trading. It is how much opposing market interest is available, at what prices, and with what immediacy. Market liquidity includes the time and expense involved in buying or selling; relevant dimensions include spread, transaction cost, price impact, and immediacy. These dimensions describe related but distinct aspects of execution. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

A market’s reported turnover, or the fact that a trading pair exists, does not by itself show how much can be executed near a particular price. Nor does a label such as “liquid” establish the conditions for a specific order. Liquidity should be understood in context: a pair can have different visible conditions on different venues, and buying and selling conditions need not match.

This distinction matters when interpreting an aggregate market view. Combining or summarizing activity can conceal differences between venues and trading pairs. A figure that describes a broad market is not automatically evidence that a particular venue has executable interest for a particular order size.

## Where liquidity comes from across crypto venues

Trading venues organize buy and sell interest under their own operating models. In a centralized exchange model, a venue commonly maintains an off-chain record of outstanding buy and sell orders in a limit order book. That internal record supports the venue’s matching process, but it is a venue-level view: it does not, on its own, describe orders held elsewhere. ([source](<https://www.bis.org/publications/aer-2022/future-monetary-system>))

A centralized exchange can also provide near-real-time trading, liquid order books, and advanced order functionality after assets are deposited. These are characteristics of the general centralized-exchange model, not a guarantee about any specific venue, asset pair, or market condition. ([source](<https://www.bis.org/publ/work1227.pdf>))

Liquidity may be considered at several scopes: one venue’s visible orders, activity across several venues, or a routed or aggregated view assembled by another system. Those scopes should not be treated as interchangeable. A venue-local snapshot describes what that venue exposes at the observation time; an aggregated view depends on which sources it includes and how it combines them. The evidence available for a given view should therefore be stated, rather than assuming that liquidity is uniformly shared across the market.

The exchange itself is only one part of the infrastructure. The relevant distinction is between where interest is recorded, where an order can be matched, and whether a system can access or combine interest across venues. Those arrangements vary. A market-level summary may show broad activity without establishing that a particular execution path can reach every source represented in that summary.

## How to assess depth, spread, and price impact

A practical assessment starts by defining the measurement. **Spread** refers to the difference between available buy and sell prices at a given observation. **Displayed depth** describes visible order interest at specified prices or within a specified range. Both are snapshots: the figures need a venue, pair, side, and observation time to be interpretable.

**Price impact** concerns how the execution price changes with trade size and available opposing interest. It connects a market’s visible conditions to the size of the order being considered. A price-impact estimate is meaningful only alongside its assumptions: the source of the data, the order size, the side, and the prices included in the calculation.

These measures capture different dimensions of liquidity. A narrow spread does not establish that substantial depth is available; a depth figure does not by itself describe the cost or immediacy of completing an order. Market liquidity encompasses spread, transaction cost, price impact, and immediacy, so a single measure cannot stand in for all of them. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

Displayed conditions also are not the same as realized execution. An order may encounter conditions different from a prior snapshot as market interest and execution circumstances change. Treat a displayed spread or depth figure as evidence about a stated moment and scope—not as a promise about a later fill.

For a useful comparison, hold the principal dimensions constant: asset, trading pair, venue or venue set, buy or sell side, order size, and observation time. If one comparison uses a single venue and another aggregates several, the results answer different questions. Likewise, comparing different order sizes or observation windows can produce figures that are not directly comparable.

## Why execution conditions change

Liquidity is conditional and time-sensitive. Trading activity, available market interest, and execution conditions can change between observations, so a depth or spread snapshot should not be treated as permanent. Comparing measurements at different times without recording the time window can obscure whether a difference reflects the market, the measurement method, or both.

Venue participation and connectivity also shape what a system can observe and use. A centralized exchange’s internal order book is a venue-specific record, while a wider market view may depend on separate data sources or routing arrangements. The existence of a broader view does not show that every order can access all of the interest it summarizes.

Concentration is another reason not to infer uniformity from a market-wide description. Crypto and decentralized-finance systems can exhibit substantial de facto centralization even when their stated architecture or ethos emphasizes decentralization. The degree and location of concentration must be assessed for a specific network, asset, application, and time window; the observation is not a universal conclusion about every market or venue. ([source](<https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks>))

Latency, routing choices, trading rules, and service interruptions may affect access to observed interest, but their effects depend on the system and conditions at the time. A liquidity measure that does not describe its execution path cannot resolve those operational questions. It is therefore useful to separate the data question—what interest was observed?—from the execution question—what interest could this system reach and match?

## Questions to ask when evaluating a liquidity view

Before relying on a reported figure, establish what it measures and what it leaves out:

- Does the view cover one venue or multiple venues? If it aggregates sources, does it state which sources and how they are combined?
- Does the figure represent displayed orders, executed trades, or another data source? What observation window does it cover, and does the method explain how stale data is handled?
- Which asset, pair, venue, market segment, and buy or sell side does it describe?
- What trade size and price range underpin any depth or price-impact estimate?
- Is the measure a snapshot, or does it summarize activity over a period? Those descriptions are not interchangeable.

The answers determine what conclusion the data can support. Displayed depth can describe visible interest at a stated scope and time; executed-trade data describes activity that occurred under its own measurement method. Neither alone assures that a new order will execute at a particular price or through a particular route.

For builders and decision-makers, the central discipline is to match the liquidity claim to the execution question. State the venue coverage, pair, side, size, source, and observation time; then distinguish observed conditions from accessible and realized execution. That approach makes liquidity assessments more informative without turning a market snapshot into a guarantee.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Crypto Ecosystem: Key Elements and Risks](https://www.bis.org/publications/crypto-ecosystem-key-elements-and-risks) — Bank for International Settlements; retrieved 2026-10-18.
