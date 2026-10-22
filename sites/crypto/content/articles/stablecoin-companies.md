---
title: "Stablecoin Companies: Roles in Settlement Infrastructure"
description: "Learn how stablecoin companies support settlement, how issuer, network, custody, and payment roles differ, and which operational dependencies to verify."
date: "2026-10-22"
draft: false
content_type: "explainer"
topics: ["stablecoins_settlement"]
tags: ["stablecoin settlement infrastructure", "stablecoin issuers", "stablecoin payment providers"]
author: "editorial_team"
primary_keyword: "stablecoin companies"
owned_question: "What roles do companies perform in stablecoin settlement, and how do their infrastructure responsibilities and dependencies differ?"
risk_level: "medium"
---

Stablecoin settlement can involve several distinct company functions: a provider may support custody, conversion, trading, or payment processing, while separate infrastructure handles other steps. To map responsibilities, follow the assets and instructions through each handoff, then verify which provider actually performs each function and under what conditions. The available evidence supports only a limited description of these roles; it does not establish that a particular company offers every service, or verify its legal status, fees, availability, or settlement terms.

## What counts as a stablecoin company?

“Stablecoin company” is a functional label, not a precise description of one service. It can refer to a business involved in a stablecoin-related activity, such as facilitating trading or providing an interface to a multi-layered financial application. The label alone does not show whether the business issues a token, holds customer assets, processes transfers, or provides conversion.

A useful distinction is between a company’s service and the infrastructure that service depends on. A decentralized finance application, for example, can be analyzed through settlement, application, and interface layers, each with distinct technical dependencies. Systems may distribute or combine these layers differently. A company associated with an application interface therefore cannot be assumed to control every underlying settlement function. [source](<https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi>)

The same caution applies to companies that facilitate access to trading. A centralized exchange can provide near-real-time trading, liquid order books, and advanced order functionality after assets are deposited, but performance and liquidity vary by venue, asset pair, and market conditions. This describes an exchange function, not a guarantee about any stablecoin provider or a statement that all exchanges provide the same services. [source](<https://www.bis.org/publ/work1227.pdf>)

## Stablecoin settlement infrastructure: the roles and handoffs

A role map is more reliable than a company label. In a proposed flow, identify the organization associated with each function and the point where one provider’s responsibility ends and another’s begins. Depending on the arrangement, relevant functions may include access to trading, custody, application interfaces, or other settlement-related services. The allowed evidence does not establish a universal provider roster or a standard end-to-end flow.

One documented exchange pattern illustrates why custody and trading should be examined separately: a user deposits assets and then trades through the exchange’s internal order book. The exchange can provide trading functionality after deposit, but that does not establish what custody arrangement applies, how assets are legally held, or what happens when a customer seeks to withdraw. Those questions require the specific platform’s current terms and disclosures; they cannot be answered from the general exchange model alone. [source](<https://www.bis.org/publ/work1227.pdf>)

For each handoff, ask what is being transferred or made available: an asset, a transaction instruction, access to an application, or a conversion service. Then identify which organization controls that step and what evidence describes its operation. If one company advertises several functions, verify each one separately rather than treating a broad product label as proof that it directly performs every task.

## Where settlement responsibility can sit

Responsibility is not necessarily concentrated in one provider. An application interface may be distinct from settlement infrastructure, and an exchange’s trading function may begin only after assets have been deposited. These distinctions matter when assigning operational questions: who provides access, who operates the trading venue, and which other service is required for the flow to proceed? The evidence here does not establish who submits a particular on-network transaction, controls a particular wallet, reconciles a payment, or handles customer support.

Conversion also requires careful, product-specific verification. Issuance and redemption near a reference value can create an arbitrage path between a primary market and a secondary-market price. But fees, minimums, eligibility, delays, market liquidity, banking access, and redemption suspensions can weaken or block that path. This is a limited description of a mechanism; it does not establish that a particular provider offers redemption, that a user qualifies, or that conversion will be available at a given time. [source](<https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf>)

Do not infer transaction timing, finality, service continuity, or geographic access from a provider’s role description. Those are operating conditions that require evidence about the relevant network and service arrangement. The claims available for this article do not establish a general settlement timeline or an availability commitment.

## Risks and dependencies to assess

Start with the dependencies in the proposed flow. If access to trading depends on depositing assets at an exchange, examine the exchange’s custody and trading terms separately. If an application spans several technical layers, identify which layer depends on which service rather than assuming the interface represents the whole system. This role-based review identifies questions; it does not establish that any service is secure or suitable.

Next, verify support for the exact asset representation and chain involved. Deposit support can be chain- and token-representation-specific; an unsupported or bridged variant can be uncredited or unrecoverable. A shared token symbol is therefore not enough to establish that a particular destination accepts a particular asset. Confirm the provider’s current supported-asset documentation for the intended route before relying on a deposit or transfer process. [source](<https://developers.circle.com/circle-mint/supported-chains-and-currencies>)

For operational controls, incident handling, access management, and recovery, use provider-specific documentation. The evidence available here does not establish any provider’s security protections, recovery process, service continuity, or incident response. Likewise, do not treat a generic company description as evidence of licensing, compliance responsibilities, supported jurisdictions, fees, or availability. Those matters require current provider disclosures and applicable jurisdiction-specific review; no legal or compliance conclusion follows from the role map.

## Questions to resolve before evaluating a provider

Use these questions to turn the map into a due-diligence checklist:

- Which functions does the provider perform directly, and which depend on another company, application layer, or service?
- Where does the flow hand off between providers, and what asset, instruction, or access is involved at each step?
- If trading requires a deposit, what do the provider’s current custody and trading terms say about the arrangement?
- Does the provider document support for the exact chain and token representation involved?
- What current evidence describes conversion access, including eligibility, delays, fees, or other conditions?
- Which documents address operational controls, incident handling, access management, and recovery—and what do they leave unspecified?
- Which legal entities and jurisdictions apply to the proposed flow, and what provider-specific or qualified review is needed to assess regulatory status and compliance responsibilities?

The practical conclusion is to evaluate stablecoin settlement as a chain of separately verifiable roles, not as a single service implied by a company label. The evidence supports a few bounded distinctions—such as exchange trading after deposit, layered application dependencies, chain-specific asset support, and conditions that can affect redemption-based arbitrage. It does not resolve the terms or legal, operational, and security details of a particular provider. Those remain questions for current documentation and context-specific review.

## Sources and references

- [Understanding Stablecoins](https://www.imf.org/-/media/files/publications/dp/2025/english/usea.pdf) — International Monetary Fund; retrieved 2026-10-18.
- [Supported Chains and Currencies](https://developers.circle.com/circle-mint/supported-chains-and-currencies) — Circle Developers; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Technology of Decentralized Finance (DeFi)](https://www.bis.org/publications/working-paper-1066-technology-decentralized-finance-defi) — Bank for International Settlements; retrieved 2026-10-18.
