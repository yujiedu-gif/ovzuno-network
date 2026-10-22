---
title: "Crypto Funding Rates: How Perpetual Futures Payments Work"
description: "Learn how crypto funding rates work in perpetual futures, why traders exchange periodic payments, and what a rate can—and cannot—tell you."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_cards_spending"]
tags: ["funding rates crypto"]
author: "editorial_team"
primary_keyword: "crypto funding rates"
owned_question: "How do crypto funding rates work in perpetual futures, and what do they indicate about positioning and trading costs?"
risk_level: "medium"
---

Crypto funding rates are periodic payments between holders of perpetual-futures positions. They are commonly used to help keep a perpetual contract’s price aligned with a reference market. The rate indicates which side pays under a contract’s rules, but it does not predict the next price move or establish whether a position is worthwhile.

## What crypto funding rates are—and what they are not

A perpetual future is a derivatives contract without a scheduled expiration. Because it does not settle at a fixed expiry, its price can diverge from the reference market it is designed to track. Funding is a recurring payment mechanism commonly used to encourage closer alignment. It does not guarantee that the contract price will match its reference price.

A funding **rate** is an input to a payment calculation, not the payment amount. The amount also depends on the position’s notional value—the value assigned to the position under the contract’s calculation method—and the venue’s rules. A percentage displayed without its associated notional and interval is not, by itself, a dollar charge or credit.

Funding is distinct from trading fees associated with executing a trade. It is also not automatically the same as interest or borrowing charges that may apply in other products. Whether a venue applies additional costs is a separate matter from the design of its funding mechanism.

## How funding payments move between long and short positions

A **long** position generally benefits if the contract price rises, while a **short** generally benefits if it falls. Under a common convention, a positive funding rate means longs pay shorts; a negative rate means shorts pay longs. This is a convention, not a universal rule: a contract’s documentation determines what its rate sign means and which positions pay.

Funding is typically exchanged between eligible position holders rather than treated as a conventional trading fee paid to an exchange. Settlement details remain specific to the contract. So does the schedule: eligibility depends on the position held at the relevant funding time, as defined by the venue. A displayed rate alone does not establish whether a position will be included in a payment event.

For an operator or analyst reviewing a contract, the practical distinction is between the displayed rate and the settlement event. Check the payment schedule, position-eligibility rule, and direction of payment in the contract documentation. Do not assume that timing or settlement rules from one contract apply to another.

## How a crypto funding rate becomes a payment

Conceptually, the payment depends on the applicable funding rate and the position’s notional value. For illustration only, suppose a hypothetical contract applies an assumed rate of 0.01% to an assumed notional of $10,000 for one funding interval. Multiplying those assumptions gives $1 before any contract-specific conventions. This is simple arithmetic, not a market quote or a claim that a particular venue uses that exact formula.

The actual calculation may depend on contract denomination, the price used to determine notional, the funding interval, caps, and other specified inputs. One venue’s displayed percentage may refer to a different period or calculation convention from another venue’s percentage. An estimated or projected rate should also not be mistaken for the final rate applied at settlement.

To understand an actual payment, identify the contract’s formula and the rate used, the position notional, the interval, and the settlement rules. Confirm whether a displayed figure is observed, estimated, or projected. Without those details, a headline percentage is not enough to calculate what a position holder will pay or receive.

## What positive, negative, and changing rates can indicate

Under the common convention, a positive rate means longs pay shorts; a negative rate means shorts pay longs. A positive reading can indicate greater demand for long exposure under the applicable contract mechanism, while a negative reading can indicate greater demand for short exposure. These interpretations describe a particular contract’s mechanism, not every trader’s view across the broader market.

Rates can change as market conditions and contract inputs change. A single reading is therefore a snapshot, not a durable description of positioning. A positive or negative sign does not establish which way an asset’s price will move next, whether the contract will converge with its reference, or whether a position will be profitable. Funding is a payment mechanism, not a stand-alone forecast.

Rate interpretation also needs context. A figure may be meaningful as a record of how the contract’s funding mechanism is operating at a particular time, but it is not a complete measure of market demand. It cannot, on its own, show whether a position is crowded, whether that condition will persist, or how the contract’s price will respond.

## Why funding rates differ across contracts and venues

Funding figures are not automatically comparable. Contract rules can differ in formulas, inputs, intervals, caps, and settlement conventions. Contract denomination, reference markets, and the time a rate is observed can also affect what a displayed number means. Two similar-looking percentages may therefore describe different time periods or methods.

Before interpreting a figure, identify:

- the venue and specific contract;
- the timestamp and funding interval;
- whether the figure is observed, estimated, or projected; and
- the contract’s payment direction, calculation inputs, and any applicable limits.

These checks establish what the number represents; they do not make separate contracts equivalent. If the documentation does not explain a displayed rate or payment clearly, treat its meaning as uncertain rather than assuming another venue uses the same method.

For business or technical review, preserve the context attached to the figure: contract identity, observation time, rate type, and interval. This helps prevent an estimate from being compared with a settled rate or a rate for one interval from being interpreted as though it applied to another. A value without those labels may be difficult to interpret even when its numerical format is clear.

## Risks and limits when interpreting funding rates

Funding can add to or reduce the result of holding a position, but it is only one component of that result. Price movement, leverage, margin, liquidation mechanics, and trading costs also matter. A funding rate does not summarize those other factors, and an unusually high or low reading does not guarantee a reversal, continuation, or profitable opportunity.

The key limitation is that funding describes a payment rule and its inputs; it does not settle the broader question of risk. A contract’s funding mechanism can produce a payment in either direction, while price changes and other contract conditions affect the overall position independently. Therefore, a rate should not be treated as a complete cost estimate or as a signal to act.

For operational details, consult the applicable contract documentation for its formula, schedule, payment direction, and eligibility rules. This explanation covers mechanics and interpretation, not a recommendation to trade, hedge, or respond to a particular rate.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
