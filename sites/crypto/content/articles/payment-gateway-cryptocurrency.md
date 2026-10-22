---
title: "Payment gateway cryptocurrency: how the payment flow works"
description: "Learn what a payment gateway cryptocurrency setup does, how a customer payment moves through confirmation and settlement, and which responsibilities vary."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_payments"]
tags: []
author: "editorial_team"
primary_keyword: "payment gateway cryptocurrency"
owned_question: "What is a cryptocurrency payment gateway, and how does it handle a payment from checkout through confirmation and settlement?"
risk_level: "medium"
---

A cryptocurrency payment gateway connects a checkout payment request with steps for receiving and monitoring a customer’s blockchain payment. It may also connect to conversion or settlement services, but those functions are not inherent in every gateway. To understand the flow, separate the merchant’s checkout, the gateway or processor, the customer’s wallet, and the blockchain network. Each can have a different role, and a transaction being broadcast does not by itself mean that the merchant’s settlement conditions have been met. [source](<https://docs.btcpayserver.org/Users/invoices/>)

## What a cryptocurrency payment gateway does

A gateway is a software layer that links a payment request at checkout to payment-handling steps. It may pass information between the checkout and a payment service, present instructions to the customer, or report transaction status. The term “gateway” alone does not establish that the service holds funds, exchanges cryptocurrency, or pays proceeds to the merchant.

The **checkout** is the merchant-facing part of a purchase: it identifies the order and presents the amount due. A **gateway** connects that request to the payment flow. A **processor** may carry out additional handling, but whether it does so depends on the arrangement. These labels do not guarantee that different services perform identical functions, and one service can combine roles that another keeps separate.

A **wallet** is software or another system used to manage or use the keys and addresses involved in a crypto transaction. The customer uses a wallet to authorize a payment; the wallet is not the blockchain network. The **blockchain network** applies its protocol rules to transactions and updates its shared record through its transaction process. A **settlement condition** is the rule an arrangement uses to decide when it treats a payment as complete for its own purposes. That operational decision is distinct from simply observing a transaction.

The exact division of responsibilities matters. The checkout may create the order and payment request; a gateway or processor may relay the request or monitor transaction information; the wallet authorizes the transaction; and the network validates and processes it. The merchant’s arrangement determines how a reported payment status affects order fulfillment. Conversion, custody, and settlement may be included, handled elsewhere, or absent; the gateway label does not answer those questions.

## Payment gateway cryptocurrency flow, from checkout to confirmation

A generic payment starts when checkout presents an amount and payment instructions. Those instructions must correspond to the recipient’s requirements, including the requested asset and network. Payment instructions are not interchangeable across every asset and network, so a customer or business should compare the exact asset and network with the recipient’s instructions before authorizing.

The customer then uses a wallet to authorize a transaction. As one network-specific illustration, an Ethereum transaction includes a sender-authorizing signature, nonce, destination, value or contract data, gas limit, and fee parameters according to its transaction type. This example describes Ethereum transaction fields; it is not a universal format for all cryptocurrencies. [source](<https://ethereum.org/developers/docs/transactions/>)

After authorization, the transaction is submitted to the network. Network processing is not the same as a merchant’s order status. As one Bitcoin-specific example, a full node generally relays a received transaction after independently checking whether it satisfies applicable validity and relay-policy rules. That describes Bitcoin peer-to-peer behavior, not every network’s process. [source](<https://developer.bitcoin.org/devguide/p2p_network.html>)

A gateway or connected service may monitor for a transaction that matches the payment request, but monitoring and confirmation criteria depend on the implementation. The available evidence does not establish one confirmation count or a universal definition of “confirmed” or “final.” A payment interface’s status labels therefore need to be understood in the context of that service’s rules and the merchant’s operating policy.

Most importantly, a merchant should not fulfill an order solely because a transaction was broadcast. The merchant’s configured settlement conditions should be met before fulfillment. What those conditions are depends on the network, asset, transaction, and arrangement; the general flow does not prescribe a threshold. [source](<https://docs.btcpayserver.org/Users/invoices/>)

## Conversion and settlement are separate steps

**Conversion** means exchanging the received cryptocurrency for another asset or currency. **Settlement** means making value available according to the merchant’s arrangement. A payment can be detected without proving that conversion or merchant payout has occurred. A service may handle cryptocurrency directly, offer a conversion step, or connect to another service, but the exact path and terms vary.

The destination for funds is also arrangement-specific. A payment might be associated with a merchant-controlled wallet, handled by a third party, or routed through another agreed setup. The evidence here does not support a general claim about who holds funds in every gateway arrangement or how quickly a merchant receives them. A business must verify those details in the relevant service documentation and terms rather than infer them from the word “gateway.”

Fees, supported assets and networks, conversion rates, settlement timing, and availability are likewise provider-specific and time-sensitive. This explainer does not assert any particular amount, schedule, or capability. Even when a service provides a transaction reference or status, that information should not be confused with the merchant’s own accounting or fulfillment decision.

## Responsibilities and operational points to verify

Before relying on a payment flow, business and product teams should map each responsibility to the party that actually performs it. Establish who creates the checkout request, controls the destination for funds, monitors network activity, decides when a payment meets confirmation criteria, reconciles transactions to orders, and handles customer questions. If conversion, refunds, or other exception handling are offered, identify which party is responsible for them and under what terms.

Compatibility is a separate check from monitoring. Confirm that the payment request names the intended asset and network and that the recipient accepts that combination before authorization. A mismatch may not be interchangeable with the requested payment, and the general technical flow does not establish whether a particular service can recover, credit, or refund an incorrect or incomplete payment.

Reconciliation links transaction information to the merchant’s order records. The service may report a status, while the merchant decides how that status changes an order. Teams should clarify how they treat a payment that is partial, late, or otherwise inconsistent with the request, because the available evidence does not establish a universal exception policy. Similarly, do not assume that refunds follow the same path as the original payment; verify the actual arrangement.

Security, recovery, and regulatory responsibilities depend on the service and applicable circumstances. This article does not identify a jurisdiction or provider, so it draws no licensing, compliance, or tax conclusions. Those matters cannot be determined from a generic description of transaction flow.

## What a gateway does not establish by itself

A gateway label does not guarantee that a payment is final, anonymous, price-stable, or converted at a particular rate. It does not by itself show who controls funds, what settlement conditions apply, or whether a refund is available. Those matters depend on the network, service design, and terms of the particular arrangement; they should not be inferred from a checkout screen or a transaction notification.

Nor does the technology description establish legal status, tax treatment, licensing, or compliance. Those questions are outside a jurisdiction-neutral account of payment mechanics. The useful mental model is to trace the sequence: checkout request, wallet authorization, network processing, service monitoring, and the merchant’s settlement decision. Treat custody, conversion, refunds, timing, and legal responsibilities as separate questions requiring evidence specific to the actual arrangement.

## Sources and references

- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-18.
- [Invoices](https://docs.btcpayserver.org/Users/invoices/) — BTCPay Server; retrieved 2026-10-19.
- [P2P Network — Bitcoin Developer Guide](https://developer.bitcoin.org/devguide/p2p_network.html) — Bitcoin.org developer documentation; retrieved 2026-10-18.
