---
title: "Liquid crypto exchange: how to assess market depth"
description: "Learn what a liquid crypto exchange means, which market-quality indicators help assess depth and execution, and why volume alone may be misleading."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "liquid crypto exchange"
owned_question: "What does it mean for a crypto exchange to be liquid, how can that condition be assessed, and what market-structure factors can affect it?"
risk_level: "medium"
---

A liquid crypto exchange is one where participants can buy or sell a particular trading pair with relatively little delay, spread, transaction cost, or price impact for the order size they need. Assess it by pairing measures of current quotes and depth with completed-trade volume, while treating every reading as specific to a venue, pair, size, and time—not as a guarantee of execution.

## What makes a crypto exchange liquid?

Liquidity describes how readily a trade can be completed and at what cost. Relevant dimensions include the time needed to trade, the gap between buying and selling prices, transaction costs, price impact, and immediacy. These dimensions can move in different directions: a market may show frequent trading but still impose substantial price impact on a larger order, or show close quotes that are available only in small quantities. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

“Exchange liquidity” is therefore a shorthand, not a single venue-wide quantity. It is more useful to ask about liquidity in a named asset pair, for a stated order size, under the conditions observed at a particular time. A venue may have a liquid market in one pair and a much thinner one in another. A change in order size can also change the execution price and the time needed to complete a trade. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

A centralized exchange may offer trading through an internal limit order book: an off-chain record of outstanding buy and sell orders. Some venues can provide near-real-time trading after assets are deposited, but performance and liquidity vary by venue, pair, and market conditions. That operating model does not establish how much executable depth any particular pair has at a given moment. ([source](<https://www.bis.org/publications/aer-2022/future-monetary-system>); [source](<https://www.bis.org/publ/work1227.pdf>))

## How to assess exchange liquidity

Start with the pair and the order you care about. Record the observation time, the best displayed buy and sell quotes, and the quantities offered at those prices. The **bid-ask spread** is the difference between the best displayed sell quote and the best displayed buy quote; it is a measure of the gap between those top quotes, not the full cost of every possible trade. A narrow spread alone does not show that substantial quantities are available near those prices. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

Next, inspect **quoted depth**: the quantity shown for buying or selling at specified price levels. State the price interval used, such as a defined distance from the best quote, rather than presenting “depth” as a context-free number. Compare the available quantities on both sides of the market and note whether the reported figure covers only the top quotes or several price levels. An order book is a record of outstanding orders, but a snapshot does not establish that every displayed order will remain available until an order reaches it. ([source](<https://www.bis.org/publications/aer-2022/future-monetary-system>); [source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

Then estimate execution cost for a defined order size. The **quoted execution price** is the price suggested by available quotes for that order; the **realized execution price** is what a completed trade actually receives. Comparing the estimated price with a relevant reference quote can help show price impact, while the spread and other transaction costs remain separate parts of the assessment. Because liquidity reflects price impact, cost, and immediacy, the same venue should be evaluated at more than one order size if those sizes matter to the intended use. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

Use completed-trade volume as a supporting indicator, not a substitute for depth. Volume records trading activity over a chosen period; it does not by itself state what quantity is currently available at nearby prices or what execution cost a new order would face. For a useful comparison, keep the venue, pair, measurement period, order sizes, price intervals, and data method consistent. If those definitions differ, the resulting figures may not describe comparable conditions. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

## Why reported volume may not show executable depth

Trading volume and resting orders answer different questions. Volume indicates that trades occurred during a period. An order book, by contrast, records outstanding buy and sell orders at the time it is observed. A high historical volume figure cannot alone establish that an order of a particular size can be executed now with limited price impact; that requires observations tied to current quotes and the intended order size. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>); [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>))

A depth snapshot is also time-bound. Market conditions can change, and a snapshot records outstanding orders rather than a promise that they will remain available. Treat a chart, reported metric, or vendor summary as evidence only to the extent that its source, time window, pair coverage, price bands, and calculation method are disclosed. Without those details, readers cannot reliably tell whether two reported measures use the same basis. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>); [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>))

This distinction matters when reviewing third-party liquidity scores or dashboards. A score may summarize useful observations, but the label alone does not reveal whether it measures spreads, displayed depth, completed trades, or some combination. Require the underlying definitions and observation periods before drawing conclusions. The evidence used here supports a measurement framework, not a judgment about any named exchange or reported metric. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

## Infrastructure factors behind liquidity

A centralized exchange’s internal order book is one part of the observable market structure: it records outstanding orders, while the trading venue provides the internal trading system. Observed liquidity therefore depends on what orders are present for the pair and the conditions under which trades take place. The existence of an order book, or a venue’s ability to support near-real-time trading, does not establish the depth or execution quality available for a specific order. ([source](<https://www.bis.org/publications/aer-2022/future-monetary-system>); [source](<https://www.bis.org/publ/work1227.pdf>))

For assessment, keep three questions separate: what is displayed, what can be accessed in time, and what trades actually execute. A market-data observation informs the first question; venue performance and market conditions are relevant to the second; completed trades inform the third. The measures should be aligned by pair, order size, and time window before they are compared. These are distinctions among evidence types, not a claim that any one infrastructure component causes a particular liquidity result. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>); [source](<https://www.bis.org/publ/work1227.pdf>))

## Limits, risks, and due diligence

Liquidity indicators describe observed market conditions, not guaranteed capacity. Spread, depth, execution cost, and immediacy can vary with the pair, trade size, and conditions, so a reading at one time should not be treated as a standing promise about future execution. Evaluate indicators against the specific operational question and record their scope. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

A practical review can document the venue and pair, timestamp, spread definition, depth price bands, displayed quantities, order sizes used for execution estimates, volume period, and data source. It can also distinguish displayed orders from completed trades rather than combining them into a single unexplained score. This makes the basis of the assessment clearer without turning a momentary observation into a universal rating. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>); [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>))

Liquidity analysis does not establish an exchange’s security, custody or recovery arrangements, regulatory status, geographic availability, fees, tax treatment, or suitability. Those are separate questions requiring evidence specific to the provider, product, jurisdiction, and time. The indicators described here support a bounded assessment of observable market quality; they do not rank venues or recommend one. ([source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>))

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
