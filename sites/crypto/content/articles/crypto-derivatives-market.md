---
title: "Crypto Derivatives Market: Structure, Contracts, and Infrastructure"
description: "Explore how the crypto derivatives market is organized, from contract types and trading venues to participants, collateral, clearing, and risk controls."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "crypto derivatives market"
owned_question: "How is the crypto derivatives market structured, and how do its contracts, venues, participants, and risk controls fit together?"
risk_level: "high"
---

The crypto derivatives market is a set of contracts and services for trading exposure linked to cryptoassets, with trading, custody, settlement, and other functions potentially handled by different firms or combined in one provider. To understand its structure, keep three layers distinct: the contract defines the exposure and obligations; a venue or access arrangement supports trading; and related entities may handle functions such as custody or settlement. The evidence available here supports this functional map, but not detailed mechanics for particular derivative contracts or margin systems. Those terms must be verified in current product and provider documentation.

## What the crypto derivatives market includes

A derivative is generally a contract whose value is linked to an underlying asset, index, or other reference. This article uses that as a conceptual definition rather than a claim about the terms of any specific crypto product. A derivative is distinct from a spot purchase: it provides contractual exposure rather than, by definition, being the same transaction as directly acquiring the referenced asset. The available evidence does not establish how a particular contract calculates value, what rights it creates, or how it ends.

The distinction matters because product labels do not describe the full operating arrangement. Exchange-related functions, including trading, custody, and other cryptoasset activities, may be distributed across different firms and services. [source](<https://www.bis.org/publications/fsi-summary-financial-stability-implications-multifunction-cryptoasset-intermediaries-executive-summary>) A crypto trading environment may also involve custody, settlement, market surveillance, or other forms of intermediation, but that list is not a checklist of duties performed by every venue. [source](<https://www.iosco.org/news/pdf/IOSCONEWS712.pdf>)

As a result, “the derivatives market” is best treated as an ecosystem rather than a single institution or technical system. The exact boundaries depend on the arrangement. A venue’s market-facing role does not, by itself, establish who holds assets, records positions, or handles post-trade obligations. Those responsibilities need separate identification.

## Contract types and their key mechanics

Futures, perpetual contracts, and options are different contract categories, but the allowed evidence does not substantiate their specific payoff structures or lifecycle mechanics. It therefore cannot support a detailed explanation of how any of these products expires, settles, references a price, or uses funding payments. Nor does it establish that a contract labeled “perpetual” or “future” follows a universal design.

For an infrastructure review, treat each contract specification as the source for its own terms. Check what reference determines the contract’s value, whether an expiry or other ending condition applies, which events trigger settlement, and what rules address collateral and positions. For an option, do not infer its holder’s rights or obligations from the label alone; confirm them in its governing product documentation. These are verification steps, not assumptions about standard terms.

This keeps contract design separate from venue design. A venue can support access to trading, while custody or other related services may be provided elsewhere. Exchange-related functions may be combined or separated among firms, so no single architecture should be inferred from a product category. [source](<https://www.bis.org/publications/fsi-summary-financial-stability-implications-multifunction-cryptoasset-intermediaries-executive-summary>)

## Venues, participants, and market functions

A venue is one part of the market arrangement, not necessarily the operator of every function. Some cryptoasset service providers may combine trading, custody, lending, market-making, and other services, but that observation does not apply to every provider. [source](<https://www.bis.org/publications/fsi-paper-27-cryptoasset-service-providers-financial-intermediaries-risks-and-policy-approaches>) A conceptual map should therefore identify the trading venue, any access or service provider, and the entities responsible for custody or settlement where those functions exist.

Market participants can carry distinct responsibilities, but the evidence available for this article does not establish a complete or universal roster for derivatives markets. It does not document the precise duties of brokers, liquidity providers, clearing entities, or market makers in a particular arrangement. A role label alone should not be treated as proof of what an entity does. Confirm the function in the relevant service and product documents.

Liquidity is one useful way to describe trading conditions, but it is not a promise that a particular order can be completed at a particular price. Market liquidity reflects the time and expense involved in buying or selling, including spread, transaction cost, price impact, and immediacy; it changes with transaction size and market conditions. [source](<https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview>) This framework helps separate the trading environment from the contract itself, without establishing liquidity for any specific derivative.

## From order to settlement: the market lifecycle

A functional lifecycle map starts with the contract terms, then traces the route from an order to its post-trade obligations. Identify the interface or service through which an order is submitted, the entity responsible for trading activity, how positions are recorded, and which process handles settlement or other obligations. If custody is part of the arrangement, identify the responsible entity separately from the trading venue.

This is a map of questions, not a universal transaction sequence. Trading, custody, and other exchange-related functions may be spread across firms or combined, and crypto trading environments can involve settlement alongside other activities without every venue performing them all. [source](<https://www.bis.org/publications/fsi-summary-financial-stability-implications-multifunction-cryptoasset-intermediaries-executive-summary>) [source](<https://www.iosco.org/news/pdf/IOSCONEWS712.pdf>)

Settlement should not be treated as synonymous with execution. As a general infrastructure distinction, settlement systems and central securities depositories have distinct roles, and relevant guidance addresses linked settlement obligations and custody-related risk. That is a conceptual distinction; it does not establish that a specific crypto derivatives venue uses such a system or falls into a particular classification. [source](<https://www.bis.org/committees/cpmi/pfmi/overview>)

For an operational map, record the responsible entity for each stage and flag any undocumented handoff. Do not infer settlement terms, custody arrangements, or responsibility for unresolved obligations solely because an order appears on a trading interface. The evidence does not define a universal derivatives lifecycle or establish that an interface or market-data feed determines contract terms.

## Collateral, margin, and risk controls

Collateral and margin are central topics to investigate, but the allowed evidence does not substantiate definitions of initial or maintenance margin or explain how a provider values collateral, calculates requirements, or handles liquidation. It also does not support claims that mark prices, position limits, or specific risk controls are universal features. Product and provider documentation must answer those questions for the arrangement under review.

Separate the contractual obligation from the provider’s operations. First, identify what the contract says about collateral and settlement. Then establish which entity holds or controls relevant assets and which documented process applies when an obligation is not met. Do not infer a guaranteed outcome or protection from the existence of a margin process; the available evidence establishes neither.

The same discipline applies to claims about security, recovery, fees, yields or funding payments, availability, regulation, tax, jurisdiction, and compliance. The allowed evidence here does not substantiate product-specific claims in those areas. They should be checked against current, specific documentation rather than generalized across venues or providers.

The resulting market map is functional: contracts set exposure and obligations; venues and access arrangements support trading; and related firms or services may provide custody, settlement, liquidity, or other functions. Because these functions can be combined or separated, a useful infrastructure review follows responsibilities across the full arrangement instead of treating a venue, contract label, or interface as a complete description of the market.

## Sources and references

- [IOSCO Finalizes its Policy Recommendations for Crypto and Digital Asset Markets](https://www.iosco.org/news/pdf/IOSCONEWS712.pdf) — International Organization of Securities Commissions (IOSCO); retrieved 2026-10-21.
- [The financial stability implications of multifunction cryptoasset intermediaries - Executive Summary](https://www.bis.org/publications/fsi-summary-financial-stability-implications-multifunction-cryptoasset-intermediaries-executive-summary) — Bank for International Settlements, Financial Stability Institute; retrieved 2026-10-21.
- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [Principles for Financial Market Infrastructures](https://www.bis.org/committees/cpmi/pfmi/overview) — Bank for International Settlements, Committee on Payments and Market Infrastructures (CPMI), and IOSCO; retrieved 2026-10-21.
- [Cryptoasset service providers as financial intermediaries: risks and policy approaches](https://www.bis.org/publications/fsi-paper-27-cryptoasset-service-providers-financial-intermediaries-risks-and-policy-approaches) — Bank for International Settlements, Financial Stability Institute; retrieved 2026-10-21.
