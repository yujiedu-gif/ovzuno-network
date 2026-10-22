---
title: "Crypto Order Book Analysis: Reading Depth, Spread, and Data Limits"
description: "Learn how crypto order book analysis interprets displayed depth, bid-ask spread, and order-book changes, and where visible-liquidity measures can mislead."
date: "2026-10-22"
draft: false
content_type: "analysis"
topics: ["exchange_market_infrastructure"]
tags: ["bid-ask spread", "order book depth", "market depth", "slippage"]
author: "editorial_team"
primary_keyword: "crypto order book analysis"
owned_question: "What can crypto order book analysis reveal about displayed liquidity, trading costs, and the limitations of visible order-book data?"
risk_level: "medium"
---

Crypto order book analysis can describe the prices and quantities displayed on one venue at a particular time, then track how those observations change. It can help characterize quoted spread and displayed depth, but it cannot establish that displayed orders will remain available or determine the cost of a future execution. Treat the measurements as venue-specific observations, not a complete account of liquidity or a price forecast.

## What crypto order book analysis measures

An order book is a record of outstanding buy and sell orders, commonly organized as a limit order book on a centralized exchange. A snapshot captures the displayed orders at one observation time; a time series compares multiple observations. Neither label says, by itself, how representative the data is of trading activity elsewhere or how long a displayed quantity will persist. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

Analysis should separate directly observed information—such as displayed prices and quantities—from interpretations. For example, a book can show a quantity offered at a listed price. Calling that quantity “available liquidity” is a stronger claim: the order may change before execution, and one venue’s book is not the whole market. A useful report states what was visible, where and when it was observed, and what remains unknown.

A single snapshot answers a narrow question: what did the recorded book show at that moment? A time series can add descriptive context, such as whether displayed quantities were still present at later sample times. It does not show what happened between samples, and it does not reveal why an order appeared or disappeared. Public transaction visibility, execution ordering, pool depth, and price impact can affect AMM swaps before block inclusion; that is a distinct execution setting from interpreting a centralized exchange’s order-book snapshot. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

## Read the bid-ask spread and order book depth

The **best bid** is the highest displayed buy price, and the **best ask** is the lowest displayed sell price. The **bid-ask spread** is the difference between those two prices. State the units: the absolute spread is expressed in the quote currency per unit of the base asset. A relative spread can be calculated as the absolute spread divided by a stated reference price, such as the midpoint between best bid and best ask. That calculation is a chosen reporting convention, not a claim that every venue reports spread in the same way.

For instance, if a hypothetical book shows a best bid of 99 and a best ask of 101 quote-currency units per base-asset unit, the absolute spread is 2 units. The midpoint is 100, so the relative spread under the stated convention is 2%. This example illustrates arithmetic only; it does not describe a market observation or a universal threshold for interpreting spread.

**Order book depth** describes the displayed quantities available at prices on one or both sides of the book. To make a depth measure interpretable, specify the side, price interval, quantity units, and whether quantities are accumulated. One possible convention is cumulative bid depth within a stated percentage below the best bid, and cumulative ask depth within the same percentage above the best ask. Another is to report quantities at explicit price levels. These are analytical choices; comparisons are meaningful only when the pair, venue, timestamp, units, and measurement method are compatible.

Depth is not a single, venue-independent measure of market liquidity. Liquidity can reflect the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. Displayed depth addresses only part of that broader picture. [source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>)

## Use imbalance and persistence cautiously

An **order-book imbalance** summarizes a difference between displayed quantities on the bid and ask sides. Its meaning depends on the selected price range, weighting, and normalization. For example, an analyst might total bid and ask quantities within a specified distance of their respective best prices, then calculate the difference divided by the sum. The result is a descriptive statistic tied to those choices—not a universal signal.

A report should identify whether quantities are counted equally across price levels or weighted by distance, and whether size is measured in base units, quote-currency value, or another stated unit. Changing those choices can change the reported imbalance, so two values should not be compared as though they used the same definition unless their methods match.

Persistence adds a time dimension. An analyst can compare the same price levels or defined price bands across repeated observations and record whether displayed quantities remain, grow, shrink, appear, or disappear. The sampling interval matters: sparse observations can miss changes between samples. The resulting pattern describes the collected data; it does not establish the reason for a change or the intentions of the order submitter.

Do not infer future price direction, intent, or executable size from imbalance alone. Nor does displayed depth alone establish realized execution cost or slippage. A venue’s internal order book records orders and executed trades within that venue’s account system; those records do not, by themselves, represent activity across other venues. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

## What visible liquidity cannot establish

Displayed orders can be revised or removed before execution. A snapshot therefore cannot guarantee that a shown quantity will still be present when a later order reaches the venue. A time series can document persistence at its observation points, but it cannot prove continuous availability between them.

A venue-specific book also has a boundary: it does not include every other venue, and visible records may not reflect hidden, internalized, or other off-book activity. Consequently, a displayed-depth total should not be presented as the total liquidity for an asset across the market.

Finally, observed depth does not determine a trader’s realized execution cost. Market liquidity includes price impact and immediacy as well as quoted spread and transaction cost; order-book measurements do not independently settle what a particular execution would cost. Keep “displayed depth,” “estimated cost,” and “realized outcome” separate in analysis. [source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>)

## A reproducible order-book reading workflow

1. **Identify the observation.** Record the venue, trading pair, timestamp, data source, and quantity units. State whether the data is a snapshot or a sequence of samples. Centralized venues commonly maintain off-chain records of outstanding buy and sell orders, so describe the source as a venue-specific record rather than a universal market ledger. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)
2. **Define the measurements before comparing.** State how spread is expressed, which price is used for any relative calculation, and the price distances or thresholds used for depth. Identify the side, aggregation method, weighting, and denomination for each quantity measure.
3. **Describe change without attributing cause.** For time-series analysis, document the sampling interval and whether quantities persisted across the recorded observations. Avoid claims about unobserved intervals, order intent, or future prices.
4. **Label the conclusion and its limits.** Say whether a finding concerns displayed spread, displayed depth, or a defined imbalance. Note missing venues, unsampled periods, and any measurement choices that could affect interpretation. Do not present a visible-liquidity statistic as a guarantee of executable size, realized slippage, or total market liquidity.

This framework makes order-book analysis more comparable and auditable by keeping definitions, units, and observation boundaries explicit. Its output remains a description of available data—not a prediction or a complete measure of trading conditions.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
