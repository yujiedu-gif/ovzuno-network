---
title: "Crypto Liquidity Heatmaps: What They Show Across Trading Venues"
description: "Learn how a crypto liquidity heatmap visualizes order-book liquidity across venues, what its colors and axes represent, and why data and aggregation choices matter."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["crypto liquidity visualization", "order book depth heatmap", "liquidity across trading venues", "crypto market depth"]
author: "editorial_team"
primary_keyword: "crypto liquidity heatmap"
owned_question: "What is a crypto liquidity heatmap, and how does it represent liquidity across trading venues?"
risk_level: "medium"
---

# What Is a Crypto Liquidity Heatmap?

A **crypto liquidity heatmap** is a visualization that assigns colors to values in a defined dataset. A tool might arrange those values by price and time, but that is a possible design, not a universal convention. The term does not, by itself, specify what is measured, which venues are covered, how observations are collected, or what each color means. Those details must be stated by the tool’s documentation or interface.

Depending on its documented measure, a heatmap may depict resting order-book data, a concentration of displayed orders, or another liquidity-related metric. A multi-venue view may show venue data in separate panels or combine it according to a stated aggregation method. These designs answer different questions: separate panels retain distinctions among their inputs, while a combined view presents an aggregate that can make those distinctions less visible.

## What a crypto liquidity heatmap represents

A centralized crypto exchange commonly maintains off-chain records of outstanding buy and sell orders in a limit order book. A visualization using such records could map a defined measure of those orders to color. The exact measure might be displayed size, notional value, or another quantity, but the visualization must define it for the colors to be interpreted.

Displayed orders and completed trades are distinct kinds of information. An outstanding order in a book is not, merely by being displayed, a record of a completed trade. A heatmap based on order-book data therefore represents something different from a chart based on executed transactions. The chart’s label alone cannot establish which type of data it uses; the measure and its source need to be identified.

Nor does a displayed-order measure capture every dimension of market liquidity. A general market-liquidity framework includes the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. Liquidity is multidimensional and changes with transaction size and market conditions. A visualization of one order-book measure should therefore be read as that measure, not as a complete account of the cost or ease of a transaction.

## How liquidity may be mapped across venues

One hypothetical design could place price levels along one axis and timestamps along another, then use color to represent a selected order-book value. This example explains one way to encode data; it should not be taken as evidence that all, or even most, heatmaps use those axes. A tool could choose another layout, and its legend and methodology determine how its colors and dimensions should be read.

For example, a hypothetical chart might assign more intense colors to larger displayed quantities at a price level in a recorded observation. That interpretation is valid only if the chart’s legend defines the scale that way. Another design might encode notional value or a normalized metric. Raw size, notional value, and normalized values are not automatically interchangeable, so the unit and any transformation need to be documented.

A venue-aware representation may involve several dimensions:

- **Market or trading pair:** The market whose data is represented. The relevant market definition should be clear before comparing records.
- **Venue:** The exchange or other venue associated with an observation. The chart should make clear which venues are included.
- **Price level and order side:** If the data distinguishes them, the price and whether the displayed order is a buy or sell order.
- **Time:** The timestamp attached to a record and, where applicable, the interval or frequency used to collect observations.
- **Measure and units:** For example, a stated order-size measure, notional value, or another defined metric, including any normalization.

A multi-venue display could keep each venue’s observations separate or combine them. If it combines them, the aggregation method affects what the aggregate represents. A combined value may make a cross-venue summary visible while making individual venue contributions harder to inspect. A side-by-side display can preserve venue distinctions, but comparison still depends on using sufficiently clear and comparable definitions, units, and scales.

These are implementation choices, not a single prescribed workflow. To interpret a chart, readers need to know the selected venues and markets, the data measure, the time associated with observations, and how values are mapped to the display. Documentation of units, color scale, sampling or refresh behavior, and aggregation is particularly useful where the chart invites comparisons across venues.

## What a heatmap can help readers observe

When the measure and encoding are defined, a heatmap can make the distribution of recorded values easier to inspect. A reader might observe that the chart assigns different colors to values at different prices or times, or that separate venue panels display different recorded values. These are observations about the data represented and the chart’s chosen scale.

A venue-separated view can make differences among included venues more apparent than a single combined view. Conversely, an aggregate can summarize inputs but may conceal how much each venue contributed or how the inputs differed. Neither design is inherently a complete account of activity across all venues; the venue coverage and aggregation method define the scope of the view.

The visualization also has a time boundary: it represents the observations that were captured and displayed. Without documentation of how data is obtained and timed, the chart cannot establish what happened between observations or whether the displayed values describe comparable moments. A visible pattern is therefore a description of the represented records, not proof that the same pattern persists outside the captured data.

## Limits and comparability across venues

A heatmap alone does not establish executable liquidity or the terms at which a transaction could be completed. If the visualization represents displayed orders, its values describe that defined data measure; they should not be treated as a guarantee that a particular amount remains available. Broader market liquidity also includes factors such as spread, transaction cost, price impact, and immediacy, which a single displayed-order measure does not necessarily represent.

Cross-venue comparisons require attention to how the data and display were constructed. Relevant questions include:

- **Coverage:** Which venues, markets, and order-book levels are included? Data from selected venues should not be mistaken for a complete view of all venues.
- **Market mapping:** Do the compared records refer to the same defined market or pair? Similar labels alone do not establish equivalence.
- **Timing:** What timestamps are attached to observations, and what sampling or refresh behavior is documented? Different observation times can limit direct comparison.
- **Data gaps:** How does the display handle missing or delayed observations? If the method is not explained, apparent differences may be difficult to interpret.
- **Units and transformations:** Is the chart showing raw size, notional value, or a normalized metric? What conversions or normalization are applied?
- **Scales and aggregation:** Do panels share a color scale? If data is combined, what aggregation method is used, and can venue-level contributions still be inspected?

Color is an encoding, not an explanation. Similar colors across panels do not necessarily indicate similar values if the scales or units differ. A concentrated region of color supports, at most, an observation about the measure encoded in the captured data and under the stated methodology. Color patterns alone do not establish manipulation, predict future price movement, or identify best execution.

## Questions to ask before interpreting a heatmap

A technical review can begin with these checks:

1. **Which venues and markets are represented?** Confirm the venue list, market or pair definitions, and the scope of the displayed order-book levels or other inputs.
2. **What does the visualization measure?** Determine whether it represents displayed orders, executed trades, or another metric. Check whether values are raw size, notional value, or a transformed measure.
3. **What do the axes, colors, and units mean?** Use the legend and methodology rather than assuming a particular axis arrangement or color convention.
4. **How are observations timed?** Find the timestamp, sampling or refresh behavior, and any stated treatment of missing or delayed data.
5. **Are venues separated or combined?** If combined, identify the aggregation method. If shown separately, check whether units and color scales are comparable.
6. **What conclusions remain outside the chart’s scope?** A visualization of a defined measure does not, on its own, establish that displayed liquidity will remain available, describe all dimensions of market liquidity, or support predictions about market outcomes.

A crypto liquidity heatmap is best understood as a visual encoding of specified data, not as a universal measurement of liquidity. Its interpretation depends on the measure, venue coverage, units, timing, aggregation, and color mapping documented for that particular display. Knowing those choices helps readers distinguish what the chart records from what it cannot establish.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
