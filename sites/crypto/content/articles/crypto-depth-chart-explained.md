---
title: "Crypto depth chart explained: reading bids, asks, and liquidity"
description: "Crypto depth chart explained: learn how order-book bids and asks appear on a chart, what visible liquidity can indicate, and where interpretation has limits."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["crypto depth chart"]
author: "editorial_team"
primary_keyword: "crypto depth chart explained"
owned_question: "What does a crypto depth chart show, how is it constructed from an order book, and what can readers infer—and not infer—from it?"
risk_level: "medium"
---

A crypto depth chart is a visual summary of buy and sell orders listed in a selected market’s order book. It plots displayed quantities across price levels, often cumulatively, so readers can see the distribution of visible bids and asks. It does not show every source of liquidity, guarantee an execution, or predict what prices will do next.

## What a crypto depth chart represents

An **order book** is a venue’s record of outstanding buy and sell orders. A centralized crypto exchange commonly maintains off-chain records of those orders in a limit order book. A depth chart presents selected information from that book in a graphic form. It is not the same as the book’s underlying list of orders, and it is not a price chart. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

A price chart organizes price information over time. A depth chart instead organizes displayed order quantity by price. That difference matters: the depth chart describes orders listed in the selected book, while a price chart describes price history according to its own time intervals and data source.

The scope of a depth chart depends on what it reads. A chart tied to one venue’s order book does not automatically include orders listed elsewhere or other forms of market liquidity. The selected market, data source, and chart settings determine what its display represents. A chart may also summarize the book rather than expose each order as a separate plotted item.

## How bids, asks, and cumulative depth appear

A **bid** is a buy order: it states a price at which a participant is willing to buy under the order’s terms. An **ask** is a sell order: it states a price at which a participant is willing to sell. The chart typically separates the two sides around the gap between the highest displayed bid and lowest displayed ask.

Price is commonly shown along the horizontal axis and order quantity along the vertical axis. However, chart conventions are not universal. Check the labels and units rather than inferring them from color, orientation, or shape. A display might show quantities at individual price levels, cumulative quantities, or a particular aggregation of the book.

In a cumulative display, the quantity at successive price levels is added together. The plotted value therefore grows as the chart includes more orders farther from the central gap. On the bid side, accumulation generally includes buy orders across a range of prices; on the ask side, it includes sell orders across a range. The direction and threshold used for accumulation depend on the interface, so read the axis and any chart legend before interpreting a curve.

Aggregation can turn a list of discrete orders into steps or a smoothed-looking line. A tall step or sharp rise can indicate that the displayed quantity changes substantially across a particular price level or group of levels. A gradual slope can reflect quantities spread across multiple levels. Neither shape is a separate market event: it is a way of plotting the orders included in the selected book.

For example, if a chart groups orders into price bands, several orders at nearby prices might appear together as one larger change. That is an illustration of how aggregation can affect appearance, not a universal chart rule. The same book can look different when the price interval or cumulative setting changes.

## Reading the spread and visible liquidity

The **best bid** is the highest bid shown in the selected book, and the **best ask** is the lowest ask shown. The difference between those prices is the **spread**. A depth chart can make the gap between the two sides easy to locate, but confirm the actual bid and ask values in the labels or underlying order-book view. A graphic’s spacing alone may not establish the numeric spread.

Order concentration near the spread shows how much quantity the chart represents at nearby prices. More displayed quantity at a given price level means that the selected book lists more quantity there at the time reflected by the data. It does not mean that quantity will remain available, that a particular order will be filled, or that execution will occur at a displayed price.

A depth chart also cannot be treated as a complete measure of market liquidity. Market liquidity involves more than the visible quantity at one price: time and expense of buying or selling can include spread, transaction cost, price impact, and immediacy. The chart’s visible book may help describe one part of that picture, but it does not by itself establish the costs or outcome for a particular transaction. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

That evidence about automated market-maker swaps concerns a different market structure: public transaction visibility, execution ordering, pool depth, and price impact can affect an AMM swap before block inclusion. It should not be confused with a centralized exchange’s internal order book. The distinction is useful because a chart’s interpretation depends on the mechanism and data it actually depicts, not merely on its title.

Scale also affects visual impressions. Changing the displayed price range, quantity units, or aggregation level can make the same concentration look more or less prominent. For a meaningful comparison, check that the market, source, time, units, visible range, and aggregation settings match. Do not infer that two charts are directly comparable just because both are labeled as depth charts.

## What a crypto depth chart cannot tell you

A depth chart is time-sensitive. It displays order-book information available to the chart at a particular moment, and the listed orders may change or be canceled. The graphic is not a promise that every shown order will still be present when another participant submits an order. Because a centralized exchange’s limit order book is its own off-chain record, it is also not a universal register of all orders across venues. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

Displayed orders are not the same as executed trades. An outstanding order is listed in the book; an executed trade records a transaction that took place. A chart of outstanding orders should not be read as a history of completed transactions, unless the interface separately provides trade data and clearly identifies it.

Nor does a single book show all liquidity that might be relevant to a market. It may exclude activity on other venues or liquidity represented through different trading mechanisms. A depth chart alone cannot tell readers why an order is present, whether it will remain, or how the book will change. It also cannot establish future price direction, execution quality, or future liquidity.

These limits are not fixed by a chart’s visual polish. A clear graphic can still be a limited view of one selected book at one point in time. Conversely, a visible concentration should not be treated as an assurance that orders can be executed against it under all conditions. The chart is informative about its displayed data, not a guarantee about outcomes.

## A practical checklist for interpreting one chart

Before interpreting a specific display, verify the following:

- **Market and source:** Identify the asset pair and the venue or data source supplying the book. Confirm whether it represents one venue or a broader combined view.
- **Timestamp or refresh status:** Check when the displayed information was captured or last refreshed. A snapshot can become outdated as orders change.
- **Price range:** Read the horizontal scale and note what lies outside the visible interval. A cropped chart does not show levels beyond its selected range.
- **Quantity units:** Determine what the vertical axis measures. Do not assume the unit or denomination based only on the chart’s appearance.
- **Aggregation:** Check whether each plotted point represents an individual level, a grouped price band, or cumulative quantity. Confirm which direction the cumulative calculation uses.
- **Bid, ask, and spread:** Use the labels or underlying order-book view to confirm the best displayed bid, best displayed ask, and gap between them.
- **Data limits:** Establish whether the chart covers only displayed orders in a selected book. Do not treat missing orders or other market mechanisms as evidence that no other liquidity exists.

This checklist is about reading the display, not choosing a transaction or predicting a market. The chart can help explain how visible bids and asks are distributed across prices. Its meaning remains bounded by the source, selected market, time, scale, and calculation method. A careful reader uses those details to describe what the chart shows—and keeps separate what it cannot establish.

## Sources and references

- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
