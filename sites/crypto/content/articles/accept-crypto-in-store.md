---
title: "Accept crypto in store: a point-of-sale workflow guide"
description: "Accept crypto in store with a practical point-of-sale workflow covering payment requests, status checks, staff procedures, exceptions, and reconciliation."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "guide"
topics: ["crypto_payments"]
tags: []
author: "editorial_team"
primary_keyword: "accept crypto in store"
owned_question: "How can a physical retail business design and operate an in-person crypto payment workflow, from presenting a payment request through status checks, exceptions, and recordkeeping?"
risk_level: "medium"
---

A physical retail business can accept crypto only with a defined checkout procedure: present a request tied to the sale, have staff check the designated payment status, set a rule for when goods may be released, and record the outcome. The available evidence does not establish a universal point-of-sale terminal workflow, supported assets, fees, settlement times, or recovery process. Verify those details against current documentation for the particular service and setup before a pilot.

## Plan the in-store payment flow

Map the people and systems involved before choosing equipment or writing staff instructions. Identify who creates the request, what the customer scans or enters, which system reports status, who decides whether the sale can proceed, and where the result is recorded. A checkout may involve a cashier, point-of-sale device, customer wallet, payment service, and sales record, but the specific arrangement must be confirmed for the system in use.

Treat the payment request as part of the sale record, not as a generic destination to reuse. The instructions should tell staff how to check that the request corresponds to the correct sale and displays the intended amount, asset, network, and destination. These details are not interchangeable across all assets and networks: before authorizing a payment, compare the exact asset and network with the recipient’s instructions and verify compatibility with the recipient or service. That check is especially important when a token name alone does not establish which network or representation is involved.

Define which system or screen staff should use to interpret the request and its status. A customer’s wallet screen may show an attempted payment, but the store needs a documented source of status and an assigned role for decisions. Record the sale reference and the actions that staff should take when information is missing or inconsistent. Avoid informal handoffs that leave the next cashier guessing which screen, request, or instruction controls.

A useful design distinction is between a payment attempt and fulfillment. A transaction being broadcast is not, by itself, a reason to release goods; the merchant’s configured settlement conditions must be met. The appropriate conditions depend on the network, asset, amount, product, and risk tolerance, so do not copy a universal threshold from this guide. Obtain the selected system’s current status definitions and document the store’s release rule before serving customers.

## Set up and rehearse the store workflow

Write a short procedure that covers device access, staff permissions, connectivity, request creation, customer instructions, status checks, and escalation. Confirm the current documentation for the specific terminal, wallet, or service. The evidence available here does not establish which products are compatible with a particular store setup or whether any service is available in a given location.

Train staff to create a distinct payment request for each sale and follow the same checks each time. The procedure should say who may initiate a request, who may approve an exception, and who can access records. If two systems report different information, direct staff to pause and escalate to a named role rather than choose whichever status appears more favorable.

Rehearse the steps internally before offering the option to customers. Include a routine checkout, a request that remains pending, an amount mismatch, and an interruption to the device or connection. The purpose is to confirm that staff understand the instructions and know when to stop; a rehearsal does not prove how a live service will behave or establish its security.

Decide in advance what happens if a device, connection, wallet, or payment service is unavailable. The store may pause crypto checkout and use another payment method, but the business must choose its fallback and explain it to staff. No universal outage, recovery, or refund path is established here. Staff should not improvise by changing a destination or asking a customer to send again outside the written procedure.

## Verify crypto payment status at checkout

At the register, staff should compare the sale reference and requested payment details with what the designated system reports. The store’s procedure should specify what status is sufficient for release, who is authorized to interpret it, and what to do when the status is pending, unclear, or inconsistent. The evidence here does not define a universal confirmation threshold or settlement rule; document the chosen service’s current instructions and the business’s own release condition.

If the system shows that a transaction was broadcast, do not treat that alone as proof that the store’s settlement conditions have been met. A transaction may require further status checks under the merchant’s configured policy. Staff should wait or escalate according to that policy rather than promise immediate fulfillment based only on a customer’s submission screen.

The procedure should provide separate paths for common exceptions:

- **Delay:** Keep the sale pending under the store’s policy, record the request reference and status, and tell the customer who will review it and how the store will communicate an update.
- **Amount mismatch:** Pause fulfillment and route the case to the assigned supervisor. Record the requested amount and the status shown by the designated system; do not silently mark the sale as paid.
- **Wrong network or asset concern:** Stop and compare the actual payment information with the recipient’s instructions. Compatibility must be checked with the recipient or service; payment instructions are not interchangeable across all assets and networks.
- **Duplicate-payment report:** Record the customer’s report and the relevant request or transaction references, then escalate. Do not assume a duplicate can be reversed or recovered.

For every unresolved case, specify what information staff may collect, who reviews it, and what the customer is told. Do not promise that an incorrect transfer can be returned: the evidence here does not establish a universal recovery mechanism or guarantee.

## Record sales, exceptions, and refunds

Link the payment activity to the store’s own sale reference so the business can distinguish completed sales from pending requests and cases sent for review. Record the information necessary for internal follow-up, such as the sale reference, request details, status, relevant time, staff action, and any supervisor decision. The exact accounting treatment, valuation method, and retention period are not established here; use qualified accounting and local guidance rather than inferring a rule from a payment screen.

Assign a person or role to review exceptions and document corrections. Preserve enough context to explain what changed, who approved it, and why. The record should make it possible for an authorized reviewer to connect a receipt or sales entry with the related payment request and its status, without treating a payment interface as a complete accounting record.

Write a refund procedure before offering checkout. It should identify who can approve a refund, what information is used to match it to the original sale, how the customer is informed, and how the decision and outcome are recorded. Check the selected service’s current documentation for the refund operations it supports. For example, Coinbase’s Payment Acceptance API documents payment authorization, capture, charge, void, refunds, webhook configuration, event queries, and delivery monitoring; that is a provider-specific API description, not evidence that every in-store terminal or service supports the same refund flow. Product access, supported assets, networks, and geography can change and require separate verification. ([source](<https://docs.cdp.coinbase.com/api-reference/payment-acceptance/overview>))

A refund request and a refund capability are different things. Staff should not tell a customer that funds have been returned until the store’s documented process confirms the action and its result. If a system is unavailable or the status is ambiguous, assign the case for follow-up and preserve the original sale record rather than replacing it with an assumption.

## Review local requirements and operational risks

Identify the jurisdictions relevant to the business, customers, payment service, and transaction handling. Seek qualified local guidance on applicable regulatory, tax, recordkeeping, consumer, and compliance questions. No jurisdiction-specific conclusion about whether a business may accept crypto or what duties apply can be drawn from general Bitcoin guidance; obligations depend on jurisdiction and circumstances.

Verify implementation claims directly against authoritative, current documentation before launch. Check supported assets and networks, fees, availability, status meanings, custody arrangements, access controls, outage handling, refund procedures, and stated recovery limitations. These are implementation-specific checks, not universal properties of crypto checkout. If a vendor’s documentation does not explain a step the store needs, treat that as an unresolved readiness question rather than filling the gap with an assumption.

A controlled internal pilot can help determine whether staff can follow the procedure and whether the store’s records connect each request to the correct sale. Define who may participate, what conditions pause the pilot, who reviews exceptions, and what evidence is required before the business decides to continue. Keep the exercise focused on operational readiness; it does not establish legal or tax suitability, guarantee recovery, or prove a system’s security.

### Readiness checklist

- A written checkout procedure covers request creation, customer instructions, status checks, release of goods, and escalation.
- Every request is associated with a distinct sale reference and checked against the intended asset, network, and recipient instructions.
- The store has documented which system status controls its release decision and who is authorized to interpret it.
- Staff have defined actions for delays, amount mismatches, wrong-network concerns, duplicate-payment reports, and outages.
- Access permissions, supervisor approvals, and refund responsibilities are assigned.
- Records connect each sale with its request, reported status, staff actions, and exception or refund decisions.
- Current service documentation and qualified local guidance have been reviewed before launch.
- A pilot has clear stop conditions and does not treat a rehearsal as proof of live performance or recovery.

## Sources and references

- [Payment Acceptance API](https://docs.cdp.coinbase.com/api-reference/payment-acceptance/overview) — Coinbase Developer Platform; retrieved 2026-10-19.
