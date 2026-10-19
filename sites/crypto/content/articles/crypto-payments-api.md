---
title: "Crypto Payments API: Capabilities, Events, and Reconciliation"
description: "Evaluate a crypto payments API across quotes, invoices, addresses, payment states, webhooks, settlement, refunds, reconciliation, security, and testing."
date: "2026-10-19"
draft: false
content_type: "explainer"
topics: ["payments-infrastructure"]
tags: ["crypto payment api", "cryptocurrency payments API", "stablecoin payment API", "crypto invoice API", "crypto payment webhooks"]
author: "editorial_team"
primary_keyword: "crypto payments api"
owned_question: "What capabilities should a crypto payments API provide from quote and address creation through settlement and reconciliation?"
risk_level: "medium"
---

A **crypto payments API** connects a merchant's order system to blockchain payment infrastructure. A useful API does more than generate an address. It must preserve the relationship among the customer-facing amount, payment destination, blockchain transaction, provider state, settlement movement, refund, and merchant ledger entry.

The required surface depends on the operating model. A hosted processor may control addresses, custody, conversion, and settlement. A self-hosted stack may expose invoices and wallet events while leaving treasury and accounting to the merchant. The right evaluation question is therefore not how many endpoints exist, but whether the API exposes every state and control the merchant must operate.

Before comparing products, map the broader operating checklist in [how to accept crypto payments](/articles/how-to-accept-crypto-payments/). The sections below translate that checklist into API capabilities.

## A payments API is a lifecycle, not one endpoint

A payment object should connect four records:

1. the merchant order and amount owed;
2. the asset, network, destination, memo or tag, and expiry shown to the payer;
3. the observed blockchain transaction and its confirmation state; and
4. the settlement, conversion, fee, refund, or payout entries used by operations and accounting.

Some APIs split these records across quotes, payment intents, invoices, deposit destinations, transfers, and balance resources. Others combine them. For example, Coinbase currently documents authorization, capture, charge, void, refund, webhook, and delivery-monitoring resources in its Payment Acceptance API. Its separate business API documents deposit destinations and a quoted transfer flow. BTCPay Server's Greenfield examples create an invoice from an amount, currency, and merchant order ID and return an invoice ID plus checkout link. These are examples of different product models, not a ranking or a universal schema.

## Asset, network, and quote discovery

An integration needs a machine-readable catalog of supported asset-and-network pairs. A ticker alone is unsafe because the same asset can exist on multiple networks. The catalog should identify network names and IDs, contract addresses where relevant, decimal precision, minimums, destination requirements, confirmation policy, maintenance state, and geographic or account restrictions.

If the customer pays one asset while the merchant prices or settles in another, the API should create an explicit quote. The response should identify the input and output assets, rate, provider fees, network-fee treatment, amount due, expiry, and what happens after expiry. The merchant should know whether the quote is firm, indicative, or recalculated when funds arrive.

Do not cache availability or pricing indefinitely. The integration needs a defined refresh policy and an error path when an asset, network, or quote becomes unavailable between checkout and payment.

## Payment, invoice, and destination creation

Creating a payment should require a merchant-generated correlation key, usually an order or payment ID. The API should support idempotency so retrying a timed-out request does not create multiple active destinations or charges. The response should return a provider ID, exact amount, asset and network, address, memo or tag, expiry, checkout data, and initial state.

The contract must define behavior for:

- underpayments, overpayments, and multiple transactions;
- payments received after expiry;
- an asset sent on the wrong network;
- reusable versus single-use destinations;
- address or memo validation; and
- cancellation before funds arrive.

BTCPay Server documents an `orderId` metadata field that links an invoice to an external order and appears in search and reporting. It also cautions against putting unnecessary personal data in metadata. That is a sound category-level principle: store the minimum identifier needed for reconciliation, not a duplicate customer profile.

## Payment states and blockchain finality

A binary paid flag is not enough. The API should publish a documented state machine that distinguishes at least created, awaiting payment, observed, confirming, confirmed, completed or settled, expired, failed, and refunded states where the model supports them. State names matter less than their definitions and allowed transitions.

The merchant needs to know when a transaction is first observed, how much was received, which transaction hash and output or log carries the payment, and when the platform considers it sufficiently final. A blockchain confirmation is not necessarily the same as provider settlement. The provider may wait for additional confirmations, run screening, convert assets, or move funds internally before making the balance available.

The API should explain reorganization handling, replaced transactions, duplicate deposits, and later reversals in provider records. Review [how a cryptocurrency transaction is verified](/articles/how-a-cryptocurrency-transaction-is-verified/) for the network layer behind these states.

## Webhooks, polling, and event recovery

Webhooks reduce latency, but they are a notification channel rather than the sole source of truth. Production integrations should verify signatures, store the provider event ID and receipt time, process events idempotently, tolerate duplicates and out-of-order delivery, and fetch the current payment object before fulfilling an irreversible order.

Signature rules are provider-specific. BTCPay Server, for example, documents computing HMAC-SHA256 over the exact request bytes and comparing the result with its signature header before acting on the parsed event. Re-serializing parsed JSON can change the byte sequence, which is why an integration must preserve the raw body when the provider's scheme requires it.

A complete API also supplies event history or redelivery information. Coinbase's Payment Acceptance overview lists webhook-event queries and delivery monitoring. Regardless of provider, the merchant needs a recovery job that polls unresolved payments and backfills events after downtime. If webhooks stop for an hour, accounting and fulfillment must converge after service resumes.

## Settlement, conversion, refunds, and payouts

Receipt and settlement should be separate objects or clearly separated states. The API should state whether the merchant receives the paid asset, a converted stablecoin, fiat balance, or another settlement asset; who takes custody; when conversion occurs; and how gross amount, rate, spread, network fees, service fees, and net proceeds are reported.

Refunds are new transfers, not reversals of the original blockchain transaction. The interface should require an approved destination, asset, network, amount, reason, and idempotency key, then expose approval, broadcast, confirmation, failure, and fee data. Reusing the original sending address without validation can be unsafe because it may belong to an exchange or intermediary rather than the payer.

If the platform supports payouts or treasury transfers, those operations need their own authorization policy and state machine. Coinbase's business API, for example, separates creating a transfer from executing a quoted transfer. The exact design varies, but a buyer should reject any model in which a read credential can silently become a money-movement credential.

## Reconciliation and financial reporting

Operations must be able to reconstruct each payment without reading a dashboard. A payment or settlement export should include:

- merchant order ID and provider payment ID;
- requested, received, refunded, and settled amounts;
- asset, network, address, memo, and transaction identifier;
- quote and conversion references;
- provider and network fees, with currency;
- event, confirmation, settlement, and refund timestamps; and
- current state plus an immutable event history or audit trail.

List endpoints need stable pagination, deterministic filters, and documented time semantics. Financial values should use decimal strings or documented integer base units rather than binary floating point. The API should expose corrections as new records or traceable state changes instead of rewriting history without an audit event.

Test reconciliation with underpayments, overpayments, late deposits, duplicate webhooks, provider downtime, refunds, and a settlement that spans two reporting periods. A happy-path checkout demo does not test whether the books can close.

## Security, access, and production readiness

Credentials should be scoped by environment, merchant account, operation, and where possible asset or wallet. BTCPay Server's authorization model allows operation permissions and store scoping and recommends the narrowest useful permissions. Hosted providers may use different mechanisms, but the acceptance criterion is the same: creating an invoice, reading a payment, issuing a refund, and moving treasury funds should not automatically require one unrestricted credential.

A production review should also check:

- separate test and live credentials, endpoints, and webhook secrets;
- key rotation without downtime and a documented revocation path;
- request idempotency and retry guidance;
- rate-limit headers, bounded retries, and stable error codes;
- API versioning, deprecation notice, and changelog practices;
- status reporting, incident communication, and event replay;
- sandbox fidelity for confirmations, expiries, and failures; and
- export and migration paths if the integration is replaced.

A strong crypto payments API makes money movement observable and recoverable. It gives product teams a checkout flow, engineers a precise state machine, security teams narrow permissions, operations a recovery path, and finance a complete trail from order to settlement. Missing any one of those layers turns an apparently simple address endpoint into manual operational risk.

## Sources and references

- [Payment Acceptance API](https://docs.cdp.coinbase.com/api-reference/payment-acceptance/overview) — Coinbase Developer Platform; retrieved 2026-10-19.
- [Business Onboarding](https://docs.cdp.coinbase.com/api-reference/v2/business-onboarding) — Coinbase Developer Platform; retrieved 2026-10-19.
- [Greenfield API Examples](https://docs.btcpayserver.org/Development/GreenFieldExample-NodeJS/) — BTCPay Server; retrieved 2026-10-19.
- [API Authentication and Authorization](https://docs.btcpayserver.org/BTCPayServer/greenfield-authorization/) — BTCPay Server; retrieved 2026-10-19.
- [Invoice Metadata](https://docs.btcpayserver.org/Developers/api/invoice-metadata/) — BTCPay Server; retrieved 2026-10-19.
