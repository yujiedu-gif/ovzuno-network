---
title: "Cryptocurrency market: participants, venues, and infrastructure"
description: "Explore how participants, trading venues, and supporting systems connect across the cryptocurrency market, with boundaries between market-wide concepts and exchange."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: []
author: "editorial_team"
primary_keyword: "cryptocurrency market"
owned_question: "What does the cryptocurrency market include, and how do trading venues, participants, and market infrastructure connect without treating any one exchange or liquidity mechanism as the whole market?"
risk_level: "medium"
---

The cryptocurrency market is a connected ecosystem of transferable digital assets, participants, trading venues, and supporting services—not one exchange or one trading mechanism. To understand how its parts fit together, distinguish the asset being exchanged from the venue handling trading activity and from services such as custody and access. These functions can be combined or separated, so a description of one arrangement should not be treated as a universal market design.

## What the cryptocurrency market includes

For this overview, cryptocurrency means a digital asset, credit, or unit that can be cryptographically transferred between users of a blockchain network. The market includes activity involving such assets, but it is broader than a single platform where people place trades. It also includes the arrangements through which participants access assets and venues, and the supporting services connected to those activities. [source](<https://csrc.nist.gov/glossary/term/Cryptocurrency>)

A trading venue is a system or setting that brings together trading activity. Venue designs differ. For example, a centralized crypto exchange commonly maintains off-chain records of outstanding buy and sell orders in a limit order book. That is one model, not a definition of every venue or of the market as a whole. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

A useful map separates four things: the assets involved, the participants, the venues that organize trading, and related functions such as custody or settlement. The functions may sit within one organization or across different firms and services. Exchange-related functions can be combined or separated across firms, including trading and custody. [source](<https://www.bis.org/publ/work1227.pdf>)

This distinction matters because the word “market” can refer to broad activity across assets and arrangements, while “exchange” refers to a particular venue or operator. Neither label alone explains where assets are held, how a trade is recorded, or which systems provide information. Those are separate questions about the specific arrangement.

## Who participates and what roles they serve

Buyers and sellers are the direct trading participants: one side seeks an asset and another offers it. This basic description does not establish how common any type of participant is, why a participant acts, or whether the same parties appear across different venues. Those claims require evidence about a defined asset, venue, and period.

Trading venues organize activity under their own operating models. In a centralized-exchange example, an internal order book records outstanding buy and sell orders. This explains one venue’s trading records at a high level; it does not describe every transaction or all activity across the cryptocurrency market. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

Custody is a distinct function. In the centralized-exchange model described by the Bank for International Settlements, customers typically transfer funds and their custody to the exchange before trading on the venue’s internal order book. This is a bounded description of that model, not a rule for every exchange or product. Custody and trading can also be assigned across different firms or services. [source](<https://www.bis.org/publ/work1227.pdf>)

Service providers may support participants or venues by performing functions beyond trading. Some cryptoasset service providers may combine trading, custody, lending, market-making, and other services. The word “some” is important: it would be inaccurate to assume that every provider performs every function, or that one provider’s responsibilities describe the entire market.

Institutions can be relevant in particular arrangements, but their presence and role cannot be assumed across every asset or venue. For any specific case, identify the entity and function involved rather than relying on a broad market label. An organization’s trading role, custody role, or other service should be considered separately when the evidence supports doing so.

## How venues and supporting infrastructure connect

At a high level, participants connect to market-facing platforms either through direct interaction or through cryptoasset service providers. This describes ways access can be organized; it does not specify a particular interface or establish that every venue offers both paths.

Trading, custody, settlement, and information are related but distinct functions. A trading system handles trading activity according to its design. Custody concerns arrangements for holding or controlling access to assets. Settlement concerns completion of obligations under a particular arrangement. Data and access services help participants observe or interact with market-facing systems. A single provider may combine several functions, but the categories should not be treated as interchangeable.

A conceptual map of a crypto market environment can connect participants and access interfaces to trading systems, while showing custody, settlement, data, and external-service relationships as variable by arrangement. This is a functional map, not a universal technical blueprint.

For example, a centralized venue may keep an internal order book, while the custody and settlement arrangements require separate examination. The order-book description alone does not establish where assets are held or how settlement occurs. Likewise, a service that provides access should not automatically be treated as the venue, custodian, or settlement provider. Establish the role of each entity from evidence about the specific arrangement.

The same caution applies to infrastructure outside a venue. A market may depend on data or external services, but this overview does not specify a universal data-distribution design or identify a standard provider role. Builders and operators should first name the component they are assessing—venue, access service, custody arrangement, settlement function, or data source—then investigate its documented boundaries.

## How to interpret market activity across venues

Every market observation needs a scope. Ask which asset, venue, source, and time period it describes. A price or activity observation associated with one venue is not automatically a statement about every venue or the cryptocurrency market overall. Broader conclusions require evidence and a method that support that broader scope.

Comparisons also require attention to what each source measures. If information concerns different venues or uses different coverage, the observations may not answer the same question. This overview provides no market-wide price, volume, liquidity, or market-share measurements, so it cannot establish rankings, trends, or forecasts.

A practical reading sequence is to identify the asset and venue, note the source and period, and preserve those boundaries when describing the observation. If evidence is limited to one venue, state that limitation rather than converting the observation into a market-wide claim. If a conclusion depends on activity across multiple venues, the evidence must support that aggregation and explain its scope.

This approach is useful for business and technical decisions because it separates the question being asked from the evidence available. A venue-specific observation may help characterize that venue; it does not, by itself, establish how the broader market behaves. Avoid treating a single system’s records as a complete market picture unless a reliable, comparable method supports that conclusion.

## What this overview does not establish

This market map does not determine legal status, licensing, tax treatment, compliance obligations, availability, fees, yields, security controls, or recovery options. Those matters require current evidence specific to the relevant provider, product, arrangement, and jurisdiction. The general structure of a market cannot settle them.

For arrangements involving asset-backed tokens, a separate question is what claim or right the holder has and how backing assets relate to that claim. The legal effect, segregation, redemption, and insolvency treatment depend on the arrangement and applicable law. This is a reason to inspect specific documentation, not a conclusion about any particular asset or provider.

For a concrete use case, identify the asset, venue, and infrastructure function involved. Then verify the responsible entity, relevant jurisdiction and legal status, functional boundaries, custody and settlement arrangements, applicable terms, and current evidence for any operational or protection claims.

Keep technical questions—such as how a venue handles orders or distributes data—separate from questions about custody, settlement, or local requirements. The central takeaway is that the cryptocurrency market comprises connected roles and systems, while each venue and service represents only part of that broader structure.

## Sources and references

- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Cryptocurrency - Glossary](https://csrc.nist.gov/glossary/term/Cryptocurrency) — National Institute of Standards and Technology; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
