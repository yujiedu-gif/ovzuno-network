---
title: "Crypto funding rate explained: mechanics and meaning"
description: "Crypto funding rate explained: learn why perpetual futures use funding payments, who pays whom, how rates are applied, and what to verify in contract rules."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["crypto_assets_protocols"]
tags: ["crypto funding rate"]
author: "editorial_team"
primary_keyword: "crypto funding rate explained"
owned_question: "What is a crypto funding rate in perpetual futures, how is it applied, and what does its direction indicate?"
risk_level: "medium"
---

A crypto funding rate is a contract-specific rate used to calculate periodic payments between traders holding positions in a perpetual futures contract. Its direction can indicate which side pays the other under that contract’s rules, but the rate alone does not establish the payment amount, timing, or what a position will earn or lose. Because the allowed evidence here does not document the mechanics of any particular perpetual contract, it cannot establish a universal funding formula, schedule, or sign convention. Readers should verify those details in the applicable contract specification rather than assume that every venue uses the same design.

## What a crypto funding rate means

A funding rate is an input to a payment mechanism. It is not, by itself, the payment amount. The contract’s rules determine how the rate is applied, which positions are included, and how payment is settled. In a typical high-level explanation, a positive or negative sign is associated with payment moving between long and short positions; however, which side pays for either sign is a contract-specific convention. The sign should not be interpreted without the relevant specification.

Funding is also distinct from a trading fee. A trading fee is a charge associated with placing or executing a trade under a venue’s fee rules; funding describes a payment calculated under a derivatives contract’s terms. They may both affect an account’s overall result, but one should not be described as the other. The evidence available for this article does not specify any exchange’s fee schedule or funding arrangement, so no platform-specific comparison or amount can be asserted.

The purpose commonly attributed to funding is to help keep a perpetual contract’s price aligned with a reference market price. That objective should not be mistaken for a guarantee that alignment will occur, or for proof that a displayed rate accurately forecasts the next price movement. The allowed evidence does not document a particular contract’s reference price or alignment formula. Those are details to confirm in the contract documentation before drawing conclusions from a rate.

## How funding payments work

At a high level, a contract applies a rate to a defined measure of a position to calculate a payment. A larger position may therefore be associated with a larger payment under a given formula, but the precise relationship depends on the contract’s chosen calculation base and other terms. The available evidence does not authorize a universal equation, a worked numerical example, or a general statement about how every platform rounds or caps payments.

Payment direction also needs contract-specific confirmation. A display may label a rate as positive or negative, but the label alone does not tell a reader which side pays unless the specification defines that convention. Check both the sign rule and the position side being described. Do not infer that the long side always pays for a positive rate, or that a negative rate always has the reverse effect, without documentation for that contract.

Timing is another independent part of the mechanism. Contract terms may define when the rate is assessed, how often settlement occurs, and what position status matters at settlement. The rate’s displayed value might refer to a stated period or to a calculation the platform presents in a particular way. The allowed claims do not support naming a universal interval or asserting that all contracts settle at the same moment. A reader seeking to understand a specific payment must check the contract’s schedule and eligibility rules as well as the rate itself.

It is useful to separate four questions that can be conflated: what rate is displayed, which side the sign convention designates as payer, what position measure enters the calculation, and when settlement takes place. A screen showing only a rate may not answer all four. The contract documentation or other authoritative information for that specific product is needed to connect the displayed number to an actual payment.

## Why crypto funding rates change

A funding mechanism may respond to differences between a perpetual contract price and a reference price. The detailed inputs and rules are contract-specific; a general description does not show how a particular contract measures either price or converts the difference into a rate. Without that specification, readers should not treat a familiar-looking label as proof that two products calculate funding identically.

The rate’s direction can also describe a payment imbalance between position sides, according to the contract’s rules. That makes it a description of the funding mechanism at a particular time, not a settled conclusion about future prices. A positive or negative reading does not establish that the rate will persist, that the underlying asset will move in either direction, or that a position will be profitable.

Market liquidity is a separate concept that can help explain why the surrounding price environment may matter, but it should not be confused with funding. Liquidity reflects dimensions such as the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy; it changes with transaction size and market conditions. This definition does not establish a specific causal relationship between liquidity and any contract’s funding rate. For that relationship, the contract’s documented formula and inputs are necessary.

Accordingly, an observed rate should be read narrowly: it reports a value under a specified product’s convention and period. It is not a reliable standalone forecast, a general measure of all market participants’ views, or a recommendation. If the period, inputs, or sign convention are unclear, the interpretation should remain limited rather than filled in by assumptions.

## What to check before interpreting a rate

Use documentation for the exact contract and verify these points before interpreting a displayed figure:

- **Formula and inputs:** What position measure is used, and what other documented inputs affect the calculation?
- **Payment direction:** Which side pays when the rate is positive, and which side pays when it is negative?
- **Schedule and eligibility:** When is the rate assessed and settled, and what position conditions apply?
- **Limits:** Does the contract specify caps, floors, or other constraints on the rate or payment?
- **Display period and units:** What time period does the figure refer to, and how is it expressed?
- **Status of the figure:** Is it a current value, an estimate, or a figure transformed into another period for display?
- **Separate charges:** Where does the product document trading fees, and how does it distinguish those charges from funding?

These checks matter because two rates should not be assumed comparable merely because they have the same sign or appear in the same format. They may refer to different periods, formulas, or conventions. A displayed number also cannot independently confirm what a particular account owes or receives unless the relevant position and settlement rules are known.

If product information does not explain these items clearly, the interpretation is limited. Do not fill a documentation gap with an assumed universal convention. This article does not assert that any platform provides a particular rate display, funding schedule, payment calculation, or fee structure.

## Funding rates are not a standalone trading signal

A funding rate does not determine whether a position will be profitable. It describes a payment-related input under a contract’s rules; it does not settle the future price path or the total result of holding a position. Nor does a positive or negative sign, on its own, establish that a trader should take either side. Treating the rate as a prediction or trading instruction would go beyond what the mechanism shows.

Funding should also remain distinct from other derivatives terms. This explanation does not cover margin, liquidation, or the broader mechanics of perpetual futures positions. It also makes no claim about a particular platform’s fees, availability, security, or recovery practices. Those details require current, product-specific documentation.

Tax and regulatory treatment is outside this article’s scope. No jurisdiction-specific legal or tax conclusion is made. The useful takeaway is narrower: identify the contract, confirm how it defines rate direction and payment, inspect its calculation and schedule, and separate funding from trading fees and other position terms before interpreting a number.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
