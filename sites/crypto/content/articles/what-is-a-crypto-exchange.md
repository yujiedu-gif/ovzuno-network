---
title: "What Is a Crypto Exchange? Trading, Custody, and Settlement"
description: "Learn how a crypto exchange handles deposits, custody, order books, matching, internal balances, fees, and blockchain withdrawals without platform rankings."
date: "2026-10-18"
draft: false
content_type: "explainer"
topics: ["exchange-and-market-infrastructure"]
tags: ["cryptocurrency exchange", "centralized crypto exchange", "crypto order book", "crypto exchange custody"]
author: "editorial_team"
primary_keyword: "crypto exchange"
owned_question: "What is a crypto exchange, and how does it match, custody, and settle transactions?"
risk_level: "medium"
---

A crypto exchange is a venue that lets customers exchange one crypto asset for another or exchange crypto assets and government-issued currency. The visible trading screen is only one part of the system. A centralized crypto exchange commonly combines customer accounts, asset custody, an order-management system, a matching engine, an internal balance ledger, market data, and blockchain deposit and withdrawal infrastructure.

That combination explains why an exchange is not the same as a wallet. A wallet primarily manages the authority to sign blockchain transactions. An exchange may control wallets on behalf of many customers while also maintaining an internal record of what each customer is entitled to withdraw. Trading between exchange customers can occur on that internal system without placing every trade directly on a blockchain.

## What a crypto exchange does

An exchange organizes markets into **trading pairs**. In a BTC/USD market, bitcoin is the base asset and US dollars are the quote asset. An order states how much of the base asset a customer wants to buy or sell and, for a limit order, the acceptable price in the quote asset.

The venue receives orders, checks account permissions and available balances, and routes valid orders to a matching engine. It publishes market data derived from available orders and completed trades. When orders match, the exchange updates the customers' internal balances and produces execution records. It also manages the paths by which assets enter and leave the platform.

A single operator may perform several roles that are separated in traditional markets. BIS research notes that centralized crypto platforms can combine customer trading, custody, proprietary activity, lending, and token-related services. Not every exchange performs every role, but the combination matters because an incident in one function can affect the others.

## How a centralized exchange trade works

A simplified spot-trade lifecycle has six stages.

1. **The customer funds an account.** Fiat funding may arrive through a bank or payment rail. Crypto funding begins with an onchain transfer to a deposit address controlled or monitored by the exchange.
2. **The exchange credits an internal balance.** A crypto deposit is usually credited only after the platform detects the transaction and applies its network-confirmation policy. The internal account entry is not itself a new blockchain transaction.
3. **The customer submits an order.** The order identifies a market, side, quantity, order type, and any price or execution conditions. The platform reserves enough balance to prevent the same account funds from supporting conflicting open orders.
4. **The matching engine compares orders.** Compatible buy and sell instructions are matched according to the venue's published priority rules. A large order may execute in several partial fills against several counterparties.
5. **The internal ledger records the fills.** The exchange adjusts customer entitlements, records fees, and makes updated balances available for more trading or withdrawal. This accounting can happen much faster than a separate blockchain transfer for every fill.
6. **The customer may withdraw.** A withdrawal request passes platform security and policy checks. The exchange then constructs and broadcasts an onchain transaction from its wallet infrastructure to the requested destination.

The distinction between trade execution and blockchain withdrawal is fundamental. A completed trade proves that the venue's matching and accounting system recorded a fill. It does not automatically prove that the resulting asset has moved to a customer-controlled blockchain address.

## How an order book sets the available market

Many centralized exchanges use a central limit order book. BIS describes these venues as maintaining off-chain records of outstanding orders, a model familiar from traditional electronic markets. The **bid** side contains offers to buy; the **ask** side contains offers to sell. The highest bid and lowest ask define the visible top of book, and the difference between them is the spread.

A **limit order** states a price boundary and can rest in the book until it executes, expires, or is canceled. A **market order** seeks immediate execution against available orders and can fill at several prices. Other labels, such as stop, post-only, immediate-or-cancel, or fill-or-kill, describe venue-specific triggers or execution conditions. Their exact behavior must be checked against the exchange's current rules.

An order that adds resting liquidity is commonly called a maker order. An order that executes against resting liquidity is a taker order. Exchanges may charge different fees for those roles, but fee schedules, tiers, and incentives are commercial terms that can change.

The displayed last price is not a promise that another order will receive the same price. Available depth, order size, volatility, and latency affect execution. This article explains the infrastructure; it does not provide a trading strategy.

## Internal settlement versus blockchain settlement

The word *settlement* can refer to more than one boundary. Inside a centralized exchange, a trade can be settled on the operator's books when the buyer's and seller's internal balances are updated. The platform may net many customer positions without creating an onchain transaction for every match.

Blockchain settlement occurs when the relevant network accepts a deposit, withdrawal, or other transfer. The exchange chooses how many confirmations or what form of finality it requires before crediting a deposit. For withdrawals, it may batch several customer requests into one transaction, apply address controls, or delay processing for security review.

This layered model creates dependencies. A functioning matching engine does not guarantee that withdrawals are available. A blockchain that is producing blocks does not guarantee that an exchange's internal ledger or wallet system is operating. Operators therefore monitor market systems, customer accounting, node connectivity, key-management services, liquidity, and withdrawal queues separately.

## Custody and control

When a customer deposits crypto with a centralized exchange, the platform typically takes control of the keys used to move the deposited assets. BIS research uses this custody transfer as a central distinction between CEX and DEX models. The customer's dashboard balance is then a claim represented in the exchange's records rather than a private key held by the customer.

The exchange may divide assets among online transaction wallets, offline or restricted storage, and operational buffers. It can also consolidate deposits, rotate addresses, or send withdrawals from addresses different from the original deposit address. Public blockchain data alone may therefore be insufficient to reconstruct each customer's internal balance.

Custody arrangements have legal and operational dimensions that vary by jurisdiction and provider. Important questions include whether customer assets are segregated, who controls signing authority, how withdrawal approvals work, what happens during an incident, and what rights customers have if the operator fails. A balance display or a proof-of-reserves snapshot does not answer every liability, control, and legal-priority question.

## Centralized exchanges and decentralized exchanges

A decentralized exchange uses smart contracts or other blockchain-based mechanisms to execute or settle trades. In the public permissionless model examined by BIS, users can retain control of their assets until a trade is executed. Some DEXs use automated market makers and liquidity pools; others use order books, relayers, or hybrid arrangements.

The labels are not absolute. A DEX can depend on a hosted interface, administrator keys, an oracle, a relayer, or off-chain order storage. A centralized exchange can publish onchain addresses and cryptographic attestations while still controlling customer keys and internal accounting. The relevant comparison is which party controls assets, matching, listing, system changes, and transaction execution at each stage.

A separate guide is needed to explain DEX smart contracts and liquidity mechanisms in detail. The central point here is that CEX trading commonly happens on an operator-controlled ledger, while DEX execution or settlement depends more directly on blockchain transactions and smart-contract rules.

## What to examine before relying on an exchange

A neutral operational review should begin with the exact legal entity and jurisdiction serving the customer. Licensing, asset eligibility, customer protections, and reporting obligations are not universal. Check the platform's current terms and the relevant regulator rather than assuming that a global brand operates under one set of rules.

Then examine the operating model:

- Who controls deposited assets and how are customer entitlements recorded?
- Are customer assets segregated, and what evidence supports that statement?
- Which networks and token contracts are accepted for each deposit and withdrawal?
- How does the venue define deposit confirmation and withdrawal completion?
- What order-priority, cancellation, outage, and error-handling rules apply?
- Which fees can apply to trading, funding, conversion, and withdrawal?
- What security controls, withdrawal restrictions, and incident communications are documented?

These questions do not identify a universally best exchange. They reveal where trust and operational responsibility sit. A crypto exchange is a coordinated stack of market, custody, accounting, and blockchain systems; understanding those boundaries is more useful than treating it as a simple buy-and-sell website.

## Sources and references

- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
