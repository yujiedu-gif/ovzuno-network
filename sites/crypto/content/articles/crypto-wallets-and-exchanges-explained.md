---
title: "Crypto Wallets and Exchanges Explained: How It Works"
description: "Understand Crypto Wallets and Exchanges Explained, including its architecture, operating flow, participants, technical dependencies, limitations, and practical veri."
date: "2026-10-20"
draft: false
content_type: "explainer"
topics: ["wallets_custody"]
tags: ["crypto wallet exchanges"]
author: "editorial_team"
primary_keyword: "crypto wallets and exchanges explained"
owned_question: "What are crypto wallets and exchanges, and how do their roles differ?"
risk_level: "medium"
---

# Crypto Wallets and Exchanges Explained: How It Works

Crypto wallets and exchanges have related but distinct roles in a digital-asset system. A wallet concerns access to assets and, in key-based arrangements, control of private keys. An exchange provides a venue or service for trading. Some exchanges also provide custody, so a single service may combine both roles. The important question is not just which interface a customer sees, but who manages access to assets and where trading takes place.

The details depend on the provider, product, and jurisdiction. General descriptions do not establish who controls keys, what rights a customer has, or how assets would be treated if a provider failed. This explainer distinguishes the documented high-level models from implementation-specific questions that teams must verify.

## What Crypto Wallets and Exchanges Explained means

A crypto wallet is an arrangement for managing access to crypto assets. In a key-based model, private keys are central to that access. A third-party custodian can manage access to private keys on behalf of customers; crypto exchanges are among the possible third-party custodians described in the U.S. Securities and Exchange Commission staff’s investor bulletin. This describes a possible custody model, not a rule that every exchange holds every customer’s keys in the same way. The bulletin is presented in a United States educational context.

An exchange is a service or venue for trading assets. In the high-level centralized-exchange model described by the Bank for International Settlements (BIS), users typically transfer funds—and custody of them—to the exchange before trading through its internal order book. A related BIS description says customers typically transfer assets into exchange custody before using the internal trading system. These are common-model descriptions, not specifications for every venue. Some venues and products use different custody, brokerage, or settlement arrangements.

The role distinction is useful, but a provider can offer both. A wallet concerns access and control, while an exchange concerns trading. Seeing a wallet interface does not by itself establish who controls the keys, whether assets are in a customer-controlled wallet, or whether a provider holds them in custody.

## Core components of Crypto Wallets and Exchanges Explained

A system that combines wallet and exchange services can include several components and responsibilities:

- **Customer or institution:** The party initiating actions and selecting a service or interface.
- **Wallet and key-control arrangement:** The mechanism through which access to assets is managed. A customer may control access, or a third party may manage private-key access on the customer’s behalf. The specific arrangement must be established from product evidence.
- **Trading interface and system:** The tools through which a customer interacts with a venue. In the centralized model described by BIS, trading occurs through the venue’s internal order book. The interface and the custody arrangement are separate questions, even when presented together.
- **Custody provider or function:** A third party may manage access to private keys for customers. An exchange can be among the providers performing this role, but the general category does not determine the terms of a specific service.
- **Operator’s other business functions:** BIS notes that a centralized crypto exchange operator may combine third-party trading, proprietary trading, margin lending, token issuance, and custody. Not every exchange performs every function; combining roles can create operational dependencies and conflicts.
- **Product documentation and records:** These are needed to establish how a particular service handles custody and trading. The accepted claims do not specify one universal implementation, so teams should not treat a general model as a product specification.

Wallet labels can also be provider-specific. Coinbase Developer Platform documentation distinguishes user wallets owned by end users from API-key wallets owned and controlled by a developer’s server. That terminology describes the documented models for that provider; it should not be generalized into a legal conclusion about custody. For technical analysis, translate labels into operational questions: who owns or controls the wallet under the provider’s definition, who can authorize actions, and what arrangement applies to the customer’s assets?

## How Crypto Wallets and Exchanges Explained works

A typical centralized-exchange arrangement can be traced in stages. This is a high-level model, not a universal transaction sequence.

1. **Establish the account and wallet arrangement.** A customer uses a wallet or exchange account. The label alone does not reveal who controls private-key access or whether a third party manages it.
2. **Determine whether assets enter exchange custody.** In the typical centralized model, the customer transfers funds or assets into the exchange’s custody before trading on its internal system. Some venues or products use different custody, brokerage, or settlement arrangements, so this step must be checked for the specific service.
3. **Use the trading venue.** The customer interacts with the exchange’s trading service. In the described centralized model, the venue uses an internal order book. The fact that trading occurs on a venue does not, on its own, answer who controls the assets involved.
4. **Account for the custody relationship.** If the exchange holds assets or manages access to keys, the customer’s arrangement depends on the provider’s custody and operations as well as its trading service. The high-level model does not establish particular customer rights or protections.
5. **Verify subsequent handling from product evidence.** The accepted claims do not define a universal withdrawal, settlement, or recovery process. Those details require documentation for the relevant venue and product.

This sequence helps separate two events that can appear as one customer experience: using a wallet-related interface and trading through an exchange. The interface may combine functions, but access control, custody, and execution remain distinct questions. The exact relationship is implementation-dependent.

## Trust and control boundaries

A wallet, an exchange, and an underlying protocol should not be treated as interchangeable sources of control or assurance. The accepted claims support a narrower distinction: wallet arrangements concern access to assets, while a centralized exchange may combine trading and custody. If a third party manages private-key access for a customer, the customer depends on that custodian’s arrangements. If an operator combines custody with trading or other services, the functions can create operational dependencies and conflicts.

The SEC staff investor bulletin notes that custody structure, customer rights, segregation, insurance, regulation, and insolvency treatment vary by provider and jurisdiction. A general description of an exchange therefore does not establish any of those features for a specific customer or product. Teams should separate documented system behavior from assumptions about legal rights or protections, and seek current, relevant evidence for the particular arrangement.

A practical control-boundary map can record four separate answers: who manages key access, who can authorize an asset movement, which system handles trading, and which entity provides custody. It can then show whether one operator performs several functions. These questions help make dependencies visible without assuming that a product label settles them.

## Limitations and failure modes

The high-level models do not guarantee a particular custody design, customer right, or operational outcome. A venue may use an arrangement different from the typical centralized-exchange model, and provider-specific wallet terms may not settle the legal characterization of custody. If a team treats a general description as a precise product specification, it may map the wrong control boundary.

Combining business functions is another consideration. BIS identifies functions a centralized exchange operator may combine, while noting that not every operator performs all of them. The possibility of dependencies or conflicts is a reason to examine how roles are organized; it does not establish that a particular provider has a specific conflict or that a particular harm will occur.

The accepted claims also do not supply a universal account of deposits, withdrawals, settlement, recovery, security controls, or failure response. They do not establish provider-specific availability, fees, or regulatory status. A review should record these as unresolved unless the relevant product and jurisdiction evidence supports an answer. Missing evidence is not, by itself, proof of either a favorable or unfavorable outcome.

## What teams should verify

Technical, operational, and institutional teams can use the following checklist to examine a specific wallet or exchange arrangement:

1. **Name the exact product and role.** Determine whether the service is acting as a wallet, exchange, custodian, or combination. Do not infer the answer from a general label.
2. **Map key access and authorization.** Establish who manages access to private keys and who can authorize relevant actions. If the provider defines different wallet models, preserve the scope of those definitions and do not treat them as a general legal custody conclusion.
3. **Trace the asset and custody flow.** Confirm whether assets must enter exchange custody before trading or whether the product uses another custody, brokerage, or settlement arrangement. Verify this for the specific venue and product.
4. **Separate trading from custody.** Identify which system handles trading and which party manages custody or key access. A shared interface does not prove that the underlying responsibilities are the same.
5. **Identify combined functions.** Check whether the operator also performs custody, proprietary trading, margin lending, or token issuance. Do not assume that one function implies another; assess any resulting dependencies or conflicts from evidence about the actual arrangement.
6. **Review rights and protections independently.** Seek current, provider- and jurisdiction-specific evidence concerning custody structure, customer rights, segregation, insurance, regulation, and insolvency treatment. These vary and cannot be inferred from a generic description.
7. **Record unresolved operational questions.** Mark withdrawal, settlement, recovery, and failure-response behavior as unknown until supported by appropriate product documentation or other evidence.

The central distinction is that wallets concern access and control, while exchanges provide trading services; an exchange may also provide custody. To understand a real system, trace who manages access to assets, where trading occurs, and which provider performs each role. Then verify those answers for the specific product and jurisdiction rather than relying on terminology alone.

## Sources and references

- [Crypto Asset Custody Basics for Retail Investors](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/crypto-asset-custody-basics-retail-investors-investor-bulletin-0) — U.S. Securities and Exchange Commission Office of Investor Education and Assistance; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Anatomy of Decentralised Exchanges](https://www.bis.org/publ/work1227.pdf) — Bank for International Settlements; retrieved 2026-10-18.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Create and Manage Wallets](https://docs.cdp.coinbase.com/server-wallets/v2/using-the-wallet-api/managing-accounts) — Coinbase Developer Platform; retrieved 2026-10-19.
