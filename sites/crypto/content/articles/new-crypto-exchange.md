---
title: "New crypto exchange: core infrastructure and launch considerations"
description: "A practical overview of new crypto exchange infrastructure, operating controls, and jurisdiction-dependent checks for teams assessing a potential launch."
date: "2026-10-22"
draft: false
noindex: true
sitemap: {disable: true}
content_type: "explainer"
topics: ["exchange_market_infrastructure"]
tags: ["crypto exchange infrastructure", "exchange architecture", "exchange operations"]
author: "editorial_team"
primary_keyword: "new crypto exchange"
owned_question: "What core systems, operational controls, and jurisdiction-specific considerations are involved in launching a new crypto exchange?"
risk_level: "high"
---

Launching a new crypto exchange involves connecting trading and customer-access systems with custody, settlement, data, and external services, then assigning accountable teams to operate them. The architecture is only one part of the launch: provider arrangements, operating procedures, security and recovery evidence, and jurisdiction-specific requirements must be checked for the proposed business model. The available evidence supports a high-level planning framework, not detailed technical specifications or a conclusion that a particular exchange can operate in a particular market.

## What a new crypto exchange must coordinate

Begin with a map of the functions the planned service will perform and the relationships among them. A crypto exchange environment can be mapped as participants and access interfaces connected to trading systems, alongside custody, settlement, data, and external-service relationships. This is a conceptual map, not a universal technical design; individual arrangements vary. [source](<https://www.iosco.org/news/pdf/IOSCONEWS712.pdf>)

Distinguish the responsibilities on that map. Exchange-related functions may be divided among different firms and services, or combined across them. [source](<https://www.bis.org/publications/fsi-summary-financial-stability-implications-multifunction-cryptoasset-intermediaries-executive-summary>) Some centralized exchange operators may combine third-party trading, proprietary trading, margin lending, token issuance, and custody. That describes possible combinations, not a package that every operator provides. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

For each intended service, record whether the exchange operator plans to provide it directly, rely on a separate firm, or leave it outside the initial scope. Then identify the point where responsibilities meet. For example, a trading function and a custody function may sit within one organization or across distinct providers; the available evidence does not establish which arrangement is appropriate or permitted for a particular launch.

Keep the distinction between a centralized venue and other exchange models at the level needed for scoping: different arrangements can allocate trading, custody, and related functions differently. This article does not assess exchange models, recommend a provider, or explain trading mechanics. The planning task is to describe the proposed arrangement precisely enough to examine its technical and operational dependencies.

## Core exchange architecture and system boundaries

At a high level, the architecture plan should show how participants reach the trading system and how that system relates to custody, settlement, data, and external services. The evidence supports these broad relationships, but not a specific design for customer accounts, identity checks, order entry, matching, execution, or market-data distribution. Treat those as requirements to define and validate for the intended product rather than as a prescribed stack.

Make asset and settlement boundaries explicit. In general financial-market-infrastructure concepts, settlement systems and central securities depositories are distinct roles, and related guidance addresses linked settlement obligations and custody risk. This is a conceptual distinction; it does not classify a particular crypto exchange or establish that a specific framework applies to it. [source](<https://www.bis.org/committees/cpmi/pfmi/overview>)

A useful architecture record names the responsible entity for each function, the assets or information it handles, its dependencies, and the handoffs to other functions. It should also identify what documentation would verify how the arrangement actually works. Separate platform or protocol behavior from the responsibilities of an application, wallet, provider, custodian, settlement service, and exchange operator. The presence of a technical component alone does not establish who operates it or who is accountable for its performance.

The evidence available here does not verify particular account or identity systems, internal-ledger design, reconciliation processes, access controls, audit logging, monitoring, deployment practices, or incident-response capabilities. These are important topics for a technical design review, but no implementation or effectiveness claim should be made without current, relevant documentation. Record them as design and evidence questions, not assumed features.

## Operational dependencies before launch

Assign an owner to every operating function and dependency. A crypto-asset venue or service-provider environment may involve trading and related activities such as custody, settlement, market surveillance, or other intermediation; do not assume that a particular venue or provider performs each one. [source](<https://www.bis.org/publications/aer-2022/future-monetary-system>)

For each function, specify who handles day-to-day operations, who is authorized to make changes, where an escalation goes, and which other functions depend on it. This map can expose handoffs between trading, custody, settlement, and external services without assuming that separate parties share procedures or responsibilities. If functions are combined, document the combined scope rather than treating the organization as one undifferentiated system.

Require current written procedures for the operating tasks on which the launch depends. Teams should identify how the proposed arrangement will address deployments, service outages, customer complaints, reconciliation, and incident escalation, then request and review evidence for the relevant procedures. The evidence in scope does not confirm that any particular exchange or provider has these processes in place, or that they have been tested.

External dependencies also need explicit owners and verification. Banking or payment access, market-data sources, custody services, and infrastructure providers may be relevant to a proposed design, but this evidence does not establish availability for a particular business, customer group, asset, or location. Verify those assumptions against current provider documentation and contractual terms instead of treating a general service description as a commitment.

## Jurisdiction, licensing, and compliance checks

Define the proposed operating model and relevant locations before assessing legal or compliance questions. The evidence available for this article does not establish licensing, registration, customer-verification, sanctions, financial-promotion, customer-eligibility, or tax requirements for any jurisdiction. It therefore cannot support a conclusion that a particular exchange may launch, serve a defined customer group, or offer a specified activity.

Obtain current, authoritative information and qualified legal review for each intended location and the actual functions involved. The review should be tied to the proposed responsibilities, entities, services, and customer scope; a general description of exchange infrastructure cannot answer those jurisdiction-dependent questions. Do not assert that a permission, exemption, or market is available without current, relevant evidence. A planning checklist is not a determination of compliance.

Keep a jurisdiction-specific record of open questions, the evidence required to resolve each one, and the person responsible for obtaining confirmation. Revisit the record if the operating model, provider relationships, customer scope, or service locations change. That process helps preserve the limits of any conclusion: evidence about one entity, service, or location should not be treated as proof about another.

## Security, recovery, and resilience evidence

The allowed evidence does not establish that any specific exchange architecture, custody arrangement, security assessment, or recovery process is secure or resilient. For each proposed service, request evidence tied to the system and the entity responsible for it. Questions about threat modeling, key management, privileged access, independent assessments, vulnerability handling, backups, recovery objectives, restoration procedures, disaster-recovery testing, insurance, and customer-asset reconciliation require specific documentation; none should be treated as a confirmed control here.

Keep custody, settlement, and recovery as separate review topics. Financial-market-infrastructure guidance distinguishes settlement roles and addresses custody-related risk, but that general distinction does not show that a specific crypto arrangement meets a standard or that its recovery processes are adequate. [source](<https://www.bis.org/committees/cpmi/pfmi/overview>)

For every claimed safeguard, record what it covers, which organization operates it, and what current evidence demonstrates its scope. Ask whether the evidence relates to the actual service under consideration rather than a different product or entity. If documentation is missing, incomplete, or not applicable to the proposed arrangement, record that limitation. A policy, assessment, or stated recovery capability is not, by itself, a guarantee of security or successful recovery.

## Validate costs, availability, and launch assumptions

Before relying on an external service, check current documentation and contract terms for availability, geographic restrictions, fees, limits, support terms, and operational commitments. These details are not established by the high-level architecture evidence. Confirm the relevant service and scope directly; do not transfer an assurance about one provider, location, or product to another.

Apply the same discipline to legal status, customer eligibility, market access, yields, and tax treatment. The evidence here does not support general conclusions on these subjects. Treat any proposed statement as an open, product- and jurisdiction-dependent question until it is supported by current documentation and, where appropriate, qualified review. Avoid presenting an estimate or assumption as an established cost, permission, return, or operating condition.

Maintain a decision register that separates verified facts from unresolved assumptions. For each item, note the responsible entity, affected function, relevant location, supporting evidence, evidence date, and decision owner. Include unresolved compliance, security, recovery, provider, and operational dependencies. Update the register when documentation, contracts, or the proposed arrangement change.

The result is a scoped launch plan, not a certification of readiness. The central planning task is to connect system boundaries to accountable operators and then verify operational and jurisdictional assumptions with current evidence specific to the intended exchange. Where the evidence does not answer a question, preserve it as an open decision rather than filling the gap with a general claim.

## Sources and references

- [IOSCO Finalizes its Policy Recommendations for Crypto and Digital Asset Markets](https://www.iosco.org/news/pdf/IOSCONEWS712.pdf) — International Organization of Securities Commissions (IOSCO); retrieved 2026-10-21.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [The financial stability implications of multifunction cryptoasset intermediaries - Executive Summary](https://www.bis.org/publications/fsi-summary-financial-stability-implications-multifunction-cryptoasset-intermediaries-executive-summary) — Bank for International Settlements, Financial Stability Institute; retrieved 2026-10-21.
- [The Future Monetary System](https://www.bis.org/publications/aer-2022/future-monetary-system) — Bank for International Settlements; retrieved 2026-10-18.
- [Principles for Financial Market Infrastructures](https://www.bis.org/committees/cpmi/pfmi/overview) — Bank for International Settlements, Committee on Payments and Market Infrastructures (CPMI), and IOSCO; retrieved 2026-10-21.
