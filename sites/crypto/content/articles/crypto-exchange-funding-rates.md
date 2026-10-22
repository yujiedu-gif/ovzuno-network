---
title: "Crypto Exchange Funding Rates: How Perpetual-Futures Payments Work"
description: "Learn how crypto exchange funding rates relate to perpetual-futures payments, what affects their calculation, and which venue-specific rules to check."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "crypto exchange funding rates"
owned_question: "What are crypto exchange funding rates, how do they determine payments between perpetual-futures positions, and what should readers check when interpreting them?"
risk_level: "medium"
---

Crypto exchange funding rates are venue-defined rates used to calculate periodic payments between eligible long and short positions in perpetual futures. The rate is not the payment amount: the resulting debit or credit also depends on the position value, sign convention, timing, and other rules specified for that contract. Readers should check the current contract terms before interpreting a displayed figure.

## What a funding rate means in perpetual futures

A perpetual future is a futures contract designed to have no fixed expiration date. Funding is a periodic payment mechanism associated with positions in these contracts. Under the applicable venue rules, one side pays and the other receives. The funding rate is the input used in the venue’s payment calculation; it is not itself a dollar payment or a complete description of what a particular position will owe or receive.

This mechanism is distinct from a venue’s trading process. A centralized crypto exchange commonly records customer orders and executed trades in an internal order book and account system. That description of trading infrastructure does not establish how a particular contract calculates funding, which positions qualify, or when a payment is settled. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

Funding should also be distinguished from other costs and market conditions. Trading fees concern trade execution, while funding concerns a payment defined by the perpetual contract’s rules. Market liquidity is another separate concept: it reflects the time and expense of buying or selling, including spread, transaction cost, price impact, and immediacy. [source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>) These are different concepts, even where a venue presents several of them together in an interface.

Some crypto service providers may combine trading with other activities, such as custody, lending, or market-making, while others may not. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>) The existence of these additional services does not establish that they are part of a funding payment or that every venue offers them. For interpreting funding, the relevant source is the specification for the particular contract, not a general description of the provider’s other activities.

## How crypto exchange funding rates translate into payments

Conceptually, a funding payment depends on the applicable rate and a venue-defined measure of the position’s value or notional. Notional means the value basis to which the rate is applied. The exact meaning and calculation of that value basis must come from the contract rules; it should not be assumed from the rate display alone.

A simplified illustration makes the distinction clear. Suppose a contract specification said to apply a rate of 0.1% to a position value of $10,000 for one funding interval. Multiplying those assumed inputs gives $10 before applying the venue’s payer direction, rounding, eligibility, and settlement rules. This is an arithmetic illustration, not a universal formula or a verified example from any venue. If the venue defined the rate differently, used another value basis, or applied additional rules, the realized payment could differ.

The sign convention determines which side pays and which side receives. A positive or negative sign has no useful payer meaning without the venue’s definition for that specific contract. Readers should locate the rule that maps the sign to long and short positions rather than importing a convention from another exchange or contract.

Timing also matters. A displayed rate may not be the final rate used at settlement, and a position may need to meet contract-specific eligibility conditions at a defined time. Rounding, position snapshots, settlement timing, and calculation stages can affect the debit or credit. The rate display alone does not establish these rules.

## Why rates can differ across venues and contracts

Funding rates may differ because venues and contracts can define the calculation differently. Rules to investigate include the formula, reference markets, observation window, and any caps or floors. These are possible contract-specific features, not assertions that every venue uses each feature. Without verified specifications for a named contract, there is no basis to present one formula, reference market, cap, or floor as universal.

The time basis is especially important when looking at rates from different contracts. One displayed number may be stated for a single interval, while another may be annualized or otherwise presented on a different basis. One figure may be estimated and another finalized. These numbers are not directly comparable unless their contracts, calculation stages, interval conventions, and rate definitions match.

Rates can also vary by contract and observation time. A number shown for one perpetual contract does not, by itself, describe another contract or establish what the first contract’s later rate will be. Even when two venues use the same label, the label alone does not prove that their calculations or settlement procedures are equivalent.

Separate the displayed data from the payment rule. An interface may show a rate, but the contract specification determines how that rate is used and what payment follows. If the display omits its time basis or status, treat that as missing context rather than filling it in by assumption.

## What to verify before interpreting a displayed rate

Use the venue’s current contract specification and check the following details:

- **Contract identity:** Confirm the exact perpetual-futures contract and which position the displayed figure concerns.
- **Sign convention:** Find the contract’s definition of positive and negative rates, including which side pays and which receives.
- **Payment interval:** Check how often the contract settles funding and identify the next settlement time. Do not assume the interval from a rate’s label.
- **Rate basis and status:** Determine whether the number is per interval, annualized, estimated, or finalized, and which calculation window it represents.
- **Payment calculation:** Verify the position-value or notional basis, formula, and any rounding rule.
- **Eligibility:** Check what position snapshot or other condition determines whether a position is included at settlement.
- **Limits and settlement:** Confirm whether the contract specifies caps or floors and how the venue applies the rate to accounts at settlement.

These checks help explain what a displayed number means; they are not a recommendation to open, close, or hold a position. If the current specification does not answer a question, the figure displayed in an interface cannot independently establish the missing rule. A venue’s general product description may not substitute for the current terms of the specific contract.

## Scope and risks of funding-rate information

A funding rate is not a price forecast and does not guarantee a future payment. It describes a contract-defined input for a particular calculation context. Rates can change, and the realized payment depends on the applicable rules and the position that qualifies under them. A current or historical figure alone does not establish a future rate, payment, or market movement.

Funding is not a complete account of a position’s outcome. Fees, margin rules, liquidation mechanics, and market movements are separate considerations. This explanation does not calculate a trader’s complete profit or loss, and it does not claim that any displayed funding figure makes a position profitable or safe. The payment mechanism should be read as one contract feature, not as a summary of every consequence of holding a position.

The relevant practical distinction is between the rate and the payment. The rate is an input defined by the venue; the payment is the resulting debit or credit after applying the contract’s calculation, sign, timing, eligibility, and settlement rules. Verify those details in current documentation for the specific perpetual contract before interpreting its displayed rate. This article does not address exchange rankings, trading strategies, price predictions, or jurisdiction-specific treatment.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
