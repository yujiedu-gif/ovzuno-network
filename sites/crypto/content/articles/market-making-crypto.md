---
title: "Market Making Crypto: How It Works"
description: "Understand Market Making Crypto, including its architecture, operating flow, participants, technical dependencies, limitations, and practical verification points."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["crypto market making"]
author: "editorial_team"
primary_keyword: "market making crypto"
owned_question: "What is crypto market making, and how does it support liquidity on digital asset exchanges?"
risk_level: "medium"
---

# Market Making Crypto: How It Works

Crypto market making is the activity of supplying buy or sell orders to a digital asset exchange, potentially giving other participants a counterparty for a trade. A market maker’s orders may be executed, remain unfilled, or be changed or withdrawn, depending on the venue and its operating arrangements. Market making can contribute to liquidity, but it does not guarantee that a trade will be available, filled, or completed at a particular price.

The term needs a system boundary. This explainer focuses on market making in exchange trading, especially the order-book model. It does not assess providers, recommend an asset, or describe jurisdiction-specific legal or tax requirements. Exchange designs and operating arrangements differ, so the discussion distinguishes general liquidity concepts from venue-dependent mechanics.

## What Market Making Crypto means

In an order-book setting, market making means supplying orders that may be available for other participants to trade against. A participant might offer to buy, sell, or both. Whether another participant can execute against an order depends on the orders available and the venue’s process. This is a conceptual description, not a claim that every venue uses the same order types, matching rules, or settlement arrangements.

Market making is related to liquidity, but the two are not interchangeable. The Bank for International Settlements describes market liquidity through the time and expense involved in buying or selling. Relevant dimensions include the bid-ask spread, transaction cost, price impact, and immediacy. These dimensions can change with transaction size and market conditions. [claim_market_liquidity_dimensions]

A market maker can support liquidity by adding potential trading interest to a venue. But an order or quote alone does not establish how much can be traded, how quickly a trade can occur, or what the total cost will be. The contribution depends on the orders actually available, their size and prices, and the circumstances in which another participant seeks to trade. Liquidity is therefore better understood as a set of execution conditions than as a single number or a guarantee.

## Core components of Market Making Crypto

A basic market-making arrangement involves several functional components. Their exact design is venue-specific; this is a map of roles, not a universal technical architecture.

- **Venue and market:** The exchange defines the market, its trading rules, and the interfaces through which participants interact. Available products and settlement arrangements can differ.
- **Order book and records:** A centralized crypto exchange commonly records customer orders and executed trades in an internal order book and account system. Venues may use additional matching models, products, and settlement arrangements. [claim_bis_exchange_internal_order_book]
- **Market-making participant:** An individual or organization supplies orders. The visible orders alone do not establish the participant’s inventory, risk controls, mandate, or relationship with the exchange.
- **Software and interfaces:** A participant needs a way to access market information and interact with the venue. The specific interface, supported actions, permissions, message behavior, and operating limits must be checked against the venue’s current documentation.
- **Accounts and assets:** The venue’s account and trading model determines what access and balances are needed. A centralized exchange may require assets to be deposited before trading, but that general model does not establish the specific custody or access terms of any provider.

A centralized crypto exchange operator may combine third-party trading, proprietary trading, margin lending, token issuance, and custody services. Not every exchange performs every function. Combining roles can create operational dependencies and conflicts, but the general possibility does not establish that a specific venue has a particular conflict. [claim_bis_cex_combined_functions]

## How Market Making Crypto works

The following sequence is a practical conceptual workflow. Specific steps, order states, and timing depend on the venue and its interfaces.

1. **Identify the venue and market.** The participant selects an exchange and trading pair, then checks the applicable market rules, account requirements, and available products. Those details are not universal.
2. **Observe available market information.** The participant obtains whatever market data the venue provides. An order-book view is a representation of available orders at a point in time; by itself, it does not establish that those orders will remain available.
3. **Determine orders to supply.** The participant chooses whether to place buy orders, sell orders, or both, and sets prices and quantities. This article does not prescribe a quoting strategy. The resulting liquidity conditions depend in part on trade size and market conditions.
4. **Submit orders through the venue.** The participant sends orders using the supported process. Whether a request is accepted and how it is represented in venue state depend on the exchange’s documented implementation. Teams should distinguish an intended request from a confirmed order state.
5. **Wait for a possible trade or update the order.** Other participants may trade against available orders. Whether and how an order can be amended or withdrawn depends on the venue. A displayed order is not a promise that another participant will execute against it.
6. **Check execution and account records.** If a trade occurs, the participant needs to establish what executed and what orders or balances remain. Centralized exchanges commonly use internal order-book and account records, but recordkeeping and settlement arrangements vary by venue. [claim_bis_exchange_internal_order_book]
7. **Continue monitoring.** Market conditions and order availability can change. A working process therefore depends on checking current state and reconciling activity, not only on the initial placement of orders. The precise monitoring tools and operational controls are implementation-dependent.

In the general centralized-exchange model, trading can be near-real-time, with liquid order books and advanced order functionality after assets are deposited. These are model-level characteristics, not guarantees for a specific venue or pair: performance and liquidity vary by venue, asset pair, and market conditions. [claim_bis_cex_fast_internal_trading]

## Trust and control boundaries

Market making takes place within a broader venue and account system. The market-making participant supplies orders using the access it has; the exchange operates its own interfaces and trading or account processes. The exact division of responsibility, status reporting, and settlement depends on the venue’s documented arrangements.

For a centralized exchange, an internal order book and account system should not be assumed to be the same thing as an individual public-blockchain settlement record. The accepted evidence describes the internal-record model and notes that venues can use additional settlement arrangements. It does not establish that every trade is individually recorded on a public chain, or that any particular custody, segregation, or recovery arrangement applies.

The exchange may combine several functions, but that does not mean every provider does so or that each function has the same terms. If trading, proprietary activity, lending, token issuance, and custody are combined, operational dependencies or conflicts may be relevant. The details must be established from the provider’s current documentation; they cannot be inferred from the words “exchange” or “market maker.” [claim_bis_cex_combined_functions]

## Limitations and failure modes

Market making can add orders, but it cannot guarantee liquidity. A trade may be larger than available orders, the spread or transaction cost may be substantial, price impact may be material, or immediate execution may not be available. These dimensions vary with transaction size and market conditions, so an observation at one moment may not describe later or larger trades. [claim_market_liquidity_dimensions]

The order-book view also has limits: it shows available information, not a guarantee about future availability. Venue-specific performance, matching models, account processes, and settlement arrangements can affect the path from an order request to a completed trade. The general description of near-real-time centralized trading does not guarantee performance or liquidity for a particular venue, pair, or market condition. [claim_bis_cex_fast_internal_trading]

Finally, a venue’s role and a market maker’s role should not be conflated. An exchange may perform several functions, but not every exchange performs all of them. Treating trading, proprietary activity, lending, issuance, and custody as interchangeable can obscure dependencies and conflicts. Each function and its terms require separate verification. [claim_bis_cex_combined_functions]

## What teams should verify

Builders, operators, institutions, and technical decision-makers can use these questions to map a market-making workflow without assuming that all venues work alike:

- **Venue and market model:** Is the venue centralized, decentralized, or another design? What matching, account, and settlement arrangements apply to the specific market?
- **Order lifecycle:** Which order types and actions are supported? How does the official documentation describe acceptance, execution, status, and cancellation?
- **Market information:** What does a market-data view represent, and what documentation explains how to interpret it? Do not treat a snapshot as proof that an order will remain available.
- **Liquidity dimensions:** For relevant trade sizes and conditions, what evidence is available about spread, transaction costs, price impact, and immediacy? These dimensions are related but not interchangeable.
- **Account and asset requirements:** Must assets be deposited before trading? Which entity operates the account, and what do current documents say about custody and access? The general exchange model does not answer provider-specific questions.
- **Records and settlement:** Where are orders and executed trades recorded? What settlement arrangements apply, and which records can the participant inspect? Verify the venue’s own documentation rather than assuming a public-chain record for each trade.
- **Combined functions:** Does the exchange also conduct proprietary activity, lending, token issuance, or custody? If so, what documentation describes the relevant roles and dependencies?
- **Evidence freshness:** Use current official documentation for interface behavior, account arrangements, fees, and settlement. The general claims in this explainer do not establish current provider availability, provider-specific fees, security outcomes, or rules in any jurisdiction.

Crypto market making is best understood as order supply within a larger exchange and account system. It can give other participants additional opportunities to trade, while the liquidity those orders provide remains conditional on size, market conditions, venue operation, and actual order availability. A technical evaluation should follow that full context without treating a displayed quote as a guarantee.

## Sources and references

- [Market and funding liquidity - an overview](https://www.bis.org/speeches/20160502-market-and-funding-liquidity-overview) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
