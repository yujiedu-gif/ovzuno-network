---
title: "Crypto exchange market making: roles, mechanisms, and infrastructure"
description: "Explore crypto exchange market making, how it interacts with exchange infrastructure, the roles involved, and operational risks that require verification."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "crypto exchange market making"
owned_question: "How does market making function within crypto exchange infrastructure, and how do its mechanisms, participants, and risks differ from exchange operation and liquidity provision in decentralized pools?"
risk_level: "medium"
---

Crypto exchange market making is activity in which a participant manages buy and sell offers, while the exchange operates the venue’s trading infrastructure. That differs from supplying assets to an automated market maker (AMM) pool, where a smart-contract pool provides swap inventory. The labels alone establish neither a venue’s liquidity nor the quality or terms of any particular service.

## What crypto exchange market making means

Market making, in this infrastructure context, refers to a participant’s trading activity: placing and managing buy and sell offers. The participant is distinct from the exchange that provides the trading venue. This distinction is useful for builders and operators because it separates a source of trading activity from the systems and services that process activity.

An exchange environment can be mapped conceptually as participants and access interfaces connected to trading systems, alongside relationships involving custody, settlement, data, and external services. This is a functional map, not a universal technical design; the arrangement varies by provider. The participant’s orders therefore should not be treated as proof of how a venue accepts, records, or processes them.

The term “market making” also does not, by itself, establish a contractual service level. It does not prove that quotes must remain available, that a participant will maintain a specified amount of trading depth, or that a venue provides a particular execution outcome. Such terms require current, specific documentation rather than inference from the name of an activity.

## How market making interacts with exchange infrastructure

At a high level, exchange-facing access connects participants with a market-facing trading platform, either through direct interaction or through cryptoasset service providers. This describes the access relationship, not a particular interface technology or provider.

The participant’s trading systems and connectivity are separate from the venue’s infrastructure. A venue may provide trading functionality after assets are deposited, but performance and liquidity vary by venue, asset pair, and market conditions. This is a general operating model, not a promise about any specific market maker, trading pair, or execution. [source](<https://www.bis.org/publ/work1227.pdf>)

For an implementation review, map the responsibilities rather than assuming they belong to one party. Identify who operates the venue, who submits and manages orders, and where custody, settlement, data, and external services fit. The architecture and rules of a specific exchange require its own documentation; the general market-making concept does not establish its APIs, access controls, order handling, or program conditions.

## Orders, quoting, and inventory management

A two-sided quote means that a participant offers to buy and to sell. When an offer is executed, the participant’s holdings change. Those holdings create inventory exposure: the participant’s position may have a different value as prices change. Managing offers and inventory is part of the activity, but it does not imply control over market outcomes.

An order’s operational context matters. The venue’s rules and systems determine how submitted orders are handled, while the participant decides what activity to submit under the applicable terms. The available evidence does not establish a universal quoting schedule, order-control method, or obligation to keep quotes open. A reader evaluating a particular arrangement should look for explicit venue rules and contractual terms.

Do not transfer execution findings from one infrastructure model to another. For public-blockchain AMM swaps, transaction visibility, execution ordering, pool depth, and price impact can affect execution before block inclusion. That finding is specific to the described public-blockchain AMM context; it is not evidence about the matching rules or performance of every centralized exchange. [source](<https://www.bis.org/publications/trading-defi-era-automated-market-maker>)

Fees, connectivity, latency, access permissions, and execution conditions may matter operationally, but their actual values and effects require venue-specific evidence. No particular fee, API behavior, incentive, or quoting obligation can be inferred from the term “market making.”

## How exchange market making differs from other liquidity models

Market-making participation and exchange matching are separate functions. The participant contributes trading activity; the venue supplies the platform and its trading systems. A different firm or service may also perform exchange-related functions, and arrangements vary.

Market making also differs from liquidity provision in a pool-based AMM. In the Uniswap v2 example, a pool uses deposited reserves of a token pair as swap inventory, and liquidity-provider shares represent contributions. This is a specific protocol example, not a universal description of all decentralized exchanges or pools.

An AMM liquidity provider contributes assets to a pool and can receive a share of trading fees while bearing inventory and adverse-selection risk. Pool formulas, fee tiers, price ranges, and loss allocation vary by protocol and position. This role is different from managing buy and sell offers as a participant on an exchange. Neither distinction proves that a particular market has available depth, continuous quotes, a particular spread, or low price impact.

A useful comparison is therefore functional, not promotional: identify who contributes trading activity or assets, and identify which system processes a trade. In an exchange arrangement, the participant’s orders interact with venue infrastructure; in the cited AMM example, deposited pool reserves supply swap inventory. The specific design, terms, and operating conditions still need separate verification.

## Operational, security, and compliance considerations

Separate trading activity from custody and settlement arrangements. In the typical centralized-exchange model described by BIS, a user transfers funds and their custody to the exchange before trading on its internal order book. Custody and legal ownership arrangements vary by platform and jurisdiction, so this model should not be assumed for every venue or market-making participant.

Access controls, API-key permissions, incident handling, and recovery procedures are likewise arrangement-specific. Require current, authoritative evidence for the controls a venue or participant actually operates. A stated security feature does not establish that every account, asset, or operational risk is addressed, and the evidence here does not establish any provider’s recovery outcomes.

The allowed evidence also does not support a general conclusion about licensing, compliance duties, or tax treatment for a particular market-making arrangement. Those questions require current, relevant jurisdictional sources and, for tax questions, qualified advice. Avoid treating a general description of infrastructure as a legal, compliance, or tax determination.

## Questions to verify before evaluating an arrangement

Before evaluating a market-making implementation, obtain current documentation that answers these questions:

- Which entity operates the venue and which entity submits or manages orders?
- What access methods, account permissions, and activity rules apply?
- Are quotes subject to stated conditions or obligations, and where are those conditions documented?
- How are fees, incentives, monitoring, settlement, and operational responsibilities defined?
- What security controls, incident processes, and recovery procedures are documented, and what limitations do they state?
- Which jurisdiction-specific compliance and tax issues need separate authoritative review?

Keep documented terms distinct from promotional claims and assumptions. A functional map can clarify where market making fits, but it cannot verify a particular venue’s availability, program terms, security, recovery, or performance.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Trading in the DeFi era: automated market-makers](https://www.bis.org/publications/trading-defi-era-automated-market-maker) — Bank for International Settlements; retrieved 2026-10-18.
