---
title: "How to Accept Crypto Payments on Your Website: Integration Guide"
description: "A vendor-neutral guide to crypto checkout integration, from payment intents and callbacks to confirmations, expirations, refunds, and reconciliation."
date: "2026-10-19"
draft: false
content_type: "guide"
topics: ["crypto_payments"]
tags: ["crypto payment integration", "crypto payments API", "crypto checkout", "crypto payment intent", "crypto payment confirmation", "crypto payment refunds", "crypto payment reconciliation"]
author: "editorial_team"
primary_keyword: "how to accept crypto payments on my website"
owned_question: "How should a website integrate crypto checkout, callbacks, confirmation handling, refunds, and reconciliation?"
risk_level: "high"
---

# How to Accept Crypto Payments on Your Website

A website crypto-payment integration connects an order system to a payment request, asynchronous status updates, a rule for deciding when an order is fulfilled, and records for refunds and reconciliation. It is not just a checkout button. Keep the merchant’s order state distinct from the payment’s status: an on-chain observation or processor event provides evidence about a payment attempt, but does not automatically instruct the business to fulfill an order.

The details depend on the selected processor, wallet infrastructure, supported network, and business risk. The lifecycle below is a vendor-neutral design framework. Treat provider-specific behavior as something to verify against current documentation, not as a universal feature.

## Map the payment flow before writing integration code

Start by drawing the components that participate in a checkout: the customer-facing website, merchant backend, payment processor or wallet infrastructure, blockchain data source, and accounting system. For each component, record what information it receives, what it is allowed to change, and what evidence it supplies. For example, the website can display payment instructions, while the backend can associate a payment request with an order and decide whether the merchant’s fulfillment criteria are met.

Define two related but separate state models:

- **Order state:** the merchant’s status for the sale, such as awaiting payment, ready for fulfillment, fulfilled, canceled, or under review.
- **Payment state:** the status of a particular payment attempt, as reported or observed through the selected service and network.

One order can have more than one payment attempt, and a payment attempt can generate multiple events. Preserve that distinction in data structures and logs. A processor event should update the payment record only after validation; a separate business rule should determine whether the order changes state. This prevents an unverified notification, duplicate delivery, or incomplete transfer from becoming an automatic fulfillment instruction.

Assign responsibility explicitly. Decide which system creates the payment request, monitors it, authenticates notifications, applies confirmation rules, handles exceptions, approves refunds, and prepares reconciliation data. The division of work depends on the actual architecture and service capabilities. Confirm those capabilities in documentation and test them in the environment you intend to use.

## Create an order and payment intent

Create a stable internal order identifier when the merchant accepts the checkout request. Create a separate payment-intent or invoice identifier for each payment attempt, and store the relationship between the identifiers. The order ID identifies the merchant transaction; the intent ID identifies the payment request. Keeping them separate makes it possible to investigate retries or multiple attempts without confusing payment records with the underlying sale.

Before presenting instructions, persist the requested amount and asset, network, expiry policy, and any pricing or conversion assumptions. The exact fields, supported assets, and meanings depend on the payment system. Record the basis for any amount or conversion value you show, and verify its validity period and fee treatment with the service documentation rather than assuming those details.

Make intent creation idempotent. A browser refresh, timed-out request, or worker retry should not unintentionally create a second merchant order or a duplicate payment request. Define what counts as the same creation request, store its result, and return or recover the existing intent when that request is retried. If the system cannot safely determine whether a timed-out creation succeeded, route the case to a controlled lookup or exception process instead of blindly issuing another request.

A scoped example illustrates why the details must be checked. BTCPay Server’s documented Greenfield invoice examples accept an amount, currency, and merchant metadata such as an order ID, and return an invoice ID and checkout link. Exact request and response models depend on the deployed BTCPay Server version and enabled plugins. BTCPay Server’s invoice metadata documentation describes an external merchant order ID that can be used in search, reports, receipts, and invoice correlation, and cautions against sending unnecessary customer data. These documented behaviors are specific to that system; they do not establish that another API has the same fields or semantics.

Before building around any provider’s intent or invoice behavior, verify the currently documented request and response models, identifier persistence, supported assets and networks, quote validity, conversion assumptions, fee treatment, and expiry semantics. If a detail is not documented or is ambiguous, avoid using it as an order-state guarantee.

## Generate and display an invoice or payment address

Address assignment and invoice construction depend on the chosen architecture and supported networks. Display the asset, network, requested amount, payment address or URI, expiry, and any required memo or tag in a way that lets the customer distinguish each value. A correct amount paired with the wrong network or missing destination information can still create a payment mismatch, so do not reduce the displayed instructions to an address alone.

Do not claim that an address is unique, safe to reuse, or reusable unless the actual system design and its documentation support that claim. Establish how the checkout will handle a customer mistake, a repeated payment, or a transfer that arrives after the displayed time window. State what customers should do when payment details no longer match the active request, and provide a support path for cases the integration cannot automatically match.

Keep the meaning of checkout expiry narrow. Expiry can describe whether a payment request is still active under a particular service’s rules. It does not by itself establish transaction finality, prevent a later transfer from being observed, or show that funds can be recovered. Verify what the actual service monitors after expiry and how late funds are represented before mapping that behavior to a merchant order state.

## Process callbacks defensively

Treat an asynchronous callback as untrusted input until it passes the authentication mechanism documented for the API. Protect secrets, restrict access to them, and ensure the verification code uses the precise input required by the API. Only after authentication should the backend parse and act on the event.

For the documented BTCPay webhook example, verification requires computing HMAC-SHA256 over the exact request bytes and comparing the result with the signature header before acting on the parsed event. Other APIs may use different algorithms, headers, replay windows, or key-rotation schemes. Do not copy the BTCPay example as a generic webhook recipe; confirm the actual API’s verification process, including how it expects the signing secret to be handled.

After authentication, validate the event against the stored payment intent. Check the intent or invoice identifier, merchant order association, asset, network, amount, and event type as applicable to the documented payload. Reject or quarantine events that do not match the stored request rather than updating an order based on a plausible-looking but inconsistent notification.

Make event handling idempotent. Keep a record that lets the backend recognize that a notification or event has already been processed, and make repeated processing produce no unintended second action. Design for delayed and out-of-order events: a later-arriving message should not blindly overwrite a more advanced or otherwise inconsistent state. Define permitted transitions and route events that do not fit them to review.

Retain the event and processing outcome needed for audit and troubleshooting, subject to the business’s data-handling rules. If a documented server-side status lookup or independent chain data is available and appropriate, use it as an additional verification step for relevant decisions. Confirm what that lookup actually establishes and how current it is; do not assume that a callback, lookup, or external data source provides guarantees beyond its documentation.

## Define confirmation and order-fulfillment rules

Create payment states that match the selected service and network, such as pending, detected, confirming, confirmed, failed, and exception. Define each state using the provider’s documented meaning and the evidence available to your system. A label such as “confirmed” should not be treated as a universal definition of finality across different services or networks.

Then specify the merchant’s fulfillment rule separately. Identify the evidence and business conditions that must be true before the order can move to fulfillment. Select confirmation and fulfillment thresholds based on evidence relevant to the asset, network, transaction value, and business risk. There is no universal confirmation count or settlement-time rule that applies to every integration, and a guide cannot establish the correct threshold for an unexamined network or business.

Document how the state machine responds to reorganizations, delayed or missing notifications, partial payments, excess payments, and transfers sent on the wrong network. For each case, specify whether the system can identify it automatically, whether it should hold the order, and who reviews it. Verify the provider’s status definitions and monitoring limits before mapping them to merchant order states. If the integration cannot establish whether a payment qualifies, keep the order in an exception state rather than treating uncertainty as confirmation.

## Handle expiry, late payments, and exceptions

Define what expiry means for the checkout in the actual system. Ask whether an expired request remains monitored, whether a late transfer can be associated with its original intent, and what status or record is returned. Document the answer and its limits. Do not infer from a checkout countdown that a later transfer is impossible or that an earlier one is final.

Provide an exception route for partial, excess, duplicate, late, or mismatched payments. The operational record should connect the observed event or transaction identifier to the relevant order and payment attempt when the available evidence allows it. A reviewer should be able to see why the case was held, what evidence is missing, and what action is permitted. Avoid promising that every exception can be automatically matched, credited, or recovered; those outcomes depend on the payment arrangement and documented capabilities.

## Design a separate refund workflow

An outbound refund is a separate payment operation, not an automatic reversal of an on-chain transfer. Retain the original payment reference, but use an authenticated process to obtain refund details. Establish approval steps and verify the destination address, asset, network, amount calculation, and any required memo or tag before sending. Record who requested and approved the refund and what information was reviewed, using controls appropriate to the actual architecture.

BTCPay Server’s pull-payment refund model provides one bounded example: the recipient can provide a payout destination through a claim rather than having the merchant reuse the original payment address. The merchant still reviews the amount, rate, network fee, and destination before signing or sending. This is a specific documented model, not a general rule for other payment arrangements.

Ask what the refund amount represents and how any rate or fee is determined before approving it. Refund timing, fees, exchange-rate treatment, and available recovery paths depend on the payment arrangement and require supporting evidence. Do not promise that a refund is reversible or that funds can be recovered if destination details are wrong. Keep the refund record linked to the original payment and order, but distinguish its pending, approved, sent, or otherwise documented status from the status of the original inbound payment.

## Reconcile payments with orders and accounting records

Reconciliation should connect payment intents, callback events, transaction identifiers, merchant orders, refunds, and settlement records. Preserve the identifiers needed to trace each relationship, including the order-to-intent association and the reference to the original payment for a refund. Record timestamps, asset and network, received amount, fees where documented, conversion basis where applicable, and exception status. Do not fill missing fee or conversion fields with assumptions.

Define a regular exception review. Look for records that are missing, duplicated, mismatched, or left in an unresolved state, and assign a procedure for investigation and correction. Reconciliation should make it possible to distinguish a notification-processing problem from a payment mismatch or a bookkeeping question. Keep an audit trail of corrections so an internal record can be traced back to the evidence and action that changed it.

Integration records can support operational review, but they do not determine accounting treatment. Bookkeeping, valuation, tax reporting, and recordkeeping obligations are jurisdiction- and business-specific questions. Obtain current, qualified evidence for those decisions rather than treating this technical guide or a processor status as accounting advice.

## Test failure cases before enabling checkout

Use the actual test environment and architecture to verify behavior where supported. A pre-launch checklist can include:

- Repeated callbacks, delayed notifications, out-of-order events, and invalid signatures.
- Retried intent creation, duplicate requests, and recovery after a timed-out creation attempt.
- Expired requests, late transfers, underpayments, overpayments, duplicate payments, and wrong-network transfers where the test environment supports them.
- Idempotent event processing, permitted state transitions, order holds, logs, alerts, and reconciliation outputs.
- Refund request authentication, approval, destination verification, and linkage to the original payment.
- Secret handling, access controls, data retention, incident response, and recovery procedures appropriate to the actual architecture.

For each test, record the expected behavior, observed result, and any remaining limitation. Confirm that a failed or ambiguous test leaves the order in a safe, reviewable state rather than silently fulfilling it. A checklist is not evidence that tests have passed: do not describe testing as complete unless results are documented for the system being deployed. Before enabling checkout, review the unresolved cases and verify provider-specific behavior against current documentation.

The core implementation control is separation: keep order state distinct from payment state, authenticate and validate asynchronous events, and make fulfillment and refunds explicit business workflows. The exact thresholds, API behavior, recovery options, accounting treatment, and operational limits must be established for the selected system and the business using it.

## Sources and references

- [Greenfield API Examples](https://docs.btcpayserver.org/Development/GreenFieldExample-NodeJS/) — BTCPay Server; retrieved 2026-10-19.
- [Invoice Metadata](https://docs.btcpayserver.org/Developers/api/invoice-metadata/) — BTCPay Server; retrieved 2026-10-19.
- [Pull Payments](https://docs.btcpayserver.org/Users/pull-payments/) — BTCPay Server; retrieved 2026-10-18.
