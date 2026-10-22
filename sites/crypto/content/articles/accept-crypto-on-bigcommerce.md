---
title: "How to accept crypto on BigCommerce: setup and checks"
description: "Learn how to accept crypto on BigCommerce by checking integration prerequisites, configuring checkout settings, testing payment flows, and planning operations."
date: "2026-10-22"
draft: false
content_type: "guide"
topics: ["crypto_payments"]
tags: []
author: "editorial_team"
primary_keyword: "accept crypto on bigcommerce"
owned_question: "What should a BigCommerce store operator verify before choosing and configuring a cryptocurrency payment integration, and how should the setup be tested?"
risk_level: "medium"
---

Before choosing or configuring a cryptocurrency payment integration for a BigCommerce store, verify current platform compatibility and setup requirements, then confirm the provider’s supported assets, networks, payment statuses, settlement and refund procedures, fees, security controls, and account recovery terms. The evidence available for this guide does not establish which integrations BigCommerce currently supports or how a specific one connects, so use current BigCommerce and provider documentation for those details.

## What a BigCommerce crypto integration needs to support

Begin with the store itself. Check BigCommerce’s current documentation for the store plan, checkout configuration, and integration methods relevant to your account. Confirm whether any prerequisites or compatibility limits apply before creating a provider account or changing checkout settings. The evidence here does not verify the current BigCommerce integration catalog, available plans, installation steps, or supported checkout methods. Do not treat a service’s general API or app listing as proof that it is compatible with your store.

Then review the payment integration’s documentation for the assets and networks it supports. Payment instructions are not interchangeable across all assets and networks: compatibility can depend on the requested asset, network, destination, recipient requirements, and service. Before authorization, compare the exact asset and network with the provider’s instructions and the recipient requirements relevant to the payment flow. Confirm whether the provider supports the exact combination your store intends to offer, rather than relying on a shared token name or symbol.

Identify which payment states the integration reports and what each means for the store. One documented e-commerce integration pattern handles states such as processing, settled, expired, invalid, partial, overpaid, and late, and calls for validating webhook signatures before updating an order. That is an implementation example, not a universal status vocabulary or proof that a BigCommerce integration supports those states. Ask the provider for its exact status definitions and how its integration authenticates notifications, handles duplicate or out-of-order events, and surfaces exceptions. ([source](<https://docs.btcpayserver.org/Development/ecommerce-integration-guide/>))

Also determine which system supplies the payment record and which system changes the store order. BigCommerce may present an order status while a provider maintains its own payment records. The integration instructions should explain how those records are linked, how an order is updated, and what staff should do if the records disagree. Avoid treating a storefront label as proof of settlement unless the documented workflow defines it that way.

## Choose an integration approach without assuming provider fit

Evaluate documented compatibility against your checkout, order review, and fulfillment workflows. Verify whether setup requires an app, an external account, API credentials, or changes to staff procedures. These are questions to resolve with current platform and provider documentation; the available evidence does not establish which requirements apply to a particular BigCommerce integration.

Next, trace the flow of order and payment information. Find out which system stores or displays each record, which staff roles can access it, and where exceptions and refund requests are managed. Ask for the provider’s written terms on supported assets and networks, settlement arrangements, fees, refund handling, account protection, support contacts, and service availability. Those details are specific to the provider and the store’s configuration; this guide cannot supply a universal answer.

When reviewing a provider’s API, separate documented capability from store compatibility. For example, one provider’s documented Payment Acceptance API includes resources for authorization, capture, charges, voids, refunds, webhook configuration, event queries, and delivery monitoring. This example shows the kinds of operations an API may expose; it does not show that BigCommerce uses that API, that it is available to a particular store, or that another provider offers the same operations. Confirm product access, asset and network support, and geographic availability directly with the current documentation. ([source](<https://docs.cdp.coinbase.com/api-reference/payment-acceptance/overview>))

Keep trading-venue records distinct from payment records. A centralized crypto exchange commonly maintains off-chain records of outstanding buy and sell orders in a limit order book. That describes an exchange’s trading system, not a merchant checkout or evidence that a customer payment has settled. If an integration uses an exchange or other service in its payment flow, ask which records are relevant to your store’s order and settlement process. ([source](<https://www.bis.org/publications/aer-2022/future-monetary-system>))

## Configure and test accept crypto on BigCommerce

Follow the current platform and integration instructions for installation and configuration. Before adding credentials, identify what permissions are requested, where the credentials will be stored, who can access them, and how they can be revoked. The available evidence does not establish credential permissions or security controls for any particular BigCommerce integration. Do not infer that an app or provider is secure simply because it is listed in a catalog or describes itself in promotional terms.

Before enabling checkout, write down the intended order workflow. For every status the provider documents, specify whether the order remains pending, becomes eligible for fulfillment, needs staff review, or is canceled. Identify who makes that decision and who can resolve a mismatch between the store record and provider record. The e-commerce example cited above includes multiple payment states and signature validation; confirm the exact state handling and notification protections for the integration you actually use rather than importing that example as a universal rule. ([source](<https://docs.btcpayserver.org/Development/ecommerce-integration-guide/>))

Use only a provider-supported test mode or another clearly documented non-production method. Read the documentation to learn what that mode simulates, which order updates it triggers, and whether it supports testing refunds and exceptions. The available evidence does not establish the test behavior of any BigCommerce crypto integration. A non-production test should therefore be recorded as evidence of the behavior it actually demonstrates, not as proof of live-network settlement, production security, or real refund processing.

Build a test checklist from documented capabilities. Where the integration supports the relevant cases, check:

- A normal payment and the resulting store order update.
- A pending payment and the rule that prevents fulfillment before the store’s documented condition is met.
- Expired, invalid, partial, overpaid, or late payment states, including what the staff member should do next.
- A refund request, the provider’s recorded result, and any corresponding change to the store order.
- A delayed, duplicated, or missing notification, along with the documented way to verify and reconcile the payment status.

These are scenarios to investigate, not assertions that a particular integration supports or passes them. For each test, note the expected behavior from current documentation, the observed non-production result, and any discrepancy that needs clarification before launch. If a capability is not documented or cannot be tested in the available mode, record that limitation rather than assuming the live behavior.

## Plan order handling, refunds, and reconciliation

Set a written fulfillment rule that identifies the payment status required before staff release an order. Specify who checks the status, what happens when records conflict, and how exceptions are escalated. A transaction being broadcast is not, by itself, sufficient reason to fulfill an order; a merchant-payment guide says the merchant’s configured settlement conditions should be met. Use the integration’s own documented policy to determine the equivalent decision for your checkout.

Confirm the refund path and limitations before offering the payment option to customers. Ask whether the provider records a refund as a separate operation, whether the integration updates the BigCommerce order, and which cases require manual review. A provider API example documents refund resources, but that alone does not establish the behavior or availability of refunds through a BigCommerce integration. The specific provider and platform documentation must explain the steps and exceptions for the setup you choose. ([source](<https://docs.cdp.coinbase.com/api-reference/payment-acceptance/overview>))

Define a regular reconciliation handoff. Decide who compares store orders with provider payment records, how mismatches and exceptions are recorded, and how fees and settlement entries are represented in the store’s accounting workflow. Identify which reports or records staff will use and who can access them. Do not assume that a store order, provider dashboard, or transaction reference by itself provides a complete accounting record; confirm how the systems represent the parts of the transaction that your workflow needs.

Create a concise staff procedure for common cases: checking a payment status, holding an order for review, escalating a mismatch, documenting a refund, and recording a reconciliation exception. Assign a role to each action and identify where the applicable provider instructions are kept. Keep the procedure aligned with the statuses and capabilities the integration actually documents, rather than copying generic labels into a workflow that may use different ones.

## Verify legal, tax, security, and recovery obligations

Legal, tax, and regulatory obligations for crypto payments depend on the user’s jurisdiction and circumstances; general Bitcoin guidance does not support a jurisdiction-specific conclusion. Consult applicable local authorities or a qualified professional for the relevant situation. This guide does not determine which rules apply to a particular BigCommerce store.

Ask BigCommerce and the provider for documented security controls, account protections, incident contacts, and procedures for removing access when staff roles change. Confirm how store and provider accounts can be recovered, and how any integration credentials are replaced or revoked. The evidence available here does not establish a recovery guarantee or the security of a specific integration, so rely on current service documentation and direct provider explanations.

Before launch, hand off the operating details to the people responsible for the store: where to find payment records, what status is required for fulfillment, how to handle exceptions, how refunds are initiated, who reconciles records, and whom to contact during an incident. Recheck platform and provider documentation before making material changes. Because the evidence here does not establish BigCommerce’s current integration support, provider availability, or the behavior of any specific integration, those details must be verified for the store and configuration in question.

## Sources and references

- [Payment Acceptance API](https://docs.cdp.coinbase.com/api-reference/payment-acceptance/overview) — Coinbase Developer Platform; retrieved 2026-10-19.
- [eCommerce Integration Guide](https://docs.btcpayserver.org/Development/ecommerce-integration-guide/) — BTCPay Server; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
