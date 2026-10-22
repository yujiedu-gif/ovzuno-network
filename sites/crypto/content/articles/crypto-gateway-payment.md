---
title: "Crypto gateway payment: how the payment flow works"
description: "Learn what a crypto gateway payment does, how a transaction moves from checkout to confirmation and settlement, and which operational details require verification."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["crypto_payments"]
tags: []
author: "editorial_team"
primary_keyword: "crypto gateway payment"
owned_question: "What is a crypto payment gateway, and how does it handle a payment from checkout through confirmation and settlement?"
risk_level: "medium"
---

A crypto payment gateway coordinates a customer’s cryptocurrency payment with a merchant’s checkout and payment-status workflow. A typical flow moves from a payment request to wallet authorization, network submission, confirmation under a service policy, and possibly a separate settlement step. The exact functions, status meanings, and settlement arrangements depend on the service; confirmation alone does not establish that funds were converted to fiat or delivered to a bank account.

## What a crypto payment gateway does

A gateway’s basic role is to connect a merchant’s payment request with the information needed to recognize a customer’s crypto transaction. Depending on its documented design, it may present payment instructions and communicate payment-status updates. That coordination role should not be confused with every other function in the transaction.

The customer’s wallet is where the customer authorizes a transfer. The blockchain network handles the transaction under its own rules. The merchant decides how its order workflow responds to a reported payment state. A separate settlement service may be involved after the transaction is recognized, but not every gateway combines these roles. Terms such as “gateway,” “processor,” and “payment service” therefore should not be assumed to describe identical functions across products.

The label “gateway” also does not establish which assets or networks a service supports, where it operates, what it charges, or how it handles settlement. Those are service-specific details that need to be checked directly in current documentation. The term alone is not evidence that a particular payment route is available.

## How a crypto gateway payment moves from checkout to confirmation

**1. Checkout creates or presents a payment request.** A customer starts with an order and a payment request. A service may display an amount and instructions specifying an asset, network, or destination. The exact information displayed, how it is generated, and how long it remains valid depend on the service. The request is not proof that the customer has sent funds.

Before authorizing a payment, the customer should compare the requested asset and network with the recipient’s instructions. Payment instructions are not interchangeable across all assets and networks; compatibility and acceptance depend on the request, destination, recipient requirements, and service. If those details are unclear, the customer should verify them with the recipient or service before proceeding.

**2. The customer authorizes a transfer in a wallet.** The wallet presents the transaction for the customer to review and authorize. For example, an Ethereum transaction can include a sender-authorizing signature, a nonce, a destination, value or contract data, a gas limit, and fee parameters according to its transaction type. That example describes Ethereum’s transaction model, not a universal format for every crypto network.

The wallet’s authorization is distinct from the gateway’s coordination role. A gateway may supply instructions or payment information, but the customer authorizes the transfer. The transaction details the wallet presents should be checked against the request before approval.

**3. The transaction is broadcast to a network.** Once authorized, a transaction can be submitted to the relevant network. For Ethereum, a transaction proceeds through network validation, execution where applicable, commitment, and propagation. A submission or broadcast is an early lifecycle event, not the same as a payment meeting the merchant’s confirmation policy.

A service may observe a submitted transaction and report that it has been detected. Detection means the service has observed relevant activity; it does not itself establish that the transaction has met a network or service confirmation threshold. The evidence here does not establish a universal threshold or waiting time. Both depend on the relevant network and the service’s documented policy.

**4. The gateway or another service reports status.** The service may communicate transaction activity or a status change to the merchant’s order workflow. That notification is information for the merchant, not automatically a decision to fulfill the order. A transaction being broadcast should not, by itself, trigger fulfillment; the merchant’s configured settlement conditions must be met.

The merchant should understand what each status means and what action follows it. A service might distinguish a request, detected transaction, confirmation, or settlement, or use different labels. Without service documentation, the status wording does not reveal the precise network condition, decision rule, or operational consequence.

**5. The merchant applies its order policy.** The merchant decides when its own workflow treats a payment as sufficient for an order action. That decision is separate from the customer’s authorization and from the network’s transaction processing. For a business, it matters whether a notification represents an observed transaction, a condition required by the service, or the merchant’s own order state. The names of these events are not universal standards.

**6. Any separate settlement takes place.** A service may have a settlement step after payment activity is recognized. The term can refer to different operational events, so it does not by itself establish that crypto has been converted to fiat, that funds have reached a bank account, or when either event occurs. The service documentation and the arrangement between the parties must define what “settled” means in that context.

## What payment status and settlement do—and do not—mean

It is useful to treat payment labels as stages in a workflow rather than interchangeable proof of a completed business outcome. A request can exist before a transfer is authorized. A transaction can be observed before it meets a confirmation policy. A service can report a network-related state while a separate settlement step remains outstanding. Services may combine stages or use different names, so interpret each status using the service’s own documentation.

A blockchain confirmation is not the same thing as fiat conversion, bank delivery, or merchant fulfillment. Those are separate events or decisions. In particular, a broadcast transaction alone should not be treated as sufficient to fulfill an order; the merchant’s configured settlement conditions govern that operational decision.

When reviewing a status description, identify the event it represents, the condition that must be met, and the action that follows. Check whether “settled” means the merchant considers the order paid, the service records a transaction as complete, or a separate funds transfer has occurred. Do not infer one meaning from another or treat a status label as a guarantee of a particular destination or timing.

## Operational details to verify before relying on a gateway

A general description cannot establish a service’s current capabilities. Check its current documentation for supported assets and networks, relevant availability, fees, confirmation policy, and settlement destination and timing. These details vary by service and arrangement. The term “crypto payment gateway” does not supply the missing specifics, and no particular capability should be assumed from the category name.

Also establish which party performs each task. Documentation should clarify who provides payment instructions, observes transactions, reports status, controls any keys, holds or moves funds, and responds to operational problems. Security controls, key-management responsibilities, incident procedures, and recovery or refund processes require service-specific evidence. Do not assume that an erroneous or incomplete transfer can be reversed or recovered, or that it has a standard remedy, unless the responsible party documents one.

Finally, determine which parties handle transaction monitoring, customer identification, sanctions screening, and recordkeeping, and verify what applies to the specific business and jurisdiction. This general explanation does not determine legal, tax, or compliance obligations. Those questions require current, qualified, jurisdiction-specific review.

The practical model is a sequence of distinct responsibilities: checkout presents a request, a wallet authorizes a transfer, a network processes it, a service may report status, and the merchant applies its order policy. Any subsequent settlement is a separate matter to define and verify. Keeping those stages separate helps a business understand what a gateway’s status information does—and does not—establish.

## Sources and references

- [Technical intro to Ethereum](https://ethereum.org/developers/docs/intro-to-ethereum/) — ethereum.org; retrieved 2026-10-19.
- [Transactions](https://ethereum.org/developers/docs/transactions/) — ethereum.org; retrieved 2026-10-18.
- [Invoices](https://docs.btcpayserver.org/Users/invoices/) — BTCPay Server; retrieved 2026-10-19.
