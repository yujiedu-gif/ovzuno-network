---
title: "Crypto Market Making Software: Core Components and Workflows"
description: "Explore crypto market making software components, from market data and quote generation to execution, inventory tracking, and operational risk controls."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["market making engine", "inventory management", "order execution", "risk controls"]
author: "editorial_team"
primary_keyword: "crypto market making software"
owned_question: "What functions does crypto market making software perform, and how do its data, quoting, execution, inventory, and risk-control components fit together?"
risk_level: "medium"
---

Crypto market making software coordinates parts of an operation that proposes and manages orders: it can process configured data, generate quotes, route orders, track inventory, and apply operator-defined controls. These functions do not guarantee execution, liquidity, or protection from losses. Implementations and venue integrations vary, so evaluate documented capabilities and operating boundaries rather than assuming one standard design.

## What crypto market making software is responsible for

Market making is the activity; market making software is a tool that can automate or organize selected tasks supporting that activity. Depending on its design, a system may collect inputs, calculate proposed orders, send instructions through an integration, and maintain an operational view of orders and positions. The operator defines relevant rules and oversight, while each venue governs what its interface accepts and how it processes instructions.

Market making software may be built for one venue or configured to coordinate activity across venues. That distinction affects what a reviewer should map: data sources, accounts, order workflows, and the boundaries between integrations. A shared screen or central control layer does not by itself show that the underlying venue functions or account records are unified.

The term also should not be mistaken for a single trading model. For example, an automated market maker (AMM) is a specific decentralized-exchange model in which a liquidity provider contributes assets to a pool and may receive a share of trading fees while bearing inventory and adverse-selection risk. This is one example of liquidity provision, not a description of every market-making operation or a requirement for market making software. [source](<https://www.bis.org/publ/work1227.pdf>)

This explainer covers system functions and evaluation questions, not vendor selection, trading recommendations, or expected returns. A useful review separates features documented by a provider from settings an operator must choose and actions a venue ultimately processes.

## From market data to a proposed quote

A quote is a proposed order with a price and size. Software may use market observations, account balances, and instrument parameters as inputs to quote logic. The specific sources, fields, refresh behavior, and supported instruments depend on the implementation and its integrations; verify those details in current documentation rather than treating them as standard across products.

Quote logic applies rules selected or configured by an operator. At a high level, those rules may specify price distance, order size, and when to update or withdraw a proposed order. The software’s output is an instruction or recommendation within that configured workflow. It does not establish that the venue will accept the instruction, that an order will execute, or that an execution will produce a favorable result.

Data handling deserves explicit review. Ask how the system identifies the time and source of inputs used in a quote, and what it does when information is missing, delayed, or inconsistent. A stale input can make a proposed quote diverge from the current operating assumptions, but this article does not claim that every implementation detects or handles staleness in the same way. Confirm whether the documented response is to pause, continue, alert, or require an operator decision.

Also establish how instrument parameters and venue-specific settings enter the calculation. A displayed quote may depend on configuration that is not visible in a summary screen. Review which values are operator-controlled, which are supplied by an integration, and how changes are logged or reviewed. Do not infer that a data feed or interface supplies every field needed by a strategy simply because it connects to a venue.

## Order execution, inventory, and risk controls

Once quote logic proposes an order, order management handles the instruction lifecycle. Common functions to assess include submitting an order, requesting an amendment or cancellation, processing venue responses, and comparing the system’s internal status with the status reported by the venue. These are review categories, not a claim that every integration supports every action or order type.

The distinction between a request and a completed change matters operationally. A system can send an instruction, but its internal view should be reconciled with the venue’s response before a reviewer assumes the intended state has been reached. Ask how rejected instructions, delayed responses, and uncertain outcomes are represented, and what the operator is expected to do when the local record and venue record differ.

Inventory tracking provides a view of assets and exposures that may be relevant to quoting. A system may use configured limits to reduce, block, or otherwise constrain proposed orders when a position reaches a threshold. For evaluation, establish which accounts, assets, and venues are included; how balances enter the system; and what behavior follows a threshold. The labels “inventory” or “risk control” do not prove that all exposures are measured or that a limit prevents loss.

Risk controls can be configured around order size, exposure, monitoring, alerts, and stopping automated activity. The implementation review should identify who can set or override each control, what event activates it, and whether its activation is recorded. A stop procedure can define how an operator interrupts software activity, but it does not by itself establish how quickly an external venue processes an instruction or what happens to an already accepted order.

Exposure remains an important boundary. In the specific AMM liquidity-provision example, a provider contributes assets to a pool and can bear inventory and adverse-selection risk; the result depends on the pool and position rather than on the software label. [source](<https://www.bis.org/publ/work1227.pdf>) For any design, ask which risks the system is intended to monitor and which remain outside its measurements. Avoid interpreting a configured threshold as a guarantee against market, venue, data, or operational problems.

## How the system components connect

A conceptual data and control flow can be organized as follows:

1. **Ingest:** Receive market and account inputs from configured sources.
2. **Calculate:** Apply operator-defined quote and update rules to produce proposed orders.
3. **Check:** Compare proposed activity with configured limits and operating conditions.
4. **Route:** Send applicable instructions through a venue integration.
5. **Observe:** Process venue responses and update the system’s order and inventory view.
6. **Reconcile:** Compare internal state with venue or account records and surface discrepancies for review.

This sequence is a conceptual map, not a universal software architecture. An implementation may combine or separate components, and integrations may provide different data or actions. For example, a data interface may expose indexed records such as balances, transactions, token transfers, logs, or address metadata across supported EVM chains; that documented example concerns an API’s indexed endpoint families and does not establish the capabilities of a market-making product or a venue integration. [source](<https://docs.etherscan.io/introduction>)

The flow also has feedback paths. A venue response or a refreshed account balance may alter the system’s recorded state and affect subsequent quote calculations. Review how the implementation associates those observations with the relevant account, instrument, and order, and whether it indicates uncertainty or missing information. The exact implementation is product-specific; the important evaluation step is to trace a proposed quote through the response and resulting internal record.

Failure scenarios should be examined alongside the normal sequence. Ask what happens after a disconnection, a delayed update, a rejected order, or a mismatch between internal and venue records. Determine whether the system pauses, retries, alerts, or requires operator action, and verify those behaviors in documentation or a controlled review appropriate to the implementation. Do not infer recovery capability from a monitoring screen, a venue connection, or an “automated” label.

## Questions to assess an implementation

A neutral requirements review can use these questions to distinguish verified capabilities from assumptions:

- **Coverage:** Which venues, instruments, data sources, and order operations are explicitly documented? Are capabilities different by account, instrument, or integration?
- **Quote configuration:** Which price, size, and update parameters can an operator set? How are input age, missing data, and configuration changes shown or recorded?
- **Order lifecycle:** How are submissions, amendments, cancellations, venue responses, rejections, and uncertain outcomes represented? What reconciliation process is documented?
- **Inventory boundaries:** Which accounts and assets are included in the position view? How are balances updated, and what does the system do when a configured threshold is reached?
- **Controls and oversight:** Which limits, alerts, and stop procedures are documented? Who can change or override them, and what records are available for review?
- **Integration requirements:** What interfaces, account connections, credentials, permissions, and internal systems are required? Confirm supported functions rather than inferring them from a general API connection.
- **Security and operations:** Review documented access controls, logging, testing, monitoring, and recovery procedures. Treat security and recovery statements as claims requiring current, attributable evidence, not as guarantees.
- **Terms and representations:** Verify fees, service availability, and any regulatory or compliance representations in current, specific documentation and applicable terms. Do not assume these are uniform across providers, venues, or jurisdictions; this article does not determine legal status or obligations.

The resulting assessment should state what the software automates, what the venue controls, what the operator must monitor, and what remains unverified. That boundary makes the system easier to evaluate without conflating quote generation with execution, or configured controls with elimination of risk.

## Sources and references

- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [Welcome to the Etherscan API](https://docs.etherscan.io/introduction) — Etherscan Documentation; retrieved 2026-10-19.
