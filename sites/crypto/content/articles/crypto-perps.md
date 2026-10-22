---
title: "Crypto perps: What perpetual futures are and how they work"
description: "Learn what crypto perps are, how perpetual futures use funding payments and margin, and why leverage, liquidation, and platform risks matter."
date: "2026-10-22"
draft: false
content_type: "definition"
topics: ["crypto_cards_spending"]
tags: ["perps crypto"]
author: "editorial_team"
primary_keyword: "crypto perps"
owned_question: "What are crypto perps, how do perpetual futures contracts work without an expiry date, and what risks should users understand?"
risk_level: "high"
---

Crypto perps are perpetual futures contracts that reference a crypto asset’s price but have no fixed expiration date. They are derivatives, not the same as owning or transferring the referenced asset. Funding payments, margin requirements, leverage, and liquidation procedures are contract-specific, so readers need the rules for the particular product to understand how it operates.

## What are crypto perps?

A derivative is a contract whose value is linked to an underlying reference. In a crypto perpetual future, that reference is a crypto asset’s price. “Perp” is shorthand for perpetual futures contract: unlike a dated future, it has no preset expiry or settlement date at which the contract must end.

The absence of a fixed expiry is the defining feature, but it does not establish all the other terms. A perp position is a contractual exposure to a price reference; it is not, by definition, the same thing as holding the referenced cryptocurrency in a wallet or transferring that asset to another person. The contract documentation determines how the position is created, managed, and closed.

That distinction matters when interpreting balances or account screens. A displayed position may represent a contract under a venue’s rules rather than a quantity of crypto available to transfer. The term “perp” alone does not tell a reader who holds collateral, how the position is settled, or what rights apply if a service provider is involved.

## How perpetual futures stay near the reference price

Perpetual futures commonly use funding payments between long and short positions as an incentive mechanism intended to help keep the contract price near a reference price. A long position generally benefits when the contract price rises, while a short position generally benefits when it falls; however, the specific payment direction and calculation are set by the contract’s rules and market conditions. The funding mechanism does not guarantee that a perp will match a spot or index price.

A reference price can be based on a spot market or an index assembled under the product’s rules, but the exact inputs and calculation must be checked in the contract documentation. A market-liquidity framework can include spread, transaction cost, price impact, and immediacy, and those dimensions change with transaction size and market conditions. These broad liquidity concepts do not establish how a particular perp computes an index, mark price, or funding payment.

For a reader, the practical question is not merely whether a product has funding. Check how often the contract applies funding, what inputs determine the payment, which position pays under which conditions, and how the venue reports the result. Do not assume the same formula or payment direction applies across products. Even when a funding mechanism is designed to encourage convergence, the price relationship is not assured.

## Margin, leverage, and liquidation

Margin is collateral assigned to support a derivatives position. Initial margin is the amount required to open or maintain a position under the product’s opening rules; maintenance margin is the minimum collateral level the contract requires for the position to remain open. These terms describe common concepts, but amounts, calculations, collateral eligibility, and monitoring rules vary by venue and contract.

Leverage means taking price exposure larger than the collateral posted. Because the position’s exposure is larger than the collateral amount, a given price move can produce a larger gain or loss relative to that collateral than it would without leverage. Leverage does not make the underlying movement predictable, and it does not limit losses to a particular amount unless the contract and applicable rules establish that outcome.

Liquidation is a venue-defined process that may reduce or close a position when collateral falls short of the required margin. The trigger, timing, execution method, and treatment of remaining collateral are not universal. A reader should look for the maintenance threshold, the price measure used to evaluate it, whether positions are partially reduced or fully closed, and any rules that apply if execution occurs during a fast or thin market.

These mechanics connect: leverage affects the size of exposure relative to collateral; margin rules determine when the position no longer meets requirements; and liquidation procedures describe what the venue may do then. The label “perpetual” does not specify any of these details. The contract documentation is needed to understand the particular sequence and potential consequences.

## Crypto perps compared with spot and dated futures

Spot trading involves buying or selling an asset. A perpetual future instead creates a derivative position that references a price. Those activities can have different ownership, custody, transfer, and settlement characteristics; one should not assume that a perp position is equivalent to holding the underlying crypto.

A dated future has an expiry or settlement date, while a perp has no fixed expiry date. That distinction does not mean a perp can never be closed or that its terms are otherwise uniform; it means the contract lacks a preset expiration date. The product’s rules explain how a user may close a position and what happens to it under specified conditions.

Neither comparison alone tells the reader how a particular product handles collateral, funding, execution, fees, or settlement. Those are separate contract features. Keeping the distinctions separate avoids mistaking a reference to an asset’s price for ownership of the asset, or mistaking the lack of expiry for the absence of other operating rules.

## Risks and details to verify before using a perp

Leverage can magnify gains and losses relative to posted collateral, and liquidation can close or reduce a position when margin requirements are not met. Funding payments can also be a cost or receipt depending on the contract’s direction and calculation. Price dislocations are possible because the contract price is not guaranteed to match a reference price. These risks are related, but none has the same mechanics in every product.

Counterparty and smart-contract risks should be evaluated where they apply to the product’s structure. The word “perp” alone does not establish whether a venue, custodian, or smart contract holds collateral or performs settlement. Nor does it prove that an arrangement has a particular security, recovery, or operational safeguard. Readers should identify the entity or code governing the contract and read the applicable terms rather than infer protections from the product label.

Before assessing a specific perp, verify its reference-price method, funding calculation and timing, accepted collateral, initial and maintenance margin rules, liquidation triggers and procedures, fees, settlement terms, and whether custody or smart contracts are involved. Market availability, funding rates, leverage limits, and other product details can vary; this article does not state current terms for any venue. Applicable regulation, tax treatment, and compliance obligations also require current authoritative information relevant to the product and jurisdiction. This explanation is educational and does not recommend trading or choosing a position size.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
