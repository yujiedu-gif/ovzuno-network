---
title: "Crypto spread explained: bid-ask gap and calculation"
description: "Crypto spread explained: learn how the bid-ask gap is calculated, what can make it widen or narrow, and how it differs from fees and slippage."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["crypto spread"]
author: "editorial_team"
primary_keyword: "crypto spread explained"
owned_question: "What is a crypto spread, how is it calculated from quoted prices, and what can cause it to widen or narrow?"
risk_level: "medium"
---

A crypto spread is the gap between the best quoted ask and bid for the same asset, market, quote unit, and observation time. Calculate the absolute spread by subtracting the bid from the ask; for a percentage, this guide divides the gap by the midpoint of those prices. The result describes quoted prices, not a guaranteed execution cost or a forecast of price direction.

## What a crypto spread measures

The **bid** is the quoted price at which a buyer is willing to buy. The **ask** is the quoted price at which a seller is offering to sell. The bid-ask spread is the difference between those quotes, provided they refer to the same asset and market at the same time.

For example, a hypothetical bid of $99 and ask of $101 produce a $2 spread per unit. The gap is a property of the quotes, not necessarily the amount a particular buyer or seller will pay in a completed transaction. A displayed quote alone does not establish that a given quantity can be traded at that price.

A spread is also not a prediction. A single pair of quotes does not show whether the asset’s price will rise or fall, and the gap should not be interpreted as a signal about future prices. It is a snapshot of the difference between the quoted buying and selling prices under the stated conditions.

The phrase “best bid” or “best ask” refers here to the most favorable displayed price on the relevant side of the market at the observation time. The quote must be read with its market and unit in view: a bid from one market and an ask from another do not form a valid same-market spread calculation unless the comparison is explicitly designed for that purpose.

## How to calculate the crypto spread

The absolute spread is the ask minus the bid:

**Absolute spread = ask price − bid price**

To express the result as a percentage, this article uses the midpoint of the bid and ask as the denominator:

**Midpoint = (ask price + bid price) ÷ 2**

**Percentage spread = (ask price − bid price) ÷ midpoint × 100**

The denominator convention matters. A percentage based on the midpoint is not automatically comparable to one calculated using only the bid, only the ask, or another reference. When reading a published percentage or comparing calculations, check which price is used as the denominator.

**Hypothetical example:** Suppose the quoted bid is $99 and the ask is $101, both in U.S. dollars for the same asset and at the same observation time.

1. Absolute spread: $101 − $99 = **$2 per unit**.
2. Midpoint: ($101 + $99) ÷ 2 = **$100**.
3. Percentage spread: ($101 − $99) ÷ $100 × 100 = **2%**.

These values are illustrative arithmetic, not live market data. If the two quotes use different currencies or refer to different assets, markets, or observation times, first establish a consistent basis before using the formula. Otherwise, the subtraction can produce a number that does not represent a meaningful spread.

The absolute and percentage measures answer slightly different questions. The absolute figure states the quoted price gap in the quote unit, such as dollars per unit. The percentage expresses that gap relative to the chosen reference price. Neither number, by itself, tells how much of an order can be completed at the displayed prices.

## Why spreads can widen or narrow

Liquidity is not just the presence of a bid and an ask. It can reflect the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. It is multidimensional and changes with transaction size and market conditions. [source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>)

Order depth is useful context for interpreting a quote. The displayed bid and ask describe prices at the top of the market, but a reader also needs to consider how much is available at those prices. If an order is larger than the amount available near the top quote, the price for the full quantity may differ from that displayed level. A spread calculation does not show the amount of available depth.

Volatility, trading activity, and differences between venues or market conditions may influence the bid and ask. These are possible influences, not reliable rules for predicting the next quote. A spread may change as market conditions change, but a displayed gap does not establish when or how it will move. Nor does it guarantee a particular execution price.

Market structure matters as well. In one example, an automated market-maker liquidity provider contributes assets to a pool and can receive a share of trading fees while bearing inventory and adverse-selection risk. Pool formulas, fee tiers, price ranges, and loss allocation vary by protocol and position. [source](<https://www.bis.org/publ/work1227.pdf>) This example illustrates that quotes and swap outcomes can arise from a pool mechanism rather than a conventional order book; it should not be treated as a universal account of crypto trading venues.

Because the percentage spread uses a reference price, the same absolute gap can correspond to different percentages at different price levels. This is a mathematical consequence of the denominator, not evidence that one quote is more executable or that a market is more liquid. Keeping both the absolute figure and percentage convention visible helps avoid reading a percentage in isolation.

## Spread, fees, and slippage are different

The **spread** is the gap between bid and ask quotes. A **fee** is a separate charge that may be imposed by a venue or service under its terms. **Slippage** is the difference between an expected or quoted price and the price ultimately realized when an order executes.

These terms describe different parts of a transaction. The spread calculation compares two quoted prices. It does not include any separate fee, and it does not prove what price a transaction will receive. Slippage concerns the difference between an expected price and a realized execution price, so it cannot be calculated from a bid and ask alone without execution information.

For this reason, a spread should not be presented as the complete cost of a transaction. A transaction’s cost may involve the quoted gap, applicable charges, and differences between expected and realized execution, depending on the specific transaction and service. The details of fees and execution depend on the relevant venue, product, and order conditions; do not infer them from the spread alone.

A quoted conversion estimate is another distinct item. For example, an onramp quote API can return estimated conversion outcomes for combinations of source amount, destination cryptocurrency, network, fees, and rate before the user enters the purchase flow. The estimate is time-sensitive, and final availability and execution can change before completion. [source](<https://docs.stripe.com/api/crypto/onramp_quotes>) Such an estimate is not the same thing as a bid-ask spread: it may incorporate multiple quoted inputs, while the spread formula specifically compares a bid and an ask.

## How to interpret a quoted spread

Use a consistent reading sequence when examining a quote:

1. **Match the inputs.** Confirm that bid and ask refer to the same asset, quote unit, market, and observation time.
2. **Identify the quote level.** Determine whether the figures are top-of-market quotes or prices for a specified order size. A top quote does not establish that the same price is available for every quantity.
3. **Calculate both measures.** Subtract bid from ask for the absolute spread, then divide by the midpoint for the percentage convention used here.
4. **Separate other costs.** Look for applicable fees and distinguish the quoted prices from any realized execution price.
5. **Keep the conclusion limited.** Treat the figure as a quote comparison, not as a guarantee of total cost, available depth, or favorable execution.

A narrow quoted spread does not, on its own, establish that a large order can be completed at the displayed prices or that total transaction costs are low. A wider spread likewise does not provide a reliable forecast of future prices. The quote’s market, timing, size, depth, and any separate charges all matter to interpretation.

The central rule is straightforward: calculate ask minus bid for the absolute gap, state the midpoint convention when expressing it as a percentage, and keep spread separate from fees and slippage. That gives a clear description of quoted prices while avoiding claims about execution that the quote alone cannot support.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Crypto Onramp Quotes](https://docs.stripe.com/api/crypto/onramp_quotes) — Stripe Documentation; retrieved 2026-10-19.
